---
title: "Aleph Alpha Kolibri — German Sovereign AI Released Under Apache 2.0"
description: "The makeup and performance of Kolibri, a 78B MoE model built and released in Germany, and how its direction differs from Korea's sovereign AI foundation model program"
date: 2026-10-05
category: AI
subcategory: News
tags: [aleph-alpha, kolibri, sovereign-ai, open-weights, moe]
image: /assets/og/en-2026-10-05-aleph-alpha-kolibri.png
---

German AI company Aleph Alpha released its language model Kolibri on Hugging Face on October 3, 2026. It is an MoE (Mixture of Experts) model that uses only 3.46 billion of its 78.1 billion total parameters per token, released under the Apache 2.0 license, which allows anyone to use it commercially.

Aleph Alpha introduced Kolibri as a sovereign model built in Germany and trained on German and Finnish infrastructure. That is a different direction from Korea's sovereign AI foundation model program, in which the government selects elite teams to develop models with hundreds of billions of parameters.

![Kolibri launch banner](/assets/images/ai/aleph-alpha-kolibri/01-hero-banner.webp)
*Kolibri launch banner — Source: Aleph Alpha*

## What was released

![Chart of Kolibri's pretraining data mix](/assets/images/ai/aleph-alpha-kolibri/02-chart.webp)
*Chart of Kolibri's pretraining data mix — Source: self-rendered from Aleph Alpha's announcement*

Kolibri handles two languages, English and German, and targets heavily regulated fields such as public administration, manufacturing, and aerospace. It is the follow-up to Kolibri Origin (30.6B total), which finished pretraining on June 11, released three months later.

| Item | Value |
| :--- | :--- |
| Total parameters | 78.1B |
| Active parameters per token | **3.46B** |
| Experts | 6 of 384 used |
| Context | Trained at 256K, up to 1M tokens |
| License | <mark>Apache 2.0</mark> |
| Distribution | FP8 weights on Hugging Face |

Training used 768 NVIDIA B200s for 21 days, on about 20 trillion pretraining tokens — curated from more than 200 trillion tokens of raw data.

German makes up 21.3% of pretraining tokens, about 4.3 trillion. Aleph Alpha said relying on machine translation degrades results, so it collected and rewrote German documents directly and capped translated data at 6%.

## Performance

![Chart comparing AA-Omniscience non-hallucination rates](/assets/images/ai/aleph-alpha-kolibri/03-chart.webp)
*Chart comparing AA-Omniscience non-hallucination rates — Source: self-rendered from Aleph Alpha's announcement*

The models Aleph Alpha chose to compare against are open-weight models of similar size: NVIDIA Nemotron 3 Super (12B active, about four times Kolibri's active parameters), Alibaba Qwen3.6-35B, and Mistral Small 4.

[Where it leads]
Math *AIME 2025* 96.9% (Nemotron 3 Super 91.7%), science reasoning *GPQA Diamond* 84.3% (Qwen3.6 83.4%)

[Where it scores lower]
Coding *HumanEval+* 92.7% (Nemotron 3 Super 94.7%), long documents *LongBench Pro* 64.5% (Qwen3.6 70.8%), tool calling *BFCL v4* 61.4% (Qwen3.6 67.2%)

The number Aleph Alpha emphasized most is hallucination suppression. Its *AA-Omniscience* non-hallucination rate — how often it declines to make up answers to questions it doesn't know — was 44.0%, about three times Kolibri Origin's 14.8% and Nemotron 3 Super's 13.9%.

All benchmarks were measured by Aleph Alpha itself; no independent verification is out yet.

## How it defines sovereign AI

![Concept image of an open-weight model trained on domestic infrastructure](/assets/images/ai/aleph-alpha-kolibri/04-agy.webp)
*Concept image of an open-weight model trained on domestic infrastructure — Source: concept image · self-generated with agy*

[How it's built]
The company controls the whole process from data collection to training and evaluation, designed to meet the EU AI Act, GDPR, and copyright standards

[How it's delivered]
Weights are published so customers can install it on their own servers and run it without control by a foreign company

> No foreign control; we own the entire pipeline (Aleph Alpha, 2026.10.3)

With 3.46B active parameters, the same quality can be served on fewer GPUs, which in turn makes it easier for public agencies and manufacturers to install and run it themselves, the company explained.

## Compared with Korea's sovereign AI models

![Chart comparing parameter counts of Kolibri and Korea's sovereign AI models](/assets/images/ai/aleph-alpha-kolibri/05-chart.webp)
*Chart comparing parameter counts of Kolibri and Korea's sovereign AI models — Source: self-rendered from company announcements*

On August 19, 2026, Korea's Ministry of Science and ICT selected SK Telecom (70.6 points), Upstage (69.9), and LG AI Research (69.0) for the next stage in the second-stage evaluation of its sovereign AI foundation model project, and will provide the three teams about ₩120 billion in GPU rental costs over six months. Motif Technologies was eliminated.

| Item | Kolibri | Korea's stage-2 models |
| :--- | :--- | :--- |
| Development | Single company | Government-backed elite teams |
| Total parameters | **78.1B** | 688B · 750B |
| Training languages | English, German | Multilingual, Korean-centered |
| Release | Apache 2.0 | Released on Hugging Face |

SK Telecom's A.X K2 has 688 billion parameters and LG AI Research's K-EXAONE 2.0 has 750 billion — about 9–10 times Kolibri's total. K-EXAONE 2.0 switched to Apache 2.0 like Kolibri, allowing commercial use, and Upstage's Solar Open 2 supports up to 1M tokens of context.

Korea's models are closer to a scale race, competing with American and Chinese models on international benchmark rankings; Kolibri goes the other way, a small model fitted to specific languages and regulated industries to lower deployment costs.

## Using it in Korea

Kolibri does not include Korean among its training languages. It can serve for English and German document work or as a comparison model for research, but it is hard to use as-is for Korean-language services.

The weights are in FP8, so at 78.1 billion parameters they come to about 78GB (counting one byte per parameter). Aleph Alpha recommends serving it with its vLLM-based package **aleph-alpha-inference**.

Because the license is Apache 2.0, Korean companies can also use it in commercial services or modify and redistribute it. The structure allows it to serve as a base for additional Korean training, but the tokenizer (the rules for splitting text into tokens), fitted to German, may be less efficient for Korean — that is a variable.

## What to watch next

- Kolibri benchmark results from independent bodies such as Artificial Analysis
- Announcements of actual adoption by German federal and state agencies
- The Ministry of Science and ICT's schedule for stage 3 of the sovereign AI program and its new support structure
- Whether Korea's elite teams also release small, lightweight models like Kolibri

## Sources

- [[Aleph Alpha] Kolibri Has Landed: A Sovereign Open-Weight Model (2026-10-03)](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/)
- [[Hugging Face] Aleph-Alpha/Kolibri-1 model repository](https://huggingface.co/Aleph-Alpha/Kolibri-1)
- [[Korea Policy Briefing] Results of the stage-2 evaluation of the sovereign AI foundation model project (2026-08-19)](https://www.korea.kr/briefing/policyBriefingView.do?newsId=156774781)
- [[Asia Economy] Team-by-team results of the stage-2 sovereign AI evaluation (2026-08-18)](https://view.asiae.co.kr/article/2026081811193867650)
- [[Light Reading] SK Telecom unveils A.X K2 (2026-07)](https://www.lightreading.com/ai-machine-learning/sk-telecom-pushes-a-x-k2-ai-into-manufacturing-and-defense-industries)
- [[Busan Ilbo] LG AI Research opens the K-EXAONE 2.0 license (2026-07-31)](https://www.busan.com/view/busan/view.php?code=2026073109201409771)
