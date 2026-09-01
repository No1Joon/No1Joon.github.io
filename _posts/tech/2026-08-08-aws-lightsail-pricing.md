---
title: "AWS Lightsail 요금 구조 — 번들에 뭐가 묶여 있나"
description: "월 4,800원짜리 AWS 서버가 싼 이유를 번들 구성에서 찾고, 같은 트래픽에서 EC2 와 갈리는 금액과 포기하는 선택지를 정리합니다"
date: 2026-08-08
category: Tech
subcategory: Explainer
tags: [aws, lightsail, cloud-pricing, ec2, bandwidth]
image: /assets/og/2026-08-08-aws-lightsail-pricing.png
---

AWS 요금이 비싸다는 말은 대개 EC2 를 두고 하는 이야기입니다. 그런데 같은 AWS 안에
**월 4,800원짜리 서버**가 있습니다. Amazon Lightsail 입니다.

싼 이유는 할인이 아니라 **묶음** 때문입니다. 인스턴스와 SSD 와 데이터 전송량을 한 값에 묶어
팔고, 그 대신 EC2 가 주는 선택지를 대부분 걷어냈습니다. 무엇이 묶였고 무엇을 포기하는지
AWS 공식 가격 목록에서 서울 리전 값만 꺼내 정리했습니다.

*주: 모든 수치는 2026년 8월 8일 AWS 공식 가격 목록(AmazonLightsail · AWSDataTransfer, ap-northeast-2)에서
직접 조회한 값입니다. 월 요금은 730시간, 1달러는 1,400원으로 환산했습니다.*

![Amazon Lightsail 제품 이미지](/assets/images/tech/aws-lightsail-pricing/01-photo-lightsail.webp)
*Amazon Lightsail 제품 이미지 — 출처: Amazon Web Services*

## 번들 하나에 세 가지가 묶여 있다

![Lightsail 서울 리전 번들 월 요금](/assets/images/tech/aws-lightsail-pricing/02-chart.webp)
*Lightsail 서울 리전 번들 월 요금 — 출처: 자가 생성*

Lightsail 요금은 **인스턴스 + SSD + 데이터 전송량**이 한 덩어리입니다.
서울 리전 Linux 기준으로 이렇게 올라갑니다.

| 메모리 · SSD | 전송량 | 월 요금 |
| :--- | :--- | :--- |
| 0.5GB · 20GB | 1TB | <mark>4,803원</mark> |
| 1GB · 40GB | 2TB | 6,868원 |
| 2GB · 60GB | 3TB | 13,736원 |
| 4GB · 80GB | 4TB | 27,471원 |
| 8GB · 160GB | 5TB | 54,943원 |

vCPU 는 이 구간 전체가 2개입니다. 가격을 가르는 건 메모리·디스크·전송량이에요.

눈에 띄는 건 **전송량**입니다. 가장 싼 4,803원짜리에 월 1TB 가 들어 있습니다.
국내 클라우드의 무료 구간이 월 20GB 안팎이고 AWS EC2 가 월 100GB 인 것과 비교하면 자릿수가 다릅니다.

## IPv6-only 번들이 더 싸다

![4GB 번들의 월 요금 — 듀얼스택과 IPv6-only](/assets/images/tech/aws-lightsail-pricing/03-chart-ipv6.webp)
*4GB 번들의 월 요금 — 듀얼스택과 IPv6-only — 출처: 자가 생성*

가격 목록을 열면 같은 사양이 두 줄씩 나옵니다. **듀얼스택 번들과 IPv6-only 번들**이에요.
4GB 번들 기준으로 듀얼스택 32,956원, IPv6-only 27,471원. 월 5,485원 차이입니다.

이 차액은 우연이 아닙니다. 시간당으로 환산하면 약 0.0054달러인데,
AWS 가 2024년 2월부터 받기 시작한 **퍼블릭 IPv4 주소 요금이 시간당 0.005달러**입니다.
번들에서 IPv4 주소를 빼면 그만큼 값을 깎아 주는 구조예요.

| 번들 | 듀얼스택 | IPv6-only |
| :--- | :--- | :--- |
| 0.5GB | 6,868원 | <mark>4,803원</mark> |
| 1GB | 9,607원 | 6,868원 |
| 4GB | 32,956원 | 27,471원 |

작은 번들일수록 할인 비율이 큽니다. 0.5GB 는 30% 차이입니다.
서버가 밖으로 나가기만 하고 밖에서 IPv4 로 들어올 일이 없다면 — 예를 들어 앞에 CDN 이나
로드밸런서를 두는 구성이라면 — IPv6-only 를 고를 실익이 있습니다.

## 싼 값에 포기하는 것 — CPU 는 버스터블이다

![AWS 공식 CPU 버스트 존 도표](/assets/images/tech/aws-lightsail-pricing/04-photo-aws.webp)
*AWS 공식 CPU 버스트 존 도표 — 출처: Amazon Web Services*

Lightsail 인스턴스는 **버스터블**입니다. AWS 문서는 CPU 사용률 그래프를
지속 가능 구간과 버스트 구간 둘로 나눠 설명합니다.

지속 가능 구간 안에서는 제한 없이 계속 돌릴 수 있습니다. 그 위로 올라가면 버스트 용량을
쓰기 시작하는데, 이 용량은 쌓이고 소모되는 잔고 같은 것이라 오래 버티지 못합니다.
문서 표현으로는 버스트 구간에 오래 머물면 결국 용량을 다 쓰고 지속 가능 구간으로 되돌아옵니다.

### 무엇을 봐야 하나

Lightsail 은 이걸 볼 수 있는 지표를 따로 줍니다.

| 지표 | 뜻 |
| :--- | :--- |
| BurstCapacityTime | 100% 로 버스트할 수 있는 남은 시간 |
| BurstCapacityPercentage | 지금 쓸 수 있는 CPU 성능 비율 |

빌드를 돌리거나 배치 작업을 하는 서버라면 이 지표가 바닥을 치는지 먼저 확인해야 합니다.
**상시 CPU 부하가 걸리는 워크로드에는 맞지 않습니다.**

## 같은 걸 EC2 로 조립하면

![같은 사양을 EC2 로 조립했을 때의 월 비용](/assets/images/tech/aws-lightsail-pricing/05-chart-ec2.webp)
*같은 사양을 EC2 로 조립했을 때의 월 비용 — 출처: 자가 생성*

Lightsail 4GB 번들(2 vCPU · 4GB · 80GB SSD · 4TB 전송)과 같은 구성을 EC2 로 맞춰 봤습니다.
버스터블끼리 비교해야 공정하니 t3.medium 을 썼습니다.

| 항목 | 월 |
| :--- | :--- |
| t3.medium | 53,144원 |
| 퍼블릭 IPv4 | 5,110원 |
| 아웃바운드 4TB | <mark>704,894원</mark> |

합계 763,148원입니다. EBS 스토리지는 여기에 더 붙습니다.
같은 조건의 Lightsail 번들이 32,956원이니 **23배** 차이입니다.

차이를 만든 건 인스턴스가 아니라 **데이터 전송**입니다. EC2 는 월 100GB 를 넘기면
GB당 0.126달러를 받는데, 4TB 면 3,996GB 가 그 단가에 걸립니다.
Lightsail 은 그 4TB 를 번들 값 안에 넣어 둡니다.

> 한 줄 요약: Lightsail 이 싼 건 서버가 싸서가 아니라 트래픽이 묶여 있어서다.

## 국내 클라우드와도 대봤다

![2 vCPU · 4GB 서버에 월 1TB 트래픽을 얹었을 때](/assets/images/tech/aws-lightsail-pricing/06-chart-1tb.webp)
*2 vCPU · 4GB 서버에 월 1TB 트래픽을 얹었을 때 — 출처: 자가 생성*

같은 2 vCPU · 4GB 서버에 월 1TB 트래픽을 얹으면 순위가 이렇게 됩니다.

| 서비스 | 월 요금 |
| :--- | :--- |
| Lightsail | <mark>32,956원</mark> |
| 네이버 클라우드 | 163,512원 |
| NHN Cloud | 180,118원 |
| EC2 조립 | 221,248원 |

Lightsail 이 국내 클라우드의 5분의 1입니다. 트래픽이 붙는 순간 격차가 이렇게 벌어집니다.

다만 **트래픽이 적으면 이 격차가 사라집니다.** 월 100GB 라면 Lightsail 32,956원,
EC2 조립 58,254원, 네이버 80,352원으로 좁혀집니다. 트래픽이 없는 내부 API 서버라면
번들의 이점을 거의 못 씁니다.

## 갈아탈 수 없는 것들

![번들 요금 개념 컷](/assets/images/tech/aws-lightsail-pricing/07-agy-bundle.webp)
*번들 요금 개념 컷 — 출처: 자가 생성*

요금이 단순해진 대가로 운영 선택지가 줄어듭니다.

| 항목 | Lightsail |
| :--- | :--- |
| 요금제 변경 | 스냅샷 떠서 새로 만들어야 함 |
| CPU 성능 | 버스터블 고정 |
| vCPU 수 | 8GB 이하 번들은 전부 2개 |

가장 걸리는 건 첫 줄입니다. AWS 문서는 더 큰 요금제로 옮기는 방법을
**"인스턴스 스냅샷을 만든 뒤 그 스냅샷으로 새 인스턴스를 만든다"** 고 안내합니다.
EC2 처럼 인스턴스를 정지하고 타입만 바꾸는 방식이 아니에요.
IP 가 바뀌고 다운타임이 생기니 트래픽이 늘 때를 대비한 절차를 미리 짜 둬야 합니다.

돌아갈 길은 열려 있습니다. Lightsail 은 **EC2 로 내보내기**를 지원합니다.
스냅샷을 EC2 로 옮겨 인스턴스 타입·네트워킹·스토리지를 세밀하게 잡는 구성으로 갈아탈 수 있습니다.

## 그래서 언제 Lightsail 인가

![선택 기준 개념 컷](/assets/images/tech/aws-lightsail-pricing/08-agy-choice.webp)
*선택 기준 개념 컷 — 출처: 자가 생성*

| 이런 상황이면 | 판단 |
| :--- | :--- |
| 트래픽이 월 수백 GB 이상 | Lightsail |
| CPU 를 상시로 쓴다 | EC2 |
| 오토스케일이 필요하다 | EC2 |
| 사양을 자주 바꾼다 | EC2 |
| 요금을 예측하고 싶다 | Lightsail |

- 기준을 하나로 줄이면 **트래픽**입니다. 이미지나 동영상처럼 밖으로 나가는 양이 많은
서비스라면 번들에 묶인 전송량이 다른 모든 항목을 압도합니다. 반대로 트래픽이 거의 없고
CPU 만 계속 쓰는 워크로드라면 버스터블 제약이 먼저 걸립니다.

요금이 매달 똑같이 찍힌다는 것도 실제 이점입니다. 사이드 프로젝트에서 청구서가 튀는 사고는
대부분 트래픽에서 나오는데, 번들 안에 있으면 그 사고가 안 납니다.

## 정리

Lightsail 은 인스턴스·SSD·데이터 전송량을 한 값에 묶은 요금제입니다.
서울 리전 기준 가장 싼 번들이 월 4,803원이고, 여기에 이미 월 1TB 전송이 들어 있습니다.

세 가지만 남기면 됩니다.

### 싼 이유는 **전송량이 묶여 있어서**입니다. 같은 4TB 를 EC2 로 내보내면 그것만 70만원입니다.

### **IPv6-only 번들이 더 쌉니다.** 차액은 AWS 의 퍼블릭 IPv4 요금과 거의 같습니다.

### 대가는 **버스터블 CPU 와 요금제 변경의 번거로움**입니다. 사양을 올리려면 스냅샷으로 다시 만들어야 합니다.

트래픽이 나가는 서비스면 Lightsail 이 압도적으로 쌉니다.
CPU 를 계속 쓰거나 구성을 자주 바꿀 거라면 처음부터 EC2 가 맞습니다.

## 참고 출처

- [[Amazon Web Services] AWS 공식 가격 목록 — Amazon Lightsail (ap-northeast-2)](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonLightsail/current/region_index.json)
- [[Amazon Web Services] AWS 공식 가격 목록 — AWS Data Transfer (서울 아웃바운드 단가)](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AWSDataTransfer/current/index.json)
- [[Amazon Web Services] Monitor Lightsail instance performance with metrics — 버스트 존과 버스트 용량 지표 (본문 도표 출처)](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-health-metrics.html)
- [[Amazon Web Services] Lightsail 리소스를 Amazon EC2 로 내보내기](https://docs.aws.amazon.com/ko_kr/lightsail/latest/userguide/amazon-lightsail-faq-export-to-ec2.html)
- [[Amazon Web Services] Amazon VPC Pricing — 퍼블릭 IPv4 시간당 단가](https://aws.amazon.com/vpc/pricing/)
- [[NAVER Cloud Platform] 서비스별 요금안내 · [NHN Cloud] 요금 (국내 클라우드 비교 수치)](https://www.ncloud.com/charge/price/ko)
- 환율: 1달러 ≈ 1,400원 기준 환산
- 조회 시점: 2026-08-08 · 서울 리전 · Linux · 월 730시간 기준
