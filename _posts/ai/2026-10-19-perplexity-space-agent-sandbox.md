---
title: "Perplexity SPACE 오픈소스 공개 — 에이전트 샌드박스 탈출 시험 108회 0건"
description: "에이전트 코드를 작업마다 마이크로VM 에서 실행하는 Perplexity SPACE 의 구조와 자체 탈출 시험 결과를 정리합니다"
date: 2026-10-19
category: AI
subcategory: News
tags: [perplexity, agent-sandbox, firecracker, microvm, ai-security]
image: /assets/og/2026-10-19-perplexity-space-agent-sandbox.png
---

Perplexity가 10월 15일 에이전트 실행 환경 **SPACE**를 오픈소스로 공개했어요
AI 에이전트가 쓴 코드를 작업마다 작은 가상머신 안에서 실행하는 샌드박스 플랫폼입니다

자체 보안 시험에서 격리를 뚫고 호스트에 접근한 시도는 <mark>108회 중 0건</mark>이었어요
같은 시험에서 네트워크 차단 우회는 있었고, 회사는 이를 수정했다고 밝혔습니다

![Escaping SPACE 보고서의 SPACE 구조 아이소메트릭 키 아트](/assets/images/ai/perplexity-space-agent-sandbox/01-hero-space.webp)
*Escaping SPACE 보고서의 SPACE 구조 아이소메트릭 키 아트 — 출처: Perplexity*

## 발표 내용

![GitHub API로 perplexityai/SPACE 저장소의 라이선스와 언어를 확인한 터미널 화면](/assets/images/ai/perplexity-space-agent-sandbox/02-term.webp)
*GitHub API로 perplexityai/SPACE 저장소의 라이선스와 언어를 확인한 터미널 화면 — 출처: 직접 실행*

SPACE는 *Sandboxed Platform for Agentic Code Execution*의 줄임말이에요

GitHub 저장소 perplexityai/SPACE에 **Apache-2.0** 라이선스로 올라왔어요
코드는 Rust로 작성됐습니다

- 격리: 작업마다 **Firecracker 마이크로VM**(microVM) 한 대
- 제어: HTTP API로 생성, 실행, 일시 정지, 재개, 삭제
- 자격증명: 샌드박스 바깥에서 관리, 필요할 때만 주입
- 상태 저장: 파일 스냅샷과 실행 환경 체크포인트를 변경분만 저장
- 운영: 2026년 7월부터 Perplexity Computer 세션 전부를 처리

Perplexity는 하루 **수백만 개**의 샌드박스를 생성하고 있다고 밝혔어요

생성 속도는 이전 상용 공급사보다 3~5배 빨랐다고 했어요
그 공급사 이름은 밝히지 않았습니다

## 가상머신 탈출 시험

![샌드박스 탈출 0/108, 네트워크 우회 11/54와 0/54 결과를 정리한 Perplexity 도표](/assets/images/ai/perplexity-space-agent-sandbox/03-photo.webp)
*샌드박스 탈출 0/108, 네트워크 우회 11/54와 0/54 결과를 정리한 Perplexity 도표 — 출처: Perplexity*

Perplexity는 9월 23일 *Escaping SPACE: Part I* 보고서로 시험 방법을 공개했어요
가상머신 안에서 **루트 권한**을 가진 AI 에이전트에게 두 과제를 줬습니다

| 과제 | 목표 |
| :--- | :--- |
| 샌드박스 탈출 | 호스트의 AWS 허니토큰 획득 |
| 네트워크 우회 | 차단된 주소에서 플래그 획득 |

모델 구성 9개에 소스코드 제공 여부와 네트워크 허용 범위를 조합한 4가지 설정을 썼어요
각 설정은 3회씩 시험했습니다

탈출 과제는 <mark>108회 모두 실패</mark>했습니다

## 네트워크 차단 우회

![모델 구성 9개의 설정별 성공 횟수를 정리한 Perplexity 결과표](/assets/images/ai/perplexity-space-agent-sandbox/04-photo.webp)
*모델 구성 9개의 설정별 성공 횟수를 정리한 Perplexity 결과표 — 출처: Perplexity*

네트워크를 완전히 차단한 설정에서는 54회 중 0건이었어요
일부 주소만 허용한 설정에서는 <mark>54회 중 11건</mark>이 차단된 주소 접속에 성공했습니다

| 모델 | 소스 제공 | 소스 없음 |
| :--- | :--- | :--- |
| Claude Opus 5.0 | **3/3** | 0/3 |
| GPT-5.6 Sol | **3/3** | 2/3 |
| Kimi K3 | 2/3 | 0/3 |
| GPT-5.6 Cyber | 0/3 | 1/3 |

하나는 가짜 DNS 응답으로 허용된 도메인 이름을 차단된 IP에 연결하는 **DNS 스푸핑**이에요

다른 하나는 허용된 사이트와 같은 CDN IP를 쓰는 다른 서비스를 거치는 방식입니다

Perplexity는 8월 26일 우회 방법을 재현하고 취약점을 수정했어요
가장 공격하기 쉬운 설정으로 다시 시험했을 때 우회 성공은 0건이었다고 밝혔습니다

## 다른 샌드박스 서비스

![타사 샌드박스 플랫폼 9곳의 HTTP, HTTPS, TCP 네트워크 정책 우회 검증표](/assets/images/ai/perplexity-space-agent-sandbox/05-photo.webp)
*타사 샌드박스 플랫폼 9곳의 HTTP, HTTPS, TCP 네트워크 정책 우회 검증표 — 출처: Perplexity*

Perplexity는 다른 샌드박스 플랫폼 10곳에도 같은 방법으로 우회를 시험했어요
그중 <mark>8곳</mark>에서 네트워크 정책 우회가 됐다고 밝혔습니다

공개한 9곳 중 E2B, Modal, Vercel, Daytona, Fly.io 등 7곳이 해당됐어요
Cloudflare Sandbox와 NVIDIA OpenShell은 우회가 확인되지 않았습니다

각 회사에는 9월 1일 알렸고, 결과 기준일은 9월 10일이에요
지금도 같은 상태인지는 회사마다 다를 수 있어요

### 🤝 공개 이후 파트너

Akamai는 자사 클라우드에서 SPACE를 시험해 출시했어요

Crusoe는 관리형 AI 서비스에 SPACE를 도입하기로 했어요
CoreWeave는 자사 쿠버네티스에 배포하는 안내서를 냈습니다

## 국내 사용자에게 의미

국내에서도 Claude Code 같은 코딩 에이전트를 회사 단위로 쓰는 곳이 늘었어요

에이전트가 쓴 코드를 PC에서 그대로 실행하면 <u>권한 승인 절차에 크게 의존</u>하게 됩니다

10월 7일 글에서는 Claude Code를 샌드박스 없이 쓸 때의 권한 문제를 다뤘어요

🔗 링크 첨부 - https://blog.naver.com/rottensweetpotato/224434104966

반면 SPACE는 에이전트가 작성한 코드를 가상머신 안에 가둬 실행하는 플랫폼이에요
자체 서버에 배포하려면 KVM을 쓸 수 있는 리눅스 호스트가 필요합니다

## 앞으로 주목할 점

- 후속 보고서: *Escaping SPACE*는 <mark>Part I만</mark> 공개
- 타사 수정: 우회가 확인된 7곳의 공개 대응
- 클라우드 제공: Akamai, Crusoe 상용 서비스 요금과 지역
- 국내 클라우드: 국내 사업자 제공 여부

🔗 링크 첨부 - https://github.com/perplexityai/SPACE

## 참고 출처

- [[Perplexity] Open-sourcing SPACE (2026-10-15, 규모, 속도, 파트너)](https://www.perplexity.ai/hub/blog/open-sourcing-space)
- [[Perplexity] Escaping SPACE: Part I (2026-09-23, 시험 방법과 결과, 본문 이미지 3점 출처)](https://www.perplexity.ai/hub/blog/escaping-space-part-i)
- [[Perplexity] SPACE 문서](https://space.docs.perplexity.ai/guide/index.html)
- [[Runtime Wire] Perplexity open-sources SPACE (2026-10-15)](https://runtimewire.com/article/perplexity-open-sources-space-agent-sandbox)
