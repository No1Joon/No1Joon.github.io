---
title: "LiteLLM MCP 인증 우회 실제 악용 — 1.84.0 미만은 지금 올려야"
description: "CISA KEV 에 오른 LiteLLM MCP 인증 우회 결함의 경위와 영향 버전, 사내 AI 게이트웨이 점검 순서를 정리합니다"
date: 2026-09-11
category: AI
subcategory: News
tags: [litellm, mcp, vulnerability, cisa-kev, ai-security]
image: /assets/og/2026-09-11-litellm-mcp-auth-bypass.png
---

사내 LLM 게이트웨이로 많이 쓰는 오픈소스 LiteLLM의 인증 우회 결함이 실제 공격에 쓰였습니다. 미국 CISA가 9월 2일 이 결함을 악용 확인 취약점 목록(KEV)에 올렸어요.

고친 버전은 이미 5월 14일에 나와 있었습니다. 넉 달 가까이 업데이트하지 않은 게이트웨이가 표적이 된 셈이고, LiteLLM이 올해 이 목록에 오른 건 두 번째입니다.

![LiteLLM 로고](/assets/images/ai/litellm-mcp-auth-bypass/01-hero-litellm-logo.webp)
*LiteLLM 로고 — 출처: BerriAI*

## 무슨 일이 있었나

CISA는 9월 2일 KEV(Known Exploited Vulnerabilities, 실제 악용이 확인된 취약점 목록)에 7건을 추가했습니다. 그중 LiteLLM·Starlette·Kestra 세 건이 AI 서비스를 받치는 인프라였어요.

- 대상은 **CVE-2026-59822**, LiteLLM의 MCP 인증 우회입니다
- 1.84.0 미만 전 버전이 해당하고, **1.84.0**에서 고쳐졌습니다
- 미국 연방기관의 조치 기한은 **9월 16일**입니다
- Wiz는 공개 하루 전인 7월 7일 자사 허니팟에서 악용을 관측했다고 밝혔습니다

심각도는 기관마다 조금 다릅니다. NVD는 CVSS 3.1 기준 8.2, GitHub 권고는 CVSS 4.0 기준 8.8로 매겼어요.

## 결함은 어디에 있었나

LiteLLM은 여러 회사의 LLM API를 OpenAI 형식 하나로 묶어 주는 프록시(AI 게이트웨이)입니다. 팀별 키 발급과 사용량·비용 관리를 한곳에서 하려고 씁니다.

문제는 MCP(Model Context Protocol, 모델이 외부 도구를 부르는 규약) 연결 부분이었습니다. LiteLLM은 MCP 요청의 키 검증이 실패하면 외부 MCP 서버용 OAuth2 인증으로 넘기는데, 이 대체 경로가 빈 인증 객체를 돌려주면서 요청을 인증된 것처럼 통과시켰어요.

그래서 아무 값이나 넣은 Bearer 토큰으로 MCP 세션을 열 수 있었습니다. 들어간 뒤에는 게이트웨이에 연결된 MCP 도구 목록을 보고 호출할 수 있어요.

![빈 인증으로 통과되는 게이트웨이 개념](/assets/images/ai/litellm-mcp-auth-bypass/02-agy.webp)
*빈 인증으로 통과되는 게이트웨이 개념 — 출처: 개념 컷 · agy 자가 생성*

피해 범위는 게이트웨이에 어떤 도구를 연결해 두었느냐가 정합니다.

| 운영 조건 | 이 결함의 위험 |
| :--- | :--- |
| 1.84.0 미만, MCP 도구 연결 | <mark>연결된 도구 호출 가능</mark> |
| 1.84.0 미만, MCP 미사용 | 부를 도구 없음, 다른 결함은 남음 |
| 사내망에만 둠 | 내부 침투 뒤 경로로 남음 |
| 1.84.0 이상 | **이 결함은 수정됨** |

Wiz 분석에 따르면 설정에 따라 데이터베이스 조회, GitHub 저장소, Jira·Slack, CI/CD 파이프라인까지 접근할 수 있고, 게이트웨이에 저장된 LLM 공급자 API 키가 함께 노출될 수 있습니다. 통과 엔드포인트 설정이 허술하면 클라우드 IAM 자격 증명까지 탈취될 수 있다고 봤어요.

국내에서도 KT가 1월 기술 블로그에서 LiteLLM을 자사 모델 오케스트레이터의 게이트웨이로 도입해 키 발급·팀별 사용량·비용 추적에 쓴다고 공개했고, AWS 한국 기술 블로그에도 서울 리전 사설 서브넷에 LiteLLM을 올린 구성 사례가 있어요. KISA의 국내 공지는 확인되지 않았습니다.

## LiteLLM만 올해 KEV에 두 번 올랐습니다

LiteLLM은 6월 8일에도 KEV에 올랐습니다. 그때 대상은 **CVE-2026-42271**, MCP 서버 설정을 저장 전에 미리 보는 엔드포인트 두 곳에서 명령을 주입할 수 있던 결함이에요.

원래는 API 키가 있어야 쓸 수 있는 곳이었지만, Horizon3는 6월 1일 LiteLLM이 쓰는 Python 웹 프레임워크 Starlette의 Host 헤더 검증 결함(**CVE-2026-48710**, 일명 BadHost)과 연계하면 키 없이도 원격 명령을 실행할 수 있다는 사실을 검증했습니다.

![LiteLLM 두 결함, 공개에서 KEV 등재까지](/assets/images/ai/litellm-mcp-auth-bypass/03-chart.webp)
*LiteLLM 두 결함, 공개에서 KEV 등재까지 — 출처: NVD·CISA KEV·LiteLLM 릴리스 노트·Wiz 기반 자가 렌더*

Wiz가 함께 짚은 올해 LiteLLM 결함은 넷입니다.

| CVE | 내용 | 수정 버전 |
| :--- | :--- | :--- |
| CVE-2026-59821 | 가드레일 코드 실행(인증 후) | 1.82.0 |
| CVE-2026-35029 | 설정 엔드포인트 권한 결함 | 1.83.0 |
| CVE-2026-42271 | MCP 미리보기 명령 주입 | 1.83.7 |
| CVE-2026-59822 | MCP 인증 우회 | **1.84.0** |

네 결함 가운데 둘이 MCP 연결 부분에서 나왔습니다. 1.84.0 이상이면 네 건이 모두 고쳐진 버전이에요.

### KEV에 함께 오른 AI 인프라 둘

| 제품 | 결함 | 수정 버전 |
| :--- | :--- | :--- |
| Starlette | Host 헤더 검증 우회 | **1.0.1** |
| Kestra OSS | 인증 없이 워크플로 실행 | 1.0.45·1.3.21 |

Starlette 결함은 CVSS 6.5지만 FastAPI처럼 Starlette 기반으로 만든 서비스 전반의 경로 기반 인증을 우회하게 합니다.

Kestra는 CVSS 10.0이고 연방기관 조치 기한이 9월 5일로 이미 지났어요.

## 지금 할 일

설치된 버전부터 확인합니다.

💻 [소스코드: 설치된 LiteLLM 버전 확인]

    pip show litellm

1.84.0 미만이면 올립니다. 1.84.0은 5월에 나온 버전이라, 이후 보안 수정까지 받으려면 최신 패치 버전으로 올리는 편이 낫습니다.

💻 [소스코드: LiteLLM 올리기]

    pip install --upgrade "litellm[proxy]"

1.84.0에는 호환성을 깨는 변경이 있어 올리기 전에 확인해야 합니다.

- 통과(pass-through) 엔드포인트가 기본으로 인증을 요구합니다. 인증 없이 열어 두려면 **auth: false**를 직접 적어야 해요
- 클라이언트가 **api_base**를 바꿔 다른 주소로 보내면 자격 증명이 빠집니다
- **mock_response** 같은 요청 제어 필드는 별도 허용 설정 없이는 막힙니다

![게이트웨이 운영자가 할 일](/assets/images/ai/litellm-mcp-auth-bypass/04-items.webp)
*게이트웨이 운영자가 할 일 — 출처: Wiz·Horizon3·LiteLLM 권고 기반 정리 · 자가 렌더*

게이트웨이를 거쳐 사내 도구를 쓰는 이용자가 따로 할 일은 없습니다. 조치는 전부 운영 쪽 몫이고, 확인 방법도 운영자가 가진 로그뿐이에요.

패치가 나온 뒤 KEV에 오르기까지 이번에는 석 달 반이 걸렸습니다. AI 게이트웨이를 직접 운영하는 팀이라면 LLM 앱과 같은 주기로 게이트웨이 버전도 점검해야 합니다.

## 참고 출처

- [[CISA] CISA Adds Seven Known Exploited Vulnerabilities to Catalog (2026-09-02 KEV 추가 7건)](https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog)
- [[NVD] CVE-2026-59822 (공개일·CVSS·KEV 등재일과 조치 기한)](https://nvd.nist.gov/vuln/detail/CVE-2026-59822)
- [[NVD] CVE-2026-42271 (6월 KEV 등재·영향 버전)](https://nvd.nist.gov/vuln/detail/CVE-2026-42271)
- [[GitLab Advisory] CVE-2026-59822 LiteLLM MCP Authentication Bypass (결함 원리·수정 버전)](https://advisories.gitlab.com/pypi/litellm/CVE-2026-59822/)
- [[Wiz] Breaking LiteLLM, From Authentication Bypass to Cloud Compromise (허니팟 관측·영향 범위·권고)](https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise)
- [[Horizon3.ai] CVE-2026-42271 chained with CVE-2026-48710 (Starlette 연쇄 검증)](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-42271-chained-with-cve-2026-48710/)
- [[LiteLLM] v1.84.0 Release Notes (배포일·호환성 변경)](https://docs.litellm.ai/release_notes/v1.84.0/v1-84-0)
- [[KT Enterprise] Multi LLM 운영을 위한 효율적인 LLM Gateway 적용 사례 (국내 도입)](https://enterprise.kt.com/bt/dxstory/3691.do)
- [[AWS 기술 블로그] 단일 LLM Gateway 아키텍처 (서울 리전 구성 사례)](https://aws.amazon.com/ko/blogs/tech/single-llm-gw-arch/)
