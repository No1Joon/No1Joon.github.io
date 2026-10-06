---
title: "Chrome 154 보안 업데이트 — 취약점 108건 중 Critical 11건"
description: "그래픽 계층에 몰린 Critical 취약점 구성과 실제 공격 여부, Edge·Whale 등 Chromium 기반 브라우저의 반영 시점을 정리합니다"
date: 2026-09-23
category: Tech
subcategory: News
tags: [chrome, browser-security, chromium, security-update, cve]
image: /assets/og/2026-09-23-chrome-154-security-update.png
---

Google이 2026년 9월 22일 Chrome 154를 데스크톱 안정판으로 배포하면서 보안 수정 108건을 함께 공개했습니다. 그중 가장 높은 등급인 Critical이 11건이고, 대부분이 화면을 그리는 그래픽 계층에 집중돼 있어요.

릴리스 노트에는 실제 공격에 쓰였다는 표기가 한 건도 없습니다. 그래도 국내 데스크톱 브라우저의 90% 이상이 같은 Chromium 엔진을 쓰고 있어, 영향이 Chrome 사용자에게만 한정되지 않아요.

![Google Chrome 공식 소개 이미지](/assets/images/tech/chrome-154-security-update/01-hero-chrome.webp)
*Google Chrome 공식 소개 이미지 — 출처: Google*

## 업데이트 개요

Chrome 154의 버전 번호는 Linux가 **154.0.8037.57**, Windows와 Mac이 **154.0.8037.57/.58**입니다. Google은 며칠에서 몇 주에 걸쳐 순차 배포한다고 밝혔어요. 같은 날 배포된 Android용 Chrome 154(154.0.8037.57)도 데스크톱판과 같은 보안 수정을 담았습니다.

보안 수정은 108건이며, 등급은 Critical 11건·High 25건·Medium 47건·Low 25건입니다. 릴리스 노트는 사용자 대부분이 업데이트를 마칠 때까지 버그 상세와 링크를 비공개로 유지한다고 적었어요.

## 등급별 수치

![Chrome 154 보안 수정 등급별 건수](/assets/images/tech/chrome-154-security-update/02-chart.webp)
*Chrome 154 보안 수정 등급별 건수 — 출처: Google Chrome Releases 기반 자가 렌더*

Chromium 보안 등급 기준에서 Critical은 공격자가 **사용자 권한 그대로 기기의 파일·레지스트리·네트워크를 읽거나 쓸 수 있는** 결함을 뜻합니다. 샌드박스(sandbox, 웹 페이지를 격리해 실행하는 공간) 안에서만 코드가 실행되는 결함은 High로 분류돼요.

| 구성 요소 | 결함 유형 | 건수 |
| :--- | :--- | :--- |
| ANGLE | 버퍼 오버플로 | <mark>3</mark> |
| GPU | 경계 밖 쓰기 | 2 |
| WebGL | 버퍼 오버플로·경계 밖 쓰기 | 2 |
| ServiceWorker·Fullscreen | 해제 후 사용 | 2 |
| WindowDialog·AdFilter | 해제 후 사용 | 2 |

ANGLE은 웹 페이지의 그래픽 명령을 Windows의 Direct3D 같은 운영체제 그래픽 API로 옮기는 계층이고, WebGL은 웹 페이지가 3D 그래픽을 그리는 표준입니다. ANGLE·GPU·WebGL을 합친 그래픽 계층이 Critical 11건 중 **7건**이에요.

나머지 4건은 해제 후 사용(use-after-free), 즉 프로그램이 이미 반납한 메모리를 다시 쓰는 결함입니다. 108건 전체로 봐도 해제 후 사용이 23건으로 가장 많았어요.

## 공격 전제와 범위

공개된 설명으로 보면 Critical 결함의 공통 전제는 **조작된 웹 페이지를 여는 것**입니다. 사용자가 파일을 내려받거나 설치하지 않아도 되는 경로라서 등급이 높게 평가돼요. 반대로 버그 상세가 비공개라, 어떤 조건에서 실제로 공격이 성립하는지는 공개 자료로 확인할 수 없습니다.

| 구분 | 내용 |
| :--- | :--- |
| 확인된 것 | 수정 108건·Critical 11건 |
| 확인된 것 | 대상 버전과 배포 시작일 |
| **확인 안 된 것** | 실제 공격 악용 여부 |
| 확인 안 된 것 | 결함별 공격 조건 |

Google은 실제 공격이 확인된 결함이면 릴리스 노트에 **exploit exists in the wild** 문구를 넣는데, 154 노트에는 이 문구가 없어요. Critical은 결함이 악용됐을 때의 피해 크기로 평가하는 등급이라, 실제 악용 여부와는 따로 읽어야 해요.

108건 중 76건은 Google 내부에서 찾았고, 32건은 외부 연구자가 제보했어요. 포상금이 정해진 5건 가운데 최고액은 700만 원(5,000달러)이고, ANGLE 버퍼 오버플로 3건은 모두 싱가포르 보안 회사 STAR Labs 연구진이 제보했습니다.

## 2주 배포 주기와 9월 제로데이

![Chrome 2주 배포 주기 시작 발표 이미지](/assets/images/tech/chrome-154-security-update/03-photo-2.webp)
*Chrome 2주 배포 주기 시작 발표 이미지 — 출처: Google*

Chrome은 2026년 9월 8일 Chrome 153부터 메이저 업데이트 주기를 4주에서 2주로 단축했어요. Chrome 154는 이 주기로 배포된 두 번째 버전이고, 기업용 Extended Stable 채널은 8주 주기를 유지하되 보안 수정을 매주 받습니다.

Chrome 154 직전 3주 사이에는 제로데이(zero-day, 수정 전에 공격에 쓰인 취약점) 두 건이 수정됐어요.

- 9월 3일: V8 엔진 형식 혼동 결함 **CVE-2026-85046** 수정, 실제 악용 확인
- 9월 8일: Chrome 153에서 보안 수정 230건과 V8 경계 밖 쓰기 결함 **CVE-2026-87491** 수정, 실제 악용 확인

CVE-2026-87491은 서울대학교 Compsec Lab의 Jihyeon Jeong 연구원이 8월 6일 제보해 포상금 350만 원(2,500달러)을 받았어요. SecurityWeek 집계로 2026년 들어 실제 악용이 확인된 Chrome 제로데이는 이 결함까지 7건입니다.

## 국내 사용 환경

![국내 데스크톱 브라우저 점유율](/assets/images/tech/chrome-154-security-update/04-chart.webp)
*국내 데스크톱 브라우저 점유율 — 출처: Statcounter Global Stats 기반 자가 렌더*

Statcounter의 2026년 8월 집계로 국내 데스크톱 브라우저 점유율은 Chrome 67.84%·Edge 14.88%·삼성 인터넷 8.14%·Whale 4.16%입니다. 이 넷은 모두 Chromium 엔진 위에서 동작해, 합치면 **95.02%**가 같은 엔진을 쓰는 셈이에요.

Chromium 기반 브라우저는 Google이 고친 코드를 각 회사가 자기 제품에 반영해 배포해야 수정이 적용됩니다. Microsoft는 9월 22일 보안 릴리스 노트에 최근 Chromium 보안 수정을 인지하고 있고 수정판을 준비 중이라고 적었고, 그 시점 Edge 안정판은 153.0.4234.48이었어요.

Whale과 삼성 인터넷은 154 수정 반영 일정을 따로 공지하지 않았습니다. 확인할 방법은 각 브라우저의 정보 화면에서 최신 버전으로 업데이트하는 것뿐이에요.

## 사용자·운영자 조치

![브라우저 업데이트 적용 개념 컷](/assets/images/tech/chrome-154-security-update/05-agy.webp)
*브라우저 업데이트 적용 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

[Chrome 사용자]
주소창에 **chrome://settings/help**를 입력하면 업데이트를 확인하고, 다시 시작 버튼을 누르면 적용됩니다.

[버전 확인]
같은 화면의 버전이 154.0.8037.57 이상이면 이번 수정이 적용된 상태예요.

[Android 사용자]
Google Play에서 Chrome을 업데이트합니다. iOS용 Chrome은 Safari와 같은 WebKit 엔진을 써서 이번 목록과 구조가 다릅니다.

[Edge·Whale 사용자]
정보 화면에서 최신 버전을 받고, Chromium 154 반영판이 배포되면 다시 적용합니다.

[기업 관리자]
Extended Stable 채널을 쓰는 조직도 주간 보안 수정은 받습니다. 업데이트를 지연하는 정책을 설정해 두었다면 배포 일정을 점검해요.

보안 공지 확인과 침해 신고는 KISA 보호나라에서, 전화 상담은 118에서 받습니다.

🔗 링크 첨부 - https://www.boho.or.kr/

## 정리

![Chrome 154 보안 업데이트 정리 카드](/assets/images/tech/chrome-154-security-update/06-items.webp)
*Chrome 154 보안 업데이트 정리 카드 — 출처: Google Chrome Releases 기반 자가 렌더*

## 앞으로 주목할 점

- 버그 상세 공개: 사용자 대부분이 업데이트를 마치면 Google이 비공개로 유지한 결함 상세를 공개한다고 밝힘
- 포상금 확정: 금액이 TBD로 남은 제보 27건의 포상금 결정
- Edge 반영: Microsoft가 준비 중이라고 밝힌 Chromium 154 수정판 배포

## 참고 출처

- [[Google Chrome Releases] Stable Channel Update for Desktop, Chrome 154 보안 수정 108건 목록 (2026-09-22)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0856730748.html)
- [[Chrome for Developers] 2주 배포 주기 시작 발표 (2026-09-08)](https://developer.chrome.com/blog/chrome-two-week-start)
- [[Chromium] 보안 등급 기준 (Critical·High 정의)](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/severity-guidelines.md)
- [[SecurityWeek] Chrome 153과 2026년 일곱 번째 제로데이 (2026-09-09)](https://www.securityweek.com/chrome-153-patches-seventh-zero-day-of-2026/)
- [[Help Net Security] CVE-2026-85046 실제 악용 수정 (2026-09-04)](https://www.helpnetsecurity.com/2026/09/04/google-chrome-zero-day-cve-2026-85046/)
- [[Microsoft Learn] Edge 보안 릴리스 노트 (2026-09-22 항목)](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
- [[Statcounter] 대한민국 데스크톱 브라우저 점유율 (2026년 8월)](https://gs.statcounter.com/browser-market-share/desktop/south-korea)
- 환율: 1달러 ≈ 1,400원 기준 환산
