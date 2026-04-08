---
title: "하네스 엔지니어링 4단계 — 고급 기능 및 운영"
description: Feature Flags, Blue/Green 배포, Harness Git Experience, 운영 시 주의사항을 다룹니다.
date: 2026-04-08
order: 4
category: Harness
tags: [harness, feature-flags, blue-green, git-experience, ops]
---

## Feature Flags

Feature Flags(FF)는 코드 배포 없이 기능을 켜고 끌 수 있는 메커니즘입니다.

### SDK 연동 (Python 예시)

```python
from featureflags.client import CfClient
from featureflags.config import with_base_url
from featureflags.evaluations.auth_target import Target

client = CfClient(
    "your-sdk-key",
    with_base_url("https://config.ff.harness.io/api/1.0")
)

target = Target(identifier="user-123", name="Joon")

if client.bool_variation("new-checkout-flow", target, False):
    return new_checkout()
else:
    return legacy_checkout()
```

### 활용 패턴

| 패턴 | 설명 |
|------|------|
| **Kill Switch** | 장애 발생 시 즉시 기능 비활성화 |
| **Percentage Rollout** | 10% → 50% → 100% 점진적 활성화 |
| **User Targeting** | 특정 사용자/그룹에만 활성화 |
| **A/B Testing** | 두 버전 동시 운영 후 지표 비교 |

## Blue/Green 배포

Canary와 달리 Blue/Green은 두 개의 완전한 환경을 유지합니다.

```yaml
- step:
    name: Blue Green Deploy
    type: K8sBlueGreenDeploy
    spec:
      skipDryRun: false

- step:
    name: Blue Green Swap
    type: K8sSwapServiceSelectors

- step:
    name: Blue Green Cleanup
    type: K8sBlueGreenStageScaleDown
```

<div class="callout why">
  <div class="callout-title">Canary vs Blue/Green</div>
  Canary는 점진적 트래픽 이동으로 위험을 분산합니다. Blue/Green은 전환이 즉각적이며 롤백도 즉시 가능하지만 리소스를 2배 사용합니다. 스테이트리스 서비스엔 Canary, DB 마이그레이션이 포함된 배포엔 Blue/Green을 권장합니다.
</div>

## Harness Git Experience

파이프라인 YAML을 Git 저장소에 저장하고 코드로 관리하는 기능입니다.

```
your-repo/
  └── .harness/
        ├── pipelines/
        │     └── deploy-production.yaml
        ├── templates/
        │     └── canary-stage.yaml
        └── inputsets/
              └── prod-values.yaml
```

### Template 재사용

반복되는 Stage나 Step을 Template으로 추출해 여러 파이프라인에서 참조할 수 있습니다.

```yaml
template:
  name: canary-deploy-template
  type: Stage
  spec:
    type: Deployment
    # ... 공통 Canary 스테이지 정의
```

파이프라인에서 참조:

```yaml
- stage:
    template:
      templateRef: canary-deploy-template
      versionLabel: v1
```

## 운영 시 주의사항

### Delegate 관리

```bash
# Delegate 로그 실시간 확인
kubectl logs -f deployment/harness-delegate -n harness-delegate

# Delegate 재시작
kubectl rollout restart deployment/harness-delegate -n harness-delegate
```

- Delegate는 **최소 2개 이상** 운영해 HA를 확보합니다.
- Delegate 버전은 Harness Platform 버전보다 **최대 3 minor 버전** 이내로 유지합니다.

### 파이프라인 거버넌스

| 정책 | 설정 위치 |
|------|-----------|
| Production 배포 전 Approval 필수 | Stage > Approval Step |
| 특정 시간대 배포 차단 | OPA Policy |
| 이미지 태그 `latest` 사용 금지 | OPA Policy |

### OPA 정책 예시 (latest 태그 차단)

```rego
package pipeline_policies

deny[msg] {
  input.pipeline.stages[_].stage.spec.serviceConfig
    .serviceDefinition.spec.artifacts.primary.spec.tag == "latest"
  msg := "latest 태그는 프로덕션 배포에 사용할 수 없습니다."
}
```

## 마무리

| 단계 | 내용 |
|------|------|
| **1단계** | Harness 개요 및 핵심 개념 |
| **2단계** | Delegate 설치 및 환경 구성 |
| **3단계** | CI/CD 파이프라인 구축 |
| **4단계** | Feature Flags, Blue/Green, 운영 |

Harness는 초기 설정 비용이 있지만, 배포 신뢰성과 팀 생산성을 크게 향상시킵니다. 특히 ML 기반 자동 롤백과 Verification 기능은 야간 배포에도 안심할 수 있는 환경을 만들어 줍니다.
