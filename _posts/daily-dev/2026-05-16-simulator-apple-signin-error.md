---
title: "시뮬레이터 Apple 로그인 실패"
description: 새 Apple 개발자 계정으로 시뮬레이터에서 Sign in with Apple 시도 시 뜬 "username or password incorrect" 오류를 iCloud 약관 동의로 해결한 기록입니다
date: 2026-05-16
order: 1
category: Daily Dev
subcategory: Troubleshooting
tags: [troubleshooting, ios-simulator, sign-in-with-apple, oauth, icloud, apple-developer]
image: /assets/og/2026-05-16-simulator-apple-signin-error.png
---

새로 만든 Apple 개발자 계정으로 앱에 Sign in with Apple OAuth 를 붙이고 iOS 시뮬레이터에서 첫 로그인을 시도하자마자 "username or password incorrect" 오류가 떴습니다. 같은 계정으로 웹 로그인은 정상으로 통과되어서 자격증명 자체가 틀린 게 아니라 계정 상태 쪽이 문제일 것으로 보고 그쪽을 건드렸습니다

## 증상

iOS 시뮬레이터에서 앱 내 Sign in with Apple 버튼을 누르고 새로 만든 Apple ID 자격증명을 입력하면, 비밀번호가 분명 맞는데도 **"username or password incorrect"** 오류가 반복됩니다. 같은 자격증명으로 `appleid.apple.com` 웹 로그인은 정상으로 통과합니다

## 환경

| 항목        | 값                              |
| ----------- | ------------------------------- |
| 디바이스    | iOS 시뮬레이터 (macOS)          |
| 계정        | 신규 생성 Apple 개발자 계정     |
| 로그인 방식 | Sign in with Apple (앱 OAuth)   |
| 웹 로그인   | 정상 (appleid.apple.com)        |
| 실패 지점   | 시뮬레이터·앱 내 Apple 로그인만 |

당시 Xcode·iOS 시뮬레이터 상세 버전은 따로 기록해두지 않아서, 이 글의 재현성은 "신규 Apple 개발자 계정 + iOS 시뮬레이터" 조합 수준까지만 보장합니다

## 시도한 것

| 시도                                          | 결과     |
| --------------------------------------------- | -------- |
| 비밀번호 재확인 후 재입력                     | 실패     |
| 동일 계정으로 웹에서 로그인 (정합성 확인)     | 정상     |
| 웹 `icloud.com` 로그인 → 약관 동의 후 재시도  | **해결** |

비밀번호 자체는 정확했고 웹 로그인이 통과되었기 때문에, 적어도 자격증명 입력 오타가 원인은 아니라는 점부터 먼저 확인했습니다

## 해결

신규 계정은 **첫 iCloud 로그인 시 약관 동의 단계가 남아 있고, 이 단계를 통과하기 전엔 시뮬레이터의 앱 내 Apple 로그인이 거부**되는 상태였습니다

1. 브라우저에서 `icloud.com` 접속
2. 신규 Apple ID 로 로그인
3. 표시되는 **iCloud Terms of Service** 화면에서 동의 (Accept)
4. 시뮬레이터로 돌아가 앱에서 Apple 로그인 재시도 → 정상 통과 확인

핵심은 한 줄로 정리됩니다 — **새 Apple ID 는 웹 iCloud 에 한 번 로그인해서 약관을 받아들이고 나서야 OAuth 로그인이 허용됩니다**

## 원인 추정

확정적인 원인은 **불명** 으로 둡니다

표시된 오류 문구는 "username or password incorrect" 였지만, 실제 차단 사유는 자격증명이 아니라 "약관 미동의 상태의 계정" 이었던 것으로 보입니다. Apple 측이 이 상태를 내부적으로 어떻게 분류하고, 왜 잘못된 오류 문구로 노출하는지는 공개된 자료가 없어 추측 이상으로는 말하지 않겠습니다

## 아직 모르는 것

- iCloud ToS 외에 추가로 동의가 필요한 약관(개발자 약관·Media Services 약관 등)이 함께 걸리는 경우가 있는지
- 실기기에서도 동일한 차단이 발생하는지 — 이번엔 시뮬레이터에서만 확인했음
- 비밀번호 오타가 아닌 상황에서 왜 굳이 "username or password incorrect" 라는 오해 소지가 큰 문구로 표시되는지
