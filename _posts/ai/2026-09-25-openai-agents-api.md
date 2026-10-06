---
title: "OpenAI Agents API — 며칠짜리 실행 전체를 맡기는 관리형 harness"
description: "Codex harness 를 API 로 내놓은 Agents API 가 대신해 주는 일과 직접 구현한 루프와의 차이, 요금·제약을 정리합니다"
date: 2026-09-25
category: AI
subcategory: Explainer
tags: [openai, agents-api, ai-agent, codex, developer-tools]
image: /assets/og/2026-09-25-openai-agents-api.png
---

OpenAI가 2026년 9월 10일 Agents API를 공개 베타로 제공하기 시작했습니다. 자사 코딩 도구 Codex를 실행하는 harness를 그대로 API로 제공한 것이라, 모델을 한 번 호출하는 것이 아니라 며칠에 걸친 작업 실행 자체를 맡기는 상품이에요.

에이전트를 직접 만들면 대화 기록이 컨텍스트 한계에 도달할 때 요약하고, 도구 호출을 관리하고, 작업을 나눠 여러 에이전트에 맡기고, 중간에 중단되면 재개하는 부분을 모두 구현해야 했습니다. Agents API는 이 기능 묶음을 OpenAI 쪽에서 실행·관리합니다.

![Agents API 개요 도표](/assets/images/ai/openai-agents-api/01-hero-agentsapi.webp)
*Agents API 개요 도표 — 출처: OpenAI*

## 관리형 harness의 역할

![OpenAI 로고](/assets/images/ai/openai-agents-api/02-logo-openai.webp)
*OpenAI 로고 — 출처: OpenAI*

공식 문서는 관리형 harness의 역할을 일곱 가지로 정리했습니다.

- 샌드박스에서 명령과 코드 실행
- 상황에 맞는 스킬·지침 적용
- 도구나 MCP로 외부 데이터 연결
- 작업 중인 에이전트에 방향 지시
- 이전 작업을 요약해 컨텍스트 창 관리
- 작업을 나눠 서브에이전트에 위임
- 중단된 세션을 이어서 재개

구성 요소는 넷으로 정리됩니다. 모델·지침·도구를 묶은 **에이전트**, 파일과 명령을 다루는 **환경**, 작업이 이어지는 **세션**, 주고받는 입력과 산출물인 **이벤트와 아이템**이에요.

세션은 한 번 만들면 상태가 OpenAI 쪽에 저장됩니다. 다음 작업을 보낼 때 대화 기록을 다시 포함해 보낼 필요가 없고, 세션을 삭제하면 산출물도 함께 삭제돼요.

## 실행 환경 세 가지

![Agents API 아키텍처 도표](/assets/images/ai/openai-agents-api/03-photo.webp)
*Agents API 아키텍처 도표 — 출처: OpenAI*

**environment.type**값으로 에이전트가 어디서 명령을 실행할지 정합니다.

| 설정 | 실행 대상 |
| :--- | :--- |
| **none** | 컴퓨터 없이 질문 답변과 도구 호출만 |
| **openai_hosted** | <mark>OpenAI가 제공하는 리눅스 샌드박스</mark> |
| **self_hosted** | 내 서버·컨테이너에 붙이는 실행기 |

호스팅 샌드박스는 Python과 Node.js, 명령줄 도구가 들어간 리눅스 작업 공간이고 작업 폴더는 **/workspace**입니다. **packages**로 패키지를 설치하고 **setup_commands**로 시작 전 명령을 실행하며, **files**로 입력 파일을 업로드해요. 네트워크는 **network.access**로 전체 허용·차단·지정 호스트만 허용 중에 고르고, 지정 방식은 정확한 호스트 이름을 1개부터 100개까지 적습니다.

비밀값은 **env**에 그대로 넣지 말라고 문서가 명시했습니다. 에이전트가 만든 코드가 그 값을 읽을 수 있어서, 실제 값은 별도로 보관하는 비밀값 관리 기능을 쓰라고 안내해요. **PATH**나 **OPENAI_API_KEY**같은 예약 이름은 아예 거부됩니다.

self_hosted를 고르면 컴퓨팅 자원을 직접 준비하고 실행기를 세션에 연결합니다. 세션이 환경보다 오래 살 수 있어서, 언제 자원을 시작하고 종료할지는 내 쪽 책임이에요.

## 서브에이전트

**agent.multi_agent.enabled**를 켜면 harness가 서브에이전트를 만들고 메시지를 보내고 기다리고 중단하는 도구를 자동으로 제공합니다. 도구를 직접 선언하지 않아요.

| 항목 | 규칙 |
| :--- | :--- |
| 동시 실행 기본값 | **6개** (조정자 제외) |
| 조정 값 | max_concurrent_subagents |
| 물려받는 것 | MCP 도구·자격 증명·웹 검색 |
| 못 쓰는 것 | <mark>함수 도구</mark> |
| 파일 시스템 | 조정자와 공유 |

문서는 독립적인 작업에만 쓰라고 권합니다. 문서 여러 건을 따로 검토하거나 장애 원인을 원인별로 조사하는 일이 해당하고, 짧은 작업이나 앞 단계 결과에 의존하는 단계는 주 에이전트가 그대로 하는 편이 낫다고 적었어요. 같은 파일을 고치는 에이전트끼리는 변경을 조율해야 합니다.

## 세 API 선택 기준

OpenAI는 에이전트를 만드는 방법을 세 갈래로 정리해 두었습니다.

| 갈래 | 루프 실행 위치 |
| :--- | :--- |
| **Agents API** | OpenAI의 관리형 Codex harness |
| Agents SDK | 내 애플리케이션 안 |
| Responses API | 내 애플리케이션, 호스팅 조정은 선택 |

연동에 드는 작업량은 Agents API가 가장 적고 Responses API가 가장 많습니다. 반대로 통제권은 Responses API가 가장 크고 Agents API가 가장 작아요. 상태 관리 방식도 다릅니다. Agents API는 세션 설정과 주고받은 기록이 OpenAI 쪽에 저장되고, Responses API는 대화 기록을 내가 직접 관리합니다.

**작업이 며칠 단위로 이어지는가**, 그리고 **중간 상태를 외부 서비스에 저장해도 되는가**. 둘 다 예라면 Agents API, 둘 중 하나라도 아니라면 나머지 둘이에요.

구버전 Assistants API는 2026년 8월 26일 종료됐습니다. Responses API와 Conversations API가 이를 대체했고, Agents API는 그 위에서 동작하는 별개 선택지예요.

## 요금과 제약

![OpenAI 호스팅 컨테이너 20분당 요금](/assets/images/ai/openai-agents-api/04-chart.webp)
*OpenAI 호스팅 컨테이너 20분당 요금 — 출처: OpenAI 요금표 기반 자가 렌더*

Agents API 자체에 추가되는 요금은 없습니다. 사용량에 따라 과금되는 항목이 셋이에요.

- 모델 토큰: 고른 모델의 API 단가 그대로 (GPT-6 Astra는 입력 100만 토큰당 1만 4,000원, 출력 7만 원)
- 도구 사용: 웹 검색은 1,000회당 1만 4,000원, 검색으로 읽은 토큰은 별도
- 호스팅 컨테이너: 메모리 크기에 따라 20분 세션당 42원에서 2,688원

컨테이너는 분 단위로 과금되고 세션당 최소 5분이 과금됩니다. 장시간 실행되는 작업일수록 토큰보다 컨테이너 쪽 비용 구조를 먼저 계산해야 해요.

데이터 저장 위치는 **미국만** 지원하고, 데이터를 남기지 않는 무보존(ZDR) 설정은 지원하지 않습니다. 샌드박스를 자기 인프라에서 운영하더라도 무보존 대상이 되지는 않는다고 문서가 명시했어요.

금융위원회는 2026년 4월 20일 전자금융감독규정 시행세칙 개정으로 금융보안원 평가를 통과한 SaaS를 내부 업무망에서 쓸 수 있게 했고, 망분리 전면 해제와 디지털금융보안법 제정도 추진 중이에요. 다만 규제가 완화돼도 세션 기록이 미국에 저장되고 무보존을 못 쓴다는 조건은 그대로라, 개인신용정보나 고객 데이터를 다루는 업무라면 국외 이전 검토가 먼저입니다.

## 정리

![Agents API 선택 기준 정리](/assets/images/ai/openai-agents-api/05-items.webp)
*Agents API 선택 기준 정리 — 출처: 본문 정리 · 자가 렌더*

## 참고 출처

- [[OpenAI] Agents API 개요 문서 (구성 요소·세션·관리형 harness)](https://developers.openai.com/api/docs/guides/agents-api/overview)
- [[OpenAI] Agents API 아키텍처 문서 (환경 세 가지·스트리밍·웹훅)](https://developers.openai.com/api/docs/guides/agents-api/architecture)
- [[OpenAI] OpenAI 호스팅 샌드박스 설정 문서 (packages·network.access·env)](https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted)
- [[OpenAI] 멀티에이전트 문서 (max_concurrent_subagents 기본값 6)](https://developers.openai.com/api/docs/guides/agents-api/multi-agent)
- [[OpenAI] 런타임 비교 표 (Agents API·Agents SDK·Responses API)](https://developers.openai.com/api/docs/guides/agents)
- [[OpenAI] 요금표 (모델 단가·웹 검색·컨테이너)](https://developers.openai.com/api/docs/pricing)
- [[OpenAI] 지원 종료 안내 (Assistants API 2026-08-26 종료)](https://developers.openai.com/api/docs/deprecations)
- [[디지털데일리] 금융권 망분리 전면 해제 추진 (2026-07-15)](https://www.ddaily.co.kr/page/view/2026071517443276094)
- [[ZDNet Korea] 전자금융감독규정 시행세칙 개정 시행 (2026-04-20)](https://zdnet.co.kr/view/?no=20260420161504)
- 환율: 1달러 ≈ 1,400원 기준 환산
