---
title: "Citrix NetScaler 제로데이 2건 — 업데이트해도 웹셸은 삭제되지 않습니다"
description: "공지 전부터 악용된 NetScaler 원격 코드 실행 취약점 두 건의 경과와, 업데이트 전에 침해 흔적부터 확인해야 하는 이유를 정리합니다"
date: 2026-10-02
category: Tech
subcategory: News
tags: [citrix, netscaler, zero-day, rce, webshell]
image: /assets/og/2026-10-02-citrix-netscaler-zero-day.png
---

Citrix가 2026년 9월 27일 NetScaler ADC와 NetScaler Gateway의 취약점 8건을 공지했습니다. 그중 **CVE-2026-88771**과 **CVE-2026-88772** 두 건은 공지가 발표되기 전부터 실제 공격에 악용된 **제로데이(zero-day, 패치가 나오기 전에 악용된 취약점)**였어요.

두 건 모두 로그인 없이 장비에서 명령을 실행하는 **RCE(원격 코드 실행)** 취약점입니다. 미국 CISA는 같은 날 두 건을 악용 확인 취약점 목록(KEV)에 등재하고 연방기관에 9월 30일까지 조치하라고 했고, KISA도 9월 29일 업데이트를 권고했어요.

업데이트만으로는 대응이 완료되지 않습니다. 이미 침입한 공격자가 설치한 웹셸은 업데이트해도 삭제되지 않아, 분석 기관들은 업데이트 전에 침해 흔적부터 확인하라고 안내하고 있어요.

![Citrix 로고](/assets/images/tech/citrix-netscaler-zero-day/01-hero-citrix-logo.webp)
*Citrix 로고 — 출처: Wikimedia Commons*

## 사건 경과

![NetScaler 제로데이 공격과 대응 경과](/assets/images/tech/citrix-netscaler-zero-day/02-chart.webp)
*NetScaler 제로데이 공격과 대응 경과 — 출처: Unit 42·GTIG·Rapid7·Citrix·CISA·KISA 발표 기반 자가 렌더*

Palo Alto Networks의 위협 분석 조직 Unit 42에 따르면 8월 21~22일부터 100곳 넘는 장비를 대상으로 버전을 식별하려는 시도가 있었습니다. Google Threat Intelligence Group(GTIG)과 Mandiant는 실제 공격이 적어도 9월 초부터 이어졌다고 9월 30일 공개한 분석에서 밝혔어요.

보안 기업 Rapid7은 9월 20일 고객 장비에서 장비 설정을 압축해 웹으로 내려받을 수 있는 경로에 저장하는 명령을, 9월 24일에는 웹셸 설치를 관측했습니다. Citrix 공지는 그 사흘 뒤인 9월 27일에 발표됐어요.

- 9월 27일: Citrix 보안 공지 CTX697096, CISA 경보와 KEV 등재
- 9월 29일: KISA 보호나라 「Citrix 제품 보안 업데이트 권고」
- 9월 30일: CISA가 연방기관에 준 조치 기한, GTIG 분석 공개
- 10월 1일: Unit 42 분석 갱신

## 영향받는 버전

Citrix 공지는 지원 중인 4개 계열을 영향 범위로 밝혔습니다. 각 계열의 해결 버전보다 낮으면 8건 모두에 해당해요.

| 버전 계열 | 영향받는 버전 | 해결 버전 |
| :--- | :--- | :--- |
| 14.1 | 14.1-73.37 미만 | **14.1-73.37 이상** |
| 13.1 | 13.1-64.23 미만 | **13.1-64.23 이상** |
| 14.1 FIPS | 14.1-73.37 FIPS 미만 | 14.1-73.37 FIPS 이상 |
| 13.1 FIPS·NDcPP | 13.1-37.279 미만 | 13.1-37.279 이상 |

NetScaler를 쓰는 Secure Private Access 하이브리드 구성도 해당합니다. Citrix가 직접 운영하는 클라우드 서비스와 Adaptive Authentication은 Citrix가 업데이트했고, 이 공지는 고객이 직접 운영하는 장비에만 적용돼요.

## 공격 전제조건

![Citrix 공지의 CVE별 전제조건](/assets/images/tech/citrix-netscaler-zero-day/03-citrix-bulletin.webp)
*Citrix 공지의 CVE별 전제조건 — 출처: Citrix (하이라이트 가공)*

두 제로데이는 전제조건이 다릅니다. CVE-2026-88771은 기본 구성 그대로인 모든 장비가 해당하고 켜야 하는 기능이 없어서, 해당 버전이면 인터넷에 열린 장비는 모두 노출된 것으로 봐야 해요.

CVE-2026-88772는 **DTLS(UDP 기반 TLS)**가 켜진 장비에 해당합니다. 조건이 붙어 있지만 VPN 가상 서버에서는 DTLS가 기본으로 켜져 있어서, SSL VPN으로 쓰는 NetScaler Gateway 대부분이 여기에 해당해요.

| CVE | 유형 | CVSS v4 |
| :--- | :--- | :--- |
| 88771 | 입력 검증 오류 RCE | <mark>9.5</mark> |
| 88772 | 메모리 오버플로 RCE | <mark>9.5</mark> |
| 88773 | HTTP 요청 밀반입 | 9.3 |
| 88774 | 정책 우회 | 7.0 |
| 88775~88777 | 메모리 오버플로 서비스 거부 | 8.8 |
| 88778 | TCP 순번 예측 | 8.8 |

실제 공격이 확인된 것은 88771과 88772 두 건이고, 나머지 6건은 공지 시점까지 악용 보고가 없었습니다. 88778은 업데이트가 아니라 Citrix 문서의 TCP 설정 변경으로 대응해요.

### DTLS 사용 여부 확인

![Citrix 공지가 제시한 DTLS 설정 줄](/assets/images/tech/citrix-netscaler-zero-day/04-term-dtls.webp)
*Citrix 공지가 제시한 DTLS 설정 줄 — 출처: Citrix 공지 CTX697096 기반 자가 렌더*

Citrix 공지는 설정 파일에서 DTLS를 명시적으로 끄지 않은 VPN 가상 서버를 해당으로 봅니다. DTLS를 꺼도 88772만 피할 수 있고, 전제조건이 없는 88771은 그대로 남아요.

## 공격에서 확인된 것

Rapid7이 9월 20일 관측한 명령은 장비 설정 전체를 압축해 웹 경로에 저장하는 것이었습니다. Rapid7은 이 압축 파일에 암호화된 비밀번호, SSL 인증서, SSH 키가 포함된다고 설명했고, 자사 고객 가운데 두 곳의 침해를 확인했어요.

GTIG는 처음 보고된 도구 두 가지를 공개했습니다.

[WHIPSHOT]
PHP 웹셸, HTTP 헤더에 Base64로 숨긴 명령을 실행하고 404 응답으로 위장

[SLAPSHOT]
파이썬 터널링 도구, WHIPSHOT의 명령을 받아 내부망으로 트래픽을 중계

공격자는 웹 서버 설정 파일 **httpd.conf**를 수정해 스크립트가 아닌 확장자의 파일도 PHP로 실행되게 했습니다. GTIG가 확인한 피해 업종은 정부, 금융, 기술, 교육, 법률·전문 서비스였고 지역은 북미와 유럽이었어요.

Unit 42는 9월 27일 기준 인터넷에 노출돼 취약할 수 있는 NetScaler가 5만 277대라고 집계했습니다. 공개된 분석에 국내 피해 언급은 없고, 국내 노출 대수도 발표되지 않았어요.

## 업데이트만으로 부족한 이유

CISA는 경보에서 업데이트 전에 침해 지표를 먼저 확인하고 포렌식 증거를 보존하라고 했습니다. 업데이트로 포렌식 가시성이 떨어질 수 있다는 이유예요.

Unit 42는 업데이트가 이미 침투한 공격자의 접근 권한을 없애지 않는다고 적었습니다. 업데이트는 취약점을 막을 뿐이고, 공격자가 수정한 **httpd.conf**나 설치한 웹셸 파일은 그대로 남기 때문이에요.

GTIG는 업데이트와 별도로 세션 종료와 자격증명 교체를 요구했습니다. 장비에 저장된 관리자 암호, SSH 키, LDAP 연동 계정, RADIUS 비밀값, TLS 인증서와 개인 키가 모두 대상이에요.

### 침해 흔적 점검

![NetScaler 셸에서 확인할 침해 흔적](/assets/images/tech/citrix-netscaler-zero-day/05-term-hunt.webp)
*NetScaler 셸에서 확인할 침해 흔적 — 출처: GTIG·Rapid7 분석 기반 자가 렌더*

GTIG와 Rapid7이 공개한 흔적 위치입니다. 하나라도 확인되면 업데이트로 끝내지 말고 장비를 신뢰할 수 있는 백업에서 다시 구축하라는 것이 분석 기관들의 공통 권고예요.

## 국내 권고

![KISA Citrix 제품 보안 업데이트 권고](/assets/images/tech/citrix-netscaler-zero-day/06-kisa-notice.webp)
*KISA Citrix 제품 보안 업데이트 권고 — 출처: KISA 보호나라*

KISA는 9월 29일 보호나라 보안공지에 8건 전체의 영향받는 버전과 해결 버전을 실었습니다. NetScaler Gateway는 재택근무용 SSL VPN과 Citrix 가상 데스크톱 접속 관문으로 쓰여, 국내 기업·기관도 이 장비를 인터넷에 노출해 운영하는 경우가 해당해요.

침해가 의심되면 KISA 인터넷침해대응센터에 신고할 수 있고, 전화는 국번 없이 118입니다.

🔗 링크 첨부 - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72201

## 운영자 조치

![운영자 조치 정리](/assets/images/tech/citrix-netscaler-zero-day/07-items.webp)
*운영자 조치 정리 — 출처: Citrix·CISA·GTIG 권고 정리 · 자가 렌더*

바로 업데이트할 수 없으면 GTIG는 운영상 가능한 범위에서 DTLS를 끄고, 경계 방화벽에서 UDP 443번 포트 유입을 차단하고, 접속 허용 IP를 제한하라고 했습니다. 이 조치들도 88772 위험만 줄이고 88771은 차단하지 못해요.

회사 VPN으로 NetScaler에 접속하는 직원이 직접 확인할 방법은 없습니다. 회사가 비밀번호 변경이나 재로그인을 요청하면 그 안내를 따르면 돼요.

## 앞으로 주목할 점

- Citrix 블로그의 침해 지표 갱신, 공지 변경 이력
- 국내 침해 사례와 KISA 추가 공지

## 참고 출처

- [[Citrix] CTX697096 NetScaler ADC·Gateway 보안 공지 (CVE 8건·전제조건·해결 버전, 본문 이미지 1점 출처)](https://support.citrix.com/external/article/697096)
- [[CISA] Critical Zero-Day Vulnerabilities Exploited in Citrix NetScaler ADC, Gateway (2026-09-27)](https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway)
- [[CISA] Known Exploited Vulnerabilities Catalog (등재일·조치 기한)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [[Google Threat Intelligence Group] Defending Against Active Exploitation of Citrix NetScaler ADC and Gateway Appliances (2026-09-30)](https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances)
- [[Unit 42] Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 (2026-10-01 갱신)](https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/)
- [[Rapid7] Zero-Day Exploitation of Citrix NetScaler ADC and Gateway (관측 경과·웹셸 경로)](https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772/)
