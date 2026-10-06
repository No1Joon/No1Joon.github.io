---
title: "ChainDrop — 서명이 유효한데도 악성이었습니다"
description: "네 시간 만에 400개 넘는 패키지를 오염시킨 npm 웜이 SLSA provenance 검증을 통과한 이유와, 증명이 보증하는 범위를 정리합니다"
date: 2026-09-08
category: Tech
subcategory: Explainer
tags: [supply-chain-attack, npm, slsa, provenance, developer-security]
image: /assets/og/2026-09-08-chaindrop-npm-worm-provenance.png
---

패키지 하나를 받았는데 서명이 붙어 있고, 그 서명이 진짜입니다. 인가된 빌드 시스템이 실제로 만들었다는 증명까지 검증을 통과해요. 그런데 내용물은 악성이었습니다.

8월 4일 npm에서 퍼진 자기복제 웜 ChainDrop이 그런 경우였습니다. 규모도 컸지만 더 중요한 건 이 사건이 증명이라는 장치의 경계를 그대로 드러냈다는 점이에요.

![검증 도장과 내용물이 따로 노는 장면](/assets/images/tech/chaindrop-npm-worm-provenance/01-agy-hero.webp)
*검증 도장과 내용물이 따로 노는 장면 — 출처: 개념 컷 · agy 자가 생성*

## 네 시간 동안 일어난 일

Elastic Security Labs는 2026년 8월 4일 미국 동부 시간 오전 5시 39분경 이 공격을 처음 탐지했다고 밝혔습니다. 출발점은 캐시 라이브러리 keyv의 유지보수자 계정이 침해된 것이었어요.

Zscaler ThreatLabz 분석에 따르면 확산은 네 시간이 채 걸리지 않았고, 정점에서는 초당 한 개꼴로 오염된 패키지가 발행됐습니다. Unit 42는 8월 6일 분석에서 400개가 넘는 패키지가 감염됐고, 웜이 만든 공개 GitHub 저장소가 453개 확인됐다고 적었어요.

정확한 개수는 분석 주체마다 갈립니다. Unit 42·Elastic·Zscaler는 400개 이상으로 잡았고, 444개 패키지와 2,200여 개 버전으로 세는 집계도 있어요. 어느 쪽이든 공통점은 오염된 것이 무명 패키지가 아니라는 점입니다.

![오염된 주요 패키지의 주간 다운로드](/assets/images/tech/chaindrop-npm-worm-provenance/02-chart.webp)
*오염된 주요 패키지의 주간 다운로드 — 출처: npm 레지스트리 다운로드 통계 기반 자가 렌더*

keyv는 최근 한 주에만 1억 4,200만 번 내려받혔고 flat-cache는 1억 3,600만 번이었습니다. 직접 설치한 적이 없어도 다른 패키지의 하위 의존성으로 함께 설치되는 라이브러리들이에요.

- 2026년 8월 4일 탐지 · 시작점은 keyv 유지보수자 계정 침해
- 네 시간 이내 확산 · 400개 이상 패키지 오염 (집계에 따라 444개)

## 공격이 성립하려면 무엇이 있어야 했나

이 공격은 세 가지 전제가 맞물려 성립했습니다.

첫째는 유지보수자 계정입니다. 공격자가 정당한 권한을 손에 넣었기 때문에 남의 저장소가 아니라 그 저장소의 main 브랜치에 코드를 넣을 수 있었습니다.

둘째는 npm의 정상 기능입니다. package.json의 **preinstall** 훅은 설치 전에 명령을 실행하라는 규격이고, 웜은 여기에 **node setup.mjs** 한 줄을 넣었어요. 이용자 동의를 묻는 단계가 원래 없는 자리입니다.

셋째는 그 저장소의 정식 CI 파이프라인입니다. 공격자는 별도 빌드를 하지 않고 GitHub Actions 워크플로를 그대로 돌렸습니다. 그래서 나온 산출물이 인가된 빌드 시스템의 산출물이 됐어요.

Unit 42에 따르면 드로퍼는 정상 런타임인 Bun 1.3.13을 내려받아 727KB 짜리 난독화 JavaScript 페이로드를 실행했습니다. 실행 파일을 새로 심는 대신 정상 도구를 그대로 쓰는 방식이에요.

## 서명이 유효했다는 말의 뜻

Zscaler는 악성 패키지가 암호학적으로 유효한 SLSA Build Level 3 증명과 함께 발행됐다고 적었어요. Unit 42도 웜이 워크플로 안에서 OIDC 토큰을 받아 Fulcio 인증서를 얻고 in-toto SLSA 증명문을 만드는 경로를 확인했습니다.

SLSA(Supply-chain Levels for Software Artifacts)는 이 산출물이 어떤 빌드 시스템에서 어떤 소스로 만들어졌는지를 증명하는 규격입니다. Sigstore는 그 증명에 서명을 붙이는 체계예요. 두 장치가 답하는 질문은 하나입니다. 이것을 누가 만들었는가.

| 증명이 말하는 것 | 증명이 말하지 않는 것 |
|---|---|
| 인가된 빌드 시스템이 만듦 | 코드가 안전함 |
| 지정된 저장소에서 나옴 | 그 저장소가 침해되지 않음 |
| 산출물이 바뀌지 않음 | 원본이 원래 정상임 |

공격자가 유지보수자 권한으로 그 저장소의 워크플로를 돌리면 증명은 정직하게 발급됩니다. 시스템이 속은 게 아니라 정확히 설계대로 동작한 거예요. Zscaler는 SLSA·Sigstore 증명을 안전의 증거로 취급하지 말라고 단호하게 권고합니다.

![npm 로고](/assets/images/tech/chaindrop-npm-worm-provenance/03-npm-icon-color.webp)
*npm 로고 — 출처: npm*

## 훔친 것은 코드가 아니라 자격증명

페이로드가 노린 대상을 보면 목적이 분명해집니다. Elastic은 이 악성코드가 300개가 넘는 패턴으로 자격증명을 훑었다고 밝혔어요.

[클라우드]
AWS·GCP·Azure·Alibaba Cloud 자격증명과 임시 토큰

[개발·배포]
GitHub 개인 액세스 토큰과 세션 토큰, npm 토큰, SSH 개인키, HashiCorp Vault, 쿠버네티스 서비스 계정 토큰, Terraform 상태, Docker·Helm 설정

[AI 도구]
Anthropic·Claude·Codex·Cursor·OpenAI·Gemini 관련 설정과 키

훔친 자격증명은 피해자의 GitHub 토큰으로 새로 만든 공개 저장소에 올라갔습니다. Zscaler는 그 저장소 설명란에 **Shai-Hulud: Here We Go Again** 이라는 문구가 붙어 있었다고 적었어요. 명령·제어 채널은 이더리움 스마트 컨트랙트에 주소를 숨기는 EtherHiding 방식을 썼습니다.

## 설정 파일이 실행 코드가 되는 자리

지속화 수법이 이번 사건에서 개발자에게 가장 직접적입니다. Unit 42 분석에 따르면 웜은 두 곳에 자기를 남겼어요.

- **.vscode/tasks.json**에 Environment Setup 이라는 이름의 작업을 추가
- **.claude/settings.json**에 SessionStart 명령 훅을 추가

둘 다 저장소를 열면 도는 자리입니다. 패키지를 지우고 토큰을 바꿔도 이 파일이 남아 있으면 다음에 그 폴더를 여는 순간 다시 실행돼요.

Zscaler는 IDE와 AI 에이전트 설정 파일을 실행 코드로 취급해야 한다고 지적합니다. 지금까지 설정 파일은 코드 리뷰에서 가볍게 넘어가는 자리였는데, 이번 사건이 그 전제를 깼습니다.

## 처음이 아닌 Shai-Hulud 계열

ChainDrop은 Shai-Hulud 라는 이름으로 이어져 온 계열의 최신 판입니다. Zscaler가 정리한 흐름을 보면 수법이 어디로 옮겨왔는지 보여요.

| 시기 | 구분 | 바뀐 것 |
|---|---|---|
| 2025년 9월 | Shai-Hulud V1 | postinstall 훅 |
| 2025년 11월 | 두 번째 판 | preinstall 전환·Bun 사용 |
| 2026년 4월 | 소규모 파동 | Actions 캐시 오염 |
| 2026년 8월 | ChainDrop | 이더리움 기반 C2 |

훅이 postinstall에서 preinstall로 옮겨간 것이 특히 중요합니다. 설치가 끝난 뒤가 아니라 시작되기 전에 돌기 때문에 개발자 노트북과 CI 러너 양쪽에서 실행 범위가 넓어졌어요.

## 지금 할 수 있는 것

이번 사건에서 막는 자리는 패치가 아니라 설치 이전입니다.

💻 [소스코드: 잠긴 의존성으로만 설치하기]

    npm ci
    npm audit signatures

- lockfile을 고정하고 설치는 **npm ci**로 (**npm install**은 잠금을 갱신함)
- 새 버전을 바로 올리지 않고 며칠 대기 기간을 두기
- npm 계정에 피싱 저항 다중 인증(FIDO2·WebAuthn) 적용
- Elastic 권고대로 preinstall 훅을 막는 npm 12 이상으로 올리기

감염이 의심되면 순서가 하나 더 붙습니다. 자격증명을 먼저 바꾸고 파일을 지우는 게 아니라, 남아 있는 훅부터 확인해야 다시 실행되지 않아요.

- **.vscode/tasks.json**·**.claude/settings.json**에 모르는 작업·훅이 있는지 확인
- **setup.mjs**·**math_init.js** 같은 낯선 파일이 저장소에 들어왔는지 확인
- npm·GitHub·클라우드·SSH·AI 도구 토큰을 회수하고 재발급

국내 접점은 사용 그 자체입니다. keyv·flat-cache는 국내 서비스의 Node.js 의존성 트리에도 흔히 들어가 있고, 이번 웜이 노린 **.claude**와 **.cursor** 설정은 국내 개발자가 지금 쓰는 도구의 설정 파일이에요. 다만 이 사건에 대한 KISA 보안 공지는 확인되지 않았고, 해외에서는 싱가포르 사이버보안청이 별도 권고를 냈습니다.

침해 신고와 상담 창구는 KISA 118 입니다.

🔗 링크 첨부 - https://www.krcert.or.kr

![글 끝 정리](/assets/images/tech/chaindrop-npm-worm-provenance/04-items.webp)
*글 끝 정리 — 출처: 본문 정리 · 자가 렌더*

## 남는 질문

증명 체계를 버리자는 이야기가 아닙니다. 증명이 없으면 이번 같은 사건에서 어느 저장소의 어느 워크플로가 산출물을 만들었는지조차 추적할 수 없어요.

문제는 그 증명을 읽는 쪽의 기대입니다. 초록색 검증 표시를 보고 안전하다고 읽으면 이번 같은 공격은 그 표시를 그대로 통과합니다. 증명은 출처를 말하고, 내용의 안전은 여전히 다른 장치가 맡아야 해요.

> 서명이 답하는 것은 누가 만들었는가이지 무엇이 들어 있는가가 아닙니다.

## 참고 출처

- [[Unit 42] ChainDrop npm worm analysis (2026.08.06)](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)
- [[Zscaler ThreatLabz] Tracking Shai-Hulud: Inside the ChainDrop npm worm](https://www.zscaler.com/blogs/security-research/tracking-shai-hulud-inside-chaindrop-npm-worm)
- [[Elastic Security Labs] Shai-Hulud strikes again: CHAINDROP worm hits 400+ npm packages](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)
- [[Cyber Security Agency of Singapore] Ongoing npm supply chain attack affecting keyv and related packages (AD-2026-009)](https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-009/)
