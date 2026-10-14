---
title: "Strands Decider 2B — Amazon's Decision Model That Runs on a Laptop"
description: "How AWS's decision model Strands Decider, which outputs one choice and its probability, works, and results from a 12-question Korean test"
date: 2026-10-07
category: AI
subcategory: Explainer
tags: [aws, strands-decider, decision-model, small-model, local-llm]
image: /assets/og/en-2026-10-07-strands-decider-decision-model.png
---

On October 1, 2026, AWS's Strands Labs team released the decision model Strands Decider 2B under the Apache 2.0 license. Instead of generating sentences, it picks one of a set of given choices and outputs the probability that the answer is correct; at 2B in size, it runs even on a laptop.

Following TypeSafe's Jev and Convai Innovations' Laya, this time Amazon released the same kind of model, and Cloudflare released Clef on the same day.

![Official Strands Decider 2B announcement](/assets/images/ai/strands-decider-decision-model/01-photo-hero.webp)
*Official Strands Decider 2B announcement — Source: Strands Agents*

## Strands Decider 2B overview

Three people including Amazon's Marc Brooker announced it on the official blog; the weights are on Hugging Face, and the code, training data, and training scripts are on GitHub. Brooker explained that after seeing Jev, released in September, he built an in-house prototype that ranked first among same-size models on JevBench, which led to the release.

| Item | Details |
| :--- | :--- |
| Release date | October 1, 2026 |
| Base model | Qwen3.5-2B-Base |
| Trained parts | LoRA r16 + pointer head |
| License | **Apache 2.0** |
| Install | pip install strands-decider |

There are three question formats: **noul**, which asks yes or no; **choice**, which picks one of several options; and **score**, which assigns an ordered grade. The uses the official blog lists are deciding the next step inside agent workflows, such as model routing, tool selection, result evaluation, guardrails, and policy classification.

## Architecture

![Strands Decider 2B architecture, the LLM body and pointer head](/assets/images/ai/strands-decider-decision-model/02-photo.webp)
*Strands Decider 2B architecture, the LLM body and pointer head — Source: Strands Agents*

The output layer (LM head) that picks the next word was removed from a pretrained Qwen3.5-2B, and a **pointer head** that computes choice scores was attached in its place. Because it processes the input once and then computes scores by comparing the last-token state of each choice line with the state at the answer position, there is no repeated process of generating tokens one by one.

The only newly trained parts are a rank-16 LoRA adapter attached to the body and a pointer head of about 1 million parameters. The model card says training took 4,204 seconds (about 70 minutes) on a single H100 GPU.

## Accuracy and calibration

According to the model card, it answered 167 of 231 questions in the JevBench public set correctly, an accuracy of **72.3%**. The official blog says this ranks 3rd among 33 models in the 2B class, or 1st among 30 if models slightly above 2B are excluded.

| Evaluation | Accuracy (%) | Questions |
| :--- | :--- | :--- |
| JevBench public set | **72.3** | 231 |
| Short tasks not used in training | 64.1 | 6,000 |
| BoardGame | 82.2 | 900 |
| ContractNLI | 87.2 | 1,026 |
| HotpotQA | 71.7 | 959 |
| MuSiQue | <mark>88.4</mark> | 1,199 |

How well the output probability matches the actual accuracy (calibration) is ECE 0.050 and Brier score 0.348. ECE is the average gap between the confidence the model outputs and the actual accuracy, so closer to 0 is better. However, the model card notes that this calibration was confirmed only on short classification tasks.

## Speed

![v18 latency by prompt length, RTX 3090](/assets/images/ai/strands-decider-decision-model/03-photo.webp)
*v18 latency by prompt length, RTX 3090 — Source: Strands Agents*

According to the official blog, v19's median latency is about 115 milliseconds on an RTX 3090 and about 153 milliseconds for short tasks on an M3 MacBook. Measuring the previous version v18 230 times including the HTTP round trip gave a median of 106 milliseconds and a 95th percentile of 296 milliseconds.

Latency rises as input length grows. Under 1,000 tokens most requests fell between 100 and 130 milliseconds, while requests over 2,500 tokens rose to the 230–300 millisecond range.

## Korean test

![Running the strands-decider ask command on a Korean inquiry](/assets/images/ai/strands-decider-decision-model/04-term.webp)
*Running the strands-decider ask command on a Korean inquiry — Source: self-rendered from an actual run*

The model card only says it was trained on English public datasets and doesn't list supported languages. So on an M3 Pro MacBook, I gave it the same task in English and Korean: classifying 12 customer inquiries into one of four teams — billing, shipping, account, or technical error.

![Correct answers on 12 support-inquiry classification questions, by language condition](/assets/images/ai/strands-decider-decision-model/en/05-chart.webp)
*Correct answers on 12 support-inquiry classification questions, by language condition — Source: self-rendered from my own measurements*

In English it got 11 of 12 right, and in Korean it got 10 right whether the choices were given in English or Korean. On the same device, median latency was 154–168 milliseconds for Korean inquiries and 227 milliseconds for English inquiries.

| Missed inquiry | Model's answer | Confidence |
| :--- | :--- | :--- |
| Changed number, not receiving verification texts | Technical error | 0.64–0.77 |
| Can't log in after changing password | Technical error | 0.47–0.60 |

Both missed questions classified an account problem as a technical error, and in some cases the confidence came out at 0.6–0.77, similar to the correctly answered questions. If you decide whether to escalate to human review based on confidence alone, wrong answers like these won't get filtered out. Twelve questions is enough to see a tendency, not enough to settle accuracy.

When I used a noul question to ask whether an inquiry saying the fee was charged again was a refund request, it output a probability of 0.222, and the sentence didn't contain the word refund. Questions that ask about implied intent need separate verification in English too.

## Compared with Jev, Laya, and Clef

![Cloudflare logo](/assets/images/ai/strands-decider-decision-model/06-logo-cloudflare.webp)
*Cloudflare logo — Source: Cloudflare*

On the same October 1, Cloudflare released Clef (27B) and Clef-flash (9B) under Apache 2.0 and also started offering them as a paid hosted service on its Workers AI. They support 64k-token context and image input, so their use differs from the laptop-oriented Strands Decider.

| Model | Size | Release form |
| :--- | :--- | :--- |
| Jev (TypeSafe) | Undisclosed | Paid API |
| Laya (Convai) | 421M | Apache 2.0 |
| **Strands Decider** | **2B** | **Apache 2.0** |
| Clef-flash (Cloudflare) | 9B | Apache 2.0 + API |
| Clef (Cloudflare) | 27B | Apache 2.0 + API |

| Model | Median latency | Price per 1M tokens |
| :--- | :--- | :--- |
| Jev | 70–500ms | ₩59 |
| Laya | 39.5ms (T4) | Free locally |
| **Strands Decider** | **115ms (3090)** | **Free locally** |
| Clef-flash | 38.8ms | $0.09 (₩126) |
| Clef | 209.3ms | $0.24 (₩336) |

The latencies were measured on different hardware, so they shouldn't be read as a ranking. Strands Decider and Laya were measured on a local machine, while Jev and Clef are based on hosted services.

[Jev — A Decision Model That Outputs Probabilities Instead of Sentences](/en/posts/jev-decision-model/)

[Laya — An Open-Source AI Decision Model You Can Run for Free](/en/posts/laya-decision-model/)

## Limitations

The official blog itself says it is much worse than reasoning models at solving complex problems and isn't suited to work that requires writing, such as coding, chatbots, or document summarization. The model card lists four limitations.

- Attention concentrates on document content rather than the question
- Weak on long, multi-step documents
- Doesn't generalize well to new grading criteria that differ from the training data
- Inherits the biases of public datasets

For use in Korea, the advantages are that Apache 2.0 allows deploying it on in-house servers for commercial use and inquiry content isn't sent to an external API. There's no official Korean evaluation, so before adopting it you should re-measure accuracy and the confidence distribution on real inquiries.

## Sources

- [[Strands Agents] Introducing Strands Decider 2B (2026-10-01, architecture, JevBench ranking, latency, limitations)](https://strandsagents.com/blog/introducing-strands-decider/)
- [[Hugging Face] StrandsAgents/strands-decider-2B-hobson-v19 model card (accuracy, ECE, Brier, training time, limitations)](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19)
- [[GitHub] strands-labs/strands-decider (code, training recipe, data)](https://github.com/strands-labs/strands-decider)
- [[Cloudflare Blog] Clef decision models (2026-10-01, latency, context, license)](https://blog.cloudflare.com/clef-decision-models/)
- [[Cloudflare Docs] Workers AI Clef and Clef-flash model pages (pricing, parameters)](https://developers.cloudflare.com/workers-ai/models/clef/)
  https://developers.cloudflare.com/workers-ai/models/clef-flash/
- [[TypeSafe AI Docs] Models (Jev pricing and latency)](https://docs.typesafe.ai/models)
- [[Hugging Face] convaiinnovations/laya model card (Laya size, T4 latency)](https://huggingface.co/convaiinnovations/laya)
- Exchange rate: converted at $1 ≈ ₩1,400
