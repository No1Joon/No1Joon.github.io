---
title: "Gemini 4 Argon 외부 평가 — Vals 1위·지능 지수 53점"
description: "정식 출시 뒤 나온 Vals AI 와 Artificial Analysis 의 독립 평가 결과와 과제당 비용을 경쟁 모델과 비교합니다"
date: 2026-10-17
category: AI
subcategory: News
tags: [google, gemini-4-argon, benchmark, vals-ai, artificial-analysis]
image: /assets/og/2026-10-17-gemini-4-argon-independent-evals.png
---

Gemini 4 Argon이 2026년 10월 13일 정식 출시됐어요
그 뒤 외부 평가 기관의 점수가 나오기 시작했습니다
9월 30일 발표 때 Google이 공개한 벤치마크는 자체 측정이었습니다
독립 평가 두 곳의 결과는 엇갈렸어요
Vals AI 종합 지수에서는 **1위**였어요
Artificial Analysis 지능 지수에서는 <mark>53점</mark>으로 1위 58점보다 5점 낮아요

![Google이 9월 30일 공개한 Gemini 4 Argon 자체 벤치마크표](/assets/images/ai/gemini-4-argon-independent-evals/01-photo.webp)
*Google이 9월 30일 공개한 Gemini 4 Argon 자체 벤치마크표 — 출처: Google*

## Artificial Analysis 지능 지수

![Artificial Analysis 지능 지수 모델별 비교 차트](/assets/images/ai/gemini-4-argon-independent-evals/02-chart.webp)
*Artificial Analysis 지능 지수 모델별 비교 차트 — 출처: Artificial Analysis 리더보드 기반 자가 렌더*

**Artificial Analysis**는 여러 벤치마크 결과를 하나의 지수로 산출하는 독립 평가 기관이에요
Argon은 추론 수준 high 설정에서 53점을 받았습니다
모델별 최고 설정의 점수를 비교하면 Claude Opus 5.5가 58점으로 1위예요
Claude Sonnet 5.5와 Muse Wonder Full이 56점으로 공동 2위입니다
Argon은 GPT-6 Astra, Claude Fable 5.1과 같은 53점이에요

### 53점 모델의 과제당 비용

![지능 지수 과제 1건당 비용 비교 차트](/assets/images/ai/gemini-4-argon-independent-evals/03-chart.webp)
*지능 지수 과제 1건당 비용 비교 차트 — 출처: Artificial Analysis 리더보드 기반 자가 렌더*

Argon은 지수 과제 1건에 약 2,790원(1.99달러)이 들었습니다
같은 53점인 GPT-6 Astra max는 4,560원이에요
Claude Fable 5.1 max는 1만 680원이 들었습니다
<mark>같은 53점에 든 비용은 GPT-6 Astra의 61%였어요</mark>
다만 Claude Opus 5.5 high 설정은 과제당 2,550원에 54점이었습니다
Argon이 비용 대비 점수가 가장 높은 모델은 아니에요

### 속도

출력 속도는 초당 99.5토큰으로 비교 대상 중앙값 86.1토큰보다 빨랐어요
첫 토큰이 나오기까지는 **44.7초**가 걸렸습니다
비교 대상 중앙값 3.94초의 11배예요!
답을 내기 전에 추론에 쓰는 시간이 길다는 뜻입니다

## Vals AI 종합 지수

![Vals AI 종합 지수 상위 4개 모델 비교 차트](/assets/images/ai/gemini-4-argon-independent-evals/04-chart-vals.webp)
*Vals AI 종합 지수 상위 4개 모델 비교 차트 — 출처: Vals AI 모델 페이지 기반 자가 렌더*

**Vals AI**는 금융·법률·의료·코딩처럼 업무형 과제로 모델을 평가하는 기관이에요
Argon은 종합 지수 68.90%로 <mark>1위</mark>를 기록했습니다
Claude Sonnet 5.5가 67.04%, Opus 5.5가 66.97%로 2·3위예요
Argon으로 전체 평가를 한 번 수행하는 비용은 약 2만 1,950원으로 가장 적었습니다
Claude Opus 5.5는 약 4만 5,000원이 들었어요

### 항목별 순위

| 벤치마크 | 점수 | 순위 |
| :--- | :--- | :--- |
| Finance Agent v2 | 65.40% | <mark>1위</mark> / 78 |
| IOI (정보올림피아드) | 100% | 1위 / 44 |
| Code Migration | 68.17% | 2위 / 77 |
| Terminal-Bench 4.0 | 57.58% | 6위 / 48 |
| Vibe Code Bench 1-100 | 21.20% | 8위 / 25 |
| CUA-bench | 4.83% | **8위** / 9 |

IOI 100%는 GPT-6 Astra와 같은 점수입니다
화면을 보고 컴퓨터를 조작하는 **CUA-bench**에서는 9개 모델 중 8위에 그쳤어요
이 항목을 한 번 평가하는 데 약 27만 1,300원이 들어 비용도 가장 컸습니다
Code Migration·Vibe Code Bench v1.1은 Sonnet 5.5가 더 높았어요

## Google 자체 수치와 외부 측정

![자체 벤치마크와 독립 평가를 대조하는 개념 컷](/assets/images/ai/gemini-4-argon-independent-evals/05-agy.webp)
*자체 벤치마크와 독립 평가를 대조하는 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

Google이 9월 30일 공개한 Argon의 Terminal-bench 4.0 점수는 57.4%였어요
Vals AI가 따로 잰 점수는 57.58%로 <mark>거의 같았습니다</mark>
Google 자체 벤치마크에서 이 항목 1위는 Claude Opus 5.5의 66.4%였어요

🔗 링크 첨부 - https://blog.naver.com/rottensweetpotato/224429639264

### 실사용 반응

경향신문은 글쓰기와 논리적 추론에 호평이 많고 코딩 평가는 엇갈린다고 전했어요
Hacker News의 한 이용자는 코딩을 뺀 모든 작업에 Argon을 쓰겠다고 했습니다
간단한 질문에도 사용 한도가 빨리 소진된다는 불만도 나왔어요
Google은 사내 개발팀의 AI 작성 코드 제출이 35% 넘게 늘었다고 밝혔습니다
수정 뒤 코드를 되돌리는 사례는 약 3분의 1 줄었다고 해요

## 국내 이용 현황

![국내 Gemini 앱과 ChatGPT 월간 활성 이용자 비교 차트](/assets/images/ai/gemini-4-argon-independent-evals/06-chart-mau.webp)
*국내 Gemini 앱과 ChatGPT 월간 활성 이용자 비교 차트 — 출처: 와이즈앱·리테일 기반 자가 렌더*

와이즈앱·리테일 집계로 국내 Gemini 앱 월간 활성 이용자는 3월 772만 명이었어요
7월에는 947만 명으로 175만 명 늘었습니다
그 뒤 두 달 동안은 40만 명 증가에 그쳤어요
9월 국내 ChatGPT 이용자는 2,470만 명으로 Gemini의 약 <mark>2.5배</mark>입니다
Argon은 Gemini 앱에서 Google AI Pro·Ultra 구독자만 쓸 수 있어요
Google 공지는 제공 국가를 따로 밝히지 않았습니다
한국어 전용 벤치마크(KMMLU 등)에서 Argon을 잰 공개 결과도 아직 없어요

## 앞으로 주목할 점

![Gemini 4 Argon 외부 평가 정리 카드](/assets/images/ai/gemini-4-argon-independent-evals/07-items.webp)
*Gemini 4 Argon 외부 평가 정리 카드 — 출처: Artificial Analysis · Vals AI 기반 자가 렌더*

- API 정가가 적용되는 <u>2026년 12월 1일</u> 이후 과제당 비용 순위
- 투표 기반 순위인 Arena의 공식 집계 결과
- 한국어 벤치마크와 국내 Gemini 앱의 Argon 제공 범위
- 첫 토큰 대기 시간을 줄이는 낮은 추론 설정의 점수

## 참고 출처

- [[Artificial Analysis] Gemini 4 Argon 모델 페이지 (지능 지수·속도·비용)](https://artificialanalysis.ai/models/gemini-4-argon)
- [[Artificial Analysis] 모델 리더보드 (모델별 지능 지수·과제당 비용)](https://artificialanalysis.ai/leaderboards/models)
- [[Vals AI] Gemini 4 Argon 모델 페이지 (종합 지수·항목별 순위·비용)](https://www.vals.ai/models/google_gemini-4-argon)
- [[Google] Gemini 4 Argon 발표 (자체 벤치마크표, 2026-09-30)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- [[Google] Gemini 4 Argon 정식 출시 (2026-10-13)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)
- [[Google] Gemini 앱 Argon 제공 안내 (2026-10-13)](https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/)
- [[경향신문] Gemini 4 Argon 반응과 국내 이용자 수 (2026-10-14)](https://www.khan.co.kr/article/202610142044005)
- 환율: 1달러 ≈ 1,400원 기준 환산
