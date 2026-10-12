---
title: "GPT-6.1 Sol Released — One Fifth of Astra's Price, With a Higher Coding Score"
description: "How much GPT-6.1 Sol, unveiled at DevDay 2026, improves, what it costs, and how its ranking against Claude Opus 5.5 shifts with reasoning effort"
date: 2026-09-30
category: AI
subcategory: News
tags: [openai, gpt-6-1-sol, devday-2026, llm-pricing, model-release]
image: /assets/og/en-2026-09-30-gpt-61-sol-release.png
---

OpenAI unveiled **GPT-6.1 Sol** at DevDay 2026 on September 29, 2026. It is an upgrade to GPT-6 Sol, released on September 22, that keeps the price the same while bringing performance close to GPT-6 Astra.

Standard API pricing is $2 (₩2,800) per million input tokens and $10 (₩14,000) per million output tokens — one fifth of Astra. On the coding benchmark DeepSWE v1.1, it beat Astra's best score by 1.1 percentage points, at about one seventh of Astra's cost per task.

![Model cards for GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna](/assets/images/ai/gpt-61-sol-release/01-hero-gpt61-sol.webp)
*Model cards for GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna — Source: OpenAI*

[GPT-6 Sol and Luna Released — Half the API Price, and How to Choose Between the Two](/en/posts/gpt-6-sol-luna-release/)

## Key points of the announcement

![OpenAI logo](/assets/images/ai/gpt-61-sol-release/02-logo-openai.webp)
*OpenAI logo — Source: OpenAI*

OpenAI said GPT-6.1 Sol is substantially better than GPT-6 Sol at writing and debugging code, understanding documents, and running multi-step workflows. According to OpenAI, it came close to Astra on several evaluations at a much lower cost.

- Model ID: **gpt-6.1-sol**, available in ChatGPT Work, Codex, and the API
- Pricing: same as GPT-6 Sol, with only cached input cut in half
- Coding: DeepSWE v1.1 **75.2%**, 6.4 percentage points above GPT-6 Sol's best
- Computer use: 2.1 percentage points behind Astra on OSWorld 2.0
- Most capable model: still GPT-6 Astra

## Pricing and availability

![Cached input price per million tokens by model](/assets/images/ai/gpt-61-sol-release/03-chart.webp)
*Cached input price per million tokens by model — Source: self-rendered from OpenAI's announcement and API docs*

Input and output prices are the same as GPT-6 Sol; what changed is cached input. The cached input price, charged when repeated requests reuse the same prefix, dropped from $0.20 (₩280) to $0.10 (₩140) per million tokens.

| Item (per million tokens) | GPT-6.1 Sol | GPT-6 Astra |
| :--- | :--- | :--- |
| Input | **$2 (₩2,800)** | $10 (₩14,000) |
| Cached input | <mark>$0.10 (₩140)</mark> | $1 (₩1,400) |
| Output | **$10 (₩14,000)** | $50 (₩70,000) |

Cached input is 95% cheaper than standard input. OpenAI said this lowers the cost of agent tasks that load the same context many times.

Per the API docs, the context window is 1.05 million tokens, max output is 128,000 tokens, and the training data cutoff is April 30, 2026. When a single request exceeds 272,000 tokens, input is billed at 2x and output at 1.5x.

In ChatGPT, Plus, Pro, Business, Enterprise, and Edu users can use it in **ChatGPT Work** and Codex. It is not yet available in Chat, the regular conversation screen, and the Free and Go plans are not included.

A faster version, **GPT-6.1 Sol Ultrafast**, was announced at the same time. OpenAI said Ultrafast is up to 8 times faster than GPT-6 Astra, and VentureBeat reported up to 300 tokens per second at 6 times the standard price. It will be offered in the API and a new $500 (₩700,000)-a-month Pro tier, and according to VentureBeat, Sol Ultrafast will roll out gradually over the next few days.

API usage is billed in dollars, so the cost in won for developers in Korea depends on the exchange rate.

## Coding performance

![Official chart of DeepSWE scores and cost per task](/assets/images/ai/gpt-61-sol-release/04-photo-deepswe.webp)
*Official chart of DeepSWE scores and cost per task — Source: OpenAI*

DeepSWE v1.1 is a benchmark of long software tasks solved in real codebases.

| Model (reasoning effort) | Score (%) | Cost per task |
| :--- | :--- | :--- |
| GPT-6.1 Sol (high) | <mark>75.2</mark> | **$0.65 (₩910)** |
| GPT-6 Astra (xhigh) | 74.1 | $4.43 (₩6,202) |
| GPT-6 Sol (max) | 68.8 | $2.74 (₩3,836) |

At one reasoning-effort level lower, GPT-6.1 Sol scored 6.4 percentage points above GPT-6 Sol's best. It is 1.1 percentage points above Astra's best, at about one seventh of the cost per task.

On the same benchmark, GPT-6 Sol was 1.1 percentage points from Claude Fable 5 (69.9%) when it was announced on September 22. This announcement did not include DeepSWE numbers for Anthropic models.

## Workflow automation and computer use

![Anthropic logo](/assets/images/ai/gpt-61-sol-release/05-logo-anthropic.webp)
*Anthropic logo — Source: Anthropic*

AutomationBench is a benchmark that handles entire workflows using 47 tools across sales, marketing, operations, customer support, finance, and HR. At medium reasoning effort, GPT-6.1 Sol scored 31.7%, 2.2 percentage points above Claude Opus 5.5 (29.5%) at the same setting, at about one third of the cost.

Raising the reasoning effort changes the ranking.

| Model (max) | Score (%) | Cost per task |
| :--- | :--- | :--- |
| Claude Opus 5.5 | <mark>42.5</mark> | $1.44 (₩2,016) |
| GPT-6 Astra | 41.4 | $1.73 (₩2,422) |
| GPT-6.1 Sol | 36.1 | **$0.30 (₩420)** |

Opus 5.5 posted the top score, while GPT-6.1 Sol costs roughly one fifth as much. The Opus 5.5 figure includes fallback calls to another model.

### Document understanding

On GDP.pdf, which answers questions from complex PDFs across 10 fields including finance, healthcare, and law, GPT-6.1 Sol (high) scored 32.0% at $0.35 (₩490) per task. Opus 5.5's best was 28.8% and Astra's best was 32.2%.

### Computer use and scientific research

On the OSWorld 2.0 offline set, GPT-6.1 Sol at max reasoning effort scored 71.4%, 7 percentage points above GPT-6 Sol (64.4%). That is 2.1 percentage points behind Astra (73.5%), at about one seventh of the cost per task.

On Terminal-Bench Science 0.1, which covers scientific workflows, it scored more than twice GPT-6 Sol. Its cost per task of $5.47 (₩7,658) is more than 75% lower than Opus 5.5 at $23.21 (₩32,494) and Astra at $23.80 (₩33,320), but the top score was Astra's 68.1%.

## Factual accuracy and safety evaluations

![Rate of not reporting a broken search tool](/assets/images/ai/gpt-61-sol-release/06-chart.webp)
*Rate of not reporting a broken search tool — Source: self-rendered from OpenAI's announcement*

In an internal OpenAI evaluation built from conversations where users reported errors, the factual error rate at xhigh was 4.1% for GPT-6.1 Sol, 4.5% for GPT-6 Sol, and 4.0% for Astra. The evaluation deliberately collects hard questions, so these are not error rates in everyday use.

In an evaluation of whether the model tells the user when the search tool isn't working instead of answering by guesswork, the rate of not telling dropped from 4.9% for GPT-6 Sol to 2.1% for GPT-6.1 Sol. GPT-6 Luna was at 28.7% on the same evaluation.

OpenAI said GPT-6.1 Sol also had lower failure rates than GPT-6 Sol on evaluations of following explicit restrictions and blocking unauthorized outcomes during agent tasks. As with GPT-6 Astra and GPT-6 Sol, no attempts to circumvent the automated safety review system were observed.

## Summary so far

![GPT-6.1 Sol summary](/assets/images/ai/gpt-61-sol-release/07-items.webp)
*GPT-6.1 Sol summary — Source: summary of this post · self-rendered*

## What to watch next

- When availability expands to ChatGPT's Chat screen and the Free and Go plans
- The actual launch date and confirmed pricing of GPT-6.1 Sol Ultrafast
- Whether outside services such as GitHub Copilot adopt GPT-6.1 Sol
- Comparison figures Anthropic publishes on the same benchmarks

## Sources

- [[OpenAI] Introducing GPT-6.1 Sol (2026-09-29, pricing, benchmarks, safety evaluations, source of two images in this post)](https://openai.com/ko-KR/index/introducing-gpt-6-1-sol/)
- [[OpenAI API Docs] GPT-6.1 Sol (context, long-context pricing, training cutoff)](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [[OpenAI] GPT-6.1 Sol system card addendum (2026-09-29)](https://deploymentsafety.openai.com/gpt-6-1-sol)
- [[VentureBeat] Ultrafast speed and price multiplier (2026-09-29)](https://venturebeat.com/technology/openais-gpt-6-1-sol-offers-astra-like-performance-at-1-5th-price-a-new-ultrafast-tier-clocks-at-300-tokens-per-second)
- [[TechCrunch] GPT-6.1 Sol launch and availability (2026-09-29)](https://techcrunch.com/2026/09/29/openai-launches-gpt-6-1-sol-says-it-nearly-matches-gpt-6-astra-and-costs-less/)
- [[Unite.AI] Codex and ChatGPT features announced alongside at DevDay 2026 (2026-09-29)](https://www.unite.ai/openai-unveils-gpt-6-1-sol-at-devday-with-new-codex-and-chatgpt-tools/)
- Exchange rate: converted at $1 ≈ ₩1,400
