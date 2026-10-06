---
title: "Gemini 4 Argon Unveiled — 1M-Token Output Limit, Cyber Defenders First"
description: "The output limit, benchmarks, and introductory price of Argon, the first Gemini 4 model, and its staged release that opens to cyber defense organizations first"
date: 2026-10-02
category: AI
subcategory: News
tags: [gemini, google-deepmind, gemini-4-argon, model-release, cybersecurity]
image: /assets/og/en-2026-10-02-gemini-4-argon.png
---

On September 30, 2026, Google announced **Gemini 4 Argon**, the first model in the Gemini 4 family. The biggest change is the output limit — how much it can generate in one go — raised from 64,000 tokens to 1 million.

It isn't open to everyone yet, though. Google said it will go to cyber defense organizations first, and then to the paid API and Google AI Ultra subscribers after a US government pre-release review process.

![Gemini 4 Argon launch key art](/assets/images/ai/gemini-4-argon/01-hero-keyart.webp)
*Gemini 4 Argon launch key art — Source: Google*

## What was announced

Google DeepMind SVP Koray Kavukcuoglu announced it himself on Google's official blog. Argon targets real-world software development, enterprise knowledge work such as law and finance, and cyber defense.

- Output limit: raised from 64,000 to **1M tokens**
- Introductory price: $2 (₩2,800) input and $10 (₩14,000) output per 1M tokens
- Release order: Fairwind program members → paid API and Google AI Ultra
- Internal use: thousands of Google employees already use it at work

No release date was given. Google only wrote that it would open it to developers, businesses, and consumers "as soon as possible."

## Benchmarks

![Official Gemini 4 Argon benchmark comparison table](/assets/images/ai/gemini-4-argon/02-photo.webp)
*Official Gemini 4 Argon benchmark comparison table — Source: Google*

Google compared Argon with GPT-6 Astra, Claude Fable 5.1, and Claude Opus 5.5 on 19 items. Argon was first outright on 13 and tied for first on CWE-bench v1; GPT-6 Astra led on 3 items and Claude Opus 5.5 on 2.

The widest gap was on Harvey's Legal Agent Benchmark, a legal agent evaluation, where Argon scored 19.6% to runner-up Claude Fable 5.1's 6.7%. On AutomationBench, which measures work automation, Argon scored 51.3% to Claude Opus 5.5's 42.5%, an 8.8-point gap.

On the coding benchmark DeepSWE v1.1, it scored 77.9%, more than 3 points above Claude Opus 5.5 (74.2%) and GPT-6 Astra (74.1%). GPT-6.1 Sol, released September 29, isn't in this table; OpenAI's reported score for Sol on the same benchmark is 75.2%.

### Where Argon scored lower

| Benchmark | Argon | Leader |
| :--- | :--- | :--- |
| FrontierSWE v2 | 55.0% | Astra **65.5%** |
| Terminal-Bench Science | 57.6% | Astra **68.1%** |
| Terminal-bench 4.0 | 57.4% | Opus 5.5 **66.4%** |
| PostTrainBench | 45.3% | Opus 5.5 **49.3%** |
| OSWorld-2.0 | 69.2% | Astra **72.6%** |

Three of the five items where it scored lower were evaluations in environments that directly operate a terminal or computer. All scores were measured by Google itself, and the evaluation methodology was published separately on the Google DeepMind site.

## A 1M-token output

The output limit is the number of tokens (the units a model processes text in) the model can generate in a single response. It is a different number from the context window, which is how much it can take as input.

Google cited tasks that work a problem all the way through in one reasoning flow while generating hundreds of thousands of tokens as the reason for raising the limit. Examples included converting an entire codebase to another language and auditing many documents at once.

### Internal examples at Google

[libgav1 video decoder]
Converted 32,000 lines of SIMD code to safe Rust, 2.7 times faster than the existing Rust port

[Fuchsia Zircon kernel]
Converting more than 800,000 lines of C/C++ to Rust, now in pre-deployment validation

[Data center memory]
Analyzed company-wide profiling data to free up more than 300 TiB of memory

## Cyber defenders first

Argon goes first to the **Fairwind program**, which Google launched on September 2 together with Gemini 3.8 Flash Cyber. Only defensive organizations vetted and selected by Google — government agencies, critical infrastructure operators, software maintainers, and so on — can join.

Google said it is giving Argon to these members and its internal teams **without cybersecurity restrictions**. The idea is to let them use its ability to find, verify, and fix vulnerabilities without limits, and to tune the security restrictions based on their feedback before general release.

![CWE-bench v1 leaderboard](/assets/images/ai/gemini-4-argon/03-photo-cwebench.webp)
*CWE-bench v1 leaderboard — Source: Google*

On CWE-bench v1, which measures the ability to fix vulnerabilities, Argon scored 68%, the same as Grok 4.7 and GPT-6 Astra. Google said cloud security company Wiz used Argon in its free public-infrastructure protection work and found a critical vulnerability exposing sensitive personal data in medical software used by hospitals worldwide.

Google models' security-related behavior was in the news just before this. On September 18, Google admitted that Gemini had accessed the systems of three real companies during a hacking evaluation run by outside firm Irregular.

## Safeguards

Google said it is taking part in the US government's voluntary pre-release model access process for pre-launch review. It described the safeguards in categories including misuse prevention, prompt injection defense, and misalignment monitoring.

- Misuse prevention: refuses cyber and CBRN attack requests, and monitors the model's internal activations to find misuse
- Misalignment monitoring: blocks attempts to carry out a task in ways that go beyond the user's intent

![Gray Swan indirect prompt injection attack success rates](/assets/images/ai/gemini-4-argon/04-photo-grayswan.webp)
*Gray Swan indirect prompt injection attack success rates — Source: Google*

**Indirect prompt injection** — steering a model with instructions planted in web pages or documents — was measured with Gray Swan's evaluation. With 15 attack attempts, Argon's success rate was 0.7%, lower than Claude Opus 5.5 and Claude Fable 5.1 (1.0% each).

## Pricing

![API output price per 1M tokens compared](/assets/images/ai/gemini-4-argon/05-chart.webp)
*API output price per 1M tokens compared — Source: self-rendered from official Google, OpenAI, and Anthropic pricing*

| | Input | Output |
| :--- | :--- | :--- |
| Argon introductory | $2 (₩2,800) | **$10 (₩14,000)** |
| Argon list | $4 (₩5,600) | $20 (₩28,000) |
| Cached input (introductory) | $0.10 (₩140) | - |

Prices are per 1M tokens. The introductory price matches GPT-6.1 Sol's standard price, and the list price after the introductory period matches Claude Opus 5.5. When the introductory period ends hasn't been announced.

Cached input is the rate charged when you resend the same prefix, at a 95% discount from the input price. On output price alone, it is one fifth of GPT-6 Astra (₩70,000).

## Availability in Korea

Argon hasn't been released to the public, including in Korea. Whether any Korean organization is in the Fairwind program hasn't been disclosed.

Once released, the paid Gemini API and a Google AI Ultra subscription will be the first ways to use it. At I/O in May, Google restructured AI Ultra into two tiers at $100 (₩140,000) and $200 (₩280,000) a month; the API is billed in dollars, so the cost in won depends on the exchange rate.

## What to watch next

- The release schedule for the paid API and AI Ultra, and how long the introductory price lasts
- How far the security-restricted general release will go in answering security-related requests
- Independent benchmark results from outside organizations

## Sources

- [[Google] Gemini 4 Argon: our next era of frontier intelligence (2026-09-30; pricing, release order, benchmarks; source of four images in this post)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- [[Google DeepMind] Gemini 4 Argon evaluation methodology](https://deepmind.google/models/evals-methodology/gemini-4-argon)
- [[VentureBeat] Google unveils Gemini 4 Argon, but in limited release (2026-09-30)](https://venturebeat.com/technology/google-unveils-gemini-4-argon-retaking-benchmark-lead-over-openai-and-anthropic-but-in-limited-release)
- [[Anthropic] Claude API pricing (Claude Opus 5.5)](https://platform.claude.com/docs/en/about-claude/pricing)
- [[Google Korea Blog] Google AI subscriptions at Google I/O 2026 (2026-05-19, AI Ultra tiers)](https://blog.google/intl/ko-kr/company-news/technology/google-ai-subscriptions-kr/)
- Exchange rate: converted at $1 ≈ ₩1,400
