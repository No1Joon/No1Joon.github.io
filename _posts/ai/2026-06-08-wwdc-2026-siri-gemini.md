---
title: "WWDC 2026 — 새 Siri AI 의 두뇌가 구글 제미나이인 이유"
description: "애플이 간판 AI 기능을 라이벌 모델에 맡긴 배경과 온디바이스·클라우드 분담, iOS 27 과 개발자 도구 변화를 정리합니다"
date: 2026-06-08
category: AI
subcategory: News
tags: [wwdc, apple, siri, gemini, on-device-ai]
image: /assets/og/2026-06-08-wwdc-2026-siri-gemini.png
---

애플이 현지시간 6월 8일 애플파크에서 **WWDC 2026** 키노트를 열었어요. 올해 주인공은 단연 **새 'Siri AI'**입니다. 그런데 그 두뇌가 애플 것이 아니라 **구글 제미나이(Gemini)**라는 점이 가장 큰 화제예요.

수년간 "AI는 우리 방식대로 직접 한다"던 애플이, 간판 기능을 라이벌 모델에 맡긴 셈이거든요. iOS 27부터 개발자 도구까지, 이번 발표를 정리해볼게요.

![WWDC 2026 OS 27 발표 공식 이미지(기기 라인업)](/assets/images/ai/wwdc-2026-siri-gemini/01-hero-wwdc26.webp)
*WWDC 2026 OS 27 발표 공식 이미지(기기 라인업) — 출처: Apple*

## 무슨 일이 있었나

이번 키노트의 핵심은 **Siri의 전면 재설계**와 **OS 네이밍 통일('27 시대')**, 그리고 **애플 인텔리전스(Apple Intelligence) 확장**입니다.

- **Siri AI** — 시스템 전반의 개인 맥락·화면 인식을 갖춘 대화형 비서로 재탄생
- Siri의 클라우드 두뇌로 **구글 제미나이의 애플 전용 버전** 채택
- **iOS 27·macOS 27·iPadOS 27·watchOS 27·tvOS 27·visionOS 27** 동시 공개('27 시대')
- macOS 27의 코드네임은 **'Golden Gate'**, 디자인 언어 **리퀴드 글래스(Liquid Glass)** 개편
- 개발자 베타는 6월 8일 즉시 배포, 정식 출시는 올가을

![Apple 로고](/assets/images/ai/wwdc-2026-siri-gemini/02-logo-apple.webp)
*Apple 로고 — 출처: Apple*

## 새 Siri AI — 무엇이 바뀌나

기존 Siri가 단순 음성 명령기였다면, 새 Siri AI는 **화면에 뭐가 떠 있는지 이해하고, 앱을 가로질러 맥락을 잇는** 비서로 바뀌었어요.

- **별도 'Siri 앱'** 신설 — 지난 대화·결과를 다시 불러올 수 있고 아이패드·맥에서도 동작
- 노트북에서 **화면 속 이미지·텍스트에 대해 바로 질문** 가능
- 다이내믹 아일랜드가 있는 아이폰은 요청 시 그 자리에 Siri 애니메이션 표시
- 비주얼 인텔리전스와 결합해 **보고 있는 것 기반**으로 답

## 핵심은 '구글 제미나이 딜'

이번 발표에서 가장 의미가 큰 대목이에요. 애플은 구글과 **다년 라이선스 계약**을 맺고, **애플 전용으로 튜닝한 제미나이**를 Siri의 클라우드 지능에 쓰기로 했어요. 외신은 그 대가를 **연 약 10억 달러(약 1조 4,000억 원) 규모로 보도**하고 있습니다(애플 공식 확인은 아님).

처리 분담이 핵심이에요.

### **온디바이스(기기 내)** — 표현력 있는 음성, 고급 받아쓰기, 화면 인식, 개인 맥락 조회는 **애플 실리콘 위 자체 차세대 파운데이션 모델**이 담당

### **클라우드** — 무거운 세계 지식·복잡한 추론만 **프라이빗 클라우드 컴퓨트(Private Cloud Compute)**를 통해 제미나이로 전달

즉 "민감하고 가벼운 건 애플이, 무겁고 똑똑해야 하는 건 구글이" 나눠 맡는 구조예요. 프라이버시를 지키면서 성능을 빌려오는 절충안인 셈입니다.

![Google 로고(제미나이 제공사)](/assets/images/ai/wwdc-2026-siri-gemini/03-logo-google.webp)
*Google 로고(제미나이 제공사) — 출처: Google*

## iOS 27 · 애플 인텔리전스 신기능

iOS 27에는 일상에서 바로 와닿는 기능이 여럿 들어왔어요.

- **Safari 탭 관리**, **원탭 비밀번호 업데이트**, 앱 간 맥락 인식
- **메시지 AI 답장 제안**, 통화 중 전화 앱이 메일·메시지에서 맥락을 끌어옴
- **Wallet 비주얼 인텔리전스** — 실물 멤버십·티켓의 바코드·QR을 스캔해 디지털 패스로 변환
- **사진 앱 'Spatial Reframing(리프레임)'** — 3D 모델링·AI로 이미 찍은 사진의 **각도·구도를 사후에 변경**
- 홈 앱 보안 카메라 알림 고도화, **자녀 보호 기능 대대적 개편**

지원 기기는 **아이폰 16 이후, 아이폰 15 Pro·Pro Max, A17 Pro 아이패드 미니, M1 이상 아이패드** 등이에요.

## 개발자 발표 (여기도 중요)

개발자 입장에선 'AI 공급자 선택권'이 커졌어요.

### **파운데이션 모델 프레임워크에 LanguageModel 프로토콜** 추가 — 온디바이스 모델로 프로토타이핑한 뒤, 복잡한 질의는 **제미나이·앤스로픽 클로드(Claude)** 등으로 라우팅하고, **Swift 패키지 의존성만 바꿔** 공급자를 교체할 수 있어요(세션 로직 수정 불필요).

### **Xcode 27** — 로컬 뉴럴 엔진 모델이 실시간 Swift 제안을 주고, 무거운 분석은 클로드·제미나이·OpenAI로 라우팅하는 **이중 엔진 에이전트형 코딩** 도입. 앱 시뮬레이션·테스트 작성/실행·라이브 프리뷰·iOS 시뮬레이터 제어까지.

### 애플은 **SiriKit 지원 종료(deprecation)**를 공식화 — 2~3년 유예(대략 iOS 29, 2028년 가을경)를 뒀어요.

![Claude 로고(Foundation Models·Xcode 27이 라우팅하는 모델 중 하나)](/assets/images/ai/wwdc-2026-siri-gemini/04-logo-claude.webp)
*Claude 로고(Foundation Models·Xcode 27이 라우팅하는 모델 중 하나) — 출처: Anthropic*

## 배경 / 맥락 (왜 지금일까)

애플은 그동안 'AI는 자체 기술·프라이버시 우선'을 강조해 왔어요. 그런 회사가 **간판 기능을 라이벌 모델에 의존**한다는 건 상징적입니다. Siri 개편이 수차례 미뤄지며 "애플이 AI 경쟁에서 뒤처졌다"는 평가가 누적된 상황이었거든요.

이번 딜은 그 현실을 인정하고, **직접 개발 대신 '제휴로 따라잡기'**를 택한 결정으로 읽혀요. 구글로선 자사 모델을 수억 대 아이폰 사용자에게 노출하는 길이 열린 셈이고요.

## 이게 왜 중요할까

사용자에겐 **올가을 iOS 27 업데이트로 똑똑해진 Siri와 사진·지갑·메시지 기능**이 실제로 손에 들어온다는 의미예요. 한국 사용자도 지원 기기라면 같은 흐름을 체감하게 됩니다.

업계 관점에선 더 큰 신호예요. **온디바이스는 자체 칩·모델, 클라우드는 외부 최강 모델**이라는 분담 구조가 표준이 될 수 있고, 개발자가 한 앱에서 **클로드·제미나이·OpenAI를 의존성 교체만으로 갈아끼우는** 시대가 열렸습니다. 'AI 공급자 중립' 경쟁이 본격화되는 거죠.

## 앞으로 주목할 점

- 제미나이 기반 Siri의 **실사용 품질·프라이버시** 체감 (가을 정식판)
- 애플-구글 계약의 **정확한 규모·기간**과 규제 당국의 시선
- 한국어 Siri AI의 적용 시점·완성도
- Foundation Models·Xcode 27 에이전트의 **개발 생산성** 실측

애플이 자존심을 내려놓고 라이벌 손을 잡은 이번 결정이, Siri를 정말 되살릴지가 올가을 첫 시험대예요. 저는 '온디바이스=애플 / 클라우드=구글'이라는 분담선이 얼마나 매끄럽게 작동할지가 가장 궁금하네요.

## 참고 출처

- [[TechCrunch] WWDC 2026: Siri AI·iOS 27·Apple Intelligence 총정리 (06.09)](https://techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/)
- [[Engadget] WWDC 2026 키노트 발표 전체 (06.09)](https://www.engadget.com/2189698/everything-announced-at-apples-wwdc-2026-keynote/)
- [[CNBC] 애플, WWDC 2026서 Siri AI 공개·리퀴드 글래스 변경 (06.08)](https://www.cnbc.com/2026/06/08/apple-wwdc-2026-live-updates.html)
- [[Google Blog] 애플 개발자에게 제미나이 모델 제공 (06.09)](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/)
- [[MacRumors] 2026 Platforms State of the Union — AI·개발자 도구 (06.09)](https://www.macrumors.com/2026/06/09/apple-outlines-major-ai-and-developer-tool-updates/)
- [[TechTimes] Foundation Models, 코드 변경 없이 AI 공급자 교체 (06.09)](https://www.techtimes.com/articles/318039/20260609/wwdc-2026-developer-tools-foundation-models-now-swaps-ai-providers-without-code-changes.htm)
