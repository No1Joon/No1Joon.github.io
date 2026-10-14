---
title: "Citrix NetScaler 세 번째 제로데이 — 9월에 업데이트한 장비도 해당"
description: "SAML 로그인을 쓰는 NetScaler 장비를 노리는 CVE-2026-88779 의 영향 범위와 수정 빌드, 점검 순서를 정리합니다"
date: 2026-10-07
category: Tech
subcategory: News
tags: [citrix, netscaler, zero-day, saml, vulnerability]
image: /assets/og/2026-10-07-citrix-netscaler-saml-zero-day.png
---

Citrix가 NetScaler ADC와 NetScaler Gateway의 새 제로데이 **CVE-2026-88779**를 10월 3일(현지 시각) 공지했습니다. 9월 27일 CVE-2026-88771 등 8건을 수정한 지 6일 만이고, 이번에도 공지 전에 공격이 먼저 확인됐어요.

SAML 로그인을 쓰도록 구성한 장비가 대상이며, 로그인 없이 보낸 트래픽으로 인증 기능을 멈추게 할 수 있습니다. 9월에 업데이트한 빌드(14.1-73.37·13.1-64.23)도 해당하니 **14.1-73.41·13.1-64.28 이상으로 한 번 더** 업데이트해야 해요.

[Citrix NetScaler 제로데이 2건 — 업데이트해도 웹셸은 삭제되지 않습니다](/posts/citrix-netscaler-zero-day/)

![Citrix 로고](/assets/images/tech/citrix-netscaler-saml-zero-day/01-hero-citrix-logo.webp)
*Citrix 로고*

## 사건 경과

![NetScaler 취약점 공지와 대응 경과](/assets/images/tech/citrix-netscaler-saml-zero-day/02-chart.webp)
*NetScaler 취약점 공지와 대응 경과 — 출처: Citrix·CISA·KISA·NVD 발표 기반 자가 렌더*

Citrix는 보안 공지 **CTX697174**에서 CVE-2026-88779를 메모리 오버플로 취약점으로 설명하고, 패치하지 않은 장비를 노린 표적 공격을 확인했으며 서비스 거부로 이어질 수 있다고 밝혔습니다. 심각도는 CVSS v4 기준 **8.7점**(높음)이에요.

미국 CISA는 다음 날인 10월 4일 이 취약점을 악용 확인 취약점 목록(KEV)에 등재하고, 연방 민간기관에 **10월 7일**까지 조치하라고 했습니다. 9월의 두 건(CVE-2026-88771·88772)에 이어 같은 장비의 취약점이 열흘 안에 세 번째로 KEV에 등재됐어요.

- 10월 3일(현지 시각): Citrix 보안 공지 CTX697174
- 10월 4일: CISA KEV 등재, NVD 등록
- 10월 5일: 캐나다 사이버보안센터 권고 AV26-996
- 10월 6일: KISA 보호나라 「Citrix 제품 보안 업데이트 권고」

## 공격 전제조건

![NetScaler SAML 구성 확인 명령](/assets/images/tech/citrix-netscaler-saml-zero-day/03-term-saml.webp)
*NetScaler SAML 구성 확인 명령 — 출처: Citrix 공지 CTX697174 기반 자가 렌더*

이번 취약점은 장비가 **SAML SP(서비스 제공자) 또는 SAML IdP(신원 제공자)**로 구성돼 있을 때만 성립합니다. SAML은 회사 계정 하나로 여러 서비스에 로그인하게 해 주는 싱글 사인온(SSO) 표준인데, Gateway를 Microsoft Entra ID나 Okta 같은 사내 로그인과 연동해 쓰는 곳이 여기에 해당해요.

반대로 SAML을 쓰지 않는 장비는 이번 건의 대상이 아니에요. 전제가 붙는다는 점이 9월의 CVE-2026-88771과 다릅니다.

| 취약점 | 성립 조건 | 공격 결과 |
| :--- | :--- | :--- |
| CVE-2026-88771 | 기본 구성 전체 | 원격 코드 실행 |
| CVE-2026-88772 | DTLS 켠 Gateway | 원격 코드 실행 |
| CVE-2026-88779 | <mark>SAML SP·IdP 구성</mark> | 서비스 거부 |

설정 파일에 **add authentication samlAction** 줄이 있으면 SP, **add authentication samlIdPProfile** 줄이 있으면 IdP로 쓰는 장비예요. 둘 다 없으면 이번 취약점의 전제를 충족하지 않지만, 9월 취약점 때문에라도 업데이트는 필요합니다.

## 9월 업데이트로 막히지 않는 이유

CVE-2026-88779는 9월에 수정한 8건과 별개의 결함이라, 9월 27일 빌드는 이 취약점을 수정하지 않았습니다. NVD와 KISA가 적은 영향받는 버전 기준선이 9월 해결 버전보다 한 단계 위에 있어요.

| 브랜치 | 9월 해결 버전 | 10월 해결 버전 |
| :--- | :--- | :--- |
| 14.1 | 14.1-73.37 | **14.1-73.41** |
| 13.1 | 13.1-64.23 | **13.1-64.28** |
| 14.1 FIPS | 14.1-73.37 FIPS | **14.1-73.41 FIPS** |
| 13.1 FIPS·NDcPP | 13.1-37.279 | **13.1-37.282** |

9월에 서둘러 업데이트한 운영자도 SAML을 쓴다면 한 달이 안 돼 정비 일정을 다시 확보해야 합니다. 이중화(HA) 쌍으로 운영하면 두 노드 모두 업데이트해야 하고, 고객이 직접 관리하는 장비가 대상이에요.

## 공격에서 확인된 것

Citrix가 공식으로 밝힌 영향은 **서비스 거부**까지예요. 메모리 오버플로를 일으키는 트래픽을 보내면 인증을 처리하는 프로세스가 중단되거나 장비가 다시 시작돼, 그동안 VPN 접속과 SSO 로그인을 쓸 수 없습니다.

BleepingComputer는 10월 3일부터 장비가 원인 모르게 재부팅된다는 보고가 있었고, 일부 연구자가 셸 명령이 들어간 사용자 이름으로 인증을 시도한 흔적과 외부 서버에서 파일을 다운로드한 기록을 확인했다고 전했습니다. 이 관측이 코드 실행으로 이어졌는지는 Citrix가 확인하지 않았어요.

2025년 CVE-2025-6543도 처음엔 서비스 거부로 공지됐다가 이후 원격 코드 실행에 악용된 사실이 확인된 전례가 있습니다. 그래서 보안 업체들은 재부팅 기록이 있는 장비를 단순 장애로 처리하지 말고 침해 여부를 함께 확인하라고 권하고 있어요.

호주 사이버보안센터(ACSC)도 자국 조직의 피해 보고를 받았다며 경보를 냈다고 보안 매체들이 전했습니다. 영향받은 조직 수나 국내 피해 사례는 공개되지 않았어요.

## 국내 권고

![KISA Citrix 제품 보안 업데이트 권고 2026-10-06](/assets/images/tech/citrix-netscaler-saml-zero-day/04-kisa-notice.webp)
*KISA Citrix 제품 보안 업데이트 권고 2026-10-06 — 출처: KISA*

KISA는 10월 6일 보호나라 보안공지에 CVE-2026-88779의 영향받는 버전과 해결 버전 6줄을 게시했습니다. 9월 29일 공지에 이은 두 번째 Citrix 권고예요.

NetScaler Gateway는 재택근무용 SSL VPN과 Citrix 가상 데스크톱 접속 관문으로 쓰여, 국내 기업·기관 가운데 이 장비를 SAML 로그인과 연동해 인터넷에 노출한 곳이 해당합니다. 국내 노출 대수는 발표되지 않았어요.

침해가 의심되면 KISA 인터넷침해대응센터에 신고할 수 있고, 전화는 국번 없이 **118**입니다.

🔗 링크 첨부 - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72209

## 운영자 조치

![운영자 조치 정리](/assets/images/tech/citrix-netscaler-saml-zero-day/05-items.webp)
*운영자 조치 정리 — 출처: Citrix·KISA 공지 기반 자가 렌더*

개인 사용자가 직접 할 일은 없습니다. 회사 VPN이 10월 초 갑자기 중단됐다면 장비 문제일 수 있으니 사내 IT 부서에 알리면 돼요.

운영자는 업데이트 전에 ns.log와 코어 덤프를 먼저 보존하는 순서가 중요합니다. 업데이트하면 재부팅으로 메모리에 남은 흔적이 소실되고, 크래시 기록은 공격이었는지 판단할 근거가 돼요. 9월 취약점(CVE-2026-88771·88772)의 침해 흔적 점검은 이번 업데이트와 별개로 계속 필요합니다.

## 앞으로 주목할 점

- Citrix가 서비스 거부 외의 영향(코드 실행)을 공지에 추가하는지
- CISA 조치 기한(10월 7일) 이후 공개될 악용 분석
- KISA 추가 공지와 국내 피해 사례 발표
- 같은 SAML 처리 코드에서 추가 취약점이 나오는지

## 참고 출처

- [[Citrix] CTX697174 NetScaler ADC·Gateway 보안 공지 (CVE-2026-88779·해결 버전)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174)
- [[CISA] Known Exploited Vulnerabilities Catalog, CVE-2026-88779 (2026-10-04 등재·10-07 기한)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [[NVD] CVE-2026-88779 상세 (영향받는 버전)](https://nvd.nist.gov/vuln/detail/CVE-2026-88779)
- [[KISA 보호나라] Citrix 제품 보안 업데이트 권고 (2026-10-06, 본문 이미지 1점 출처)](https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72209)
- [[Canadian Centre for Cyber Security] Citrix security advisory AV26-996 (2026-10-05)](https://cyber.gc.ca/en/alerts-advisories/citrix-security-advisory-av26-996)
- [[BleepingComputer] Citrix patches NetScaler SAML zero-day exploited in attacks (재부팅 보고·연구자 관측)](https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/)
- [[Tenable] Citrix NetScaler 제로데이 FAQ (9월·10월 해결 버전 비교)](https://www.tenable.com/blog/frequently-asked-questions-about-reported-citrix-netscaler-zero-day-vulnerabilities)
