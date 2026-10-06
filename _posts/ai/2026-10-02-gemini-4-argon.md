---
title: "Gemini 4 Argon 공개 — 출력 한도 100만 토큰, 사이버 방어 기관에 먼저"
description: "Gemini 4 계열 첫 모델 Argon 의 출력 한도·벤치마크·도입가와, 사이버 방어 기관부터 여는 단계적 제공 방식을 정리합니다"
date: 2026-10-02
category: AI
subcategory: News
tags: [gemini, google-deepmind, gemini-4-argon, model-release, cybersecurity]
image: /assets/og/2026-10-02-gemini-4-argon.png
---

Google이 2026년 9월 30일 Gemini 4 계열의 첫 모델 **Gemini 4 Argon**을 발표했습니다. 한 번에 생성할 수 있는 출력 한도를 6만 4,000토큰에서 100만 토큰으로 늘린 것이 가장 큰 변화예요.

다만 아직 누구나 쓸 수 있는 모델은 아닙니다. Google은 사이버 방어 기관에 먼저 제공하고, 미국 정부의 출시 전 검증 절차를 거친 뒤 유료 API와 Google AI Ultra 구독자에게 제공하겠다고 밝혔어요.

![Gemini 4 Argon 발표 키 아트](/assets/images/ai/gemini-4-argon/01-hero-keyart.webp)
*Gemini 4 Argon 발표 키 아트 — 출처: Google*

## 발표 내용

Google DeepMind의 Koray Kavukcuoglu 수석부사장이 Google 공식 블로그에 직접 발표했습니다. Argon은 실제 소프트웨어 개발, 법률·금융 같은 기업 지식 업무, 사이버 방어를 겨냥한 모델이에요.

- 출력 한도: 6만 4,000토큰에서 **100만 토큰**으로 확대
- 도입가: 100만 토큰당 입력 2,800원(2달러), 출력 1만 4,000원(10달러)
- 공개 순서: Fairwind 프로그램 참여 기관 → 유료 API·Google AI Ultra
- 사내 사용: 수천 명의 Google 직원이 이미 업무에 사용 중

출시일은 밝히지 않았습니다. Google은 「가능한 한 빨리」 개발자·기업·일반 이용자에게 공개하겠다고만 적었어요.

## 벤치마크

![Gemini 4 Argon 공식 벤치마크 비교표](/assets/images/ai/gemini-4-argon/02-photo.webp)
*Gemini 4 Argon 공식 벤치마크 비교표 — 출처: Google*

Google은 19개 항목에서 Argon을 GPT-6 Astra, Claude Fable 5.1, Claude Opus 5.5와 비교했습니다. Argon이 13개 항목에서 단독 1위, CWE-bench v1에서 공동 1위였고, GPT-6 Astra가 3개, Claude Opus 5.5가 2개 항목에서 앞섰어요.

차이가 가장 큰 항목은 법률 에이전트 평가인 Harvey's Legal Agent Benchmark로, Argon 19.6%에 2위 Claude Fable 5.1이 6.7%였습니다. 업무 자동화를 보는 AutomationBench는 Argon 51.3%, Claude Opus 5.5 42.5%로 8.8%포인트 차이였어요.

코딩 벤치마크 DeepSWE v1.1은 77.9%로 Claude Opus 5.5(74.2%)와 GPT-6 Astra(74.1%)보다 3%포인트 넘게 높았습니다. 9월 29일 나온 GPT-6.1 Sol은 이 표에 없고, OpenAI가 발표한 Sol의 같은 벤치마크 점수는 75.2%예요.

### Argon 점수가 더 낮은 항목

| 벤치마크 | Argon | 1위 |
| :--- | :--- | :--- |
| FrontierSWE v2 | 55.0% | Astra **65.5%** |
| Terminal-Bench Science | 57.6% | Astra **68.1%** |
| Terminal-bench 4.0 | 57.4% | Opus 5.5 **66.4%** |
| PostTrainBench | 45.3% | Opus 5.5 **49.3%** |
| OSWorld-2.0 | 69.2% | Astra **72.6%** |

점수가 더 낮은 다섯 개 중 세 개가 터미널·컴퓨터를 직접 조작하는 환경의 평가였습니다. 점수는 모두 Google이 직접 측정한 값이고, 평가 방법은 Google DeepMind 누리집에 따로 공개됐어요.

## 출력 100만 토큰

출력 한도는 모델이 한 번의 응답에서 생성할 수 있는 토큰(token, 모델이 글을 처리하는 단위) 수입니다. 입력으로 받을 수 있는 양을 뜻하는 컨텍스트 윈도와는 다른 값이에요.

Google은 출력 한도를 늘린 이유로 한 번의 추론 흐름에서 수십만 토큰을 생성하며 문제를 끝까지 푸는 작업을 들었습니다. 코드베이스 전체를 다른 언어로 변환하거나 여러 문서를 한 번에 감사하는 일이 예로 나왔어요.

### Google 사내 사례

[libgav1 영상 디코더]
SIMD 코드 3만 2,000줄을 안전한 Rust로 변환해 기존 Rust 이식판보다 2.7배 빠르게

[Fuchsia Zircon 커널]
80만 줄 넘는 C/C++를 Rust로 변환하는 작업 진행, 배포 전 검증 단계

[데이터센터 메모리]
전사 프로파일링 자료를 분석해 300TiB 넘는 메모리 확보

## 사이버 방어 기관 먼저

Argon을 먼저 제공하는 대상은 Google이 9월 2일 Gemini 3.8 Flash Cyber와 함께 시작한 **Fairwind 프로그램**입니다. 정부기관, 핵심 기반시설 운영사, 소프트웨어 관리자 등 Google이 심사해 선정한 방어 조직만 참여할 수 있어요.

Google은 이 참여 기관과 사내 팀에는 Argon을 **사이버 보안 제한 없이** 제공한다고 밝혔습니다. 취약점을 발견하고 검증하고 수정하는 능력을 제한 없이 쓰게 하겠다는 것이고, 일반 공개 전에는 이들의 피드백으로 보안 제한을 조정하겠다고 했어요.

![CWE-bench v1 리더보드](/assets/images/ai/gemini-4-argon/03-photo-cwebench.webp)
*CWE-bench v1 리더보드 — 출처: Google*

취약점을 고치는 능력을 보는 CWE-bench v1에서 Argon은 68%로, Grok 4.7·GPT-6 Astra와 같은 점수를 받았습니다. 클라우드 보안 기업 Wiz는 무료 공공 인프라 보호 활동에 Argon을 써서, 전 세계 병원이 쓰는 의료 소프트웨어에서 민감한 개인정보가 노출되는 심각한 취약점을 발견했다고 Google은 전했어요.

Google 모델의 보안 관련 행동은 직전에도 보도됐습니다. 9월 18일 Google은 Gemini가 외부 업체 Irregular의 해킹 평가 중 실제 회사 세 곳의 시스템에 접근한 일을 시인했어요.

## 안전장치

Google은 출시 전 검증을 위해 미국 정부의 자발적 사전 모델 접근 절차에 참여하고 있다고 밝혔습니다. 안전장치는 악용 방지, 프롬프트 인젝션 방어, 정렬 이탈 감시 등으로 나눠 설명했어요.

- 악용 방지: 사이버·화생방(CBRN) 공격 요청은 거절하고, 모델 내부 활성값을 감시해 오용을 찾아냄
- 정렬 이탈 감시: 사용자 의도를 넘는 방식으로 과제를 수행하려는 행동을 차단하는 기능 적용

![Gray Swan 간접 프롬프트 인젝션 공격 성공률](/assets/images/ai/gemini-4-argon/04-photo-grayswan.webp)
*Gray Swan 간접 프롬프트 인젝션 공격 성공률 — 출처: Google*

웹페이지나 문서에 삽입된 지시로 모델을 조종하는 **간접 프롬프트 인젝션(prompt injection)**은 Gray Swan 평가로 쟀습니다. 공격을 15번 시도했을 때 성공률이 Argon 0.7%로, Claude Opus 5.5와 Claude Fable 5.1(각 1.0%)보다 낮았어요.

## 요금

![출력 100만 토큰당 API 요금 비교](/assets/images/ai/gemini-4-argon/05-chart.webp)
*출력 100만 토큰당 API 요금 비교 — 출처: Google·OpenAI·Anthropic 공식 요금 기반 자가 렌더*

| 구분 | 입력 | 출력 |
| :--- | :--- | :--- |
| Argon 도입가 | 2,800원 | **1만 4,000원** |
| Argon 정가 | 5,600원 | 2만 8,000원 |
| 캐시 입력 (도입가) | 140원 | - |

단위는 100만 토큰당입니다. 도입가는 GPT-6.1 Sol의 표준 요금과 같고, 도입 기간이 끝난 뒤의 정가는 Claude Opus 5.5와 같아요. 도입 기간이 언제 끝나는지는 발표되지 않았습니다.

캐시 입력은 같은 앞부분을 반복해서 보낼 때 부과되는 요금으로, 입력 요금에서 95% 할인됩니다. 출력 요금만 보면 GPT-6 Astra(7만 원)의 5분의 1이에요.

## 국내 이용

Argon은 국내를 포함해 일반 공개 전입니다. Fairwind 프로그램에 국내 기관이 참여하는지는 밝혀지지 않았어요.

공개되면 유료 Gemini API와 Google AI Ultra 구독이 첫 이용 경로입니다. Google은 5월 I/O에서 AI Ultra를 월 14만 원(100달러)과 28만 원(200달러) 두 등급으로 개편했고, API는 달러로 청구돼 원화 부담은 환율에 따라 달라져요.

## 앞으로 주목할 점

- 유료 API·AI Ultra 공개 일정과 도입가 적용 기간
- 보안 제한을 적용한 일반 공개판의 보안 관련 응답 범위
- 외부 기관의 독립 벤치마크 결과

## 참고 출처

- [[Google] Gemini 4 Argon: our next era of frontier intelligence (2026-09-30, 요금·공개 순서·벤치마크, 본문 이미지 4점 출처)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- [[Google DeepMind] Gemini 4 Argon 평가 방법](https://deepmind.google/models/evals-methodology/gemini-4-argon)
- [[VentureBeat] Google unveils Gemini 4 Argon, but in limited release (2026-09-30)](https://venturebeat.com/technology/google-unveils-gemini-4-argon-retaking-benchmark-lead-over-openai-and-anthropic-but-in-limited-release)
- [[Anthropic] Claude API 요금 (Claude Opus 5.5)](https://platform.claude.com/docs/en/about-claude/pricing)
- [[Google 한국 블로그] 구글 I/O 2026 구글 AI 구독 (2026-05-19, AI Ultra 등급)](https://blog.google/intl/ko-kr/company-news/technology/google-ai-subscriptions-kr/)
- 환율: 1달러 ≈ 1,400원 기준 환산
