---
title: "AI 가 진짜 F-16 을 몰았다 — 조종사는 스위치만 지켰다"
description: "시뮬레이터가 아닌 실제 F-16 에서 이뤄진 DARPA VENOM 자율 비행 시험의 조건과 개조 방식, KF-21 무인편대의 현재 위치를 정리합니다"
date: 2026-08-13
category: Robot
subcategory: News
tags: [darpa, venom, f-16, autonomous-flight, physical-ai]
image: /assets/og/2026-08-13-darpa-venom-f16-autonomy.png
---

전투기 한 대가 활주로를 떠난 뒤, 조종사는 스위치를 한 번 넘기고 손을 뗐습니다. 그다음부터는 AI가 기체를 몰았어요.

시뮬레이터가 아니라 실제 F-16, 실제 비행입니다. 조종사는 좌석에 그대로 앉아 있었지만 조종은 하지 않았습니다.

![자율 비행 시험을 앞둔 VENOM 개조 F-16과 정비사](/assets/images/robot/darpa-venom-f16-autonomy/01-hero-venom-ground.webp)
*자율 비행 시험을 앞둔 VENOM 개조 F-16과 정비사 — 출처: DARPA / U.S. Air Force*

## 플로리다 상공에서 벌어진 일

DARPA와 미 공군이 7월 16일 공개한 내용입니다. 플로리다 Eglin Air Force Base에서 자율 비행 시험대로 개조한 F-16이 AI 에이전트의 제어로 비행했습니다.

![자율 시스템 시험 중 비행하는 VENOM 개조 F-16](/assets/images/robot/darpa-venom-f16-autonomy/02-venom-flight.webp)
*자율 시스템 시험 중 비행하는 VENOM 개조 F-16 — 출처: DARPA / U.S. Air Force*

시험 조건은 이렇습니다.

| 항목 | 이번 시험 |
|---|---|
| 기체 | 운용 중인 표준 F-16 |
| 조종사 | <mark>좌석에 탑승, 감시</mark> |
| 조종권 | 스위치로 즉시 회수 |
| 장소 | Eglin 공군기지 |

핵심은 **human-on-the-loop**입니다. 사람이 고리 안에 있되 조작하지는 않고, 감시하다가 필요하면 끊어내는 방식이에요. 기체 개조 사진과 함께 공개된 설명에 따르면 조종사는 비행 내내 좌석에서 AI의 판단을 지켜봅니다.

보도에 따르면 6월에 먼저 개조기가 안전하게 뜨는지 확인하는 비행을 했고, 7월에 AI가 실제로 기체를 제어하는 비행으로 넘어갔습니다. 이륙은 사람이 하고 그 뒤 대부분의 비행을 AI가 맡았다고 전해집니다. Eglin에 배치된 개조기는 여섯 대로 알려졌습니다.

## 코어 소프트웨어를 건드리지 않았다

이 발표에서 기술적으로 가장 중요한 문장은 성능이 아니라 개조 방식에 있습니다.

![사람과 AI 사이에서 조종 권한이 넘어가는 개념 컷](/assets/images/robot/darpa-venom-f16-autonomy/03-agy-switch.webp)
*사람과 AI 사이에서 조종 권한이 넘어가는 개념 컷 — 출처: DARPA 공개 자료 기반 자가 생성*

### 개조 키트 하나를 얹는 방식

**VENOM**은 Viper Experimentation and Next-generation Operations Model의 약자입니다. 여기 쓰인 **VENOM Autonomy Kit**은 기체의 비행 제어와 센서를 자동화하되, F-16의 코어 소프트웨어는 그대로 뒀습니다.

DARPA 프로그램 매니저 James Valpiani 준장은 표준 F-16의 비행 제어와 센서를 자동화하면서 기체의 코어 소프트웨어를 바꾸지 않았다고 밝혔습니다. 조종사가 스위치를 넘기면 기존 조종과 AI 제어 사이를 오갈 수 있게 만든 인터페이스가 그 사이에 들어갑니다.

### 왜 이게 중요한가

특수 제작한 시제기 한 대로 묘기를 보이는 것과, **이미 운용 중인 기종을 개조해 같은 일을 하는 것**은 다른 문제입니다. 후자는 숫자를 늘릴 수 있어요.

전투 AI를 개발하려면 실제 비행 데이터가 필요한데, 시험할 기체가 한 대뿐이면 개발 속도가 그 한 대에 묶입니다. 운용 기종을 키트로 바꿀 수 있으면 시험대를 여러 대 만들 수 있고, 여러 AI 에이전트를 동시에 검증할 수 있습니다. DARPA가 이번 시험을 확장 가능한 개발 기반이라고 부르는 이유입니다.

> 기록이 아니라 생산 라인을 만든 셈입니다

## 여기까지 온 길

AI가 전투기를 모는 실험은 이번이 처음이 아닙니다. 다만 그동안은 세상에 한 대뿐인 특수 기체가 무대였어요.

![VENOM 이전 단계였던 X-62A VISTA 시험기](/assets/images/robot/darpa-venom-f16-autonomy/04-x62a-vista.webp)
*VENOM 이전 단계였던 X-62A VISTA 시험기 — 출처: U.S. Air Force 412TW*

**X-62A VISTA**는 F-16D를 개조한 시험기입니다. 2024년 4월, 이 기체에 올라탄 AI 에이전트가 사람이 조종하는 전투기를 상대로 실제 공중전을 벌였습니다. 모의 교전이었지만 시뮬레이터가 아닌 실기였고, AI가 전투 기동을 스스로 수행할 수 있다는 걸 보여준 시험이었습니다.

VENOM은 그 결과를 한 대에서 여러 대로 옮기는 단계입니다. DARPA는 이번 비행을 두고 미국이 표준 운용 기체를 최신 AI를 쓰는 기체로 바꿀 수 있음을 보여줬다고 설명했습니다.

두 시험 사이의 차이는 이렇습니다.

| 구분 | X-62A VISTA | VENOM |
|---|---|---|
| 기체 | 특수 시험기 1대 | 표준 F-16 |
| 목표 | 능력 증명 | 개발 기반 확장 |
| 초점 | 공중전 기동 | 다기체 시험 |

## 다음은 편대다

VENOM 기체들은 DARPA의 **AIR**(Artificial Intelligence Reinforcements) 프로그램의 토대가 됩니다.

![X-62A에서 VENOM, AIR로 이어지는 프로그램 흐름](/assets/images/robot/darpa-venom-f16-autonomy/05-chart-timeline.webp)
*X-62A에서 VENOM, AIR로 이어지는 프로그램 흐름 — 출처: 직접 작성 (자료: DARPA·U.S. Air Force)*

AIR에서는 여러 AI 에이전트를 실제 비행 시나리오에 올려 시험하고, 시야 밖 원거리 교전과 여러 기체가 함께 움직이는 상황까지 복잡도를 올립니다. 최종 목표는 사람이 탄 전투기 한 대가 무인기 여러 대를 지휘하는 구도이고, 미 공군의 **Collaborative Combat Aircraft**(협력 전투기, CCA) 계획으로 이어집니다.

### 한국은 어디쯤인가

같은 구도를 한국도 준비하고 있습니다. KAI는 다목적무인기 **AAP**의 실물을 공개하고 시험비행에 들어갔고, 7월 파른버러 에어쇼에서는 KF-21 한 대가 무인기 여러 대를 지휘하는 편대 개념을 선보였습니다.

다만 에어쇼에서 나온 편대 구성은 모형과 운용 개념으로 제시된 것이고, 실제로 여러 기체가 함께 난 결과는 아닙니다. 국내 업체들이 AI 파일럿 소프트웨어를 각각 개발하는 단계이기도 하고요. 미국이 운용 기종을 개조해 실기 시험에 들어간 것과는 아직 단계가 다릅니다.

### 남아 있는 물음

Valpiani 준장은 같은 발표에서 신중한 말도 남겼습니다. 시야 밖 교전에서 AI가 복잡성을 다루는 데 큰 잠재력이 있지만, 현대전의 혼란 속에서 전투 AI의 성능과 신뢰성에 관해 어려운 질문이 많이 남아 있다는 것입니다.

기술적으로 가능하다는 것과 전장에서 믿고 맡길 수 있다는 것은 다른 문제입니다. 이번 비행이 답한 건 앞쪽이고, 뒤쪽은 AIR 프로그램이 앞으로 확인할 몫으로 남았습니다.

> 조종석은 아직 비어 있지 않습니다

## 정리하면

이번 시험에서 새로운 건 AI가 전투기를 몰았다는 사실 자체가 아닙니다. 그건 2024년에 이미 한 번 나왔어요.

달라진 건 그 일을 **특수 기체가 아닌 표준 기체에서** 할 수 있게 됐다는 점입니다. 시험대가 여러 대로 늘어나면 전투 AI 개발은 실험이 아니라 반복 작업이 됩니다. 다음 소식은 한 대가 아니라 편대에서 나올 가능성이 큽니다.

## 참고 출처

- [[DARPA] DARPA, U.S. Air Force fly AI-controlled F-16 (공식 발표, 본문 이미지 2점 출처)](https://www.darpa.mil/news/2026/darpa-us-air-force-fly-ai-controlled-f-16)
- [[Stars and Stripes] F-16 outfitted with AI kit completes pathbreaking sortie (개조기 대수·비행 경과)](https://www.stripes.com/branches/air_force/2026-07-20/first-venom-autonomous-jet-flight-22317435.html)
- [[Wikimedia Commons] X-62A VISTA flies over Edwards AFB (본문 이미지 1점 출처)](https://commons.wikimedia.org/wiki/File:X-62A_VISTA_flies_over_Edwards_AFB_(8417484).jpg)
- [[나우뉴스] KF-21 한 대가 무인기 12대 지휘 — 한국형 AI 편대 공개 (파른버러 전시 내용)](https://nownews.seoul.co.kr/news/newsView.php?id=20260727601007)
