---
title: "Claude 세션 탈취로 사용량이 소진됩니다 — 로그아웃만으로는 안 끝납니다"
description: "인포스틸러에 감염된 PC 에서 Claude 로그인 세션이 빠져나간 경위와, MFA 로 막히지 않는 이유·조치 순서를 정리합니다"
date: 2026-09-16
category: Tech
subcategory: News
tags: [infostealer, session-hijacking, claude, malware, account-security]
image: /assets/og/2026-09-16-infostealer-claude-session-theft.png
---

Claude를 켜지도 않았는데 사용량이 절반 넘게 사라졌다면, 계정이 아니라 PC를 먼저 봐야 합니다.

Anthropic이 8월 말 일부 Claude 이용자에게 통지를 보냈습니다. 정보 탈취 악성코드(인포스틸러)에 감염된 PC에서 Claude 로그인 세션이 통째로 빠져나갔고, 공격자가 그 세션으로 계정에 들어와 유료 사용량을 소진하고 있다는 내용이었어요.

**Claude 서비스가 침해된 것이 아닙니다.** 공격이 성립하려면 이용자 PC에 이미 악성코드가 깔려 있어야 해요. 그래서 이 사건은 서비스 장애가 아니라 개인 PC 감염 문제에 가깝습니다.

![로그인 없이 넘어간 세션](/assets/images/tech/infostealer-claude-session-theft/01-agy-hero.webp)
*로그인 없이 넘어간 세션 — 출처: 개념 컷 · agy 자가 생성*

## 사건 경과

시작은 이용자 쪽이었습니다. TechCrunch에 따르면 개발자 그랜트 드 스와르트(Grant De Swardt)는 8월 4일 아무 작업도 하지 않는 동안 토큰 사용량이 45%에서 55%로 오르는 것을 발견했어요. 그가 Reddit에 올린 글에는 80개 가까운 댓글이 붙었고 GitHub에도 비슷한 보고가 이어졌습니다.

8월 30일에는 Anthropic이 피해로 확인된 계정에 통지를 보냈다는 사실이 보도됐습니다. 통지문에는 흔한 정보 탈취 악성코드로 이용자 컴퓨터에서 Claude 로그인 세션을 훔친 뒤 그 세션으로 계정에 접근하는 공격자를 확인했다는 설명이 담겼어요.

Anthropic은 통지문에서 이 악성코드가 Claude와 관련이 있거나 Claude를 통해 설치됐다고 볼 근거는 없다고 밝혔습니다. 사용량이 채워졌다가 본인이 쓰지 않는 사이 줄어든 것처럼 보였다면 이것이 원인일 가능성이 크다고도 적었어요.

- 첫 이용자 보고: 8월 4일
- 공격 경로: PC 감염 → 브라우저 세션 탈취 → Claude 계정 접근
- 소진 대상: 유료 요금제의 사용량 한도, 일부는 자동 업그레이드 결제까지
- 공식 블로그 성명이 아니라 **피해 계정 개별 통지**로 알려졌습니다

![첫 피해 보고부터 통지까지의 경과](/assets/images/tech/infostealer-claude-session-theft/02-chart.webp)
*첫 피해 보고부터 통지까지의 경과 — 출처: TechCrunch·BleepingComputer 보도 기반 자가 렌더*

## 비밀번호를 바꿔도 막히지 않는 이유

이 공격의 핵심은 비밀번호를 훔치지 않는다는 데 있습니다. 가져가는 것은 **세션 쿠키**예요.

세션 쿠키는 로그인에 성공한 뒤 브라우저에 저장되는 값입니다. 이미 인증을 마친 상태를 증명하는 표라서, 이 값을 가진 쪽은 아이디도 비밀번호도 2단계 인증도 거치지 않고 로그인된 상태로 들어갑니다.

| 방어 수단 | 세션 탈취에 |
| :--- | :--- |
| 비밀번호 변경 | **막지 못함** |
| MFA·2단계 인증 | **막지 못함** |
| 세션 폐기(로그아웃) | 훔친 세션은 차단 |
| 악성코드 제거 | <mark>근본 차단</mark> |

BleepingComputer 보도를 보면 공격자는 훔친 세션 쿠키로 Claude Code용 OAuth 토큰까지 무단 발급했습니다.

Anthropic은 통지문에서 로그아웃은 훔친 세션을 끊을 뿐 악성코드를 지우지는 못하며, 악성코드가 PC에 남아 있으면 다음 로그인 세션도 같은 방식으로 탈취될 수 있다고 경고했습니다.

[MFA 를 켰는데 세션을 털렸다면 — AitM 피싱과 세션 탈취](/posts/aitm-session-hijacking/)

## 피해자들이 본 화면

보도된 사례는 사용량 그래프의 이상한 움직임으로 시작합니다.

TechCrunch가 전한 사례 중에는 본인이 Claude를 쓰지 않는 사이 사용량이 0%에서 49%까지 12분 만에 오른 경우가 있었습니다. 0%에서 100%로 치솟으며 동의 없이 요금제가 자동 상향되고 신용카드에 청구된 사례, 사흘 연속 일일 한도가 소진된 사례도 함께 전해졌어요.

![한 피해자가 12분 만에 소진당한 사용량](/assets/images/tech/infostealer-claude-session-theft/03-chart.webp)
*한 피해자가 12분 만에 소진당한 사용량 — 출처: TechCrunch 보도 수치 기반 자가 렌더*

드 스와르트는 계정을 되찾기까지 2주가 걸렸고 약 7만 8,700원(44.49파운드)을 환불받았다고 밝혔습니다.

## Anthropic이 한 것과 하지 않은 것

회사가 취한 조치는 세 가지로 전해집니다.

- 피해 계정을 강제 로그아웃해 탈취된 세션을 무효화
- 저장된 결제 수단을 제거
- 무단 청구로 확인된 금액을 환불

이용자에게는 자격 증명을 바꾸고, 다른 세션을 폐기하고, PC에서 악성코드를 제거하라고 권고했습니다.

공개 보안 공지나 블로그 게시물 형태의 성명은 확인되지 않고, 알림은 피해로 확인된 계정에 개별 발송됐어요. 피해 규모도 공개되지 않았습니다. TechCrunch는 이용자가 자기 계정의 오용을 스스로 식별할 방법을 물었지만 답을 받지 못했다고 전했습니다.

![Anthropic 로고](/assets/images/tech/infostealer-claude-session-theft/04-anthropic-logo-color.webp)
*Anthropic 로고 — 출처: Anthropic*

## 국내 유포 현황

Anthropic이 지목한 악성코드는 Claude를 겨냥해 만들어진 것이 아닙니다. 예전부터 돌던 범용 정보 탈취 악성코드예요.

| 운영체제 | 지목된 인포스틸러 |
| :--- | :--- |
| Windows | <mark>Vidar · LummaC2 · StealC</mark> |
| Windows | RedLine · Acreed |
| macOS | Atomic Stealer(AMOS), 소수 |

이 이름들이 국내와 무관하지 않습니다. 안랩 ASEC이 낸 2026년 7월 인포스틸러 동향 보고서를 보면 국내에서 그달 유포된 주요 인포스틸러로 Remus, **LummaC2**, ACRStealer, **Vidar**가 꼽혔어요. Anthropic이 지목한 것과 겹칩니다.

유포 방식도 특별하지 않습니다. ASEC은 크랙과 키젠, 불법 프로그램으로 위장한 형태를 주요 경로로 들었고, 실행 파일 형태가 89.6%, DLL 사이드로딩이 10.4%였습니다. 내려받는 곳은 mega.nz나 mediafire.com 같은 파일 공유 서비스가 많았어요. 정상 기업을 사칭한 이름을 쓰는데, 가장 많이 도용된 이름은 Microsoft였고 AnyDesk와 Kaspersky, 삼성전자도 사칭 대상에 들었습니다.

유료 AI 구독이 새로운 표적이 됐을 뿐, 감염되는 경로는 예전 그대로예요.

## 대응 순서

악성코드를 지우지 않은 채 비밀번호만 바꾸면 바뀐 자격 증명이 다시 유출됩니다.

- **먼저 PC를 검사해 악성코드를 제거**하세요. 백신을 최신 상태로 두고 전체 검사를 돌리고, 감염이 확인되면 그 PC에서는 로그인하지 않는 편이 안전합니다.
- 그다음 **Claude 비밀번호를 바꾸고 다른 기기의 세션을 폐기**하세요.
- **사용량 그래프**를 확인하세요. 쓰지 않은 시간대에 사용량이 오른 구간이 있는지 보는 것이 가장 빠른 신호입니다.
- **결제 내역에서 모르는 청구**가 있는지 보세요. 동의하지 않은 요금제 상향이나 추가 결제가 있으면 고객센터에 환불을 요청할 수 있습니다.
- 최근에 크랙이나 불법 유틸리티, 파일 공유 사이트에서 받은 실행 파일이 있다면 그것부터 의심하세요.

내 계정이 피해 대상에 들었는지 이용자가 직접 조회할 창구는 공개되지 않았습니다. 개별 통지를 받지 않았다고 해서 안전하다고 단정하기는 어려워요.

## 앞으로 주목할 점

- Anthropic이 공개 보안 공지와 피해 규모를 밝히는지
- 이용자가 계정 오용을 스스로 확인할 수단(세션 목록·접속 기록)이 제공되는지
- 다른 유료 AI 서비스에서도 같은 방식의 사용량 탈취가 보고되는지
- 국내 인포스틸러 유포량이 AI 구독 계정을 노리는 쪽으로 옮겨 가는지

![이번 사건에서 확인할 것 정리](/assets/images/tech/infostealer-claude-session-theft/05-items.webp)
*이번 사건에서 확인할 것 정리 — 출처: 본문 요약 카드 · 자가 렌더*

## 참고 출처

- [[TechCrunch] Hackers are stealing Claude tokens from subscribers (09.08, 피해 사례·수치)](https://techcrunch.com/2026/09/08/hackers-are-stealing-claude-tokens-from-subscribers/)
- [[BleepingComputer] Anthropic warns infostealer malware is hijacking Claude sessions to drain usage (08.30, 통지문 문구·악성코드 목록)](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/)
- [[Help Net Security] Anthropic locks out Claude users after infostealers hijack login sessions (08.31)](https://www.helpnetsecurity.com/2026/08/31/claude-accounts-compromised-through-infostealer/)
- [[SecurityWeek] Anthropic Warns Claude Users of Infostealer Malware Infections](https://www.securityweek.com/anthropic-warns-claude-users-of-infostealer-malware-infections/)
- [[Dark Reading] Anthropic Users Hit by Infostealer Attacks, Session Thefts](https://www.darkreading.com/cyberattacks-data-breaches/anthropic-users-infostealer-attacks-session-thefts)
- [[ASEC] 2026년 7월 인포스틸러 동향 보고서 (국내 유포 종류·경로·비율)](https://asec.ahnlab.com/ko/95065/)
- Anthropic 통지문 인용 문구: TechCrunch·BleepingComputer 보도 기반
- 환율: 1파운드 ≈ 1,770원 기준 환산
