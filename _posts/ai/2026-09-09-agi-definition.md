---
title: "AGI 는 무엇인가 — 왜 아무도 같은 뜻으로 쓰지 않나"
description: "AGI 도달을 두고 기사가 서로 어긋나는 이유를 회사·계약·법마다 다른 정의로 풀고, 도달 시점 전망이 갈리는 까닭을 정리합니다"
date: 2026-09-09
category: AI
subcategory: Explainer
tags: [agi, google-deepmind, openai, ai-regulation, ai-definition]
image: /assets/og/2026-09-09-agi-definition.png
---

AGI라는 말이 하루에도 몇 번씩 나옵니다. 어떤 기사는 이미 도달했다고 하고, 어떤 기사는 아직 멀었다고 해요.

둘 다 틀리지 않았을 수 있습니다. **AGI에는 합의된 정의가 없어서**, 서로 다른 기준으로 재고 있기 때문입니다.

![같은 대상을 서로 다른 자로 재는 장면](/assets/images/ai/agi-definition/01-agy-hero.webp)
*같은 대상을 서로 다른 자로 재는 장면 — 출처: 개념 컷 · agy 자가 생성*

## 정의가 회사마다 다릅니다

AGI는 Artificial General Intelligence, 우리말로 범용 인공지능입니다. 특정 작업만 잘하는 게 아니라 사람이 하는 지적 작업 전반을 해낸다는 뜻으로 쓰여요.

문제는 「전반」과 「해낸다」를 어디서 끊느냐입니다. 회사마다, 심지어 회사끼리 맺는 계약마다 조작적 정의가 달라서, 「AGI에 도달했나」를 두고 벌어지는 논쟁이 깔끔하게 끝나는 일이 드뭅니다.

그래서 정의를 단계 기준으로 바꾸려는 시도가 나왔습니다. 대표적인 것이 둘인데, 축이 서로 다릅니다.

## DeepMind는 깊이와 폭으로 나눕니다

Google DeepMind 연구진이 2023년 11월에 내놓고 ICML 2024에 실은 *Levels of AGI for Operationalizing Progress on the Path to AGI*가 출발점이고, DeepMind 공동 창업자인 셰인 레그(Shane Legg)가 공저자로 참여했습니다.

이 틀의 요점은 능력을 **깊이(성능)와 폭(일반성)** 두 축으로 나눈 것입니다. 성능은 단계로 세고, 그 능력이 좁은 영역에만 걸리는지 전반에 걸리는지는 별도 축으로 봅니다.

| 단계 | 이름 | 기준 |
|---|---|---|
| 1 | Emerging | 미숙련자 수준 |
| 2 | Competent | 상위 50% |
| 3 | Expert | 상위 10% |
| 4 | Exceptional | <mark>상위 1%</mark> |
| 5 | Superhuman | 모든 사람 상회 |

여기에 **자율성을 따로 둔 것**이 이 틀의 두 번째 요점입니다. 능력이 높다고 스스로 움직이는 것은 아니어서, 사람이 도구로 쓰는 단계부터 완전 자율까지를 별도 단계로 셉니다. 능력과 독립성을 섞어 재면 위험 평가가 어긋난다는 이유예요.

정의가 계속 움직인다는 점은 논문 개정판에서 4단계 이름이 Virtuoso에서 Exceptional로 바뀐 데서도 드러납니다.

## OpenAI는 하는 일로 나눕니다

OpenAI가 쓰는 내부 틀은 축이 다릅니다. 능력의 높이가 아니라 **무엇을 하는 존재인가**로 다섯 단계를 나눠요.

| 단계 | 이름 | 하는 일 |
|---|---|---|
| 1 | Chatbots | 대화 |
| 2 | Reasoners | 문제 해결 |
| 3 | Agents | <mark>대신 실행</mark> |
| 4 | Innovators | 새 발견 |
| 5 | Organizations | 조직 운영 |

이 틀은 논문이 아니라 보도로 알려진 것이라, DeepMind 쪽처럼 공개된 기준표가 있는 것은 아닙니다. 회사가 밝힌 자체 평가로는 추론 모델 계열에서 2단계에 도달했고 3단계로 넘어가는 중이라고 했어요.

두 틀을 같은 모델에 대 보면 답이 다르게 나옵니다. DeepMind 쪽은 「어느 정도로 잘하나」를 묻고, OpenAI 쪽은 「무엇까지 맡기나」를 묻기 때문입니다.

## AGI 도달 시점 전망이 엇갈리는 까닭

샘 올트먼과 다리오 아모데이 계열은 2026년 말에서 2027년 초를 말해 왔고, 데미스 하사비스와 셰인 레그 계열은 2028~2030년에 50% 확률을 둡니다.

이 간격을 낙관과 비관의 차이로만 읽으면 절반만 본 것입니다. **무엇을 AGI라고 부르기로 했는지가 다르면** 같은 모델을 놓고도 도달 여부가 갈려요.

- 경제적으로 유용한 작업 대부분을 해내면 AGI인가
- 사람 없이 스스로 목표를 세워야 AGI인가
- 새로운 과학 발견을 내놔야 AGI인가

세 기준은 도달 시점이 몇 년씩 벌어집니다. 그래서 전망을 읽을 때는 연도보다 **그 사람이 쓰는 정의**를 먼저 봐야 합니다.

## 규제는 AGI라는 말을 쓰지 않습니다

2026년 1월 22일 시행된 인공지능 기본법에는 AGI라는 범주가 없어요. 대신 고영향 인공지능, 생성형 인공지능, 고성능 인공지능으로 나눠 의무를 부과합니다.

고성능 인공지능의 기준은 능력이 아니라 **누적 학습 연산량**입니다.

| 규제 | 기준 연산량 |
|---|---|
| 한국 AI 기본법 고성능 AI | <mark>10²⁶ FLOPs 이상</mark> |
| EU AI Act 체계적 위험 | 10²⁵ FLOPs 이상 |

한국 기준이 EU의 열 배입니다. 같은 성격의 규제인데 문턱이 한 자릿수 갈리는 것이라, 어느 모델이 규제 대상에 들어가는지가 관할에 따라 달라져요.

![규제가 능력 대신 연산량으로 선을 긋는 장면](/assets/images/ai/agi-definition/02-agy-threshold.webp)
*규제가 능력 대신 연산량으로 선을 긋는 장면 — 출처: 개념 컷 · agy 자가 생성*

능력은 합의가 안 되지만 연산량은 셀 수 있습니다. 규제가 능력 수준 대신 투입된 연산량으로 기준을 세운 것은 이 차이 때문이고, 그래서 AGI 논쟁과 무관하게 법이 먼저 작동할 수 있습니다.

[AI 와 법 (2) — 오픈소스면 규제 무관? EU AI Act 는 다릅니다](/posts/ai-law-02-eu-ai-act-open-source/)

![글 끝 정리](/assets/images/ai/agi-definition/03-items.webp)
*글 끝 정리 — 출처: 본문 정리 · 자가 렌더*

## 기사를 읽을 때 확인할 것

「AGI에 도달했다」는 문장을 만나면 세 가지를 확인하면 됩니다.

- 누구의 정의를 쓰고 있나
- 능력을 말하나, 자율성을 말하나
- 어느 범위의 작업을 근거로 삼았나

셋이 안 적혀 있으면 그 문장은 검증할 수 있는 주장이 아니라 표현입니다. 반대로 셋이 적혀 있으면 동의하지 않더라도 무엇을 두고 다투는지는 분명해집니다.

## 참고 출처

- [[arXiv] Levels of AGI for Operationalizing Progress on the Path to AGI (DeepMind 성능·일반성·자율성 축, ICML 2024)](https://arxiv.org/abs/2311.02462)
- [[Google DeepMind] Levels of AGI 연구 페이지 (논문 소개와 저자)](https://deepmind.google/research/publications/66938/)
- [[법률신문] AI 기본법 시행과 그 시사점 (2026-01-22 시행·고영향·생성형·고성능 구분)](https://www.lawtimes.co.kr/news/articleView.html?idxno=216500)
- [[디지털데일리] AI 기본법이 정의한 고성능 AI 기준, 10의 26제곱이 뭐길래 (연산량 기준·EU 비교)](https://m.ddaily.co.kr/page/view/2025100221471816780)
- [[Bloomberg / Yahoo Finance] OpenAI scale ranks progress toward human-level problem solving (OpenAI 5단계 내부 틀)](https://finance.yahoo.com/news/openai-develops-system-track-progress-194820951.html)
