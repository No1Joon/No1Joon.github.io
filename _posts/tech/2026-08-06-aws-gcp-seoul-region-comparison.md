---
title: "AWS와 GCP 서울 리전, 같은 사양 시간당 0.0008달러 차이"
description: "양쪽 공식 가격표에서 서울 리전 값만 뽑아 맞대고, 정가가 아니라 자동 할인과 이그레스에서 청구서가 갈리는 이유를 정리합니다"
date: 2026-08-06
category: Tech
subcategory: Explainer
tags: [aws, gcp, cloud-pricing, seoul-region, egress]
image: /assets/og/2026-08-06-aws-gcp-seoul-region-comparison.png
---

"AWS가 비싸다"거나 "GCP가 싸다"는 말은 대개 출처가 없습니다. 리전마다 다르고, 인스턴스 세대마다 다르고,
약정을 걸었느냐에 따라 또 달라지니까요. 그래서 양쪽 공식 가격표에서 **서울 리전 값만** 뽑아 맞대 봤습니다.

결론부터 말하면 정가는 놀랄 만큼 붙어 있습니다. 갈리는 건 정가가 아니라 **아무것도 안 했을 때 무슨 일이
벌어지는가**, 그리고 **밖으로 나가는 트래픽 값**입니다.

*주: 이 글의 모든 수치는 2026년 8월 6일 AWS 가격 피드(ap-northeast-2)와 Google Cloud 공식 가격표
(asia-northeast3)에서 직접 조회한 Linux 기준 값입니다. 클라우드 요금은 예고 없이 바뀝니다.*

## 정가는 소수점 셋째 자리까지 붙어 있다

![서울 리전 2 vCPU · 8 GiB 급 온디맨드 시간당 요금](/assets/images/tech/aws-gcp-seoul-region-comparison/01-chart.webp)
*서울 리전 2 vCPU · 8 GiB 급 온디맨드 시간당 요금 — 출처: 자가 생성*

가장 흔한 사양인 **2 vCPU · 8 GiB 범용 인스턴스**로 맞춰 보겠습니다.
AWS의 m7i.large가 시간당 **0.1239달러**, GCP의 n2-standard-2가 **0.124718달러**입니다.
차이가 시간당 0.0008달러, 비율로 0.66%예요. 우연이라고 보기 어려운 수준으로 서로를 보고 있습니다.

같은 급 안에서도 선택지는 갈립니다.

| 인스턴스 | vCPU · 메모리 | 시간당 (달러) | 성격 |
| :--- | :--- | :--- | :--- |
| GCP e2-standard-2 | 2 · 8 GiB | <mark>0.085966</mark> | CPU 플랫폼 미지정, 비용 우선 |
| AWS m7g.large | 2 · 8 GiB | 0.100300 | Graviton3 Arm |
| GCP n4-standard-2 | 2 · 8 GiB | 0.116477 | 최신 세대, 자동 할인 없음 |
| AWS m7i.large | 2 · 8 GiB | 0.123900 | Intel 범용 기준선 |
| GCP n2-standard-2 | 2 · 8 GiB | 0.124718 | 자동 할인 대상 |

정가표만 놓고 "GCP가 30% 싸다"고 말할 수도 있습니다. e2-standard-2를 기준으로 잡으면요.
그런데 E2는 CPU 플랫폼을 고를 수 없고 성능 편차를 감수하는 계열이라, m7i.large와 같은 줄에 세우면
비교가 성립하지 않습니다. **같은 값끼리 비교하려면 세대와 보장 수준을 먼저 맞춰야 합니다.**

## 아무것도 안 하면 GCP가 20% 싸진다

![약정 없이 730시간 가동한 한 대의 월 요금](/assets/images/tech/aws-gcp-seoul-region-comparison/02-chart.webp)
*약정 없이 730시간 가동한 한 대의 월 요금 — 출처: 자가 생성*

여기서 첫 번째 갈림길이 나옵니다. GCP에는 **지속 사용 할인**(Sustained Use Discount)이 있습니다.
약정도, 신청도, 설정도 필요 없습니다. 청구 월의 25%를 넘겨 켜두면 자동으로 붙기 시작해서,
한 달을 통째로 돌리면 N2 계열은 **정가의 80%** 가 됩니다.

- 약정 없이 730시간 가동: AWS m7i.large **90.45달러**(약 12.7만원)
- 같은 조건: GCP n2-standard-2 **72.84달러**(약 10.2만원)

한 대당 월 17.6달러, 연 211달러(약 30만원) 차이입니다. 인스턴스 100대면 연 3천만원이고요.
**아무 최적화도 하지 않은 팀일수록 이 격차가 그대로 청구서에 나타납니다.**

### 다만 최신 계열에는 안 붙는다

이 할인이 만능은 아닙니다. 적용 대상은 N1·N2·N2D·C2·M1·M2 계열이고, 할인율도 갈립니다.

| 계열 | 월 100% 가동 시 자동 할인 |
| :--- | :--- |
| N1 · M1 · M2 | 최대 30% |
| N2 · N2D · C2 | <mark>최대 20%</mark> |
| E2 · N4 · C4 · C3 | **없음** |

정가가 더 싼 N4나 E2를 고르면 이 할인을 못 받습니다. n4-standard-2는 정가 0.116477달러로
n2-standard-2보다 6.6% 싸지만, 한 달을 꽉 채워 돌리면 지속 사용 할인이 붙은 N2 쪽이 14% 더 쌉니다.
**정가 순위와 실청구 순위가 뒤집히는 구간**이 여기예요.

> 한 줄 요약: GCP N2 계열은 한 달 내내 켜두면 자동으로 20% 깎이고, AWS는 약정을 걸어야 깎인다.

## 약정은 문법이 다른데 도착점은 같다

![약정 종류별 정가 대비 절감률](/assets/images/tech/aws-gcp-seoul-region-comparison/03-chart.webp)
*약정 종류별 정가 대비 절감률 — 출처: 자가 생성*

양쪽 다 약정 할인이 있고, 구조가 둘로 갈리는 것까지 똑같습니다.

| 성격 | AWS | GCP |
| :--- | :--- | :--- |
| 금액만 약속, 인스턴스는 자유 | Compute Savings Plans | Compute Flexible CUD |
| 특정 계열 고정, 대신 더 깊게 | EC2 Instance Savings Plans | Compute Resource CUD |

이름과 약속 방식이 다를 뿐 성격이 같고, 놀랍게도 **깎이는 폭까지 거의 같습니다.**
선결제 없이 3년을 걸면 인스턴스 고정 쪽은 AWS가 54.8%, GCP가 55.0%를 깎아 줍니다.
유연한 쪽은 3년에 AWS 47.7%, GCP 46.0%고요.

1년 약정에서만 방향이 조금 다릅니다. 인스턴스를 고정하는 조건에서 GCP가 37.0%, AWS가 34.6%로
GCP가 조금 더 깊고, 유연한 쪽에서는 AWS 28.4%, GCP 28.0%로 거의 같습니다.

- 실무에서 갈리는 건 할인 폭이 아니라 **약정을 못 채웠을 때**입니다.
AWS Savings Plans는 시간당 약정 금액을 못 쓰면 그 차액이 그냥 사라집니다.
GCP의 리소스 CUD도 마찬가지로 해당 리전·계열에 묶여 낭비될 수 있고요.
두 쪽 다 "쓸 만큼만 약속하고 나머지는 온디맨드"가 안전한 출발점입니다.

## 공식 가격표를 열면 보이는 것

![Google Cloud 서울 리전 공식 가격표](/assets/images/tech/aws-gcp-seoul-region-comparison/04-photo-gcp.webp)
*Google Cloud 서울 리전 공식 가격표 — 출처: Google Cloud*

위 화면은 Google Cloud 가격표에서 리전을 서울로 맞춘 상태입니다. 표 자체보다 그 위의 안내문이
중요합니다 — Compute Engine의 디스크 용량, 머신 메모리, **네트워크 사용량을 GiB로 센다**고 적혀 있어요.

1 GiB는 2³⁰바이트, 1 GB는 10⁹바이트입니다. 7.4% 차이고요.
AWS는 데이터 전송을 GB로 셉니다. **같은 숫자가 적혀 있어도 같은 값이 아니라는 뜻입니다.**

이 표를 여는 김에 하나 더 확인해 둘 것이 있습니다. 표 왼쪽의 리전 선택기에서 어떤 계열은
서울이 아예 목록에 없습니다. 뒤에서 다시 보겠습니다.

## 단위를 맞추면 네트워크가 갈린다

![이그레스 단가를 같은 단위로 맞춘 계산](/assets/images/tech/aws-gcp-seoul-region-comparison/05-term.webp)
*이그레스 단가를 같은 단위로 맞춘 계산 — 출처: 자가 생성*

컴퓨트가 붙어 있으니 승부는 네트워크에서 납니다. 서울 리전에서 인터넷으로 나가는 첫 10TB 구간
단가를 같은 단위로 환산하면 **GCP가 AWS의 1.4배**입니다.

| 항목 | AWS 서울 | GCP 서울 |
| :--- | :--- | :--- |
| 인터넷 송신 (첫 10TB) | <mark>GB당 0.126달러</mark> | GiB당 0.19달러 (GB당 0.177달러) |
| 더 싼 경로 | 없음 | 스탠다드 티어 GiB당 0.119달러 |
| 무료 송신 | 월 100GB (전 서비스·리전 합산) | 프리미엄 티어에는 해당 구간 없음 |
| 인바운드 | 무료 | 무료 |
| 가용영역·존 간 | GB당 0.01달러, **양쪽 모두 과금** | GiB당 0.01달러, 보내는 쪽만 |
| 서울 → 도쿄 | GB당 0.08달러 | — |

두 줄을 짚고 가겠습니다.

### 스탠다드 티어는 요금이 싼 대신 구글 백본을 타지 않는다

GCP의 스탠다드 티어는 GiB당 0.119달러(GB당 0.111달러)로 AWS보다도 쌉니다. 대신 트래픽이
구글 백본을 타지 않고 **가까운 접속점에서 공용 인터넷으로 빠집니다.** 지연과 안정성을 요금과
맞바꾸는 선택이라, 글로벌 사용자를 받는 서비스에서는 기본값으로 고르기 어렵습니다.

### AZ 간 요금은 AWS가 두 배로 붙는다

AWS는 가용영역을 넘는 트래픽에 보내는 쪽과 받는 쪽 **양쪽에 GB당 0.01달러**를 매깁니다.
1GB를 옮기면 실제로는 0.02달러입니다. GCP는 존을 넘을 때 보내는 쪽에만 GiB당 0.01달러를 매기고요.
이중화를 위해 3-AZ로 깔고 서비스끼리 활발히 통신하는 구조라면, 이 줄이 컴퓨트 차액을 삼킬 수 있습니다.

> 시간당 요금이 같아도 GiB·GB 단위와 트래픽 방향이 다르면 청구서 금액은 달라집니다.

## 서울에는 Arm이 한쪽에만 있다

![서울 리전 Arm 가용성 개념 컷](/assets/images/tech/aws-gcp-seoul-region-comparison/06-agy-arm.webp)
*서울 리전 Arm 가용성 개념 컷 — 출처: 자가 생성*

가격표를 리전별로 훑다 보면 요금보다 큰 차이가 하나 나옵니다.
**Google Cloud의 Arm 계열은 2026년 8월 현재 서울 리전에서 제공되지 않습니다.**

가격표의 리전 선택기를 직접 열어 확인한 결과입니다.

| 계열 | 프로세서 | 서울 제공 |
| :--- | :--- | :--- |
| GCP C4A | Google Axion | ❌ (도쿄는 제공) |
| GCP N4A | Google Axion | ❌ |
| GCP Tau T2A | Ampere Altra | ❌ |
| AWS m7g · c7g · r7g | Graviton3 | ⭕ |
| AWS m8g · c8g | Graviton4 | ⭕ |

AWS 쪽에서 Graviton은 단순한 선택지가 아니라 **가격 카드**입니다. 서울에서 m7g.large는
0.1003달러로 같은 사양 m7i.large보다 19% 쌉니다. 컨테이너로 굴러가는 스테이트리스 워크로드라면
아키텍처 전환 비용이 크지 않으니, 이 19%는 그대로 절감으로 남습니다.

정리하면 **서울에서 Arm으로 원가를 낮추는 전략은 지금 AWS에서만 가능합니다.**
도쿄까지 갈 수 있는 워크로드라면 GCP에서도 Axion을 쓸 수 있지만, 그 순간 지연과
국내 데이터 보관 요건이 새 변수로 들어옵니다.

## 그래서 어디를 고르나

![선택 기준 개념 컷](/assets/images/tech/aws-gcp-seoul-region-comparison/07-agy-choice.webp)
*선택 기준 개념 컷 — 출처: 자가 생성*

정가가 붙어 있다는 건 **가격만으로는 결정이 안 난다**는 뜻입니다. 갈리는 지점으로 판단하는 게 맞습니다.

| 이런 상황이면 | 유리한 쪽 | 이유 |
| :--- | :--- | :--- |
| 최적화할 인력이 없고 그냥 계속 켜둔다 | GCP | 지속 사용 할인이 자동으로 20% |
| Arm으로 옮길 수 있는 워크로드가 많다 | AWS | 서울에서 Graviton은 19% 싸고 GCP엔 Arm이 없다 |
| 밖으로 나가는 트래픽이 많다 | AWS | 이그레스가 GCP의 약 70% 수준 |
| 서비스 간 통신이 AZ를 자주 넘는다 | GCP | 존 간 요금이 보내는 쪽에만 붙는다 |
| 3년을 확신할 수 있다 | 비슷함 | 55% 대 54.8%, 사실상 동률 |
| 성능 편차를 감수하고 원가를 낮춘다 | GCP | E2 계열에 대응할 AWS 카드가 마땅치 않다 |

- 한 가지만 고르라면 **트래픽 방향**을 먼저 재는 게 좋습니다. 컴퓨트 차이는 잘해야 20% 안쪽인데,
이그레스가 많은 서비스는 네트워크 요금이 컴퓨트를 넘어서는 경우가 흔합니다.
반대로 내부 통신만 많고 밖으로 거의 안 나가는 배치 시스템이면 존 간 요금 쪽이 더 크게 작용하고요.

> 정가가 같아졌으니 어느 쪽이 싼지는 트래픽 방향과 Arm 사용 여부가 정합니다.

## 정리

서울 리전에서 같은 급 범용 인스턴스의 시간당 정가는 AWS 0.1239달러, GCP 0.124718달러로
0.66% 차이입니다. 3년 약정을 걸었을 때의 절감률도 54.8% 대 55.0%로 사실상 같고요.
경쟁이 가격표를 수렴시킨 결과입니다.

기억할 건 셋입니다.

### 약정을 걸지 않고 한 달 내내 켜두면 GCP N2 계열은 자동으로 20% 깎입니다. 대신 **N4·C4·E2 에는 그 할인이 없습니다.**

### 나가는 트래픽은 AWS가 쌉니다. 단, **GiB와 GB를 맞춰 놓고** 비교해야 합니다.

### 서울에서 **Arm은 AWS에만** 있고, m7g.large 는 같은 사양 m7i.large 보다 19% 쌉니다.

가격 비교표를 만들 때 시간당 요금 열 하나로 끝내면 거의 틀립니다. 단위, 자동 할인, 방향별 트래픽
요금까지 같은 표에 놓아야 비로소 우리 워크로드에서 어느 쪽이 싼지가 나옵니다.

## 참고 출처

- [[Amazon Web Services] EC2 온디맨드 요금 — 서울 리전 정가·월 100GB 무료 송신 고지](https://aws.amazon.com/ko/ec2/pricing/on-demand/)
- [[Amazon Web Services] AWS Data Transfer 공식 가격 목록 — 서울 이그레스·AZ 간·리전 간 단가](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json)
- [[Amazon Web Services] Compute Savings Plans 공식 가격 목록 (ap-northeast-2)](https://pricing.us-east-1.amazonaws.com/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json)
- [[Google Cloud] General-purpose machine type family pricing (본문 가격표 캡처 출처)](https://cloud.google.com/products/compute/pricing/general-purpose)
- [[Google Cloud] 지속 사용 할인 — 적용 대상 계열과 20%·30% 구간](https://docs.cloud.google.com/compute/docs/sustained-use-discounts)
- [[Google Cloud] All networking pricing — 서울 리전 이그레스·존 간 데이터 전송 단가](https://cloud.google.com/vpc/network-pricing)
- 환율: 1달러 ≈ 1,400원 기준 환산
- 조회 시점: 2026-08-06 · Linux · 선결제 없음 기준
