---
title: "Claude Sonnet 5.5 Released — Scores Close to Opus 5.5 at Half the Price"
description: "Benchmarks within 1–2 points of Opus 5.5, unchanged pricing, and how to choose between the two models by task"
date: 2026-10-05
category: AI
subcategory: News
tags: [anthropic, claude-sonnet-5-5, model-release, llm-pricing, benchmark]
image: /assets/og/en-2026-10-05-claude-sonnet-55-release.png
---

Anthropic released Claude Sonnet 5.5 on September 28, 2026. It costs half as much as Opus 5.5, released on September 22, yet came within 1–2 points of Opus 5.5 on work-document and computer-use benchmarks — and actually scored higher on terminal tasks.

Pricing is the same as Sonnet 5, and output speed is more than 30% faster. Anthropic says it handles the same work with fewer tokens, so cost per task is up to 30% lower.

![Claude Sonnet 5.5 launch key art](/assets/images/ai/claude-sonnet-55-release/01-hero-keyart.webp)
*Claude Sonnet 5.5 launch key art — Source: Anthropic*

## What was released

![Chart comparing Terminal-Bench 4.0 scores](/assets/images/ai/claude-sonnet-55-release/02-chart.webp)
*Chart comparing Terminal-Bench 4.0 scores — Source: self-rendered from Anthropic's announcement*

Sonnet 5.5 is the second model in the Claude 5.5 family, offered as a faster, cheaper option than Opus 5.5. It is available right away in the Claude apps, the Claude API, and on Amazon Web Services, Google Cloud, and Microsoft Azure.

- API model ID: **claude-sonnet-5-5**
- 1M-token context window (the input length you can send at once), up to 128,000 output tokens
- Output speed more than 30% faster than Sonnet 5
- Training data cutoff: June 2026
- Default reasoning effort **high**, with adaptive thinking that lets the model decide how much to reason

The biggest jump was on the terminal-task benchmark *Terminal-Bench 4.0*. Sonnet 5 scored 10.3%; Sonnet 5.5 scored 70.6%, 4.2 percentage points above Opus 5.5's 66.4%.

## Benchmarks

![Evaluation summary table from the Claude Sonnet 5.5 system card](/assets/images/ai/claude-sonnet-55-release/03-capture.webp)
*Evaluation summary table from the Claude Sonnet 5.5 system card — Source: Anthropic Claude Sonnet 5.5 System Card*

In the system card's evaluation summary, Sonnet 5.5's results split into items where it nearly matches Opus 5.5 and items where it scores lower. All results are averages of five runs at maximum reasoning effort.

[Within 1–2 points of Opus 5.5]
Work-output evaluation *GDPval-AA v2.1* 1,844 vs. 1,846, computer use *OSWorld 2.1* 80.1% vs. 81.8%, document work *AA-Briefcase v1.1* 1,811 vs. 1,822

[Higher than Opus 5.5]
*Terminal-Bench 4.0* 70.6% vs. 66.4%, work automation *AutomationBench* 44.7% vs. 42.5%, medical professional questions *HealthBench Professional* 69.2% vs. 65.6%

[Lower than Opus 5.5]
Coding *SWE-Bench Pro* 81.3% vs. 89.9%, *FrontierCode v1.1* 46.2% vs. 54.4%, *Humanity's Last Exam* without tools 56.9% vs. 64.4%

Against GPT-6 Sol, Sonnet 5.5 was higher on *GDPval-AA* (1,844 vs. 1,487) and *AutomationBench* (44.7% vs. 32.0%), while GPT-6 Sol scored higher on *FrontierCode* (46.2% vs. 49.3%).

Hedge fund Balyasny Asset Management said tokens per answer dropped from 497,000 with Sonnet 5 to 121,000, and Box said it was 2.4 times faster with 12% fewer total tokens. Zendesk said support tickets were handled 20% faster.

## Pricing

![Chart of output price per 1M tokens by model](/assets/images/ai/claude-sonnet-55-release/04-chart.webp)
*Chart of output price per 1M tokens by model — Source: self-rendered from Anthropic pricing docs and OpenAI's announcement*

Standard API pricing is $2 (₩2,800) input and $10 (₩14,000) output per 1M tokens. That is half of Opus 5.5's $4 (₩5,600) input and $20 (₩28,000) output, and the same price tier as GPT-6.1 Sol, released September 30.

| Item | Sonnet 5.5 | Opus 5.5 |
| :--- | :--- | :--- |
| Input | <mark>$2 (₩2,800)</mark> | $4 (₩5,600) |
| Output | <mark>$10 (₩14,000)</mark> | $20 (₩28,000) |
| Cache read | $0.20 (₩280) | $0.20 (₩280) |
| Batch input · output | $1 · $5 (₩1,400 · ₩7,000) | $2 · $10 (₩2,800 · ₩14,000) |

Cache reads alone cost the same for both models, $0.20 (₩280). That's because Opus 5.5 charges 5% of the input price for cache reads, and Sonnet 5.5 charges 10%. For agent workloads that repeatedly read the same long documents, the price difference between the two models comes only from output and new input.

Sonnet 5's $2/$10 was originally a launch discount through August 31, 2026, set to rise to $3/$15 on September 1, but Anthropic withdrew the increase and made it the standard price. Sonnet 5.5 carries that price over unchanged.

## Choosing between it and Opus 5.5

![Anthropic logo](/assets/images/ai/claude-sonnet-55-release/05-logo-anthropic.webp)
*Anthropic logo — Source: Anthropic*

| Task | Score gap | Pick |
| :--- | :--- | :--- |
| Writing reports and documents | 1–11 points | **Sonnet 5.5** |
| Computer and browser use | 1.7 pp | **Sonnet 5.5** |
| Terminal and work automation | Sonnet higher | **Sonnet 5.5** |
| Large-scale code changes | 8.6 pp | Opus 5.5 |
| Coding with images mixed in | 7.1 pp | Opus 5.5 |
| Hard reasoning without tools | 7.5 pp | Opus 5.5 |

Anthropic's developer docs recommend starting with Opus 5.5 for most tasks and classify Sonnet 5.5 as the model that balances speed and performance. Going by scores alone, switching to Sonnet 5.5 changes results little outside large code work — at half the price.

## Using it from Korea

API charges are billed in dollars, so the cost in won depends on the exchange rate. Per Anthropic's docs, 1M tokens is about 2.5 million characters, so for an individual using it conversationally, a Claude app subscription plan is the first thing to consider rather than the API.

The system card evaluated harmful-request refusal rates in seven languages including Korean, and *GMMLU*, the average accuracy across 42 languages, was 92.1%, up from Sonnet 5's 89.2%. A Korean-only score was not published, however.

## What to watch next

- Whether the default model on each Claude app plan switches to Sonnet 5.5, and changes to usage limits
- The retirement date of Haiku 4.5, scheduled for after October 15, 2026, and whether a successor Haiku model is announced
- Results from independent benchmarks (Artificial Analysis and others) at the same price tier as GPT-6.1 Sol

## Sources

- [[Anthropic] Introducing Claude Sonnet 5.5 (2026-09-28)](https://www.anthropic.com/claude-sonnet-5-5)
- [[Anthropic] Claude Sonnet 5.5 System Card (source of one image in this post)](https://www-cdn.anthropic.com/870c8f525702625d2c62fc6dd04c857e3250bec1/Claude%20Sonnet%205.5%20System%20Card.pdf)
- [[Anthropic] Models overview (model ID, context, default effort)](https://platform.claude.com/docs/en/about-claude/models/overview)
- [[Anthropic] Pricing (API, cache, and batch pricing; Sonnet 5 price footnote)](https://platform.claude.com/docs/en/about-claude/pricing)
- [[Anthropic] Claude release notes (2026-09-28)](https://support.claude.com/en/articles/12138966-release-notes)
- Exchange rate: converted at $1 ≈ ₩1,400
