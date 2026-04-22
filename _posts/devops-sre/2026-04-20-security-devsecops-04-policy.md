---
title: "Secrets와 정책 자동화"
description: Vault·Sealed Secrets·OPA로 비밀 관리와 정책을 코드화하는 방법을 정리해요.
date: 2026-04-20
order: 4
category: DevOps & SRE
subcategory: Security / DevSecOps
tags: [devsecops, secrets, vault, opa, policy-as-code]
---

DevSecOps의 마지막 퍼즐은 사람이 수동으로 개입하던 보안 결정을 시스템이 대신하게 만드는 것입니다. 데이터베이스 패스워드 같은 **비밀 정보**(Secrets)를 안전하게 유통하고, 클러스터의 모든 리소스가 보안 표준을 따르는지 **정책**(Policy)으로 강제하는 방법을 정리해요.

## 비밀 정보 관리 (Secrets Management)

코드 저장소에 API 키나 패스워드를 평문으로 올리는 것은 보안 사고의 지름길입니다. 이를 방지하기 위한 세 가지 실전 패턴입니다.

| 패턴 | 도구 | 동작 방식 | 장점 |
|---|---|---|---|
| **중앙 집중형** | HashiCorp Vault | 애플리케이션이 실행 시점에 API로 직접 비밀값 조회 | 가장 안전, 동적 비밀번호 발급 가능 |
| **저장소 암호화** | Sealed Secrets | 비밀값을 공개키로 암호화하여 Git에 저장, 클러스터 내에서만 복호화 | GitOps 워크플로우에 최적 |
| **클라우드 연동** | External Secrets | AWS/GCP의 Secret Manager 값을 K8s Secret으로 자동 동기화 | 클라우드 네이티브 환경에서 관리 용이 |

<div class="callout why">
  <div class="callout-title">핵심 인사이트: "환경 변수는 안전하지 않습니다"</div>
  많은 개발자가 비밀값을 환경 변수(Env Var)로 주입하곤 합니다. 하지만 환경 변수는 컨테이너 로그에 찍히거나, <code>docker inspect</code> 명령으로 쉽게 노출될 수 있습니다. 중요한 비밀값은 <b>메모리 내에서만 사용</b>하거나 <b>파일 마운트</b> 방식을 사용하는 것이 훨씬 안전합니다.
</div>

## 정책의 코드화 (Policy as Code)

"루트 권한으로 실행되는 Pod 금지", "특정 레지스트리 이미지만 허용"과 같은 규칙을 사람이 일일이 검토할 수 없습니다. **Policy as Code**(PaC)는 이러한 규정을 코드로 정의하고 자동 검증합니다.

### 1. OPA (Open Policy Agent)
**Rego**라는 전용 언어를 사용하여 매우 복잡하고 세밀한 정책을 세울 수 있습니다. 쿠버네티스뿐만 아니라 API, Terraform 설정 검증 등 범용적으로 쓰입니다.

### 2. Kyverno
Rego 같은 별도 언어 학습 없이, **쿠버네티스 리소스 형식(YAML)** 그대로 정책을 정의할 수 있어 접근성이 매우 높습니다.

```yaml
# Kyverno 정책 예시: 루트 권한 Pod 금지
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: disallow-root-user
spec:
  rules:
  - name: check-run-as-non-root
    match:
      resources:
        kinds: [Pod]
    validate:
      message: "비-루트 사용자로 실행해야 합니다."
      pattern:
        spec:
          securityContext:
            runAsNonRoot: true
```

## 컴플라이언스 자동화

금융권이나 공공 기관처럼 엄격한 보안 규정을 준수해야 하는 조직은 **컴플라이언스 대시보드**를 자동화합니다.

- **Continuous Compliance**: 배포된 모든 리소스가 정책을 준수하는지 실시간 감시 (Drift Detection)
- **Auto-remediation**: 정책 위반이 발견되면 자동으로 리소스를 삭제하거나 수정 (예: Public S3 버킷을 즉시 Private으로 전환)

## 정리

- **비밀 정보**는 절대 코드 저장소에 평문으로 두지 않으며, 전용 도구(Vault, External Secrets 등)를 사용합니다.
- **Policy as Code**를 통해 보안 규정을 자동화하고 강제합니다.
- 사람이 하는 보안 검토를 **기계가 수행하는 정책 검증**으로 대체하여 배포 속도를 높입니다.
- 보안은 일회성 점검이 아닌 **지속적인 감시와 수정**의 과정이어야 합니다.

DevSecOps 시리즈를 통해 보안을 파이프라인의 핵심 구성 요소로 통합하는 여정을 살펴보았습니다. 자동화된 도구와 투명한 정책은 개발팀과 보안팀이 서로 신뢰하며 협력할 수 있는 단단한 기반이 될 것입니다.
