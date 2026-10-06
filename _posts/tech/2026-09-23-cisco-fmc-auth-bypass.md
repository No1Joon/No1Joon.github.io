---
title: "Cisco 방화벽 관리 서버 CVSS 10.0 취약점 — 실제 공격 확인"
description: "3월에 고친 Cisco FMC 인증 우회 결함이 9월에 다시 긴급해진 경위와, 확인된 공격 도구·수정 버전·점검할 로그를 정리합니다"
date: 2026-09-23
category: Tech
subcategory: News
tags: [cisco, firewall, vulnerability, authentication-bypass, ransomware]
image: /assets/og/2026-09-23-cisco-fmc-auth-bypass.png
---

Cisco가 2026년 9월 16일 방화벽 관리 서버 Secure Firewall Management Center(FMC)의 인증 우회 취약점 **CVE-2026-20079** 보안 권고를 갱신했습니다. 3월에 공개하고 고친 결함인데, 8월부터 실제 공격에 쓰인 사실이 확인되면서 긴급도가 다시 높아졌어요.

CVSS 점수는 만점인 10.0이고, 인증 없이 조작된 HTTP 요청만으로 서버의 root 권한까지 얻을 수 있습니다. Cisco는 우회책이 없다고 밝혔고, 수정 릴리스로 업데이트하는 것이 유일한 해결책이에요.

![Cisco 로고](/assets/images/tech/cisco-fmc-auth-bypass/01-logo-cisco.webp)
*Cisco 로고 — 출처: Cisco*

## 사건 경과

![CVE-2026-20079 공개부터 실제 악용 확인까지 경과](/assets/images/tech/cisco-fmc-auth-bypass/02-chart.webp)
*CVE-2026-20079 공개부터 실제 악용 확인까지 경과 — 출처: Cisco·Cisco Talos·CISA 발표 기반 자가 렌더*

Cisco는 3월 4일 자체 보안 시험에서 찾은 이 결함을 공개하면서 당시에는 악용 사례가 없다고 밝혔습니다. BleepingComputer에 따르면 7월 29일 권고를 갱신하며 침해 지표를 더했고, 그 지표에 해당하는 로그의 첫 기록은 7월 23일이었어요.

Cisco 보안사고대응팀(PSIRT)은 8월에 실제 악용을 인지했고, 9월 9일 이를 공식 확인했습니다. 같은 날 미국 사이버보안·인프라보안청(CISA)은 이 결함을 실제 악용 취약점 목록(KEV)에 올리고, 연방 민간기관에 9월 12일까지 조치하라고 지시했어요.

9월 16일 갱신한 권고 v2.6은 그동안 배포한 임시 핫픽스를 보안 강화 릴리스로 대체했습니다. 이 릴리스에는 Cisco가 내부에서 찾은 다른 취약점 수정도 함께 포함돼 있어요.

## 공격 전제와 범위

FMC는 여러 대의 Cisco 방화벽 정책과 설정을 한곳에서 관리하는 서버입니다. 공격이 성립하려면 공격자가 **FMC의 웹 관리 인터페이스에 네트워크로 접근할 수 있어야** 하고, 계정이나 사용자 조작은 필요 없어요. Cisco는 관리 인터페이스가 인터넷에 열려 있지 않으면 공격 표면이 줄어든다고 적었습니다.

결함은 부팅할 때 잘못 만들어지는 시스템 프로세스에서 비롯되고, 공격자는 이를 이용해 서버에서 스크립트를 root 권한으로 실행할 수 있습니다.

| 구분 | 제품 |
| :--- | :--- |
| **영향 있음** | Secure FMC 소프트웨어 전 구성 |
| 영향 있음·자동 수정 | Security Cloud Control 방화벽 관리 |
| 영향 없음 | Secure Firewall Threat Defense(FTD) |
| 영향 없음 | Secure Firewall ASA |
| 영향 없음 | Firewall Device Manager(FDM) |

방화벽 장비 자체의 FTD·ASA 소프트웨어는 영향을 받지 않아요. 다만 관리 서버가 침해되면 그 서버가 관리하는 방화벽 설정을 공격자가 볼 수 있다는 점이 이번 사고에서 확인됐습니다.

인터넷에 노출된 FMC 수는 검색 엔진마다 다르게 집계됩니다. 보안 매체 보도에 따르면 Censys는 약 300대, FOFA는 600~700대를 찾았고, 국가별 수치는 공개되지 않았어요.

## 확인된 침입 사례

![방화벽 관리 서버 침입 경로 개념 컷](/assets/images/tech/cisco-fmc-auth-bypass/03-agy.webp)
*방화벽 관리 서버 침입 경로 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

Cisco Talos는 9월 9일 FMC를 노린 침입 활동을 세 묶음으로 나눠 공개했습니다.

| 묶음 | 쓴 취약점 | 결과 |
| :--- | :--- | :--- |
| UAT-12197 | 20079 | 웹 셸·계정정보 탈취 |
| UAT-11823 | 20079·20316 | <mark>Cyclops Blink 설치</mark> |
| UAT-11988 | 20316 | Qilin 랜섬웨어 배포 |

UAT-11823은 침해 흔적 파일인 license.tmp를 악성 파일로 바꿔 원격 셸을 열고, 관리 대상 방화벽의 설정을 수집한 뒤 악성코드 Cyclops Blink의 변종을 설치했어요. Cyclops Blink는 러시아 정부 연계 해킹 조직 Sandworm의 도구로 알려져 있고, Talos는 이 묶음을 국가 연계 조직으로 높은 확신을 갖고 분류했습니다.

함께 쓰인 **CVE-2026-20316**은 저권한 계정에 고정된 비밀번호가 설정돼 있던 결함으로, 7월 29일 공개됐고 CVSS 점수는 5.3이에요. 점수는 낮지만 다른 결함과 함께 악용되면 권한 상승에 이용될 수 있다고 Talos는 설명했습니다.

Cisco는 공격 조직의 표적 업종·국가와 침해된 장비 수를 공개하지 않았어요.

## 국내 접점

Qilin은 2025년 9~10월 국내 IT 관리업체 한 곳을 거쳐 자산운용사 등 금융 조직 28곳의 자료를 탈취한 **Korean Leaks** 사건을 벌인 랜섬웨어 조직입니다. Bitdefender 분석으로 당시 유출 규모는 파일 100만 개 이상, 2TB였어요.

한국인터넷진흥원(KISA)은 9월 17일 추석 연휴를 앞두고 기업 보안점검 권고를 발표했습니다. 외부에 노출된 서비스의 버전 확인과 보안 업데이트, 관리자 계정의 다중 인증(MFA) 적용, 랜섬웨어 대비 백업 분리를 점검 항목으로 꼽았어요. 노출된 관리 서버, 고정 비밀번호 계정, 랜섬웨어 배포로 이어진 FMC 사고가 이 세 항목과 겹쳐요.

국내에서 FMC를 쓰는 조직 수나 피해 사례는 공개된 자료로 확인되지 않아요.

## 수정 버전

Cisco가 9월 16일 공지한 릴리스별 첫 수정 버전은 다음과 같습니다.

| 릴리스 계열 | 첫 수정 버전 |
| :--- | :--- |
| 7.0 이하 | 7.0.10 |
| 7.2 | 7.2.12 |
| 7.4 | 7.4.8 |
| 7.6 | 7.6.6 |
| 7.7 | 7.7.13 |
| 10.0 | **10.0.2** |
| 10.1 | 10.1.0 |

클라우드로 제공하는 Security Cloud Control 방화벽 관리는 Cisco가 이미 수정을 마쳐 사용자 조치가 필요 없어요.

## 운영자 조치

![한국인터넷진흥원 로고](/assets/images/tech/cisco-fmc-auth-bypass/04-logo-kisa.webp)
*한국인터넷진흥원 로고 — 출처: KISA*

[버전 업데이트]
해당 릴리스의 첫 수정 버전 이상으로 업데이트합니다. 임시 핫픽스만 적용했다면 보안 강화 릴리스로 다시 업데이트해야 해요.

[노출 차단]
업데이트 전까지 FMC 관리 인터페이스의 인터넷 접근을 차단하고, 접근 허용 대상을 관리자 망으로 제한합니다.

[침해 점검]
Cisco 권고는 expert 모드에서 시스템 로그를 검색해 **/var/tmp/license.tmp** 흔적이 확인되면 침해로 의심하라고 안내합니다. 흔적이 확인되면 Cisco TAC(기술지원센터)에 연락해요.

[이미 침해됐다면]
Cisco는 핫픽스가 앞으로의 악용을 차단할 뿐 기존 침해를 없애지는 않는다고 밝혔습니다. 관리 대상 방화벽의 계정과 설정도 함께 점검합니다.

[탐지 규칙]
Snort 규칙 66075~66080·66883·66960~66961을 적용합니다.

침해 신고와 상담은 KISA 118에서 받습니다.

🔗 링크 첨부 - https://www.boho.or.kr/

## 정리

![시스코 FMC 취약점 정리 카드](/assets/images/tech/cisco-fmc-auth-bypass/05-items.webp)
*시스코 FMC 취약점 정리 카드 — 출처: Cisco 보안 권고 기반 자가 렌더*

## 앞으로 주목할 점

- 피해 규모: Cisco가 공개하지 않은 침해 장비 수와 표적 업종
- 추가 결함: 보안 강화 릴리스에 함께 포함된 내부 발견 취약점의 개별 공개
- 국내 권고: KISA 보호나라의 FMC 관련 별도 권고 여부
- 공격 확산: 노출 FMC를 노리는 스캔과 다른 조직의 악용 보고

## 참고 출처

- [[Cisco] Secure FMC 인증 우회 취약점 보안 권고 v2.6 (2026-09-16 갱신)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2)
- [[Cisco Talos] FMC 취약점 실제 악용과 침입 묶음 세 개 (2026-09-09)](https://blog.talosintelligence.com/fmc-ongoing-exploitation/)
- [[BleepingComputer] 악용 확인과 경과 (2026-09)](https://www.bleepingcomputer.com/news/security/cisco-confirms-cve-2026-20079-secure-fmc-flaw-exploited-in-attacks/)
- [[Help Net Security] 20079·20316 악용과 조직별 행위 (2026-09-10)](https://www.helpnetsecurity.com/2026/09/10/cisco-fmc-exploited-cve-2026-20079-cve-2026-20316/)
- [[The Hacker News] CISA KEV 등재와 9월 12일 기한 (2026-09)](https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html)
- [[KISA 보호나라] 추석 명절 대비 기업 보안점검·모니터링 강화 (2026-09-17)](https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72189&menuNo=205020)
- [[Bitdefender] Korean Leaks와 Qilin 분석 (2025)](https://www.bitdefender.com/en-us/blog/businessinsights/korean-leaks-campaign-targets-south-korean-financial-services-qilin-ransomware)
