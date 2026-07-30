---
title: "아틀라스 (1) — 현대가 만드는 휴머노이드의 정체와 스펙"
description: "보스턴 다이내믹스 아틀라스가 어떤 로봇인지, 유압에서 완전 전기구동으로 넘어온 세대 교체와 56 자유도 스펙을 정리합니다"
date: 2026-06-17
category: Robot
subcategory: Explainer
tags: [atlas, humanoid, boston-dynamics, hyundai, physical-ai]
image: /assets/og/2026-06-17-atlas-humanoid-01-what-and-spec.png
---

요즘 뉴스에 "현대 아틀라스"라는 말이 부쩍 자주 보이시죠?

자동차 회사인 현대가 왜 사람처럼 걷는 로봇을 만드는지, 그 아틀라스(Atlas)가 대체 뭔지 궁금하셨던 분들을 위해 준비했어요.

오늘은 그 **정체와 스펙**부터 차근차근 풀어드릴게요. ([아틀라스 시리즈] 1탄입니다.)

![신형 전기구동 아틀라스 휴머노이드 로봇](/assets/images/robot/atlas-humanoid-01-what-and-spec/01-hero-bostondynamics.webp)
*신형 전기구동 아틀라스 휴머노이드 로봇 — 출처: Boston Dynamics*

## 아틀라스가 뭐길래?

아틀라스는 **보스턴 다이내믹스(Boston Dynamics)**가 만든 사람 모양 로봇, 즉 **휴머노이드(humanoid)**예요.

보스턴 다이내믹스는 백덤블링하는 로봇 영상으로 유명해진 그 회사 맞습니다.

여기서 많은 분이 헷갈려 하시는 포인트 하나.

- **보스턴 다이내믹스는 현재 현대차그룹이 최대주주인 회사**예요.

2021년 현대차그룹이 경영권을 인수했고, 그래서 "현대 아틀라스"라고 부르는 겁니다.

자동차를 만들던 회사가 이제는 **사람 대신 일하는 로봇**까지 직접 만드는 셈이죠.

> 한 줄 요약: 아틀라스 = 보스턴 다이내믹스의 휴머노이드 로봇, 그리고 그 회사 주인은 현대차그룹.

## 유압을 버리고 '완전 전기'로 — 세대 교체

아틀라스는 사실 한 가지 모델이 아니에요. 크게 **구버전과 신버전**으로 나뉩니다.

### 구버전 (유압식)

![2013년 구형 유압식 아틀라스 정면](/assets/images/robot/atlas-humanoid-01-what-and-spec/02-darpa-pd.webp)
*2013년 구형 유압식 아틀라스 정면 — 출처: DARPA(퍼블릭 도메인)*

예전 아틀라스는 **유압(hydraulic)** 방식이었어요.

기름의 압력으로 관절을 움직이다 보니 힘은 셌지만, 기름이 새고 소음이 크고 구조가 복잡했죠.

연구·시연용에 가까웠습니다.

### 신버전 (완전 전기식)

![신형 완전 전기 아틀라스가 현장에서 작업하는 모습](/assets/images/robot/atlas-humanoid-01-what-and-spec/03-bostondynamics.webp)
*신형 완전 전기 아틀라스가 현장에서 작업하는 모습 — 출처: Boston Dynamics*

지금 화제의 아틀라스는 **완전 전기구동(all-electric)**으로 새로 태어났어요.

유압 장치를 싹 걷어내고 전기 모터로만 움직입니다.

그 덕분에 더 조용하고, 더 정밀하고, **공장에서 진짜로 일할 수 있는** 로봇이 됐어요.

이게 핵심 변화예요. **'보여주는 로봇'에서 '일하는 로봇'으로** 넘어온 거죠.

## 스펙으로 보는 신형 아틀라스

신형 아틀라스가 왜 대단한지, 숫자로 보면 더 와닿아요.

![신형 아틀라스 손·촉각 센서 매크로](/assets/images/robot/atlas-humanoid-01-what-and-spec/04-agy-hand.webp)
*신형 아틀라스 손·촉각 센서 매크로 — 출처: agy 생성*

### 56 자유도(DoF)

가장 눈에 띄는 건 **56 자유도**예요.

자유도(Degrees of Freedom)는 쉽게 말해 **따로따로 움직일 수 있는 관절의 개수**입니다.

사람 몸처럼 56곳을 독립적으로 꺾고 비틀 수 있다는 뜻이에요.

그래서 동작이 뻣뻣하지 않고 사람처럼 부드럽습니다.

### 사람 손 + 촉각 센서

손도 **사람 손 크기**로 만들어졌어요.

손가락과 손바닥에 **촉각 센서(tactile sensor)**가 들어가 있어서, 물건을 얼마나 세게 쥐는지 느끼며 섬세하게 다룰 수 있습니다.

### 360도 시야

머리에는 **360도 카메라**가 달려 사방을 한 번에 봐요.

사람처럼 고개를 돌릴 필요 없이 전방위를 인식합니다.

### 힘과 자율성

최대 **약 50kg(110파운드)**까지 들어 올리고, 사람이 일일이 조종하지 않아도 **스스로 판단해 작업**해요.

새로운 일도 빠르게 학습합니다.

![공장에서 일하는 휴머노이드](/assets/images/robot/atlas-humanoid-01-what-and-spec/05-agy-factory.webp)
*공장에서 일하는 휴머노이드 — 출처: agy 생성*

## 그래서, 왜 현대가 만들까?

정리하면 아틀라스는 **산업용 엔터프라이즈급 휴머노이드**예요.

전시장에서 재주 부리는 로봇이 아니라, **공장·물류 현장에서 부품을 나르고 물건을 다루는** 실전용 로봇이라는 뜻입니다.

현대차그룹 입장에선 자기 공장에서 쓸 로봇을 직접 만들 수 있게 된 거죠.

자동차를 만들던 제조 노하우 위에 **'사람처럼 일하는 로봇'**을 얹는 그림입니다.

이게 요즘 말하는 **피지컬 AI(Physical AI)** 경쟁의 한복판이에요.

## 1탄 정리

- 아틀라스 = 보스턴 다이내믹스의 휴머노이드, 최대주주는 현대차그룹
- 유압 → **완전 전기구동**으로 세대 교체, '일하는 로봇'으로 진화
- **56 자유도** + 사람 손·촉각 센서 + 360도 시야 + 50kg 적재 + 자율 작업

이제 정체와 스펙을 알았으니, 다음 편이 진짜 본론이에요.

- **2탄에서는 이 아틀라스가 실제로 현대 공장에 들어가는 이야기** — 조지아 공장 첫 투입과 연 3만 대 양산 계획을 다룹니다.
- **3탄에서는 노조 반발과 테슬라 옵티머스 경쟁** 같은 진짜 변수들을 짚어볼게요.

다음 편도 기대해 주세요!

## 참고 출처

- [[Boston Dynamics] Boston Dynamics Unveils New Atlas Robot to Revolutionize Industry](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/)
- [[Hyundai Motor Group] Boston Dynamics Atlas Named 'Best Robot' in Best of CES 2026 Awards by CNET Group](https://www.hyundaimotorgroup.com/en/news/boston-dynamics-atlas-named-best-robot-in-best-of-ces-2026-awards-by-cnet-group)
- [본문 이미지: 신형 아틀라스 히어로 — Boston Dynamics 공식 / 구형 유압 아틀라스(2013) — DARPA, 퍼블릭 도메인(Wikimedia Commons) / 손·공장 연출 컷 — agy 생성](https://commons.wikimedia.org/wiki/File:Atlas_frontview_2013.jpg)
