---
title: "Xiaomi MiMo V2.6 — 1조 파라미터 모델을 MIT 라이선스로"
description: "오픈 가중치 최고 점수를 받은 MiMo-V2.6 Pro·Flash 의 구성과 가격, 함께 공개된 강화학습 코드와 학습 환경을 정리합니다"
date: 2026-09-28
category: AI
subcategory: News
tags: [xiaomi, mimo, open-weights, moe, llm]
image: /assets/og/2026-09-28-xiaomi-mimo-v26.png
---

Xiaomi가 2026년 9월 21일 LLM(대규모 언어모델) MiMo-V2.6 시리즈를 공개하고 가중치를 MIT 라이선스로 공개했습니다. 플래그십 MiMo-V2.6-Pro는 전체 파라미터가 1조 200억 개로, 독립 평가 기관 Artificial Analysis의 지능 지수에서 오픈 가중치 모델 중 가장 높은 46.32점을 받았어요.

Xiaomi는 여기에 강화학습(RL) 코드와 학습 환경 7,000여 개까지 함께 공개했습니다.

![Xiaomi MiMo 워드마크](/assets/images/ai/xiaomi-mimo-v26/01-logo-mimo.webp)
*Xiaomi MiMo 워드마크 — 출처: Xiaomi*

## 모델 구성

![Xiaomi 로고](/assets/images/ai/xiaomi-mimo-v26/02-logo-xiaomi.webp)
*Xiaomi 로고 — 출처: Xiaomi*

MiMo-V2.6은 모델 두 개와 속도 옵션 하나로 구성됩니다. Hugging Face에 가중치가 공개됐고, Xiaomi AI Studio·MiMo Code·MiMo Desktop·자체 API와 OpenRouter에서 바로 쓸 수 있어요.

- MiMo-V2.6-Pro: 전체 1.02T, 활성 42B의 MoE(전문가 혼합) 모델
- MiMo-V2.6-Flash: 전체 309B, 활성 15B의 경량 모델
- Pro-UltraSpeed: Pro와 같은 품질로 출력 속도를 최대 20배 높인 유료 옵션
- 두 모델 모두 텍스트·이미지·영상·음성을 한 모델에서 받는 옴니모달, 컨텍스트 100만 토큰
- MiMo-V2.6-Distill-Qwen-9B: Alibaba Qwen3.5-9B를 MiMo 생성 데이터로 미세조정한 연구용 체크포인트

## 스펙·수치 풀이

![MiMo-V2.6 백본과 멀티모달 인코더 구조도](/assets/images/ai/xiaomi-mimo-v26/03-photo-architecture.webp)
*MiMo-V2.6 백본과 멀티모달 인코더 구조도 — 출처: Xiaomi*

MoE는 전체 파라미터를 여러 전문가(expert) 묶음으로 나눠 두고, 토큰마다 그중 일부만 계산에 쓰는 구조입니다. Pro는 전문가 384개 중 8개를 선택해 사용해 토큰 하나를 처리할 때 1조 개가 아니라 420억 개만 계산해요.

어텐션은 가까운 구간만 보는 Sliding Window Attention(SWA)과 전체를 보는 Global Attention(GA)을 함께 사용합니다. Pro는 70층 중 60층이 SWA, 10층이 GA예요. 100만 토큰 컨텍스트에서 모든 층이 전체를 보면 계산량이 급격히 늘어나서, 대부분의 층은 가까운 구간만 보게 한 구조입니다.

한 번에 토큰 여러 개를 미리 예측하는 MTP(Multi-Token Prediction) 블록도 결합돼 있어 출력 속도를 높여요.

| 항목 | V2.6-Pro | V2.6-Flash |
| :--- | :--- | :--- |
| 전체 파라미터 | **1.02T** | 309B |
| 활성 파라미터 | 42B | 15B |
| 전문가 수 | 384개 중 8개 | 256개 중 8개 |
| 층 (SWA/GA) | 70 (60/10) | 48 (39/9) |
| 컨텍스트 | 100만 토큰 | 100만 토큰 |

시각 인코더는 6억 8,100만 파라미터, 음성은 3억 800만 파라미터 토크나이저와 1억 2,700만 파라미터 인코더가 맡습니다.

모델 카드가 권장하는 배포 설정은 Pro가 GPU 서버 2노드(SGLang 기준 텐서 병렬 16), Flash가 GPU 4~8장이라 개인 PC에서 돌릴 크기는 아니에요.

## 벤치마크

Xiaomi 모델 카드는 Pro를 Anthropic Claude Opus 5, OpenAI GPT-5.6 Sol과 에이전트·코딩 벤치마크 다섯 개로 비교했습니다.

| 벤치마크 | V2.6-Pro | Claude Opus 5 |
| :--- | :--- | :--- |
| DeepSWE v1.1 | 71.9 | **74.0** |
| AutomationBench | <mark>53.1</mark> | 50.3 |
| Toolathlon-Verified | 76.9 | **80.6** |
| Terminal Bench 2.1 | <mark>89.9</mark> | 89.1 |
| OSWorld-Verified | 82.0 | **83.4** |

다섯 개 중 두 개에서 Opus 5보다 높고 세 개에서 낮아요. GPT-5.6 Sol과 비교하면 AutomationBench(45.8점)·Terminal Bench 2.1(88.8점)·Toolathlon(74.9점)에서 Pro가 앞섰습니다. Flash는 AutomationBench 52.3점으로 Pro와 0.8점 차이였지만, 더 어려운 Terminal Bench 4.0에서는 28.8점으로 Opus 5(49.0점)와 20점 넘게 차이가 났어요.

이 점수는 Xiaomi가 직접 측정한 결과입니다. 제3자 수치는 Artificial Analysis 지능 지수(v4.3) 46.32점이 있고, Xiaomi는 이 점수로 Kimi K3·Qwen3.8 Max보다 높은 점수를 기록한 오픈 가중치 모델 1위라고 밝혔어요. eWeek는 DeepSWE 같은 코딩 벤치마크가 채점 방식과 데이터 오염 문제로 신뢰도 논란이 있다는 점, 보안 관련 외부 검증이 아직 없다는 점을 함께 짚었습니다.

## 가격

![출력 100만 토큰 가격, MiMo-V2.6 세 등급과 Claude Opus 5](/assets/images/ai/xiaomi-mimo-v26/04-chart-price.webp)
*출력 100만 토큰 가격, MiMo-V2.6 세 등급과 Claude Opus 5 — 출처: OpenRouter · Anthropic 공개 가격 기반 자가 렌더*

OpenRouter 기준 100만 토큰당 가격은 Flash가 입력 196원(0.14달러)·출력 392원(0.28달러), Pro가 입력 609원(0.435달러)·출력 1,218원(0.87달러)입니다. Claude Opus 5는 입력 7,000원(5달러)·출력 35,000원(25달러)이라, 출력 기준으로 Pro가 약 29분의 1이에요. 속도를 높인 Pro-UltraSpeed는 Pro의 10배인 입력 6,090원(4.35달러)·출력 12,180원(8.7달러)입니다.

가격은 4월에 나온 V2.5와 같게 유지했습니다. Xiaomi는 SiliconANGLE을 통해 Pro의 비용이 비슷한 지능의 해외 모델 대비 20분의 1에서 60분의 1 수준이라고 주장했어요.

## 강화학습 과정 공개

Xiaomi는 사전학습을 마친 모델에 강화학습을 30단계 진행했고, 6일이 안 걸렸다고 밝혔어요. 단계마다 프롬프트 1,568개에 응답을 16개씩 생성해 약 35억~37억 토큰을 만들었고, 전체 궤적은 약 75만 개였습니다.

강화학습에 든 비용은 Pro 약 36억 7,000만 원(262만 달러), Flash 약 11억 9,000만 원(85만 달러)으로 합쳐 약 48억 6,000만 원(347만 달러)이에요. 사전학습과 다른 개발 비용은 제외된 수치라, 국내 일부 보도처럼 총 학습 비용으로 읽으면 안 됩니다. 공개 대상은 가중치 외에 기술 보고서, 소프트웨어 개발·취약점 재현·웹 개발 등 7,000개가 넘는 RL 학습 환경, 궤적 수집·보상 평가·정책 최적화 프레임워크까지예요.

## 배경과 맥락

Xiaomi의 MiMo는 2025년 4월 7B 추론 모델 MiMo-7B로 시작해 12월 309B MoE인 MiMo-V2-Flash를 MIT로 공개했습니다. 2026년 3월에는 1조 파라미터급 MiMo-V2-Pro를 비공개로 출시했다가 4월 V2.5부터 대형 모델도 가중치를 공개했어요.

팀은 DeepSeek-V2 개발에 참여했던 뤄푸리(Luo Fuli)가 2025년 말부터 이끌고 있고, 레이쥔(Lei Jun) CEO는 2026년 3월 3년간 AI에 최소 87억 달러(약 12조 1,800억 원)를 투자하겠다고 밝혔습니다.

Alibaba는 9월 20일 이미지 모델 Qwen-Image-2.1을 연구용 한정 라이선스로 공개했는데, Xiaomi는 1조 파라미터 모델을 상업 이용까지 자유로운 MIT 라이선스로 공개해 라이선스 조건에서 차이가 뚜렷했어요.

## 국내 사용자에게 주는 의미

국내에서 중국 AI 서비스를 쓸 때 확인해야 할 지점은 데이터 이전입니다. 개인정보보호위원회는 2025년 2월 DeepSeek 앱의 국내 신규 다운로드를 개인정보 처리 문제로 중단시킨 적이 있어요. MiMo API나 Xiaomi AI Studio를 쓰면 입력 데이터가 Xiaomi 서버로 가지만, MIT 가중치를 받아 국내 클라우드나 사내 GPU에 배포하면 데이터가 밖으로 나가지 않습니다.

다만 Pro를 자체 운영하려면 GPU 서버 2노드가 필요해서, 중소 규모 팀이 현실적으로 쓸 수 있는 것은 Flash나 OpenRouter 경유 API입니다.

한국어 성능에 대한 Xiaomi의 공식 수치는 발표 자료에 없어요.

## 앞으로 주목할 점

- LMArena 등 외부 평가에서 Xiaomi 자체 벤치마크 점수가 유지되는지
- 공개된 RL 환경·코드로 외부 연구진이 결과를 재현하는지
- Xiaomi 스마트폰·HyperOS·전기차에 V2.6이 적용되는 시점
- 국내 클라우드 사업자의 MiMo 모델 제공 여부

## 참고 출처

- [[Hugging Face] XiaomiMiMo/MiMo-V2.6-Pro-RL 모델 카드 (구조·벤치마크·배포 설정, 본문 이미지 1점 출처)](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [[Hugging Face] XiaomiMiMo/MiMo-V2.6-Flash-RL 모델 카드 (Flash 구조·벤치마크)](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [[SiliconANGLE] Xiaomi introduces MiMo-V2.6 series open-source AI model family (가격·Artificial Analysis 점수·비용 주장)](https://siliconangle.com/2026/09/22/xiaomi-introduces-mimo-v2-6-series-open-source-ai-model-family/)
- [[RuntimeWire] Xiaomi open-sources MiMo-V2.6 and the RL machinery behind it (강화학습 단계·궤적 수)](https://runtimewire.com/article/xiaomi-open-sources-mimo-v2-6-rl-cost-3-47m)
- [[eWeek] Xiaomi MiMo-V2.6 Open Source: Pro, Flash, 9B Models (RL 비용 범위·공개 대상·벤치마크 한계)](https://www.eweek.com/news/xiaomi-mimo-v26-open-source-rl-reproduction/)
- [[Wikipedia] Xiaomi MiMo (버전 이력·투자 계획)](https://en.wikipedia.org/wiki/Xiaomi_MiMo)
- [[AI타임스] 샤오미, 오픈 모델 미모-V2.6 공개 (국내 보도)](https://www.aitimes.com/news/articleView.html?idxno=215552)
- [[Anthropic] Claude API 가격 (Claude Opus 5 요금)](https://platform.claude.com/docs/en/about-claude/pricing)
- 환율: 1달러 ≈ 1,400원 기준 환산
