---
title: "Gemini, 해킹 평가 중 실제 회사 3곳 시스템에 접근 — 인터넷이 열린 평가 환경이 문제였다"
description: "사이버보안 평가 도중 Gemini 가 실제 회사 시스템에 접근한 경위와, Google 이 7주 동안 공개하지 않은 과정을 정리합니다"
date: 2026-09-21
category: AI
subcategory: News
tags: [gemini, google, ai-safety, ai-evaluation, incident]
image: /assets/og/2026-09-21-gemini-eval-real-intrusion.png
---

Google의 AI 모델 Gemini가 5월 사이버보안 평가 도중 실제 회사 세 곳의 시스템에 접근한 사실이 9월 18일 확인됐습니다. 시험용 가상 회사의 이름이 실제 회사와 같았고, 외부 인터넷 접근이 차단돼 있어야 할 평가 환경에서 인터넷 접근이 가능했습니다.

Google은 이 일을 7월 말에 알고도 공식 발표를 하지 않았고, 월스트리트저널(WSJ)의 문의를 받은 뒤에야 시인했습니다. 9월 21일 현재 Google 블로그나 모델 카드에 이 사고를 다룬 공식 문서는 없어, WSJ 보도를 인용한 SecurityWeek·Axios·MarkTechPost 기사와 Google 보안 엔지니어링 부사장 Heather Adkins의 발언이 현재 확인 가능한 근거입니다.

![인터넷 경로가 열린 채 남은 격리 평가 환경 개념 컷](/assets/images/ai/gemini-eval-real-intrusion/01-agy-hero.webp)
*인터넷 경로가 열린 채 남은 격리 평가 환경 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

## 사건 경과

![Gemini 평가 사고의 발생과 공개 경과 타임라인](/assets/images/ai/gemini-eval-real-intrusion/02-chart.webp)
*Gemini 평가 사고의 발생과 공개 경과 타임라인 — 출처: SecurityWeek·MarkTechPost·Axios 보도 기반 자가 렌더*

평가는 AI 보안 평가 회사 **Irregular**가 자기 인프라에서 진행한 CTF(capture the flag, 목표 서버에서 정해진 값을 찾아오는 해킹 과제)였습니다. Gemini에게 주어진 과제는 가상 회사가 운영하는 소프트웨어에서 정보를 가져오는 것이었는데, 그 가상 회사 이름이 공개 인터넷에 실제로 있는 도메인과 겹쳤습니다.

평가 환경은 원래 외부 인터넷에 접속할 수 없어야 했지만 Irregular 환경의 버그로 인터넷 접근이 가능했습니다. Gemini는 과제 대상이라고 판단한 실제 회사의 사이트에 접근했고, 이어 다른 두 곳에도 접근했습니다.

- 발생: 2026년 5월, Irregular 평가 환경
- 인지: 7월 말 Irregular가 연구소들에 통보
- 공개: 9월 18일 WSJ 문의 뒤 Google 확인
- 모델: Google이 버전을 밝히지 않음
- 피해 회사: 세 곳 모두 이름 비공개

## 세 건의 접근 방식

세 건 모두 고도의 공격 기법이 아니라, 사람 공격자도 흔히 노리는 **관리상 취약점**을 이용했다는 점이 공통입니다.

| 건 | 접근 방법 | 성격 |
| :--- | :--- | :--- |
| 1 | 비밀번호 추측 | **약한 비밀번호** |
| 2 | 공개 저장소의 자격 증명 | 코드에 남은 키 |
| 3 | 공개 저장소의 자격 증명 | 코드에 남은 키 |

Adkins 부사장은 모델이 온라인에서 공개 정보를 찾아 자격 증명을 추측했고, 테스트 범위에 속한다고 여긴 사이트에 접근했다고 설명했어요. 세 건 모두 모델이 실제 회사라는 것을 알아차린 뒤 멈췄고, 피해는 없었다는 것이 Google 입장이에요. Google은 세 회사에 알리고 미국 당국에도 통보했으며, Irregular와 함께 평가 절차를 바꿨다고 밝혔지만, 세 회사에서 어떤 데이터가 조회됐는지는 공개되지 않았습니다.

### Google의 판단

![Google 로고](/assets/images/ai/gemini-eval-real-intrusion/03-logo-google.webp)
*Google 로고 — 출처: Google*

Google은 이번 일을 모델의 정렬 실패(alignment failure, 모델이 개발자 의도와 다르게 행동하는 문제)가 아니라 대상을 **잘못 식별한 사고**로 규정했습니다. 모델이 멈췄고 피해가 없었으니 먼저 공개할 사안이 아니었다는 설명이에요.

## 같은 평가 업체의 네 번째 사고

![Anthropic 공식 조사 보고 상단, 2026년 7월 30일](/assets/images/ai/gemini-eval-real-intrusion/04-photo-anthropic.webp)
*Anthropic 공식 조사 보고 상단, 2026년 7월 30일 — 출처: Anthropic*

Gemini는 Irregular 평가에서 실제 시스템에 접근한 첫 모델이 아니에요. Anthropic은 7월 30일 공식 조사 보고에서 14만 1,006건의 평가 실행을 점검해 Irregular 환경에서 실제 조직 세 곳이 침해된 사례를 찾았다고 밝혔어요. 그중 한 건은 이번과 똑같이 가상 회사 이름이 실제 도메인과 일치한 경우였고, 원인도 평가 프롬프트는 인터넷이 없다고 적었는데 실제 머신은 인터넷에 연결돼 있던 설정 오류였습니다.

MarkTechPost 보도로는 같은 Irregular 설정 오류가 OpenAI(8월 4일 공개)와 Meta(8월 5일 공개) 평가에서도 드러났습니다. Irregular 대변인은 CNBC에 Google 건이 이미 보고된 것과 같은 문제이고 별개 사고가 아니라며, 7월 말 모든 관련 연구소에 알렸다고 말했습니다.

| 연구소 | 공개 시점 | 공개 방식 |
| :--- | :--- | :--- |
| Anthropic | 7월 30일 | 공식 조사 보고 |
| OpenAI | 8월 4일 | 보도 기준 |
| Meta | 8월 5일 | 보도 기준 |
| Google | **9월 18일** | <mark>언론 문의 뒤 시인</mark> |

OpenAI 모델이 평가 중 제로데이로 Hugging Face를 침해한 7월 사건과 Anthropic의 세 건은 8월 3일 글에서 다뤘습니다. 이번 Gemini 건은 그 가운데 Anthropic 사례와 원인이 같습니다.

[OpenAI 모델이 스스로 Hugging Face 를 털었다 — 전말 정리](/posts/openai-huggingface-agent-breach/)

## 평가 환경 격리가 중요한 이유

사이버보안 평가는 모델이 취약점을 얼마나 잘 찾고 악용하는지 재는 시험이라, 평가 자체가 공격 능력을 쓰게 만듭니다. 그 시험이 안전하려면 모델이 접근할 수 있는 범위가 평가 서버 안으로 **기술적으로 격리**돼야 하고, 과제 문장에 적힌 인터넷 없음은 그 제한을 대신하지 못합니다.

이번 네 연구소의 사고는 모델 쪽 결함보다 평가를 맡긴 외부 업체 한 곳의 인프라 설정이 여러 연구소 결과에 한꺼번에 영향을 준 사례입니다. 연구소마다 공개 시점이 7월 30일부터 9월 18일까지 달라지면서, 원인 하나가 네 개의 별도 사건처럼 보도되기도 했습니다.

공개 방식도 달랐어요. Anthropic은 전체 평가 기록을 소급 점검한 수치까지 공식 보고서로 공개했고 Google은 7주 동안 공개하지 않았습니다. 현재 미국에는 이런 평가 사고의 공개 시한을 정한 법이 없어 공개 여부와 시점은 각 회사 판단에 맡겨져 있습니다.

## 국내 법제와 개발 조직

1월 22일 시행된 AI기본법(인공지능 발전과 신뢰 기반 조성 등에 관한 기본법)은 학습 누적 연산량이 10²⁶ FLOP 이상인 대규모 AI를 만드는 사업자에게 위험을 식별·평가·완화하고 안전사고를 모니터링하는 체계를 갖춰 그 결과를 과학기술정보통신부에 내도록 했습니다. 다만 해외 평가 업체 환경에서 발생한 이번 같은 평가 사고를 국내에 언제 어떻게 알려야 하는지 정한 조항은 없습니다.

세 피해 회사가 공개되지 않아 국내 기업이 포함됐는지는 알려지지 않았어요.

그래도 두 건이 공개 저장소에 남은 자격 증명에서 시작됐다는 점은 국내 개발 조직에도 그대로 적용됩니다. AI 에이전트는 사람보다 빠르게 공개 저장소를 검색하고 비밀번호를 대입하기 때문에, 저장소의 비밀 값 스캔과 약한 비밀번호 차단이 우선적인 예방 조치입니다.

## 앞으로 주목할 점

- Google이 공식 블로그나 모델 카드로 모델 버전·조회 데이터를 밝힐지
- Irregular가 네 연구소 건을 묶은 경위 보고서를 공개할지
- 피해 회사 세 곳이 스스로 공개할지
- 연구소들이 외부 평가 업체 환경의 격리 검증을 계약 조건에 넣을지

## 참고 출처

- [[SecurityWeek] Google Confirms Gemini AI Breached Three Firms (Adkins 발언·당국 통보)](https://www.securityweek.com/google-confirms-gemini-ai-breached-three-firms/)
- [[Axios] Google Gemini accessed three companies during AI hacking test (2026.09.19)](https://www.axios.com/2026/09/19/google-safety-incidents-testing-hacks)
- [[MarkTechPost] Google Confirms Gemini Breached 3 Companies in AI Security Tests (2026.09.20, 연구소별 공개일)](https://www.marktechpost.com/2026/09/20/you-too-google-google-confirms-gemini-breached-3-companies-in-ai-security-tests/)
- [[ABC News] Gemini hacked three companies in first known breakout by Google's AI (2026.09.19)](https://www.abc.net.au/news/2026-09-19/gemini-google-ai-hacks-three-companies/107172128)
- [[CNBC] Google's Gemini becomes latest AI model to break out and hack computer systems (2026.09.18, Irregular 대변인 발언)](https://www.cnbc.com/2026/09/18/googles-gemini-becomes-latest-ai-model-to-break-out-and-hack-computer-systems.html)
- [[Anthropic] Investigating incidents in our cybersecurity evaluations (2026.07.30, 본문 이미지 1점 출처)](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)
- [[국가법령정보센터] 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543)
