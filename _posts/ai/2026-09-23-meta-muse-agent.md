---
title: "Meta Muse — 일을 대신 처리하는 개인 AI 에이전트"
description: "이메일 발송·예약·결제까지 맡는 Meta 의 개인 에이전트 Muse 의 요금제와 개인정보 구조, 기반 모델 Muse Spark 1.3 을 정리합니다"
date: 2026-09-23
category: AI
subcategory: News
tags: [meta, muse, ai-agent, muse-spark, privacy]
image: /assets/og/2026-09-23-meta-muse-agent.png
---

Meta가 2026년 9월 8일 개인 AI 에이전트 Muse를 공개했습니다. 질문에 답하는 챗봇이 아니라 이메일을 보내고 여행을 예약하고 요금을 낮추는 일까지 대신 처리하는 에이전트로, 미국에서 먼저 출시됐어요.

Muse라는 이름은 Meta 초지능 연구소(MSL)의 모델 Muse Spark와 8월 5일 공개한 코딩 도구 Muse Code에도 쓰였습니다. 가장 최근에 발표된 것이 에이전트 Muse이고, 그 기반 모델의 새 버전 Muse Spark 1.3은 6일 앞선 9월 2일에 공개됐어요.

![Meta Muse 공식 소개 이미지](/assets/images/ai/meta-muse-agent/01-hero-muse.webp)
*Meta Muse 공식 소개 이미지 — 출처: Meta*

## Muse의 정체

Meta는 Muse를 *a secure, private personal AI agent that proactively helps with people's goals*, 즉 사람의 목표를 먼저 파악해 돕는 개인 AI 에이전트라고 소개했습니다. 기반 모델은 Meta가 가장 성능이 높다고 밝힌 Muse Spark예요.

- 대화 방식: 메시지를 주고받듯 일을 맡기고, 에이전트 이름·아바타·말투를 사용자가 정함
- 먼저 제안: 사용자에게 중요한 것을 기억하고, 사용자가 묻지 않아도 제안
- 장시간 작업: 앱을 닫아도 계속 일하고, 상황이 바뀌면 다시 알림
- 저장 콘텐츠 활용: 저장해 둔 레시피 릴스를 장보기 목록으로 바꾸는 식

TechCrunch는 Muse가 할 수 있는 일로 이메일 발송, 여행 예약, 요금 인하 협상, 양식 작성, 계획 수립, 구매를 꼽았어요.

## 작동 구조

![에이전트 전용 가상 머신 개념 컷](/assets/images/ai/meta-muse-agent/02-agy.webp)
*에이전트 전용 가상 머신 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

Muse는 Meta 클라우드의 **Muse Secure VM**이라는 전용 가상 머신에서 실행됩니다. 에이전트와 사용자 데이터가 이 가상 머신 안에 함께 있고, 에이전트는 내장 브라우저를 열어 웹사이트에서 양식을 채우고 사용자를 대신해 협상도 해요. 브라우저 화면은 사용자에게 보입니다.

Gmail·캘린더·결제 연동은 기본으로 제공되고, 공개 API가 없는 서비스는 사용자가 제공한 계정 정보로 브라우저에서 접속합니다. 모든 작업 기록은 사용자가 볼 수 있게 남아요.

## 쓰는 법과 요금

Muse는 웹 muse.ai, iOS·Android 앱, WhatsApp 채팅에서 쓸 수 있고, Meta의 AI 안경에도 곧 지원될 예정입니다. 출시 지역은 미국이에요.

| 요금제 | 월 요금 |
| :--- | :--- |
| 무료 | 0원 |
| Power | 2만 8,000원(20달러) |
| Maximum | **14만 원(100달러)** |

Meta는 대부분의 용도는 무료로 충분하고, 더 많이 쓰는 사람을 위해 유료 요금제를 제공한다고 밝혔어요. 요금제별 사용 한도는 공개된 자료에서 확인되지 않았습니다.

![Stripe 로고](/assets/images/ai/meta-muse-agent/03-logo-stripe.webp)
*Stripe 로고 — 출처: Stripe*

구매는 Stripe의 간편 결제 Link로 처리하고, Shopify의 Shop Pay도 곧 지원한다고 Meta는 밝혔습니다.

## 개인정보와 안전장치

Meta는 Muse가 사용자의 비밀번호와 결제 수단을 볼 수 없고, 대화와 데이터를 Meta 광고 시스템과 공유하지 않는다고 밝혔어요.

| 장치 | 내용 |
| :--- | :--- |
| 연결 권한 | 사용자가 앱별 연결과 접근 범위 설정 |
| 민감 작업 확인 | **이메일 발송·구매 전 사용자 확인** |
| 작업 기록 | 모든 행동의 기록 제공 |
| Confidential VM | 2026년 안에 도입 예정 |

Confidential VM은 가상 머신 전체를 사용자만 가진 키로 암호화해 Meta도 데이터와 대화를 볼 수 없게 하는 방식이에요. 출시 시점에는 아직 적용되지 않았습니다.

TechCrunch는 Meta가 2011년과 2019년 미국 연방거래위원회(FTC)와 개인정보 문제로 합의했고, Cambridge Analytica 사건을 겪었다는 점을 들어 소비자가 이메일·결제 권한을 넘길지가 관건이라고 짚었어요.

## 기반 모델 Muse Spark 1.3

![Artificial Analysis 지능 지수 비교](/assets/images/ai/meta-muse-agent/04-chart.webp)
*Artificial Analysis 지능 지수 비교 — 출처: Artificial Analysis 지수 기반 자가 렌더*

Meta는 9월 2일 Muse Spark 1.3을 공개했고, Mark Zuckerberg는 코딩 능력이 가장 크게 향상됐다고 설명했습니다. VentureBeat가 인용한 Artificial Analysis 지능 지수는 xhigh 설정 기준 61로, Claude Opus 5와 같고 GPT-5.6 Sol(max, 62)보다 1점 낮아요.

Meta가 공개한 점수 가운데 가장 높은 결과는 max 설정에서 나왔는데, 이 설정은 안전성 시험을 마치지 않아 일부 파트너에게만 제공됩니다. 비교 대상도 1.2의 xhigh 설정이라 세대 차이만으로 해석하기는 어렵다고 VentureBeat는 지적했어요.

API 요금은 100만 토큰당 입력 1,750원(1.25달러), 출력 5,950원(4.25달러)으로 1.2와 같습니다.

## 국내 접점

Muse는 미국에서만 출시됐고, Meta는 국내 출시 일정을 밝히지 않았습니다. 국내 사용자는 muse.ai와 앱을 쓸 수 없어요.

Muse Spark 1.3 모델은 Meta Model API로 쓸 수 있어, 국내 개발자는 요금표대로 모델을 먼저 시험해 볼 수 있습니다.

결제 연동에 쓰이는 Stripe Link와 Shop Pay가 국내 쇼핑몰에서 널리 쓰이지 않아, 국내에 출시되더라도 지원되는 결제 수단은 달라질 수 있어요.

## 정리

![Meta Muse 정리 카드](/assets/images/ai/meta-muse-agent/05-items.webp)
*Meta Muse 정리 카드 — 출처: Meta 발표 기반 자가 렌더*

## 앞으로 주목할 점

- Confidential VM: Meta가 2026년 안에 도입하겠다고 밝힌 암호화 가상 머신의 출시
- AI 안경: Meta가 곧 지원한다고 밝힌 AI 안경 연동
- Shop Pay: Stripe Link에 이어 지원 예정인 결제 수단
- max 설정: 안전성 시험 중인 Muse Spark 1.3 max 설정의 일반 공개

## 참고 출처

- [[Meta] Introducing Muse, 개인 AI 에이전트 공식 발표 (2026-09-08)](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
- [[TechCrunch] Muse 요금제·연동·신뢰 문제 (2026-09-08)](https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/)
- [[Axios] Muse 출시와 가상 머신 구조 (2026-09-08)](https://www.axios.com/2026/09/08/meta-debuts-muse-personal-ai-agent)
- [[VentureBeat] Muse Spark 1.3 성능과 max 설정 제한 (2026-09)](https://venturebeat.com/technology/meta-says-muse-spark-1-3-has-frontier-performance-but-its-best-results-come-from-a-model-developers-cant-broadly-use-yet)
- [[CNBC] Muse Code 공개 (2026-08-05)](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html)
- 환율: 1달러 ≈ 1,400원 기준 환산
