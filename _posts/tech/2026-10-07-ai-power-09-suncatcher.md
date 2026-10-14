---
title: "AI의 전기 (9) — Google 선캐처, 궤도에 오른 TPU 4개"
description: "궤도 위에서 AI 칩의 전력과 냉각을 해결하려는 Google 선캐처 시제 위성의 구성과 논문이 제시한 비용 전제를 정리합니다"
date: 2026-10-07
category: Tech
subcategory: Explainer
tags: [google, suncatcher, space-data-center, tpu, ai-power]
image: /assets/og/2026-10-07-ai-power-09-suncatcher.png
---

8탄까지 본 것은 땅 위에서 AI 데이터센터에 전기를 공급하는 방법이었습니다. 구글은 다른 선택지를 시험하기 시작했어요. 태양빛이 거의 끊기지 않는 궤도에 AI 칩을 올려, 전력과 냉각을 우주에서 해결할 수 있는지 보는 실험입니다.

[AI 의 전기 (8) — Google 이 핀란드 원전 절반을 22년 사들였습니다](/posts/ai-power-08-loviisa-ppa/)

![Project Suncatcher 공식 키 아트](/assets/images/tech/ai-power-09-suncatcher/01-hero.webp)
*Project Suncatcher 공식 키 아트 — 출처: Google*

## 사건 경과

구글은 10월 1일 Project Suncatcher의 첫 시제 위성이 궤도에 올랐다고 발표했습니다. 위성 영상 기업 Planet과 함께 만든 위성으로, SpaceX의 공유 발사 임무 Transporter-18에 실려 반덴버그 우주군 기지에서 Falcon 9으로 발사됐어요. 구글은 위성과 교신해 정상 작동을 확인했다고 밝혔습니다.

- 위성 내부 이름은 MVP, 냉장고 크기
- Trillium 세대 TPU 4개 탑재, 태양전지 약 1kW
- 수 주 동안 발사 충격·방사선·온도 변화에서 TPU가 버티는지 측정
- 근거 연구는 학술지 Joule에 동료 심사를 거쳐 게재

TPU(텐서 처리 장치)는 구글이 AI 연산용으로 직접 설계하는 칩이에요. Trillium은 6세대 TPU로, 구글 클라우드에서 TPU v6e라는 이름으로 쓰입니다.

## 수치 풀이

![Trillium TPU 방사선 시험 누적 선량 차트](/assets/images/tech/ai-power-09-suncatcher/02-chart.webp)
*Trillium TPU 방사선 시험 누적 선량 차트 — 출처: Google Suncatcher 논문 기반 자가 렌더*

저궤도에서 칩에 영향을 주는 것은 누적 방사선이에요. 구글 연구팀은 UC Davis에서 67MeV 양성자 빔을 Trillium TPU에 쏘며 AI 작업을 실행했습니다.

고대역폭 메모리(HBM)는 5년 예상치의 약 2.7배에서야 이상을 보였고, 최대 시험 선량에서도 칩이 멈추는 고장은 없었어요. 다만 메모리 오류는 시험 조건에서 약 50rad마다 한 번 발생했고, 논문은 추론에는 감당할 수 있지만 학습 작업에 주는 영향은 더 연구해야 한다고 적었습니다.

구글이 선택한 궤도는 고도 약 650km의 새벽-황혼 태양동기궤도예요. 이 궤도에서는 태양전지가 거의 계속 빛을 받아 지상보다 최대 8배 많은 전력을 생산합니다.

## 경제성 계산

![Suncatcher 논문 Figure 4 SpaceX 발사 단가 추이](/assets/images/tech/ai-power-09-suncatcher/03-capture.webp)
*Suncatcher 논문 Figure 4 SpaceX 발사 단가 추이 — 출처: Google*

우주 데이터센터의 비용을 좌우하는 값은 발사 단가입니다. 논문은 SpaceX가 쏘아 올린 누적 질량이 두 배가 될 때마다 kg당 가격이 약 20%씩 하락했다고 분석했어요. Falcon Heavy의 최저가는 아직 kg당 약 224만 원(1,600달러) 안팎입니다.

이 추세가 이어지면 2035년 무렵 저궤도 발사 단가가 kg당 28만 원(200달러) 아래로 하락할 수 있다는 것이 논문의 계산이에요. 그러려면 Starship이 1년에 약 180번 발사돼야 합니다.

![1kW 1년 전력 비용 지상·우주 비교 차트](/assets/images/tech/ai-power-09-suncatcher/04-chart.webp)
*1kW 1년 전력 비용 지상·우주 비교 차트 — 출처: Google Suncatcher 논문 기반 자가 렌더*

발사 단가가 kg당 28만 원(200달러)이 되면 궤도에 태양전지 1kW를 올려 1년 쓰는 비용은 약 113만 원(810달러)으로 계산됩니다. 미국 지상 데이터센터가 1kW에 1년 내는 전력 비용은 지역과 전력 효율에 따라 80만~420만 원(570~3,000달러)이에요. 우주 비용이 지상 비용 범위와 겹친다는 계산이지, 더 싸다는 뜻은 아닙니다.

## 남은 과제

### 위성 간 연결

지상 데이터센터는 칩끼리 광케이블로 연결됩니다. 우주에서는 위성 사이를 레이저로 연결해야 하고, 구글은 실험실에서 양방향 1.6Tbps를 기록했어요. 그만한 대역폭을 확보하려면 위성들이 100~200m 간격을 유지하며 비행해야 하고, 논문은 반경 1km 안에 81기를 모은 구성을 계산했습니다.

### 열과 설계

우주에는 공기가 없어 열을 복사로만 방출해야 합니다. 논문은 방열과 시스템 통합을 큰 공학 과제로 꼽았고, 장기적으로 스마트폰처럼 여러 부품을 한 칩에 통합하는 설계가 필요할 수 있다고 적었어요.

### 규모

The Register는 논문의 비용 목표를 맞추려면 Starship 발사 약 1,800번과 부품 100배 재사용이 필요하다고 정리했습니다. 연구팀도 여러 단계의 과제를 해결해야 한다고 인정했어요.

## 배경과 국내 접점

1탄에서 본 대로 미국 데이터센터는 전력망 접속을 몇 년씩 기다리고, 8탄의 구글은 기존 원전 전력을 22년 단위로 확보했습니다. 선캐처는 전력망 자체를 거치지 않는 선택지를 시험하고 있어요. 구글은 2025년 11월 이 구상을 처음 공개하며 2027년 초까지 Planet과 시제 위성을 올리겠다고 했는데, 일정보다 먼저 첫 위성을 쏘았습니다.

국내에서는 한화가 7월 3일 2040년까지 우주항공·AI에 55조 원을 투자한다고 발표했고, 이 가운데 한화시스템이 약 20조 원을 SAR 위성·저궤도 통신망과 함께 우주 AI 데이터센터 확보에 쓰겠다고 밝혔습니다. 우주 데이터센터의 구체적인 일정·규모는 공개되지 않았어요.

## 앞으로 주목할 점

- 수 주 안에 나올 궤도 데이터: TPU가 실제 우주 방사선·온도에서 지상 시험과 같은 결과를 보이는지
- 다음 단계 위성 2기: 구글이 언급한 위성 간 레이저 연결 시험의 발사 시점
- Starship 발사 횟수: 논문의 비용 전제를 좌우하는 값

[AI 의 전기 (8) — Google 이 핀란드 원전 절반을 22년 사들였습니다](/posts/ai-power-08-loviisa-ppa/)

## 참고 출처

- [[Google] Our Project Suncatcher prototype satellite is in orbit (2026-10-01, 발사·교신 확인)](https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-prototype/)
- [[Google Research] Exploring a space-based, scalable AI infrastructure system design (궤도·방사선·81기 구성, 본문 이미지 1점 출처)](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/)
- [[Joule] Toward a future space-based, highly scalable AI infrastructure system design (논문 게재본)](https://www.cell.com/joule/fulltext/S2542-4351(26)00362-4)
- [[Google] Suncatcher 논문 PDF (발사 단가·전력 비용 수치, 본문 이미지 1점 출처)](https://services.google.com/fh/files/misc/suncatcher_paper.pdf)
- [[The Register] Google launches first datacenter satellite (Starship 1,800회·남은 과제)](https://www.theregister.com/systems/2026/10/02/google-launches-first-datacenter-satellite-and-research-that-finds-orbiting-bit-barns-can-work/5300721)
- [[Smithsonian Magazine] Google wants to send data centers to space (TPU 4개·냉장고 크기)](https://www.smithsonianmag.com/smart-news/google-wants-to-send-data-centers-to-space-and-just-launched-a-satellite-to-test-whether-its-ambitious-plan-will-work-180989613/)
- [[뉴시스] 한화, AI 우주 강국 중장기 전략 발표 (55조 원·한화시스템 20조 원)](https://mobile.newsis.com/view/NISX20260703_0003695284)
- 환율: 1달러 ≈ 1,400원 기준 환산
