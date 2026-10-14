---
title: "마거릿 해밀턴 별세 — 아폴로 11호 1202 경보와 소프트웨어 공학"
description: "착륙 직전 과부하 경보에도 필수 계산이 멈추지 않은 설계와, 해밀턴이 소프트웨어 공학을 분야로 세운 과정을 정리합니다"
date: 2026-10-13
category: Tech
subcategory: Explainer
tags: [margaret-hamilton, apollo, software-engineering, nasa, history]
image: /assets/og/2026-10-13-margaret-hamilton-apollo-1202.png
---

아폴로 비행 소프트웨어를 이끈 마거릿 해밀턴(Margaret Hamilton)이 2026년 9월 30일 미국 매사추세츠주 케임브리지에서 90세로 별세했어요. MIT는 10월 7일 부고를 발표하고 그를 소프트웨어 공학을 하나의 분야로 정립한 사람으로 소개했습니다.

해밀턴의 이름이 자주 언급되는 장면은 1969년 7월 20일 아폴로 11호 착륙 직전이에요. 착륙선 컴퓨터가 과부하 경보를 다섯 번 표시했는데도 착륙에 필요한 계산을 중단하지 않았고, 그 설계에 해밀턴 팀의 설계 원칙이 반영돼 있었습니다.

![1969년 마거릿 해밀턴과 아폴로 비행 소프트웨어 출력물](/assets/images/tech/margaret-hamilton-apollo-1202/01-photo.webp)
*1969년 마거릿 해밀턴과 아폴로 비행 소프트웨어 출력물 — 출처: Draper Laboratory*

## 마거릿 해밀턴의 이력

1936년 인디애나주에서 태어나 1958년 얼럼 칼리지에서 수학을 전공한 뒤, 1959년 MIT에서 기상학자 에드워드 로렌츠(Edward Lorenz)의 날씨 예측 프로그램을 작성하며 프로그래밍을 시작했어요. 1961년에는 미 공군 방공 시스템 SAGE를 거쳐, 1965년 MIT 계측연구소(Instrumentation Laboratory, 지금의 Draper)에 아폴로 프로젝트의 첫 여성 프로그래머로 합류했습니다.

이후 사령선(Command Module) 소프트웨어 팀을 이끌다가 비행 소프트웨어 전체를 책임지는 직책을 맡았어요. 1976년 Higher Order Software를, 약 10년 뒤 Hamilton Technologies를 설립했고, 2016년 버락 오바마 당시 대통령에게 대통령 자유 훈장을 받았습니다. 훈장 사유에는 그의 작업이 현대의 고신뢰 소프트웨어 설계·공학의 기초를 마련했다고 적혔어요.

소프트웨어 공학(software engineering)이라는 용어의 보급에 기여한 사람으로도 꼽힙니다. 해밀턴은 2018년 인터뷰에서 하드웨어처럼 소프트웨어도 공학으로 대접받게 하려고 이 말을 쓰기 시작했고, 한동안은 농담처럼 받아들여졌다고 회고했어요.

## 아폴로 유도 컴퓨터의 제약

![아폴로 유도 컴퓨터(AGC) 실물](/assets/images/tech/margaret-hamilton-apollo-1202/02-photo-agc.webp)
*아폴로 유도 컴퓨터(AGC) 실물 — 출처: Wikimedia Commons*

착륙선에 탑재된 아폴로 유도 컴퓨터(Apollo Guidance Computer, AGC)는 지금 기준으로 아주 작은 기계였어요. 착륙선 소프트웨어를 맡았던 Don Eyles의 정리에 따르면 사양은 이렇습니다.

| 항목 | 값 |
| :--- | :--- |
| 고정 메모리 (ROM) | 36K 워드 |
| 쓰기 가능 메모리 (RAM) | <mark>2K 워드</mark> |
| 메모리 사이클 | 11.7µs |
| 논리 소자 | 3입력 NOR 게이트 약 5,600개 |
| 무게 · 전력 | 약 32kg · 약 55W |

프로그램은 구리선을 자기 코어에 통과시키느냐 비켜 가느냐로 0과 1을 기록한 로프 메모리에 저장해서, 발사 뒤에는 수정할 수 없었어요. 해밀턴이 로프 마더(rope mother)라고 불린 것도 이 메모리를 책임졌기 때문입니다.

![우주비행사가 컴퓨터와 소통한 DSKY 인터페이스 도해](/assets/images/tech/margaret-hamilton-apollo-1202/03-photo-dsky.webp)
*우주비행사가 컴퓨터와 소통한 DSKY 인터페이스 도해 — 출처: NASA · Wikimedia Commons*

우주비행사는 계산기처럼 생긴 DSKY에 동사(Verb)와 명사(Noun) 번호를 입력해 컴퓨터에 명령했어요. 경보가 발생하면 이 화면에 PROG 등이 표시되고 1202 같은 숫자 코드가 출력됐습니다.

## 1202 경보와 우선순위 스케줄링

![아폴로 11호 동력 하강 중 프로그램 경보 경과 타임라인](/assets/images/tech/margaret-hamilton-apollo-1202/04-chart.webp)
*아폴로 11호 동력 하강 중 프로그램 경보 경과 타임라인 — 출처: Don Eyles 기록 기반 자가 렌더*

동력 하강을 시작하고 약 5분 뒤, 버즈 올드린(Buzz Aldrin)이 고도·속도 화면을 호출한 직후 첫 1202 경보가 표시됐어요. 착륙까지 모두 다섯 번(1202 네 번, 1201 한 번)의 경보가 났습니다.

AGC의 실행 관리자(Executive)는 작업마다 우선순위를 지정하고, 작업이 쓸 작업 자리(코어 세트) 8개와 벡터 계산 공간(VAC) 5개를 할당했어요. 1202는 남은 코어 세트가 없다는 뜻이고, 1201은 VAC가 없다는 뜻입니다. MIT 부고는 이렇게 우선순위에 따라 필수 작업을 계속 실행하도록 하는 설계를 해밀턴 팀의 성과로 소개해요.

랑데부 레이더 스위치가 절차대로 둔 위치에서, 레이더 쪽 장치의 전원 위상이 컴퓨터와 맞지 않아 불필요한 신호가 초당 최대 6,400회씩 수신됐습니다. 이 신호를 세느라 컴퓨터의 연산 시간 중 약 13%가 소모됐고, 우선순위가 가장 낮지만 가장 긴 항법 계산(SERVICER)이 제시간에 완료되지 못하고 누적되면서 작업 공간이 부족해졌어요.

이때 작동한 기능이 재시작 보호예요. 자리가 없으면 컴퓨터는 스스로 재시작하고, 미리 표시해 둔 지점부터 가장 최근의 항법 계산만 복구한 뒤 보류된 작업과 보호 표시가 없는 덜 중요한 작업은 폐기했습니다. 올드린이 호출한 화면 표시가 재시작 뒤 사라진 것도 이 때문이었어요. 유도·조종 계산은 중단되지 않았고, 휴스턴 관제는 경보가 반복되지 않는 한 진행해도 된다고 판단했습니다.

착륙 직전 단계에서는 필수 작업만으로도 여유가 10% 미만으로 감소해 재시작으로도 부하를 완전히 해소하지 못했어요. 닐 암스트롱(Neil Armstrong)이 102:43:08에 자세 유지 모드로, 이어 수동 조종에 가까운 P66으로 전환하면서 계산량이 감소했고, 착륙선은 102:45:40에 내려앉았습니다.

## 오늘날 소프트웨어에 적용된 설계 원칙

![아폴로 1202 경보 정리 카드](/assets/images/tech/margaret-hamilton-apollo-1202/05-items.webp)
*아폴로 1202 경보 정리 카드 — 출처: Don Eyles 기록·MIT 부고 기반 자가 렌더*

해밀턴 팀의 설계는 하드웨어 이상이나 사람의 조작이 언제든 시스템에 영향을 줄 수 있다고 보고, 그때 어떤 작업을 우선 유지할지 소프트웨어에 지정한 것이었어요. 해밀턴은 1971년 Datamation에 보낸 편지에서 이 복구 동작이 없었다면 아폴로 11호가 성공하지 못했을 수도 있다고 썼습니다.

작업 우선순위, 감시 타이머(워치독)에 의한 재시작, 재시작 뒤 이어서 계산할 수 있도록 상태를 저장하는 체크포인트는 지금 자동차 제어기, 의료기기, 서버 운영체제에서 흔히 쓰는 기법이에요. 해밀턴은 이후 Universal Systems Language라는 설계 언어로 오류를 설계 단계에서 방지하는 연구를 이어 갔고, 130편이 넘는 논문을 발표했습니다.

## 참고 출처

- [[MIT News] Margaret Hamilton, computing pioneer who led software development for the Apollo program, dies at 90 (2026-10-07)](https://news.mit.edu/2026/margaret-hamilton-computing-pioneer-dies-1007)
- [[The Boston Globe] Margaret Hamilton 부고 (2026-10-07, 사망일·이력)](https://www.bostonglobe.com/2026/10/07/nation/margaret-hamilton-apollo-software-mit/)
- [[NPR] Apollo software pioneer Margaret Hamilton dies at 90 (2026-10-08)](https://www.npr.org/2026/10/08/nx-s1-5994972/margaret-hamilton-obituary-software-engineer-apollo)
- [[Don Eyles] Tales from the Lunar Module Guidance Computer (1202·1201 경보 원인과 처리, AGC 사양)](https://www.doneyles.com/LM/Tales.html)
