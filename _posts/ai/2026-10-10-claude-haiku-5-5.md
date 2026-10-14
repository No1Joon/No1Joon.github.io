---
title: "Claude Haiku 5.5 출시 — Haiku 4.5 의 10분의 1 요금"
description: "Claude 5.5 계열 마지막 모델 Haiku 5.5 의 요금과 컴퓨터 조작 벤치마크, 전환할 때 바꿀 설정을 정리합니다"
date: 2026-10-10
category: AI
subcategory: News
tags: [anthropic, claude-haiku, llm, pricing, computer-use]
image: /assets/og/2026-10-10-claude-haiku-5-5.png
---

Anthropic이 2026년 10월 7일 Claude Haiku 5.5를 공개했습니다. 프롬프트 10만 토큰 이하 기준 100만 토큰당 입력 140원(0.10달러), 출력 700원(0.50달러)으로 Haiku 4.5의 10분의 1이고, 컴퓨터 조작 벤치마크 OSWorld 2.1 점수는 15.7%에서 72.4%로 상승했어요. 9월 22일 Opus 5.5, 9월 28일 Sonnet 5.5에 이어 Claude 5.5 계열 세 모델이 모두 공개됐습니다.

![Claude Haiku 5.5 발표 키 비주얼](/assets/images/ai/claude-haiku-5-5/01-hero-keyart.webp)
*Claude Haiku 5.5 발표 키 비주얼 — 출처: Anthropic*

## 발표 내용

Haiku는 Claude 모델 가운데 가장 작고 빠른 계열이에요. Anthropic은 Haiku 5.5를 요약, 컨텍스트 압축(compaction), 데이터베이스 조회, 분류처럼 양이 많고 비용에 민감한 작업용으로 소개했고, 코딩 작업에서 Opus 5.5·Sonnet 5.5가 맡긴 일을 처리하는 서브에이전트(sub-agent)로 쓰는 구성을 함께 제시했어요.

| 항목 | Haiku 5.5 | Haiku 4.5 |
| :--- | :--- | :--- |
| 컨텍스트 윈도 | **100만 토큰** | 20만 토큰 |
| 최대 출력 | 12만 8천 토큰 | 6만 4천 토큰 |
| 추론 조절 | effort 5단계 | 토큰 예산 지정 |
| 지식 컷오프 | 2026년 6월 | 2025년 2월 |

effort는 모델이 답변을 생성하기 전에 추론 강도를 정하는 설정으로, Low·Medium·High·Xhigh·Max 다섯 단계가 있고 API 기본값은 Medium이에요. Haiku에 effort가 적용된 것은 처음입니다. Claude API와 Amazon Web Services, Google Cloud, Microsoft Azure(Foundry)에서 바로 쓸 수 있어요.

## 벤치마크

![OSWorld 2.1 모델별 점수 차트](/assets/images/ai/claude-haiku-5-5/02-chart-osworld.webp)
*OSWorld 2.1 모델별 점수 차트 — 출처: Anthropic 발표 페이지 기반 자가 렌더*

가장 크게 상승한 점수는 컴퓨터 화면을 보고 조작하는 *OSWorld 2.1*이에요. Haiku 4.5는 15.7%였는데 Haiku 5.5는 72.4%를 기록해, OpenAI의 소형 모델 GPT-6 Luna(48.9%)보다 23.5%포인트 높고 Sonnet 5.5(83.9%)와는 11.5%포인트 차이예요.

| 벤치마크 | Haiku 5.5 | Haiku 4.5 |
| :--- | :--- | :--- |
| Terminal-Bench 4.0 | **39.2%** | 0.0% |
| HLE (도구 없음) | **45.9%** | 10.2% |
| HLE (도구 사용) | **57.4%** | 18.7% |
| Chartography (도구 없음) | **46.4%** | 6.4% |
| GDPval-AA v2.1 (Elo) | **1,620** | 735 |

터미널 작업을 보는 *Terminal-Bench 4.0*에서는 Haiku 4.5가 0.0%였어요. Haiku 5.5는 39.2%로 GPT-6 Luna(16.4%)의 두 배를 넘었지만, Sonnet 5.5(70.6%)보다 31.4%포인트 낮아요. 코드 작성 벤치마크 *FrontierCode 1.1*은 Haiku 5.5 46.4%, GPT-6 Luna 42.4%, Sonnet 5.5 52.1%(Xhigh)로 세 모델 차이가 가장 작았습니다.

## 요금

![모델별 100만 토큰당 출력 요금 차트](/assets/images/ai/claude-haiku-5-5/03-chart.webp)
*모델별 100만 토큰당 출력 요금 차트 — 출처: Anthropic 모델 문서 기반 자가 렌더*

Haiku 5.5는 프롬프트 길이에 따라 요금이 두 구간으로 나뉘어요. 10만 토큰 이하 요청은 Haiku 4.5의 10분의 1, 10만 토큰을 넘는 요청은 Haiku 4.5의 절반이에요.

| 100만 토큰당 | 10만 이하 | 10만 초과 |
| :--- | :--- | :--- |
| 입력 | <mark>140원</mark> | 700원 |
| 출력 | <mark>700원</mark> | 3,500원 |
| 캐시 읽기 | 14원 | 70원 |
| 캐시 쓰기 | 175원 | 875원 |

요금표는 10분의 1인데 Anthropic이 밝힌 절감 폭은 평균 약 75%예요. Haiku 5.5는 Claude 4.7부터 쓰는 새 토크나이저(tokenizer, 글을 토큰으로 분할하는 규칙)를 써서 같은 글이 Haiku 4.5보다 약 30% 많은 토큰으로 계산되고, 이전 대화의 추론 블록도 입력에 계속 포함돼요. 큰 이미지는 고해상도 처리 대상에 포함돼 2,000×1,500픽셀 이미지 한 장이 Haiku 4.5보다 약 2.5배의 토큰으로 계산됩니다.

같은 발표에서 Sonnet 5.5의 캐시 읽기 요금은 100만 토큰당 280원(0.20달러)에서 140원(0.10달러)으로 인하했어요. 배치 API는 모든 모델에서 50% 할인입니다.

## 서브에이전트 구성

![큰 모델이 작은 모델들에 일을 나눠 주는 개념 컷](/assets/images/ai/claude-haiku-5-5/04-agy.webp)
*큰 모델이 작은 모델들에 일을 나눠 주는 개념 컷 — 출처: 개념 컷 · agy 자가 생성*

Opus 5.5·Sonnet 5.5 같은 큰 모델이 계획을 세우고, 파일 탐색·요약·검색처럼 단순하지만 양이 많은 작업을 여러 Haiku 5.5에 분배해 처리하도록 하는 방식이에요. 출력 요금이 Opus 5.5의 40분의 1이라, 토큰을 많이 쓰는 탐색 단계를 Haiku로 옮기면 전체 비용이 감소해요.

모델 사이 추론 블록 호환에는 방향이 있어요. Claude API와 Google Cloud에서 Opus 5.5·Sonnet 5.5는 Haiku 5.5가 생성한 추론 블록을 읽지만, Haiku 5.5는 Opus 5.5·Sonnet 5.5의 추론 블록을 읽지 못하고 API가 오류 없이 제외해요.

Anthropic은 Haiku 5.5의 안전장치를 사이버 보안 제한을 Haiku 4.5보다 엄격하고 Sonnet 5.5보다는 덜 엄격하게 설정했다고 밝혔어요. 방어 작업의 허용 범위는 확대하고 침투 테스트 같은 공격형 작업은 제한해요.

## Haiku 4.5에서 옮길 때

![Haiku 5.5 전환 시 바꿀 설정 정리 카드](/assets/images/ai/claude-haiku-5-5/05-items.webp)
*Haiku 5.5 전환 시 바꿀 설정 정리 카드 — 출처: Anthropic 마이그레이션 가이드 기반 자가 렌더*

모델 이름만 변경하면 기존에 정상 처리되던 요청이 400 오류를 반환할 수 있어요. Haiku 4.5에서 허용하던 설정 가운데 몇 가지가 Haiku 5.5에서는 지원되지 않기 때문이에요.

![Anthropic 로고](/assets/images/ai/claude-haiku-5-5/06-logo-anthropic.webp)
*Anthropic 로고*

Amazon Bedrock에서는 Haiku 5.5의 구조화 출력(structured outputs)을 쓸 수 없고, Haiku 4.5의 Priority Tier 계약도 Haiku 5.5에는 적용되지 않아요. Claude Code를 쓰고 있다면 **/claude-api migrate** 명령으로 모델 ID 교체와 위 설정 변경을 한 번에 적용할 수 있습니다. Anthropic은 Haiku 5.5를 2027년 10월 7일 이전에는 종료하지 않겠다고 밝혔어요.

## 참고 출처

- [[Anthropic] Claude Haiku 5.5 발표, 요금·벤치마크·안전장치 (2026-10-07)](https://www.anthropic.com/claude-haiku-5-5)
- [[Anthropic] 모델 개요, 컨텍스트 윈도·최대 출력·지식 컷오프·기본 effort](https://platform.claude.com/docs/en/about-claude/models/overview)
- [[Anthropic] Haiku 5.5 마이그레이션 가이드, 토크나이저·오류 설정·플랫폼 제한](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)
- [[Anthropic] Claude Haiku 5.5 시스템 카드](https://www.anthropic.com/claude-haiku-5-5-system-card)
- 환율: 1달러 ≈ 1,400원 기준 환산
