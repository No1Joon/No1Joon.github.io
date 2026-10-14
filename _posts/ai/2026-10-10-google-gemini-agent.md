---
title: "Google Gemini agent — Claude 모델도 호출하는 업무용 범용 에이전트"
description: "Gemini at Work 2026 에서 공개된 Gemini agent 의 기능과 모델 배정 방식, 에이전트 계정 구조를 정리합니다"
date: 2026-10-10
category: AI
subcategory: News
tags: [google, gemini-agent, ai-agent, enterprise-ai, claude]
image: /assets/og/2026-10-10-google-gemini-agent.png
---

Google Cloud가 2026년 10월 8일 Gemini at Work 2026에서 업무용 범용 에이전트 Gemini agent를 공개했어요. 질문 답변, 문서 작업, 이미지·미디어 생성, 코드 작성·실행을 에이전트 하나와 API 하나로 통합했고, 작업마다 Gemini와 Anthropic의 Claude 가운데 적합한 모델을 선택해 작업을 배정합니다. 비공개 프리뷰라 정식 출시일과 가격은 정해지지 않았어요.

![Gemini at Work 2026 발표 이미지](/assets/images/ai/google-gemini-agent/01-hero-gemini-agent.webp)
*Gemini at Work 2026 발표 이미지 — 출처: Google*

## 발표 내용

![Google 로고](/assets/images/ai/google-gemini-agent/02-logo-google.webp)
*Google 로고*

Google Cloud CEO Thomas Kurian은 Gemini agent를 지시가 아니라 목표를 지정하면 완성된 결과물을 반환하는 에이전트로 소개했어요. 대화, 자율 작업, 코드 생성을 한 화면에서 처리하고, 작업을 예약하거나 특정 이벤트에 반응해 작업을 실행할 수도 있어요.

| 항목 | 내용 |
| :--- | :--- |
| 쓰는 곳 | 웹·모바일·데스크톱 앱·CLI |
| 업무 도구 | Google Workspace·Microsoft 365·Slack |
| 연결 시스템 | Jira·Salesforce·BigQuery 등 |
| 확장 | 사내 스킬 레지스트리·MCP 서버 |
| 제공 상태 | **비공개 프리뷰** |

작업은 클라우드에서 실행돼서, 노트북을 닫거나 기기를 바꿔도 몇 시간에서 며칠 걸리는 작업도 계속 수행돼요. 큰 작업은 그때그때 서브에이전트 여러 개를 만들어 병렬·순차 단계로 분할해 처리합니다.

## Claude까지 고르는 모델 라우팅

![Anthropic 로고](/assets/images/ai/google-gemini-agent/03-logo-anthropic.webp)
*Anthropic 로고*

Gemini agent는 Gemini 계열과 Anthropic의 Claude 모델을 함께 쓰고, 앞으로 다른 비공개·오픈 모델도 추가하겠다고 Google은 밝혔어요. Smart Routing 기능이 작업마다 정확도와 비용을 평가해 모델을 선택하는 방식이에요.

Google Cloud 릴리스 노트에 따르면 Gemini Enterprise 관리자는 10월 8일부터 Claude Opus 5.5와 Sonnet 5.5를 활성화할 수 있습니다. 별도 Anthropic 계정 없이 콘솔에서 약관에 동의하면 되지만 타사 모델은 기본으로 비활성화돼 있고, 사용량은 Cloud Billing에 종량제로 청구돼요. 제공 지역은 global·us·eu로, 국가별 리전 상품에서는 쓸 수 없어요.

Google은 자사 에이전트에서 경쟁사 모델도 고를 수 있게 했고, 기업은 계약 하나로 두 회사 모델을 함께 쓸 수 있어요.

## 회사 계정을 가진 coworker agent

![사람 팀원 옆에서 일하는 에이전트 동료 개념 컷](/assets/images/ai/google-gemini-agent/04-agy.webp)
*사람 팀원 옆에서 일하는 에이전트 동료 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

개인 비서로 쓰면 캘린더·팀·프로젝트 맥락을 알고 있어서, 이름이나 메일 주소 없이 「지난번 그 회의 다시 잡아 줘」 같은 요청을 처리해요.

팀원으로 쓰는 coworker agent는 역할만 설명하면 만들어지고, 자기 이름의 Google Workspace 계정을 부여받습니다. 회사 도메인의 에이전트용 메일 주소와 캘린더·Drive를 갖고 디렉터리에도 등록되며, Google Chat 스페이스에 추가하거나 @멘션으로 일을 맡기고, 문서 댓글로 수정을 제안하면 그 에이전트 이름으로 버전 기록이 남아요. 권한은 공유·멤버십 범위만 따르고, 작업을 지시한 사람의 권한을 사용하지 않아요.

메모리는 네 가지로 나뉘어요. 지금 작업의 맥락(세션), 문서·사람에게서 축적한 지식(시맨틱), 일하는 방법과 에이전트가 직접 작성한 스킬(절차적), 지난 작업 이력(에피소딕)이에요.

## 보안과 비용 통제

Google은 에이전트마다 암호학적으로 검증할 수 있는 고유 신원과 최소 권한을 주고, 모든 행동을 사람이 아닌 그 에이전트 이름으로 감사 로그에 남긴다고 밝혔어요. 에이전트는 네트워크가 분리된 샌드박스에서 실행되고, 모든 트래픽은 정책을 실시간으로 적용하는 Agent Gateway를 지나요.

비용은 Cloud Billing 콘솔에서 프로젝트별 실시간 지출 한도로 제한해요. 한도에 도달하면 에이전트 실행이 일시 중지되고, 콘솔에서 다시 활성화할 수 있어요.

## 발표된 고객 사례

![Google Cloud 발표 고객 사례의 작업 시간 차트](/assets/images/ai/google-gemini-agent/05-chart.webp)
*Google Cloud 발표 고객 사례의 작업 시간 차트 — 출처: Google Cloud 블로그 기반 자가 렌더*

Google이 같은 글에서 제시한 사례는 Gemini Enterprise 전반의 도입 결과로, Gemini agent만의 성과는 아닙니다.

브라질 은행 Bradesco는 문서 검토 시간을 1시간에서 5분으로, Snap은 진단 문제 해결 시간을 30분에서 30초로 단축했다고 소개됐어요. 일본 NTT DOCOMO는 연간 45만 시간을 절감했고, SOMPO는 직원 3만 4,000명이 에이전트 1만 개 이상을 만들었다고 해요. 모두 Google 발표 수치이며 측정 기준은 공개되지 않았습니다.

## Gemini Code Assist 판매 종료

같은 시기 Google Cloud는 10월 9일부터 Gemini Code Assist Standard·Enterprise 신규 구독 판매를 끝냈습니다. 기존 구독은 2026년까지 자동 갱신되고 2027년에 갱신이 끝나며, 대신 Gemini Enterprise 구독에 포함된 Antigravity 개발 도구를 안내하고 있어요. 국내에서 Code Assist를 쓰는 개발팀이라면 2027년 갱신 전에 전환할 도구를 정해야 해요.

![도입 전 확인 정리 카드](/assets/images/ai/google-gemini-agent/06-items.webp)
*도입 전 확인 정리 카드 — 출처: Google Cloud 블로그·릴리스 노트 기반 자가 렌더*

Gemini agent는 일부 Business·Enterprise 요금제의 Google Workspace 고객부터 제공 범위를 확대한다고 9to5Google은 전했어요.

10월 2일 공개된 OpenAI dots가 자체 클라우드 컴퓨터에서 24시간 작업을 수행하는 에이전트라면, Gemini agent는 회사 계정·권한·감사 체계 안에서 관리되도록 설계됐어요.

## 참고 출처

- [[Google Cloud 블로그] Welcome to Gemini at Work 2026, 기능·메모리·보안·고객 사례 (2026-10-09)](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026)
- [[Google 블로그] Gemini agent 발표 요약 (2026-10-08)](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-at-work/)
- [[Google Cloud] 릴리스 노트, Claude Opus 5.5·Sonnet 5.5 활성화와 Code Assist 판매 종료 (2026-10-08~09)](https://docs.cloud.google.com/release-notes)
- [[9to5Google] 비공개 프리뷰·제공 대상·@Gemini 호출 (2026-10-08)](https://9to5google.com/2026/10/08/gemini-agent-google-cloud/)
