---
title: "Reflection AI Beam — A 501-Billion-Parameter Open-Weight Model"
description: "The architecture, performance claims, and release schedule of Beam, an MoE open-weight model a US company is releasing under Apache 2.0"
date: 2026-10-07
category: AI
subcategory: News
tags: [reflection-ai, beam, open-weights, moe, llm]
image: /assets/og/en-2026-10-07-reflection-ai-beam-open-weights.png
---

On October 5, Reflection AI, founded by former DeepMind researchers, unveiled **Beam**, its first frontier-class open-weight model. It is a mixture-of-experts (MoE) model that uses only 23 billion of its 501 billion total parameters at a time.

The weights are due out this month under the Apache 2.0 license, which permits downloading, running on in-house servers, and modifying the model. It's a model from a US company entering the top tier of open weights, which Chinese models have dominated.

![Beam key visual](/assets/images/ai/reflection-ai-beam-open-weights/01-hero-beam.webp)
*Beam key visual — Source: Reflection AI*

## Timeline

![Reflection logo](/assets/images/ai/reflection-ai-beam-open-weights/02-logo-reflection.webp)
*Reflection logo*

Reflection AI was founded in March 2024 by Misha Laskin (CEO) and Ioannis Antonoglou (CTO), both formerly researchers at Google DeepMind. Antonoglou worked on AlphaGo.

The announcement came first and the weights come later. The company said Beam is going through final red-teaming (attack testing) and evaluation, and that it will release the weights along with a technical report, model card, and tools for running, evaluating, and fine-tuning within the month. Until then, it is only accepting early access applications.

- October 5: Beam announced, early access applications open
- During October: Weights and technical report to be released (Apache 2.0)

## Model specs

![Beam pretraining loss curve](/assets/images/ai/reflection-ai-beam-open-weights/03-pretraining-loss.webp)
*Beam pretraining loss curve — Source: Reflection AI*

| Item | Beam |
| :--- | :--- |
| Total parameters | **501 billion** |
| Active parameters | <mark>23 billion</mark> |
| Architecture | Sparse MoE |
| Pretraining data | 23.8 trillion tokens |
| Context length | Up to 1 million tokens |
| License | Apache 2.0 |

MoE is an architecture that selects and computes only some of many expert blocks for each token. So the compute is at the level of a 23-billion-parameter model, but all 501 billion parameters have to be loaded into memory.

The company said pretraining used 6,144 NVIDIA GB300 GPUs for under four weeks, followed by reinforcement learning that ran more than 100 million rollouts over four weeks on 10,500 GB300s. Reinforcement learning used a 256,000-token length, and mid-training extended the context to 1 million tokens.

## Benchmark scores

In Reflection AI's published figures, Beam scored close to Z.ai's GLM-5.2 from China.

| Benchmark | Beam | GLM-5.2 |
| :--- | :--- | :--- |
| DeepSWE v1.1 | **44.4** | 44.0 |
| Terminal Bench v2.1 | 80.1 | **81.0** |
| AIME 2026 | 97.8 | **99.2** |
| GPQA Diamond | 90.5 | **91.2** |
| SWE Bench Pro v2-Hard | <mark>77.2</mark> | Not disclosed |
| SciCode | 49.7 | Not disclosed |

In the same published figures, Moonshot AI's Kimi K3 scored higher than Beam on all five items with published scores: 68.0 on DeepSWE v1.1 and 88.3 on Terminal Bench v2.1. Alibaba's Qwen 3.8-Max also beat Beam on four items.

All scores were measured by Reflection AI itself, and since the weights aren't out yet, there are no external reproductions.

## The inference compute efficiency claim

![Terminal Bench 2.1 score versus generation compute](/assets/images/ai/reflection-ai-beam-open-weights/04-efficiency.webp)
*Terminal Bench 2.1 score versus generation compute — Source: Reflection AI*

Reflection AI emphasizes inference compute more than scores. It claims Beam scores similarly to GLM-5.2 on hard reasoning benchmarks while using **3–4 times less** inference compute.

The comparison used score against the compute (PFLOP) needed to generate one answer. CEO Laskin said large-scale reinforcement learning let the model reach competitive performance using a fraction of the token cost and inference compute. Training reportedly included tuning a length penalty to make answers shorter, but this efficiency also hasn't been independently verified.

## The open-weight competitive landscape

The top tier of open weights has been held by Chinese models such as Kimi K3, DeepSeek V4, and GLM-5.2/5.3. On the US side, Thinking Machines Lab released Inkling in July and NVIDIA releases Nemotron, but Fortune saw Beam as a new US model aiming to compete directly with Chinese models.

The funding is large too. Reflection AI raised $2 billion (about ₩2.8 trillion) in an NVIDIA-led round in October 2025, and CEO Laskin said in April that the company was valued at $25 billion (about ₩35 trillion). In May it also signed an agreement to supply models to the US Department of Energy and Department of War.

## If a Korean company wants to use it

![Memory needed to hold Beam's weights](/assets/images/ai/reflection-ai-beam-open-weights/en/05-chart.webp)
*Memory needed to hold Beam's weights — Source: self-rendered from Reflection AI parameter count*

Apache 2.0 is a license that permits commercial use, modification, and redistribution, and also grants patent rights. It sets no user-count or revenue caps, so there are no strings attached for a Korean company deploying it on in-house servers without sending customer data outside.

The constraint is hardware. The weights alone are about 501GB in FP8 (1 byte per parameter) and about 1TB in BF16 (2 bytes), so even in FP8, eight 80GB GPUs (640GB) may not have enough room once the runtime cache is included. A server with eight 141GB-class GPUs or 4-bit quantization is the realistic option, and how much accuracy drops at 4 bits needs to be checked after release.

In Korea, LG AI Research, Upstage, SK Telecom, and others are building their own models under the government's sovereign AI foundation model project. Once Beam's weights are out, there will be one more US-made baseline model that can be compared with these models under the same conditions.

## What to watch next

- Whether the weights and technical report actually come out this month
- Benchmark scores reproduced by external evaluators
- Whether the 3–4x lower inference compute claim holds up in actual token usage
- Whether Korean cloud and inference services support Beam

## Sources

- [[Reflection AI] Introducing Beam (2026-10-05, specs, benchmarks, license; source of 2 images in the body)](https://reflection.ai/blog/introducing-beam)
- [[Fortune] The U.S. has a new horse in the race to build the best open-source AI model (2026-10-06, competitive landscape, valuation, CEO quotes)](https://fortune.com/2026/10/06/the-us-new-horse-race-to-build-best-open-source-ai-model/)
- [[MarkTechPost] Reflection AI Introduces Beam (2026-10-05, architecture summary)](https://www.marktechpost.com/2026/10/05/reflection-ai-introduces-beam-a-501b-open-weight-moe-model-with-23b-active-parameters-for-coding-and-agentic-workloads/)
- [[Wikipedia] Reflection AI (founding and funding history)](https://en.wikipedia.org/wiki/Reflection_AI)
- [[Apache Software Foundation] Apache License 2.0 (commercial use and patent clauses)](https://www.apache.org/licenses/LICENSE-2.0)
- Exchange rate: converted at $1 ≈ ₩1,400
