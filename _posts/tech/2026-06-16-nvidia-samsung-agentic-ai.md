---
title: "엔비디아·삼성 AI 동맹 — 에이전틱 AI 로 다시 짜는 반도체 설계·제조"
description: "GTC 2026 과 컴퓨텍스 2026 을 관통한 에이전틱 AI 협력이 메모리 공급을 넘어 어디까지 확장됐는지 정리합니다"
date: 2026-06-16
category: Tech
subcategory: News
tags: [nvidia, samsung, agentic-ai, semiconductor, foundry]
image: /assets/og/2026-06-16-nvidia-samsung-agentic-ai.png
---

올해 반도체 업계의 두 거대 무대인 **GTC 2026(3월)**과 **컴퓨텍스 2026(6월)**을 관통한 키워드는 하나였어요. 바로 **'에이전틱 AI(Agentic AI)'**입니다.

그 중심에 엔비디아(NVIDIA)와 삼성전자(Samsung)의 'AI 동맹'이 있어요. 메모리 공급을 넘어 반도체 설계·제조 방식 자체를 AI로 바꾸는 그림인데요. 핵심만 정리해볼게요.

## 무슨 일이 있었나

엔비디아와 삼성전자는 GTC 2026과 컴퓨텍스 2026을 거치며 **에이전틱 AI 협력**을 전방위로 확대했어요. 단순 부품 거래가 아니라, AI가 칩을 설계·검증·생산하는 '에이전틱 AI 팩토리' 구상이 핵심입니다.

- 삼성이 GTC 2026에서 **6세대 HBM4(고대역폭 메모리)**와 **HBM4E**를 공개, 엔비디아 **베라 루빈(Vera Rubin)** 플랫폼용으로 양산 돌입
- 송용호 삼성전자 AI센터장이 **'설계부터 제조까지 에이전틱 AI로 반도체 엔지니어링 혁신'** 세션 발표
- 컴퓨텍스 2026(6월 1~5일, 타이베이·주제 'AI Together')에서 엔비디아가 **베라 루빈 풀 생산**과 에이전틱 AI 팩토리 비전 공개
- 젠슨 황 CEO가 삼성을 콕 집어 **파운드리 협력(그록 LPU 생산)**까지 언급하며 'AI 동맹' 확장 강조

![송용호 삼성전자 AI센터장 NVIDIA GTC 2026 '에이전틱 AI 반도체 엔지니어링' 발표](/assets/images/tech/nvidia-samsung-agentic-ai/01-press-samsung-gtc2026.webp)
*송용호 삼성전자 AI센터장 NVIDIA GTC 2026 '에이전틱 AI 반도체 엔지니어링' 발표 — 출처: Samsung*

## 자세히 보기 — 에이전틱 AI로 반도체를 짓는다

이번 협력의 진짜 핵심은 **'에이전틱 AI가 반도체 설계와 제조에 직접 들어왔다'**는 점이에요.

삼성 설명에 따르면, AI가 **트랜지스터 사이징·회로 최적화** 같은 설계 작업을 자동화해 **설계 턴어라운드(TAT) 시간을 약 50% 단축**한다고 해요. 단순 보조가 아니라 설계 흐름을 스스로 돌리는 수준입니다.

제조 단계에서는 **엔비디아 옴니버스(Omniverse) 기반 디지털 트윈(digital twin)**으로 **실시간 모니터링·예측 위험 평가·선제 개입**을 구현해요. **전자설계자동화(EDA)**와 **컴퓨테이셔널 리소그래피**부터 첨단 공장의 설계·운영까지 AI가 관여합니다.

특히 HBM4E처럼 미세한 공정 변동도 수율에 큰 영향을 주는 영역에서, 삼성은 기존 **제조실행시스템(MES)**을 넘어 **에이전틱 AI로 품질 관리를 진화**시키고 있어요. 대규모 제조 데이터를 실시간 분석해 이상의 근본 원인을 빠르게 찾아내는 방식입니다.

## 메모리·칩 — HBM4부터 파운드리까지

하드웨어 공급에서도 협력 범위가 넓어졌어요.

- 삼성 **HBM4**는 양산 상태로 베라 루빈용 설계, 처리속도 **11.7Gbps**(업계 표준 8Gbps 상회, 최대 13Gbps까지 확장)
- 베라 루빈에는 **Rubin GPU용 HBM4 + Vera CPU용 LPDDR5X 기반 SOCAMM2**가 적용
- 젠슨 황은 삼성·SK하이닉스·마이크론 **3사 모두 HBM4 공급 자격(퀄)을 통과**했다고 밝힘
- 삼성이 **그록(Groq)의 'Groq3' LPU(언어처리장치) 칩을 파운드리로 생산** — HBM·모듈·저장장치에 이어 협력 확대

![엔비디아(NVIDIA) 로고](/assets/images/tech/nvidia-samsung-agentic-ai/02-logo-nvidia.webp)
*엔비디아(NVIDIA) 로고 — 출처: NVIDIA*

## 배경 / 맥락

컴퓨텍스 2026은 152개국에서 11만여 명이 찾은 대형 무대였고, 엔비디아는 여기서 **베라 루빈을 에이전틱 AI 팩토리의 엔진**으로 내세웠어요. 메모리·연산·소프트웨어가 한 몸처럼 묶여야 'AI가 일하는 공장'이 돌아간다는 메시지였죠.

엔비디아는 케이던스·다쏘시스템·PTC·지멘스·시놉시스 등과 손잡고 **CUDA-X·옴니버스 기반 산업용 소프트웨어**를 제공해요. 삼성·SK하이닉스·TSMC가 이 스택 위에서 설계·엔지니어링·제조를 가속하는 에이전틱 솔루션을 선보였습니다.

![삼성전자(Samsung) 로고](/assets/images/tech/nvidia-samsung-agentic-ai/03-logo-samsung.webp)
*삼성전자(Samsung) 로고 — 출처: Samsung*

## 이게 왜 중요할까

한국 산업 관점에서 의미가 커요. 삼성은 **메모리(HBM4) 주도권 + 파운드리(그록 LPU) 반등**이라는 두 축을 엔비디아 동맹 위에서 동시에 챙기게 됐거든요.

또 '에이전틱 AI로 반도체를 만든다'는 흐름은 **설계·수율·납기**라는 제조 경쟁력의 핵심 지표를 직접 끌어올립니다. AI가 단순 챗봇을 넘어 **산업 현장의 엔지니어링 도구**로 자리 잡는 대표 사례라, 국내 반도체·장비·소프트웨어 생태계에도 파급이 클 전망이에요.

## 앞으로 주목할 점

- 삼성 HBM4/HBM4E의 **베라 루빈 본격 공급 물량·점유율**
- 삼성 파운드리의 **그록 LPU 양산 성과**와 추가 고객 확보
- 에이전틱 AI 설계·제조의 **실측 수율·납기 개선** 데이터
- SK하이닉스·마이크론·TSMC와의 **공급 경쟁 구도** 변화

부품 공급사를 넘어 'AI로 칩을 만드는 파트너'로 관계가 바뀌는 흐름이라, 저는 다음 분기 실적과 공급 물량에서 이 동맹의 진짜 성적표가 나올 거라고 봐요.

## 참고 출처

- [[Samsung Semiconductor] Samsung Showcases Agentic AI–Driven Semiconductor Engineering at NVIDIA GTC 2026](https://semiconductor.samsung.com/news-events/tech-blog/samsung-showcases-agentic-ai-driven-semiconductor-engineering-innovation-at-nvidia-gtc-2026/)
- [[Samsung Semiconductor] Samsung Unveils HBM4E, NVIDIA Partnership at GTC 2026 (03.16)](https://semiconductor.samsung.com/news-events/news/samsung-unveils-hbm4e-showcasing-comprehensive-ai-solutions-nvidia-partnership-and-vision-at-nvidia-gtc-2026/)
- [[서울경제] 젠슨 황 "생큐 삼성"…HBM 이어 파운드리로 진화한 AI 동맹](https://www.sedaily.com/article/20020593)
- [[머니투데이] 젠슨 황 "삼성·하이닉스 HBM4 퀄 통과…베라 루빈 공급 경쟁" (06.05)](https://www.mt.co.kr/industry/2026/06/05/2026060515111684507)
- [[헤럴드경제] 젠슨 황 "40년 된 PC, 에이전틱 AI 맞춰 완전히 재발명" [GTC 타이베이]](https://biz.heraldcorp.com/article/10762135)
- [[인벤] 엔비디아, GTC 2026서 한국 기업들과 AI 협력 확대](https://www.inven.co.kr/webzine/news/?news=314575)
