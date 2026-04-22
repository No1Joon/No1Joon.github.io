---
title: "Harness Feature Flags와 거버넌스"
description: Feature Flags로 코드 없이 기능을 제어하고, OPA 정책과 Approval 게이트로 배포 거버넌스를 구축합니다.
date: 2026-04-08
order: 4
category: CI/CD
subcategory: Harness
tags: [harness, feature-flags, blue-green, opa, governance, git-experience]
---

## 배포와 릴리즈의 분리

전통적인 배포에서는 코드를 프로덕션에 올리는 순간 사용자에게 노출됩니다. 이 두 가지를 분리하면 다음이 가능해집니다

- 기능이 완성되지 않아도 코드를 먼저 배포
- 특정 사용자 그룹에만 새 기능 노출
- 문제가 생기면 코드 배포 없이 즉시 비활성화

Harness Feature Flags는 이 패턴을 플랫폼 수준에서 지원합니다

## Feature Flags 구조

Feature Flag는 **Flag** 와 **Target** 두 개념으로 동작합니다

- **Flag**: 켜고 끌 수 있는 기능의 단위. Boolean, String, Number, JSON 타입을 지원합니다
- **Target**: Flag의 ON/OFF 대상. 사용자 ID, 이메일, 국가 등 속성으로 정의합니다
- **Segment**: Target의 그룹. 여러 Target을 묶어 규칙을 적용합니다

```
Flag: new-checkout-flow
  ├── Default Rule: OFF (모든 사용자)
  ├── Target Rule: ON (beta-testers Segment)
  └── Percentage Rollout: 10% → 50% → 100%
```

## SDK 연동

SDK는 **앱 시작 시 1회 초기화** → **요청마다 Target 생성** → **Flag 평가** 세 단계만 기억하면 됩니다. Target은 사용자 ID를 식별자로 쓰고 이메일·플랜·국가 같은 속성을 붙여 Segment 규칙 매칭에 활용합니다

```python
from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target

client = CfClient(sdk_key="...")
client.wait_for_initialization()

target = Target(identifier=user_id, attributes={"plan": "enterprise", "country": "KR"})

if client.bool_variation("new-checkout-flow", target, default=False):
    return new_checkout_handler()
return legacy_checkout_handler()
```

FastAPI 같은 웹 프레임워크에서는 `lifespan` 에서 `CfClient` 를 싱글톤으로 띄우고, 미들웨어에서 요청 Target을 `request.state` 에 주입하는 패턴이 표준입니다

## Feature Flag 활용 패턴

| 패턴 | 평가 타입 | 전형 용도 |
|------|-----------|-----------|
| Kill Switch | `bool_variation` default=`True` | 장애 시 외부 API·결제 모듈 즉시 차단 |
| Percentage Rollout | UI에서 5%→20%→50%→100% | 신규 기능 점진 공개 |
| A/B 테스트 | `string_variation` | 버튼 텍스트·결제 플로우 변형 |
| 권한별 노출 | Segment 규칙 | 베타 테스터·내부 팀 우선 공개 |

Kill Switch는 SDK 관점에서 **default 값을 `True` 로 두는 게 포인트**입니다. FF 서비스에 장애가 생겨 Flag 조회가 실패해도 기능이 계속 동작하도록요. 차단이 필요할 때만 콘솔에서 OFF로 내립니다

```python
async def call_external_api(data):
    if not ff_client.bool_variation("external-api-enabled", target, default=True):
        return get_cached_response(data)
    return await actual_api_call(data)
```

## Blue/Green 배포

Canary 배포와 달리 Blue/Green은 두 개의 완전한 환경을 유지합니다. 전환이 즉각적이고 롤백도 서비스 셀렉터 변경만으로 즉시 가능합니다

<div class="callout why">
  <div class="callout-title">Canary vs Blue/Green 선택 기준</div>
  Canary는 점진적 트래픽 이동으로 위험을 분산하지만 전환 시간이 길고 설정이 복잡합니다. Blue/Green은 즉각적인 전환과 롤백이 가능하지만 리소스를 2배 사용합니다. DB 스키마 마이그레이션이 포함된 배포나 즉각적인 롤백이 필요한 서비스에는 Blue/Green을 선택합니다
</div>

순서는 **Green 배포 → Verify → Traffic Swap → Blue Scale Down**, 롤백은 `K8sSwapServiceSelectors` 하나로 Blue로 되돌립니다

```yaml
execution:
  steps:
    - step: { type: K8sBlueGreenDeploy, spec: { pruningEnabled: true } }
    - step:
        type: Verify
        timeout: 15m
        spec: { type: BlueGreen, healthSources: [ { identifier: prometheus_prod } ] }
    - step: { type: K8sSwapServiceSelectors }
    - step: { type: K8sBlueGreenStageScaleDown }
rollbackSteps:
  - step: { type: K8sSwapServiceSelectors }
```

## Harness Git Experience

파이프라인, 서비스, 환경, 템플릿을 Git 저장소에 YAML로 저장하는 기능입니다. GitOps 원칙에 따라 모든 변경이 코드 리뷰를 거칩니다

```
your-repo/
  └── .harness/
        ├── pipelines/
        │     ├── deploy-production.yaml
        │     └── deploy-staging.yaml
        ├── services/
        │     └── your-service.yaml
        ├── environments/
        │     ├── production.yaml
        │     └── staging.yaml
        ├── templates/
        │     ├── canary-stage-template.yaml
        │     └── build-step-template.yaml
        └── inputsets/
              ├── prod-inputset.yaml
              └── staging-inputset.yaml
```

### Template 재사용

반복되는 Stage·StepGroup·Step은 템플릿으로 추출하고 **`versionLabel`** 로 버전을 고정합니다. 템플릿 내부의 값 중 파이프라인마다 달라지는 부분은 `<+input>` 으로 비워두면, 파이프라인에서 `templateInputs` 로 주입합니다

```yaml
# 파이프라인 쪽
- stage:
    name: Deploy Production
    template:
      templateRef: canary_deploy_stage
      versionLabel: v1.2
      templateInputs:
        spec:
          execution:
            steps:
              - stepGroup:
                  steps:
                    - step: { spec: { instanceSelection: { spec: { percentage: 20 } } } }
                    - step: { timeout: 10m }
```

`versionLabel` 을 올리지 않고 템플릿을 수정하면 **기존 파이프라인에 즉시 영향**이 갑니다. 운영 팁은 *수정 시 새 버전 라벨을 부여하고, 파이프라인은 준비되는 대로 점진 전환* 입니다

## OPA 기반 거버넌스 정책

Harness는 파이프라인 실행 전에 OPA 정책을 평가하고, `deny` 가 하나라도 발생하면 실행을 막습니다. 입력은 파이프라인 YAML을 JSON으로 파싱한 구조 전체(`input.pipeline.*`)입니다

자주 쓰는 정책 아이디어

| 정책 | 검사 지점 |
|------|-----------|
| `latest` 태그 차단 | `stage.spec.serviceConfig...artifacts.primary.spec.tag` |
| Production 앞 Approval 강제 | `stages[*].stage.type == "Approval"` 이 `Deployment` 앞에 존재 |
| 업무 시간 외 배포 차단 | `time.clock(time.now_ns())[0]` 가 10~18 범위 밖 |
| Canary 단계 필수 | `Deployment` Stage에 `K8sCanaryDeploy` Step 존재 |

대표 예시 하나만 보면 Rego 작성 패턴이 그대로 보입니다

```rego
package pipeline
import future.keywords.if
import future.keywords.in

deny contains msg if {
  some stage in input.pipeline.stages
  stage.stage.type == "Deployment"
  tag := stage.stage.spec.serviceConfig.serviceDefinition.spec.artifacts.primary.spec.tag
  tag == "latest"
  msg := sprintf("Stage '%v': latest 태그 금지", [stage.stage.name])
}
```

## Approval 게이트

배포 전에 사람의 승인을 받거나, Jira·ServiceNow 티켓 상태를 확인하는 Step입니다

`HarnessApproval` Step은 `approvers.userGroups` 로 승인자를 지정하고, `approvalMessage` 에 Harness 표현식을 섞어 맥락을 자동으로 채웁니다. `timeout` 을 명시하지 않으면 파이프라인이 무기한 대기하니 8시간 정도로 두는 게 안전합니다

```yaml
- step:
    type: HarnessApproval
    timeout: 8h
    spec:
      approvalMessage: |
        서비스: <+service.name> / 태그: <+artifact.tag> / 실행: #<+pipeline.sequenceId>
      approvers: { userGroups: [engineering-leads], minimumCount: 1 }
      includePipelineExecutionHistory: true
    failureStrategies:
      - onFailure: { errors: [ApprovalRejection], action: { type: AbortPipelineOnFailure } }
```

## Delegate HA 운영

프로덕션 Delegate는 반드시 2개 이상. 단일 장애점을 없애는 동시에, 자동 업그레이드가 순차적으로 돌 때 파이프라인이 끊기지 않습니다

| 항목 | 권장 |
|------|------|
| 최소 Replica | 2 |
| HPA | CPU 70% 기준, min 2 / max 5 |
| 재시작 | `kubectl rollout restart deployment/harness-delegate` (순차) |
| 장애 징후 확인 | `kubectl logs -l app=harness-delegate --since=1h`에서 `ERROR/FAILED/Exception` |

## 정리

| 주제 | 핵심 포인트 |
|------|-------------|
| **Feature Flags** | 배포와 릴리즈를 분리. Kill Switch로 즉시 비활성화 가능 |
| **Blue/Green** | 즉각적 전환과 롤백. DB 마이그레이션 포함 배포에 적합 |
| **Git Experience** | 파이프라인을 코드로 관리. 템플릿으로 표준화 |
| **OPA 정책** | latest 태그 차단, Approval 강제, 배포 시간 제한 |
| **Delegate HA** | 최소 2개 운영, 자동 업그레이드 활성화 |

Harness는 초기 설정 비용이 크지만, 배포 자동화를 넘어 **배포 신뢰성을 플랫폼이 보장** 하는 수준까지 끌어올립니다. 특히 팀이 커지고 배포 빈도가 높아질수록 OPA 정책과 Feature Flags의 가치가 더 커집니다
