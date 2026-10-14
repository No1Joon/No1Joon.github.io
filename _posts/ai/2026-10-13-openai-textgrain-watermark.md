---
title: "OpenAI textGrain — ChatGPT 글에 보이지 않는 워터마크, EU 부터"
description: "EU AI법 대응으로 도입된 텍스트 워터마크 textGrain 의 적용 범위와 우회 내성, 한국 적용 여부를 정리합니다"
date: 2026-10-13
category: AI
subcategory: News
tags: [openai, watermark, ai-act, ai-detection, chatgpt]
image: /assets/og/2026-10-13-openai-textgrain-watermark.png
---

OpenAI가 2026년 10월 5일 ChatGPT가 생성한 글에 보이지 않는 텍스트 워터마크 textGrain을 삽입한다고 발표했어요. 첫 적용 지역은 EU이고, 앞으로 몇 주에 걸쳐 EU 안의 ChatGPT·Codex 텍스트 출력에 적용됩니다.

EU AI법이 생성형 AI 출력에 기계가 읽을 수 있는 표시를 요구하면서 도입된 조치예요. 한국 사용자의 ChatGPT 출력에는 기본으로 적용되지 않고, 탐지기도 일반에 공개되지 않습니다.

![OpenAI 2026년 10월 5일 공지 Our approach to EU text provenance rules](/assets/images/ai/openai-textgrain-watermark/01-capture.webp)
*OpenAI 2026년 10월 5일 공지 Our approach to EU text provenance rules — 출처: OpenAI*

## 발표 내용

지역마다 적용 방식이 다르고, 텍스트에만 해당하는 내용입니다.

- EU: 몇 주에 걸쳐 전 요금제 ChatGPT·Codex의 해당 텍스트 출력에 워터마크 적용
- API: 10월 5일부터 전 세계 고객이 일부 모델에서 직접 활성화할 수 있음, 기본값은 비활성화
- 탐지기: 승인된 연구자·전문기관만 신청 가능, 일반 공개는 하지 않음
- 클라우드 파트너를 거쳐 쓰는 OpenAI 모델에도 몇 주 안에 선택 적용 예정

이미지와 오디오는 이미 별도 체계가 있어요. OpenAI는 생성 이미지에 C2PA 콘텐츠 자격 증명과 SynthID 워터마크를 삽입하고 openai.com/verify에서 누구나 확인하게 했지만, 텍스트 탐지기는 오탐과 미탐 위험 때문에 공개하지 않는다고 밝혔습니다.

## 작동 방식과 탐지 성능

textGrain은 모델이 다음 단어를 선택할 때 비밀 키에서 나온 무작위 값과 연결해, 단어 선택에 통계적 신호를 삽입합니다. 같은 날 공개된 기술 리포트에 따르면 Gumbel 값과 KL 정규화를 쓴 최적 수송 문제로 단어 선택을 키에 연계하고, 신호 세기는 생성 다양성(엔트로피)을 얼마나 줄일지에 따라 정해요. 탐지기는 글과 키만 있으면 되고, 생성 때 쓴 설정 값을 몰라도 됩니다.

![글 길이와 종류에 따른 워터마크 탐지율 그래프](/assets/images/ai/openai-textgrain-watermark/02-capture.webp)
*글 길이와 종류에 따른 워터마크 탐지율 그래프 — 출처: OpenAI*

성능은 사람이 쓴 글을 AI 글로 잘못 분류하는 오탐률을 1%로 설정한 상태에서 측정했어요. 심리학 같은 설명형 글은 200토큰에서 약 80%, 400토큰에서 약 95%를 탐지했습니다. 수학 글은 같은 길이에서 훨씬 낮아 400토큰에서도 60% 안팎이에요. 수식과 용어가 정해진 글은 다른 단어를 선택할 여지가 적어 신호를 삽입할 기회가 적기 때문입니다.

OpenAI는 자체 평가에서 textGrain이 Google의 SynthID 텍스트와 같거나 더 나았다고 밝혔지만, 비교표는 공개하지 않았어요.

## 편집하면 약해지는 신호

글을 수정하면 신호가 빠르게 감소해요. OpenAI가 400토큰 글에서 단어 일부를 동의어로 치환한 결과입니다.

![편집 정도에 따른 워터마크 탐지율 그래프](/assets/images/ai/openai-textgrain-watermark/03-capture.webp)
*편집 정도에 따른 워터마크 탐지율 그래프 — 출처: OpenAI*

단어 10%만 바꿔도 탐지율은 92%에서 66%로, 25%를 바꾸면 17%로 감소합니다. 공지는 번역한 글이나 짧은 글도 탐지가 어렵다고 적었어요. 그래서 워터마크가 탐지되지 않았다고 사람이 쓴 글이라는 증거가 되지 않는다는 점을 OpenAI가 직접 지적했습니다.

9월 11일 글에서 살펴본 SynthID 논문은 같은 ELI5 질문 모음으로 400토큰 탐지율 약 87%(Gemma 7B, 오탐률 1%)를 보고했어요. 모델과 조건이 달라 두 수치를 직접 비교할 수는 없고, 길이가 길수록 탐지율이 높고 표현 선택지가 적을수록 탐지율이 낮아지는 경향은 두 방식이 같습니다.

[Claude 워터마크의 바탕 — Google SynthID 논문 분석](/posts/claude-watermark-synthid/)

## 출력 품질

최신 모델 Astra(최대 설정)로 여덟 개 벤치마크를 워터마크 유무에 따라 실행한 결과, 차이는 증감이 혼재한 약 3%포인트 이내였습니다.

| 벤치마크 | 워터마크 없음 | 워터마크 있음 |
| :--- | :--- | :--- |
| AA Intelligence Index | 49.57 | 49.76 |
| DeepSWE v1.1 | 72.80% | 71.68% |
| Terminal-Bench 4.0 | 53.90% | **56.06%** |
| BrowseComp | 87.92% | 87.35% |
| GPQA Diamond | 94.44% | 93.94% |
| HealthBench Professional | 64.27% | 64.60% |

공지에 함께 포함된 AutomationBench(34.09%→34.86%)와 Terminal-Bench Science 0.1(56.90%→60.00%)도 같은 방향이에요. 한 번씩 실행해 얻은 결과라 워터마크 쪽 점수가 높게 나온 항목도 실행마다 생기는 편차일 수 있습니다.

## 국내 적용 여부

![textGrain 발표 내용 정리 카드](/assets/images/ai/openai-textgrain-watermark/04-items.webp)
*textGrain 발표 내용 정리 카드 — 출처: OpenAI 공지 기반 자가 렌더*

이번 기본 적용은 EU 한정이라, 한국에서 ChatGPT가 만든 텍스트에는 textGrain이 기본으로 적용되지 않아요. 한국 API 고객은 일부 모델에서 직접 활성화할 수 있습니다.

국내에도 표시 의무가 있어요. 2026년 1월 22일 시행된 인공지능기본법 제31조는 생성형 AI 사업자가 결과물이 AI로 생성됐다는 사실을 표시하도록 하고, 과학기술정보통신부는 육안으로 보이지 않는 워터마크도 허용 방식으로 안내했습니다. 정부는 과태료보다 안내에 집중하는 1년 이상의 계도기간을 두겠다고 밝혔어요. OpenAI가 국내 텍스트 출력에 어떤 방식으로 이 의무에 대응하는지는 이번 공지에 명시되지 않았습니다.

EU 쪽 일정은 AI법 제50조 적용일인 2026년 8월 2일부터 시작됐고, 그 전에 출시된 서비스는 기계 판독 표시를 12월 2일까지 갖추면 되는 것으로 알려져 있어요. textGrain의 몇 주 단위 배포는 이 기한 안에 진행됩니다.

## 앞으로 주목할 점

- 기술 리포트 보강과 오픈소스 공개 시점 (OpenAI는 몇 주 안에 보강하겠다고 밝힘)
- 연구자 탐지기 접근 이후 나오는 외부 평가, 특히 한국어 글의 탐지율
- 국내 인공지능기본법 하위 고시에 맞춘 OpenAI의 국내 대응
- Anthropic·Google 등 다른 회사 워터마크와 상호 탐지 체계가 생기는지

## 참고 출처

- [[OpenAI] Our approach to EU text provenance rules (2026-10-05, 본문 이미지 3점 출처)](https://openai.com/index/eu-text-provenance/)
- [[OpenAI] textGrain: Entropy-Calibrated Watermarking for Language Model Text (기술 리포트)](https://cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf)
- [[European Commission] Code of Practice on AI-generated content](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)
- [[Baker Botts] EU AI Act Article 50 Transparency Obligations Go Live (2026-09, 적용일·유예 기한)](https://www.bakerbotts.com/thought-leadership/publications/2026/september/eu-ai-act-article-50-transparency-obligations-go-live)
- [[아주경제] 과기정통부, AI기본법 하위법령 제정, 생성형 AI 워터마크 의무화 (비가시적 워터마크 허용)](https://www.ajunews.com/view/20250917134029501)
- [[디지털데일리] AI기본법 시행령 입법예고, 과태료 계도기간 운영](https://www.ddaily.co.kr/page/view/2025090815422394673)
