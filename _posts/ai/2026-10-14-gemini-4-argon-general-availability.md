---
title: "Gemini 4 Argon 정식 출시 — 12월부터 API 요금 2배"
description: "Gemini 4 Argon 의 제공 범위와 확정된 도입가 종료일, 12월 이후 API 요금을 정리합니다"
date: 2026-10-14
category: AI
subcategory: News
tags: [google, gemini-4-argon, llm, pricing, api]
image: /assets/og/2026-10-14-gemini-4-argon-general-availability.png
---

Google이 2026년 10월 13일 Gemini 4 Argon을 정식 출시했습니다. 9월 30일 발표 때는 사이버 방어 기관에 먼저 제공한다고만 했는데, 2주 만에 Gemini 앱의 Google AI Pro·Ultra 구독자와 유료 API 이용자에게 제공되기 시작했어요.

발표 당시 공지되지 않았던 도입가 종료일도 확정됐습니다. API 요금은 **2026년 11월 30일**까지 100만 토큰당 입력 2,800원(2달러)·출력 1만 4,000원(10달러)이고, 12월 1일부터 입력·출력·캐시 단가가 모두 두 배로 인상돼요.

![Google 공식 블로그 Gemini 4 Argon 앱 출시 글](/assets/images/ai/gemini-4-argon-general-availability/01-capture.webp)
*Google 공식 블로그 Gemini 4 Argon 앱 출시 글 — 출처: Google*

## 정식 제공 범위

![Gemini 4 Argon 공식 키 아트](/assets/images/ai/gemini-4-argon-general-availability/02-photo-keyart.webp)
*Gemini 4 Argon 공식 키 아트 — 출처: Google*

| 경로 | 대상 | 비고 |
| :--- | :--- | :--- |
| Gemini 앱 | **AI Pro·Ultra 구독자** | 일부 국가 |
| Gemini API | 유료 티어 | 무료 티어 불가 |
| Antigravity·AI Studio | AI Ultra·기업 | 코딩 에이전트 |
| Fairwind 프로그램 | 사이버 방어 기관 | 9월 30일부터 |

9월 30일 발표에서 Google은 유료 API와 AI Ultra 구독자에게 먼저 제공하겠다고 했는데, 실제 출시에서는 Ultra보다 아래 등급인 AI Pro 구독자도 앱에서 쓸 수 있게 됐습니다. 미국 기준 AI Pro는 월 2만 8,000원(19.99달러)이에요.

한국에서 Gemini 앱으로 Argon을 쓸 수 있는지는 확인되지 않았습니다. Google One 요금제 페이지는 「일부 국가의 Google AI Pro 및 Ultra 구독자에게 제공」이라고만 적었고, 국가 목록은 공개하지 않았어요.

[Tasks 전환]
채팅창의 토글로 Tasks를 켜면 사용자가 자리를 비워도 Gemini가 작업을 이어서 수행함 (일부 국가·언어)

[Antigravity 코딩 화면]
macOS Gemini 앱 안에서 Google Antigravity의 에이전트 코딩 화면으로 바로 전환

[앱 연동 40여 개]
Instacart·OpenTable·Adobe·Shopify 등 외부 앱과 연결

Google은 Argon이 답변을 더 직접적으로 하고 같은 말을 반복하지 않으며, 긴 작업에서는 진행 상황을 더 자주 알려 준다고 설명했어요.

## API 요금, 12월 1일부터 두 배

![Gemini API 요금표의 Gemini 4 Argon 항목](/assets/images/ai/gemini-4-argon-general-availability/03-capture-api.webp)
*Gemini API 요금표의 Gemini 4 Argon 항목 — 출처: Google*

![Gemini 4 Argon API 도입가와 12월 정가 비교 차트](/assets/images/ai/gemini-4-argon-general-availability/04-chart.webp)
*Gemini 4 Argon API 도입가와 12월 정가 비교 차트 — 출처: Gemini API 요금표 기반 자가 렌더*

출력 단가에는 모델이 답변을 생성하기 전 내부 추론에 사용하는 thinking 토큰이 포함됩니다. 어려운 문제일수록 답변보다 thinking 토큰 사용량이 많아질 수 있어, 화면에 보이는 답변 길이만으로 요금을 추정하면 실제 청구액보다 적게 계산돼요.

한 달에 입력 1억 토큰과 출력 2,000만 토큰을 쓰면 요금이 56만 원에서 112만 원으로 늘어요.

| 구분 | 11월 30일까지 | 12월 1일부터 |
| :--- | :--- | :--- |
| 입력 1억 토큰 | 28만 원 | 56만 원 |
| 출력 2,000만 토큰 | 28만 원 | 56만 원 |
| 월 합계 | 56만 원 | <mark>112만 원</mark> |

4,096토큰이 넘는 프롬프트에는 암묵적 캐싱이 자동으로 적용되고, 캐시에 적중한 입력은 95% 할인됩니다. 같은 시스템 프롬프트나 문서를 반복해서 보내는 서비스라면 입력 비용은 계산 예시보다 훨씬 낮아져요. 대신 캐시를 직접 만드는 명시적 캐싱은 지원하지 않습니다.

급하지 않은 작업은 Batch·Flex를 쓰면 Standard의 절반 요금이고, 응답 속도를 보장받는 Priority는 Standard의 1.8배예요. 12월 이후 Batch 단가는 지금 Standard 단가와 같습니다.

9월 30일 발표 정리 글에서 비교한 GPT-6 Astra·Claude Opus 5.5 요금과 벤치마크는 아래 글에 있습니다.

🔗 링크 첨부 - https://blog.naver.com/rottensweetpotato/224429639264

## API 이용자 변경점

![한 번에 아주 긴 출력을 만드는 모델 개념 컷](/assets/images/ai/gemini-4-argon-general-availability/05-agy.webp)
*한 번에 아주 긴 출력을 만드는 모델 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

Argon은 입력·thinking·출력이 총 100만 토큰의 컨텍스트 한도를 공유합니다. 일반 요청의 출력 한도는 6만 5,536토큰이고, 백그라운드 실행(background)을 켜면 한 응답이 최대 100만 토큰까지 길어질 수 있어요. 이때 응답이 여러 단계로 분할돼 전송되므로 각 단계의 출력을 결합해야 합니다.

사고 수준(thinking_level)은 low·medium·high 세 단계이고 기본값은 medium입니다. Google은 세 단계를 모두 시험해 품질 기준을 넘는 가장 낮은 단계를 고르라고 권했어요.

10월 8일에는 Gemini 3.7 Flash와 3.5 Flash의 지원이 중단돼 요청이 3.8 Flash로 자동 전환되고, Deep Research 에이전트의 2025년 12월 미리보기 버전은 10월 23일 종료돼요.

![API 이용자가 확인할 다섯 가지 정리 카드](/assets/images/ai/gemini-4-argon-general-availability/06-items-api.webp)
*API 이용자가 확인할 다섯 가지 정리 카드 — 출처: Google Gemini API 문서 기반 자가 렌더*

## 앞으로 주목할 점

- Gemini 앱 Argon 제공 국가에 한국이 포함되는지와 한국어 Tasks 지원
- 12월 1일 정가 전환 뒤 Batch·Flex로 옮기는 이용자 비중
- 무료 티어와 AI Plus 요금제로 제공 범위가 넓어지는지
- OpenAI·Anthropic이 Argon 정가 전환에 맞춰 요금을 조정하는지

## 참고 출처

- [[Google] Gemini 4 Argon comes to the Gemini app (2026-10-13, 본문 이미지 출처)](https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/)
- [[Google] Gemini 4 Argon: Built to solve your hardest problems (2026-09-30, 본문 이미지 출처)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)
- [[Google AI for Developers] Gemini Developer API 요금 (본문 이미지 출처)](https://ai.google.dev/gemini-api/docs/pricing)
- [[Google AI for Developers] What's new in Gemini 4 Argon·모델 문서](https://ai.google.dev/gemini-api/docs/latest-model)
- [[Google AI for Developers] Gemini API 변경 내역 (2026-10-06~13)](https://ai.google.dev/gemini-api/docs/changelog)
- [[Google One] Google AI 요금제 (제공 국가 문구)](https://one.google.com/intl/ko_kr/about/google-ai-plans/)
- 환율: 1달러 ≈ 1,400원 기준 환산
