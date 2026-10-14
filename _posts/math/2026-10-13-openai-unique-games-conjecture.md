---
title: "OpenAI 내부 모델의 고유 게임 추측 증명 — Lean 은 통과, 사람 검증은 아직"
description: "OpenAI 가 공개한 수학 원고 가운데 고유 게임 추측 증명이 무엇을 주장하고 어디까지 검증됐는지 정리합니다"
date: 2026-10-13
category: Math
subcategory: Explainer
tags: [unique-games-conjecture, ai-math, lean, complexity-theory, openai]
image: /assets/og/2026-10-13-openai-unique-games-conjecture.png
---

OpenAI가 2026년 10월 6일 공개하지 않은 내부 모델이 만든 수학 원고를 대량 공개했고, 그중에 이론 컴퓨터과학의 대표 미해결 문제인 고유 게임 추측(Unique Games Conjecture)의 증명이 포함돼 있습니다.

증명에는 컴퓨터가 논리를 한 줄씩 확인하는 증명 보조기 Lean 형식화 자료가 포함돼 있어요. 다만 사람 전문가가 원고를 검토해 맞다고 확인한 단계는 아직 아닙니다. 스콧 애런슨(Scott Aaronson)은 블로그에 사람이 제대로 이해한 증명이 아직 거의 없다고 썼어요.

![OpenAI 원고 The Unique Games Theorem 첫 장 초록](/assets/images/math/openai-unique-games-conjecture/01-capture.webp)
*OpenAI 원고 The Unique Games Theorem 첫 장 초록 — 출처: OpenAI*

## 공개된 내용

공개처는 GitHub의 openai/math 저장소입니다. 2026년 10월 7일 기준 원고 719편이 결과 묶음(family) 372개로 나뉘어 있고, 모델에 제시한 문제는 약 4,000개였어요. OpenAI는 결과 하나당 평균적으로 ChatGPT Pro가 약 3시간 동안 추론할 때에 해당하는 연산을 사용했다고 밝혔습니다.

- 102번 묶음: 고유 게임 추측 증명, Max-Cut·Vertex Cover 근사 한계 등 원고 5편
- 105번 묶음: Khot의 2-to-1 게임 추측(완전 만족 판) 증명
- 그 밖에 행렬 곱셈 지수, 리만 제타 함수 영점 없는 영역, 호지 추측 특수한 경우 등
- OpenAI의 저장소 안내에 따르면 원고 대부분은 사람이 고치지 않은 모델 출력 그대로

보도마다 숫자가 다른 것은 집계 시점 때문이에요. 처음 공개 때는 원고가 722편이었고, 하루 뒤 3편이 철회돼 719편이 됐습니다. 372는 원고 수가 아니라 묶음 수예요.

## 고유 게임 추측이 묻는 것

그래프의 정점마다 색(라벨)을 하나씩 할당하는데, 선마다 "이쪽이 a색이면 저쪽은 반드시 b색" 같은 규칙이 붙어 있다고 해 봅시다. 한쪽 색이 정해지면 다른 쪽 색이 하나로 정해져서 고유 게임이라는 이름이 붙었어요.

![2002년 추측 제시부터 2026년 OpenAI 공개까지 경과 타임라인](/assets/images/math/openai-unique-games-conjecture/02-chart.webp)
*2002년 추측 제시부터 2026년 OpenAI 공개까지 경과 타임라인 — 출처: Khot 원논문 · Quanta Magazine · openai/math 기반 자가 렌더*

수배시 코트(Subhash Khot)가 2002년 대학원생 시절 제시한 추측은 이렇습니다. 규칙의 99%를 만족시킬 수 있는 문제와 1%도 만족시킬 수 없는 문제를 구별하는 일조차 다항 시간 안에는 불가능하다(NP-난해)는 주장이에요. 거의 모든 규칙을 만족시킬 수 있는 문제인데도 그 사실을 판별하기 어렵다는 뜻입니다.

그래프의 정점을 두 집합으로 나눴을 때 집합 사이 간선 수를 최대로 만드는 Max-Cut 문제에서, 1995년 개발된 Goemans–Williamson 알고리즘은 최적값의 약 **87.8%**까지 보장합니다. 2004년 연구로 고유 게임 추측이 참이면 이보다 나은 다항 시간 알고리즘은 없다는 것이 알려졌고, Vertex Cover의 2배 근사도 마찬가지로 더 줄일 수 없게 돼요.

2018년 Khot·Dor Minzer·Muli Safra가 2-to-2 정리를 증명하며 이 추측의 증명에 처음으로 큰 진전을 이뤘습니다. 그래도 추측 자체는 24년 동안 증명되지 않았어요.

## Lean 검증과 사람 검증

102번 묶음의 Lean 설명 문서는 형식화한 진술을 이렇게 적어요. 0과 1/2 사이의 어떤 ε, δ에 대해서도 3SAT을 고유 게임으로 변환하는 결정적 다항 시간 환원이 있고, 만족 가능한 입력은 값이 1−ε 이상, 만족 불가능한 입력은 δ 이하가 된다는 것입니다.

![openai/math 대표 결과 중 Lean 형식화 비율 게이지](/assets/images/math/openai-unique-games-conjecture/03-chart-lean.webp)
*openai/math 대표 결과 중 Lean 형식화 비율 게이지 — 출처: openai/math 저장소 기반 자가 렌더*

Lean은 증명이 그 진술을 논리적으로 도출하는지 기계적으로 확인합니다. 증명 보조기가 받아들였다면 증명 과정에 논리적 오류가 있을 가능성은 크게 줄어요. 남은 검토 대상은 형식 진술입니다.

| 질문 | Lean이 답하나 |
| :--- | :--- |
| 증명이 형식 진술을 이끄나 | <mark>답한다</mark> |
| 형식 진술이 Khot의 추측과 같나 | **사람이 확인** |
| 다항 시간 정의가 표준과 같나 | 사람이 확인 |
| 원고 설명이 Lean 증명과 같나 | 사람이 확인 |

형식 진술은 3SAT 입력의 부호화, 기계 모델, 시간 한계까지 Lean 정의로 형식화해야 해서 길고 세밀합니다. 정의 하나가 표준과 미묘하게 달라도 Lean 검증은 통과할 수 있지만 수학계가 말하는 추측과는 다른 정리가 될 수 있어요. 8월 13일 글에서 다룬 Astra의 경우처럼, 형식화는 1차 검증 단계이고 진술 검토가 끝나야 결론이 납니다.

[AI 가 27년 묵은 수학 난제를 풀었다 — 검증은 누구나 할 수 있다](/posts/astra-math-lean-proofs/)

저장소 전체로 보면 대표 결과 719건 중 300건, 약 42%에만 Lean 형식화가 있어요. 나머지 58%는 원고만 있는 상태이고, OpenAI도 저장소 안내문에 형식화되지 않은 결과에는 문제가 있을 수 있다고 적었습니다.

## 수학자들의 반응

애런슨은 공개 다음 날 블로그 글에서 이날을 수학사에서 가장 큰 날 중 하나라고 부르면서도, 사람이 이해한 증명이 거의 없고 이를 이해하려는 경쟁이 막 시작됐다고 썼어요. 고유 게임 추측을 오래 연구해 온 그의 배우자 Dana Moshkovitz는 원고가 AI 도움 없이는 읽기 힘들 만큼 거칠게 쓰였다고 했고, AI 도움을 받아 증명의 대부분을 이해했다고 전해졌습니다.

Quanta Magazine에 따르면 MIT의 Dor Minzer는 9월 11일 OpenAI가 증명을 발견했다는 소문을 들었고, 사흘 뒤 대학원생 Yumou Fei·Shuo Wang과 함께 2-to-1 추측보다 약한 4-to-1 형태의 95쪽 논문을 공개했어요. Minzer는 6절 이후로는 연결하는 문장이 하나도 없을 만큼 서둘렀다고 말했습니다.

프린스턴의 Mark Braverman은 보도자료로 수학 성과를 발표하는 방식은 건강하지 않다며 AI 증명도 한 번의 발표로 검증이 끝나는 일이 아니라고 했어요.

OpenAI는 10월 7일 아벨 다양체 관련 원고 하나의 부호 오류로 그 원고와 이를 바탕으로 작성한 원고 2편, 모두 3편을 철회했고, 다른 14편은 증명을 보완해 수정했어요. 고유 게임 원고와는 다른 분야지만 형식화 없는 원고를 그대로 믿기 어렵다는 점을 보여 줍니다.

## 앞으로 확인할 것

![고유 게임 추측 증명 주장 정리 카드](/assets/images/math/openai-unique-games-conjecture/04-items.webp)
*고유 게임 추측 증명 주장 정리 카드 — 출처: openai/math · Quanta Magazine 기반 자가 렌더*

- 고유 게임 원고를 사람이 다시 쓴 해설과 외부 전문가 검토 결과
- Lean 형식 진술의 정의가 표준 정의와 맞는지에 대한 검토
- 학회·학술지 투고 여부, OpenAI가 밝힌 개정 기록에 102번 묶음이 포함되는지
- Minzer 팀 4-to-1 논문과 OpenAI 2-to-1 결과의 관계 정리

## 참고 출처

- [[OpenAI] openai/math 저장소 README·history (원고 수, Lean 비율, 철회 내역, 본문 이미지 1점 출처)](https://github.com/openai/math)
- [[OpenAI] 102번 묶음 Lean 형식화 범위 설명](https://github.com/openai/math/blob/main/lean/docs/102.md)
- [[OpenAI Developer Community] First look at mathematics manuscripts from an internal frontier model (2026-10-06)](https://community.openai.com/t/first-look-at-mathematics-manuscripts-from-an-internal-frontier-model-at-openai/1403886)
- [[Quanta Magazine] As AI Closed In on Unique Games Proof, Researchers Raced to Beat the Machines (2026-10-07)](https://www.quantamagazine.org/as-ai-closed-in-on-unique-games-proof-researchers-raced-to-beat-the-machines-20261007/)
- [[Shtetl-Optimized] Scott Aaronson, The Mathocalypse (2026-10-07)](https://scottaaronson.blog/?p=10169)
- [[Wikipedia] Unique games conjecture (배경, Max-Cut 연결)](https://en.wikipedia.org/wiki/Unique_games_conjecture)
