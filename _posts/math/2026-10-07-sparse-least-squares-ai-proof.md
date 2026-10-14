---
title: "희소 최소제곱의 조건수 장벽 — 증명은 Gemini 에이전트가 먼저 도출했다"
description: "Google 논문이 다룬 희소 회귀 추측과 그 증명을 Gemini 기반 에이전트가 먼저 찾고 사람이 검증한 과정을 정리합니다"
date: 2026-10-07
category: Math
subcategory: Explainer
tags: [sparse-regression, least-squares, ai-math, gemini, theorem-proving]
image: /assets/og/2026-10-07-sparse-least-squares-ai-proof.png
---

Google Research 연구자 세 명이 8월 3일 arXiv에 올린 논문 초록 끝에는 이런 문장이 있어요. 증명은 Google 내부의 완전 자동화된 Gemini 기반 에이전트 시스템이 먼저 도출했고, 저자들은 그 증명을 검증하고 가독성을 높이도록 수정했다는 내용입니다.

증명한 내용은 2021년 Axiotis와 Sviridenko가 남긴 추측으로, 변수를 적게 쓰는 회귀 문제에서 지금 알고리즘보다 확실히 나은 다항 시간 알고리즘은 없다는 주장이에요.

![논문 제목·저자·초록, AI 기여 문장 하이라이트](/assets/images/math/sparse-least-squares-ai-proof/01-hero-abstract.webp)
*논문 제목·저자·초록, AI 기여 문장 하이라이트 — 출처: arXiv*

## 논문 정보

| 항목 | 내용 |
| :--- | :--- |
| 제목 | *The Condition-Number Barrier in Sparse Least Squares* |
| 저자 | Honghao Lin · Vahab Mirrokni · David P. Woodruff |
| 소속 | **Google Research**, Carnegie Mellon University |
| 게시 | arXiv, 2026년 8월 3일 (cs.DS) |
| 유형 | <mark>이론 증명 논문, 동료 심사 전</mark> |

실험이나 측정이 없는 순수 이론 논문이에요. 17쪽 분량이고, 학술지나 학회 심사를 거치기 전의 프리프린트라 증명의 정확성은 저자 검증까지만 확인된 상태입니다.

## 논문이 다룬 문제

![희소 최소제곱 변수 개수 연구의 흐름](/assets/images/math/sparse-least-squares-ai-proof/02-chart.webp)
*희소 최소제곱 변수 개수 연구의 흐름 — 출처: arXiv 2608.02588·2609.15983 기반 자가 렌더*

**최소제곱(least squares)**은 데이터에 가장 잘 맞는 계수를 오차 제곱합이 가장 작아지게 찾는 방법이에요. 여기에 **희소(sparse)** 조건이 붙으면 0이 아닌 계수를 k개 이하로만 쓰라는 뜻이 되고, 수천 개 변수 중에서 결과를 설명하는 몇 개만 선택하는 변수 선택 문제가 됩니다.

정확히 k개로 최적해를 구하는 일은 1995년 Natarajan이 NP-난해임을 보였어요. 그래서 연구자들은 조건을 완화했습니다. 최적의 k개짜리 해와 거의 같은 오차(ε 이내)를 달성하되, 변수는 k개보다 더 써도 되게 한 거예요. 질문은 **변수를 얼마나 더 써야 하는가**입니다.

필요한 변수 개수를 좌우하는 값이 **제한 조건수(restricted condition number)** κ예요. 변수들이 서로 얼마나 닮아서 구분하기 어려운지를 나타내는 값으로, 1이면 변수가 서로 독립적이고 클수록 구분이 어렵습니다.

| 시기 | 필요한 변수 개수 | 결과 |
| :--- | :--- | :--- |
| 2010년 무렵 | k × κ² | 상한 |
| 2021년 | <mark>k × κ</mark> | Axiotis·Sviridenko 상한 |
| 2021년 추측 | k × κ¹⁻ᵞ 불가능 | 추측 27 |

Axiotis와 Sviridenko는 k × κ개의 변수를 사용하는 알고리즘을 만들고, 지수를 1보다 조금이라도 낮춘 k × κ¹⁻ᵞ개로는 다항 시간 안에 못 한다고 추측했어요(γ는 0보다 크고 1 이하인 상수). 특정 알고리즘이 실패하는 예시는 있었지만, 모든 다항 시간 알고리즘에 적용되는 하한 증명은 없었습니다.

## 논문의 결론

![논문의 주정리 Theorem 1.1](/assets/images/math/sparse-least-squares-ai-proof/03-theorem.webp)
*논문의 주정리 Theorem 1.1 — 출처: arXiv*

주정리는 이 추측이 최소제곱 문제에서는 맞다고 증명합니다. 어떤 무작위 다항 시간 알고리즘도 2/3 이상의 확률로 아래 두 조건을 함께 만족하는 해를 구할 수 없다는 내용이에요.

**‖Ax − b‖² ≤ (최적 k개 해의 오차) + ε**

**s ≤ C · k · κ¹⁻ᵞ**

여기서 s는 알고리즘이 쓴 변수 개수예요. 다만 증명은 **조건부**입니다. 그래프를 다루는 **작은 집합 확장 가설(Small-Set Expansion Hypothesis)**이 참이라는 전제가 붙어요. 이 가설은 그래프에서 바깥과 연결이 적은 작은 부분집합이 있는지 없는지를 다항 시간에 구분할 수 없다는 미증명 가설이고, Unique Games 추측과 관련된 연구에서 나왔습니다.

증명 방식은 환원(reduction)이에요. 가설에서 어렵다고 보는 그래프 문제를 최소제곱 문제로 환원하고, 만약 추측보다 적은 변수로 푸는 알고리즘이 있으면 그 그래프 문제도 해결할 수 있다는 걸 보여 모순을 도출합니다. 그래프의 각 연결선이 행렬 A의 한 줄이 되기 때문에, 어려운 예시는 **한 줄에 0이 아닌 값이 두 개 이하**인 단순한 행렬이에요. 계수가 유리수이고 A가 완전 열 랭크(full column rank)인 경우에도 결론이 성립합니다.

## AI가 한 일과 사람이 한 일

![감사의 글의 AI 기여 문장](/assets/images/math/sparse-least-squares-ai-proof/04-acknowledgements.webp)
*감사의 글의 AI 기여 문장 — 출처: arXiv*

논문은 기여를 두 곳에 적었어요. 초록과 감사의 글이 같은 문장으로 시작하고, 감사의 글에는 한 구절이 더 추가됩니다.

| 주체 | 논문에 적힌 일 |
| :--- | :--- |
| Gemini 기반 에이전트 | <mark>증명을 처음 찾음 (완전 자동)</mark> |
| 저자 3명 | 증명 검증 |
| 저자 3명 | 읽기 좋게 편집 |
| 저자 3명 | **최종본에 책임** |

에이전트가 무엇이었는지는 이 논문에 나오지 않아요. 같은 저자들이 9월 15일 arXiv에 올린 *Stellar Colosseum* 논문이 관련 정보를 제공합니다. 이 논문은 수학·이론 컴퓨터과학 연구용 다중 에이전트 작업 틀을 소개하면서, 이 작업 틀이 기여한 연구 결과 다섯 가지 중 하나로 이 하한 증명을 포함했어요.

![Stellar Colosseum의 단계별 연구 흐름](/assets/images/math/sparse-least-squares-ai-proof/05-colosseum-workflow.webp)
*Stellar Colosseum의 단계별 연구 흐름 — 출처: arXiv*

Colosseum은 증명 전략 탐색, 준비도 판정, 증명을 절 단위로 나누기, 절별 풀이, 전체 검증의 다섯 단계로 진행돼요. 단계마다 후보 답안을 여러 개 만들고, 반례를 찾는 반박 역할이 각 후보를 검증하고, 통과한 후보를 통합합니다. 저자들은 Gemini 3.1 Pro로 이 틀을 실행했고, FOCS·STOC·SODA 논문에서 뽑은 연구 수준 정리 증명 벤치마크 TCS-Bench에서 정답률 71.0%를 기록했다고 밝혔어요.

문제를 고른 것, 증명이 맞는지 확인한 것, 논문으로 내고 책임지는 것은 사람이 담당했어요. 반대로 증명의 핵심 아이디어를 찾는 단계는 사람이 개입하지 않았다는 것이 논문 문장의 뜻입니다.

## 저자가 적은 범위와 한계

논문은 한계를 따로 한 절로 적지 않았어요. 대신 본문이 결과의 범위를 분명히 정해 둡니다.

- 증명은 작은 집합 확장 가설을 전제로 한 조건부 결과
- 대상은 최소제곱 목표 함수, 추측 원문은 희소 볼록 최적화 전반
- 하한이 적용되는 대상은 다항 시간 알고리즘, 지수 시간 알고리즘은 해당 없음
- 최악의 경우 하한이라 실제 데이터에서 알고리즘이 잘 되는 경우와는 무관

여기부터는 이 글의 관점이에요. 증명이 동료 심사를 거치지 않았고, AI가 찾은 증명이라는 사실이 검증 부담을 줄여 주지도 않습니다. Colosseum 논문도 긴 증명에서는 앞 단계의 오류가 후속 단계로 전파될 수 있다는 점을 작업 틀을 설계한 이유로 적었어요.

## 국내 접점

이 논문에 국내 연구진은 참여하지 않았어요. 실무 쪽 접점은 희소 회귀 자체입니다. 유전체 분석, 금융 위험 요인 선택, 추천 모델 특징 선택처럼 국내 기업·연구소가 변수 수천 개 중 일부만 선택하는 작업에 LASSO·OMP 같은 기법을 쓰는데, 이 결과는 그 알고리즘들이 최악의 경우 κ에 비례해 변수를 더 선택하는 성질을 다항 시간 안에서는 피할 수 없다는 주장에 근거를 추가합니다.

## 앞으로 확인할 사항

- 학회·학술지 심사 통과와 외부 검증
- 최소제곱 밖의 희소 볼록 최적화로 결과의 적용 범위가 확대되는지
- 작은 집합 확장 가설 없이 같은 하한을 증명하는 결과가 발표되는지
- Colosseum이 기여한 나머지 네 결과의 심사 결과

## 참고 출처

- [[arXiv] Lin·Mirrokni·Woodruff, The Condition-Number Barrier in Sparse Least Squares, arXiv:2608.02588 (2026-08-03, 본문 이미지 3점 출처)](https://arxiv.org/abs/2608.02588)
- [[arXiv] Lin·Woodruff 외, Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science, arXiv:2609.15983 (2026-09-15, 본문 이미지 1점 출처)](https://arxiv.org/abs/2609.15983)
- [[Journal of Machine Learning Research] Axiotis·Sviridenko, Sparse convex optimization via adaptively regularized hard thresholding, 22(122), 2021 (추측 27 원문)](https://jmlr.org/papers/v22/20-661.html)
