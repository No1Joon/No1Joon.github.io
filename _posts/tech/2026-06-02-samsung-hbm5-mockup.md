---
title: "삼성전자 HBM5 목업 첫 공개 — 발열을 먼저 잡은 이유"
description: "컴퓨텍스 2026 에서 공개된 7세대 HBM 의 방열 기술 Heat Path Block 과 2나노 베이스 다이 계획을 정리합니다"
date: 2026-06-02
category: Tech
subcategory: News
tags: [samsung, hbm5, memory, semiconductor, computex]
image: /assets/og/2026-06-02-samsung-hbm5-mockup.png
---

삼성전자가 차세대 AI 메모리 'HBM5'의 실물 목업(mockup, 실물 모형)을 처음 공개했어요.

6월 2일 대만 타이베이에서 열린 컴퓨텍스(Computex) 2026 현장에서였는데요.

HBM 시장의 주도권을 두고 SK하이닉스를 추격하는 삼성의 '다음 카드'가 드디어 윤곽을 드러냈습니다. 핵심은 두 가지, 바로 발열과 2나노였어요.

![삼성전자 로고](/assets/images/tech/samsung-hbm5-mockup/01-logo-samsung.webp)
*삼성전자 로고 — 출처: Samsung*

## 무슨 일이 있었나

삼성전자는 컴퓨텍스 2026에서 7세대 고대역폭 메모리(HBM, High Bandwidth Memory)인 HBM5의 목업을 선보였다.

The Korea Herald에 따르면 이번 공개의 주인공은 'Heat Path Block(열 전달 경로 블록)'이라는 새 방열 기술이에요. 메모리를 더 높이 쌓고 데이터 속도가 빨라질수록 발열이 심해지는데, 이 열을 빼내기 위한 기술입니다.

- 7세대 HBM인 'HBM5'의 설계 방향을 목업으로 처음 공개
- 새 방열 기술 'Heat Path Block' — 열 전달 경로를 하나 더 만들어 열 저항을 낮춤
- 이 방열 기술은 이미 HBM4E에 적용(신뢰성·패키징 검증 완료), HBM5로 확대 예정
- HBM5 베이스 다이(base die)에 삼성 파운드리 2나노 공정 적용 계획 (HBM4·HBM4E의 4나노에서 미세화)

## HBM이 뭐길래

HBM은 쉽게 말해 'AI 가속기 전용 초고속 메모리'예요.

일반 D램을 옆으로 늘어놓는 대신, 여러 층으로 수직으로 쌓아 올려 데이터가 오가는 길(대역폭)을 확 넓힌 메모리입니다. 엔비디아(NVIDIA)의 AI 가속기 바로 옆에 붙어, 거대한 AI 모델이 요구하는 막대한 데이터를 끊김 없이 공급하는 역할을 하죠.

AI 열풍으로 가속기가 불티나게 팔리면서, 그 옆에 반드시 따라붙는 HBM도 메모리 업계에서 가장 비싸고 가장 치열한 제품이 됐어요.

## 자세히 보기 — 숫자로 본 로드맵

삼성의 HBM 라인업은 지금 빠르게 세대 교체 중이에요.

- HBM4: 올해 초 양산 시작. 핀당 11.7Gbps(최대 13Gbps), 4나노 로직 베이스 다이
- HBM4E: 핀당 14~16Gbps, 대역폭 4TB/s급. 샘플이 막 출하되기 시작
- HBM5: 7세대. 이번엔 목업·방열 기술 위주라 구체 성능 수치는 아직 미정
- HBM5E: 차세대 1d D램 적용 계획(현 HBM4·HBM4E의 1c D램에서 진화) — 아직 개발 단계

여기서 '2나노 베이스 다이'가 의미 있는 이유가 있어요. 베이스 다이는 메모리 칩 아래에서 데이터를 정리하고 내보내는 일종의 '관제탑'인데, 이걸 더 미세한 공정으로 만들수록 전력 효율과 처리 성능을 끌어올릴 수 있거든요. 삼성은 HBM4·HBM4E엔 4나노를 썼는데, HBM5에선 2나노로 한 단계 더 미세화하겠다는 겁니다.

삼성전자 메모리개발실 황상준 부사장은 앞서 엔비디아 GTC에서 HBM5에 2나노 공정을 쓰겠다고 밝혔다고 ETNews가 전했어요.

## 배경 / 맥락 — 왜 지금, 누구와 싸우나

지금 HBM 시장을 이끄는 건 SK하이닉스예요. 엔비디아에 HBM을 주력으로 공급하며 앞서 나가고 있고, 삼성전자는 그 격차를 좁혀야 하는 추격자 입장입니다.

그래서 삼성의 전략은 '물량'과 '기술'을 동시에 미는 모양새예요. 삼성은 2026년 HBM 매출을 작년의 3배 이상으로 키우겠다는 목표를 내놨고, HBM 생산능력도 현재 월 약 17만 장에서 2026년 말 약 25만 장으로(약 47% 증가) 끌어올릴 계획이라고 전해집니다.

여기에 이번 컴퓨텍스에서 HBM5 목업과 방열 기술까지 공개하며 "차세대 기술도 준비돼 있다"는 신호를 던진 셈이에요.

## 이게 왜 중요할까

HBM은 단순한 부품 하나가 아니라, 한국 반도체 산업의 'AI 시대 성적표'에 가까워요.

메모리 시장이 D램·낸드 같은 범용 제품 위주에서 HBM 같은 고부가 AI 메모리로 무게중심을 옮기는 중이고, 그 흐름의 승자가 누가 되느냐에 따라 삼성과 SK하이닉스의 위상이 갈립니다.

시장 자체도 폭발적이에요. 시장조사업체 옴디아(Omdia)는 글로벌 HBM 시장이 2026년 $58.9B(약 82조 원)에서 2029년 $198.3B(약 278조 원)로 3배 이상 커질 것으로 전망했습니다.

## 앞으로 주목할 점

- HBM5의 구체적 성능(대역폭·속도)과 양산 시점 — 이번엔 목업 단계라 추후 공개될 듯
- 1d D램 양산 성공 여부 — HBM5E의 핵심이자 아직 개발 단계
- 2나노 베이스 다이가 실제 수율·전력 효율로 이어질지
- SK하이닉스의 맞대응과 엔비디아 차세대 가속기의 HBM 채택 동향

HBM5는 아직 목업 단계지만, 발열과 베이스 다이라는 'AI 메모리의 진짜 승부처'를 정조준한 공개였어요. 양산 로드맵이 더 나오면 그때 다시 정리해서 가져올게요 :)

## 참고 출처

- [[The Korea Herald] Samsung reveals HBM5 mockup in bid to regain AI memory lead (2026.06.02)](https://www.koreaherald.com/article/10762419)
- [[TrendForce] Samsung Reportedly Eyes 2nm Base Die for HBM5, 1d DRAM for HBM5E; HBM4 to Exceed 50% of Output (2026.03.18)](https://www.trendforce.com/news/2026/03/18/news-samsung-reportedly-eyes-2nm-base-die-for-hbm5-1d-dram-for-hbm5e-hbm4-to-exceed-50-of-output/)
- [[Samsung Semiconductor] Samsung Ships Industry-First Commercial HBM4 With Ultimate Performance for AI Computing](https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/)
