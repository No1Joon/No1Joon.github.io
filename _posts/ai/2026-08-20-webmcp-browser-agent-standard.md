---
title: "웹사이트가 AI 에게 스스로 기능을 알려줍니다 — WebMCP"
description: "에이전트가 화면을 추측하던 방식을 뒤집는 WebMCP 의 동작과 document.modelContext 한 줄, 표준화 절차의 현재 위치를 정리합니다"
date: 2026-08-20
category: AI
subcategory: Explainer
tags: [webmcp, mcp, browser-agents, web-standards, ai-agents]
image: /assets/og/2026-08-20-webmcp-browser-agent-standard.png
---

에이전트한테 항공권을 찾아 달라고 시키면, 지금 그 에이전트는 화면을 캡처해서 어디가 검색 버튼인지 눈으로 짐작합니다. 사람이 하는 짓을 그대로 흉내 내는 거예요.

그걸 뒤집자는 표준이 나왔습니다. **웹사이트가 먼저 "나는 이런 걸 할 수 있고, 이런 값을 넣으면 된다"고 알려주는** 방식이요. 이름은 **WebMCP**입니다.

![사이트가 에이전트에게 할 수 있는 일 목록을 건네는 구조 개념 컷](/assets/images/ai/webmcp-browser-agent-standard/01-agy-hero-handover.webp)
*사이트가 에이전트에게 할 수 있는 일 목록을 건네는 구조 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

🔗 링크 첨부 - [여기에 MCP 편 네이버 링크]

## 지금은 에이전트가 화면을 추측합니다

![화면을 캡처해 클릭 좌표를 추측하는 기존 방식 개념 컷](/assets/images/ai/webmcp-browser-agent-standard/02-agy-guess.webp)
*화면을 캡처해 클릭 좌표를 추측하는 기존 방식 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

InfoQ가 정리한 기존 방식은 이렇습니다. 에이전트가 DOM을 통째로 내려받고, 어느 요소가 버튼 역할인지 파악하고, 스크린샷을 찍어 분석한 다음, 마우스를 어디에 클릭할지 좌표를 추론합니다.

네 단계 전부가 **추측**이에요. 그래서 화면 구조가 조금만 바뀌어도 깨집니다. 버튼 위치가 20픽셀 밀리거나, 팝업이 하나 뜨거나, 로딩이 늦어지면 엉뚱한 곳을 누릅니다.

에이전트가 웹에서 유독 못 미더웠던 이유가 여기 있었습니다. 모델이 멍청해서가 아니라, **애초에 사람 눈으로 보라고 만든 화면을 기계가 되짚어 읽고 있었기** 때문이에요.

## 그래서 사이트가 먼저 알려주기로 했습니다

![Google 로고](/assets/images/ai/webmcp-browser-agent-standard/03-logo-google.webp)
*Google 로고 — 출처: Google*

WebMCP는 Google과 Microsoft 엔지니어들이 만들어 W3C Web Machine Learning 커뮤니티 그룹에서 다듬고 있는 규격입니다. 사이트가 자기 기능을 **도구**로 등록해 두면 브라우저 안의 에이전트가 그걸 발견해 호출합니다.

등록하는 방법은 두 가지예요.

**선언형**은 이미 있는 폼에 속성만 붙입니다.

💻 [소스코드: 폼에 속성으로 도구 선언하기]

    <form toolname="Search flights"
          tooldescription="항공권을 검색합니다"
          toolautosubmit>

**명령형**은 자바스크립트로 등록합니다. 이름과 설명, 입력 스키마, 실제로 실행할 함수를 함께 넘겨요.

💻 [소스코드: 자바스크립트로 도구 등록하기]

    await document.modelContext.registerTool({
      name: "add-todo",
      description: "Add item to todo list",
      inputSchema: {
        type: "object",
        properties: { text: { type: "string" } },
        required: ["text"]
      },
      async execute({ text }) { /* 구현 */ }
    });

**inputSchema**가 핵심입니다. 어떤 값을 어떤 형태로 넣어야 하는지를 사이트가 못 박아 주니까, 에이전트가 화면을 보고 짐작할 일이 없어져요. 등록 말고도 도구를 찾는 **getTools()**, 실행하는 **executeTool()**, 목록이 바뀌면 알려주는 **toolchange** 이벤트가 있습니다.

### 브라우저가 가운데 서 있습니다

여기서 중요한 게, 사이트가 에이전트에게 직접 문을 여는 게 아니라 **브라우저가 중개한다**는 점입니다. 저장소 문서는 이걸 *브라우저 매개 환경* 이라고 부릅니다.

| 통제 장치 | 무엇을 정하나 |
|---|---|
| **allow="tools"** | iframe 이 도구를 쓸 수 있는지 |
| **exposedTo** | 이 도구를 어느 출처에 공개할지 |
| **fromOrigins** | 다른 출처의 도구를 명시적으로 요청 |

원문 표현으로는 브라우저가 호출을 중개하면서 **exposedTo**와 **fromOrigins**가 서로 맞는지를 확인합니다. 사용자 동의도 브라우저가 강제하고요.

설계 철학도 분명합니다. 백엔드를 새로 붙이는 게 아니라 **클라이언트 쪽 도구**라서, 사람이 보던 웹 UI는 그대로 남습니다. 사람과 에이전트가 같은 화면에서 같이 일하는 그림이에요.

## 어디까지 왔나

![WebMCP 표준화 경과](/assets/images/ai/webmcp-browser-agent-standard/04-chart.webp)
*WebMCP 표준화 경과 — 출처: W3C CG 저장소·InfoQ·Chrome 공지 기반 자가 렌더*

스펙 초판은 2025년 8월 13일에 나왔고, W3C 커뮤니티 그룹 초안 보고서가 2026년 4월 23일에 공개됐습니다. Chrome은 2026년 5월 149 버전에서 오리진 트라이얼을 열었고, Microsoft Edge 147은 네이티브로 지원합니다. Firefox와 Safari는 논의에 참여하고 있지만 일정은 밝히지 않았어요.

여기서 한 가지 짚을 게 있습니다. **아직 W3C 표준 트랙이 아닙니다.** 커뮤니티 그룹 단계이고, 그래서 실제로 API가 움직였어요.

원래는 **navigator.modelContext** 였는데, 도구가 특정 페이지에 속한다는 걸 반영해 **document.modelContext** 로 옮겨졌습니다. Chrome 150에서 옛 이름은 폐기 예정이고요. 이 변경이 2026년 8월 10일자입니다.

> 표준이 되기 전이라, 지금 짠 코드는 다음 달에 고쳐야 할 수 있습니다

지금 붙이실 거면 오리진 트라이얼 신청이 필요하고, API 표면이 더 바뀔 수 있다는 걸 감안하셔야 합니다. 프로토타입까지는 충분하지만 운영 서비스에 넣기엔 이릅니다.

### 국내는 지금 반대로 가고 있습니다

재미있는 대목이 여기예요. 표준은 사이트가 에이전트에게 문을 열어 주는 쪽인데, **국내 사이트들은 막는 쪽으로 가고 있습니다.**

네이버는 에이전트 트래픽이 늘면서 스마트스토어와 플레이스에서 캡차가 뜨는 빈도가 올라갔습니다. 쿠팡은 이미 차단이 강한 편이고요. 업계 집계로는 가격표·카탈로그 같은 공개 정보를 긁으려는 시도가 2022년 대비 138% 넘게 늘었다고 합니다.

둘이 모순처럼 보이지만 사실 같은 문제의 앞뒤입니다. 지금 막는 이유는 에이전트가 **사람인 척 몰래** 들어오기 때문이에요. WebMCP처럼 사이트가 무엇을 허용할지 정하고 브라우저가 중개하면, 막을 이유가 줄어듭니다. 무단 수집과 허가된 호출을 구분할 방법이 생기니까요.

### 무엇을 조심해야 하나

도구를 등록한다는 건 **악성 사이트도 도구를 등록할 수 있다**는 뜻입니다. 설명란에 에이전트를 겨냥한 문장을 심어 두는 방식이 바로 프롬프트 인젝션이고, 이건 이미 카톡 요약 같은 일상 기능에서도 문제가 됐던 방식이에요.

브라우저가 중개하고 사용자 동의를 받는 구조는 그래서 장식이 아니라 이 설계의 핵심입니다. 다만 동의 화면이 잦아지면 사람은 결국 습관적으로 누르게 되는데, 그 지점을 어떻게 풀지는 아직 공개된 답이 없습니다.

저장소에 열려 있는 논의만 봐도 멀티모달 입출력, 스트리밍, 출력 스키마, 진행 상황 보고, 서비스 워커 연동이 전부 미결입니다. 방향은 잡혔지만 세부는 아직 그리는 중이에요.

## 참고 출처

- [[W3C Web Machine Learning CG] WebMCP 스펙 저장소 — API 표면·보안 모델·열린 논의](https://github.com/webmachinelearning/webmcp)
- [[InfoQ] WebMCP Standard Proposal for Agentic Web Actuation Now Available in Chrome (2026-06-13)](https://www.infoq.com/news/2026/06/webmcp-web-agent-standard-chrome/)
- [[헤럴드경제] 사람보다 많아진 봇 — 웹 데이터 수집 지형 변화](https://biz.heraldcorp.com/article/10823728)
- [[에스티씨랩] AI 봇은 어떻게 웹사이트와 API를 위협하는가 — 국내 스크래핑 시도 증가 집계](https://www.stclab.com/blog/ai-bots-websites-api-threats)
- 브라우저 지원 현황과 API 이동(2026-08-10)은 Chrome·Edge 릴리스 공지 기준이며, 오리진 트라이얼 단계라 바뀔 수 있습니다
