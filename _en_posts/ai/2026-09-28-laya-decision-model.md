---
title: "Laya — An Open-Source AI Decision Model You Can Run for Free"
description: "The architecture and real-world performance of Laya, the same kind of model as Jev but with open weights, and the limits of its accuracy before fine-tuning"
date: 2026-09-28
category: AI
subcategory: Explainer
tags: [laya, decision-model, open-source, modernbert, classification]
image: /assets/og/en-2026-09-28-laya-decision-model.png
---

On September 18, 2026, Convai Innovations released the weights of its decision model Laya on Hugging Face under the Apache 2.0 license. In that it returns only probabilities for each option instead of generating text, it is the same kind of model as Jev, released by TypeSafe AI on September 15 — but Jev is a paid API with closed weights, while anyone can download Laya and run it for free.

I covered how Jev arrives at its decisions in the post below.

[Jev — An AI Decision Model That Outputs Probabilities Instead of Sentences (in Korean)](/posts/jev-decision-model/)

![Laya logo](/assets/images/ai/laya-decision-model/01-logo-laya.webp)
*Laya logo — Source: Convai Innovations*

## Laya at a glance

Laya takes an input (**state**) and a few questions, and returns an answer and a probability distribution for each question in a single computation. Unlike an LLM (large language model), which generates text one token at a time, it produces zero output tokens, so malformed JSON or invented options are structurally impossible.

The underlying architecture is a BERT-family bidirectional encoder. Decision heads for each question type sit on top of an encoder that reads the text forward and backward at once. Three checkpoints were released.

| Checkpoint | Encoder · size | Purpose |
| :--- | :--- | :--- |
| laya | ModernBERT-large · **421M** | English decisions |
| laya-multilingual | mmBERT-base · 322M | 100+ languages |
| laya-typed-decisions | ModernBERT-large · 421M | Fine-tuned on the benchmark |

Input length is 512 tokens for the English checkpoint and 1,024 tokens for the multilingual one (extendable up to 8,192).

Installation is a single line, **pip install laya**, and requires Python 3.10 or later.

### Three question types

[choice]
Picks one of several options; inquiry-type classification, routing to a department

[score]
An ordered grade such as 0–3; urgency or severity rating

[noul]
Returns the probability of being true from 0.0 to 1.0; detecting phishing or jailbreak attempts

These correspond to Jev's Choice, Score, and true/false questions. The response includes the probability for each option, a confidence value, and which checkpoint handled it.

## Speed

![p50 latency by number of questions on a single Tesla T4](/assets/images/ai/laya-decision-model/02-photo-speed.webp)
*p50 latency by number of questions on a single Tesla T4 — Source: Convai Innovations*

According to the model card, on a single Tesla T4 GPU, one question took 39.5 milliseconds on the English checkpoint and 32.8 milliseconds on the multilingual one. Ten questions took 158.6 and 72.3 milliseconds, and fifty took 771 and 337 milliseconds. Batched input processed 103–332 questions per second.

Laya's side claims it is 7.8 times faster, putting Jev at 236–276 milliseconds. The model card notes, however, that this Jev figure was published by a third party and that the Laya developer did not measure it directly, having no access to the TypeSafe API. Laya measured on a local GPU and Jev as a hosted API differ in conditions, starting with whether a network round trip is included, so the multiple is hard to compare at face value.

Jev charges about $0.042 (₩59) per million input tokens, while Laya costs nothing to use beyond GPU running costs. The T4 is among the cheapest inference GPUs in the cloud, making it an easy size to put on an in-house server or a domestic cloud.

## Accuracy

![Accuracy comparison on the same three public datasets as Jev](/assets/images/ai/laya-decision-model/03-photo-vs-jev.webp)
*Accuracy comparison on the same three public datasets as Jev — Source: Convai Innovations*

On AG News, a 4-class news topic task, Laya scored 0.947, higher than Jev (0.910), and on DAIR Emotion, a 6-class emotion task, it scored 0.573, also above Jev (0.480). On typed-decisions, the business-style benchmark Jev published (400 items, 2,000 decisions), it was 0.766 vs. 0.727.

![typed-decisions benchmark accuracy, baselines and checkpoints](/assets/images/ai/laya-decision-model/04-chart-typed.webp)
*typed-decisions benchmark accuracy, baselines and checkpoints — Source: self-rendered from figures in the Laya model card*

The 0.766 on typed-decisions is the score of laya-typed-decisions, fine-tuned on that benchmark's training data. The base laya without fine-tuning scored 0.362 — above random (0.318) but below the majority-class baseline (0.461), which keeps picking the single most common answer. The model card itself describes Laya not as a zero-shot decision engine but as a starting point to be fine-tuned.

With more options, the advantage flips. On Banking77, a 77-class banking inquiry task, Laya scored 0.425 and Jev 0.870, and Laya's documentation says performance drops once there are more than 20 options.

The score type, which assigns ordered grades, was the weakest of the three, at 0.372 on SST-5, a 5-grade movie review task.

> In one line: it beat Jev only on narrow classification tasks where it can be fine-tuned with labeled data.

## Calibration (confidence) figures

A decision model needs its 0.85 answers to be right about 85% of the time before its confidence score can be used to separate automatic handling from human review. The metric for this mismatch is ECE (expected calibration error); lower is better.

After re-fitting the temperature on user data, Laya's English checkpoint recorded an ECE of 0.081 and the multilingual checkpoint 0.106. Out of the box, the mismatch is considerably larger, so the model card recommends recalibrating on your own task data before setting confidence thresholds. Unlike the undisclosed calibration curves I pointed out in the Jev post, Laya published before-and-after calibration figures and a reproduction script in its repository.

## Korean performance

![Accuracy per language on 51-language MASSIVE intent classification, English and multilingual checkpoints](/assets/images/ai/laya-decision-model/05-photo-languages.webp)
*Accuracy per language on 51-language MASSIVE intent classification, English and multilingual checkpoints — Source: Convai Innovations*

To classify Korean inquiries, you need the multilingual checkpoint. On 51-language intent classification (MASSIVE, 20 options, random 0.05), the English checkpoint reached a usable level (3x random or better) in 23 languages, and the multilingual checkpoint in 45.

For Korean (ko), the English checkpoint scores about 0.11 and the multilingual checkpoint about 0.45. The English checkpoint's accuracy drops sharply on non-Latin scripts; Khmer, with 0.000 accuracy at 0.952 confidence, was presented as a case of confidently wrong answers. Laya detects the input script within 0.5 milliseconds and automatically switches to the multilingual checkpoint for non-Latin scripts.

0.45 is a zero-shot score before fine-tuning, so to use it for classifying customer-service inquiries in Korea, you would need to fine-tune it on Korean labeled data and measure again.

Being Apache 2.0, a fine-tuned model can be run in-house and used commercially, and since data never goes out to an external API, it can be deployed even for finance and public-sector work in network-separated environments.

## Limits and known issues

![Accuracy by length of unrelated preceding text, multilingual checkpoint at max_len 8192](/assets/images/ai/laya-decision-model/06-photo-long-context.webp)
*Accuracy by length of unrelated preceding text, multilingual checkpoint at max_len 8192 — Source: Convai Innovations*

In a test that extended the multilingual checkpoint to 8,192 tokens and appended 20 support requests to the end of unrelated documents, it got 19/20 on short inputs. It fell to 11/20 with about 5,000 tokens of preceding text and 8/20 with 7,000. That is why you should feed in only the part needed for the decision rather than a whole long document.

- Input is text only; no images or audio
- The act_probability signal, meant to indicate whether to act, has an AUROC of 0.30, too low to use, and the docs advise using confidence thresholds instead
- noul questions are sometimes answered more on the wording of the question label than on the input content
- Work that needs reasoning, summarization, or text generation is still for LLMs

## Prior-work claim

Laya developer Nandakishor M claimed to have published the approach of producing decision probabilities with reinforcement learning instead of generating text a year before Jev. He cited two arXiv papers as evidence.

| Paper | Submitted | Content |
| :--- | :--- | :--- |
| SalesRLAgent | March 30, 2025 | Predicting sales conversion probability with reinforcement learning |
| Confidence-Aware Routing | September 23, 2025 | Branching the processing path by pre-generation confidence |

The two papers cover reinforcement learning models that output probabilities directly and confidence-based routing, which overlap in part with the idea behind Jev and Laya. Neither, however, lays out Laya's encoder architecture or its choice·score·noul question scheme as such. No official response from TypeSafe AI has been confirmed.

## Summary

[What Laya is]
Convai Innovations' 421M open-source decision model, Apache 2.0

[How it differs from Jev]
Open weights, free to self-host; Jev is a closed paid API

[Where it's strong]
Fine-tuned narrow classification, tens of milliseconds per question on a single T4

[Where it's weak]
Zero-shot accuracy, more than 20 options, long context, grading

[Check before adopting it for Korean]
Use the multilingual checkpoint, fine-tune on Korean labeled data and re-measure

## Sources

- [[Hugging Face] convaiinnovations/laya model card (checkpoints, latency, accuracy, calibration, language figures)](https://huggingface.co/convaiinnovations/laya)
- [[GitHub] NandhaKishorM/laya repository (source of five images in this post, long-context test)](https://github.com/NandhaKishorM/laya)
- [[OrcaRouter] Laya Explained: A Decision Model With Zero Output Tokens (release date, Jev comparison, known issues)](https://www.orcarouter.ai/blog/laya-decision-model-explained)
- [[eesel AI] Laya AI: the open 33ms decision model (Jev pricing, prior-paper claim)](https://www.eesel.ai/blog/laya-ai)
- [[AI Weekly] Convai ships Laya, a 421M ModernBERT decision model (zero-shot baselines)](https://aiweekly.co/alerts/convai-ships-laya-a-421m-modernbert-decision-model-apache-20)
- [[Hugging Face Blog] Laya AI Model: How It Works, Run It Locally, and Evaluate It (installation, running)](https://huggingface.co/blog/sora-2/laya-ai-model-how-it-works-run-it-locally-and-eval)
- [[arXiv] SalesRLAgent (2503.23303)](https://arxiv.org/abs/2503.23303)
- [[arXiv] Confidence-Aware Routing for Large Language Model Reliability Enhancement (2510.01237)](https://arxiv.org/abs/2510.01237)
- Exchange rate: converted at $1 ≈ ₩1,400
