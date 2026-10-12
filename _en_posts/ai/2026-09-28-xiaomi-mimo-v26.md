---
title: "Xiaomi MiMo V2.6 — A 1-Trillion-Parameter Model Under the MIT License"
description: "The makeup and pricing of MiMo-V2.6 Pro and Flash, which took the top open-weights score, and the reinforcement learning code and training environments released with them"
date: 2026-09-28
category: AI
subcategory: News
tags: [xiaomi, mimo, open-weights, moe, llm]
image: /assets/og/en-2026-09-28-xiaomi-mimo-v26.png
---

On September 21, 2026, Xiaomi unveiled its MiMo-V2.6 series of LLMs (large language models) and released the weights under the MIT license. The flagship MiMo-V2.6-Pro has 1.02 trillion total parameters and scored 46.32 on the Intelligence Index of independent evaluator Artificial Analysis, the highest among open-weights models.

Xiaomi also released its reinforcement learning (RL) code and more than 7,000 training environments.

![Xiaomi MiMo wordmark](/assets/images/ai/xiaomi-mimo-v26/01-logo-mimo.webp)
*Xiaomi MiMo wordmark — Source: Xiaomi*

## The lineup

![Xiaomi logo](/assets/images/ai/xiaomi-mimo-v26/02-logo-xiaomi.webp)
*Xiaomi logo — Source: Xiaomi*

MiMo-V2.6 consists of two models and one speed option. The weights are on Hugging Face, and the models are available right away in Xiaomi AI Studio, MiMo Code, MiMo Desktop, Xiaomi's own API, and OpenRouter.

- MiMo-V2.6-Pro: an MoE (mixture of experts) model with 1.02T total and 42B active parameters
- MiMo-V2.6-Flash: a lightweight model with 309B total and 15B active parameters
- Pro-UltraSpeed: a paid option with the same quality as Pro and up to 20 times the output speed
- Both models are omnimodal, taking text, images, video, and audio in one model, with a 1-million-token context
- MiMo-V2.6-Distill-Qwen-9B: a research checkpoint of Alibaba's Qwen3.5-9B fine-tuned on MiMo-generated data

## The specs explained

![Diagram of the MiMo-V2.6 backbone and multimodal encoders](/assets/images/ai/xiaomi-mimo-v26/03-photo-architecture.webp)
*Diagram of the MiMo-V2.6 backbone and multimodal encoders — Source: Xiaomi*

MoE splits the total parameters into groups of experts and uses only some of them for each token. Pro selects 8 of its 384 experts, so it computes with 42 billion parameters per token rather than 1 trillion.

For attention, it combines Sliding Window Attention (SWA), which looks only at a nearby span, with Global Attention (GA), which looks at everything. In Pro, 60 of 70 layers are SWA and 10 are GA. With a 1-million-token context, having every layer look at everything would blow up the compute, so most layers look only at a nearby span.

It also includes an MTP (Multi-Token Prediction) block that predicts several tokens ahead at once, raising output speed.

| Item | V2.6-Pro | V2.6-Flash |
| :--- | :--- | :--- |
| Total parameters | **1.02T** | 309B |
| Active parameters | 42B | 15B |
| Experts | 8 of 384 | 8 of 256 |
| Layers (SWA/GA) | 70 (60/10) | 48 (39/9) |
| Context | 1M tokens | 1M tokens |

The vision encoder has 681 million parameters, and audio is handled by a 308-million-parameter tokenizer and a 127-million-parameter encoder.

The model card's recommended deployment is two GPU server nodes for Pro (tensor parallelism 16 with SGLang) and 4–8 GPUs for Flash, so neither is sized to run on a personal PC.

## Benchmarks

Xiaomi's model card compares Pro with Anthropic's Claude Opus 5 and OpenAI's GPT-5.6 Sol on five agent and coding benchmarks.

| Benchmark | V2.6-Pro | Claude Opus 5 |
| :--- | :--- | :--- |
| DeepSWE v1.1 | 71.9 | **74.0** |
| AutomationBench | <mark>53.1</mark> | 50.3 |
| Toolathlon-Verified | 76.9 | **80.6** |
| Terminal Bench 2.1 | <mark>89.9</mark> | 89.1 |
| OSWorld-Verified | 82.0 | **83.4** |

It beats Opus 5 on two of the five and trails on three. Against GPT-5.6 Sol, Pro led on AutomationBench (45.8), Terminal Bench 2.1 (88.8), and Toolathlon (74.9). Flash scored 52.3 on AutomationBench, 0.8 points behind Pro, but on the harder Terminal Bench 4.0 it scored 28.8, more than 20 points behind Opus 5 (49.0).

These scores were measured by Xiaomi itself. The third-party figure is the Artificial Analysis Intelligence Index (v4.3) score of 46.32, with which Xiaomi said it ranks first among open-weights models, ahead of Kimi K3 and Qwen3.8 Max. eWeek noted that coding benchmarks like DeepSWE face credibility debates over scoring methods and data contamination, and that there has been no outside security validation yet.

## Pricing

![Price per million output tokens for the three MiMo-V2.6 tiers and Claude Opus 5](/assets/images/ai/xiaomi-mimo-v26/04-chart-price.webp)
*Price per million output tokens for the three MiMo-V2.6 tiers and Claude Opus 5 — Source: self-rendered from OpenRouter and Anthropic's published prices*

On OpenRouter, the price per million tokens is $0.14 (₩196) input and $0.28 (₩392) output for Flash, and $0.435 (₩609) input and $0.87 (₩1,218) output for Pro. Claude Opus 5 is $5 (₩7,000) input and $25 (₩35,000) output, so on output Pro is about one twenty-ninth the price. The faster Pro-UltraSpeed is 10 times Pro: $4.35 (₩6,090) input and $8.7 (₩12,180) output.

Prices were kept the same as V2.5, released in April. Through SiliconANGLE, Xiaomi claimed Pro costs one twentieth to one sixtieth as much as overseas models of similar intelligence.

## The reinforcement learning process, released

Xiaomi said it ran 30 steps of reinforcement learning on the pretrained model, taking under 6 days. Each step generated 16 responses for each of 1,568 prompts, producing about 3.5–3.7 billion tokens, for roughly 750,000 trajectories in total.

The reinforcement learning cost about $2.62 million (₩3.67 billion) for Pro and about $850,000 (₩1.19 billion) for Flash, about $3.47 million (₩4.86 billion) combined. Pretraining and other development costs are excluded, so it should not be read as the total training cost, as some Korean reports did. Besides the weights, the release includes the technical report, more than 7,000 RL training environments covering software development, vulnerability reproduction, web development, and more, and the frameworks for trajectory collection, reward evaluation, and policy optimization.

## Background and context

Xiaomi's MiMo began in April 2025 with the 7B reasoning model MiMo-7B, and in December released MiMo-V2-Flash, a 309B MoE, under MIT. In March 2026 it launched the trillion-parameter-class MiMo-V2-Pro as a closed model, then started releasing weights for its large models too from V2.5 in April.

The team has been led since late 2025 by Luo Fuli, who worked on DeepSeek-V2, and CEO Lei Jun said in March 2026 that the company would invest at least $8.7 billion (about ₩12.18 trillion) in AI over three years.

Alibaba released its image model Qwen-Image-2.1 on September 20 under a research-only license, while Xiaomi released a trillion-parameter model under the MIT license, which permits even commercial use freely — a clear difference in license terms.

## What it means for users in Korea

The point to check when using a Chinese AI service in Korea is data transfer. In February 2025, the Personal Information Protection Commission halted new downloads of the DeepSeek app in Korea over personal data handling. Using the MiMo API or Xiaomi AI Studio sends input data to Xiaomi's servers, but downloading the MIT weights and deploying them on a domestic cloud or in-house GPUs keeps the data from leaving.

Running Pro yourself, however, requires two GPU server nodes, so what small and mid-sized teams can realistically use is Flash or the API via OpenRouter.

Xiaomi's announcement materials include no official figures on Korean-language performance.

## What to watch next

- Whether Xiaomi's own benchmark scores hold up in outside evaluations such as LMArena
- Whether outside researchers reproduce the results with the released RL environments and code
- When V2.6 comes to Xiaomi smartphones, HyperOS, and electric vehicles
- Whether Korean cloud providers offer MiMo models

## Sources

- [[Hugging Face] XiaomiMiMo/MiMo-V2.6-Pro-RL model card (architecture, benchmarks, deployment settings, source of one image in this post)](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
- [[Hugging Face] XiaomiMiMo/MiMo-V2.6-Flash-RL model card (Flash architecture, benchmarks)](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [[SiliconANGLE] Xiaomi introduces MiMo-V2.6 series open-source AI model family (pricing, Artificial Analysis score, cost claims)](https://siliconangle.com/2026/09/22/xiaomi-introduces-mimo-v2-6-series-open-source-ai-model-family/)
- [[RuntimeWire] Xiaomi open-sources MiMo-V2.6 and the RL machinery behind it (RL steps, trajectory counts)](https://runtimewire.com/article/xiaomi-open-sources-mimo-v2-6-rl-cost-3-47m)
- [[eWeek] Xiaomi MiMo-V2.6 Open Source: Pro, Flash, 9B Models (RL cost range, what was released, benchmark limits)](https://www.eweek.com/news/xiaomi-mimo-v26-open-source-rl-reproduction/)
- [[Wikipedia] Xiaomi MiMo (version history, investment plans)](https://en.wikipedia.org/wiki/Xiaomi_MiMo)
- [[AI Times] Xiaomi releases open model MiMo-V2.6 (Korean report)](https://www.aitimes.com/news/articleView.html?idxno=215552)
- [[Anthropic] Claude API pricing (Claude Opus 5 rates)](https://platform.claude.com/docs/en/about-claude/pricing)
- Exchange rate: converted at $1 ≈ ₩1,400
