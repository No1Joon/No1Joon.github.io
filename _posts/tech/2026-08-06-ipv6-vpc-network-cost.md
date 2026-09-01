---
title: "IPv4 주소 30개에 연 350만원 — IPv6-Only VPC 계산기"
description: "퍼블릭 IPv4 과금·NAT 게이트웨이·이그레스로 갈리는 클라우드 네트워크 청구서를 계산하고, IPv6-Mostly 전환의 손익을 따집니다"
date: 2026-08-06
category: Tech
subcategory: Explainer
tags: [ipv6, vpc, nat-gateway, cloud-cost, networking]
image: /assets/og/2026-08-06-ipv6-vpc-network-cost.png
---

클라우드 청구서에서 컴퓨트와 스토리지는 다들 한 번쯤 뜯어봅니다. 그런데 네트워크 줄은 이상하게 잘 안 열립니다.
금액이 작아서가 아니라 **무엇 때문에 붙었는지 청구서만 봐서는 알 수 없기** 때문입니다.

2024년 2월부터 AWS는 퍼블릭 IPv4 주소 하나에 시간당 0.005달러를 받습니다. 인스턴스에 붙어 있든,
할당만 해두고 놀고 있든 똑같습니다. 그리고 2026년 3월, 구글 측정 기준으로 IPv6가 처음 인터넷 접속의
절반을 넘었습니다. 주소가 과금 단위가 된 것과 IPv6가 과반이 된 것 — 두 사건은 같은 이야기의 앞뒤입니다.

## 주소가 월세가 된 순간

![주소가 과금 단위가 된 네트워크 개념 컷](/assets/images/tech/ipv6-vpc-network-cost/01-agy-hero.webp)
*주소가 과금 단위가 된 네트워크 개념 컷 — 출처: 자가 생성*

IPv4 주소는 32비트, 이론상 약 43억 개입니다. IANA가 최상위 블록을 다 나눠준 게 2011년 2월이니
공식적으로 바닥난 지 15년이 지났습니다. 그동안 클라우드 사업자들은 유통 시장에서 주소를 사들여
버텼고, 그 원가를 요금에 반영하지 않았습니다. 무료였다는 뜻이 아니라 **다른 요금에 섞여 있었다**는 뜻입니다.

2024년 2월 1일부터 AWS가 그 원가를 분리해 청구하기 시작했습니다. 퍼블릭 IPv4 주소 1개당
**시간당 0.005달러**, 730시간을 곱하면 **월 3.65달러**(약 5,100원), 연 43.80달러입니다.
Elastic IP를 할당만 해놓고 아무 데도 안 붙인 유휴 주소에도 같은 단가가 붙습니다.

한 개는 껌값입니다. 문제는 개수가 조용히 늘어난다는 점이에요.
NAT 게이트웨이마다 하나, 인터넷 페이싱 로드밸런서는 가용 영역마다 하나, 퍼블릭 서브넷의 인스턴스마다
하나 — 3-AZ 표준 구성 하나만 세워도 주소가 스무 개를 넘어갑니다. 계정이 열 개면 그게 열 배가 되고요.

### 왜 이 줄이 유독 안 읽히나

퍼블릭 IPv4 요금은 EC2·ELB·NAT 게이트웨이 어느 서비스에도 속하지 않습니다.
청구서에서 **PublicIPv4:InUseAddress** 같은 사용 유형으로 흩어져 찍히기 때문에, 서비스별로 묶어 보는
대시보드에서는 **어느 팀 것인지 귀속되지 않은 채 남습니다.** AWS가 Public IP Insights라는 별도 도구를
따로 내놓은 이유이기도 합니다.

FinOps Foundation의 2026년 조사(응답자 1,192명, 연간 클라우드 지출 830억 달러 규모)에서 실무자들은
"눈에 띄는 큰 낭비는 이미 다 잡았고, 이제 작고 잡기 어려운 절감만 남았다"고 답했습니다.
네트워크 계층이 바로 그 잡기 어려운 쪽입니다.

## IPv6가 인터넷 절반을 넘긴 해

![주소 고갈에서 IPv6 과반까지 연표](/assets/images/tech/ipv6-vpc-network-cost/02-chart-ipv6.webp)
*주소 고갈에서 IPv6 과반까지 연표 — 출처: 자가 생성*

2026년 3월 28일, 구글 서비스에 IPv6로 접속한 사용자 비율이 **50.10%** 를 기록했습니다.
구글이 이 수치를 재기 시작한 지 18년 만이고, 2025년 6월 21일의 49.56%에서 아깝게 미끄러진 뒤
아홉 달 만이었습니다.

다만 이 숫자는 **하루짜리 봉우리**였습니다. 이후로는 45~50% 사이를 오가고 있고, 다른 측정치는 더 낮습니다.
APNIC Labs는 같은 시기 IPv6 지원 네트워크 비율을 약 43%로, Cloudflare Radar는 IPv6로 오가는
HTTP 요청을 40.1%로 잡습니다. 측정 방식이 달라서 생기는 차이인데, 이 셋을 묶어 보면
**실제 IPv6 도달률은 대략 40~50% 구간**이라고 읽는 게 맞습니다.

국가별 편차는 그 평균보다 훨씬 큽니다.

| 구간 | 국가 | IPv6 비율 |
| :--- | :--- | :--- |
| 선두 | 프랑스 | <mark>73%</mark> |
| 선두 | 인도 | 72% |
| 선두 | 사우디아라비아 | 65% |
| 후발 | 이탈리아 | 17% |
| 후발 | 스페인 | 10% |
| 후발 | 이집트 | 4% |

여기서 실무자가 봐야 할 숫자는 전 세계 평균이 아닙니다. **내 서비스 이용자가 어느 나라에서 오는가**,
그리고 **내가 쓰는 클라우드 리전이 IPv6를 어디까지 지원하는가** 둘입니다. 인바운드는 아직 IPv4를
버릴 수 없지만, 아웃바운드와 내부 통신은 사정이 완전히 다릅니다. 비용이 갈리는 지점도 거기예요.

한편 미국 연방정부는 이 전환을 이미 강제로 밀고 있습니다. 백악관 예산관리국의 OMB M-21-07은
연방 네트워크 자산의 **80%를 2025 회계연도까지 IPv6-only 환경으로** 옮기도록 못 박았고, 기한을 놓친
기관에는 2026년 60%, 2027년 80%, 2028년 100%라는 새 목표가 다시 걸렸습니다.
공공 조달에 들어가는 서비스라면 이건 비용 문제가 아니라 요건 문제가 됩니다.

## 네트워크 청구서에서 안 읽히는 세 줄

![퍼블릭 IPv4 주소 1개의 월 비용](/assets/images/tech/ipv6-vpc-network-cost/03-chart-ipv4.webp)
*퍼블릭 IPv4 주소 1개의 월 비용 — 출처: 자가 생성*

주소 시장에서 IPv4 블록 임대 시세는 2026년 기준 /24~/22 크기에서 IP 하나당 **월 0.38~0.50달러**입니다.
같은 주소 하나를 클라우드에서 빌리면 3.65달러고요. 여덟 배 가까운 차이는 폭리라기보다,
주소 자체가 아니라 **주소에 딸린 운영과 회수 부담까지 얹힌 값**이라고 보는 편이 정확합니다.
어느 쪽으로 읽든 결론은 같습니다 — 안 쓰는 게 제일 쌉니다.

네트워크 청구서에서 잘 안 읽히는 줄은 세 개고, IPv6로 지워지는 정도가 각각 다릅니다.

| 항목 | 언제 붙나 | IPv6로 전환하면 |
| :--- | :--- | :--- |
| 퍼블릭 IPv4 주소 | 붙어 있든 놀든 시간당 | <mark>사라진다</mark> — IPv6 주소는 무료 |
| NAT 게이트웨이 시간 요금 | 게이트웨이가 떠 있는 동안 계속 | <mark>사라진다</mark> — 아웃바운드 전용 게이트웨이는 무료 |
| NAT 게이트웨이 데이터 처리 | 통과하는 GB마다 | <mark>사라진다</mark> — IPv6 경로엔 처리 요금이 없다 |
| 인터넷 이그레스 전송 | 밖으로 나가는 GB마다 | **그대로 남는다** — 프로토콜과 무관 |

마지막 줄이 중요합니다. IPv6는 **주소와 변환 장치에 붙는 비용**을 지우지, 나가는 트래픽 요금을 깎아주지
않습니다. 이그레스는 AWS가 첫 10TB 구간 GB당 0.09달러, Azure가 0.087달러, GCP가 첫 1TB에 0.12달러로
프로토콜과 상관없이 그대로 붙습니다. IPv6 전환을 이그레스 절감 명목으로 결재 올리면 나중에 숫자가 안 맞아요.

### NAT 게이트웨이의 진짜 원가

NAT 게이트웨이는 시간당 0.045달러, 월 32.85달러입니다. 여기에 게이트웨이가 쓰는 퍼블릭 IPv4 주소값
3.65달러가 더 붙어 **한 대에 월 36.50달러**, 3-AZ 이중화를 하면 그냥 떠 있는 것만으로 월 109.50달러입니다.
데이터 처리 요금 GB당 0.045달러는 여기에 별도로 얹힙니다.

IPv6 아웃바운드에는 이 장치가 아예 필요 없습니다. **아웃바운드 전용 인터넷 게이트웨이**(egress-only
internet gateway)가 대신 서고, AWS 공식 문서는 이 게이트웨이에 대해 "요금이 없다"고 명시합니다.
안에서 밖으로는 나가고 밖에서 안으로는 못 들어오는 동작은 NAT 게이트웨이와 같은데, 시간 요금도
데이터 처리 요금도 붙지 않습니다.

> 한 줄 요약: IPv6가 지우는 건 주소값과 변환 장치값이지 트래픽값이 아니다.

## IPv6-Only 서브넷이 실제로 지우는 것

![AWS 공식 IPv6-only 서브넷 레퍼런스 아키텍처](/assets/images/tech/ipv6-vpc-network-cost/04-diagram-aws-ipv6only-subnet.webp)
*AWS 공식 IPv6-only 서브넷 레퍼런스 아키텍처 — 출처: Amazon Web Services*

AWS는 2021년 11월부터 듀얼스택 VPC 안에 **IPv6-only 서브넷**을 만들 수 있게 했습니다.
Nitro 기반 EC2 인스턴스는 IPv4 주소를 아예 받지 않고 IPv6 주소만 가진 채 뜹니다.

이 구조가 지우는 건 비용만이 아닙니다.

### 사설 IPv4 대역이 모자라서 생기는 문제

사내 IPv4 대역은 유한합니다. 10.0.0.0/8을 팀별·계정별·리전별로 쪼개다 보면 언젠가 겹치고,
겹치면 VPC 피어링도 Transit Gateway 연결도 막힙니다. 인수합병으로 다른 회사 네트워크가 들어오면
그 순간 사설 대역 충돌이 터지죠. 쿠버네티스는 이 문제를 가장 먼저 만납니다 —
VPC CNI가 파드마다 VPC 대역의 IPv4 주소를 하나씩 떼어주기 때문에, 노드를 늘리기 전에
**서브넷 주소가 먼저 바닥납니다.**

IPv6-only EKS 클러스터에서는 파드와 서비스가 IPv6 주소를 받으면서 이 한계가 사라집니다.
파드 밀도를 제한하는 건 주소가 아니라 CPU와 메모리가 되고요. AWS는 여기에 더해 2024년 8월부터
인터넷으로 광고되지 않는 **프라이빗 IPv6 주소**(ULA·GUA)를 VPC에 붙일 수 있게 했습니다.
"IPv6는 다 공인 주소라 위험하다"는 오래된 반론에 대한 답이 이걸로 나온 셈입니다.

### 세 가지 서브넷이 한 VPC에 공존한다

전부 갈아엎을 필요는 없습니다. 하나의 듀얼스택 VPC 안에 IPv6-only 서브넷과 듀얼스택 서브넷,
IPv4-only 서브넷이 나란히 존재할 수 있습니다.
가용 영역마다 필요한 조합을 고르고, 옮길 수 있는 워크로드부터 IPv6-only 서브넷으로 내리면 됩니다.

제약은 하나뿐입니다 — **IPv6-only 서브넷의 리소스는 IPv4-only 서브넷의 리소스와 직접 통신할 수
없습니다.** 그래서 다음 이야기가 필요합니다.

## IPv4로만 사는 서비스는 어떻게 부르나

![IPv4-only 엔드포인트를 dig로 확인한 세션](/assets/images/tech/ipv6-vpc-network-cost/05-term-dig-aaaa.webp)
*IPv4-only 엔드포인트를 dig로 확인한 세션 — 출처: 자가 생성*

IPv6만 가진 인스턴스가 IPv4로만 서비스되는 외부 API를 불러야 하는 상황은 반드시 옵니다.
얼마나 흔한지는 dig 한 줄로 확인됩니다. **www.google.com**은 AAAA 레코드로 IPv6 주소를 돌려주는데,
AWS 자신의 **checkip.amazonaws.com**은 AAAA를 물어도 CNAME만 나오고 **IPv6 주소가 없습니다.**
A 레코드로는 IPv4 주소가 멀쩡히 나오고요.

이 간극을 메우는 게 **DNS64**와 **NAT64**입니다.

### 둘이 하는 일

DNS64는 서브넷 설정입니다. IPv6-only 서브넷의 인스턴스가 DNS를 물었을 때 AAAA 레코드가 없으면,
Route 53 Resolver가 A 레코드의 IPv4 주소를 가져다 **64:ff9b::/96 이라는 예약 프리픽스 뒤에 붙여
가짜 IPv6 주소를 합성**해 돌려줍니다. RFC 6052에 정의된 방식이에요.

NAT64는 그 가짜 주소로 온 패킷을 받아 진짜 IPv4로 바꿔 내보내는 쪽입니다. 별도 기능을 켜는 게 아니라
**NAT 게이트웨이에 이미 들어 있습니다.** 라우트 테이블에서 **64:ff9b::/96** 을 NAT 게이트웨이로 보내면 끝입니다.

여기서 비용 구조가 갈립니다. IPv6-only로 내려도 NAT 게이트웨이가 완전히 사라지지는 않아요.
다만 **모든 아웃바운드가 아니라 IPv4-only 목적지로 가는 트래픽만** 통과하므로, 3-AZ에 세 대를 두는 대신
한 대로 줄이거나 공유 네트워킹 계정에 몰아둘 수 있습니다. 지워지는 게 아니라 **작아지는** 겁니다.

> IPv6 로 옮겨도 NAT 게이트웨이는 남습니다. IPv4-only 목적지로 가는 트래픽만 지나가므로 대수를 줄일 수 있습니다.

## 3-AZ 표준 구성으로 계산해 본 연간 고정비

![3-AZ 구성에서 아키텍처별 연간 네트워크 고정비](/assets/images/tech/ipv6-vpc-network-cost/06-chart.webp)
*3-AZ 구성에서 아키텍처별 연간 네트워크 고정비 — 출처: 자가 생성*

AWS 공시 단가로 흔한 구성 하나를 세워 계산해 봤습니다. 전제는 us-east-1, 가용 영역 3개,
월 730시간, **데이터 처리와 이그레스 전송량은 뺀 고정비만** 입니다.

| 구성 | 퍼블릭 IPv4 주소 | NAT 게이트웨이 | 월 고정비 |
| :--- | :--- | :--- | :--- |
| 듀얼스택 관행 | 30개 | 3대 | 208.05달러 |
| IPv6-Mostly | 6개 | 3대 | 120.45달러 |
| IPv6-Only | <mark>4개</mark> | <mark>1대</mark> | <mark>47.45달러</mark> |

**듀얼스택 관행**은 NAT 게이트웨이 3대에 각각 Elastic IP, 로드밸런서 노드에 AZ당 하나, 나머지는
퍼블릭 서브넷에 흩어진 인스턴스와 유휴 주소입니다. 특별히 방만한 구성이 아니라 기본값대로 만들면
이렇게 됩니다. 연 2,496달러, 약 350만원이 오로지 주소값과 게이트웨이 대여료로 나갑니다.

**IPv6-Mostly**는 내부 워커와 배치 노드를 IPv6-only 서브넷으로 내리고, IPv4 주소는 NAT 게이트웨이와
인터넷 페이싱 로드밸런서에만 남긴 구성입니다. 주소가 30개에서 6개로 줄면서 월 87달러가 빠집니다.
애플리케이션 코드는 한 줄도 안 건드리고 서브넷 배치만 바꿔서 나오는 절감이에요.

**IPv6-Only**는 아웃바운드를 아웃바운드 전용 게이트웨이로 돌리고, NAT64용 NAT 게이트웨이 한 대만
공유로 남긴 구성입니다. 로드밸런서는 여전히 듀얼스택이라 IPv4 주소 3개가 남습니다 —
이용자의 절반 이상이 아직 IPv4로 들어오니 인바운드를 IPv6로만 열 수는 없습니다.
연 569달러, 약 80만원. 처음 구성 대비 **77%가 줄어듭니다.**

계정이 하나일 때 이야기입니다. 조직 단위로 계정이 서른 개면 같은 비율이 그대로 곱해집니다.

> 이 절감은 트래픽을 줄여서가 아니라 서브넷 배치만 바꿔서 나옵니다.

## 아직 IPv4를 붙잡고 있는 것들

![IPv4에서 IPv6로 넘어가는 전환 순서 개념 컷](/assets/images/tech/ipv6-vpc-network-cost/07-agy-migration.webp)
*IPv4에서 IPv6로 넘어가는 전환 순서 개념 컷 — 출처: 자가 생성*

숫자만 보면 지금 당장 옮기지 않을 이유가 없어 보입니다. 실제로는 걸리는 자리가 있습니다.

| 걸리는 자리 | 내용 | 우회 |
| :--- | :--- | :--- |
| IPv6 미지원 서비스 | 일부 관리형 서비스와 API 엔드포인트가 아직 IPv4 전용 | DNS64·NAT64로 통과 |
| EKS 프로토콜 확정 | **ipFamily: IPv6** 는 **클러스터 생성 시에만** 지정, 이후 변경 불가 | 새 클러스터를 만들어 옮김 |
| EKS 노드 제약 | Windows 파드 미지원, Nitro 또는 Fargate 노드만 가능, Outposts 미지원 | 해당 워크로드는 듀얼스택에 남김 |
| 하드코딩된 IPv4 | 설정 파일·보안 그룹·방화벽 정책에 박힌 32비트 주소와 정규식 | 코드 감사가 실제 작업량의 대부분 |
| 관측·로깅 | VPC 플로우 로그·모니터링 쿼리가 IPv4 필드를 전제 | 대시보드와 알람 쿼리 동시 개편 |

### 코드에 박힌 IPv4 가정이 가장 오래 걸린다

관리형 서비스의 IPv6 지원은 매달 늘고 있습니다. AWS만 해도 2025년에 AppConfig·Health·Control Tower가,
2026년 1월에는 RDS 서비스 API용 VPC 엔드포인트가 IPv6를 받았습니다. 시간이 해결하는 쪽입니다.

시간이 해결해주지 않는 건 **우리 코드 안에 박힌 IPv4 가정**입니다.
주소를 담는 컬럼이 **VARCHAR(15)** 로 잡혀 있거나, 로그 파서가 점 세 개짜리 정규식으로 IP를 뽑거나,
보안 그룹 규칙이 CIDR로만 쓰여 있거나 — 이런 자리는 전환 계획서에 안 적히는데 막상 붙으면 제일 오래 걸립니다.

### 옮기는 순서

전면 전환은 실패합니다. 위험이 낮고 절감이 바로 보이는 쪽부터 잡는 게 맞습니다.

① 계정별로 퍼블릭 IPv4 주소를 세고 **유휴 Elastic IP부터 회수**합니다. 코드 변경 없이 즉시 줄어듭니다.
② VPC에 IPv6 CIDR을 붙여 **듀얼스택으로 만듭니다.** 기존 IPv4 경로는 그대로 살아 있어 되돌리기 쉽습니다.
③ 외부에서 들어올 일이 없는 **배치 잡·워커·빌드 러너**를 IPv6-only 서브넷으로 내립니다.
④ DNS64를 켜고 **64:ff9b::/96** 라우트를 NAT 게이트웨이로 보내 IPv4-only 목적지를 뚫습니다.
⑤ 남은 NAT 게이트웨이 수를 줄이고, 아웃바운드 전용 게이트웨이로 IPv6 경로를 분리합니다.
⑥ 인터넷 페이싱 로드밸런서를 듀얼스택으로 바꿔 IPv6 이용자를 받습니다. 여기서 IPv4는 마지막까지 남습니다.

①번만 해도 계정에 따라 월 수십 달러가 즉시 빠집니다. 대부분의 조직은 여기서부터 시작하면 됩니다.

## 정리

퍼블릭 IPv4 주소가 과금 대상이 되면서 네트워크 설계는 아키텍처 취향의 문제에서 **비용 결정**으로 넘어왔습니다.
주소 하나가 월 3.65달러라는 사실은, 서브넷을 어떻게 나눌지가 곧 청구서를 어떻게 쓸지라는 뜻입니다.

세 가지만 남겨두면 충분합니다.

### IPv6가 지우는 건 **주소값과 NAT 게이트웨이값**이지 이그레스 전송료가 아닙니다.

### 착지점은 IPv6-Only가 아니라 **IPv6-Mostly** 인 경우가 많습니다. 인바운드는 한참 더 IPv4로 옵니다.

### 가장 빨리 회수되는 건 아키텍처 전환이 아니라 **유휴 Elastic IP 회수**입니다. 오늘 셀 수 있습니다.

인터넷의 절반이 이미 넘어간 프로토콜을 사내 VPC만 끝까지 안 쓸 이유는 별로 없습니다.
다만 순서는 지켜야 하고, 그 순서의 첫 칸은 코드가 아니라 **세는 일**입니다.

## 참고 출처

- [[Amazon Web Services] Amazon VPC Pricing — 퍼블릭 IPv4·NAT 게이트웨이 공시 단가](https://aws.amazon.com/vpc/pricing/)
- [[Amazon Web Services] Amazon EC2 On-Demand Pricing — 인터넷 이그레스 전송 단가](https://aws.amazon.com/ec2/pricing/on-demand/)
- [[Microsoft Azure] Bandwidth pricing — 이그레스 단가 대조](https://azure.microsoft.com/en-us/pricing/details/bandwidth/)
- [[Google Cloud] VPC network pricing — 이그레스 단가 대조](https://cloud.google.com/vpc/network-pricing)
- [[Amazon Web Services] Enable outbound IPv6 traffic using an egress-only internet gateway — 요금 없음 명시](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html)
- [[Amazon Web Services] DNS64 and NAT64 — 64:ff9b::/96 합성 방식](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-nat64-dns64.html)
- [[Amazon Web Services] Dual Stack and IPv6-only Amazon VPC Reference Architectures (본문 아키텍처 도면 출처)](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/IPv6-reference-architectures-for-AWS-and-hybrid-networks-ra.pdf)
- [[Amazon Web Services] AWS announces private IPv6 addressing for VPCs and subnets (2024-08-08)](https://aws.amazon.com/about-aws/whats-new/2024/08/aws-private-ipv6-addressing-vpcs-subnets/)
- [[Amazon Web Services] Running IPv6 EKS Clusters — 클러스터 생성 시 확정·노드 제약](https://docs.aws.amazon.com/eks/latest/best-practices/ipv6.html)
- [[Internet Society Pulse] 18 Years Later, IPv6 Reaches Majority — 2026-03-28 50.10% 기록](https://pulse.internetsociety.org/en/blog/2026/04/18-years-later-ipv6-reaches-majority/)
- [[APNIC Blog] Google hits 50% IPv6 (2026-04-28) — APNIC Labs 측정치 대조](https://blog.apnic.net/2026/04/28/google-hits-50-ipv6/)
- [[The Register] Google: IPv6 carried half of internet traffic for one day — Cloudflare Radar 40.1% 대조](https://www.theregister.com/2026/04/17/ipv6_50_percent_google/)
- [[FinOps Foundation] State of FinOps 2026 — 응답자 1,192명·연 830억 달러 규모 조사](https://data.finops.org/)
- [[The White House OMB] M-21-07, Completing the Transition to Internet Protocol Version 6](https://www.whitehouse.gov/wp-content/uploads/2020/11/M-21-07.pdf)
- 환율: 1달러 ≈ 1,400원 기준 환산
