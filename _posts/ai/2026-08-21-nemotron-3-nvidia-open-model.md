---
title: "GPU 파는 회사가 왜 모델을 공짜로 풀까 — Nemotron 3"
description: "가중치에 학습 데이터와 레시피까지 연 Nemotron 3 의 세 크기를 정리하고, 라이선스를 직접 읽어 완전 공개라는 말의 경계를 확인합니다"
date: 2026-08-21
category: AI
subcategory: Explainer
tags: [nemotron, nvidia, open-weights, license, moe]
image: /assets/og/2026-08-21-nemotron-3-nvidia-open-model.png
---

모델을 공짜로 푸는 회사는 이제 흔합니다. 그런데 **GPU를 파는 회사**가 그러면 이야기가 조금 달라져요.

엔비디아가 Nemotron 3라는 이름으로 세 종류를 열었습니다. 가중치만 준 게 아니라 학습 데이터와 사후학습 레시피, 파인튜닝 코드까지 함께요. 다만 *완전 공개* 라는 말에는 경계가 있고, 라이선스에 대해 떠도는 이야기 중에는 틀린 것도 있습니다.

![NVIDIA 로고](/assets/images/ai/nemotron-3-nvidia-open-model/01-logo-nvidia.webp)
*NVIDIA 로고 — 출처: NVIDIA*

## 세 종류를 단계로 풀었습니다

![Nemotron 3 세 모델의 전체·활성 파라미터](/assets/images/ai/nemotron-3-nvidia-open-model/02-chart.webp)
*Nemotron 3 세 모델의 전체·활성 파라미터 — 출처: NVIDIA 모델 카드·공식 발표 기반 자가 렌더*

크기가 셋인데, 전체 파라미터보다 **토큰당 실제로 켜지는 양**이 더 중요합니다.

| 모델 | 전체 / 활성 | 공개 |
|---|---|---|
| Nano | 30B / **3.5B** | 2025년 12월 |
| Super | 120B / **12B** | 2026년 3월 GTC |
| Ultra | 550B / <mark>55B</mark> | 2026년 6월 Computex |

전문가 혼합(MoE, Mixture of Experts) 구조라 그렇습니다. 550B를 다 들고 있어도 한 토큰을 처리할 때 켜지는 건 55B뿐이에요. 그래서 덩치에 비해 추론이 쌉니다.

구조는 한 가지 더 특이합니다. **Mamba-2와 트랜스포머를 섞었어요.** Nano 기준으로 Mamba-2/MoE 레이어 23개에 어텐션 레이어 6개입니다. 어텐션은 문맥이 길어질수록 비용이 급격히 늘어나는데, Mamba 계열은 그 부담이 덜해요. 긴 문맥에서 병목을 줄이려고 둘을 섞은 겁니다.

실제로 Super는 BF16에서 100만 토큰 문맥을, Ultra는 262k를 지원하고 Blackwell 하드웨어에서 NVFP4로 쓰면 100만까지 갑니다. 엔비디아는 Ultra가 초당 300 토큰 넘게 내놓는다고 밝혔습니다.

성능은 Artificial Analysis 지능 지수 기준 Super 36점, Ultra 48점입니다. 다만 이건 **미국 오픈웨이트 진영 안에서의 순위**라는 걸 감안해서 보셔야 해요.

## "완전 공개"의 경계는 데이터에 있습니다

![열려 있는 문과 승인이 필요한 문이 나뉜 구조 개념 컷](/assets/images/ai/nemotron-3-nvidia-open-model/03-agy-gate.webp)
*열려 있는 문과 승인이 필요한 문이 나뉜 구조 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

여기가 이 발표의 진짜 특징입니다. 보통 오픈웨이트라고 하면 **가중치만** 줍니다. 어떻게 만들었는지는 안 알려주고요.

엔비디아는 그 위에 사전학습·사후학습 데이터와 레시피, 파인튜닝 코드를 얹었습니다. 사전학습은 Common Crawl·arXiv·GitHub 같은 공개 데이터와 합성 데이터를 썼고, 사후학습은 영어와 6개 언어의 합성 데이터를 썼다고 모델 카드에 적혀 있어요.

다만 **전부가 조건 없이 열린 건 아닙니다.** 코드·수학·다국어 데이터 일부는 **승인을 받아야 접근**할 수 있습니다. 모델 카드에도 *gating and approval is required* 라고 적혀 있고요.

### 라이선스는 실제로 어떤가

여기서 떠도는 이야기를 하나 바로잡아야겠습니다. 엔비디아 오픈 모델 라이선스에 **안전 가드레일을 우회하면 권리가 자동 해지된다**는 조항이 있다는 분석이 돌아다니는데, 그건 예전 판 얘기입니다.

**Nemotron 전용 라이선스 본문을 직접 읽어보면 그 조항이 없습니다.**

| 조항 | 내용 |
|---|---|
| 상업 이용 | **가능** |
| 파생 모델 | 만들고 배포하는 것 **자유** |
| 출력물 소유권 | 엔비디아가 <mark>주장하지 않음</mark> |
| 해지 조건 | 특허·저작권 소송을 걸면 해지 |
| 그 밖 | 수출·제재 법규 준수, 무보증(AS IS) |

특허 소송을 걸면 해지된다는 건 오픈소스 라이선스에서 흔한 특허 보복 조항이고, 수출통제 준수는 미국 회사면 다 붙습니다. 그러니 **쓰는 입장에서는 꽤 관대한 편**이에요.

그렇다고 OSI가 정의한 오픈소스냐 하면 그건 또 다른 문제입니다. 수출·제재 조항이 들어가는 순간 특정 지역 사용자를 차별하지 않는다는 조건과 부딪히거든요. 엔비디아는 자사 표현으로 *truly open source* 라고 쓰지만, 그 표현을 그대로 받아 적을 필요는 없습니다.

## GPU 파는 회사가 왜 모델을 푸나

![모델이 싸질수록 하드웨어 수요가 느는 구조 개념 컷](/assets/images/ai/nemotron-3-nvidia-open-model/04-agy-economics.webp)
*모델이 싸질수록 하드웨어 수요가 느는 구조 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

이게 이 글에서 제일 중요한 질문입니다. OpenAI나 Anthropic이 모델을 팔아 돈을 번다면, 엔비디아는 **그 모델이 돌아가는 하드웨어**를 팔아 돕니다.

그러면 계산이 뒤집힙니다. 좋은 모델이 공짜로 풀릴수록 그걸 돌려 보려는 곳이 늘고, 돌리려면 GPU가 필요해요. 모델 자체는 엔비디아에게 매출원이 아니라 **수요 유발 장치**에 가깝습니다.

여기에 조건 하나가 더 붙습니다. Ultra의 100만 토큰 문맥은 **Blackwell 하드웨어에서 NVFP4로 쓸 때** 열립니다. 모델은 어디서든 받을 수 있지만, 최대 성능은 자사 칩에서 나오는 구조예요. 열어 주되 제일 좋은 자리는 자기 쪽에 남겨 둔 겁니다.

> 모델을 여는 것과 생태계를 여는 것은 다른 일입니다

이걸 나쁘다고만 볼 일은 아닙니다. 학습 데이터와 레시피가 공개되면 연구자들이 실제로 그 위에서 다음 모델을 만들 수 있으니까요. 가중치만 던져 주는 공개보다 재현 가능성이 훨씬 높습니다.

## 국내엔 무엇이 달라지나

![Nemotron 3 가 풀린 순서](/assets/images/ai/nemotron-3-nvidia-open-model/05-chart.webp)
*Nemotron 3 가 풀린 순서 — 출처: NVIDIA 공식 발표·모델 카드 기반 자가 렌더*

국내에서 이 발표가 의미 있는 자리는 두 곳입니다.

첫째는 **온프레미스**예요. 공공기관이나 금융처럼 데이터를 밖으로 못 내보내는 곳은 API를 쓸 수 없습니다. 그런 곳에 올릴 수 있는 상업 이용 가능한 모델이 하나 더 늘어난 셈이고, 심지어 파인튜닝 레시피까지 딸려 옵니다.

둘째는 **국산 NPU**입니다. 리벨리온의 REBEL이나 퓨리오사의 RNGD 같은 칩은 결국 그 위에서 돌릴 모델이 있어야 값을 합니다. 자체 모델을 만들 여력이 없는 곳일수록 쓸 만한 오픈웨이트가 늘어나는 게 직접적인 도움이 돼요. 다만 Nemotron 3가 국산 NPU에서 실제로 어떻게 도는지는 **공개된 실측이 없습니다** — 이건 확인되면 따로 다뤄야 할 주제입니다.

### 정리하면

- 크기 셋을 단계로 풀었고, 덩치 대비 활성 파라미터가 작아 추론이 쌉니다
- 가중치 너머 데이터·레시피까지 열었지만 **일부 데이터는 승인이 필요**합니다
- 라이선스는 관대합니다. 가드레일 조항이 있다는 이야기는 Nemotron 라이선스에는 해당하지 않습니다
- 다만 최대 성능은 자사 하드웨어에서 열리는 구조라, 공개의 방향과 사업의 방향이 어긋나지 않습니다

## 참고 출처

- [[NVIDIA] Nemotron-3-Nano-30B-A3B 모델 카드 — 파라미터·아키텍처·데이터 접근 조건](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
- [[NVIDIA] Nemotron Open Model License 본문 — 상업 이용·파생물·해지 조건](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license)
- [[NVIDIA] Nemotron 파운데이션 모델 소개 페이지](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
- [[Open Source Guy] The Hidden Risks of NVIDIA's Open Model License — 구판 라이선스의 OSI 정의 충돌 분석](https://shujisado.org/2025/12/19/nvidia-open-model-license-a-corporate-risk-analysis/)
- 지능 지수는 Artificial Analysis 집계 기준이며, 추론 속도·비용 절감 수치는 엔비디아 자체 발표입니다
