---
title: "GPT-6 Astra 가 내 화면엔 왜 안 보이나 — Chat 이 아니라 Work·Codex 에 있습니다"
description: "GPT-6 Astra 가 열린 자리와 요금제별 배포 순서를 정리해, 모델 목록에서 찾을 수 없는 이유를 풀어봅니다"
date: 2026-09-09
category: AI
subcategory: News
tags: [openai, gpt-6-astra, chatgpt, codex, pricing-plans]
image: /assets/og/2026-09-09-gpt-6-astra-availability.png
---

GPT-6 아스트라가 나왔다는 소식을 보고 ChatGPT를 열었는데 모델 목록에 없는 경우가 많습니다. 결제도 멀쩡하고 앱도 최신인데 안 보여요.

고장이 아니라 **배포 구조**입니다. 아스트라가 열리는 자리가 우리가 늘 쓰던 대화 화면이 아니에요.

![같은 건물의 문이 요금제마다 다르게 열리는 장면](/assets/images/ai/gpt-6-astra-availability/01-agy-hero.webp)
*같은 건물의 문이 요금제마다 다르게 열리는 장면 — 출처: 개념 컷 · agy 자가 생성*

## 아스트라가 먼저 열린 자리

OpenAI 공지에 따르면 Pro와 Enterprise, Business Premium 이용자에게 **ChatGPT Work와 Codex에서** 먼저 열고, API에도 함께 올렸습니다. Plus와 Business 이용자에게는 며칠에 걸쳐 순차로 배포한다고 했어요.

대부분의 혼선은 「모든 Plus 이용자에게 제공」이라는 문장을 읽고 평소 쓰던 대화 화면의 모델 목록을 뒤질 때 생깁니다. 아무리 새로고침해도 아스트라가 안 보이는 것은 그 자리가 아니기 때문이에요.

OpenAI 개발자 포럼에도 같은 질문이 올라와 있습니다. 발표는 Plus 전체라고 했는데 실제 접근은 Work와 Codex로 한정돼 있다는 내용이에요.

![Chat·Work·Codex 세 입구가 갈리는 장면](/assets/images/ai/gpt-6-astra-availability/02-agy-entrances.webp)
*Chat·Work·Codex 세 입구가 갈리는 장면 — 출처: 개념 컷 · agy 자가 생성*

## 요금제마다 열리는 화면이 다릅니다

같은 아스트라라도 어느 화면에서 어떤 이름으로 보이는지가 요금제를 따라 갈립니다.

| 요금제 | 일반 Chat | Work·Codex |
|---|---|---|
| Free | 없음 | 없음 |
| Plus | 없음 | <mark>아스트라 (제한)</mark> |
| Pro | GPT-6 Pro | 아스트라 |
| Business | 등급에 따라 | 아스트라 |
| Enterprise | GPT-6 Pro | **관리자 설정 필요** |

Plus 요금제는 일반 Chat 화면에 아스트라 계열이 아예 표시되지 않고, Work와 Codex로 들어가야 모델 선택에 나옵니다.

## Chat의 GPT-6 Pro는 다른 이름입니다

일반 Chat 화면에서 보이는 **GPT-6 Pro**는 아스트라 계열을 그 화면에 맞춰 내놓은 이름입니다. 이름이 다르니 「아스트라가 없다」고 읽기 쉬운데, 실제로는 Plus 요금제에 그 항목이 포함되지 않은 것이에요.

- Pro·Business·Enterprise는 Chat에서 GPT-6 Pro로 만난다
- Plus는 Chat에 그 항목이 없고 Work·Codex로 간다
- 둘 다 아스트라 계열이지만 열리는 화면과 요금제가 다르다

## 사용량도 요금제를 따라갑니다

접근이 열려도 쓸 수 있는 양이 같지는 않습니다.

| 구분 | 아스트라 사용량 |
|---|---|
| Pro·Business Premium | 기존 Work·Codex 한도 그대로 |
| Plus·Business Standard | <mark>제한된 양</mark> + 초과 시 크레딧 |

Plus에서 사용 한도가 빠르게 소진되는 것은 이 구조 때문이고, 한도를 넘긴 뒤에는 별도 크레딧을 추가해 쓰는 선택지가 제공됩니다.

## 안 보일 때 점검할 네 가지

- **Work 모드로 들어갔는지** 확인합니다. 일반 대화 화면과 모델 목록이 다릅니다
- **앱을 최신 버전으로 올립니다.** 데스크톱 앱 구버전에서는 새 모델이 표시되지 않습니다
- **회사 계정이면 관리자에게 묻습니다.** Enterprise 워크스페이스는 출시 시점 기본값이 꺼짐이라 관리자가 켜야 합니다
- **며칠 기다립니다.** 국가와 조직 단위로 순차 배포라 같은 요금제라도 시점이 갈립니다

넷을 다 확인했는데도 없으면 아직 내 계정 차례가 안 온 것입니다. 설정에서 바꿀 수 있는 값이 아니에요.

![글 끝 정리](/assets/images/ai/gpt-6-astra-availability/03-items.webp)
*글 끝 정리 — 출처: 본문 정리 · 자가 렌더*

## API는 요금제와 무관합니다

구독 화면에서 안 보이더라도 API로는 바로 부를 수 있습니다. 모델 ID는 **gpt-6-astra**이고 Chat Completions가 아니라 **Responses API**로 호출합니다. Microsoft Azure와 AWS Bedrock에도 함께 올라가 있어요.

요금은 100만 토큰당 입력 1만 3,445원(10달러), 출력 6만 7,225원(50달러)입니다. 컨텍스트 길이와 세부 성능 수치는 9월 6일 출시 편의 사양을 따릅니다.

[GPT-6 Astra 출시 — 105만 토큰과 두 갈래 요금, 그리고 걸어 둔 조건](/posts/gpt-6-astra-release/)

## 정리하면

아스트라가 안 보이는 이유는 대부분 화면을 잘못 찾았거나, 요금제에 해당 항목이 없거나, 배포 순번이 아직 안 온 세 경우 중 하나입니다.

컴퓨터 사용 기능을 실제로 써 보려면 Plus 기준으로는 Work나 Codex가 유일한 경로이고, 회사 계정이라면 관리자 설정이 먼저입니다. 둘 다 아니면 API 쪽이 남습니다.

## 참고 출처

- [[OpenAI] GPT-6 Astra: A new generation of intelligence (2026-09-03, 발표문·제공 범위)](https://openai.com/index/gpt-6-astra/)
- [[OpenAI] 공식 계정 공지 (Pro·Enterprise·Business Premium 우선, Plus·Business 순차 배포)](https://x.com/OpenAI/status/2095968413646737608)
- [[OpenAI Help Center] ChatGPT Work and Codex (Work·Codex 화면 구분)](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)
- [[OpenAI Developer Community] Clarification needed: GPT-6 Astra announced for all Plus users but access limited to Work/Codex (혼선 사례)](https://community.openai.com/t/clarification-needed-gpt-6-astra-was-announced-for-all-chatgpt-plus-users-but-plus-access-is-currently-limited-to-work-codex/1395038)
- [[OpenAI] GPT-6 Astra 모델 문서 (모델 ID·Responses API·요금)](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [[Notebookcheck] GPT-6 Astra is on ChatGPT Plus, but only in Work and Codex (요금제별 노출 정리)](https://www.notebookcheck.net/GPT-6-Astra-is-on-ChatGPT-Plus-but-only-in-Work-and-Codex.1391574.0.html)
- 원화 환산은 2026년 9월 8일 은행 매매기준율 1달러 1,344.50원을 적용했습니다.
