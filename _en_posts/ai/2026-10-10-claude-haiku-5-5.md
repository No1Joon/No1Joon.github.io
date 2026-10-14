---
title: "Claude Haiku 5.5 Released — One Tenth the Price of Haiku 4.5"
description: "Pricing and computer-use benchmarks for Haiku 5.5, the last model in the Claude 5.5 family, and the settings to change when switching"
date: 2026-10-10
category: AI
subcategory: News
tags: [anthropic, claude-haiku, llm, pricing, computer-use]
image: /assets/og/en-2026-10-10-claude-haiku-5-5.png
---

Anthropic released Claude Haiku 5.5 on October 7, 2026. For prompts of 100,000 tokens or less, it costs $0.10 (₩140) per million input tokens and $0.50 (₩700) per million output tokens, one tenth of Haiku 4.5, and its score on the computer-use benchmark OSWorld 2.1 rose from 15.7% to 72.4%. Following Opus 5.5 on September 22 and Sonnet 5.5 on September 28, all three models in the Claude 5.5 family are now out.

![Claude Haiku 5.5 announcement key visual](/assets/images/ai/claude-haiku-5-5/01-hero-keyart.webp)
*Claude Haiku 5.5 announcement key visual — Source: Anthropic*

## What was announced

Haiku is the smallest and fastest line among Claude models. Anthropic introduced Haiku 5.5 for high-volume, cost-sensitive work such as summarization, context compaction, database lookups, and classification, and also suggested using it as a sub-agent that handles work handed off by Opus 5.5 or Sonnet 5.5 in coding tasks.

| Item | Haiku 5.5 | Haiku 4.5 |
| :--- | :--- | :--- |
| Context window | **1 million tokens** | 200,000 tokens |
| Max output | 128,000 tokens | 64,000 tokens |
| Reasoning control | 5 effort levels | Token budget |
| Knowledge cutoff | June 2026 | February 2025 |

Effort is a setting that determines how hard the model reasons before generating an answer, with five levels — Low, Medium, High, Xhigh, and Max — and the API default is Medium. This is the first time effort applies to Haiku. It's available now on the Claude API, Amazon Web Services, Google Cloud, and Microsoft Azure (Foundry).

## Benchmarks

![Chart of OSWorld 2.1 scores by model](/assets/images/ai/claude-haiku-5-5/en/02-chart-osworld.webp)
*Chart of OSWorld 2.1 scores by model — Source: self-rendered from Anthropic's announcement page*

The score that rose most is *OSWorld 2.1*, which has the model look at and operate a computer screen. Haiku 4.5 scored 15.7%, while Haiku 5.5 recorded 72.4%, 23.5 percentage points higher than OpenAI's small model GPT-6 Luna (48.9%) and 11.5 points behind Sonnet 5.5 (83.9%).

| Benchmark | Haiku 5.5 | Haiku 4.5 |
| :--- | :--- | :--- |
| Terminal-Bench 4.0 | **39.2%** | 0.0% |
| HLE (no tools) | **45.9%** | 10.2% |
| HLE (with tools) | **57.4%** | 18.7% |
| Chartography (no tools) | **46.4%** | 6.4% |
| GDPval-AA v2.1 (Elo) | **1,620** | 735 |

On *Terminal-Bench 4.0*, which looks at terminal tasks, Haiku 4.5 scored 0.0%. Haiku 5.5's 39.2% is more than double GPT-6 Luna's (16.4%) but 31.4 points below Sonnet 5.5's (70.6%). On the code-writing benchmark *FrontierCode 1.1*, the three models were closest: Haiku 5.5 at 46.4%, GPT-6 Luna at 42.4%, and Sonnet 5.5 at 52.1% (Xhigh).

## Pricing

![Chart of output price per million tokens by model](/assets/images/ai/claude-haiku-5-5/en/03-chart.webp)
*Chart of output price per million tokens by model — Source: self-rendered from Anthropic's model documentation*

Haiku 5.5 pricing splits into two tiers by prompt length. Requests of 100,000 tokens or less cost one tenth of Haiku 4.5, and requests over 100,000 tokens cost half of Haiku 4.5.

| Per million tokens | Up to 100K | Over 100K |
| :--- | :--- | :--- |
| Input | <mark>$0.10 (₩140)</mark> | $0.50 (₩700) |
| Output | <mark>$0.50 (₩700)</mark> | $2.50 (₩3,500) |
| Cache read | $0.01 (₩14) | $0.05 (₩70) |
| Cache write | $0.125 (₩175) | $0.625 (₩875) |

The price list says one tenth, but the savings Anthropic cites average about 75%. Haiku 5.5 uses the new tokenizer (the rules for splitting text into tokens) used since Claude 4.7, so the same text counts as about 30% more tokens than on Haiku 4.5, and reasoning blocks from earlier turns keep being included in the input. Large images fall under high-resolution processing, so a single 2,000×1,500-pixel image counts as about 2.5 times the tokens it did on Haiku 4.5.

In the same announcement, Sonnet 5.5's cache read price was cut from $0.20 (₩280) to $0.10 (₩140) per million tokens. The batch API is 50% off for all models.

## Sub-agent setups

![Concept image of a large model handing out work to small models](/assets/images/ai/claude-haiku-5-5/04-agy.webp)
*Concept image of a large model handing out work to small models — Source: concept image · self-generated with agy*

In this approach, a large model such as Opus 5.5 or Sonnet 5.5 makes the plan and distributes simple but high-volume tasks such as file exploration, summarization, and search to multiple Haiku 5.5 instances. Since its output price is one fortieth of Opus 5.5's, moving the token-heavy exploration stage to Haiku lowers the overall cost.

Compatibility of reasoning blocks between models has a direction. On the Claude API and Google Cloud, Opus 5.5 and Sonnet 5.5 can read reasoning blocks generated by Haiku 5.5, but Haiku 5.5 can't read reasoning blocks from Opus 5.5 or Sonnet 5.5, and the API drops them without an error.

Anthropic said it set Haiku 5.5's cybersecurity safeguards to be stricter than Haiku 4.5's and less strict than Sonnet 5.5's. It widens what's allowed for defensive work and restricts offensive work such as penetration testing.

## Moving from Haiku 4.5

![Summary card of settings to change when switching to Haiku 5.5](/assets/images/ai/claude-haiku-5-5/en/05-items.webp)
*Summary card of settings to change when switching to Haiku 5.5 — Source: self-rendered from Anthropic's migration guide*

If you only change the model name, requests that used to work may return 400 errors. That's because several settings Haiku 4.5 allowed aren't supported on Haiku 5.5.

![Anthropic logo](/assets/images/ai/claude-haiku-5-5/06-logo-anthropic.webp)
*Anthropic logo*

On Amazon Bedrock, Haiku 5.5's structured outputs aren't available, and Haiku 4.5 Priority Tier contracts don't apply to Haiku 5.5. If you use Claude Code, the **/claude-api migrate** command applies the model ID swap and the setting changes above in one go. Anthropic said it won't retire Haiku 5.5 before October 7, 2027.

## Sources

- [[Anthropic] Claude Haiku 5.5 announcement: pricing, benchmarks, safeguards (2026-10-07)](https://www.anthropic.com/claude-haiku-5-5)
- [[Anthropic] Models overview: context window, max output, knowledge cutoff, default effort](https://platform.claude.com/docs/en/about-claude/models/overview)
- [[Anthropic] Haiku 5.5 migration guide: tokenizer, error-causing settings, platform limits](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)
- [[Anthropic] Claude Haiku 5.5 system card](https://www.anthropic.com/claude-haiku-5-5-system-card)
- Exchange rate: converted at $1 ≈ ₩1,400
