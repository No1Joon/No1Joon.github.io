---
title: "GPU 를 묶는 선을 누가 쥐나 — UALink 와 Ultra Ethernet"
description: "랙 안과 랙 밖에서 따로 벌어지는 두 전선을 갈라 보고, 표준이 NVLink 에 던진 숫자와 스펙만 나온 채 칩이 없는 현재 위치를 정리합니다"
date: 2026-08-20
category: Tech
subcategory: Explainer
tags: [ualink, ultra-ethernet, nvlink, interconnect, ai-infrastructure]
image: /assets/og/2026-08-20-ai-interconnect-ualink-ultra-ethernet.png
---

엔비디아의 해자를 층으로 나눠 보면 프레임워크는 이미 갈라졌고, 라이브러리와 시스템 두 층이 남습니다. 그중 시스템 층 — 그러니까 GPU와 GPU를 잇는 선 — 이 지금 표준 싸움의 한복판이에요.

여기서 헷갈리기 쉬운 게 하나 있습니다. **경쟁이 두 군데서 따로 벌어지고 있다는 것**입니다.

![랙 안 연결과 랙 밖 연결이 서로 다른 층이라는 구조 개념 컷](/assets/images/tech/ai-interconnect-ualink-ultra-ethernet/01-agy-hero-twolayers.webp)
*랙 안 연결과 랙 밖 연결이 서로 다른 층이라는 구조 개념 컷 — 출처: Anthropic 공식 발표 수치 기반 자가 생성*

🔗 링크 첨부 - [여기에 CUDA 해자 편 네이버 링크]

## 두 전선을 가르는 게 먼저입니다

![AI 인터커넥트 표준이 발표된 순서](/assets/images/tech/ai-interconnect-ualink-ultra-ethernet/02-chart.webp)
*AI 인터커넥트 표준이 발표된 순서 — 출처: 각 컨소시엄·NVIDIA 공식 발표 기반 자가 렌더*

랙 하나 안에서 가속기들을 촘촘히 묶는 걸 **스케일업**, 랙과 랙을 이어 클러스터를 만드는 걸 **스케일아웃**이라고 합니다. 두 자리에서 각각 다른 도전자가 서 있어요.

| 구분 | 스케일업 (랙 안) | 스케일아웃 (랙 밖) |
|---|---|---|
| 지금 강자 | **NVLink** | InfiniBand · RoCE |
| 도전 표준 | <mark>UALink</mark> | <mark>Ultra Ethernet</mark> |
| 성격 | 전용 규격 대 개방 표준 | 이미 있는 이더넷의 개량 |

이 둘을 한 덩어리로 묶어 *엔비디아 대항마* 라고 부르면 판이 안 보입니다. 스케일아웃 쪽은 원래도 표준 장비를 골라 쓸 수 있었고, 진짜로 잠겨 있던 건 스케일업이거든요.

## 랙 안 — UALink가 던진 숫자

![NVLink와 UALink 1.0의 최대 연결 가속기 수 비교](/assets/images/tech/ai-interconnect-ualink-ultra-ethernet/03-chart.webp)
*NVLink와 UALink 1.0의 최대 연결 가속기 수 비교 — 출처: UALink Consortium·NVIDIA 사양 기반 자가 렌더*

UALink 컨소시엄은 2025년 4월 1.0 최종 스펙을 냈습니다. 레인당 200GT/s에 **한 도메인에 최대 1,024개** 가속기를 묶을 수 있다고 규정했어요. NVLink의 최대치가 576개니 규모만 놓고 보면 앞섭니다.

다만 이 우위는 레인 하나가 빨라서 나온 게 아니라 **레인 수와 토폴로지**에서 나옵니다. 실제 대역폭은 별개예요. AMD가 올해 1월 CES에서 밝힌 MI455X는 72장짜리 Helios 랙에서 가속기당 약 3.6TB/s의 스케일업 대역폭을 낸다고 했는데, NVLink 5.0의 GPU당 1.8TB/s와 견주면 이쪽이 높습니다.

그리고 여기가 이 글에서 가장 중요한 대목입니다.

> 스펙은 두 번 나왔는데, 그 스펙으로 만든 칩은 아직 없습니다

컨소시엄은 2026년 4월 **2.0 스펙**을 발표했습니다. DL과 PL 규격을 분리하고 네트워크 안에서 연산을 처리하는 In-Network Compute, 관리 규격과 칩렛 규격을 더했어요. 그런데 정작 **1.0 실리콘은 2026년 말에야 나옵니다.** AMD·인텔·아스테라랩스가 준비 중이고요.

스펙이 실물보다 두 걸음 앞서 있는 상태입니다. 표준 진영이 흔히 겪는 자리인데, 그동안 상대는 이미 파는 물건으로 점유율을 쌓습니다.

## 랙 밖 — 이더넷이 밀고 들어옵니다

![랙과 랙을 잇는 이더넷 패브릭 개념 컷](/assets/images/tech/ai-interconnect-ualink-ultra-ethernet/04-agy-fabric.webp)
*랙과 랙을 잇는 이더넷 패브릭 개념 컷 — 출처: Anthropic 공식 발표 수치 기반 자가 생성*

바깥쪽 싸움은 결이 다릅니다. Ultra Ethernet Consortium은 2025년 6월 11일 1.0 스펙을 냈고, 9월에 1.0.1로 손봤습니다. 리눅스재단 산하에서 굴러가는 개방 규격이에요.

무엇을 규정하느냐가 핵심입니다. **NIC와 스위치, 광모듈, 케이블까지** 한 벌로 묶어 여러 벤더 장비를 섞어 쓸 수 있게 했어요. 그 위에 이더넷·IP용으로 다시 짠 RDMA를 얹었습니다. RDMA는 CPU를 거치지 않고 메모리끼리 직접 데이터를 옮기는 방식인데, 인피니밴드가 강했던 이유가 바로 여기였습니다.

방향은 이미 기울어 보입니다. 인피니밴드의 주인인 엔비디아조차 이더넷 기반 Spectrum-X로 무게를 옮겼고, Blackwell 세대에서는 Spectrum-X가 Quantum 인피니밴드보다 더 팔린다고 알려졌어요.

## 엔비디아의 응수 — 패브릭을 반쯤 엽니다

![NVIDIA 로고](/assets/images/tech/ai-interconnect-ualink-ultra-ethernet/05-logo-nvidia.webp)
*NVIDIA 로고 — 출처: NVIDIA*

닫아걸기만 한 게 아닙니다. 엔비디아는 2025년 5월 **NVLink Fusion**을 내놨어요. 남의 칩을 자기 패브릭에 붙일 수 있게 여는 겁니다.

- 미디어텍·마벨·알칩·아스테라랩스·시놉시스·케이던스가 초기 채택사로 붙었습니다
- 후지쯔와 퀄컴의 CPU를 엔비디아 GPU와 묶는 구성도 가능해졌습니다
- 커스텀 실리콘은 UCIe 인터페이스로 연결하고, 엔비디아가 브리지 칩렛을 제공합니다
- 올해 엔비디아는 마벨에 20억 달러(약 2조 8,000억 원)를 직접 투자하며 이 생태계를 넓혔습니다

읽는 방법은 이렇습니다. 개방 표준이 아직 실리콘을 못 낸 사이에, 엔비디아가 **개방의 편익 일부를 자기 규격 안에서 미리 제공**해 버린 거예요. 커스텀 칩을 만들고 싶은 하이퍼스케일러 입장에선 표준 실리콘을 기다릴 이유가 하나 줄어듭니다.

## 한국 NPU는 어느 쪽에 서게 되나

![리벨쿼드가 발표한 H200 대비 성능 배수](/assets/images/tech/ai-interconnect-ualink-ultra-ethernet/06-chart-npu.webp)
*리벨쿼드가 발표한 H200 대비 성능 배수 — 출처: 리벨리온 발표 수치 기반 자가 렌더*

국산 AI 반도체 두 곳은 추론에 초점을 맞춰 왔습니다.

리벨리온의 **REBEL**은 삼성 파운드리 4나노 공정으로 만들고 HBM3E 144GB에 4.8TB/s 대역폭을 답니다. 넉 장을 묶은 리벨쿼드는 엔비디아 H200 대비 연산 처리량 1.2배, 전력 효율 2.4배라고 회사가 밝혔어요. SK텔레콤 공급도 확정됐습니다. 퓨리오사AI의 **RNGD**는 TSMC 5나노 공정에 180W라는 낮은 전력 프로파일이 특징이고, LG 엑사원 3.5 실증에서 GPU 대비 전력당 성능 2.25배가 나왔습니다.

다만 두 회사가 **칩과 칩을 어떤 규격으로 잇는지는 공개되지 않았습니다.** 추론은 학습보다 스케일업 의존도가 낮아 당장은 급하지 않은 선택이긴 해요. 모델 하나를 수십 장에 쪼개 올리는 건 주로 학습 쪽 일이니까요.

그래도 이 선택은 언젠가 해야 합니다. 자체 규격을 만들면 생태계를 혼자 짊어져야 하고, UALink에 붙으면 실리콘이 나올 때까지 기다려야 하고, 이더넷으로 가면 스케일업 성능을 어느 정도 포기해야 합니다. 셋 다 공짜가 아니에요.

### 앞으로 볼 것

- 2026년 말 UALink 1.0 실리콘이 실제로 나오는지, 그리고 첫 상용 랙이 언제 뜨는지
- NVLink Fusion 파트너가 더 느는지 — 늘수록 표준 진영의 명분이 줄어듭니다
- Ultra Ethernet 상호운용 검증이 얼마나 빨리 붙는지
- 국산 NPU가 스케일업 규격을 공개하는 시점

해자 이야기를 층으로 나눠 보면, 프레임워크는 소프트웨어라 갈라지기 쉬웠고 시스템 층은 물리 규격이라 더딥니다. 케이블과 스위치는 컴파일하듯 바꿀 수 있는 게 아니니까요. 그래서 이 층의 승부는 발표가 아니라 **실리콘이 나오는 날짜**로 판가름 납니다.

## 참고 출처

- [[UALink Consortium] UALink 1.0 최종 스펙 — 레인당 200GT/s·최대 1,024 가속기](https://ualinkconsortium.org/)
- [[Network World] New v2 UALink specification aims to catch up to NVLink — 2.0 스펙 구성과 1.0 실리콘 일정 (2026-04-07)](https://www.networkworld.com/article/4155357/new-v2-ualink-specification-aims-to-catch-up-to-nvlink.html)
- [[Ultra Ethernet Consortium] UEC Specification 1.0 발표 — NIC·스위치·광모듈·케이블 범위와 이더넷용 RDMA (2025-06-11)](https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/)
- [[NVIDIA] NVLink Fusion 공개 — 세미커스텀 AI 인프라와 파트너 생태계](https://nvidianews.nvidia.com/news/nvidia-nvlink-fusion-semi-custom-ai-infrastructure-partner-ecosystem)
- [[Spheron] UALink vs NVLink 2026 — MI455X 스케일업 대역폭과 NVLink 5.0 비교](https://www.spheron.network/blog/ualink-vs-nvlink-open-gpu-interconnect-2026/)
- [[ZDNet Korea] 리벨리온, SK텔레콤에 K-NPU 리벨 칩 공급 (2026-08-12)](https://zdnet.co.kr/view/?no=20260812150846)
- [[전자신문] 2026 10대 핫이슈 — 국산 추론용 AI 반도체 양산과 RNGD·REBEL 사양](https://www.etnews.com/20251224000251)
- 환율: 1달러 ≈ 1,400원 기준 환산
