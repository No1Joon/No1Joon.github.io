---
title: "AI의 전기 (10) — Anthropic 오사카 500MW 데이터센터, 전력망 대신 현장 발전"
description: "NTT DATA 가 오사카에 짓는 Anthropic 전용 데이터센터 협상을 따라, 전력망 연결을 기다리지 않고 부지 안에서 전기를 만드는 방식을 정리합니다"
date: 2026-10-19
category: Tech
subcategory: Explainer
tags: [anthropic, ntt-data, data-center, onsite-generation, ai-power]
image: /assets/og/2026-10-19-ai-power-10-osaka-onsite-generation.png
---

9탄까지는 데이터센터가 전력망이나 원전, 궤도에서 전기를 얻는 방법을 봤습니다
이번에는 전력망 연결을 기다리지 않고 부지 안에서 전기를 만드는 쪽입니다

🔗 링크 첨부 - https://blog.naver.com/rottensweetpotato/224434111541

닛케이는 10월 13일 NTT DATA가 오사카에 **Anthropic 전용 데이터센터**를 짓는다고 보도했어요
전력 인입은 최대 <mark>500MW</mark>이고, 두 회사는 최종 협상 중입니다

계통 연결이 오래 걸려 현장 발전과 연료전지를 먼저 검토한다는 내용이에요

![Anthropic과 NTT DATA 로고](/assets/images/tech/ai-power-10-osaka-onsite-generation/01-hero.webp)
*Anthropic과 NTT DATA 로고*

## 보도 내용

닛케이 보도를 로이터 등이 전재했고, 두 회사는 논평을 거부했어요
아래는 모두 보도 기준입니다

| 항목 | 보도 내용 |
| :--- | :--- |
| 위치 | 일본 오사카 |
| 전력 인입 | **최대 500MW** |
| 건설비 | 최대 약 8조 8천억 원(1조 엔) |
| 서명 목표 | 2027년 3월 말 |
| 일부 가동 | 이르면 2028년 |

건설비 약 8조 8천억 원(1조 엔)에는 GPU 서버 비용이 포함되지 않았어요
서버 비용까지 포함하면 총비용은 <mark>수조 엔</mark>에 이를 것으로 닛케이는 봤습니다

성사되면 Anthropic의 **일본 첫 전용 데이터센터**가 돼요
닛케이는 Anthropic이 다른 아시아 국가에서도 새 데이터센터를 검토 중이라고 전했습니다

## 500MW의 크기

![Google TPU 확장분, 오사카, River Bend의 전력 규모 비교 막대 차트](/assets/images/tech/ai-power-10-osaka-onsite-generation/02-chart.webp)
*Google TPU 확장분, 오사카, River Bend의 전력 규모 비교 막대 차트 — 출처: Anthropic, Hut 8, 닛케이 보도 기반 자가 렌더*

Anthropic은 2025년 10월 Google TPU 용량을 증설한다고 밝혔어요
2026년에 1GW 이상을 가동하는 규모입니다

같은 해 12월 Hut 8은 루이지애나 River Bend 245MW 임대 계약을 공시했어요
임차인은 Fluidstack이고, Anthropic 추론에 쓰이는 시설입니다

오사카 500MW는 River Bend의 약 <mark>2배</mark>예요

Mordor Intelligence는 일본 데이터센터 전력 용량을 2026년 3.57GW로 추정했어요
오사카 한 곳이 그 14%에 해당합니다

## 전력망 대신 현장 발전

![데이터센터 옆에 연료전지 모듈이 늘어선 장면을 표현한 개념 컷](/assets/images/tech/ai-power-10-osaka-onsite-generation/03-agy.webp)
*데이터센터 옆에 연료전지 모듈이 늘어선 장면을 표현한 개념 컷 — 출처: 개념 컷, agy 자가 생성*

1탄에서 본 것처럼 대형 부하를 전력망에 연결하려면 송전선과 변전소를 새로 짓고 수년을 기다려야 해요

계통에서 500MW를 공급받기까지 시간이 오래 걸린다는 것이 닛케이 보도예요
그래서 **현장 발전과 연료전지**를 먼저 검토한다고 전했습니다

이렇게 전력망 계량기 뒤쪽, 부지 안에서 전기를 만드는 방식을 *behind-the-meter*라고 해요
미국 데이터센터에서도 현장 발전 방식을 사용하고 있습니다

### ⚡ 연료전지 계약 사례

미국 전력회사 AEP는 2024년 11월 Bloom Energy와 연료전지 **최대 1GW** 계약을 맺었어요
첫 주문은 100MW였습니다

부지에 고체산화물 연료전지(SOFC)를 두고 계통 연결 전까지 전력을 공급하는 용도예요

Bloom Energy는 2025년 10월 Brookfield와 협력도 발표했어요
AI 데이터센터용 연료전지에 최대 7조 원(50억 달러)을 투입하는 내용입니다

이 연료전지들은 주로 **천연가스**를 연료로 씁니다

<mark>전력망 연결보다 빨리 가동할 수 있지만, 연료를 태우는 발전 설비를 데이터센터 옆에 둬야 해요</mark>

## 한국과의 차이

Anthropic은 2026년 6월 서울 사무소를 열었어요

Claude는 Amazon Bedrock과 Vertex AI를 통해 한국 내 데이터 상주를 선택할 수 있어요
다만 Anthropic 전용 데이터센터 계획은 일본이 먼저입니다

국내 10MW 이상 데이터센터의 전력계통영향평가는 1탄에서 다뤘어요

2026년 5월 국회를 통과한 **AI 데이터센터 특별법**은 2027년 2월 시행 예정이에요
비수도권 일정 규모 이하 데이터센터는 이 평가를 면제받습니다

전력망 연결을 기다리는 동안 현장 발전을 쓰는 방식의 허용 범위는 하위법령에서 정해져요

## 앞으로 주목할 점

- 서명 여부: <mark>2027년 3월 말</mark> 목표, 양사 공식 확인 전
- 전력원: 현장 발전 연료가 가스인지, 연료전지 규모는 얼마인지
- 아시아 추가 거점: 닛케이가 전한 다른 아시아 국가 검토
- 국내: AI 데이터센터 특별법 하위법령의 자가발전과 직접 전력거래 특례

🔗 링크 첨부 - https://blog.naver.com/rottensweetpotato/224434111541

## 참고 출처

- [[The Star, 로이터] NTT Data in final talks to build Anthropic's first data centre in Japan, Nikkei reports (2026-10-13)](https://www.thestar.com.my/tech/tech-news/2026/10/13/ntt-data-in-final-talks-to-build-anthropic039s-first-data-centre-in-japan-nikkei-reports)
- [[The Next Web] NTT Data reportedly nears deal to build Anthropic's first Japan data centre (서버 포함 총비용, 전력 대안)](https://thenextweb.com/news/ntt-data-anthropic-osaka-data-centre)
- [[W.Media] NTT Data in talks with Anthropic (서명 목표, 일본 데이터센터 전력 용량 추정)](https://w.media/?p=44256)
- [[Anthropic] Expanding our use of Google Cloud TPUs (2025-10-23)](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
- [[SEC] Hut 8 Corp. 10-K FY2025 (River Bend 245MW 임대)](https://www.sec.gov/Archives/edgar/data/1964789/000110465926019392/hut-20251231x10k.htm)
- [[Utility Dive] AEP, Bloom Energy 연료전지 최대 1GW 계약 (2024-11)](https://www.utilitydive.com/news/aep-bloom-energy-fuel-cell-data-center/733150/)
- [[Data Center Dynamics] Bloom Energy, Brookfield와 7조 원 규모 협력 (2025-10)](https://www.datacenterdynamics.com/en/news/bloom-energy-signs-5bn-partnership-with-brookfield-to-deploy-fuel-cell-tech-across-ai-data-centers/)
- [[Anthropic] 지역별 데이터 상주 안내](https://claude.com/ko/regional-compliance)
- [[스마트시티] AI 데이터센터 특별법 본회의 통과, 2027년 2월 시행 (2026-05-08)](https://smartcity.go.kr/2026/05/08/ai데이터센터-규제-확-푼다인허가-절차-대폭-단축/)
- 환율: 1달러 ≈ 1,400원, 1조 엔 ≈ 63억 달러(보도 환산) 기준
