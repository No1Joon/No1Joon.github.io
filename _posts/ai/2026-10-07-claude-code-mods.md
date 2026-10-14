---
title: "Claude Code mods — 직접 만들어 본 모드와 샌드박스 없는 권한"
description: "이벤트마다 호출되는 함수로 Claude Code 동작을 바꾸는 mods 의 구조와 직접 만든 가드, 설치 전 확인할 권한을 정리합니다"
date: 2026-10-07
category: AI
subcategory: Explainer
tags: [claude-code, mods, plugins, hooks, agent-security]
image: /assets/og/2026-10-07-claude-code-mods.png
---

Claude Code에 mods가 추가됐어요. 스피너 문구를 바꾸는 장식부터 Claude의 명령을 가로채 막는 가드까지, 타입스크립트 함수 몇 줄로 Claude Code 내부 동작을 수정할 수 있습니다.

![스피너 옆에 도구 호출 수를 띄우는 mod 데모](/assets/images/ai/claude-code-mods/01-hero-mods.webp)
*스피너 옆에 도구 호출 수를 띄우는 mod 데모 — 출처: Anthropic*

## mods의 정체

mod는 Claude Code에서 이벤트가 발생할 때마다 호출되는 자바스크립트·타입스크립트 함수 묶음이에요. 도구 호출, 프롬프트 제출, 화면 그리기가 이벤트이고, 함수는 그 이벤트를 감시하거나, 수정해 전달하거나, 직접 응답해 원래 동작을 대신할 수 있습니다.

Anthropic 개발자 계정은 10월 1일 이 기능을 발표했고, 터미널은 v2.1.287부터, 데스크톱 앱 Code 탭은 v2.1.286부터 기본으로 활성화돼 있어요. 실측은 v2.1.292에서 했습니다.

기존 확장 수단과의 차이는 실행 위치입니다.

| 수단 | 실행 위치 | 화면 그리기 |
| :--- | :--- | :--- |
| **mod** | <mark>Claude Code 프로세스 안</mark> | 가능 |
| 설정 훅 | 외부 스크립트·HTTP | 불가 |
| 스킬 | Claude가 읽는 문서 | 불가 |
| MCP 서버 | 외부 프로세스 | 불가 |

/diff 창과 AGENTS.md 읽기 기능도 이제 내장 mod로 실행됩니다. 공식 문서의 첫 예제는 도구 호출 수를 집계해 스피너 옆에 표시하는 mod로, 위 데모가 그 결과예요.

## 직접 만든 가드 mod

![rm-guard 훅 모듈 코드](/assets/images/ai/claude-code-mods/02-term.webp)
*rm-guard 훅 모듈 코드 — 출처: 직접 작성 코드 자가 렌더*

첫 번째로 Claude가 Bash로 rm -rf나 강제 푸시를 실행하려 하면 차단하는 rm-guard를 만들었어요.

[.claude-plugin/plugin.json]
이름·버전·설명을 적는 플러그인 매니페스트

[hooks/hooks.json]
훅 모듈 파일 경로 한 줄

[hooks/register.ts]
이벤트에 함수를 등록하는 본체

**tool.call** 이벤트에서 Bash 호출만 골라 받고, 명령이 패턴에 맞으면 **deny**를 반환해 실행을 차단합니다. 맞지 않으면 **next(e)**로 원래 흐름에 전달하고, 차단할 때마다 상태 줄에 누적 횟수를 표시해요.

![rm-guard validate 출력 전후](/assets/images/ai/claude-code-mods/03-term.webp)
*rm-guard validate 출력 전후 — 출처: claude plugin validate 실행 출력 자가 렌더*

**claude plugin validate**는 첫 버전에 「gating hook without .catch」 경고를 표시했어요. 막는 역할을 하는 훅에 오류 처리기가 없다는 뜻입니다. 공식 문서 설명대로라면 훅이 예외를 던지거나 제한 시간을 넘기면 Claude Code는 그 훅을 실행하지 않아, 검사 코드에 오류가 생기면 명령이 그대로 실행돼요. **.catch**를 추가해 검사가 실패하면 거부하도록 바꾸자 경고가 「with .catch」로 바뀌었습니다.

## 테스트로 확인한 가드의 한계

![rm-guard 테스트 5건 결과](/assets/images/ai/claude-code-mods/04-term.webp)
*rm-guard 테스트 5건 결과 — 출처: claude plugin test 실행 출력 자가 렌더*

**claude plugin test**는 세션 없이 mod의 테스트 파일을 실행해요. 다섯 건을 입력했는데, 앞의 둘은 의도대로 rm -rf build를 차단하고 ls를 통과시켰습니다.

나머지 셋은 같은 일을 하는 다른 표기를 입력해 본 것이고, 세 건 모두 차단되지 않았어요.

| 명령 | 하는 일 | 가드 결과 |
| :--- | :--- | :--- |
| rm -rf build | 폴더 강제 삭제 | **차단** |
| rm -r -f build | 같음 | <mark>통과</mark> |
| rm --recursive --force build | 같음 | <mark>통과</mark> |
| find build -delete | 같음 | <mark>통과</mark> |

문자열 패턴으로 명령을 필터링하는 가드는 표기만 바꾼 명령을 탐지하지 못합니다. Anthropic 샘플 mod인 blast-radius도 위험한 셸 명령을 탐지해 표시하는 용도이고, 이런 mod는 안전장치를 하나 더하는 것이지 격리가 아니에요. 지워지면 안 되는 경로는 settings.json의 **deny** 규칙으로 차단하고, Bash 격리가 필요하면 Claude Code 샌드박스를 활성화하는 쪽이 맞습니다.

> 한 줄 요약: mod 가드는 실수를 줄이는 장치이고, 우회하려는 명령까지 차단하지는 못합니다.

## mods가 제공하는 권한

mod에는 샌드박스가 없어요. 공식 문서는 mod가 설치한 사용자의 권한으로 실행되며 파일 읽기·쓰기, 프로그램 실행, 네트워크 요청을 할 수 있다고 적고 있습니다.

| 할 수 있는 것 | 관련 API |
| :--- | :--- |
| 파일 읽기·쓰기 | **$.fs.read · $.fs.write** |
| 프로그램 실행 | **$.process.run** |
| 네트워크 요청 | **$.http.fetch** |
| 환경 변수·설정 읽기 | **$.env.get** |
| 모델 호출 | <mark>사용자 요금제로</mark> |
| 도구 호출 승인 | **tool.check** 훅 |

ask 규칙이 물어볼 호출을 mod가 대신 승인할 수 있고, auto 모드에서는 mod가 승인한 호출이 분류기 검사 없이 실행돼요. Claude Code 샌드박스를 활성화해도 격리되는 것은 Claude가 실행하는 Bash 명령이고, mod가 실행한 프로세스는 샌드박스 밖에서 동작합니다.

deny 규칙도 범위가 정해져 있어요. 내장 가드가 로드된 환경에서는 deny 규칙이 사용자 mod의 승인보다 앞서지만, 이는 Claude의 도구 호출에만 해당합니다. 공식 문서 예시대로 **Read(.env)**를 차단해 두어도 mod는 **$.fs.read**로 그 파일을 직접 읽을 수 있어요.

Team·Enterprise 플랜으로 로그인했거나 관리 설정이 있는 기기에서는 내장 가드 **sec-default**가 사용자 mod보다 먼저 로드돼, 조직이 관리하는 훅·지침·설정을 사용자 mod가 수정하지 못하도록 제한합니다. API 키로만 쓰는 개인 사용자에게는 관리 설정이 없으면 이 가드가 로드되지 않아요.

## 남의 mod를 설치 전에 보는 법

![직접 만든 memo와 Anthropic 샘플 blast-radius의 validate 출력](/assets/images/ai/claude-code-mods/05-term.webp)
*직접 만든 memo와 Anthropic 샘플 blast-radius의 validate 출력 — 출처: claude plugin validate 실행 출력 자가 렌더*

**claude plugin validate**는 mod를 실행하지 않고 코드만 읽어, 어떤 이벤트를 받는지(hooks 줄)와 어떤 API를 부르는지(calls 줄)를 보여 줘요. Claude Code는 이 명령이 분석할 수 없는 방식으로 API를 쓰는 mod는 로드를 거부합니다.

두 번째로 만든 memo는 /memo 명령으로 받은 글을 홈 폴더 파일에 저장하는 mod예요. validate는 **$.fs.write**와 함께 **env reads: HOME**을 표시해, 이 mod가 파일을 쓰고 HOME 환경 변수를 읽는다는 것을 실행 전에 표시했습니다.

Anthropic 공식 샘플 두 개도 같은 방식으로 확인했어요. 컨텍스트 사용량을 그리는 token-weather는 사용량 조회와 화면 그리기만 불렀고, blast-radius는 **$.process.run**으로 프로그램을 실행하며 막는 훅에 .catch가 없다는 경고가 나왔습니다. 공식 샘플도 프로세스를 실행하니, calls 줄에 $.process가 있다고 악성은 아니에요. 그 줄이 보이면 코드를 확인해 무엇을 실행하는지 읽어야 한다는 뜻입니다.

hooks 줄에서는 **tool.call**과 **prompt.submit**을 확인해요. 둘은 모든 도구 호출과 프롬프트를 보고 바꿀 수 있다는 뜻이고, **tool.check**는 권한 프롬프트가 표시되기 전에 승인하거나 거부할 수 있다는 뜻입니다.

권한 프롬프트를 줄이는 허용 목록을 다룬 앞선 글과 같이 보면, mod가 승인을 대신하는 범위가 더 분명히 보여요.

[스킬 실사용 (3) — Claude Code 명령 12,411건 중 81%는 원래 묻지도 않았습니다](/posts/skill-in-use-03-permission-prompts/)

## 사용자와 조직의 조치

![mods 점검 정리 카드](/assets/images/ai/claude-code-mods/06-items.webp)
*mods 점검 정리 카드 — 출처: Anthropic 공식 문서 기반 자가 렌더*

### 조직 관리자

- 사용자 mod를 제한하려면 관리 설정의 sec-default 옵션 **allowManagedModsOnly**를 활성화
- 승인한 마켓플레이스만 허용하려면 **disableSideloadFlags**로 --plugin-dir 로드를 차단
- 정책 mod를 만들어 **plugin.register** 이벤트에서 위험 API를 쓰는 mod를 거부할 수 있음

국내 조직도 같은 설정을 관리 설정 파일·MDM·claude.ai 관리 콘솔로 적용할 수 있으며, 한국어 공식 문서는 아직 없고 영어 원문을 기준으로 해야 합니다.

## 참고 출처

- [[Anthropic] Mods overview (정의·할 수 있는 일·버전·샌드박스 없음, 본문 이미지 1점 출처)](https://code.claude.com/docs/en/plugins/mods/overview)
- [[Anthropic] Manage mods for your organization (sec-default·deny 규칙 범위·validate 읽는 법)](https://code.claude.com/docs/en/plugins/mods/admin)
- [[Anthropic] Create a mod (파일 구성)](https://code.claude.com/docs/en/plugins/mods/create)
- [[GitHub] anthropics/claude-code-playground mods (token-weather·blast-radius 샘플)](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods)
- [[Pasquale Pillitteri] Claude Code Gets Mods, Plugins That Rewrite the Agent (10월 1일 발표)](https://pasqualepillitteri.it/en/news/19871/claude-code-mods-plugins)
