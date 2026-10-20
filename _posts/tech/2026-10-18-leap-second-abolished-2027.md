---
title: "윤초 2027년 폐지 확정 — 서버 장애 원인이던 1초 추가가 멈춘다"
description: "국제도량형총회의 윤초 폐지 결의 내용과 윤초가 생긴 이유, 윤초 때문에 서버 장애가 났던 사례를 정리합니다"
date: 2026-10-18
category: Tech
subcategory: Explainer
tags: [leap-second, utc, timekeeping, ntp, outage]
image: /assets/og/2026-10-18-leap-second-abolished-2027.png
---

2026년 10월 15일 세계 시간 규칙이 바뀌었어요

국제도량형총회가 **윤초**를 없애기로 결의했습니다

2027년 5월 20일부터 세계 표준시에 1초를 더 추가하지 않아요

윤초로 서버 장애가 난 사례가 있어 IT 업계가 오래전부터 없애자고 요구해 온 규칙이에요

![원자시계와 자전하는 지구 사이에서 1초 조각이 빠져나가는 개념 컷](/assets/images/tech/leap-second-abolished-2027/01-agy-hero.webp)
*원자시계와 자전하는 지구 사이에서 1초 조각이 빠져나가는 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

## 결정 내용

![연대별 윤초 추가 횟수 막대 차트](/assets/images/tech/leap-second-abolished-2027/02-chart.webp)
*연대별 윤초 추가 횟수 막대 차트 — 출처: IANA tz 데이터베이스 기반 자가 렌더*

결정한 곳은 프랑스 베르사유에서 열린 **제28차 국제도량형총회(CGPM)**예요

4년마다 열려 미터·킬로그램·초 같은 단위를 정하는 회의입니다

| 항목 | 내용 |
| :--- | :--- |
| 결의일 | 2026년 10월 15일 |
| 시행일 | <mark>2027년 5월 20일</mark> |
| 허용 오차 | 1초 → 최대 3,600초 |
| 원래 목표 | 2035년까지 |

UTC(협정세계시)와 지구 자전 기준 시각의 차이가 **최대 1시간까지** 커지는 것을 허용하는 결정이에요

차이가 1시간에 닿기까지는 1,000년 넘게 걸릴 것으로 봅니다

1972년 첫 윤초 이후 27차례 추가된 윤초를 앞으로는 더 추가하지 않아요

과학자들이 이 문제를 놓고 30년 동안 논쟁해 왔어요

## 윤초의 원리

![macOS tz 데이터에 기록된 윤초 횟수와 최근 세 번](/assets/images/tech/leap-second-abolished-2027/03-term-leapseconds.webp)
*macOS tz 데이터에 기록된 윤초 횟수와 최근 세 번 — 출처: macOS IANA tz 데이터 실행 화면*

세계 표준시는 원자시와 지구 자전 기준 시각의 차이를 조정해 왔어요

[원자시]
세슘 원자시계가 재는 1초, 흔들림 없이 일정함

[천문시 UT1]
지구가 한 바퀴 도는 시간, 해마다 조금씩 달라짐

UTC는 원자시를 따르되 UT1과의 차이가 0.9초를 넘기 전에 1초를 추가해 왔어요

그 1초가 **윤초**예요

윤초를 추가하는 날 UTC 시계는 23시 59분 59초 다음에 <mark>23시 59분 60초</mark>를 한 번 더 셉니다

한국 시각으로는 1월 1일이나 7월 1일 <u>오전 8시 59분 60초</u>예요

마지막 윤초는 2016년 12월 31일 UTC, 한국 시각 2017년 1월 1일 아침에 추가됐어요

## 윤초가 일으킨 장애

![Cloudflare 2017년 윤초 장애 기록 제목과 원인 문단](/assets/images/tech/leap-second-abolished-2027/04-cloudflare-2017.webp)
*Cloudflare 2017년 윤초 장애 기록 제목과 원인 문단 — 출처: Cloudflare*

컴퓨터는 1분이 60초라고 가정하고 시간을 계산해요

61번째 초가 추가되면 그 가정과 달라져요

[2012년 6월 Reddit]
Linux 고해상도 타이머 처리에 오류가 생겨 CPU가 멈춤, 30~40분 접속 불가

[2017년 1월 Cloudflare]
측정한 응답 시간이 음수가 돼 DNS 서버에서 오류 발생, 최대 0.2% 질의 실패

Cloudflare 장애는 1월 1일 0시 UTC에 시작해 6시간 45분 동안 이어졌어요

시간 측정값이 이전 값보다 작아질 수 없다고 가정한 코드 한 줄이 원인이었어요!

그래서 대형 업체는 윤초 1초를 하루에 걸쳐 분산 반영하는 **leap smear**를 써 왔어요

| 업체 | 스미어 방식 |
| :--- | :--- |
| Google | 24시간 선형, 1초당 약 11.6μs |
| Meta | <mark>17시간</mark>, 2차 함수 |

Meta는 2022년 엔지니어링 블로그에서 윤초를 더 넣지 말자는 움직임을 지지했어요

27차례에서 멈추자는 업계 제안이에요

<mark>윤초 1초는 시간이 되돌아가지 않는다는 코드의 가정과 맞지 않아 오류를 일으켜 왔습니다</mark>

## 일정을 앞당긴 음의 윤초

![Nature 2024년 Agnew 논문 제목과 초록, 2029년 음의 윤초 예측 하이라이트](/assets/images/tech/leap-second-abolished-2027/05-nature-agnew.webp)
*Nature 2024년 Agnew 논문 제목과 초록, 2029년 음의 윤초 예측 하이라이트 — 출처: Nature*

원래 폐지 목표는 2035년이었어요

앞당긴 이유는 **음의 윤초**예요

지구 자전이 빨라지면 1초를 더하는 게 아니라 빼야 합니다

UTC 시계가 23시 59분 58초에서 곧바로 다음 날 0시로 넘어가요

윤초 역사 54년 동안 한 번도 없었던 일이라 소프트웨어가 검증된 적이 없어요!!

Scripps 해양연구소의 **Duncan Carr Agnew**가 이 시점을 계산했어요

2024년 3월 Nature에 실린 논문이에요

[예측]
지금 정의대로면 2029년까지 음의 윤초가 필요

[원인]
지구 액체 핵의 회전이 줄면서 나머지 지구의 자전이 빨라짐

[얼음]
그린란드·남극 얼음이 녹아 자전이 늦춰졌고, 이게 없었다면 3년 일렀음

국제도량형국(BIPM)은 2035년까지 음의 윤초가 필요할 확률을 약 30%로 봤어요

미국 해군천문대 Nick Stamatakos도 음의 윤초 회피를 큰 이유로 꼽았어요

## 바뀌는 것과 그대로인 것

휴대폰·PC 시계와 **한국 표준시는 그대로**예요

한국은 UTC보다 9시간 빠른 체계를 유지하고, 사용자가 따로 설정을 바꿀 필요는 없어요

바뀌는 쪽은 <u>정밀한 시간 동기화를 쓰는 곳</u>이에요

통신망·데이터센터·금융 거래·위성항법이 여기에 들어가요

다만 GPS 시각과 UTC 사이에는 기존의 18초 차이가 그대로 유지돼요

국내 표준시를 관리하는 **한국표준과학연구원**은 PC 시각을 표준시에 맞추는 프로그램 UTCk를 배포하고 있어요

2026년 10월 18일 기준 이 결정에 대한 연구원의 공식 안내는 찾지 못했어요

![윤초 폐지로 바뀌는 것과 그대로인 것 정리 카드](/assets/images/tech/leap-second-abolished-2027/06-items.webp)
*윤초 폐지로 바뀌는 것과 그대로인 것 정리 카드 — 출처: CGPM 결의 보도 기반 자가 렌더*

## 참고 출처

- [[Scientific American] 국제도량형총회 윤초 폐지 결의, 시행일·허용 오차·관계자 발언 (2026-10-15)](https://www.scientificamerican.com/article/scientists-vote-to-end-leap-seconds-redefining-how-the-world-keeps-time/)
- [[지디넷코리아] 윤초 폐지와 2035년 목표를 앞당긴 이유, BIPM 확률 추정 (2026-10-16)](https://zdnet.co.kr/view/?no=20261016191813)
- [[BIPM] 제27차 CGPM 결의 4, 2035년 목표와 허용 오차 재정의 요청 (2022)](https://www.bipm.org/en/cgpm-2022/resolution-4)
- [[Nature] Agnew, A global timekeeping problem postponed by global warming (2024, 본문 이미지 출처)](https://www.nature.com/articles/s41586-024-07170-0)
- [[Cloudflare Blog] 2017년 윤초 DNS 장애 기록 (2017-01-01)](https://blog.cloudflare.com/how-and-why-the-leap-second-affected-cloudflare-dns/)
- [[Engineering at Meta] It's time to leave the leap second in the past (2022-07-25)](https://engineering.fb.com/2022/07/25/production-engineering/its-time-to-leave-the-leap-second-in-the-past/)
- [[Google Public NTP] Leap Smear 방식 (24시간 선형)](https://developers.google.com/time/smear)
