---
title: "iOS 27.0.1 배포 — 아이폰 18 프로 패닉풀 수정"
description: "패닉풀과 카메라·터치 오류를 고친 iOS 27.0.1 의 수정 항목과, 함께 배포된 iOS 26.7.1 을 정리합니다"
date: 2026-09-29
category: Tech
subcategory: News
tags: [ios-27, iphone-18-pro, panic-full, apple, software-update]
image: /assets/og/2026-09-29-ios-27-0-1-panic-full-fix.png
---

Apple이 한국 시간 9월 29일 새벽 **iOS 27.0.1**을 배포했습니다. iPhone 18 Pro와 iPhone 18 Pro Max에서 Face ID 인증에 실패하면 기기가 멈췄다가 재시작되던 이른바 패닉풀 현상을 수정한 업데이트예요.

같은 업데이트에 카메라 색상 이상과 터치 무반응 수정이 함께 포함됐고, iOS 26을 계속 쓰는 사용자용으로는 **iOS 26.7.1**이 따로 배포됐습니다.

![iPhone 18 Pro와 iPhone 18 Pro Max](/assets/images/tech/ios-27-0-1-panic-full-fix/01-hero-iphone18pro.webp)
*iPhone 18 Pro와 iPhone 18 Pro Max — 출처: Apple*

[아이폰 18 프로 재부팅, Apple 이 원인을 밝혔습니다 — Face ID 소프트웨어 문제](/posts/iphone-18-pro-panic-full-cause/)

## 릴리스 노트 수정 항목

Apple 릴리스 노트가 밝힌 수정 항목은 세 가지입니다. 문구에 **포함해(including)**라는 표현이 들어가 있어, 적히지 않은 버그 수정이 더 포함됐을 수 있어요.

| 수정 항목 | 대상 |
| :--- | :--- |
| <mark>Face ID 실패 시 재시작</mark> | 18 Pro·18 Pro Max |
| 2배 사진 색상 이상 | 일부 18 Pro·Pro Max |
| 알림·제어 센터 터치 무반응 | 모델 명시 없음 |

배포 시각은 미국 태평양 시간 9월 28일 오전 10시 9분, 한국 시간으로 9월 29일 새벽 2시 9분입니다. iOS 27이 배포된 지 2주 만의 첫 수정판이고, 같은 날 iPadOS 27.0.1과 visionOS 27.0.1도 배포됐어요.

Apple 보안 문서에는 iOS 27.0.1에 대해 **공개된 CVE 항목이 없다**고 적혀 있습니다. 이번 업데이트는 보안이 아니라 버그 수정판이에요.

## Face ID 재부팅 수정

![아이폰 18 프로 패닉풀 대응 경과](/assets/images/tech/ios-27-0-1-panic-full-fix/02-chart.webp)
*아이폰 18 프로 패닉풀 대응 경과 — 출처: Apple 릴리스 노트·보도 종합 기반 자가 렌더*

릴리스 노트의 첫 항목은 **iPhone 18 Pro와 iPhone 18 Pro Max가 Face ID 인증에 실패하면 예기치 않게 재시작될 수 있는 문제**입니다. 잠금이 설정된 앱을 열다 인증에 실패하면 화면이 몇 초 멈추고 기기가 다시 켜지던 증상이 이 항목에 해당해요.

기기 진단 기록에 **panic-full**이라는 로그가 남아 국내에서는 패닉풀로 불렸습니다. 9월 18일 국내 출시 다음 날부터 제보가 이어졌고, Apple은 한국 시간 9월 24일 소프트웨어 문제이며 기기 교체 없이 업데이트로 해결된다고 밝혔어요.

공식 확인에서 배포까지 닷새가 걸렸습니다. Apple이 예고한 9월 28일이 속한 주 초반 일정도 지켰어요.

원인에 대해서는 Apple이 설명을 더하지 않았습니다. iPhone 18 Pro는 Face ID 적외선 카메라를 화면 아래로 옮겼는데, MacRumors는 업데이트로 고칠 수 있다는 점에서 이 부품 자체의 결함은 아닌 것으로 봤어요.

## 카메라와 터치 수정

![iPhone 18 Pro 가변 조리개 촬영 예시](/assets/images/tech/ios-27-0-1-panic-full-fix/03-photo-aperture.webp)
*iPhone 18 Pro 가변 조리개 촬영 예시 — 출처: Apple*

두 번째 항목은 카메라입니다. 소수의 iPhone 18 Pro·Pro Max에서 **f/1.48** 조리개로 **2배** 사진을 찍으면 특정 조명 아래 색상 이상이 생길 수 있는 문제를 고쳤어요.

iPhone 18 Pro는 메인 카메라의 f/1.78 고정 조리개를 f/1.48, f/1.8, f/2.8, f/4.0 네 단계 가변 조리개로 바꿨습니다. MacObserver에 따르면 2배 사진은 별도 렌즈가 아니라 메인 센서의 일부 영역을 사용하는 방식이라 메인 카메라의 조리개 값을 그대로 따라가요.

세 번째 항목은 **알림 센터와 제어 센터를 동시에 열면 터치스크린이 반응하지 않을 수 있는 문제**입니다. iDrop News는 특정 스와이프 동작을 타이밍에 맞춰 하면 재현되는 이 버그가 SNS에서 장난으로 확산됐다고 전했어요.

iPhone 18 Pro 출시 직후 Macworld가 보도한 터치 무반응 증상이 이 항목과 같은 것인지는 Apple이 밝히지 않았습니다.

## 같은 날 배포된 iOS 26.7.1

![Apple 로고](/assets/images/tech/ios-27-0-1-panic-full-fix/04-logo-apple.webp)
*Apple 로고 — 출처: Apple*

iOS 27로 업데이트하지 않은 기기에는 **iOS 26.7.1**이 따로 배포됐습니다. iPhone 11 이후 모델이 대상이고, 실제 공격에 악용된 취약점 하나를 수정하는 보안 업데이트예요.

| 항목 | 내용 |
| :--- | :--- |
| 취약점 | **CVE-2026-86950** |
| 위치 | CoreGraphics |
| 유형 | 경계 밖 쓰기 |
| 영향 | 조작한 파일로 코드 실행 |
| 제보 | Meta Product Security |

Apple은 이 취약점이 **iOS 27 이전 버전**을 쓰는 특정 개인을 겨냥한 매우 정교한 공격에 악용됐을 수 있다는 보고를 받았다고 밝혔습니다. 같은 수정이 iPadOS 26.7.1, macOS Tahoe 26.7.1, macOS Sequoia 15.8.1에도 포함됐어요.

MacRumors는 iOS 27이 이 취약점의 영향을 받지 않는 것으로 봤습니다. iOS 26을 쓰는 기기라면 iOS 27로 업데이트하지 않더라도 26.7.1은 바로 설치하는 편이 안전해요.

## 수정 범위 밖의 증상

이번 수정은 Face ID 인증 실패에 이어 발생한 재부팅에 한정됩니다. 전자신문은 충전 중이나 앱 실행 중에 재부팅된다는 제보도 있었지만 이번 패치와의 관련성은 확인되지 않았다고 전했어요.

파이낸셜뉴스도 Apple이 확인한 원인은 Face ID 인증 실패 하나라며, 제보된 패닉풀 전부가 같은 원인인지는 검증되지 않았다고 짚었습니다. 업데이트 후에도 인증과 무관하게 재시작이 반복되면 이번 버그와 다른 문제일 가능성을 고려해야 해요.

국내에서는 애플코리아가 9월 23일 김장겸 의원실에 소프트웨어 업데이트를 예정하고 있으며 개별 피해 사례는 AppleCare를 통해 조치한다고 전달했습니다. 패닉풀 제보 초기에 기기를 교환받은 사용자에 대한 별도 안내는 9월 29일까지 확인되지 않았어요.

## 지금 정리

![iOS 27.0.1 패닉풀 수정 정리](/assets/images/tech/ios-27-0-1-panic-full-fix/05-items.webp)
*iOS 27.0.1 패닉풀 수정 정리 — 출처: 본문 정리 · 자가 렌더*

## 앞으로 주목할 점

- iOS 27.0.1 설치 뒤에도 재부팅 제보가 이어지는지
- 충전·앱 실행 중 재부팅에 대한 Apple의 별도 설명
- 기기를 교환한 사용자에 대한 애플코리아의 안내 여부
- iOS 27.1 정식판에 추가 안정성 수정이 포함되는지

## 참고 출처

- [[Apple] iOS 27.0.1·26.7.1 보안 릴리스 목록 (27.0.1 CVE 없음 확인)](https://support.apple.com/en-us/100100)
- [[Apple] iOS 26.7.1 보안 문서 (CVE-2026-86950, 대상 기기)](https://support.apple.com/en-us/149226)
- [[MacRumors] iOS 27.0.1 릴리스 노트 원문과 배포 시각 (2026-09-28)](https://www.macrumors.com/2026/09/28/apple-releases-ios-27-0-1/)
- [[9to5Mac] iOS 27.0.1 수정 항목 (2026-09-28)](https://9to5mac.com/2026/09/28/apple-releases-ios-27-0-1-for-iphone-heres-whats-new/)
- [[MacRumors] iOS 26.7.1 악용 취약점 수정 (2026-09-28)](https://www.macrumors.com/2026/09/28/ios-26-7-1-active-exploit-fixed/)
- [[iDrop News] 터치 무반응 버그 재현 방식 (2026-09-28)](https://www.idropnews.com/news/apple-releases-ios-27-0-1-iphone-18-pro-face-id-fix/268975)
- [[전자신문] 국내 배포와 수정 범위 밖 증상 (2026-09-29)](https://www.etnews.com/20260929000291)
- [[파이낸셜뉴스] 원인 확인 범위와 남은 의문 (2026-09-29)](https://www.fnnews.com/news/202609290854105354)
- [[MacRumors] iPhone 18 Pro 가변 조리개 네 단계](https://www.macrumors.com/how-to/iphone-18-pro-using-variable-aperture/)
- [[MacObserver] 가변 조리개가 적용되는 렌즈와 2배 촬영](https://www.macobserver.com/tips/round-ups/iphone-18-pro-variable-aperture-one-lens-shot-list-four-stops/)
- [[전자신문] 애플코리아 국내 입장, AppleCare 조치 (2026-09-24)](https://www.etnews.com/20260924000017)
