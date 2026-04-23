---
title: "컴퓨트·스토리지 최적화"
description: Spot/Reserved·Rightsizing·Lifecycle Policy로 컴퓨트와 스토리지 비용을 줄이는 방법을 정리해요.
date: 2026-04-20
order: 2
category: DevOps & SRE
subcategory: Cost Optimization
tags: [finops, spot, reserved, rightsizing, storage]
image: /assets/og/2026-04-20-cost-optimization-02-compute.png
---

클라우드 비용의 가장 큰 비중을 차지하는 것은 단연 컴퓨트와 스토리지입니다. "일단 넉넉하게 잡고 보자"는 식의 관성은 매달 불필요한 지출을 유발합니다. 기술적인 관점에서 즉시 적용할 수 있는 비용 절감 기법들을 컴퓨트와 스토리지 중심으로 정리해요

## 컴퓨트 최적화: 필요한 만큼만, 더 저렴하게

컴퓨트 비용을 줄이는 세 가지 핵심 전략입니다

### 1. 적정 사이즈 조정 (Rightsizing)
실제 사용량 메트릭(CPU, Memory)을 분석하여 오버 프로비저닝된 인스턴스를 낮은 사양으로 변경합니다

- **방법**: 2주 이상의 평균 및 최대 사용량을 모니터링하여 가동률이 20~30% 이하인 인스턴스를 타겟으로 합니다
- **도구**: AWS Trusted Advisor, Compute Optimizer 등을 활용합니다

### 2. 구매 옵션 활용 (RI / Savings Plans)
고정적으로 사용하는 인스턴스는 예약 인스턴스(Reserved Instances)나 Savings Plans를 통해 최대 70%까지 할인받을 수 있습니다

| 옵션 | 특징 | 적합한 워크로드 |
|---|---|---|
| **On-Demand** | 가변적, 가장 비쌈 | 신규 프로젝트, 예측 불가능한 트래픽 |
| **RI / SP** | 약정 기반, 높은 할인 | DB, Core API 등 24시간 가동 서버 |
| **Spot** | 유휴 자원 입찰, 최대 90% 할인 | 데이터 처리, CI 빌드 등 중단 가능한 작업 |

### 3. 스팟 인스턴스 (Spot Instances)
언제든 회수될 수 있다는 단점이 있지만, 가격 매력이 압도적입니다. 상태가 없는(Stateless) 배치 작업이나 테스트 환경에서 적극 활용해야 합니다

## 스토리지 최적화: 잊혀진 데이터 찾아내기

스토리지는 생성은 쉽지만 삭제는 잊기 쉽습니다

```mermaid
flowchart LR
    Data["데이터 생성"] --> Hot["Standard<br/>(자주 접근)"]
    Hot -->|"Lifecycle"| Warm["IA / Glacier<br/>(가끔 접근)"]
    Warm -->|"Lifecycle"| Cold["Deep Archive<br/>(장기 보관)"]
    Cold -->|"Delete"| End["영구 삭제"]

    classDef neutral fill:#475569,stroke:#334155,color:#ffffff
    classDef success fill:#059669,stroke:#047857,color:#ffffff
    classDef info fill:#0891b2,stroke:#0e7490,color:#ffffff

    class Data,End neutral
    class Hot success
    class Warm,Cold info
```

- **S3 수명 주기 정책(Lifecycle Policy)**: 데이터가 생성된 지 일정 기간이 지나면 자동으로 저렴한 스토리지 클래스로 이동하거나 삭제하도록 설정합니다
- **연결되지 않은 볼륨(Unattached Volumes)**: EC2 인스턴스를 삭제해도 연결된 EBS 볼륨은 남는 경우가 많습니다. 주기적으로 찾아내어 스냅샷 후 삭제합니다
- **고아 스냅샷**: 너무 오래된 백업 스냅샷이나 중복된 데이터를 정리합니다

<div class="callout why">
  <div class="callout-title">핵심 인사이트: 최적화는 한 번으로 끝나지 않습니다</div>
  인프라는 살아있는 유기체와 같습니다. 서비스가 성장하거나 코드가 효율적으로 바뀌면 필요한 자원의 양도 변합니다. <b>매월 또는 분기별로 Rightsizing 세션</b>을 열어 기술 부채를 정리하듯 비용 부채를 정리하는 습관이 필요합니다
</div>

## 비용 알람 및 예산 설정

비용 폭탄을 막기 위해 예산(Budgets) 알람을 설정하는 것은 엔지니어의 기본 소양입니다

1. **임계치 설정**: 월 예상 비용의 50%, 80%, 100% 도달 시 알람 발송
2. **이상 징후 탐지(Anomaly Detection)**: 평소와 다른 급격한 비용 상승 발생 시 즉시 알림

## 정리

- **Rightsizing**을 통해 사용하지 않는 자원의 낭비를 막습니다
- **RI / Savings Plans**로 고정 비용을 낮추고, **Spot**으로 가변 비용을 극대화합니다
- **S3 수명 주기 정책**으로 스토리지 비용의 자동화를 실현합니다
- **비용 알람**을 통해 예상치 못한 지출에 선제적으로 대응합니다

다음 글에서는 컨테이너 환경의 특수한 비용 관리 방식인 **Kubernetes 비용 관리**에 대해 알아봐요
