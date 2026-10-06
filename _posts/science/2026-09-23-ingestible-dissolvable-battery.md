---
title: "삼키는 배터리 — MIT 1.84V 종이 배터리는 몸속에서 분해된다"
description: "삼키는 캡슐 기기의 전원 문제를 녹는 마그네슘 종이 배터리로 풀려는 연구의 구조와 성능, 한계를 정리합니다"
date: 2026-09-23
category: Science
subcategory: Explainer
tags: [ingestible-electronics, biodegradable-battery, mit, medical-device, bioelectronics]
image: /assets/og/2026-09-23-ingestible-dissolvable-battery.png
---

MIT 연구진이 삼킨 뒤 몸속에서 녹는 종이 배터리를 만들어 2026년 9월 21일 Nature Chemical Engineering에 발표했습니다. 최대 1.84V를 출력하고, 돼지 위 속에서 3일 동안 캡슐 기기를 작동시킨 뒤 수 주에 걸쳐 조각나 분해돼요.

삼키는 캡슐 기기는 지금 대부분 산화은 코인 전지로 동작합니다. 연구진은 캡슐 외피가 손상됐을 때 전지가 소화관을 다치게 할 위험과 배설된 전지가 환경에 남는 문제를 함께 줄이려 했다고 밝혔어요.

![논문 제목과 초록, 1.84V·Mg–MoO3 종이 배터리·돼지 실험 하이라이트](/assets/images/science/ingestible-dissolvable-battery/01-paper.webp)
*논문 제목과 초록, 1.84V·Mg–MoO3 종이 배터리·돼지 실험 하이라이트 — 출처: Say et al., Nature Chemical Engineering (2026) (CC BY 4.0, 하이라이트 추가)*

## 연구 개요

논문 제목은 *Bioresorbable batteries for transient ingestible bioelectronics*이고, MIT 기계공학과 Giovanni Traverso 교수 연구실이 주도했습니다. 제1저자는 MIT 박사후연구원 출신 Mehmet Girayhan Say이고, 2025년 11월 투고해 2026년 8월 게재가 확정됐어요.

- 음극: 마그네슘 합금(AZ31)
- 양극: 삼산화몰리브덴(MoO3)과 셀룰로스 나노섬유를 섞은 종이 복합재
- 전해질: 염화콜린과 젖산으로 만든 생분해 이온성 액체 젤
- 포장: 밀랍과 칸델릴라 왁스

연구진은 배터리 부품의 양이 모두 하루 섭취 권장 한도 안에 들도록 설계했다고 밝혔습니다. 크기는 지름 7.5mm 원형과 길이 24mm 막대형 두 가지로, 원형은 의약품용 000 캡슐(길이 26mm, 지름 9.5mm)에 들어가요.

## 배터리 구조와 쓰임새

![녹는 배터리의 구조, 복약 추적 RFID와 위 전기자극 캡슐, 분해 과정 개념도](/assets/images/science/ingestible-dissolvable-battery/02-paper-fig1.webp)
*녹는 배터리의 구조, 복약 추적 RFID와 위 전기자극 캡슐, 분해 과정 개념도 — 출처: Say et al., Nature Chemical Engineering (2026) Fig. 1 (CC BY 4.0)*

### 복약 확인 RFID

RFID(무선 인식) 태그는 약을 삼켰는지 밖에서 확인하는 데 씁니다. 기존 수동형 태그는 전지가 없어 판독기를 목이나 허리에 가까이 대야 했는데, 이 배터리를 단 태그는 1.5m 떨어진 판독기와 계속 통신했어요. 캡슐이 식도로 들어가면 신호 세기가 약 10dB 감소해, 이 변화로 삼킨 시점을 알아냅니다.

### 위 전기자극 캡슐

위벽에 약한 전류를 흘려 식욕 호르몬 그렐린(ghrelin) 분비를 증가시키는 캡슐입니다. 배터리 1개로 3일, 2개를 병렬로 연결하면 7일까지 자극을 유지했어요. 돼지 3마리에서 20분 자극 뒤 혈중 그렐린이 평균 36.3% 늘었고, 최대치는 약 50%였습니다.

MIT는 그렐린 분비 자극이 암 환자 등에서 체중이 감소하는 악액질(cachexia) 치료에 쓰일 수 있다고 설명했어요. 이 캡슐의 이전 버전은 산화은 코인 전지 2개로 동작했습니다.

## 전압과 작동 시간

![마그네슘 음극 배터리의 양극 재료별 개방전압](/assets/images/science/ingestible-dissolvable-battery/03-chart.webp)
*마그네슘 음극 배터리의 양극 재료별 개방전압 — 출처: Nature Chemical Engineering 논문 수치 기반 자가 렌더*

마그네슘은 몸속에서 하루 1.2~12㎛(마이크로미터) 속도로 녹는 금속이라 생분해 배터리 음극으로 연구돼 왔습니다. 논문이 인용한 선행 연구에서 마그네슘을 몰리브덴·철·텅스텐과 짝지으면 전압이 0.15~0.75V였는데, 삼산화몰리브덴 양극 조합은 **1.84V**까지 높아졌어요.

작동 전압 1.84V에서 면적당 용량은 2.43mAh/㎠였고, 연구진은 에너지·출력 밀도까지 포함해 다른 생분해 배터리와 비슷한 수준이라고 적었습니다. 직렬로 연결하면 3V 이상을 24시간 넘게 공급해, 마이크로컨트롤러나 무선 통신 모듈을 단 캡슐에도 쓸 수 있다고 봤어요.

![돼지 위 속에 둔 배터리의 개방전압 변화](/assets/images/science/ingestible-dissolvable-battery/04-chart.webp)
*돼지 위 속에 둔 배터리의 개방전압 변화 — 출처: Nature Chemical Engineering 논문 Fig. 2 기반 자가 렌더*

연구진은 배터리를 캡슐에 넣어 내시경으로 돼지 위에 고정한 뒤 1일·3일 차에 꺼내 측정했습니다. 두 형태 모두 3일 동안 전압이 서서히 감소했고, 대형 배터리의 에너지 밀도는 1.32mWh/㎠에서 0.22mWh/㎠로 줄었어요.

## 몸속 분해 과정

![위 전기자극 캡슐이 인공 위액에서 0·14·40·90일에 걸쳐 분해되는 과정](/assets/images/science/ingestible-dissolvable-battery/05-paper-fig4.webp)
*위 전기자극 캡슐이 인공 위액에서 0·14·40·90일에 걸쳐 분해되는 과정 — 출처: Say et al., Nature Chemical Engineering (2026) Fig. 4k (CC BY 4.0)*

인공 위액(pH 1.2, 37℃)에 담근 캡슐은 14일 차부터 녹기 시작했고, 분해를 앞당기는 75℃ 조건으로 옮기자 40일 안에 대부분 녹았습니다. 90일 차에는 작은 입자만 남았어요.

돼지 실험에서는 캡슐이 1~2주에 걸쳐 물러지고 조각나며 소화관을 통과했고, 배터리의 금속 잔여물만 가끔 발견됐습니다. RFID 태그에서 녹지 않는 부분은 약 18㎟ 크기의 RFID 칩 하나로, 연구진은 자연 배설될 것으로 봤어요.

## 국내 접점

한국소비자원 집계로 10세 미만 어린이의 단추형 전지 삼킴 사고는 최근 5년 동안 268건 발생했습니다. 삼킨 전지는 체내에서 전기화학 반응을 일으켜 식도·위에 화상과 천공을 낼 수 있어, 국가기술표준원은 2025년 7월 단추형 전지에 어린이보호포장을 적용하는 기준을 마련한다고 밝혔어요.

이번 논문도 서론에서 버튼 전지를 잘못 삼켰을 때의 식도 천공·사망 사례를 들며, 녹는 배터리가 캡슐이 깨지거나 몸속에 오래 머물 때의 안전성을 높일 수 있다고 설명했습니다. 다만 이 배터리는 의료용 캡슐 전원으로 설계된 것이라, 가정용 버튼 전지를 대체하는 제품과는 거리가 있어요.

국내 기업이나 기관이 이 연구에 참여했거나 도입을 밝힌 사례는 확인되지 않았습니다.

## 한계와 남은 과제

![몸속에서 녹는 캡슐 개념 컷](/assets/images/science/ingestible-dissolvable-battery/06-agy.webp)
*몸속에서 녹는 캡슐 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

[회로 기판]
전기자극 캡슐의 회로 기판(PCB)은 아직 녹지 않고, 연구진은 완전히 녹는 회로를 다음 과제로 꼽았어요.

[실험 조건]
동물 실험은 굶긴 돼지 소수로 진행됐고, 음식물이 있는 상태·산도 변화·장 운동 차이는 아직 시험하지 않았습니다.

[작동 기간]
현재 포장으로는 1주 이상 두면 성능이 크게 저하돼요. 전해질 젤이 마르고 포장이 일부 녹는 영향으로 분석했습니다.

[개체 편차]
배터리마다 성능 차이가 있었고, 연구진은 제조 공차와 왁스 두께 차이를 원인으로 봤어요. 보관 수명도 추가 검증이 필요하다고 적었습니다.

[사람 적용]
사람 대상 시험은 아직 없습니다. MIT는 이 배터리를 쓰는 RFID 복약 확인 시스템 SAFARI의 임상시험을 약 2년 뒤 시작할 계획이라고 밝혔어요.

연구비는 Novo Nordisk 등이 지원했습니다.

## 정리

![녹는 종이 배터리 정리 카드](/assets/images/science/ingestible-dissolvable-battery/07-items.webp)
*녹는 종이 배터리 정리 카드 — 출처: Nature Chemical Engineering 논문 기반 자가 렌더*

## 앞으로 주목할 점

- 임상 진입: MIT가 약 2년 뒤로 잡은 SAFARI 복약 확인 시스템의 사람 대상 시험
- 이식형 확장: 연구진이 언급한 수 시간~수일짜리 단기 이식 기기 적용

## 참고 출처

- [[Nature Chemical Engineering] Say et al., Bioresorbable batteries for transient ingestible bioelectronics (2026-09-21, 본문 이미지 3점 출처)](https://www.nature.com/articles/s44286-026-00443-7)
- [[MIT News] 소화관에서 녹는 배터리 연구 소개 (2026-09-21)](https://news.mit.edu/2026/batteries-safely-break-down-in-gi-tract-could-improve-ingestible-devices-0921)
- [[아주경제] 단추형 전지 어린이보호포장 적용과 삼킴 사고 268건 (2025-07-15)](https://www.ajunews.com/view/20250715082228941)
