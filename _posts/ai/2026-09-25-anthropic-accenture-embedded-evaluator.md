---
title: "Anthropic 내장 평가자 1호는 Accenture — 정해진 것과 남은 것"
description: "직원급 접근 권한을 받는 내장 평가자 제도의 첫 계약 내용과, 독립성 논란·아직 정하지 않은 운영 방식을 정리합니다"
date: 2026-09-25
category: AI
subcategory: News
tags: [anthropic, accenture, embedded-evaluation, ai-safety, ai-governance]
image: /assets/og/2026-09-25-anthropic-accenture-embedded-evaluator.png
---

Anthropic이 2026년 9월 18일 Accenture를 첫 **내장 평가자**(embedded evaluator)로 정했습니다. 두 회사가 이 분야 역량을 키우는 데 향후 5년 동안 각자 최소 약 1조 4,000억 원(10억 달러)을 쓸 계획이에요.

내장 평가자는 회사 밖에서 완성된 모델을 받아 시험하는 기존 외부 평가와 달리, Anthropic 안에서 직원에 준하는 접근 권한을 받고 일합니다. 다리오 아모데이(Dario Amodei) CEO가 9월 12일 에세이에서 속도 조절 1단계로 제시한 약속이 조직 형태로 처음 구현된 것인데, 발표문도 세부 운영 방식은 아직 정하는 중이라고 적었어요.

![Anthropic 발표 대표 이미지](/assets/images/ai/anthropic-accenture-embedded-evaluator/01-hero-anthropic.webp)
*Anthropic 발표 대표 이미지 — 출처: Anthropic*

[아모데이의 AI 속도 조절 제안 — 이번엔 경쟁사도 동의했습니다](/posts/amodei-pace-the-frontier/)

## 발표 내용

![Faculty 로고](/assets/images/ai/anthropic-accenture-embedded-evaluator/02-logo-faculty.webp)
*Faculty 로고 — 출처: Faculty*

평가 업무는 Accenture의 AI 전문 사업부 Faculty가 담당합니다. Faculty는 영국 AI 회사로 Accenture가 2026년 1월 인수했고, 코로나19 때 영국 국민보건서비스(NHS) 조기 경보 시스템을 만든 이력이 있어요. Faculty CEO 마크 워너(Marc Warner)가 Accenture 최고기술책임자를 겸합니다.

- 수행 업무: 모델 평가와 레드팀, 정렬(alignment) 평가, 안전장치 시험
- 접근 수준: 직원에 준하는 권한, 학습 중인 모델 관찰, 직원 직접 면담
- 투자: Anthropic과 Accenture가 각자 5년간 최소 약 1조 4,000억 원(10억 달러)
- 비용 부담: Accenture의 평가 업무는 Anthropic이 직접 지급
- 배타성: 없음, Anthropic은 다른 평가자를 추가 발표하고 Accenture도 다른 AI 개발사와 같은 일을 할 수 있음

Anthropic은 METR 등 비영리 평가 기관과도 내장 평가 일부를 시범 운영하는 논의를 하고 있고, 이쪽은 각 기관이 자체 자금으로 참여하는 방식이에요. 발표문은 내장 평가가 회사의 책임을 덜어 주는 장치가 아니라 그 책임을 검증 가능하게 만드는 것이며, 모델 안전의 책임은 계속 Anthropic에 있다고 적었습니다.

## 기존 외부 평가와의 차이

![METR 로고](/assets/images/ai/anthropic-accenture-embedded-evaluator/03-logo-metr.webp)
*METR 로고 — 출처: METR*

| 구분 | 기존 외부 평가 | 내장 평가 |
| :--- | :--- | :--- |
| 일하는 곳 | 회사 밖 | **회사 안** |
| 보는 대상 | 출시 전 모델 | 학습 중인 모델까지 |
| 의사결정 관찰 | 불가 | <mark>개발·배포 결정 추적</mark> |
| 직원 면담 | 제한적 | 직접 면담 |
| 사고 보고 | 계약 범위 안 | 보고·대외 설명 가능 |

지금까지 프런티어 모델의 외부 평가는 출시 전 모델에 대한 사전 접근이 중심이었습니다. 영국 AI안전연구소가 Anthropic과 2025년 2월 협약을 맺고 미공개 모델을 미리 시험한 것, METR가 출시 전 모델을 받아 자율 작업 능력을 측정해 온 것이 대표 사례예요. 내장 평가는 결과물이 아니라 모델이 만들어지는 과정과 그 과정을 정하는 회사의 결정을 관찰한다는 점이 다릅니다.

## 에세이의 약속과 이번 발표

![AI 연구소 안에서 일하는 내장 평가자 개념 컷](/assets/images/ai/anthropic-accenture-embedded-evaluator/04-agy.webp)
*AI 연구소 안에서 일하는 내장 평가자 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

아모데이는 9월 12일 에세이 *We Must Pace the Frontier*에서 평가자에게 사무 공간과 출입증, 내부 위험 평가팀에 준하는 시스템 권한을 주고, 찾아낸 내용을 회사 편집 없이 공개할 수 있게 계약으로 보장하겠다고 했습니다.

| 항목 | 에세이 | 9월 18일 발표 |
| :--- | :--- | :--- |
| 첫 평가자 | 언급 없음 | **Accenture(Faculty)** |
| 접근 권한 | 직원 수준 | 직원에 준함 |
| 공개권 보장 | 계약으로 보장 | <mark>기준 없음</mark> |
| 보고 방식 | 사고 보고 | 기준 없음 |
| 자금 | 언급 없음 | Anthropic 직접 지급 |

발표문은 평가자가 어떤 정보에 접근할지, 찾은 내용을 어떻게 보고할지에 대한 기준이 아직 없다고 인정했습니다. 장기적으로는 공동 기금이나 정부 재원이 평가 비용을 대야 한다는 입장이지만, 둘 다 없어서 평가자마다 다른 자금 구조를 적용한다고 밝혔어요. 에세이에서 가장 구체적이었던 **편집 없는 공개권**이 첫 계약 발표에는 포함되지 않았습니다.

## Accenture 선정과 독립성 논란

![Accenture 로고](/assets/images/ai/anthropic-accenture-embedded-evaluator/05-logo-accenture.webp)
*Accenture 로고 — 출처: Accenture*

첫 평가자가 METR 같은 비영리 안전 기관이 아니라 컨설팅 회사라는 점에서 상반된 반응이 나왔습니다. 두 회사는 이미 여러 사업 관계를 맺고 있어요. 2025년 12월 Accenture Anthropic Business Group을 만들었고, Accenture 직원 약 3만 명을 Claude로 교육하기로 했습니다.

X에서는 Anthropic이 Accenture를 독립 평가자라고 부른 게시물에 커뮤니티 노트가 붙었습니다. 평가 비용을 Anthropic이 지급하고 두 회사가 이미 사업 파트너라는 점을 들어 독립이라는 표현이 오해를 일으킨다는 내용이에요. TechCrunch는 비영리 기관을 예상한 업계 관계자들이 의외라는 반응을 보였고, Accenture 주가는 발표 뒤 시간외 거래에서 8% 상승했다고 전했습니다.

Anthropic은 Accenture가 기업·정부의 실제 AI 도입을 다뤄 본 경험을 안전 평가에 가져온다는 점과, AI 시대 이전부터 있던 상장사라는 점을 선정 이유로 들었습니다. 평가 결과를 고객사에 불리하게 공개할 수 있는지에 대해서는 발표문에 설명이 없어요.

OpenAI도 참여 의사를 밝혀 둔 상태입니다. 샘 올트먼(Sam Altman) CEO는 9월 12일 X에 직원 수준 접근 권한을 가진 독립 평가자는 좋은 방안이고 OpenAI도 하겠다고 적었지만, 9월 25일까지 평가자를 발표하지는 않았습니다.

## 국내 AI 안전성 평가와 비교

![한국 AI안전연구소 평가 모델 수와 월 출시 프런티어 모델](/assets/images/ai/anthropic-accenture-embedded-evaluator/06-chart.webp)
*한국 AI안전연구소 평가 모델 수와 월 출시 프런티어 모델 — 출처: 아주경제 보도 수치 기반 자가 렌더*

한국 AI안전연구소는 출범 1년 반이 지난 2026년 5월 기준으로 보고서 7건을 발표했지만, 해외 프런티어 모델을 독자 평가한 공개 보고서는 없었습니다. 주요 AI 개발사와 맺은 협약도 없어 미공개 모델에 사전 접근할 경로가 없어요.

| 항목 | 한국 AI안전연구소 |
| :--- | :--- |
| 평가용 GPU | NVIDIA H200 **16장** |
| 모델 1개 평가 기간 | 7~10일 |
| 벤치마크 1회 토큰 비용 | 5,000만~6,000만 원 |
| 해외 개발사 협약 | <mark>0건</mark> |

평가한 모델은 3월 6개에서 8월 11개로 늘었지만, 아주경제는 매달 프런티어 모델이 10개 이상 출시돼 연구소 장비로는 평가 속도를 맞추기 어렵다고 보도했습니다. 2026년 1월 시행된 AI 기본법은 고영향 AI에 대해 사업자가 배포 전 영향평가를 할 수 있게 했지만, 외부 평가자가 개발사 안에 상주하는 방식에 해당하는 조항은 없어요. 해외 개발사 모델을 출시 전에 보려면 지금 구조에서는 개발사와 개별 협약을 맺는 수밖에 없습니다.

## 앞으로 주목할 점

- Anthropic이 예고한 추가 평가자 명단과 METR 시범 운영 범위
- Accenture 평가팀의 첫 공개 보고서 시점과, 회사 편집 없이 공개된다는 조건이 계약에 들어가는지
- OpenAI가 고를 첫 내장 평가자와 비용 부담 방식
- 공동 기금이나 정부 재원 논의가 미국·영국에서 구체화되는지
- 한국 AI안전연구소의 해외 개발사 협약 체결 여부

## 참고 출처

- [[Anthropic] Partnering with Accenture on embedded evaluation (2026-09-18)](https://www.anthropic.com/news/accenture-embedded-evaluation)
- [[Accenture] Accenture and Anthropic Partner to Build Team of Embedded Evaluators (2026-09-18)](https://newsroom.accenture.com/news/2026/accenture-and-anthropic-partner-to-build-team-of-embedded-evaluators-at-anthropic)
- [[TechCrunch] Anthropic의 첫 내장 평가자, Faculty 인수·주가 반응 (2026-09-18)](https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/)
- [[TechCrunch] 내장 평가자의 독립성 쟁점 (2026-09-16)](https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/)
- [[OfficeChai] X 커뮤니티 노트와 두 회사의 기존 사업 관계](https://officechai.com/ai/anthropic-community-noted-on-x-for-calling-accenture-an-independent-evaluator-of-its-ai-despite-their-business-relationship/)
- [[Unite.AI] 올트먼, OpenAI도 내장 평가자 도입 약속](https://www.unite.ai/altman-says-openai-will-match-anthropics-embedded-evaluator-pledge/)
- [[디지털데일리] 한국 AI안전연구소 프런티어 모델 독자 평가 공개 0건 (2026-05-13)](https://www.ddaily.co.kr/page/view/2026051315321599128)
- [[아주경제] H200 16장으로 버티는 한국 AI 안전성 평가 (2026-09-16)](https://www.ajunews.com/view/20260916141912494)
- [[국가법령정보센터] 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543)
- 환율: 1달러 ≈ 1,400원 기준 환산
