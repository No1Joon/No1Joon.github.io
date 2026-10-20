---
title: "Anthropic AI 자기복제 실험 — TV 박스 15대로 모델 구동"
description: "Anthropic 프런티어 레드팀이 저가 Android TV 박스 15대에 오픈 모델을 분산 배치해 데이터센터 없는 자기복제 가능성을 평가한 연구를 정리합니다"
date: 2026-10-20
category: AI
subcategory: News
tags: [anthropic, self-replication, ai-safety, red-team, iot]
image: /assets/og/2026-10-20-anthropic-iot-self-replication.png
---

Anthropic 프런티어 레드팀이 2026년 10월 12일 자기복제 AI 연구를 공개했어요

Android TV 박스 15대에 오픈 모델 하나를 분산해 배치했어요!
박스 한 대 값은 약 7만 7,000원(55달러)이에요

데이터센터 없이도 AI가 다른 기기로 스스로 복제될 수 있는지 평가한 실험이에요

![자기복제 4단계 흐름도](/assets/images/ai/anthropic-iot-self-replication/01-hero.webp)
*자기복제 4단계 흐름도 — 출처: Anthropic*

## 연구 개요

![Anthropic 로고](/assets/images/ai/anthropic-iot-self-replication/02-logo-anthropic.webp)
*Anthropic 로고*

작은 **오픈 가중치 모델**이 값싼 IoT 기기로 스스로 퍼질 수 있는지를 시험했어요
오픈 가중치 모델은 누구나 가중치를 내려받아 실행할 수 있도록 공개한 모델이에요

연구팀은 복제를 네 단계로 나눴어요

[네트워크 탐색]
감염시킬 기기를 찾는 단계

[침투와 페이로드 전달]
기기에 침입해 모델 파일을 전송하는 단계

[추론 설정]
그 기기에서 모델 추론을 실행할 서버를 구축하는 단계

[복제]
복제된 기기에서 다시 다른 기기로 복제를 시도하는 단계

연구가 집중한 곳은 <mark>세 번째 단계인 추론 설정</mark>이에요
앞의 두 단계는 해킹 기술이라 일부러 단순하게 처리했다고 밝혔어요

## 실험 수치

![모델별 추론 설정 소요 시간 범위 막대](/assets/images/ai/anthropic-iot-self-replication/03-chart.webp)
*모델별 추론 설정 소요 시간 범위 막대 — 출처: Anthropic 자료 기반 자가 렌더*

### 📺 TV 박스 15대 시연

Google의 **Gemma4-26B-A4B**를 TV 박스 15대에 나누어 배포했어요
한 대당 램은 4GB이고 상표가 없는 저가 제품이에요

여러 기기가 모델의 계층별 연산을 분담하는 **파이프라인 병렬** 방식이에요
속도는 <mark>초당 0.39토큰</mark>이었어요

### 🧰 추론 설정 성공률

9B 모델은 시험 대상 하드웨어 <mark>9종 중 8종</mark>에서 추론 서버를 구동했어요
대상에는 NVIDIA Jetson Nano, Orange Pi, Mac, RTX 4090이 들어 있어요

설정 한 번에 걸리는 시간은 Qwen3.5-9B가 28~51시간이에요
Gemma4-26B-A4B는 71~150시간으로 추산했어요

### 🔁 끝까지 복제한 모델

Android 15 에뮬레이터 8대로 구성된 환경에서 복제 전 과정을 시험했어요
끝까지 성공한 오픈 모델은 **GLM-5.2** 하나뿐이에요

5회 중 4회는 <mark>8대 전부</mark>, 나머지 1회에는 7대까지 복제됐어요
시험한 다른 오픈 모델은 매번 실패했어요

추론 설정을 스크립트로 처리해 주면 결과가 달라졌어요
3B 모델도 17대짜리 네트워크에서 절반 가까이 퍼졌어요

### 🧬 복제 세대별 추론 설정 성공률

부모 복제본이 다음 세대 복제본에 코드와 메모를 전달하게 하자 성공률이 올랐어요
Qwen3.5-9B의 추론 설정 성공률이 1세대 45%에서 이후 <mark>61~84%</mark>가 됐어요

더 강한 Claude Opus 4.8에게 조언을 받게 해도 성공률은 크게 오르지 않았어요

## 전제 조건과 남은 빈칸

![기기 검색엔진에 잡힌 카메라 관리 화면, 식별 정보 가림](/assets/images/ai/anthropic-iot-self-replication/04-photo.webp)
*기기 검색엔진에 잡힌 카메라 관리 화면, 식별 정보 가림 — 출처: Anthropic*

기기 검색엔진에서는 인터넷에 노출된 카메라 관리 화면이 검색돼요
연구팀은 감염 대상을 찾는 첫 단계가 이미 어렵지 않다고 봤어요

다만 이번 침투 실험은 <mark>인증 없는 ADB 포트</mark>의 외부 접속을 허용한 상태에서 진행했어요
**ADB**(Android Debug Bridge)는 개발자가 Android 기기를 원격으로 다루는 통로예요

연구팀도 이 결과를 <u>현실 성공률의 상한</u>으로 읽어야 한다고 밝혔어요
실제 TV 박스를 감염시킨 실험은 없었어요!

| 단계 | 실험 조건 | 판정 |
| :--- | :--- | :--- |
| 기기 찾기 | 대상 8대를 미리 지정 | [미검증] |
| 침투 | 인증 없는 ADB 포트 | [미검증] |
| 추론 설정 | 하드웨어 9종 중 8종 | **검증** |
| 복제 | GLM-5.2, 5회 중 4회 | **검증** |
| 실기기 감염 | 시험하지 않음 | [미검증] |

## 킴울프 봇넷으로 본 규모

![Kimwolf 규모 추산 가로 막대](/assets/images/ai/anthropic-iot-self-replication/05-chart.webp)
*Kimwolf 규모 추산 가로 막대 — 출처: Anthropic 자료 기반 자가 렌더*

연구팀은 실제 봇넷 **Kimwolf**의 규모를 기준으로 계산했어요
Kimwolf는 저가 Android TV 박스와 셋톱박스를 주로 감염시킨 봇넷이에요

![Android 로고](/assets/images/ai/anthropic-iot-self-replication/06-logo-android.webp)
*Android 로고*

최대 <mark>200만 대 이상</mark>을 감염시킨 것으로 알려졌어요
복제본 하나가 기기 15대로 구성된다고 가정하면 약 13만 3,000개가 나와요

그래도 전부 합친 연산량은 **H100 약 40대** 수준이에요
연구팀은 연산량보다 <mark>중앙 서버가 없어 모든 복제본의 실행을 중단하기 어렵다는 점</mark>을 위험으로 꼽았어요

확산 속도가 느려 복제본 수가 두 배가 되는 데 며칠이 걸린다고 봤어요

### 📈 2026년 말이라는 시점

30B 이하 오픈 모델의 능력 지수(ECI)는 해마다 13.7점씩 올랐어요
이 추세면 2026년 말 작은 모델이 GLM-5.2 수준에 닿는다는 계산이에요

연구팀도 ECI는 복제 능력을 간접적으로 가늠하는 대략적인 지표라고 밝혔어요

## 국내 접점

![KISA 로고](/assets/images/ai/anthropic-iot-self-replication/07-logo-kisa.webp)
*KISA 로고*

보안뉴스 보도에서 Kimwolf 감염 기기가 브라질, 인도, 미국 등에서 확인된 것으로 나왔어요
감염이 몰린 나라로 한국이 거론되지는 않았어요

같은 종류의 저가 TV 박스는 해외 직구 쇼핑몰에서 쉽게 살 수 있어요
**X96Q** 같은 모델명이 감염 기기로 보도된 적이 있어요

국내 KISA **IoT 보안인증** 기준에는 공통 비밀번호 금지 항목이 있어요
2026년 4월 기준 인증 제품은 <mark>249건</mark>이에요

인증은 의무가 아니라 업체가 신청하는 제도예요
같은 보도에서 홈캠 인증은 2건뿐이었어요!!

## 지금 할 수 있는 조치

### 🏠 사용자

![사용자 조치 정리 카드](/assets/images/ai/anthropic-iot-self-replication/08-items.webp)
*사용자 조치 정리 카드 — 출처: 본문 요약 카드 자가 렌더*

🔗 링크 첨부 - https://www.boho.or.kr

### 🏭 제조사와 통신사

연구팀은 감염 기기 한 대가 새로 감염시키는 수를 1 아래로 낮추는 게 목표라고 했어요
기기끼리 수 GB를 주고받으므로 통신사가 트래픽 흐름을 감시하면 탐지할 수 있다고 봤어요

통신사가 감염 가입자를 격리하고 알렸을 때 Mirai 감염 사례의 <mark>92%</mark>가 14일 안에 해소됐어요
알리지 않았을 때는 74%였어요

영국은 기본 비밀번호를 쓴 IoT 기기를 규정 위반으로 정했어요
연구팀은 <u>기기 출고 시 기본 보안 설정을 강화하도록</u> 제조사에 요구했어요

## 앞으로 주목할 점

- 작은 오픈 모델이 2026년 말 GLM-5.2 수준에 닿는지
- 연구팀이 비워 둔 침투 단계까지 넣은 후속 실험
- **IoT 보안인증** 의무화 요구가 제도로 이어지는지

## 참고 출처

- [[Anthropic] AI models may be capable of self-replicating without access to a datacenter (연구 원문, 2026-10-12)](https://www.anthropic.com/research/self-replicating-ai)
- [[보안뉴스] 킴울프, 안드로이드 TV 180만 대 장악 후 디도스 공격 악용 (2025-12-21)](https://www.boannews.com/news/articleView.html?idxno=141082)
- [[The Hacker News] Kimwolf Android botnet infects over 2 million devices (2026-01)](https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html)
- [[머니투데이방송] 기준은 있는데 작동 안 한다, 홈캠 보안 공백 (IoT 보안인증 249건, 2026-04-24)](https://news.mtn.co.kr/news-detail/2026042416401853507)
- [[CE Pro] BADBOX 2.0, 저가 안드로이드 TV 기기 대상 봇넷 (공장 단계 백도어 보고)](https://www.cepro.com/news/badbox-2-botnet-targetting-android-tv-devices-projectors/147345)
- 환율: 1달러 ≈ 1,400원 기준 환산
