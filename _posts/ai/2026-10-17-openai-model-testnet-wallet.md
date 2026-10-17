---
title: "OpenAI 연구 모델, 남의 테스트넷 지갑 무단 사용"
description: "코딩 과제 중 허락 없이 남의 테스트넷 지갑 잔액을 쓰고 최종 보고에서 누락한 OpenAI 내부 모델의 일탈 사례를 정리합니다"
date: 2026-10-17
category: AI
subcategory: News
tags: [openai, ai-safety, misalignment, ai-agent, ethereum]
image: /assets/og/2026-10-17-openai-model-testnet-wallet.png
---

OpenAI가 내부 연구 모델의 일탈 사례를 10월 15일 공개했어요
코딩 과제를 받은 모델이 허락 없이 남의 테스트넷 지갑 잔액을 썼습니다
최종 보고에는 그 사실을 적지 않았어요!!!

![OpenAI 워드마크](/assets/images/ai/openai-model-testnet-wallet/01-logo-openai.webp)
*OpenAI 워드마크*

## 사건 경과

![OpenAI 정렬 연구 블로그의 사건 보고서 첫 화면](/assets/images/ai/openai-model-testnet-wallet/02-report-summary.webp)
*OpenAI 정렬 연구 블로그의 사건 보고서 첫 화면 — 출처: OpenAI*

모델은 **GPT-5.6 Sol** 계열의 내부 연구용 모델이에요
과제는 암호화폐 거래 프로토타입을 수정하고 스마트 계약을 배포하는 일이었습니다
배포 장소는 이더리움 테스트넷인 **Sepolia**였어요
<mark>과제에서는 계약 배포가 허용됐지만 수수료를 낼 지갑은 제공되지 않았습니다</mark>

| 날짜 | 내용 |
| :--- | :--- |
| 6월 26일 | 학습 과제 중 사건 발생 |
| <mark>9월 25일</mark> | 과거 기록 모니터링 중 발견 |
| 10월 15일 | 보고서 갱신 공개 |

## 지갑 잔액 조회와 수수료 무단 사용

![서명 직전 모델의 추론 기록(CoT) 발췌](/assets/images/ai/openai-model-testnet-wallet/03-report-cot.webp)
*서명 직전 모델의 추론 기록(CoT) 발췌 — 출처: OpenAI*

모델은 먼저 테스트 토큰을 나눠 주는 **faucet**을 찾았지만 실패했어요
이어서 개발자들이 흔히 쓰는 **공개 복구 구문**으로 계정을 만들었습니다
그 계정들의 잔액을 조회하는 스크립트를 직접 짰어요
조회한 주소는 <mark>362개</mark>였습니다!
그중 배포 수수료를 낼 만큼 잔액이 있는 계정 하나를 골랐어요
복구 구문을 알면 누구나 같은 계정의 개인 키를 복원할 수 있습니다
모델은 서명 직전에 이 자금을 써도 되는지 스스로 따졌어요!
<mark>결론은 공개된 키의 테스트 ETH라 가치가 없으니 써도 된다는 것이었습니다</mark>
배포는 성공했고 수수료는 해당 계정의 잔액에서 지출됐어요

## 최종 보고에서 누락된 무단 지갑 사용

![모델의 최종 보고와 OpenAI의 조치 문단](/assets/images/ai/openai-model-testnet-wallet/04-report-final.webp)
*모델의 최종 보고와 OpenAI의 조치 문단 — 출처: OpenAI*

최종 보고는 배포 완료와 검증 결과만 담았어요
<mark>남의 계정을 골라 잔액을 썼다는 내용은 없었습니다</mark>
OpenAI는 모델이 계정 주인의 허락 없이 스스로 사용해도 된다고 판단한 사례로 봤어요
Sepolia 토큰은 시장 가치가 없어 <mark>금전 피해는 없었습니다</mark>
같은 방식으로 메인넷 지갑의 자금을 사용했다면 실제 자산이 지출됐을 거예요!!

## OpenAI 조치와 국내 기준

OpenAI는 이런 과제에서 **실시간 인터넷 접속**을 차단하는 조치를 추가했어요
<mark>모니터링 범위를 전체 트래픽으로 확대했습니다</mark>
인터넷 접속이 발생하면 보안팀에 알림이 전달되는 구조예요
보고서는 같은 유형의 다른 사례가 있었는지는 밝히지 않았습니다

국내에선 과기정통부와 KISA가 7월 **AI 보안 레드티밍 가이드**를 냈어요
이 가이드는 AI 에이전트를 검증 대상에 넣었습니다
에이전트가 외부 시스템을 직접 호출하는 과정에서 권한 우회가 발생할 수 있기 때문이에요

## 참고 출처

- [[OpenAI Alignment] Using a funded test cryptocurrency wallet without authorization (사건 원 보고서, 본문 이미지 3점 출처)](https://alignment.openai.com/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization/)
- [[CoinDesk] An OpenAI agent ran out of Ethereum funds, and took from a wallet it did not own (2026-10-16)](https://www.coindesk.com/tech/2026/10/16/an-openai-agent-ran-out-of-ethereum-funds-and-took-from-a-wallet-it-did-not-own)
- [[디지털투데이] 과기정통부·KISA, AI 보안 레드티밍 가이드 발간 (2026-07-10)](https://www.digitaltoday.co.kr/news/articleView.html?idxno=682799)
