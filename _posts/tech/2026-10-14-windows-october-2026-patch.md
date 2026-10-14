---
title: "Windows 10월 보안 업데이트 1,413건 — 24H2 는 지원 종료"
description: "역대 최대 규모인 10월 정기 업데이트의 제로데이와 Windows 11 24H2 Home·Pro 지원 종료 대응을 정리합니다"
date: 2026-10-14
category: Tech
subcategory: News
tags: [windows, patch-tuesday, zero-day, microsoft, windows-11]
image: /assets/og/2026-10-14-windows-october-2026-patch.png
---

Microsoft가 2026년 10월 13일(미국 시간) 정기 보안 업데이트로 자사 취약점 **1,413건**을 수정했습니다. 9월 999건에 이어 다시 최대치이고, 6월 220건과 비교하면 넉 달 만에 6배로 증가했어요. 이 가운데 1건은 이미 실제 공격에 악용되고 있던 제로데이(zero-day, 공개·패치 전에 악용되는 취약점)입니다.

같은 날 Windows 11 24H2 Home·Pro 버전의 지원도 종료됐습니다. 10월 업데이트가 24H2에 나오는 마지막 정기 보안 업데이트라, 이 버전을 쓰는 PC는 25H2 이상으로 업그레이드해야 11월부터 보안 패치를 받아요.

![Microsoft Security Update Guide 2026년 10월 릴리스 노트](/assets/images/tech/windows-october-2026-patch/01-capture-msrc.webp)
*Microsoft Security Update Guide 2026년 10월 릴리스 노트 — 출처: Microsoft*

## 실제 악용된 제로데이 CVE-2026-96951

Microsoft가 악용을 확인한 취약점은 **CVE-2026-96951**(Windows Shell 보안 기능 우회, CVSS 8.8)입니다. 공격자는 이 취약점으로 MotW(Mark of the Web) 방어를 우회할 수 있어요.

MotW는 인터넷에서 받은 파일에 Windows가 붙이는 표시입니다. 이 표시가 있으면 파일을 열 때 SmartScreen 경고나 Office의 제한된 보기가 먼저 표시되는데, 우회되면 이 경고 없이 파일이 열려요.

공격이 성립하려면 사용자가 직접 행동해야 합니다. Microsoft 설명에 따르면 공격자는 조작한 파일을 이메일·메신저로 보내거나 링크로 유도해야 하고, 사용자가 그 파일을 열지 않으면 공격을 강제할 방법이 없어요. 누가 어떤 공격에 썼는지는 공개되지 않았습니다.

| 구분 | CVE | 내용 |
| :--- | :--- | :--- |
| 악용 확인 | <mark>CVE-2026-96951</mark> | Windows Shell MotW 우회 |
| 사전 공개 | CVE-2026-108398 | .NET Framework WDAC 우회 |
| 사전 공개 | CVE-2026-92707 | MessagePack-CSharp 서비스 거부 |

CVE-2026-108398은 Google Project Zero의 James Forshaw가 보고했고, 이미 시스템에 접근한 공격자가 기업용 애플리케이션 실행 통제(WDAC)를 우회할 수 있는 취약점이에요. 두 취약점 모두 사전 공개됐지만 악용은 확인되지 않았습니다.

## 1,413건의 구성

![2026년 10월 Microsoft CVE 영향 유형별 건수 차트](/assets/images/tech/windows-october-2026-patch/02-chart.webp)
*2026년 10월 Microsoft CVE 영향 유형별 건수 차트 — 출처: Microsoft Security Update Guide 기반 자가 렌더*

절반에 가까운 677건이 권한 상승입니다. 이미 PC에 들어온 공격자나 악성코드가 관리자 권한을 얻는 데 쓰이는 유형이라, 첫 침투에 쓰이는 원격 코드 실행(316건)과 결합돼 다단계 공격에 악용돼요.

| 제품군 | 취약점 (건) | 업데이트 수 |
| :--- | :--- | :--- |
| Windows | **1,102** | 39 |
| Office | 134 | 11 |
| 개발 도구 | 61 | 60 |
| SharePoint Server | 36 | 1 |
| SQL Server | 22 | 8 |
| Azure | 15 | 20 |

매체마다 총계가 1,411건·1,413건·1,760건으로 다르게 나온 것은 집계 범위 차이입니다. 릴리스 노트 제목은 Microsoft CVE 1,413건이고, 같은 페이지 표의 합계는 1,414건이에요. 1,760건은 Azure Linux 등 Microsoft가 재배포하는 외부 오픈소스 취약점까지 더한 수치입니다.

## 건수가 늘어난 배경

![2026년 월별 정기 보안 업데이트 Microsoft CVE 수 막대 차트](/assets/images/tech/windows-october-2026-patch/03-chart.webp)
*2026년 월별 정기 보안 업데이트 Microsoft CVE 수 막대 차트 — 출처: Microsoft Security Update Guide 월별 릴리스 노트 기반 자가 렌더*

2026년 4~6월 매달 160~220건이던 수치가 7월 663건, 9월 999건, 10월 1,413건으로 증가했습니다. Microsoft는 건수가 늘어난 원인을 구체적으로 밝히지 않았지만, 10월 13일 MSRC 블로그에서 AI 기반 연구가 취약점 발견에 기여하고 있어 많은 CVE를 묶어 검토하는 방식이 더 유용해질 수 있다고 적었어요.

10월 Microsoft CVE 1,413건 가운데 발견자 이름에 AI 모델이나 AI 보안 회사가 함께 적힌 것은 약 70건이에요. 악용된 CVE-2026-96951의 감사 명단에도 Anthropic의 Claude를 사용한 연구자가 들어 있습니다. 다만 나머지 1,340여 건은 익명(Anonymous)이나 개인 이름만 적혀 있어, 명단만으로는 AI를 쓴 비율 전체를 알 수 없어요.

Microsoft는 늘어난 건수를 다루기 위해 사용 환경과 관련된 확인 사항이 비슷한 취약점끼리 묶은 위험 코호트(risk cohort)를 실험적으로 공개했습니다. 파일시스템·스토리지 136건, Office 문서·메일 135건처럼 묶는 방식인데, 공식 분류가 아니고 개별 평가를 대체하지 않는다고 밝혔어요.

> Cohorts do not replace careful review of high-severity or actively exploited vulnerabilities. (MSRC, 2026.10.13)

## Windows 11 24H2 지원 종료

![Microsoft Learn Windows 11 Home·Pro 버전별 지원 기간](/assets/images/tech/windows-october-2026-patch/04-capture.webp)
*Microsoft Learn Windows 11 Home·Pro 버전별 지원 기간 — 출처: Microsoft*

Windows 11 Home·Pro의 하반기(H2) 버전은 출시 후 24개월 동안 보안 업데이트를 받습니다. 2024년 10월에 출시된 24H2는 2026년 10월 13일(미국 태평양 시간)로 기간이 끝났고, 10월 누적 업데이트 KB5127648이 마지막이에요.

| 버전 | 출시 | 지원 종료 |
| :--- | :--- | :--- |
| 24H2 | 2024년 10월 | <mark>2026년 10월 13일</mark> |
| 25H2 | 2025년 9월 | 2027년 10월 12일 |
| 26H2 | 2026년 9월 | 2028년 10월 9일 |

종료 후에도 PC는 그대로 켜지고 쓸 수 있지만 새 보안 패치가 배포되지 않습니다. 11월 정기 업데이트부터 24H2에 해당하는 취약점이 공개돼도 수정되지 않는다는 뜻이에요. 같은 24H2라도 Enterprise·Education 에디션은 2027년 10월까지 지원됩니다.

Windows 10은 2025년 10월 일반 지원이 끝났고, 개인 사용자는 확장 보안 업데이트(ESU)에 등록해야 패치를 받습니다. Microsoft는 개인용 ESU 종료일을 2026년 10월 13일에서 2027년 10월 12일로 1년 연장했어요. 10월 ESU 업데이트는 KB5126657입니다.

| ESU 등록 방법 | 비용 |
| :--- | :--- |
| PC 설정 동기화(백업) 사용 | **무료** |
| Microsoft Rewards | 1,000포인트 |
| 일회성 구매 | 4만 2,000원(30달러) |

## 내 PC 점검

![내 PC 점검 다섯 가지 정리 카드](/assets/images/tech/windows-october-2026-patch/05-items-pc.webp)
*내 PC 점검 다섯 가지 정리 카드 — 출처: Microsoft 안내 기반 자가 렌더*

악용된 CVE-2026-96951은 받은 파일을 열 때 표시되는 경고를 우회하는 취약점이라, 업데이트를 마치기 전까지는 출처를 모르는 첨부파일·다운로드 파일을 열지 않는 것이 직접적인 대응입니다.

24H2에서 25H2로 전환하는 업데이트는 같은 기반에서 기능을 활성화하는 방식이라 설치 시간이 짧습니다. Windows 업데이트 화면에 기능 업데이트가 보이지 않으면 Microsoft가 기기별로 순차 배포하는 중일 수 있어요.

## 앞으로 주목할 점

- CVE-2026-96951을 실제 공격에 쓴 주체와 공격 대상 공개 여부
- 11월 정기 업데이트에서 Microsoft CVE 수가 1,000건대를 유지하는지
- 위험 코호트가 Security Update Guide 정식 기능으로 추가되는지
- 24H2 Home·Pro 기기의 25H2·26H2 자동 업데이트 진행 상황

## 참고 출처

- [[Microsoft] Security Update Guide 2026년 10월 릴리스 노트·CVRF (본문 이미지 출처, 건수·유형 집계)](https://msrc.microsoft.com/update-guide/releaseNote/2026-Oct)
- [[MSRC] Using risk cohorts to prioritize security updates (2026-10-13)](https://www.microsoft.com/en-us/msrc/blog/2026/10/using-risk-cohorts-to-prioritize-security-updates)
- [[Microsoft Learn] Windows 11 Home and Pro 수명 주기 (본문 이미지 출처)](https://learn.microsoft.com/en-us/lifecycle/products/windows-11-home-and-pro)
- [[Microsoft] Windows 10 개인용 확장 보안 업데이트](https://www.microsoft.com/en-us/windows/extended-security-updates)
- [[BleepingComputer] Microsoft October 2026 Patch Tuesday (2026-10-13)](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2026-patch-tuesday-fixes-1-411-flaws-3-zero-days/)
- 환율: 1달러 ≈ 1,400원 기준 환산
