---
title: "ChatGPT 맞춤형 GPT 12월 11일 종료 — 플러그인으로 옮겨지는 것과 빠지는 것"
description: "맞춤형 GPT 를 대체하는 ChatGPT 플러그인 이전 기능에서 지침·지식 파일은 넘어가고 커스텀 액션·공유 설정은 빠지는 범위를 정리합니다"
date: 2026-10-20
category: AI
subcategory: News
tags: [openai, chatgpt, custom-gpt, chatgpt-plugins, migration]
image: /assets/og/2026-10-20-chatgpt-custom-gpts-shutdown.png
---

ChatGPT의 **맞춤형 GPT**(custom GPT)가 2026년 12월 11일 종료됩니다!

OpenAI는 맞춤형 GPT를 **플러그인**(plugin)으로 대체하고
기존 GPT를 플러그인으로 이전하는 기능을 출시했어요

지침과 지식 파일은 이전되지만 커스텀 액션과 공유 설정은 이전되지 않습니다

![OpenAI 도움말 맞춤형 GPT 종료와 이전 FAQ 첫 화면](/assets/images/ai/chatgpt-custom-gpts-shutdown/01-photo-faq.webp)
*OpenAI 도움말 맞춤형 GPT 종료와 이전 FAQ 첫 화면 — 출처: OpenAI*

## 종료 일정

![9월 11일 공지부터 2027년 2월 11일까지 맞춤형 GPT 종료 일정 타임라인](/assets/images/ai/chatgpt-custom-gpts-shutdown/02-chart.webp)
*9월 11일 공지부터 2027년 2월 11일까지 맞춤형 GPT 종료 일정 타임라인 — 출처: OpenAI 도움말 기반 자가 렌더*

종료일은 <mark>12월 11일</mark>이고 모든 ChatGPT 요금제가 대상이에요
그날부터 맞춤형 GPT와 GPT 페이지에 접근할 수 없습니다

유예 승인을 받은 Enterprise 워크스페이스는 예외예요
이곳은 2027년 2월 11일까지 쓸 수 있습니다

일정표의 중간 날짜는 Enterprise 기준이고, OpenAI는 날짜가 바뀔 수 있다고 적었어요

이전 기능을 사용할 수 있게 되는 시점도 계정마다 달라
<u>내 계정에 표시된 공지</u>가 최종 기준입니다

## 신규 생성과 게시 중단

![개인 계정의 새 GPT 생성과 게시 중단을 적은 OpenAI 도움말](/assets/images/ai/chatgpt-custom-gpts-shutdown/03-photo.webp)
*개인 계정의 새 GPT 생성과 게시 중단을 적은 OpenAI 도움말 — 출처: OpenAI*

개인 계정은 **새 GPT를 만들 수도, 새로 게시할 수도 없어요**
Free, Go, Plus, Pro 모두 해당합니다

이미 만든 GPT는 종료일까지 그대로 쓸 수 있어요
기존 GPT를 고치려면 편집 자격이 있는 구독이 필요합니다

Business, Enterprise, Edu 워크스페이스는
생성과 편집 가능 여부가 워크스페이스 설정에 따라 결정돼요

Enterprise의 신규 생성은 10월 26일 중단될 예정입니다

## 플러그인의 구성

플러그인은 ChatGPT와 Codex에서 함께 쓰는 기능 묶음이에요

[스킬(skill)]
반복해서 쓰는 지침과 작업 순서

[앱(app)]
Slack, Google Drive 같은 외부 서비스 연결

[앱 템플릿]
관리자가 워크스페이스용 앱을 구성하는 틀

[확장(extension)]
대화 안 화면, 파일 열기와 편집, 입력 양식

요청에 필요한 경우 ChatGPT가 설치한 플러그인을 자동으로 사용해요
직접 고를 때는 대화창에서 <mark>@ 뒤에 플러그인 이름</mark>을 입력하면 됩니다

새로 만들 때는 플러그인 목록에서 **Plugin Creator**를 설치하고 대화로 설명하면 돼요

## 플러그인 이전 항목과 제외 항목

![플러그인으로 넘어가는 항목과 커스텀 액션 처리를 적은 OpenAI FAQ](/assets/images/ai/chatgpt-custom-gpts-shutdown/04-photo.webp)
*플러그인으로 넘어가는 항목과 커스텀 액션 처리를 적은 OpenAI FAQ — 출처: OpenAI*

| GPT 구성 | 이전 후 |
| :--- | :--- |
| 지침 | 플러그인의 스킬 |
| 지식 파일 | 참고 파일로 복사 |
| 연결한 앱 | 플러그인의 앱 |
| 선택한 모델 | 이전되지 않음 |
| 커스텀 액션 | <mark>이전되지 않음</mark> |
| 공유 설정 | 이전되지 않음, 비공개로 시작 |
| 미게시 편집 | 이전되지 않음 |

이전 후 별도 재구성이 필요한 항목은 **커스텀 액션**(custom action)이에요
외부 API를 호출하던 GPT는 이전 직후 해당 연동 기능이 동작하지 않습니다

대체할 앱이 있는지 먼저 보고, 없으면 <u>MCP 서버를 직접 구성</u>해야 해요
OpenAI도 다시 만든 연동이 원래 액션의 기능을 전부 갖추지 않을 수 있다고 적었습니다

맞춤형 GPT와 나눈 대화는 종료 뒤에도 열어 볼 수 있다고 OpenAI가 밝혔습니다

## 이전하는 순서

이전 기능이 제공되면 **My GPTs**에서 옮길 GPT의 **Migrate to plugin**을 누릅니다
안내에 따라 진행하면 플러그인이 생성돼요

이전은 GPT의 <mark>마지막 게시 버전</mark>을 이전해요
고칠 것이 있으면 이전 전에 끝내고 게시해 두세요~

게시라고 해서 공개 공유를 할 필요는 없어요
이전한 원래 GPT는 종료일까지 쓸 수 있지만 **읽기 전용**이 되고 삭제도 안 됩니다

### 🧪 옮긴 뒤 비교할 것

플러그인은 같은 질문에도 GPT와 다르게 답할 수 있어요
OpenAI는 익숙한 프롬프트와 어려운 사례 하나 이상으로 비교하라고 권합니다

[스킬 선택]
관련 스킬을 선택해 지침대로 작업을 수행하는지

[참고 자료]
옮겨 온 지식 파일을 실제로 쓰는지

[출력 형식]
답이나 파일이 원래 형식대로 나오는지

[도구]
작업에 필요한 앱과 연동이 설정돼 있는지

## 남이 만든 GPT를 쓰는 경우

쓰기만 하는 GPT는 내가 이전할 수 없어요
GPT 화면의 공지와 <u>제작자의 대체 플러그인 안내</u>를 확인하면 됩니다

원래 GPT를 쓸 수 있었다고 대체 플러그인 사용 권한이 자동으로 부여되지는 않아요
제작자가 플러그인을 공유하거나 공개 목록에 등록해야 쓸 수 있습니다

Enterprise에서 만든 공개 GPT는 다른 요금제에서 써도 그 일정을 따라요
기준은 내 요금제가 아니라 **GPT가 만들어진 곳**입니다

한국 계정에 따로 공지된 일정은 없어요
회사나 학교 워크스페이스를 쓴다면 <u>관리자 공지</u>도 확인하세요

## 종료 전 점검

![맞춤형 GPT를 플러그인으로 옮기기 전 점검할 다섯 가지](/assets/images/ai/chatgpt-custom-gpts-shutdown/05-items.webp)
*맞춤형 GPT를 플러그인으로 옮기기 전 점검할 다섯 가지 — 출처: OpenAI 도움말 기반 자가 렌더*

Business와 Enterprise 워크스페이스는 구성원끼리 플러그인을 공유할 수 있어요
개인 계정의 플러그인을 공개하려면 <mark>별도 제출 절차</mark>를 거쳐야 합니다

## 참고 출처

- [[OpenAI] Custom GPT retirement and migration FAQ (종료일, 이전 항목, Enterprise 일정)](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq)
- [[OpenAI] GPTs in ChatGPT (개인 계정 생성과 게시 중단, 편집 조건)](https://help.openai.com/en/articles/8554407-gpts-in-chatgpt)
- [[OpenAI] Plugins in ChatGPT (플러그인 구성, 사용법, Plugin Creator, 공유 권한)](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt)
