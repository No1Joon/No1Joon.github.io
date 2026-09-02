---
title: "RAM에 대하여 (7) — 메모리를 GPU 옆에서 떼어내는 빛, CPO"
description: "SK하이닉스 연구진이 Nature Electronics 에 낸 논문을 따라, 구리 배선의 한계와 100Tb/s·100W 라는 목표 숫자를 정리합니다"
date: 2026-08-23
category: Tech
subcategory: Explainer
tags: [cpo, optical-interconnect, sk-hynix, nature-electronics, memory]
image: /assets/og/2026-08-23-ram-07-cpo-optical-interconnect.png
---

HBM 옆에 낸드를 한 층 더 쌓는 이야기가 메모리 용량을 늘리는 쪽이었다면, 이번에는 그 메모리를 GPU 옆에서 아예 떼어내자는 이야기입니다.

SK하이닉스 연구진이 미국·싱가포르 대학들과 함께 쓴 논문이 8월 19일 **Nature Electronics** 에 실렸습니다. 주제는 칩과 칩을 구리 배선 대신 빛으로 잇는 기술입니다.

메모리를 만드는 회사가 배선 기술 로드맵을 학술지에 낸다는 게 좀 낯설게 들립니다. 논문을 읽어 보면 그 이유가 분명합니다.

[RAM에 대하여 (6) — HBM 옆에 낸드를 쌓는 새 계층, HBF](/posts/ram-06-hbf/)

![논문에 참여한 SK하이닉스 연구진, 뒤 화면은 Nature Electronics 지면](/assets/images/tech/ram-07-cpo-optical-interconnect/01-hero-skhynix-nature.webp)
*논문에 참여한 SK하이닉스 연구진, 뒤 화면은 Nature Electronics 지면 — 출처: SK hynix Newsroom*

## 어떤 논문인가

![논문 Fig. 1c — 칩 안(마이크로미터)부터 랙 사이(킬로미터)까지 거리 스케일 세 단](/assets/images/tech/ram-07-cpo-optical-interconnect/02-paper-fig1c-scales.webp)
*논문 Fig. 1c — 칩 안(마이크로미터)부터 랙 사이(킬로미터)까지 거리 스케일 세 단 — 출처: Nature Electronics (Fig. 1c 부분 크롭)*

논문이 다루는 범위가 위 그림 한 장에 들어 있습니다. 칩 안 몇 마이크로미터부터 랙과 랙 사이 킬로미터까지, 거리 구간마다 무엇으로 잇는 게 맞는지를 한 판에 놓고 따집니다.

| 항목 | 내용 |
|---|---|
| 제목 | Co-packaged optics for high-performance computing and artificial intelligence |
| 저널·게재일 | <mark>Nature Electronics · 2026-08-19</mark> |
| 권·쪽 | 9권 853~867쪽 |
| 유형 | **Review Article** |
| 교신저자 | Seunghoon Hong · Kyusang Lee |

교신저자는 SK하이닉스에서 AI 인프라를 맡고 있는 홍승훈 팀장과 미국 버지니아대(University of Virginia) 전기컴퓨터공학과 이규상 교수입니다. 저자는 모두 12명이고 SK하이닉스와 University of Virginia 외에 University of Illinois Urbana-Champaign, MIT, Nanyang Technological University, 연세대가 참여했습니다.

### 먼저 짚을 것 — 이건 실험 논문이 아닙니다

유형이 **Review Article** 입니다. 새로 만든 칩을 측정해서 성능을 보고한 글이 아니라, 흩어져 있던 기존 연구를 정리하고 앞으로 어디로 가야 하는지 방향을 제시한 글입니다. 그래서 뒤에 나오는 숫자들은 **달성한 값이 아니라 달성해야 할 목표값**입니다.

이 구분을 흐리면 기사 제목만 읽고 이미 되는 기술이라고 오해하게 됩니다. 아직 상용 제품은 없습니다.

*주: 논문 본문은 유료 구독이라, 이 글은 공개된 초록과 SK하이닉스가 공식 공개한 자료를 근거로 정리했습니다.*

## 연산은 8.8배씩 뛰는데 선은 1.4배입니다

![AI 연산과 인터커넥트의 성장률 — 논문 재구성 도표](/assets/images/tech/ram-07-cpo-optical-interconnect/03-official-growth-rate.webp)
*AI 연산과 인터커넥트의 성장률 — 논문 재구성 도표 — 출처: SK hynix Newsroom*

논문이 잡은 문제는 하나입니다. 계산하는 속도는 미친 듯이 빨라졌는데, 계산할 데이터를 **옮기는** 속도가 못 따라온다는 것입니다.

SK하이닉스가 논문 내용을 재구성해 공개한 도표를 보면 2년마다 늘어나는 배수가 이렇게 갈립니다.

| 구분 | 2년마다 |
|---|---|
| AI 모델 규모 | <mark>8.8배</mark> |
| 하드웨어 연산 성능 | 3.0배 |
| DRAM | 1.6배 |
| **인터커넥트 대역폭** | **1.4배** |

여기서 **인터커넥트(interconnect)** 는 칩과 칩, 서버와 서버를 잇는 통로를 말합니다. 도로에 비유하지 않고 그대로 쓰자면, 데이터가 지나다니는 배선과 그 배선을 굴리는 회로 전체입니다.

모델은 8.8배씩 커지는데 통로는 1.4배씩만 넓어집니다. 이 격차가 계속 벌어지면 GPU 를 아무리 많이 사도 절반은 데이터를 기다리며 놀게 됩니다. 논문은 이 지점을 **대역폭 월(bandwidth wall)**, 그러니까 대역폭이 만드는 벽이라고 부릅니다.

### 구리가 안 되는 이유는 물리에 있습니다

초록에서 저자들은 전기 배선의 한계를 세 가지로 적었습니다. 저항 때문에 신호가 열로 새고, 배선이 축전기처럼 굴어서 신호가 느려지고, 주파수가 높아질수록 파형이 뭉개진다는 것입니다.

속도를 올릴수록 이 셋이 같이 나빠집니다. 그래서 요즘 고속 배선에는 뭉개진 파형을 되살리는 보정 회로가 붙는데, 이 회로가 다시 전력을 먹고 지연을 더합니다. 문제를 푸는 방법이 문제를 키우는 구조입니다.

### 그런데 빛이 항상 이기는 건 아닙니다

![논문 Fig. 1b — 거리에 따른 전기(주황)와 빛(파랑)의 효율](/assets/images/tech/ram-07-cpo-optical-interconnect/04-paper-fig1b-distance.webp)
*논문 Fig. 1b — 거리에 따른 전기(주황)와 빛(파랑)의 효율 — 출처: Nature Electronics (Fig. 1b 부분 크롭)*

논문에서 가장 오래 들여다볼 만한 그림입니다. 가로축은 신호가 가야 하는 최대 거리, 세로축은 대역폭 밀도와 에너지 효율을 곱한 값입니다. 위로 갈수록 좋습니다.

주황색 전기 쪽을 보면 패키지 안 1mm 남짓 거리에서는 값이 압도적으로 높습니다. HBM 과 **UCIe Advanced** 가 그 위쪽에 몰려 있습니다. 그런데 거리가 늘어날수록 이 선이 가파르게 떨어집니다.

파란색 빛 쪽은 반대입니다. 짧은 거리에서는 전기에 한참 못 미치는데, 거리가 늘어도 거의 안 떨어집니다. 두 선이 만나는 지점이 대략 **1m 부근**이고, 논문은 그 근처를 보드 위 광 백플레인이 차지한다고 표시해 뒀습니다.

그래서 결론이 전기를 다 걷어내자가 아닙니다. 1m 안쪽은 여전히 전기가 유리하고, 그 바깥부터 빛이 유리합니다. CPO 가 노리는 건 **그 경계선을 칩 쪽으로 더 당기는** 일입니다.

## 구리 배선을 빛으로 바꾸면

![기존 방식과 CPO 방식의 비교 — 논문 재구성 도표](/assets/images/tech/ram-07-cpo-optical-interconnect/05-official-cpo-vs-legacy.webp)
*기존 방식과 CPO 방식의 비교 — 논문 재구성 도표 — 출처: SK hynix Newsroom*

논문이 내놓은 답이 **CPO(Co-Packaged Optics)** 입니다. 우리말로는 코패키지 옵틱스, 빛을 다루는 부품을 연산 칩과 **같은 패키지 안에** 넣는 방식입니다.

지금은 이렇게 돌아갑니다. 연산 칩(SoC)이 전기 신호를 만들면, 그 신호가 기판 위 구리 배선을 한참 달려 보드 가장자리의 광 엔진까지 갑니다. 거기서 비로소 빛으로 바뀌어 광섬유를 탑니다. 전기로 달리는 그 구간이 길수록 손실과 전력이 붙습니다.

CPO 는 빛으로 바꾸는 부품, 즉 **광 트랜시버(TRx)** 를 연산 칩 바로 옆으로 끌고 옵니다. 둘 사이를 잇는 판이 **인터포저(interposer)** 인데, 칩과 기판 사이에 깔아 배선을 촘촘하게 뽑아 주는 중간 판입니다.

> 전기로 달리는 거리를 최대한 짧게 자르고, 나머지는 전부 빛으로 보냅니다

논문은 이 판을 세 부분으로 나눠 분석합니다.

- 전기 서브시스템 — 드라이버, 수신기, 신호를 한 줄로 펴는 SerDes, 클록, 전력 관리
- 전기-광 변환부 — 전기를 빛으로 바꾸는 변조기(modulator), 빛을 전기로 되돌리는 광검출기(photodetector)
- 광 전송망 — 빛이 지나는 길인 도파로(waveguide), 광섬유, 커플러, 스위치, 여러 파장을 한 가닥에 겹쳐 싣는 다중화 구조

이 셋 중 하나만 좋아서는 소용이 없다는 게 논문의 관점입니다. 대역폭·전력·지연은 세 부분이 함께 정하는 값이기 때문입니다.

## 숫자 세 개 — 100 Tb/s · 1 pJ/bit · 10 ns

![SK하이닉스 로고](/assets/images/tech/ram-07-cpo-optical-interconnect/06-logo-skhynix.webp)
*SK하이닉스 로고 — 출처: SK hynix*

논문이 차세대 AI 인프라의 조건으로 못 박은 목표값이 셋입니다. 다시 말하지만 **지금 되는 값이 아니라 가야 할 값**입니다.

| 목표 | 값 |
|---|---|
| 노드당 대역폭 | <mark>100 Tb/s 이상</mark> |
| 비트당 에너지 | 1 pJ 미만 |
| 칩 간 지연 | 10 ns 미만 |

감이 잘 안 오는 단위라 하나씩 풀어 보겠습니다.

**100 Tb/s** 는 초당 100조 비트, 바이트로 고치면 초당 12.5테라바이트입니다. 25GB 짜리 영화 500편을 1초에 옮기는 양이 서버 한 대에서 나와야 한다는 뜻입니다.

**1 pJ/bit** 의 pJ(피코줄)은 1조분의 1 줄입니다. 비트 하나 옮기는 데 쓰는 에너지인데, 위의 두 값을 곱하면 의미가 분명해집니다. 100조 비트를 비트당 1 pJ 로 옮기면 초당 100줄, 곧 **100W** 입니다. 선풍기 두 대 정도 전력으로 영화 500편어치를 매초 밀어 넣겠다는 목표입니다.

**10 ns** 는 1억분의 1초입니다. 빛이 광섬유 안에서 10ns 동안 가는 거리가 대략 2m 니까, 랙 안에서 칩과 칩이 오가는 거리 정도는 지연 없이 붙어 있는 것처럼 쓰겠다는 이야기입니다.

### 어떻게 거기까지 가나

논문은 집적 방식을 세 단계로 그립니다. 뒤로 갈수록 신호가 다니는 거리가 짧아집니다.

| 단계 | 방식 |
|---|---|
| 2D | 칩과 광 엔진을 **같은 기판에 나란히** |
| 2.5D | 사이에 인터포저를 깔아 촘촘하게 |
| 3D | <mark>위로 쌓는 이종 집적</mark> |

3D 쪽의 **이종 집적(heterogeneous integration)** 은 성질이 다른 칩들, 여기서는 전자 회로와 광 회로를 한 덩어리로 수직으로 붙이는 방식입니다. 각각 가장 잘 만들 수 있는 공정으로 따로 만든 뒤 합치는 게 요점입니다.

## 메모리를 GPU 옆에서 떼어냅니다

![옵틱스 중심 아키텍처 — XPU 풀과 메모리 풀](/assets/images/tech/ram-07-cpo-optical-interconnect/07-official-optics-centric.webp)
*옵틱스 중심 아키텍처 — XPU 풀과 메모리 풀 — 출처: SK hynix Newsroom*

메모리 회사가 이 논문을 쓴 이유가 여기 있습니다. 논문이 가장 멀리 내다본 그림은 스위치나 네트워크가 아니라 **메모리 인터페이스까지 빛으로 바꾸는** 것입니다.

지금 구조는 GPU 하나에 HBM 몇 덩이가 딱 붙어 있는 모양입니다. 붙어 있으니 빠르지만, 그 GPU 가 쓰지 않는 용량은 옆 GPU 가 빌려 쓸 방법이 없습니다. 모델이 커질수록 이 낭비가 커집니다.

논문이 제시한 **옵틱스 중심(Optics-centric) 아키텍처** 는 연산 칩 무리와 메모리 무리를 아예 따로 세워 놓고 광섬유로 잇습니다. 메모리 쪽 판에는 **광 인터포저(photonic interposer)**, 그러니까 빛을 그대로 받아 메모리 스택에 물려 주는 중간 판이 깔립니다.

이렇게 되면 여러 가속기가 멀리 있는 대용량 메모리를 **함께** 씁니다. 이 구조를 분리형 메모리 풀이라고 부릅니다. 네트워크를 거쳐 돌아가는 게 아니라 광 인터포저로 직접 물리기 때문에, 논문은 지연을 낮게 유지한 채로 나눠 쓰는 게 목표라고 적었습니다.

HBM 옆에 낸드를 붙여 계층을 하나 늘리는 접근과 방향이 다릅니다. 그쪽이 **용량 계층**을 만드는 일이라면, 이쪽은 메모리를 아예 **공유 자원**으로 돌리는 일입니다.

## 저자들이 남긴 숙제

![열과 정렬 — 광·전자 소자가 한 패키지에 놓일 때의 난제 개념 컷](/assets/images/tech/ram-07-cpo-optical-interconnect/08-agy-thermal-alignment.webp)
*열과 정렬 — 광·전자 소자가 한 패키지에 놓일 때의 난제 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

리뷰 논문의 값어치는 여기 있습니다. 저자들은 상용화 전에 풀어야 할 문제를 직접 적었습니다.

- **열 관리** — 전력을 많이 먹는 연산 칩과 열에 예민한 광 소자를 한 패키지에 넣어야 합니다. 온도가 오르면 재료의 굴절률이 변해 빛이 지나는 길이 틀어집니다. 논문은 열을 갈라놓는 설계와 미세 유체 냉각을 함께 봐야 한다고 적었습니다.
- **제조 정밀도** — 광섬유와 칩 위의 도파로를 맞추는 정렬 오차가 곧 손실입니다. 이걸 실험실이 아니라 양산 라인에서 반복해야 합니다.
- **표준화** — 인터페이스와 검사 절차가 회사마다 다르면 부품을 섞어 쓸 수 없습니다. 특히 메모리를 광으로 물릴 때 필요한 저지연 일관성 규약은 아직 업계 공통안이 없습니다.

그리고 결론이 흥미롭습니다. 논문은 구리를 전부 걷어내자고 하지 않습니다. **거리와 대역폭에 따라 전기와 빛을 나눠 맡기는** 것이 답이라고 적었습니다. 짧은 구간은 전기가 여전히 싸고 빠릅니다.

*주: 여기까지가 논문이 적은 한계이고, 아래 국내 이야기는 공개 자료로 덧붙인 관점입니다.*

## 국내에는 무슨 의미일까

![파운드리가 공표한 실리콘 포토닉스·CPO 일정](/assets/images/tech/ram-07-cpo-optical-interconnect/09-chart-foundry-roadmap.webp)
*파운드리가 공표한 실리콘 포토닉스·CPO 일정 — 출처: TrendForce·The Elec 보도 종합 기반 자가 렌더*

빛으로 칩을 잇는 기술은 **실리콘 포토닉스(silicon photonics)** 라고 부릅니다. 따로 만들던 광 부품을 실리콘 칩 위에 직접 새겨 넣는 공정입니다. 이 판이 지금 빠르게 움직이고 있습니다.

TSMC 는 COUPE 라는 이름으로 2026년 양산을 목표로 잡았습니다. 삼성전자 파운드리는 실리콘 포토닉스 진입을 공식화하고 300mm 웨이퍼 플랫폼과 공정 설계 키트(PDK)를 갖췄으며, 2027년 열압착 방식 광 엔진, 2028년 하이브리드 본딩 광 엔진, 2029년 CPO 턴키 서비스를 목표로 제시했습니다.

SK하이닉스는 여기에 **메모리 쪽에서** 들어갑니다. 광 엔진을 파는 회사가 아니라 광으로 물릴 메모리를 만드는 회사이고, 이번 논문의 교신저자가 SK하이닉스 AI 인프라 팀장이라는 사실이 그 위치를 보여 줍니다.

국내 광부품 업체들도 이미 이 공급망 안에 들어가 있습니다. 디일렉 보도에 따르면 광 트랜시버, 정렬 장비, 레이저 패키지 같은 부품과 장비를 국내 업체들이 글로벌 CPO 모듈 제조사에 대고 있습니다. HBM 때처럼 소재·부품·장비가 함께 움직이는 모양입니다.

## 앞으로 볼 것

![NVIDIA 로고](/assets/images/tech/ram-07-cpo-optical-interconnect/10-logo-nvidia.webp)
*NVIDIA 로고 — 출처: NVIDIA*

- **엔비디아 Spectrum-X Photonics** — CPO 를 적용한 네트워크 스위치입니다. 스위치에서 먼저 검증되고 나서 메모리로 내려오는 순서가 될 가능성이 큽니다.
- **표준 논의** — 광으로 물린 메모리를 여러 가속기가 나눠 쓰려면 규약이 먼저입니다. 어느 단체에서 누가 이 논의를 여는지가 신호입니다.
- **정렬 수율** — 실험실 성능보다 양산 수율이 이 기술의 일정을 정합니다. 파운드리들이 공표한 연도가 지켜지는지 보면 됩니다.
- **목표값과 실제값의 거리** — 100 Tb/s·1 pJ/bit·10 ns 에 실제 시제품이 얼마나 근접하는지가 다음 논문들의 관전 포인트입니다.

메모리 회사가 배선 로드맵을 학술지에 낸 이유는 결국 하나로 읽힙니다. 메모리를 더 빨리 만드는 것만으로는 더 이상 병목이 안 풀린다는 판단입니다.

[RAM에 대하여 (6) — HBM 옆에 낸드를 쌓는 새 계층, HBF](/posts/ram-06-hbf/)

## 참고 출처

- [[Nature Electronics] Kim, B. et al., Co-packaged optics for high-performance computing and artificial intelligence, 9권 853~867쪽 (2026-08-19) — 이 글의 중심 논문](https://www.nature.com/articles/s41928-026-01681-6)
- [[SK hynix Newsroom] AI 전장은 칩에서 시스템으로 — 네이처 일렉트로닉스 논문 소개 (2026-08-20)](https://news.skhynix.co.kr/cpo-in-nature-electronics/)
- [[SK hynix Newsroom] SK hynix's technology roadmap for co-packaged optics features in Nature Electronics (2026-08-20)](https://news.skhynix.com/en/cpo-in-nature-electronics/)
- [[StorageReview] 100Tb/s Nodes, Sub-1pJ/bit, Under 10ns — 논문 목표값 해설 (2026-08)](https://www.storagereview.com/news/sk-hynix-takes-its-co-packaged-optics-roadmap-to-nature-electronics-100tb-s-nodes-sub-1pj-bit-under-10ns)
- [[디일렉] SK하이닉스, CPO 청사진 공개 — 메모리도 빛으로 연결 (2026-08)](https://www.thelec.kr/news/articleView.html?idxno=61167)
- [[디일렉] 엔비디아가 쏘아 올린 CPO — 국내 소부장도 수주 러시 (국내 공급망 근거)](https://www.thelec.kr/news/articleView.html?idxno=58033)
- [[TrendForce] Silicon Photonics Race — TSMC 2026 COUPE, Samsung 2029 CPO 턴키 (파운드리 일정 근거)](https://www.trendforce.com/news/2026/04/01/news-silicon-photonics-race-intensifies-as-tsmc-targets-2026-coupe-production-samsung-eyes-2029-cpo-turnkey/)
