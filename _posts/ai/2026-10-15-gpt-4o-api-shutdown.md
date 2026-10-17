---
title: "GPT-4o·GPT-4.1 API 2027년 1월 14일 종료 — GPT-6 Luna 로 바꾸면 요금은"
description: "OpenAI API 주요 모델의 단계별 종료 일정과 GPT-6 Luna 로 옮길 때 같은 작업량의 월 요금 차이를 정리합니다"
date: 2026-10-15
category: AI
subcategory: News
tags: [openai, gpt-4o, api-deprecation, gpt-6-luna, pricing]
image: /assets/og/2026-10-15-gpt-4o-api-shutdown.png
---

OpenAI가 10월 14일 개발자들에게 GPT-4o·GPT-4o mini·GPT-4.1·GPT-4.1 mini를 **2027년 1월 14일** API 지원을 종료한다고 알렸습니다. 이 모델로 챗봇이나 사내 도구를 운영하고 있다면 석 달 안에 모델 이름을 바꿔야 해요. 그보다 먼저 10월 23일에 종료되는 모델들도 있습니다.

API는 다른 회사가 자기 서비스에 OpenAI 모델을 붙여 쓰는 연결 통로입니다. ChatGPT 앱이나 웹에서 대화만 하는 사용자는 바꿀 것이 없고, 이 일정은 ChatGPT 모델을 넣어 만든 챗봇·상담 서비스·사내 도구를 운영하는 쪽에 해당해요.

![OpenAI 로고](/assets/images/ai/gpt-4o-api-shutdown/01-logo-openai.webp)
*OpenAI 로고*

## 종료 일정

![OpenAI API 주요 모델 종료 일정](/assets/images/ai/gpt-4o-api-shutdown/02-chart.webp)
*OpenAI API 주요 모델 종료 일정 — 출처: OpenAI Deprecations 문서 기반 자가 렌더*

OpenAI Deprecations 문서의 10월 14일 항목에 올라간 모델은 날짜가 붙은 스냅샷(특정 시점에 고정한 모델 버전) 다섯 개입니다.

| 모델 | 종료되는 스냅샷 |
| :--- | :--- |
| GPT-4o | **gpt-4o-2024-08-06**, **gpt-4o-2024-11-20** |
| GPT-4o mini | **gpt-4o-mini-2024-07-18** |
| GPT-4.1 | **gpt-4.1-2025-04-14** |
| GPT-4.1 mini | **gpt-4.1-mini-2025-04-14** |

권장 대체 모델은 다섯 개 모두 <mark>gpt-6-luna</mark>입니다. 이 모델들을 미세조정(fine-tuning)해 만든 모델도 원래 모델과 같은 날 함께 지원이 종료된다고 문서에 적혀 있어요. **gpt-4o**처럼 날짜 없이 부르는 별칭(alias)이 어떻게 되는지는 이 항목에 따로 적혀 있지 않습니다.

종료 시점에 그 모델에 전송된 요청은 처리되지 않습니다. 문서는 종료 시점에 "모델이나 엔드포인트에 더 이상 접근할 수 없다"고 설명해요. ChatGPT 앱에서 쓰는 모델과는 별개로, API로 직접 호출하는 서비스에만 해당하는 일정입니다.

## 10월 23일 먼저 지원 종료되는 모델

4월 22일에 예고된 종료가 10월 23일에 적용됩니다. 1월보다 석 달 앞서는 일정이라, 아래 모델을 아직 쓰고 있다면 이 모델들의 전환이 더 시급합니다.

| 종료 모델 | 권장 대체 |
| :--- | :--- |
| GPT-4, GPT-4 Turbo | gpt-5.6-sol |
| GPT-3.5 Turbo | gpt-5.6-terra |
| <mark>gpt-4.1-nano</mark> | gpt-5.6-luna |
| gpt-4o-2024-05-13 | gpt-5.6-sol |
| o1, o3-mini | gpt-5.6-sol |
| o4-mini | gpt-5.6-terra |

GPT-4.1 계열 가운데 nano만 1월이 아니라 10월 23일 종료라는 점이 헷갈리기 쉽습니다. 이 날짜에는 GPT-3.5 Turbo·GPT-4 기반 미세조정 모델과 이미지 모델 gpt-image-1도 함께 지원 종료돼요.

## 요금 비교

![같은 작업량의 월 요금](/assets/images/ai/gpt-4o-api-shutdown/03-chart.webp)
*같은 작업량의 월 요금 — 출처: OpenAI 요금표 기반 자가 렌더*

| 모델 | 입력 (100만 토큰) | 출력 (100만 토큰) |
| :--- | :--- | :--- |
| GPT-4o | 3,500원 | 14,000원 |
| GPT-4.1 | 2,800원 | 11,200원 |
| GPT-4.1 mini | 560원 | 2,240원 |
| GPT-4o mini | 210원 | 840원 |
| GPT-6 Luna | <mark>140원</mark> | <mark>700원</mark> |

OpenAI 요금표 Standard 기준으로 GPT-6 Luna는 입력 140원(0.10달러), 출력 700원(0.50달러)이라 1월에 종료되는 네 모델보다 모두 쌉니다. 국내 서비스에서 흔히 쓰는 GPT-4o mini와 비교하면 입력은 3분의 2, 출력은 약 83% 수준이에요.

입력 1억 토큰과 출력 2,000만 토큰을 쓰는 서비스로 계산하면 차이가 분명해집니다. GPT-4o는 한 달 약 63만 원, GPT-4o mini는 약 3만 7,800원, GPT-6 Luna는 약 2만 8,000원이에요. GPT-4o에서 옮기는 쪽은 같은 작업량에서 요금이 약 22분의 1로 감소합니다.

이 계산은 추론 강도를 none으로 둔 경우입니다. 추론 강도는 모델이 답하기 전에 내부적으로 얼마나 더 따져 보는지 정하는 설정이고, 그 과정에서 쓰인 토큰도 출력 요금으로 계산됩니다. 추론 토큰 사용량이 추가되면 출력 요금이 증가하므로, 아래 설정을 먼저 확인해야 해요.

## 옮길 때 확인할 것

![옮길 때 확인할 설정](/assets/images/ai/gpt-4o-api-shutdown/04-agy.webp)
*옮길 때 확인할 설정 — 출처: 개념 컷 · agy 자가 생성*

### 추론 강도

GPT-6 Luna의 **reasoning_effort**는 none·low·medium·high·xhigh·max 여섯 단계이고, 값을 지정하지 않으면 **medium**이 기본입니다. GPT-4o mini 자리에 모델 이름만 변경하면 추론 토큰이 발생하고, 그만큼 출력 요금이 추가로 청구돼요. OpenAI 도움말의 GPT-4.x 이전 안내는 none에서 시작해 기존 결과와 비교하라고 권합니다.

### 함수 호출

Chat Completions API에서는 추론 강도가 none일 때만 함수 호출(function calling, 모델이 날씨 조회·예약 같은 외부 기능을 불러 쓰는 방식)이 됩니다. 추론 강도를 올리면서 도구를 쓰려면 Responses API로 전환해야 해요.

### 미세조정 모델

GPT-6 Luna 모델 문서의 지원 기능 목록에는 미세조정이 없고, 미세조정 엔드포인트도 지원 안 함으로 표시돼 있습니다. GPT-4o mini나 GPT-4.1 mini를 미세조정해 쓰던 서비스는 1월 14일에 그 모델의 지원도 함께 종료되고, Luna로는 같은 방식으로 다시 만들 수 없어요. 프롬프트와 예시로 대신할지 먼저 시험해야 합니다.

### 긴 입력 요금

입력이 27만 2,000토큰을 넘는 요청은 그 요청 전체에 입력·캐시 요금 2배, 출력 요금이 1.5배로 적용됩니다. 컨텍스트 윈도(context window)는 105만 토큰이지만 긴 문서를 한 번에 입력하는 서비스는 이 구간을 따로 계산해야 해요.

## 정리

![GPT-4 계열 API 종료 정리](/assets/images/ai/gpt-4o-api-shutdown/05-items.webp)
*GPT-4 계열 API 종료 정리 — 출처: 본문 정리 · 자가 렌더*

2027년 1월 14일 종료 대상은 날짜가 붙은 스냅샷 다섯 개와 해당 스냅샷을 미세조정한 모델이고, 10월 23일에는 GPT-4·GPT-3.5 Turbo·gpt-4.1-nano 같은 더 오래된 모델의 지원이 먼저 종료됩니다. 대체 모델 GPT-6 Luna는 토큰 단가가 더 싸지만, 추론 강도를 none으로 두고 기존 결과와 맞춰 본 뒤에 트래픽을 옮겨야 추론 토큰에 따른 추가 요금을 피할 수 있어요.

## 참고 출처

- [[OpenAI] Deprecations 문서 (2026-10-14 GPT-4 계열 종료 공지·2026-04-22 공지의 10월 23일 종료 목록·종료 후 접근 불가)](https://developers.openai.com/api/docs/deprecations)
- [[OpenAI] API 요금표 (GPT-6 Luna·GPT-4o·GPT-4o mini·GPT-4.1·GPT-4.1 mini Standard 요금)](https://developers.openai.com/api/docs/pricing)
- [[OpenAI] GPT-6 Luna 모델 문서 (추론 강도 기본값·함수 호출 조건·미세조정 미지원·272K 초과 요금)](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [[OpenAI Help Center] Migrating from GPT-4.x to GPT-6 Luna (추론 강도 none에서 시작 권장)](https://help.openai.com/en/articles/20001600-migrating-from-gpt-4x-to-gpt-6-luna)
- 환율: 1달러 ≈ 1,400원 기준 환산
