---
title: "PoeLLM 봇넷 — 노출된 AI 서버 3,400대를 채굴에 악용"
description: "LiteLLM·Ollama 등 노출 서버를 감염시킨 PoeLLM 봇넷의 경과와 명령 서버 은닉 방식, 서버 운영자 점검 항목을 정리합니다"
date: 2026-10-13
category: Tech
subcategory: News
tags: [botnet, cryptomining, ollama, litellm, ai-security]
image: /assets/og/2026-10-13-poellm-botnet.png
---

인터넷에 그대로 노출돼 있던 AI 서버 3,400대 이상이 암호화폐 채굴 봇넷 PoeLLM에 감염됐어요. 미국 통신사 Lumen의 보안 연구조직 Black Lotus Labs가 10월 초 공개한 분석입니다.

감염 대상은 LiteLLM·Ollama처럼 개인과 연구실이 직접 실행해 사용하는 LLM 서버, 그리고 Gotenberg·Gitea 같은 개발 도구였어요. 명령 서버 주소는 GitHub에 게시한 시 한 편 속 단어 네 개에 숨겨 두었습니다.

![Lumen Black Lotus Labs의 PoeLLM 보고서 대표 이미지](/assets/images/tech/poellm-botnet/01-hero-lumen.webp)
*Lumen Black Lotus Labs의 PoeLLM 보고서 대표 이미지 — 출처: Lumen Black Lotus Labs*

## 사건 경과

Black Lotus Labs는 이 캠페인을 Canto Incognito, 악성코드를 PoeLLM이라고 명명했어요. 시를 GitHub에 처음 커밋한 날이 2026년 4월 13일이고, 5월부터 대규모 스캔과 공격이 시작됐습니다. 연구팀은 6월 초 Ivanti Sentry 침해 사고를 조사하다 이 인프라를 처음 발견했어요.

![2026년 5월~10월 일별 활성 PoeLLM 감염 서버 수 그래프](/assets/images/tech/poellm-botnet/02-capture.webp)
*2026년 5월~10월 일별 활성 PoeLLM 감염 서버 수 그래프 — 출처: Lumen Black Lotus Labs*

- 누적 감염 서버: 3,400대 이상 (보고서 요약 기준)
- 하루 최대 활성 감염: 약 800대 (6월 중순)
- 사용한 명령 서버(C2): 최소 12곳, 10월 기준 3곳 활성
- 피해 지역: 미국과 서유럽에 집중

BleepingComputer는 처음 2,100대로 보도했다가 연구팀이 실시간 보고서를 수정한 뒤 3,400대로 정정했고, 보고서 본문에는 약 2,200대라는 표현도 남아 있어요. 보고서는 3,400대를 요약 수치로 제시했지만 두 숫자의 차이는 설명하지 않았습니다. 일별 그래프의 수치는 10월 초에 다시 증가하고 있어 감염이 끝난 상태가 아닙니다.

## 감염 경로와 공격 대상 소프트웨어

PoeLLM은 인터넷 전체를 대상으로 3000번과 4000번 포트를 스캔해요. 3000번은 PDF 변환기 Gotenberg, 4000번은 여러 LLM API를 단일 주소로 통합하는 프록시 LiteLLM이 기본으로 쓰는 포트입니다.

![Canto Incognito 캠페인 구조도](/assets/images/tech/poellm-botnet/03-capture.webp)
*Canto Incognito 캠페인 구조도 — 출처: Lumen Black Lotus Labs*

LiteLLM 쪽 공격에 쓰인 취약점은 **CVE-2026-42271**이에요. MCP 서버를 저장하기 전에 연결을 시험하는 엔드포인트(**/mcp-rest/test/connection**)가 요청에 담긴 명령을 서버에서 그대로 실행하는 결함으로, 1.74.2부터 1.83.6까지가 영향을 받고 2026년 5월 8일 배포된 1.83.7에서 수정됐습니다. 원래는 API 키가 있어야 쓸 수 있는 엔드포인트였지만, 보안업체 Horizon3.ai는 Starlette의 Host 헤더 검증 우회(**CVE-2026-48710**)와 결합해 악용하면 인증 없이 원격 코드 실행(RCE)이 된다고 확인했어요. 미국 CISA는 6월 9일 이 취약점을 실제 악용 목록(KEV)에 등재했습니다.

| 대상 | 기본 포트 | 보고서가 밝힌 경로 |
| :--- | :--- | :--- |
| LiteLLM | 4000 | <mark>CVE-2026-42271</mark> |
| Gotenberg | 3000 | 외부 노출 악용 |
| Ollama | 11434 | **경로 미공개** |
| Gitea | 3000 | 경로 미공개 |

감염되면 **libgcrypt**라는 이름의 리눅스 실행 파일이 설치되고, 이 파일이 원격 셸, 채굴기 XMRig·Iron, 스캐너, 공격 코드를 모두 포함해요. 채굴 수익은 러시아 채굴 서비스 Kryptex로 지급됩니다. 감염된 서버는 다시 3000·4000번 포트를 스캔해 다음 공격 대상 서버를 탐색하는 수단이 되고, 일부는 SSH 로그인 무차별 대입 실험에도 쓰였어요.

## 시 속에 숨긴 명령 서버 주소

감염 서버는 명령 서버 주소를 코드에 하드코딩하지 않고 매번 GitHub에서 조회해요. Node.js 공식 사이트 저장소를 포크한 계정의 **dash.css** 파일 안에 *On the Nature of Connection*이라는 시가 포함돼 있습니다.

![C2 주소를 숨긴 시 On the Nature of Connection (2026년 9월 기준)](/assets/images/tech/poellm-botnet/04-capture.webp)
*C2 주소를 숨긴 시 On the Nature of Connection (2026년 9월 기준) — 출처: Lumen Black Lotus Labs*

악성코드는 시의 정해진 자리에서 단어 네 개를 추출해 내장 사전으로 숫자로 변환하고, 그 네 숫자를 IPv4 주소로 씁니다. 보고서 예시로는 driver가 92, diode가 119가 되는 식이에요. 운영자는 서버를 변경할 때 악성코드를 재배포하지 않고 시의 단어만 수정하면 되고, 시는 지금까지 11번 수정됐습니다.

감염 서버가 접속하는 곳이 평범한 GitHub 파일이라 차단 목록으로 탐지되지 않고, 명령 서버 IP가 변경돼도 악성코드 표본은 그대로입니다. 연구팀은 C2 서버 여러 대가 관리 화면이 노출된 공유기였던 점을 근거로, 운영자가 해킹한 공유기를 명령 서버로 재활용한 것으로 봤어요.

운영자는 확정되지 않았습니다. 코드 주석이 이탈리아어이고 관리 서버가 이탈리아에 있어 연구팀은 이탈리아어를 쓰는 금전 목적 집단으로 보되, 확신도는 중간이라고 밝혔어요.

## 국내 노출 현황

Black Lotus Labs 보고서에는 한국 피해가 별도로 언급되지 않아요.

![인증 없이 노출된 Ollama 서버 상위 6개국 막대](/assets/images/tech/poellm-botnet/05-chart-ollama.webp)
*인증 없이 노출된 Ollama 서버 상위 6개국 막대 — 출처: LeakIX 스캔 자료 기반 자가 렌더*

보안 검색엔진 LeakIX가 2026년 2월 인터넷을 스캔했을 때 인증 없이 외부에 노출된 Ollama 서버는 12,269대였고, 그중 한국이 453대로 다섯 번째였어요. 이 수치는 PoeLLM 감염 수가 아니라 누구나 접속할 수 있는 상태로 노출된 서버 수입니다.

Ollama는 기본값으로는 자기 컴퓨터(127.0.0.1)에서만 접속을 받지만, 다른 기기에서 접근하려고 **OLLAMA_HOST=0.0.0.0**으로 바꾸는 순간 인증 없이 외부에 노출돼요. 그 상태에서는 제3자가 모델 목록을 조회하고, 서버 GPU에서 추론을 실행하고, 모델 파일을 반출할 수 있습니다. PoeLLM이 Ollama를 어떤 방식으로 감염시켰는지는 보고서가 밝히지 않았어요.

[맥북에서 Gemma 4 돌려봤습니다 — 크기별 속도와 함정 하나](/posts/gemma-4-macbook-local/)

## 점검과 조치

감염 여부를 개인이 확실히 판별할 공개 검사 도구는 없어요.

![PoeLLM 대응 점검·조치 정리 카드](/assets/images/tech/poellm-botnet/06-items.webp)
*PoeLLM 대응 점검·조치 정리 카드 — 출처: Lumen Black Lotus Labs · LeakIX 권고 기반 자가 렌더*

채굴 악성코드는 CPU·GPU 사용률이 이유 없이 높게 유지되는 것으로 드러나는 경우가 많아요. 서버 사용률이 평소와 다르면 **libgcrypt** 라는 이름의 낯선 프로세스와 외부 3778·5001·5002·9999번 포트로 나가는 연결이 있는지 확인합니다. 감염이 의심되면 프록시에 저장된 API 키부터 변경하고, KISA 118로 신고할 수 있어요.

🔗 링크 첨부 - https://github.com/blacklotuslabs/IOCs

## 참고 출처

- [[Lumen Black Lotus Labs] Canto Incognito: Tracking the PoeLLM Malware (1차 보고서, 본문 이미지 4점 출처)](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)
- [[BleepingComputer] PoeLLM malware infects exposed AI servers in cryptomining attacks (2026-10-07, 감염 수 정정)](https://www.bleepingcomputer.com/news/security/poellm-malware-infects-exposed-ai-servers-in-cryptomining-attacks/)
- [[보안뉴스] PoeLLM 봇넷 보도 (2026-10-08)](https://www.boannews.com/news/articleView.html?idxno=146255)
- [[Horizon3.ai] CVE-2026-42271 chained with CVE-2026-48710 (인증 우회 연쇄)](https://www.horizon3.ai/cve-2026-42271-chained-with-cve-2026-48710)
- [[GitLab Advisory Database] CVE-2026-42271 영향 버전·수정 버전](https://advisories.gitlab.com/pypi/litellm/CVE-2026-42271/)
- [[Help Net Security] CISA KEV 등재 (2026-06)](https://www.helpnetsecurity.com/?p=373845)
- [[LeakIX] 12,000 Ollama Instances Exposed (2026-02-23, 국가별 노출 수)](https://blog.leakix.net/2026/02/ollama-exposed/)
