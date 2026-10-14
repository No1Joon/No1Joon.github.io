---
title: "ChatGPT Intelligent UI — 답변에 차트·버튼·입력 폼이 들어온다"
description: "GPT-6 와 함께 배포된 Intelligent UI 의 형식과 요금제별 제공 범위, 끄는 방법을 정리합니다"
date: 2026-10-10
category: AI
subcategory: News
tags: [openai, chatgpt, gpt-6, generative-ui, ux]
image: /assets/og/2026-10-10-chatgpt-intelligent-ui.png
---

OpenAI가 2026년 10월 7일 ChatGPT에 GPT-6와 Intelligent UI를 배포하기 시작했어요. 질문에 따라 답변 안에 그래픽, 누를 수 있는 버튼, 입력 양식, 차트가 포함되고, 대화창 안에서 바로 조작할 수 있습니다. 전 세계 동시 배포라 국내 계정도 대상이고, 유료 요금제에 먼저 제공된 뒤 10월 8일부터 무료·Go 요금제로 확대됐어요. OpenAI는 같은 날 한국어 발표 페이지도 올렸어요.

![Intelligent UI 발표 키 아트](/assets/images/ai/chatgpt-intelligent-ui/01-hero-keyart.webp)
*Intelligent UI 발표 키 아트 — 출처: OpenAI*

## Intelligent UI의 형식

OpenAI는 GPT-6가 텍스트·시각 자료·인터랙티브 요소로 답변을 구성하고, 질문마다 어떤 조합을 사용할지 선택하도록 훈련했다고 밝혔어요. 비교 질문이면 나란히 배치하고, 설명이면 직접 조작하는 도식을 쓰고, 텍스트가 가장 나은 질문에는 텍스트로 답하는 방식이에요.

![같은 질문에 대한 GPT-5.6 Instant와 GPT-6 Instant 답변 비교](/assets/images/ai/chatgpt-intelligent-ui/02-capture.webp)
*같은 질문에 대한 GPT-5.6 Instant와 GPT-6 Instant 답변 비교 — 출처: OpenAI*

OpenAI 발표 페이지는 같은 질문을 GPT-5.6 Instant와 GPT-6 Instant에 입력한 결과를 나란히 보여 줘요. 친구들과 먹을 일요일 양고기 로스트 계획을 묻자 GPT-5.6은 목록과 표로 답했고, GPT-6은 요리 사진과 함께 인원수에 따라 내용을 조정하는 저녁 계획 카드를 표시했어요.

[일상 질문]
조리 시간표를 레시피 옆에 추가하거나 여행 경유지를 지도에 표시

[학습]
중심극한정리·몬티 홀 문제처럼 입력값을 변경해 결과를 확인하는 설명

[도구 만들기]
더치페이 계산기·노후 저축 계산기·대화 안에서 하는 게임

## 말 한마디로 만드는 도구

![영수증 사진으로 만든 더치페이 계산기 데모](/assets/images/ai/chatgpt-intelligent-ui/03-capture.webp)
*영수증 사진으로 만든 더치페이 계산기 데모 — 출처: OpenAI*

발표 페이지 예시에서는 식당 영수증 사진을 업로드하고 「다섯 명이 먹은 대로 나누는 계산기를 클립보드처럼 만들어 달라」고 하자, 손님 이름 칸과 메뉴별로 누가 먹었는지 고르는 칸이 있는 계산기가 대화 안에 생성됐어요.

체크리스트 같은 일부 구성 요소는 대화 화면을 새로고침해도 입력한 상태가 유지돼요. 다른 대화로는 전달되지 않아서, 만든 도구는 그 대화 안에서만 계속 쓸 수 있어요.

## 작동 방식

OpenAI는 화면에 스트리밍으로 바로 표시할 수 있는 네이티브 구성 요소 라이브러리와, 모델이 만든 인터페이스를 즉시 처리하는 컴파일러를 함께 만들었다고 설명했어요. 라이브러리가 디자인의 기본 틀을 정하고 어떤 요소를 어떻게 조합할지는 모델이 정해서, 답변 전체가 끝날 때까지 기다리지 않고 생성되는 대로 화면에 표시돼요.

OpenAI는 답변의 명확성·유용성·완성도를 평가하는 과정을 훈련에 포함해, 언제 인터랙티브 요소를 쓰고 언제 텍스트로 충분한지도 모델이 판단하게 했다고 밝혔어요. 디자인 판단력과 만들 수 있는 결과물의 범위는 아직 개선할 부분이 남았다고도 적었습니다.

## 요금제별 모델

![OpenAI 로고](/assets/images/ai/chatgpt-intelligent-ui/04-logo-openai.webp)
*OpenAI 로고*

| 요금제 | GPT-6 모델 | Intelligent UI |
| :--- | :--- | :--- |
| Free·Go | GPT-6 Luna | 10월 8일부터 |
| Plus·Pro·Business | GPT-6 Sol | <mark>10월 7일부터</mark> |
| Enterprise | GPT-6 Sol | 관리자 설정에 따름 |
| Pro 추론 옵션 | GPT-6 Astra | **지원 안 함** |

Luna와 Sol은 9월 API로 먼저 공개된 모델이고, ChatGPT 쪽은 둘 다 일상 대화에 맞춰 조정됐어요. 이번 업데이트는 Chat 탭에만 적용돼 Work 탭과 Codex를 실행하는 모델은 변경되지 않았어요.

GPT-6 Instant는 추론 중에도 답변을 생성하기 시작하도록 훈련돼, 웹 검색이 필요한 질문에서 GPT-5.6 Instant보다 평균 44% 빨리 답변을 시작한다고 OpenAI는 밝혔어요.

## 끄는 법과 제한

![Intelligent UI 설정·제한 정리 카드](/assets/images/ai/chatgpt-intelligent-ui/05-items.webp)
*Intelligent UI 설정·제한 정리 카드 — 출처: OpenAI 도움말 센터 기반 자가 렌더*

시각 요소가 부담스러우면 웹 ChatGPT 설정에서 **Personalization → Layout and Visuals → Simple**(한국어 화면은 개인 맞춤 설정 메뉴)을 고르면 되고, OpenAI 도움말은 이렇게 해도 시각·인터랙티브 요소가 줄어들 뿐 일부는 여전히 나타날 수 있다고 적었습니다. 대화 하나에서만 바꾸고 싶으면 「표로만 비교해 줘」처럼 그 대화에서 요청하면 되고, 늘 같은 형식을 원하면 맞춤형 지침에 적어 둘 수 있어요.

Intelligent UI는 Instant부터 Extra High까지 모든 추론 단계에서 쓸 수 있지만, Work 탭과 음성 모드에서는 쓸 수 없어요. Gmail 같은 연결 앱은 지금처럼 그대로 작동해요.

## 참고 출처

- [[OpenAI] 모두를 위한 GPT-6과 Intelligent UI, 제공 일정·요금제별 모델·작동 방식 (2026-10-07)](https://openai.com/ko-KR/index/gpt-6-for-everyone/)
- [[OpenAI 도움말 센터] Intelligent UI in ChatGPT, 끄는 법·지원 범위·상태 저장](https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt)
- [[OpenAI] GPT-6 Sol과 Luna 소개](https://openai.com/ko-KR/index/introducing-gpt-6-sol-and-luna/)
