---
title: "OpenAI 가 나비에-스토크스에 내놓은 건 해답이 아니라 반례입니다"
description: "밀레니엄 상금이 그대로 남은 이유를 증명한 명제와 상금 문항의 조건 차이로 풀고, Lean 검증 뒤에도 남는 물음을 정리합니다"
date: 2026-09-09
category: Math
subcategory: Explainer
tags: [navier-stokes, millennium-prize, openai, lean, ai-math]
image: /assets/og/2026-09-09-navier-stokes-openai-counterexample.png
---

OpenAI가 2026년 9월 8일 나비에-스토크스 방정식에 대한 증명을 내놨습니다. 국내 보도는 「7대 난제를 풀었다」로 받았는데, 클레이 수학연구소의 상금은 그대로 남아 있어요.

푼 게 아니라서가 아닙니다. **증명한 명제가 상금이 걸린 문항과 조건이 다르기** 때문입니다.

![매끄럽던 흐름이 한 점으로 치솟는 장면](/assets/images/math/navier-stokes-openai-counterexample/01-agy-hero.webp)
*매끄럽던 흐름이 한 점으로 치솟는 장면 — 출처: 개념 컷 · agy 자가 생성*

## 이 방정식이 묻는 것

나비에-스토크스 방정식은 점성이 있는 유체가 어떻게 흐르는지를 기술합니다. 물과 공기의 움직임을 계산하는 데 쓰이니 실무에서는 이미 매일 풀리고 있어요.

밀레니엄 문제가 묻는 것은 계산이 아니라 **보장**입니다. 3차원 비압축성 유체에 매끄러운 초기 조건을 주면, 그 해가 영원히 매끄럽게 남는가. 이것을 존재성과 평활성 문제라고 부릅니다.

반대편에 있는 것이 **특이점**입니다. 유한한 시간 안에 유체의 속도가 무한대로 치솟는 상황이에요. 실제 물에서 일어나지 않는 일이라 방정식이 현실을 제대로 담고 있다면 나오지 말아야 합니다.

답은 영원히 매끄럽다고 증명하거나, 그렇지 않은 반례를 하나 만들어 보이는 두 갈래입니다.

## OpenAI가 증명했다고 밝힌 것

OpenAI가 발표문에 밝힌 조건은 처음에 정지해 있던 매끄러운 유체에 **매끄러운 외력**을 가하고, 전 과정에서 에너지가 유한하게 유지되는데도, 유한한 시간 안에 특이점이 생긴다는 것입니다.

즉 반례 쪽입니다. 영원히 매끄럽다는 명제를 깨는 사례를 하나 구성했다는 주장이에요.

| 항목 | OpenAI 발표 기준 |
|---|---|
| 원고 분량 | 166쪽 + Lean 형식화 |
| 투입 규모 | 에이전트 약 <mark>1만 개</mark> |
| 연산 시간 | 88시간, 1,300억 토큰 |

Lean은 증명을 기계가 검사할 수 있는 형태로 다시 쓰는 언어입니다. 사람이 읽고 넘어가는 논리 비약을 기계가 잡아내기 때문에, 형식화가 붙었다는 것은 **논리 자체는 검사를 통과했다**는 뜻이에요.

## 상금이 그대로 남아 있는 이유

클레이 연구소가 내건 문항은 **외력이 없는** 나비에-스토크스입니다. 이번 결과에는 외력이 붙어 있어요.

| 구분 | 클레이 문항 | 이번 증명 |
|---|---|---|
| 외력 | 없음 | <mark>매끄러운 외력 있음</mark> |
| 묻는 것 | 평활성 보장 | 특이점 구성 |
| 판정 | 미해결 | **심사 전** |

외력이 붙은 형태는 유체 방정식 연구에서 오래 다뤄 온 별도의 문제입니다. 밖에서 힘을 계속 넣어 줄 수 있으면 흐름을 원하는 방향으로 유도하기가 그만큼 수월해지고, 그래서 같은 질문이라도 난이도가 갈립니다.

그러니 「나비에-스토크스가 풀렸다」는 요약은 정확하지 않습니다. 정확히 적으면 **외력이 있는 나비에-스토크스에서 유한 시간 특이점을 구성했다**는 주장이고, 이것도 아직 동료 심사를 거치지 않았습니다.

![발표가 이어진 순서](/assets/images/math/navier-stokes-openai-counterexample/02-chart.webp)
*발표가 이어진 순서 — 출처: Tao 블로그와 본인 서술 기반 자가 렌더*

## 9월 7일 버크마스터·알푀게의 선행 발표

9월 7일, 뉴욕대의 트리스탄 버크마스터(Tristan Buckmaster)와 레벤트 알푀게(Levent Alpöge)가 세 방정식에 대한 유한 시간 특이점 결과를 Lean 형식화와 함께 공개했습니다. 비압축성 다공질 매질 방정식, 2차원 부시네스크 방정식, 3차원 비압축성 오일러 방정식입니다.

셋 다 나비에-스토크스 자체는 아니고, 같은 계열에서 더 다루기 쉬운 방정식들이에요. 테런스 타오(Terence Tao)는 같은 날 블로그에 이 결과를 소개하면서 코르도바와 마르티네스-소로아가 개척한 접근을 두 사람이 발전시켜 주요 유체 방정식들에서 특이점을 구성했다고 적었습니다.

여기서 우선권 문제가 제기됩니다. 버크마스터는 OpenAI가 자신들의 진행 상황을 알게 된 뒤 같은 방법을 채택했다고 주장했고, OpenAI가 주말에 자신들에게 연락해 온 정황도 함께 이야기했어요. 자신이 Codex에 넣어 둔 메모와 아이디어가 어떻게 쓰였는지도 문제로 삼았습니다.

OpenAI 쪽 설명과 두 사람의 서술이 아직 맞춰지지 않은 상태라, 지금 확실한 것은 **공개 시점이 하루 차이라는 사실**까지입니다.

## 기계 검증을 통과해도 남는 물음

8월 Lean 검증 편에서 살펴봤듯 형식 검증의 값어치는 누구나 다시 돌려 볼 수 있다는 데 있지만, 이번 건은 그 장치가 무엇을 보증하지 않는지를 함께 보여줍니다.

[AI 가 27년 묵은 수학 난제를 풀었다 — 검증은 누구나 할 수 있다](/posts/astra-math-lean-proofs/)

- Lean은 증명이 논리적으로 맞는지를 본다
- 그 명제가 상금이 걸린 문항인지는 안 본다
- 그 아이디어가 누구 것인지도 안 본다

첫째는 기계가 답할 수 있고 둘째는 사람이 문항을 대조해야 하며, 셋째는 기록과 증언으로만 가려집니다. 이번에 갈린 지점이 정확히 둘째와 셋째예요.

![글 끝 정리](/assets/images/math/navier-stokes-openai-counterexample/03-items.webp)
*글 끝 정리 — 출처: 본문 정리 · 자가 렌더*

## 앞으로 주목할 점

- 166쪽 원고의 동료 심사 착수와 결과
- OpenAI가 우선권 문제 제기에 어떤 기록을 내놓는지
- 외력 없는 형태로 확장 가능한지에 대한 후속 연구
- 클레이 수학연구소의 공식 입장 표명 여부

밀레니엄 문제는 논문이 나온 뒤 2년의 대기와 동료 심사를 거쳐야 판정에 들어갑니다.

## 참고 출처

- [[OpenAI] On the Navier–Stokes Millennium Prize Problem (2026-09-08, 발표문·증명 조건)](https://openai.com/index/navier-stokes-solution/)
- [[OpenAI] Finite Time Blowup for Navier–Stokes (원고 PDF)](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
- [[What's new / Terence Tao] Finite time blowup with smooth forcing term for the incompressible porous medium, Boussinesq, and incompressible Euler equations (2026-09-07, 세 방정식 결과 소개)](https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/)
- [[Forkast] OpenAI's 10,000-agent Navier-Stokes claim solves the wrong problem (클레이 문항과 외력 조건의 차이)](https://forkast.news/openais-10000-agent-navier-stokes-claim-solves-the-wrong-problem-and-the-right-one-has-a-provenance-controversy/)
- [[Unite.AI] Buckmaster and Alpöge post AI fluid blowup proofs, dispute OpenAI contact (8월 15일·22일 경위, 우선권 제기)](https://www.unite.ai/buckmaster-and-alpoge-post-ai-fluid-blowup-proofs-dispute-openai-contact/)
- [[Scientific American] OpenAI claims blockbuster math breakthrough amid swirl of controversy (논쟁 개요)](https://www.scientificamerican.com/article/openai-claims-blockbuster-math-breakthrough-amid-swirl-of-controversy/)
- [[이데일리] OpenAI, 90년 묵은 난제 나비에-스토크스 해법 제시 (국내 보도·투입 규모 수치)](https://www.edaily.co.kr/News/Read?newsId=02896246645578480)
