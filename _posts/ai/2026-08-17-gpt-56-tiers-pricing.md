---
title: "GPT-5.6 은 모델 하나가 아닙니다 — Sol·Terra·Luna 고르는 법"
description: "한 이름 아래 25배 벌어진 세 티어의 단가와 모드별 배수를 정리하고, 어느 일을 어느 티어에 맡길지 기준을 세웁니다"
date: 2026-08-17
category: AI
subcategory: Explainer
tags: [gpt-56, openai, llm-pricing, model-tiers, api-cost]
image: /assets/og/2026-08-17-gpt-56-tiers-pricing.png
---

GPT-5.6은 모델 하나가 아니라 **세 개**입니다. 이름도 GPT-5.6 하나로 부르지만 실제로 고르는 건 Sol·Terra·Luna 셋 중 하나예요.

그리고 이 셋의 값 차이가 25배입니다. 게다가 출시 3주 만에 그중 하나가 80% 싸졌어요. 어느 일을 어느 티어에 맡기느냐가 곧 청구서를 정하는 구조가 됐습니다.

![OpenAI 로고](/assets/images/ai/gpt-56-tiers-pricing/01-hero-openai-logo.webp)
*OpenAI 로고 — 출처: OpenAI*

## 한 이름 아래 세 모델

GPT-5.6은 2026년 6월 26일 제한 프리뷰로 먼저 나왔고, 7월 9일 정식 공개되며 ChatGPT·API·Codex· GitHub Copilot에 함께 올라갔습니다.

티어는 셋입니다. 플래그십 **Sol**, 균형형 **Terra**, 고속·저비용 **Luna**. 여기에 Sol을 더 오래 생각하게 돌리는 **Sol Ultra** 모드가 붙습니다.

헷갈리기 쉬운 건 **성능이 갈리는 만큼 스펙이 갈리지는 않는다**는 점이에요. 컨텍스트 윈도 (context window)와 출력 한도, 지식 컷오프는 셋이 똑같습니다.

| 항목 | 세 티어 공통 |
|---|---|
| 컨텍스트 윈도 | **105만 토큰** |
| 최대 출력 | 12만 8천 토큰 |
| 지식 컷오프 | 2026년 2월 |

- 즉 티어를 고르는 건 담을 수 있는 분량이 아니라 **판단의 품질과 값**을 고르는 일입니다.

성능 쪽에서 가장 많이 인용되는 수치는 명령줄 작업을 다루는 *Terminal-Bench 2.1* 입니다.

![더 오래 생각하게 했을 때의 격차](/assets/images/ai/gpt-56-tiers-pricing/02-chart-sol-ultra.webp)
*더 오래 생각하게 했을 때의 격차 — 출처: 직접 작성 (OpenAI 공식 발표 수치 기반)*

Sol Ultra가 91.9%, 기본 Sol이 88.8%예요. **3.1%p**를 더 얻자고 생각을 더 시키는 셈입니다.

여기서 짚어둘 게 있어요. **Ultra는 별도 요금표가 있는 모델이 아닙니다.** 가격표에 Sol Ultra 행은 없고, 더 오래 생각한 만큼 출력 토큰이 늘어 청구서가 올라가는 구조예요. 같은 단가에 더 많은 토큰을 쓰는 것이지 단가가 오르는 게 아닙니다.

## 7월 30일, 바닥이 내려앉았다

정식 출시 3주 만인 7월 30일, OpenAI가 값을 다시 매겼습니다. **Luna는 80%, Terra는 20% 내렸고 Sol의 표준 가격은 그대로**입니다.

![Luna 출력 단가 인하 폭](/assets/images/ai/gpt-56-tiers-pricing/03-chart-luna-cut.webp)
*Luna 출력 단가 인하 폭 — 출처: 직접 작성 (OpenAI 공식 가격표 기반)*

현재 공식 가격표 기준으로 정리하면 이렇습니다.

| 티어 | 입력 (100만 토큰) | 출력 (100만 토큰) |
|---|---|---|
| Sol | 7,100원 | 42,600원 |
| Terra | 2,840원 | 17,040원 |
| Luna | <mark>284원</mark> | <mark>1,704원</mark> [80% 인하] |

캐시된 입력은 여기서 다시 10분의 1입니다. Luna는 캐시 입력이 100만 토큰당 **28원**이에요. 같은 프롬프트 앞부분을 반복해 보내는 작업이라면 이 항목이 실제 청구서를 크게 좌우합니다.

인하 폭은 티어마다 달랐습니다.

| 티어 | 인하율 | 남은 값 |
|---|---|---|
| Sol | 없음 | 그대로 |
| Terra | **20%** | 100만 토큰당 17,040원 |
| Luna | <mark>80%</mark> | 100만 토큰당 1,704원 |

- 위쪽은 그대로 두고 아래쪽만 내렸다는 건, 지키려는 자리가 플래그십이 아니라 **대량 처리 시장**이라는 뜻입니다.

3주 만의 인하는 정상적인 가격 정책이라기보다 대응에 가깝습니다. CNBC 보도에 따르면 OpenRouter 기준으로 중국산 모델이 미국 기업 토큰 사용량의 **46%**를 가져갔고, 기업들이 비용에 민감해지면서 충분히 좋은 저가 모델로 옮겨 가고 있었거든요.

> 성능 경쟁이 아니라 단가 경쟁으로 전선이 옮겨 갔습니다.

## 속도는 따로 판다

값을 이야기할 때 티어만 보면 절반만 본 겁니다. GPT-5.6은 **같은 모델을 어느 모드로 돌리느냐**에 따라 단가가 또 갈려요.

![모드만 바꿨을 때의 단가](/assets/images/ai/gpt-56-tiers-pricing/04-chart-mode.webp)
*모드만 바꿨을 때의 단가 — 출처: 직접 작성 (OpenAI 공식 가격표 기반)*

표준을 기준으로 **Fast 모드는 2배, Batch·Flex는 절반**입니다. 응답이 급하지 않은 야간 배치 작업이라면 같은 모델을 절반 값에 돌릴 수 있고, 반대로 사용자가 화면 앞에서 기다리는 작업이라면 2배를 내고 속도를 사는 구조예요.

여기에 8월 13일 **Ultrafast** 모드가 프리뷰로 열렸습니다. Sol을 초당 최대 750토큰으로 뽑아내는데, 표준 대비 최대 14배 속도라는 게 회사 설명입니다. 2,500문항을 처리하는 데 11시간 11분이 걸렸고, 같은 작업에 78시간 27분이 걸린 모델과 정확도는 비슷했다고 밝혔어요.

- 정리하면 GPT-5.6의 요금은 **티어(품질) × 모드(속도)** 두 축으로 정해집니다.

## 경쟁자와 나란히 놓으면

Google은 8월 13일 Gemini 3.7 Flash를 내며 **반값**을 앞세웠습니다. 그런데 대량 처리에 쓰는 모델들을 한 줄에 세워 보면 그림이 조금 달라져요.

![대량 처리 모델들의 출력 단가](/assets/images/ai/gpt-56-tiers-pricing/05-chart-vs.webp)
*대량 처리 모델들의 출력 단가 — 출처: 직접 작성 (OpenAI·Google 공식 가격표 기반)*

Gemini 3.7 Flash의 프로모션가(출력 100만 토큰 5,325원)는 **Luna의 세 배**입니다. 연말에 프로모션이 끝나 정가 1만 650원으로 돌아가면 여섯 배가 되고요. Google 진영에서 가장 싼 Flash-Lite와 비교해도 Luna가 절반 수준입니다.

감이 잘 안 오면 실제 작업으로 환산해 봅니다. 고객 문의 한 건을 분류하는 데 프롬프트 65토큰, 답 2토큰이 든다고 치고 **100만 건**을 돌리면 Luna 기준 입력 6,500만 토큰에 출력 200만 토큰이에요. 값으로는 **약 2만 2천 원**입니다.

다만 이건 토큰 수를 고정했을 때의 계산입니다. 실제로는 모델마다 같은 질문에 쓰는 토큰이 다르고, 특히 생각 토큰이 붙으면 출력 쪽이 몇 배로 불어납니다. **단가표는 출발점일 뿐 청구서는 토큰 수가 정한다**는 뜻이에요. 그래도 출발점 자체가 지금은 Luna 쪽이 낮습니다.

## 어느 티어에 무엇을 시킬까

OpenAI가 직접 제시한 구분이 명확한 편입니다. 대규모 문서 분석과 고객 문의 분류, 반복적인 코드 구현은 Luna와 Terra로 처리하고, 복잡한 판단과 계획 수립에 Sol을 쓰라는 거예요.

![작업에 따라 티어를 고르는 개념](/assets/images/ai/gpt-56-tiers-pricing/06-agy-tier-choice.webp)
*작업에 따라 티어를 고르는 개념 — 출처: agy 생성*

| 작업 | 티어 | 모드 |
|---|---|---|
| 분류·태깅·요약 | <mark>Luna</mark> | Batch |
| 일상 개발·문서 작업 | **Terra** | 표준 |
| 복잡한 판단·계획 | **Sol** | 표준 |
| 사용자가 기다리는 응답 | Terra 이상 | **Fast** |

국내에서도 접점이 늘고 있습니다. OpenAI는 2025년 한국 법인을 세웠어요. 아시아 세 번째, 전 세계 열두 번째 거점입니다.

협력도 이어졌습니다. 카카오·SK텔레콤·LG전자·크래프톤·야놀자와 파트너십을 발표했고, 법무법인 태평양은 ChatGPT Enterprise를 전사에 도입했습니다. 다만 GPT-5.6의 특정 티어를 어디에 쓰는지까지 공개한 국내 사례는 아직 확인되지 않습니다.

> 모델을 고르는 시대에서, 같은 모델의 어느 단을 쓸지 고르는 시대로 넘어왔습니다.

## 참고 출처

- [[OpenAI] GPT-5.6 공식 발표 (티어 구성·벤치마크)](https://openai.com/index/gpt-5-6/)
- [[OpenAI] GPT-5.6 Sol 프리뷰 공지 (6월 26일 제한 프리뷰)](https://openai.com/index/previewing-gpt-5-6-sol/)
- [[OpenAI] 가격·성능 프런티어 갱신 발표 (7월 30일 Luna·Terra 인하)](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)
- [[OpenAI] API 공식 가격표 (티어·모드별 단가 — 본문 표·차트의 근거)](https://developers.openai.com/api/docs/pricing)
- [[CNBC] OpenAI cuts prices for two of its GPT-5.6 AI models (인하 배경·중국 모델 점유율)](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html)
- [[OpenAI] Ultrafast 모드 프리뷰 공지 (8월 13일·초당 750토큰)](https://openai.com/index/previewing-ultrafast/)
- [[TechCrunch] OpenAI introduces 'Ultrafast', a new mode that makes GPT-5.6 Sol work at 14x the speed](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/)
- [[Google] Gemini API 가격표 (비교에 쓴 Gemini 단가)](https://ai.google.dev/gemini-api/docs/pricing)
- [[The Korea Herald] OpenAI's Seoul debut (한국 법인·국내 협력)](https://www.koreaherald.com/article/10577647)
- 환율: 1달러 ≈ 1,420원 기준 환산
