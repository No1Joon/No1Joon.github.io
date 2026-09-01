---
title: "패스키가 뚫렸다는 말, 전제를 보면 다릅니다 — Pass-ta-key"
description: "악성코드가 이미 돌고 있어야 성립하는 공격 3단계를 풀고, 그런데도 동기화 패스키 구조에서 이 연구가 중요한 이유를 짚습니다"
date: 2026-08-21
category: Tech
subcategory: Explainer
tags: [passkey, webauthn, fido, infostealer, account-security]
image: /assets/og/2026-08-21-passkey-pass-ta-key-attack.png
---

패스키가 뚫렸다는 소식이 이달 초에 돌았습니다. 비밀번호를 없애자고 밀던 그 방식이요.

먼저 전제부터 정확히 짚고 가겠습니다. **이 공격은 피해자 기기에 이미 악성코드가 돌고 있어야 성립합니다.** 그러니 "패스키를 쓰면 위험하다"로 읽으면 틀립니다. 그런데도 이 연구가 중요한 이유가 따로 있어요.

![한 곳에 모아 둔 열쇠 뭉치가 통째로 빠져나가는 구조 개념 컷](/assets/images/tech/passkey-pass-ta-key-attack/01-agy-hero-synckeys.webp)
*한 곳에 모아 둔 열쇠 뭉치가 통째로 빠져나가는 구조 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

## 무엇이 뚫렸나 — 세 단계입니다

![단계가 올라갈수록 얻는 것이 커지는 구조 개념 컷](/assets/images/tech/passkey-pass-ta-key-attack/02-agy-ladder.webp)
*단계가 올라갈수록 얻는 것이 커지는 구조 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

Palo Alto Networks의 Unit 42가 8월 3일 공개한 연구입니다. 연구자는 Arie Olshtein이고, 이름을 **Pass-ta-key**로 붙였어요. 윈도우 도메인 공격의 고전인 *pass-the-ticket* 계열 작명을 그대로 가져온 겁니다.

단계가 셋인데, 올라갈수록 얻는 게 달라집니다.

| 단계 | 무엇을 얻나 |
|---|---|
| Pass-ta-key | 사용자 상호작용 없이 **계정 접근** |
| Silver Pass-ta-key | 피해자 기기 없이도 쓰는 <mark>재사용 가능한 접근권</mark> |
| Golden Pass-ta-key | **동기화된 패스키 전부**의 개인키 |

마지막 단계가 이 연구의 핵심입니다. 구글이 동기화하는 패스키의 개인키는 **보안 도메인 시크릿(SDS)** 이라는 32바이트 대칭 마스터키가 보호하는데, 그걸 뽑아내면 계정에 물린 패스키가 전부 풀립니다. 하나가 아니라 전부요.

Unit 42는 그렇게 빼낸 것이 자격증명 암시장에서 **공유하거나 팔 수 있는 형태**가 된다고 적었습니다. 한 대가 감염되면 그 사람이 패스키로 잠가 둔 모든 서비스가 한꺼번에 넘어간다는 뜻이에요.

## 전제를 정확히 읽으면

![Google 로고](/assets/images/tech/passkey-pass-ta-key-attack/03-logo-google.webp)
*Google 로고 — 출처: Google*

앞서 말한 대로 출발점은 악성코드입니다. 그래서 "이미 털린 기기면 뭐든 털리는 거 아니냐"는 반응이 나오는데, 연구가 짚은 조건을 보면 그렇게 넘기기 어렵습니다.

- 관리자 권한이 **필요 없습니다**
- 기기 잠금해제가 **필요 없습니다**
- 검증 환경은 윈도우 + TPM(보안 칩) 장착 기기의 Chrome입니다. Chrome 142에서 확인했고 최신 안정 버전까지 동작했습니다

일반 사용자 권한으로 도는 흔한 인포스틸러가 할 수 있는 범위라는 뜻입니다. 생체인증을 요구하는 화면을 통과했는지 여부는 응답에 담긴 **사용자 검증(UV) 플래그** 한 비트로 표시되는데, 진짜로 지문을 찍고 만든 응답과의 차이가 그 한 비트뿐이었다고 합니다.

CVE는 붙지 않았습니다. Olshtein은 구글이 **기기가 이미 침해된 상태를 전제하는 문제에는 CVE를 잘 부여하지 않는다**고 설명했어요. 구글 쪽 답변은 이랬습니다.

> 클라우드 엔클레이브 인증기의 주 기능은 패스키 개인 데이터를 훔치기 어렵게 만드는 것입니다

*어렵게* 라고 했지 *불가능하게* 라고 하지 않았다는 점이 이 문장의 전부입니다. 설계 목표 자체가 그 선에 그어져 있었던 거예요.

구글은 보고받은 것 중 Chrome 로그에 SDS가 남던 문제는 고쳤습니다. 기기 키 검증이 없다는 지적과 서명 카운터 개선 제안은 별도 이슈로 올라가 있고요.

### 그러면 패스키는 실패한 걸까요

아닙니다. 패스키가 원래 막겠다고 한 건 **피싱**입니다. 가짜 사이트에 비밀번호를 넣는 사고요. 그건 여전히 잘 막습니다. 패스키는 도메인에 묶여 있어서 가짜 사이트에서는 아예 동작하지 않으니까요.

이번에 드러난 건 **악성코드가 이미 들어온 뒤**의 이야기입니다. 다만 비밀번호 시절과 달라진 게 하나 있어요. 예전에는 감염되면 그 기기에 저장된 것이 샜는데, 지금은 **클라우드에 동기화해 둔 것까지 함께 샙니다.** 편해지자고 한 동기화가 피해 범위를 넓힌 셈입니다.

## 국내 서비스는 어떤가

![국내 서비스의 패스키 도입 경과](/assets/images/tech/passkey-pass-ta-key-attack/04-chart.webp)
*국내 서비스의 패스키 도입 경과 — 출처: 각 사 공지·국내 보도 종합 기반 자가 렌더*

국내도 패스키를 이미 밀고 있습니다. 네이버가 2025년 1월 PC·모바일 웹에 도입했고, 카카오계정도 지문·얼굴로 로그인하는 방식을 넣었어요. 카카오는 웹까지 지원해서 카카오 로그인을 쓰는 외부 서비스에도 적용됩니다. SK텔레콤 PASS와 KT 앱에도 들어가 있고, 금융·쇼핑 앱으로 번지는 중입니다.

여기서 갈라 봐야 할 게 있습니다. 이번 연구는 **구글이 동기화하는 패스키**를 대상으로 했습니다. 네이버나 카카오에 패스키를 걸었더라도, 그 패스키를 **크롬·구글 계정에 동기화해 두었다면 같은 사슬에 걸립니다.** 반대로 아이폰 iCloud 키체인이나 별도 보안 키에 저장했다면 이 연구의 범위 밖이에요.

서비스를 만드는 쪽에서 막을 방법도 나왔습니다. Unit 42는 **userVerification을 required로 요구하고 모든 응답에서 UV 플래그를 실제로 검증**하라고 권고했습니다. 새로 등록되는 기기 키의 출처와 증명을 확인하고, 불필요하게 재등록이 반복되는 흐름을 제한하라는 것도 함께요. 실제로 검증이 엄격한 GitHub은 기본 단계 공격이 막혔고, 약점이 있던 eBay는 통보를 받고 고쳤습니다.

### 지금 할 수 있는 것

- 결국 **악성코드가 안 들어오게 하는 게 1번**입니다. 이 공격은 거기서 출발합니다
- 구글 비밀번호 관리자의 PIN을 바꾸거나 데이터를 지우는 선택지가 있습니다. 다만 **내 SDS가 이미 샜는지 확인할 방법이 없고**, 그것만 골라 교체하는 기능도 없습니다
- 중요한 계정은 패스키를 기기에만 두거나 별도 보안 키를 쓰는 쪽이 동기화보다 안전합니다. 편의는 그만큼 줄어듭니다
- 윈도우 + 크롬 조합이 아니면 이번 연구의 검증 범위 밖입니다. 다만 검증하지 않았다는 것이지 안전하다고 확인된 건 아닙니다

가장 답답한 대목은 두 번째입니다. 털렸는지 아닌지를 사용자가 알 수 없고, 의심스러우면 통째로 지우는 것 말고 방법이 없어요. 비밀번호는 유출이 의심되면 그 하나만 바꾸면 됐는데, 지금은 그 단위가 사라졌습니다.

## 참고 출처

- [[Unit 42] Pass the Passkey: A Novel Attack Surface in Passwordless Authentication — 3단계 공격·SDS·권고 사항 (2026-08-03)](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/)
- [[The Hacker News] Google Password Manager Attacks Could Let Malware Hijack Passkey-Protected Accounts (2026-08-03)](https://thehackernews.com/2026/08/google-password-manager-attacks-could.html)
- [[BleepingComputer] New Pass-ta-key attacks let malware hijack Google-synced passkeys](https://www.bleepingcomputer.com/news/security/new-pass-ta-key-attacks-let-malware-hijack-google-synced-passkeys/)
- [[카카오] 카카오계정에 패스키 로그인 도입 공지](https://www.kakaocorp.com/page/detail/11349)
- [[SK쉴더스] 비밀번호 없는 로그인 — 패스키 보안성과 기업 도입 시 주의사항](https://www.skshieldus.com/security-insights/trends/passkeys-security-enterprise-considerations)
- 검증 환경은 윈도우 + TPM 장착 기기의 Chrome 이며, 다른 환경은 연구에서 다루지 않았습니다
