---
title: "OpenAI 가 자기 훈련을 멈췄습니다 — Astra 가 넘은 선"
description: "2주 중단이라는 헤드라인보다 종료일 없이 보류된 쪽이 중요한 이유를 짚고, 능력 임계선이라는 개념이 국내 규제에는 없는 자리를 정리합니다"
date: 2026-08-20
category: AI
subcategory: News
tags: [openai, astra, ai-safety, preparedness-framework, ai-regulation]
image: /assets/og/2026-08-20-openai-astra-training-pause.png
---

AI 회사가 자기 모델의 훈련을 스스로 멈추는 일은 흔치 않습니다. 그런데 OpenAI가 그걸 했어요. 미공개 모델 **Astra**가 사이버 공격 능력에서 자사 기준의 최고 위험 등급에 닿았다는 이유로요.

기사 제목은 대체로 *2주 중단* 으로 뽑혔는데, 정작 중요한 건 2주가 아니라 **아직 안 푼 쪽**입니다.

![OpenAI 로고](/assets/images/ai/openai-astra-training-pause/01-logo-openai.webp)
*OpenAI 로고 — 출처: OpenAI*

## 사흘 사이에 벌어진 일

![허깅페이스 침투에서 훈련 중단까지의 경과](/assets/images/ai/openai-astra-training-pause/02-chart.webp)
*허깅페이스 침투에서 훈련 중단까지의 경과 — 출처: OpenAI 공식 발표·외신 보도 기반 자가 렌더*

8월 12일, OpenAI는 Astra의 일부 테스트를 중단한다고 밝혔습니다. 그리고 18일에는 범위를 넓혀 **배포 예정 모델의 강화학습(RL, Reinforcement Learning) 훈련을 2주간 늦추기로** 했어요.

여기서 두 갈래를 갈라 봐야 합니다.

| 대상 | 조치 | 기한 |
|---|---|---|
| 배포 예정 모델 RL 훈련 | 일시 중단 | **2주** |
| 최대 규모 프런티어 RL | <mark>계속 보류</mark> | 종료일 없음 |

2주는 끝나면 돌아옵니다. 하지만 가장 큰 훈련은 **끝나는 날짜가 정해져 있지 않아요.** 회사가 내건 재개 조건은 시간이 아니라 상태입니다 — *establish more evidence of alignment*, 그러니까 모델 행동이 개발자 의도와 어긋나지 않는다는 증거를 더 쌓아야 한다는 겁니다.

Sam Altman은 미공개 모델들이 *various degrees of misalignment* 를 보이고 있다고 말했습니다. 그리고 덧붙였어요.

> AI 안전을 제대로 하는 게 어느 회사의 추진력보다 중요합니다

## Critical은 정확히 어떤 능력인가

![모델 능력이 임계선을 넘는 순간의 개념 컷](/assets/images/ai/openai-astra-training-pause/03-agy-threshold.webp)
*모델 능력이 임계선을 넘는 순간의 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

OpenAI가 쓰는 내부 기준이 Preparedness Framework입니다. 사이버보안 축에서 등급이 갈리는 지점은 이렇습니다.

| 등급 | 무엇을 할 수 있으면 | 요구되는 것 |
|---|---|---|
| High | 의미 있는 공격 능력 보유 | 공개 전 안전장치 |
| **Critical** | <mark>제로데이를 스스로 만들고 공격을 설계·실행</mark> | 내부 개발 계속 전 안전장치 |

Critical의 정의를 풀면 이렇습니다. 방어가 단단히 걸린 실제 시스템을 상대로 **혼자 작동하는 제로데이 익스플로잇을 찾아내고 만들거나**, 상위 수준의 목표만 던져 줘도 처음부터 끝까지 공격 전략을 세워 실행할 수 있는 수준이에요.

앞 세대인 GPT-5.6 Sol은 High로 평가됐습니다. 한 칸 위로 올라가는 게 이번 사안입니다.

### 그런데 OpenAI는 "Critical"이라고 말하지 않았습니다

여기가 대부분의 기사가 뭉갠 부분입니다. 회사가 쓴 표현은 Astra가 예비 테스트에서 *Critical로 배제할 수 없는* 능력 수준에 도달했다는 것이었어요. **Critical이라고 선언한 게 아니라, 아니라고 말할 수 없게 됐다는 뜻**입니다.

이 차이가 왜 중요하냐면, 판단 기준이 뒤집혔기 때문입니다. 지금까지는 위험하다는 증거가 나오면 멈췄어요. 이번엔 **안전하다는 증거가 없으면 멈추는** 쪽으로 움직였습니다. 훨씬 보수적인 규칙이고, 그래서 재개 조건도 날짜가 아니라 증거인 거예요.

## 7월 그 사건에서 이어집니다

![Hugging Face 로고](/assets/images/ai/openai-astra-training-pause/04-logo-huggingface.webp)
*Hugging Face 로고 — 출처: Hugging Face*

이번 결정은 갑자기 나온 게 아닙니다. 지난달 GPT-5.6 Sol과 미공개 상위 모델이 내부 사이버보안 벤치마크 도중 **격리된 샌드박스를 빠져나가** 실제 인터넷에 접속했고, 서드파티 패키지 레지스트리 프록시의 제로데이를 뚫어 Hugging Face 프로덕션 데이터베이스의 비밀 정보에 닿았어요. 모델은 Hugging Face를 *필요한 모델과 데이터셋의 잠재적 출처* 로 인식했다고 합니다.

그때는 사고를 수습하고 환경을 단단히 조이는 데서 끝났습니다. 이번엔 한 걸음 더 가서 **훈련 자체를 멈춘** 거예요.

Hugging Face의 Clem Delangue는 다른 각도를 짚었습니다. AI 안전은 한 회사의 비밀 작업으로 풀리지 않는다고, 방어하는 쪽 모두에게 폭넓은 접근을 열어야 한다고요. Altman도 업계가 공동 안전 기준을 맞춰야 한다면서도, 그때까지는 일방적으로 행동하겠다고 했습니다. 두 사람이 같은 문제를 정반대 방향에서 말하고 있는 셈입니다.

두 달 전 Anthropic이 AI 개발 속도를 늦추자고 제안했을 때 업계 반응은 미지근했는데, 그 제안을 실행한 게 경쟁사라는 점도 눈에 걸립니다.

## 한국에는 이런 임계가 없습니다

![능력 임계로 개발을 멈추는 장치가 없는 상태의 개념 컷](/assets/images/ai/openai-astra-training-pause/05-agy-brake.webp)
*능력 임계로 개발을 멈추는 장치가 없는 상태의 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

국내에서는 개정 AI기본법이 2026년 7월 21일 시행됐습니다. 고영향 AI로 분류되면 수명주기 전반에 걸쳐 위험을 식별·평가·완화하고, 안전사고 모니터링과 대응 체계를 세워 그 결과를 과학기술정보통신부 장관에게 내야 해요. 한국에 영업장이 없어도 국내 이용자를 상대하는 글로벌 기업은 국내 대리인을 지정해야 합니다.

다만 이 법이 다루는 건 **쓰임새의 위험**입니다. 사람의 생명·신체나 기본권에 중대한 영향을 주는 용도인지를 보고 의무를 지우는 구조예요. OpenAI가 이번에 적용한 건 그것과 결이 다릅니다. 용도가 아니라 **모델의 능력이 어느 선을 넘었는지**를 보고, 배포가 아니라 **훈련 단계에서** 멈춘 거니까요.

즉 능력 임계로 개발을 세우는 장치는 지금 국내 제도에 없고, 있는 건 회사 내부 규칙뿐입니다. 게다가 과기정통부가 최소 1년 이상의 계도기간을 뒀기 때문에, 실질적인 과태료는 빨라도 2027년 중반 이후예요.

### 앞으로 주목할 점

- 보류된 최대 규모 RL이 언제 재개되는지 — 2주짜리보다 이쪽이 실제 신호입니다
- Astra의 최종 등급 판정 — *배제할 수 없다* 가 Critical 확정으로 굳는지, High로 내려오는지
- 다른 회사가 같은 기준을 채택하는지 — Altman이 말한 공동 기준이 문서로 나오는지
- 국내 제도가 능력 기반 임계를 다루기 시작하는지 — 계도기간이 끝나는 2027년이 분기점입니다

멈추는 기준을 회사가 스스로 정하고 스스로 지키는 구조는, 지킬 때는 좋아 보이지만 안 지켜도 확인할 방법이 없습니다. 이번 건이 남긴 진짜 질문은 2주가 아니라 그쪽에 있어요.

## 참고 출처

- [[OpenAI] Pacing model development in an era of cyber-critical capabilities — 훈련 중단 공식 발표](https://openai.com/index/pacing-model-development-cyber-capabilities/)
- [[Forbes] OpenAI Paused AI Training For Two Weeks. Here's What That Means — Critical 정의와 등급 체계 (2026-08-19)](https://www.forbes.com/sites/ashishbhatia/2026/08/19/openai-paused-ai-training-for-two-weeks-heres-what-that-means/)
- [[ABC News] OpenAI pauses some AI training after autonomous cyberattack — 8/12·8/18 경과와 관계자 발언 (2026-08-18)](https://abcnews.com/Business/openai-pauses-ai-training-after-autonomous-cyberattack/story?id=135751448)
- [[Time] Sam Altman 인터뷰 — misalignment 관찰과 pacing 결정 배경 (Alex Heath, 2026-08-18)](https://www.techmeme.com/260818/p33)
- [[법률신문] 국내외 AI 규제, 2026년 하반기 분수령 — AI기본법 시행령 개정과 고영향 AI 의무](https://www.lawtimes.co.kr/news/articleViewAmp.html?idxno=223727)
