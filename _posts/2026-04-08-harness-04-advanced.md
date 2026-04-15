---
title: "Harness Feature Flags와 거버넌스 — 배포와 릴리즈를 분리하는 방법"
description: Feature Flags로 코드 없이 기능을 제어하고, OPA 정책과 Approval 게이트로 배포 거버넌스를 구축해요.
date: 2026-04-08
order: 4
category: CI/CD
subcategory: Harness
tags: [harness, feature-flags, blue-green, opa, governance, git-experience]
---

## 배포와 릴리즈의 분리

전통적인 배포에서는 코드를 프로덕션에 올리는 순간 사용자에게 노출돼요. 이 두 가지를 분리하면 다음이 가능해져요.

- 기능이 완성되지 않아도 코드를 먼저 배포
- 특정 사용자 그룹에만 새 기능 노출
- 문제가 생기면 코드 배포 없이 즉시 비활성화

Harness Feature Flags는 이 패턴을 플랫폼 수준에서 지원해요.

## Feature Flags 구조

Feature Flag는 **Flag** 와 **Target** 두 개념으로 동작해요.

- **Flag**: 켜고 끌 수 있는 기능의 단위. Boolean, String, Number, JSON 타입을 지원해요.
- **Target**: Flag의 ON/OFF 대상. 사용자 ID, 이메일, 국가 등 속성으로 정의해요.
- **Segment**: Target의 그룹. 여러 Target을 묶어 규칙을 적용해요.

```
Flag: new-checkout-flow
  ├── Default Rule: OFF (모든 사용자)
  ├── Target Rule: ON (beta-testers Segment)
  └── Percentage Rollout: 10% → 50% → 100%
```

## SDK 연동

### Python SDK

```python
from featureflags.client import CfClient
from featureflags.config import with_base_url, with_events_url
from featureflags.evaluations.auth_target import Target

# 클라이언트 초기화 (앱 시작 시 1회)
client = CfClient(
    sdk_key="your-sdk-key",
    *with_base_url("https://config.ff.harness.io/api/1.0"),
    *with_events_url("https://events.ff.harness.io/api/1.0"),
)
client.wait_for_initialization()

# 요청마다 Target 생성
def get_target(user_id: str, email: str) -> Target:
    return Target(
        identifier=user_id,
        name=email,
        attributes={
            "email": email,
            "plan": "enterprise",
            "country": "KR",
        }
    )

# Flag 평가
def checkout(user_id: str, email: str):
    target = get_target(user_id, email)

    if client.bool_variation("new-checkout-flow", target, default=False):
        return new_checkout_handler()
    return legacy_checkout_handler()
```

### FastAPI 미들웨어 패턴

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request

ff_client: CfClient | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global ff_client
    ff_client = CfClient(sdk_key=settings.FF_SDK_KEY)
    ff_client.wait_for_initialization()
    yield
    ff_client.close()

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def feature_flag_middleware(request: Request, call_next):
    user_id = request.headers.get("X-User-Id", "anonymous")
    target = Target(identifier=user_id, name=user_id)
    request.state.ff_client = ff_client
    request.state.ff_target = target
    return await call_next(request)
```

## Feature Flag 활용 패턴

### Kill Switch

장애 발생 시 코드 배포 없이 즉시 기능을 비활성화해요.

```python
# 외부 API 호출 기능에 Kill Switch 적용
async def call_external_api(data: dict) -> dict:
    target = Target(identifier="system", name="system")

    if not ff_client.bool_variation("external-api-enabled", target, default=True):
        # FF가 OFF면 캐시 또는 폴백 응답 반환
        return get_cached_response(data)

    return await actual_api_call(data)
```

### Percentage Rollout

Harness UI에서 설정하고, SDK 코드 변경 없이 비율을 조절해요.

| 단계 | 설정 | 기간 |
|------|------|------|
| 초기 | 5% (내부 팀) | 1일 |
| 1차 확장 | 20% | 2일 |
| 2차 확장 | 50% | 3일 |
| 전체 출시 | 100% | — |

### String Flag로 A/B 테스트

```python
variant = ff_client.string_variation(
    "checkout-button-text",
    target,
    default="구매하기"
)
# "구매하기", "지금 주문", "바로 결제" 중 하나 반환
return render_button(text=variant)
```

## Blue/Green 배포

Canary 배포와 달리 Blue/Green은 두 개의 완전한 환경을 유지해요. 전환이 즉각적이고 롤백도 서비스 셀렉터 변경만으로 즉시 가능해요.

<div class="callout why">
  <div class="callout-title">Canary vs Blue/Green 선택 기준</div>
  Canary는 점진적 트래픽 이동으로 위험을 분산하지만 전환 시간이 길고 설정이 복잡해요. Blue/Green은 즉각적인 전환과 롤백이 가능하지만 리소스를 2배 사용해요. DB 스키마 마이그레이션이 포함된 배포나 즉각적인 롤백이 필요한 서비스에는 Blue/Green을 선택해요.
</div>

```yaml
execution:
  steps:
    - step:
        name: Blue Green Deploy
        identifier: bg_deploy
        type: K8sBlueGreenDeploy
        spec:
          skipDryRun: false
          pruningEnabled: true

    - step:
        name: Verify Green
        identifier: verify_green
        type: Verify
        timeout: 15m
        spec:
          type: BlueGreen
          monitoredService:
            type: Default
          healthSources:
            - identifier: prometheus_prod

    - step:
        name: Swap Traffic to Green
        identifier: bg_swap
        type: K8sSwapServiceSelectors

    - step:
        name: Scale Down Blue
        identifier: bg_cleanup
        type: K8sBlueGreenStageScaleDown

  rollbackSteps:
    - step:
        name: Swap Back to Blue
        type: K8sSwapServiceSelectors
```

## Harness Git Experience

파이프라인, 서비스, 환경, 템플릿을 Git 저장소에 YAML로 저장하는 기능이에요. GitOps 원칙에 따라 모든 변경이 코드 리뷰를 거쳐요.

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

반복되는 Stage를 템플릿으로 추출해 여러 파이프라인에서 공유해요.

```yaml
# .harness/templates/canary-stage-template.yaml
template:
  name: Canary Deploy Stage
  identifier: canary_deploy_stage
  type: Stage
  versionLabel: v1.2
  spec:
    type: Deployment
    spec:
      deploymentType: Kubernetes
      execution:
        steps:
          - stepGroup:
              name: Canary Phase
              steps:
                - step:
                    type: K8sCanaryDeploy
                    spec:
                      instanceSelection:
                        type: Percentage
                        spec:
                          percentage: <+input>  # 런타임 입력
                - step:
                    type: Verify
                    timeout: <+input>
                - step:
                    type: K8sCanaryDelete
          - step:
              type: K8sRollingDeploy
```

파이프라인에서 템플릿 참조:

```yaml
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
                    - step:
                        spec:
                          instanceSelection:
                            spec:
                              percentage: 20
                    - step:
                        timeout: 10m
```

## OPA 기반 거버넌스 정책

Harness는 Open Policy Agent(OPA)를 사용해 파이프라인 실행 전에 정책을 검사해요.

### latest 태그 사용 차단

```rego
package pipeline

import future.keywords.if
import future.keywords.in

deny contains msg if {
  some stage in input.pipeline.stages
  stage.stage.type == "Deployment"
  tag := stage.stage.spec.serviceConfig.serviceDefinition.spec.artifacts.primary.spec.tag
  tag == "latest"
  msg := sprintf(
    "Stage '%v': latest 태그는 프로덕션 배포에 사용할 수 없어요.",
    [stage.stage.name]
  )
}
```

### Production 배포 시 Approval Stage 필수

```rego
package pipeline

deny contains msg if {
  some stage in input.pipeline.stages
  stage.stage.type == "Deployment"
  stage.stage.spec.environment.environmentRef == "production"
  not has_approval_before(input.pipeline.stages, stage)
  msg := "Production 배포 전에 Approval Stage가 반드시 있어야 해요."
}

has_approval_before(stages, target_stage) if {
  some i, j
  stages[i].stage.type == "Approval"
  stages[j] == target_stage
  i < j
}
```

### 업무 시간 외 Production 배포 차단

```rego
package pipeline

deny contains msg if {
  some stage in input.pipeline.stages
  stage.stage.spec.environment.environmentRef == "production"
  hour := time.clock(time.now_ns())[0]
  not (hour >= 10 and hour < 18)
  msg := "Production 배포는 업무 시간(10:00~18:00 KST)에만 가능해요."
}
```

## Approval 게이트

배포 전에 사람의 승인을 받거나, Jira·ServiceNow 티켓 상태를 확인하는 Step이에요.

```yaml
- stage:
    name: Production Approval
    identifier: prod_approval
    type: Approval
    spec:
      execution:
        steps:
          - step:
              name: Engineering Lead Approval
              type: HarnessApproval
              spec:
                approvalMessage: |
                  ## 배포 승인 요청

                  - **서비스**: <+service.name>
                  - **이미지 태그**: <+artifact.tag>
                  - **환경**: Production
                  - **파이프라인 실행**: #<+pipeline.sequenceId>

                  변경사항을 확인하고 승인해 주세요.
                approvers:
                  userGroups:
                    - engineering-leads
                  minimumCount: 1
                approverInputs:
                  - name: DeploymentReason
                    defaultValue: ""
                includePipelineExecutionHistory: true
              timeout: 8h
              failureStrategies:
                - onFailure:
                    errors:
                      - ApprovalRejection
                    action:
                      type: AbortPipelineOnFailure
```

## Delegate HA 운영

프로덕션 환경의 Delegate는 단일 장애점을 없애기 위해 반드시 2개 이상 운영해요.

```bash
# Delegate 상태 모니터링
kubectl get pods -n harness-delegate -w

# Delegate 강제 재시작 (순차적으로)
kubectl rollout restart deployment/harness-delegate -n harness-delegate

# Delegate 로그에서 태스크 실패 확인
kubectl logs -n harness-delegate -l app=harness-delegate \
  --since=1h | grep -E "ERROR|FAILED|Exception"
```

### Delegate 자원 설정 (HPA)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: harness-delegate-hpa
  namespace: harness-delegate
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: harness-delegate
  minReplicas: 2
  maxReplicas: 5
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

## 정리

| 주제 | 핵심 포인트 |
|------|-------------|
| **Feature Flags** | 배포와 릴리즈를 분리. Kill Switch로 즉시 비활성화 가능 |
| **Blue/Green** | 즉각적 전환과 롤백. DB 마이그레이션 포함 배포에 적합 |
| **Git Experience** | 파이프라인을 코드로 관리. 템플릿으로 표준화 |
| **OPA 정책** | latest 태그 차단, Approval 강제, 배포 시간 제한 |
| **Delegate HA** | 최소 2개 운영, 자동 업그레이드 활성화 |

Harness는 초기 설정 비용이 크지만, 배포 자동화를 넘어 **배포 신뢰성을 플랫폼이 보장** 하는 수준까지 끌어올려요. 특히 팀이 커지고 배포 빈도가 높아질수록 OPA 정책과 Feature Flags의 가치가 더 커져요.
