---
title: "Gemini 3.8 Flash — 43일 만의 세 번째 판, 단가는 그대로인데 청구서는 커집니다"
description: "6주 사이 Flash 가 세 번 나온 배경과, 같은 단가로 돌려도 비용이 늘어나는 이유를 점수표와 함께 정리합니다"
date: 2026-09-05
category: AI
subcategory: News
tags: [gemini, google-deepmind, llm-pricing, model-release, benchmark]
image: /assets/og/2026-09-05-gemini-38-flash-release-cadence.png
---

Google이 9월 2일 Gemini 3.8 Flash 를 공개했습니다. 7월 21일 3.6 Flash, 8월 13일 3.7 Flash 에 이어 43일 만에 나온 세 번째 판이에요.

100만 토큰당 단가는 세 판이 모두 같습니다. 그런데 같은 단가로 돌려도 청구서는 3.7 Flash 때보다 커집니다.

![Gemini 로고](/assets/images/ai/gemini-38-flash-release-cadence/01-hero-gemini-logo.webp)
*Gemini 로고 — 출처: Google*

## 43일 사이에 Flash 가 세 번 나왔습니다

Google DeepMind 가 2026년 9월 2일 Gemini 3.8 Flash 와 보안 전용 파생 모델인 Gemini 3.8 Flash Cyber 를 함께 공개했습니다. Flash 계열의 직전 두 판이 7월 21일과 8월 13일에 나왔으니, 3.6 Flash 에서 3.8 Flash 까지 43일이 걸린 셈이에요.

- 3.6 Flash에서 3.7 Flash까지 23일
- 3.7 Flash에서 3.8 Flash까지 20일
- 3.6 Flash에서 3.8 Flash까지 43일

간격이 줄고 있습니다. 벤치마크 측정 기관인 Artificial Analysis 는 3.8 Flash 를 소개하면서 4개월도 안 되는 사이에 나온 네 번째 Flash 라고 적었어요.

![Flash 세 판이 나온 날](/assets/images/ai/gemini-38-flash-release-cadence/02-chart-timeline.webp)
*Flash 세 판이 나온 날 — 출처: Google 공식 발표 기반 자가 렌더*

이렇게 빨리 나올 수 있는 이유는 매번 바닥부터 다시 학습하지 않기 때문입니다. 3.7 Flash 가 3.6 Flash 의 추론(inference) 기반에 알고리즘 개선을 얹은 판이었고, 3.8 Flash 도 새 기반 모델을 처음부터 학습한 것이 아니라 3.7 Flash 위에 얹은 판이라는 분석이 나왔습니다.

모델 ID 는 **gemini-3.8-flash**, 컨텍스트 윈도(context window, 한 번에 넣을 수 있는 입력 길이)는 100만 토큰, 한 번에 받을 수 있는 출력 상한은 6만 4,000 토큰입니다. 이 세 값은 3.7 Flash 와 같아요.

## Google이 내놓은 성적표

Google이 공개한 수치에서 3.8 Flash 는 3.7 Flash 를 모든 항목에서 앞섭니다. 폭이 큰 쪽은 자율 소프트웨어 엔지니어링과 다단계 추론이에요.

![3.7 Flash 대 3.8 Flash 공식 벤치마크](/assets/images/ai/gemini-38-flash-release-cadence/03-chart-bench.webp)
*3.7 Flash 대 3.8 Flash 공식 벤치마크 — 출처: Google 공식 발표 수치 기반 자가 렌더*

자율 코딩 과제인 *DeepSWE v1.1* 이 65.3%에서 73.7%로, 컴퓨터 조작 과제인 *OSWorld-2.0* 이 50.6%에서 59.0%로 올랐습니다. 어려운 생물 추론 문제를 모은 *BioMysteryBench* 상급 문항은 43.5%에서 56.5%로 가장 크게 뛰었어요.

프롬프트 인젝션(prompt injection, 입력에 숨긴 지시로 모델을 조종하는 공격) 방어도 함께 개선됐습니다. *Gray Swan* 측정에서 공격 성공률이 9.2%에서 **5.5%**로 내려갔어요.

경쟁 모델과 붙이면 결과가 갈립니다.

| 벤치마크 | 3.8 Flash (%) | Claude Opus 5 (%) |
|---|---|---|
| DeepSWE v1.1 | 73.7 | **74.0** |
| Terminal-bench 2.1 | <mark>89.4</mark> | 89.1 |
| Terminal-bench 4.0 | 19.1 | **51.8** |
| OSWorld-2.0 | 59.0 | **75.4** |
| HLE-Verified | <mark>54.9</mark> | 54.4 |

짧고 정형화된 과제에서는 Flash 같은 경량 모델이 최상위 모델과 소수점 차이까지 붙습니다. 반대로 *Terminal-bench 4.0* 처럼 수행 단계가 많은 과제로 가면 19.1% 대 51.8%로 벌어져요. 모델 규모 차이가 사라진 것이 아니라, 붙는 구간과 벌어지는 구간이 나뉜 것입니다.

## 제3자 측정은 조금 다르게 읽힙니다

Artificial Analysis 의 인텔리전스 인덱스에서 3.8 Flash 는 **59점**을 받아 196개 모델 가운데 17위에 올랐습니다. 비교 대상 모델의 중앙값은 36점이에요.

![Flash 세 판의 인텔리전스 인덱스](/assets/images/ai/gemini-38-flash-release-cadence/04-chart-index.webp)
*Flash 세 판의 인텔리전스 인덱스 — 출처: Artificial Analysis 수치 기반 자가 렌더*

세대마다 오르기는 하는데 폭은 3점에서 4점입니다. 6주 만에 판이 바뀌는 속도에 비하면 점수가 뛰는 폭은 완만해요.

같은 측정에서 눈에 띄는 것은 점수가 아니라 그 점수를 내는 데 쓴 자원입니다.

| 지표 | 3.8 Flash | 비교 모델 중앙값 |
|---|---|---|
| 인텔리전스 인덱스 | <mark>59</mark> | 36 |
| 인덱스 완주 출력 토큰 | **1억 2,000만** | 7,100만 |
| 첫 토큰까지 (초) | **13.30** | 2.99 |

인덱스를 다 푸는 데 출력 토큰을 1억 2,000만개 썼습니다. 비교 대상 모델의 중앙값보다 약 70% 많은 양이고, 3.7 Flash 와 같은 과제로 비교하면 대략 30% 더 씁니다.

Gemini 3.x 계열은 답을 내기 전에 생각 토큰(thinking token)을 먼저 쓰고, 그 분량은 응답으로 돌아오지 않으면서 **출력 토큰과 합산돼 과금**됩니다. 더 오래 생각하는 모델은 단가가 같아도 청구서가 커져요.

실제로 인덱스 한 벌을 돌리는 데 든 비용은 **117만 3,000원(825.83달러)**, 과제 하나당 824원(0.58달러)이었습니다. 출력 속도 자체는 초당 302.1 토큰으로 전체 3위였는데, 첫 토큰이 나오기까지는 13.30초가 걸렸어요. 비교 대상 모델 중앙값 2.99초의 약 4.5배입니다.

빠른 모델이라는 이름과 달리, 사람이 화면 앞에서 기다리는 자리에는 기본 설정 그대로 넣기 어려운 수치입니다.

## MINIMAL 은 3.8 에서도 돌아오지 않았습니다

지난 8월 3.7 Flash 실측에서 가장 큰 변화는 성능이 아니라 생각의 양을 고르는 등급이 하나 사라진 것이었습니다. 생각 토큰을 아예 0개로 두는 **MINIMAL** 이 3.6 Flash 까지만 있고 3.7 Flash 에서 빠지면서, 답이 정해진 대량 분류 작업의 비용이 7.8배로 뛰었어요.

[Gemini 3.7 Flash — 생각의 양을 숫자에서 등급으로 바꿨습니다](/posts/gemini-37-flash-thinking-levels/)

3.8 Flash 도 그대로입니다. 공식 문서는 **minimal 등급은 Gemini 3.8 Flash 에서 지원되지 않으며 오류를 반환한다** 고 명시해 뒀어요.

| 모델 | 받는 등급 | 기본값 |
|---|---|---|
| Gemini 3.8 Flash | <mark>LOW 이상 3단</mark> | MEDIUM |
| Gemini 3.7 Flash | LOW 이상 3단 | MEDIUM |
| Gemini 3.6 Flash | **MINIMAL 포함 4단** | MEDIUM |

![세대가 올라갈수록 생각의 양이 늘어난다는 개념](/assets/images/ai/gemini-38-flash-release-cadence/05-agy-thinking.webp)
*세대가 올라갈수록 생각의 양이 늘어난다는 개념 — 출처: 개념 컷 · agy 자가 생성*

여기에 3.8 Flash 는 같은 등급에서 더 많이 생각합니다. 등급이 줄어든 상태에서 등급당 소모량까지 늘었으니, 대량 처리 쪽 비용은 3.7 Flash 때보다 한 번 더 올라가는 구조예요.

Google도 이 점을 숨기지 않았습니다. 공식 발표문은 **연산 효율이 가장 중요한 제약인 곳에서는 더 낮은 effort 등급을 쓰거나 Gemini 3.7 Flash 를 계속 쓰라** 고 적었어요. 새 모델을 내면서 이전 모델을 남겨 두라고 안내한 것입니다.

## 단가는 같은데 할인 기간만 짧아집니다

3.8 Flash 의 도입가는 입력 100만 토큰당 **1,065원(0.75달러)**, 출력 100만 토큰당 **5,325원(3.75달러)** 입니다. 3.7 Flash 와 3.6 Flash 의 도입가와 똑같은 값이에요. 캐시에서 읽는 입력은 107원(0.075달러)입니다.

도입가가 끝나는 날짜도 세 판 모두 **2026년 12월 31일**로 같습니다. 2027년 1월 1일부터 입력 2,130원(1.50달러), 출력 1만 650원(7.50달러)으로 두 배가 됩니다.

![출시일부터 도입가 만료일까지 남은 기간](/assets/images/ai/gemini-38-flash-release-cadence/06-chart-promo.webp)
*출시일부터 도입가 만료일까지 남은 기간 — 출처: Google 공식 가격표 기반 자가 렌더*

만료일이 고정된 채로 출시일만 뒤로 밀리니, 새 판일수록 할인을 받는 기간이 짧습니다. 3.6 Flash 는 163일, 3.7 Flash 는 140일, 3.8 Flash 는 120일이에요. 같은 가격표를 받았어도 3.8 Flash 로 갈아탄 쪽이 실제로 누리는 할인은 3.6 Flash 를 쓰던 쪽의 4분의 3 수준입니다.

국내에서 개발자는 Gemini API 와 Google AI Studio, Vertex AI 에서 바로 부를 수 있고, 일반 사용자는 Gemini 앱과 Google 검색 AI 모드, Google 스프레드시트에서 쓰게 됩니다.

다만 Gemini 앱에서는 Google AI Pro 이상 구독자에게 먼저 열립니다. Google AI Pro 의 국내 구독료는 월 **29,000원**이고, 그 아래 Google AI Plus 는 월 7,500원이에요. Ultra 요금은 국내 정리마다 값이 갈려서 공식 구독 페이지에서 확인하는 편이 정확합니다.

## 3.8 Flash Cyber 는 신청해야 씁니다

같은 날 나온 Gemini 3.8 Flash Cyber 는 API 가격표에 올라오는 모델이 아닙니다. Google이 함께 연 **Fairwind Program** 을 통해서만 접근이 열려요.

![CyberGym 취약점 탐지 성적](/assets/images/ai/gemini-38-flash-release-cadence/07-chart-cyber.webp)
*CyberGym 취약점 탐지 성적 — 출처: Google 공식 발표 수치 기반 자가 렌더*

취약점 탐지 과제인 *CyberGym* 에서 pass@1 86.2%로 GPT-5.5 Cyber(85.6%)와 Claude Mythos 5(83.8%)를 앞섰습니다. 패치 생성 과제인 *CWE-Bench* 에서는 47.2%로, 선도 모델의 47.8%에 근접했어요. 20개 프로그래밍 언어를 대상으로 한 Google 내부 측정에서는 성공률이 70%를 넘었다고 밝혔습니다.

접근 조건이 까다롭습니다. Fairwind Program 은 공개 셀프 가입 창구가 없고 건별로 승인해요.

- 정부기관과 국가 사이버 당국
- 의료·통신·에너지·금융 등 핵심 인프라 운영자
- 핵심 기술 플랫폼, Google Cloud 고객과 보안 파트너

승인받은 조직은 운영 요건도 함께 지켜야 합니다. 접근을 사내 보안·침해대응·모의해킹 팀으로 제한하고, 다중 인증(MFA)을 적용하는 것이 최소 기준이에요.

프로그램은 취약점을 찾고 고치는 CodeMender 하니스와 묶여 있습니다. 승인받은 조직은 자기 클라우드 안에서 검증된 패치를 만들어 볼 수 있어요.

Google은 전 세계에서 650곳이 넘는 파트너가 참여한다고 밝혔는데, 국내 기관의 승인 사례는 공개된 것이 없습니다.

## 그래서 지금 무엇을 쓰고 무엇을 기다릴까

성능이 오른 것도, 단가가 그대로인 것도 사실입니다. 다만 같은 단가로 더 많은 토큰을 쓰는 모델이라 실제 지출은 작업 성격에 따라 갈려요.

![지금 고를 때 기준 넷](/assets/images/ai/gemini-38-flash-release-cadence/08-items.webp)
*지금 고를 때 기준 넷 — 출처: 본문 정리 · 자가 렌더*

앞으로 확인할 신호도 몇 가지 남아 있습니다.

- 12월 31일 도입가 만료 이후 Google이 연장할지, 그대로 두 배로 올릴지
- 20일까지 좁혀진 간격이 유지되는지, 다음 Flash 가 언제 나오는지
- 대량 처리용으로 MINIMAL 등급을 받는 Lite 계열이 3.8 세대에도 나오는지
- Fairwind Program 에 국내 기관이나 인프라 사업자가 포함되는지

6주에 세 번이면 벤치마크 표를 외우는 것보다, 지금 돌리는 작업이 어느 쪽 구간에 있는지를 아는 편이 오래 갑니다.

## 참고 출처

- [[Google] Introducing Gemini 3.8 Flash and 3.8 Flash Cyber (공식 발표·가격·권장 사용처, 2026-09-02)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- [[Google] Fairwind Program (Cyber 접근 조건·CodeMender·파트너 규모, 2026-09-02)](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)
- [[Google] What's new in Gemini 3.8 Flash (모델 ID·컨텍스트·thinking_level 등급, 2026-09)](https://ai.google.dev/gemini-api/docs/latest-model)
- [[Artificial Analysis] Gemini 3.8 Flash 측정 (인덱스 점수·출력 토큰·과제당 비용)](https://artificialanalysis.ai/articles/gemini-3-8-flash)
- [[Vellum] Gemini 3.8 Flash & 3.8 Flash Cyber Benchmarks Explained (3.7 대비·경쟁 모델 수치 정리)](https://www.vellum.ai/blog/gemini-3-8-flash-benchmarks-explained)
- [[eesel AI] Gemini 3.8 Flash review 2026 (첫 토큰 지연·토큰 소모 해설)](https://www.eesel.ai/blog/gemini-3-8-flash)
- [[9to5Google] Gemini 3.7 Flash launches three weeks after last model (3.7 Flash 출시일, 2026-08-13)](https://9to5google.com/2026/08/13/gemini-3-7-flash-launch/)
- [[Google One 고객센터] Google AI Pro 멤버십 가입하기 (국내 구독료)](https://support.google.com/googleone/answer/16476811?hl=ko)
- 환율: 1달러 ≈ 1,420원 기준 환산
- 벤치마크: 비교표 수치는 Google 공식 발표의 경쟁 모델 비교표 기준이다. Cloud 개발자 가이드의 세대 비교표는 같은 Terminal-bench 2.1 을 90.8%(3.7 Flash 81.6%)로 적어, 표가 다르면 값도 다르다
