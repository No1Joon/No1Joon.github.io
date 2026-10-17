---
title: "Meta Muse Spark Open — 816B 오픈 가중치 공개와 Muse Wonder"
description: "Meta 첫 프런티어 모델 Muse Wonder 와 사흘 뒤 가중치를 푼 Muse Spark Open 의 구조·성능·라이선스를 정리합니다"
date: 2026-10-16
category: AI
subcategory: News
tags: [meta, muse-spark, open-weights, moe, llm]
image: /assets/og/2026-10-16-meta-muse-spark-open-816b.png
---

Meta가 10월 12일 첫 프런티어 모델 **Muse Wonder**를 API와 구독 형태로만 제공하고, 사흘 뒤인 10월 15일 한 단계 아래 모델 **Muse Spark Open**의 가중치를 공개했어요. 전체 파라미터 8,160억 개 가운데 한 번에 420억 개를 쓰는 전문가 혼합(MoE) 모델이고, Meta는 미국에서 나온 오픈 가중치 모델 가운데 가장 성능이 높다고 발표했습니다.

![Muse Spark Open Weights 발표 키 비주얼](/assets/images/ai/meta-muse-spark-open-816b/01-hero-social.webp)
*Muse Spark Open Weights 발표 키 비주얼 — 출처: Meta*

## 사흘 사이 두 발표

- 10월 12일: Muse Wonder·Muse Wonder Full 공개, Meta 첫 프런티어 모델
- 10월 15일: Muse Spark Open 가중치 공개, Hugging Face 등에서 내려받기 가능
- 두 모델 모두 context window(한 번에 처리하는 입력 길이) 100만 토큰
- Wonder는 API·구독 전용, Spark Open은 Muse Model License로 가중치 배포

TechCrunch에 따르면 Muse Wonder는 오하이오주 중부의 Meta Prometheus 데이터센터에서 학습했고, Alexandr Wang이 2025년 8월 Meta의 AI 조직을 개편한 뒤 처음 출시된 프런티어 모델입니다. Muse Spark Open은 8월에 공개한 Muse Spark 1.2를 바탕으로 하고, Muse Spark 1.3과 같은 기반 모델을 공유해요.

## Muse Wonder, 가중치 비공개 최상위 모델

![Meta 로고](/assets/images/ai/meta-muse-spark-open-816b/02-logo-meta.webp)
*Meta 로고*

Muse Wonder는 Meta Model API와 코딩 도구 Muse Code에서 쓸 수 있고, 상위판인 Wonder Full은 API로 제공하지 않고 Muse Code 구독자에게만 제공했어요. 텍스트·이미지·영상·음성을 입력으로 받고, Meta는 사용자가 알려 준 정보를 기억해 다시 쓰는 **active memory**를 내세웠습니다.

| 항목 | Muse Wonder | Muse Wonder Full |
| :--- | :--- | :--- |
| 제공 경로 | API·Muse Code | Muse Code 구독만 |
| 입력 100만 토큰 | **5,600원($4)** | API 미제공 |
| 출력 100만 토큰 | 28,000원($20) | API 미제공 |
| AA 지능 지수 | 52 (Max 설정) | <mark>56</mark> (보도) |

API 요금은 TechCrunch가 GPT-6 Sol·Claude Opus 5.5와 비슷한 수준이라고 평가했어요.

독립 평가 기관 Artificial Analysis의 비교 페이지에서 Muse Wonder(Max 설정)는 지능 지수 52점, Claude Opus 5.5(Max)는 58점입니다. Wonder Full이 56점이라는 수치는 2차 보도에서 나온 것이라 Artificial Analysis 원문에서 확인하지 못했어요.

Meta는 자체 시험에서 Wonder 계열이 Fable 5.1·GPT-6 Astra와 비슷한 점수를 냈고 기억 성능을 평가하는 MemoryBench에서는 Fable·Opus·Astra보다 높은 점수를 기록했다고 밝혔습니다.

## Muse Spark Open 사양

Hugging Face 모델 카드에 적힌 구조는 이렇습니다.

| 항목 | 값 |
| :--- | :--- |
| 전체·활성 파라미터 | **816B · 42B** |
| 전문가 수 | 256개 중 8개 사용 |
| 층 수 | 62 |
| 컨텍스트 | 100만 토큰 |
| 입력 | 텍스트·이미지·영상·음성 |
| 출력 | 텍스트 |
| 배포 정밀도 | BF16·NVFP4 |

전문가 혼합 구조는 토큰마다 전문가 256개 중 8개만 계산에 쓰기 때문에 계산량은 420억 파라미터 모델 수준이에요.

메모리에는 8,160억 개의 파라미터를 모두 적재해야 해서 모델 카드는 NVFP4 기준 VRAM 700GB 이상, BF16 기준 2TB가 필요하다고 적었습니다. Meta는 512GB 통합 메모리를 단 M5 Ultra Mac Studio 두 대를 MLX로 연결해 모델을 실행할 수 있다고도 밝혔어요.

### 벤치마크

![Muse Spark Open과 다른 오픈 가중치 모델의 벤치마크 비교표](/assets/images/ai/meta-muse-spark-open-816b/03-bench-scorecard.webp)
*Muse Spark Open과 다른 오픈 가중치 모델의 벤치마크 비교표 — 출처: Meta*

Meta가 공개한 표에서 Muse Spark Open은 에이전트 작업과 지식 문항에서 비교 모델보다 높은 점수를 기록했어요. 실제 업무를 흉내 낸 JobBench 61.8, 도구 호출 시험 MCP-Atlas 89.2, 도구 없이 푸는 HLE-Diamond 26.1은 비교 모델 가운데 가장 높습니다.

코딩 시험 Terminal-Bench 2.1에서는 76.4로, Kimi K3(85.0)·GLM 5.3(83.9)은 물론 같은 미국 모델인 Reflection AI의 Beam(80.1)보다도 낮은 점수를 기록했어요.

![오픈 가중치 모델 Artificial Analysis 지능 지수 비교](/assets/images/ai/meta-muse-spark-open-816b/04-chart-aa.webp)
*오픈 가중치 모델 Artificial Analysis 지능 지수 비교 — 출처: Meta 모델 카드 기반 자가 렌더*

Artificial Analysis 지능 지수는 여러 시험 결과를 합산한 지표예요. Muse Spark Open은 39점으로 GLM 5.3(45점)·Kimi K3(44점)·Qwen3.8(40점) 같은 중국 모델 아래에 있고, NVIDIA의 Nemotron 3 Ultra(23점)보다는 높습니다. Meta가 말한 미국 최고는 중국 모델을 뺀 비교에서 나온 표현이에요. 이 표는 모두 Meta가 직접 잰 값이고 독립 평가는 아직 나오지 않았습니다.

안전성 지표는 Meta가 따로 강조한 부분이에요. 가중치를 공개하면 시스템 차원의 안전장치 없이 모델만 쓰일 수 있어서 추가 안전 학습을 했고, 탈옥 시도 시험인 StrongREJECT v2에서 0.5(낮을수록 좋음)를 기록해 비교 모델(62.9~86.4)과 차이가 컸습니다.

## 라이선스와 배포 경로

![Hugging Face 로고](/assets/images/ai/meta-muse-spark-open-816b/05-logo-huggingface.webp)
*Hugging Face 로고*

가중치는 Hugging Face·Amazon SageMaker AI·Google Cloud Model Garden·Microsoft Foundry에서 받을 수 있고, Baseten·Fireworks AI·Groq·OpenRouter·Together AI 등 7곳이 API로도 제공해요. Hugging Face에서 가중치를 다운로드하려면 법적 이름·생년월일·소속 기관명을 적는 신청서를 내야 하고, 제출한 뒤에는 고칠 수 없습니다.

| 조건 | Muse Model License |
| :--- | :--- |
| 상업 이용·파인튜닝·증류 | 허용 |
| 표기 의무 | **Built with Muse Spark Open** |
| API 제공 사업 | 연 매출 280억 원 초과 시 별도 계약 |
| 이용 연령 | 만 18세 이상 |

제품 화면이나 문서, 설정 화면에 Built with Muse Spark Open을 눈에 띄게 적어야 하고, 이 모델을 파인튜닝하거나 증류한 파생 모델에도 같은 의무가 적용돼요.

모델을 API로 외부 고객에게 제공하는 사업자는 12개월 매출이 약 280억 원(2,000만 달러)를 넘으면 Meta에 알리고 별도 계약을 맺어야 합니다. 사내 사용·연구·자사 제품 안에 넣어 쓰는 경우는 이 조건의 적용 대상에서 제외돼요. Apache 2.0으로 공개되는 Reflection AI Beam이나 MIT 라이선스인 Xiaomi MiMo V2.6과 비교하면 조건이 붙은 라이선스입니다.

## 국내 접점

모델 카드는 100개 넘는 언어 데이터로 학습했다고 적었지만 지원 언어 목록에 한국어를 따로 명시하지 않았어요. 학습 데이터의 모든 언어를 평가하지는 않았고 주력 언어 외에는 성능이 저하될 수 있다고도 밝혀서, 한국어 서비스에 쓰려면 직접 시험해 봐야 합니다.

국내 기업이 사내 서버에 받아 쓰는 경우는 매출 조건과 무관하고 표기 의무만 지키면 됩니다. 이 모델로 외부 고객에게 API를 파는 클라우드·AI 기업은 연 매출 280억 원 기준을 따져 봐야 해요. NVFP4 가중치를 메모리에 적재하는 데만 VRAM 700GB가 필요해서, 80GB급 GPU로 계산하면 최소 9장이 필요하고 KV 캐시까지 더하면 서버 두 대 규모가 됩니다. Muse Wonder API의 국내 제공 여부는 공개된 자료에서 확인되지 않았어요.

## 앞으로 주목할 점

- Artificial Analysis 등 독립 기관의 Muse Spark Open 평가 결과
- Meta가 예고한 Muse Spark Open 전체 안전성 평가 보고서
- Muse Wonder Full의 API 개방 여부
- 한국어 성능에 대한 국내 개발자 실측

## 참고 출처

- [[Meta] Muse Spark Open 발표 (2026-10-15, 사양·배포처·안전 학습, 본문 이미지 2점 출처)](https://research.meta.ai/blog/muse-spark-open)
- [[Hugging Face] meta-models/Muse-Spark-Open-816B-A42B 모델 카드 (구조·벤치마크·라이선스·요구 메모리)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- [[PyTorch] Muse Spark Is Now an Open-Weights Model (2026-10-15, Helion 커널·TorchTitan)](https://pytorch.org/blog/muse-spark-open/)
- [[TechCrunch] Meta releases its first frontier model, Muse Wonder (2026-10-12, 요금·학습 데이터센터)](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder)
- [[Artificial Analysis] Muse Wonder vs Claude Opus 5.5 비교 (지능 지수)](https://artificialanalysis.ai/models/comparisons/muse-wonder-vs-claude-opus-5-5)
- [[MindStudio] Muse Wonder benchmarks vs Opus·GPT-6 (Wonder Full 56점 보도)](https://www.mindstudio.ai/blog/muse-wonder-benchmarks-vs-opus-gpt6)
- 환율: 1달러 ≈ 1,400원 기준 환산
