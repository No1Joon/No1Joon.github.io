---
title: "모델 증류는 왜 공격이 되나 — 하루 300만 건을 빼 간 방식"
description: "10년 넘게 쓰인 정상 기법인 증류가 허가·규모·대상에 따라 공격으로 바뀌는 지점을 Anthropic 이 적발한 사례로 정리합니다"
date: 2026-09-11
category: AI
subcategory: Explainer
tags: [model-distillation, knowledge-distillation, anthropic, ai-security, chain-of-thought]
image: /assets/og/2026-09-11-model-distillation-attack.png
---

AI 모델을 만들 때 쓰는 증류(distillation)는 10년 넘게 쓰인 정상 기법입니다. 그런데 Anthropic은 9월 10일 보고서에서 중국 AI 연구소 7곳의 증류를 공격이라고 불렀어요.

Alibaba 쪽 한 캠페인은 하루 최대 약 300만 건씩 Claude의 추론 과정을 빼 갔습니다. 같은 기법이 공격으로 바뀌는 지점은 허가, 규모, 그리고 무엇을 빼 가느냐에 있어요.

![증류 원 논문 Distilling the Knowledge in a Neural Network 첫 장](/assets/images/ai/model-distillation-attack/01-hero.webp)
*증류 원 논문 Distilling the Knowledge in a Neural Network 첫 장 — 출처: arXiv / Hinton, Vinyals, Dean (2015)*

## 증류는 원래 정상 기법이다

증류라는 이름은 2015년 Geoffrey Hinton·Oriol Vinyals·Jeff Dean의 논문 *Distilling the Knowledge in a Neural Network*에서 굳었습니다. 여러 모델을 함께 돌려야 나오던 성능을, 배포하기 쉬운 모델 하나로 옮기는 방법이었어요.

크고 성능 좋은 교사(teacher) 모델에 입력을 넣어 답을 받고, 그 답을 정답 삼아 작은 학생(student) 모델을 학습시킵니다. 학생 모델은 정답 한 개가 아니라 교사가 여러 후보에 매긴 확률까지 따라 배워서, 같은 데이터로 처음부터 학습할 때보다 적은 자원으로 비슷한 성능에 가까워져요.

![교사 모델과 학생 모델 공식 도식](/assets/images/ai/model-distillation-attack/02-photo.webp)
*교사 모델과 학생 모델 공식 도식 — 출처: Anthropic*

지금도 AI 회사들은 자기 큰 모델을 증류해 가볍고 빠른 모델을 만듭니다. Anthropic 보고서도 증류 자체는 정당한 학습 방법이라는 전제에서 시작해요.

## 불법 증류는 어디서 갈리나

Anthropic은 불법 증류를 허가 없이 남의 모델 역량을 산업 규모로 몰래 뽑아 다른 모델에 복제하는 캠페인이라고 정의했습니다. 대개 사기 수단이 동원된다고 덧붙였어요.

| 구분 | 정상 증류 | 불법 증류 |
| :--- | :--- | :--- |
| 교사 모델 | 내 모델·허가받은 모델 | 남의 상용 모델 |
| 접근 방식 | 정상 계정·계약 | 위장 계정·도난 카드·도난 키 |
| 규모 | 필요한 만큼 | <mark>하루 수백만 건</mark> |
| 안전장치 | 함께 설계 | **복제본에는 없음** |

![불법 증류 캠페인 4단계 공식 도식](/assets/images/ai/model-distillation-attack/03-photo.webp)
*불법 증류 캠페인 4단계 공식 도식 — 출처: Anthropic*

접근 경로는 주로 중계 서비스였습니다. 중국에서 transfer station으로 불리는 이 서비스들이 가짜 신원과 도난 카드로 계정 수천 개를 만들어 이용 지역 제한을 우회했고, 정상 기업이나 개인에게서 훔친 API 키도 썼어요.

중계 서비스는 두 번째 수익원도 만들었습니다. 이용자가 모르는 사이 대화를 저장해 두었다가 다른 연구소에 팔았어요. SenseTime은 이렇게 사들인 대화를 증류에 썼고, MiniMax는 관계를 숨긴 위장 회사(shell company)로 Anthropic·OpenAI 모델만 제공하는 중계 서비스를 직접 차렸다고 보고서는 적었습니다.

## 얼마나 빼 갔나

Anthropic은 2월 23일 첫 공개에서 DeepSeek·Moonshot·MiniMax가 위장 계정 약 2만 4,000개로 Claude와 1,600만 건 넘게 주고받았다고 밝혔습니다. 그중 MiniMax가 1,300만 건 이상이었어요.

9월 보고서는 그 뒤로 중국 연구소 7곳을 더 적발했다고 밝혔습니다. Alibaba·Moonshot·DeepSeek·Zhipu·Xiaomi·SenseTime·MiniMax이고, 모두 일반에 공개된 모델을 노렸어요.

![Anthropic이 밝힌 업체별 증류 교환 건수](/assets/images/ai/model-distillation-attack/04-chart.webp)
*Anthropic이 밝힌 업체별 증류 교환 건수 — 출처: Anthropic 위협 보고서 기반 자가 렌더*

가장 큰 건 Alibaba였습니다. 5~7월에 1억 5,100만 건이 넘었고, 한창때는 위장 계정 3,500여 개로 하루 300만 건 가까이 보냈어요. Opus 4.6·4.7의 추론 과정을 노렸고, 그 결과물이 Qwen 3.5·3.6·3.7 학습에 쓰였다고 보고서는 밝혔습니다.

Alibaba는 처음에 주거용 프록시·일회용 이메일·가상 카드로 만든 계정 5,000개 가까이를 돌렸습니다. Anthropic이 이 묶음을 막자 곧바로 두 번째 계정 묶음으로 옮겨 갔어요. 표적은 에이전트 작업, 소프트웨어 엔지니어링, 커널 개발, 장기 과제였습니다.

## 추론 과정을 뽑아내는 방식

증류하는 쪽이 가장 원하는 건 최종 답이 아니라 그 앞의 사고 과정, 즉 chain-of-thought 전사본입니다. 이 전사본이 있으면 SFT(지도 미세조정) 데이터로 바로 바꿀 수 있어요.

### 사고 과정을 쓰게 만들기

Alibaba는 요청마다 고정 지시를 넣어 Claude가 답하기 전에 사고 과정을 태그 안에 적게 했습니다. 그 전사본을 모아 학습 데이터로 바꿨어요.

### 서명을 원문으로 되돌리기

Claude는 증류를 막으려고 원래 사고 과정 대신 참조용 thinking signature를 돌려줍니다. Moonshot과 DeepSeek은 이 서명을 저장했다가 새 세션에서 원래 사고 과정으로 풀어내게 했고, Anthropic은 이를 cross-session replay 공격으로 불렀어요.

### 자사 이용자 요청을 몰래 중계하기

Moonshot은 자사 Kimi를 쓰는 고객 요청을 몰래 Claude로 넘기고 그 답을 Kimi의 답인 것처럼 보여 줬습니다. 열흘 동안 약 30만 건을 넘겼고 대부분 Opus로 갔어요. DeepSeek도 Claude Code 같은 코딩 도구로 들어온 이용자를 골라 요청을 Claude로 넘겼습니다.

![사용자 요청을 몰래 다른 모델로 중계하는 개념](/assets/images/ai/model-distillation-attack/05-agy.webp)
*사용자 요청을 몰래 다른 모델로 중계하는 개념 — 출처: 개념 컷 · agy 자가 생성*

Zhipu는 처음에 Anthropic의 Fable을 노렸지만 강화된 사이버 안전장치에 막히자 포기했어요. 이후 안전장치가 약하다고 판단한 Opus 4.6과 다른 회사 모델로 옮겨 갔다고 보고서는 적었습니다.

## 왜 공격으로 보나

첫째, 안전장치가 따라가지 않습니다. Claude가 위험한 요청을 거절하도록 만든 장치는 복제된 모델에 옮겨지지 않아요. Anthropic은 자체 연구에서 증류된 모델이 생물·사이버 분야의 위험한 역량을 얻을 수 있었고, 수집한 대화에 그 분야 내용이 거의 없어도 그랬다고 밝혔습니다.

둘째, 이용자 데이터가 함께 샜습니다. Moonshot·DeepSeek·Xiaomi가 Claude로 넘긴 요청에는 이름·이메일·회사 데이터가 들어 있었고, 일부에는 실제로 쓰이는 API 자격 증명까지 있었어요. 미국·유럽 이용자가 흔히 쓰는 제3자 모델 라우터를 거친 요청도 섞여 있었습니다.

해외 모델을 중계 서비스나 제3자 라우터로 쓰는 개발자라면 같은 위험에 놓입니다. 코딩 도구 설정에 넣은 키와 붙여넣은 코드가 그 경로에서 저장되고 팔릴 수 있다는 것이 이번 보고서로 확인됐어요.

[Anthropic 위협 보고서 — 연애앱 상대 4분의 3이 AI 였다](/posts/anthropic-threat-report-romance-scam/)

국내에서도 모델의 출처는 이미 평가 기준입니다. 과기정통부는 2월 브리핑에서 독자 AI 파운데이션 모델의 독자성 기준에 처음부터 학습한 기록을 넣었어요. 그때 논란이 된 건 가중치 재사용이라 출력으로 베끼는 증류와는 다르지만, 남의 모델에 기댄 부분을 따지는 흐름은 같습니다.

[보안 특화 국산 AI, 네이버클라우드 컨소시엄 선정 — 700B 모델을 방어용·공격용 둘로](/posts/naver-lg-security-ai-model/)

Anthropic의 대응은 겹겹이 막는 방식입니다. 메타데이터로 중계망 계정을 찾아 개별 계정이 아니라 배후 조직 단위로 제재하고, 추출을 잡는 전용 분류기를 Fable 5 출시에 맞춰 강화했어요. 답하기 전 사고 과정을 요약해서 넘기도록 바꿔, 훔친 전사본의 학습 가치도 떨어뜨렸습니다.

![정리](/assets/images/ai/model-distillation-attack/06-items.webp)
*정리 — 출처: Anthropic 보고서 기반 정리 · 자가 렌더*

이용자 쪽에서 할 수 있는 건 해외 모델을 공식 API나 정식 판매처로 쓰는 것, 그리고 중계 서비스에 자격 증명을 넣지 않는 것입니다. 증류 공방은 앞으로도 이어지겠지만, 내 대화가 학습 데이터로 넘어가는 경로는 이용자가 끊을 수 있어요.

## 참고 출처

- [[Anthropic] Detecting and countering misuse of AI: September 2026 (2026-09-10 보고서 원문, 증류 사례·대응, 본문 이미지 2점 출처)](https://www.anthropic.com/threat-intelligence-report-september-2026)
- [[Anthropic] Detecting and preventing distillation attacks (2026-02-23 첫 공개, 계정·교환 규모)](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks)
- [[arXiv] Hinton, Vinyals, Dean, Distilling the Knowledge in a Neural Network (2015, 본문 이미지 1점 출처)](https://arxiv.org/abs/1503.02531)
- [[대한민국 정책브리핑] 독자AI파운데이션모델 추가 발표 브리핑 (2026-02-20, 독자성 기준)](https://www.korea.kr/briefing/policyBriefingView.do?newsId=156745273)
