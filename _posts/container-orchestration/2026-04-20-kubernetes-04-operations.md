---
title: "프로덕션 운영 패턴"
description: 리소스 제한·HPA·PDB·affinity로 Kubernetes 워크로드를 안정적으로 운영하는 기준을 정리합니다.
date: 2026-04-20
order: 4
category: Container & Orchestration
subcategory: Kubernetes
tags: [kubernetes, hpa, pdb, resources, autoscaling, operations]
image: /assets/og/2026-04-20-kubernetes-04-operations.png
---

애플리케이션을 Kubernetes에 배포하는 것을 넘어, 프로덕션 환경에서 장애에 견디고 자원을 효율적으로 사용하기 위해서는 명확한 **운영 정책**이 필요합니다. 리소스 할당부터 자동 확장, 고가용성 보장을 위한 핵심 패턴들을 정리합니다

## 리소스 관리: Requests와 Limits

가장 기초적이면서 중요한 설정입니다. 리소스를 정의하지 않으면 하나의 Pod가 노드의 모든 자원을 점유하여 다른 서비스에 영향을 줄 수 있습니다

| 설정 | 역할 | 특징 |
|---|---|---|
| Requests | 최소 보장량 | 스케줄러가 노드를 선택하는 기준 |
| Limits | 최대 제한량 | 초과 시 CPU는 쓰로틀링, 메모리는 종료(OOM) |

메모리의 경우 **Requests와 Limits를 동일하게** 설정하여 성능 예측 가능성을 높이는 것을 권장합니다

## 오토스케일링 전략

트래픽 변동에 유연하게 대응하기 위해 자동화된 확장 체계를 구축합니다

- **HPA**(Horizontal Pod Autoscaler): CPU나 메모리 사용량에 따라 Pod의 개수를 조절합니다
- **VPA**(Vertical Pod Autoscaler): 실제 사용량에 맞춰 Pod의 리소스 예약 값을 조정합니다
- **CA**(Cluster Autoscaler): 노드 자원이 부족할 때 새로운 서버를 자동으로 추가합니다

```mermaid
flowchart LR
    Metrics["Metrics Server"]
    HPA["HPA Controller"]
    Dep["Deployment"]
    Pod["Pod Instances"]

    Metrics --> HPA --> Dep --> Pod

    classDef primary fill:#2563eb,stroke:#1e40af,color:#ffffff
    classDef success fill:#059669,stroke:#047857,color:#ffffff

    class Metrics,HPA primary
    class Dep,Pod success
```

## 가용성 보장: PDB와 Affinity

노드 점검이나 업데이트 상황에서도 서비스 연속성을 유지하기 위한 장치들입니다

### Pod Disruption Budget (PDB)
자발적인 점검 상황에서 동시에 중단될 수 있는 Pod의 최대 개수나 최소 유지 개수를 정의합니다. 이를 통해 무리한 노드 비우기 작업으로부터 서비스를 보호합니다

### Affinity와 Anti-Affinity
- **Affinity**: 특정 노드나 다른 Pod와 가까운 곳에 배치되도록 유도합니다
- **Anti-Affinity**: 동일 서비스의 Pod들이 서로 다른 노드나 가용 영역(AZ)에 흩어지도록 강제하여 노드 장애 시 전체 중단을 막습니다

## Graceful Shutdown 설정

Pod가 종료될 때 처리 중인 요청을 안전하게 마무리하는 과정이 필요합니다. `preStop` 훅을 사용하여 트래픽이 완전히 차단될 때까지 앱 종료를 지연시키고, `terminationGracePeriodSeconds`를 통해 정리 시간을 충분히 부여합니다

<div class="callout why">
  <div class="callout-title">QoS 클래스의 이해</div>
  리소스 설정 방식에 따라 <b>Guaranteed, Burstable, BestEffort</b> 클래스가 결정됩니다. 노드 자원이 부족하여 Pod를 쫓아내야 할 때, 중요한 서비스가 먼저 종료되지 않도록 <b>Guaranteed</b> 등급을 유지하는 것이 중요합니다
</div>

## 안정적인 운영을 위한 체크리스트

1. 모든 컨테이너에 리소스 **Requests/Limits** 선언
2. **Liveness/Readiness Probe**의 세밀한 튜닝
3. 가용성 보장을 위한 **PDB** 적용
4. 다중 노드/영역 분산을 위한 **Anti-Affinity** 설정
5. 배포 안전을 위한 **RollingUpdate** 전략 수립

## 정리

- **리소스 제한**은 클러스터 안정성의 시작점입니다
- **HPA**와 **CA**의 조합으로 인프라 효율과 가용성을 동시에 잡습니다
- **PDB**와 **분산 배치** 정책으로 예기치 못한 중단을 방어합니다
- 정상 종료 처리를 통해 사용자 경험의 단절을 막습니다

이로써 Kubernetes의 핵심 운영 패턴을 살펴보았습니다. 다음 시리즈에서는 복잡한 매니페스트를 재사용 가능한 패키지로 관리하는 **Helm**에 대해 알아봅니다
