---
title: "Claude Opus 5.5 Released — 20% Cheaper, and Four Requests That Now Return 400"
description: "Performance close to Fable 5.1, the lower pricing, and the four requests that return a 400 error when you move over from Opus 5"
date: 2026-09-23
category: AI
subcategory: News
tags: [anthropic, claude-opus-5-5, model-release, llm-pricing, api-migration]
image: /assets/og/en-2026-09-23-claude-opus-55-release.png
---

Anthropic unveiled Claude Opus 5.5 on September 22, 2026. It performs comparably to the higher-tier Claude Fable 5.1 on most tasks, while pricing came down 20% on both input and output from Opus 5.

Anthropic said that at default settings, typical tasks cost 40% less than with Opus 5.

If you're already using the API, though, changing the model name is not enough. Four requests that worked on Opus 5 now return a 400 error.

![Official key visual for the Claude Opus 5.5 announcement](/assets/images/ai/claude-opus-55-release/01-hero-opus55.webp)
*Official key visual for the Claude Opus 5.5 announcement — Source: Anthropic*

## The gist of the announcement

Claude Opus 5.5 is the first model in the new Claude 5.5 family, and the first released after Anthropic CEO Dario Amodei published his piece arguing that frontier model development should be paced. Sonnet 5.5 and Haiku 5.5 of the same generation were announced for release within weeks.

- Performance: on par with Fable 5.1 on most tasks, with the top score among compared models on 7 of the 9 benchmarks Anthropic published
- Pricing: $4 (₩5,600) per million input tokens, $20 (₩28,000) per million output tokens
- Speed: output generation more than 30% faster than Opus 5
- Context window (how much input it takes at once): 1 million tokens, max output 128,000 tokens, the same as Opus 5
- Availability: Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry
- Subscriptions: higher 5-hour usage limits on the Pro, Max, Team, and seat-based Enterprise plans, plus one chance for subscribers to reset their usage limit whenever they choose

Anthropic explained that Opus 5.5 takes less compute to serve than Opus 5, and that the price cut reflects that difference.

## Benchmark figures

![Terminal-Bench 4.0 scores by model](/assets/images/ai/claude-opus-55-release/02-chart-terminalbench.webp)
*Terminal-Bench 4.0 scores by model — Source: self-rendered from figures in Anthropic's announcement*

Terminal-Bench 4.0 is an agent benchmark in which the model solves tasks by running commands in a terminal. Opus 5.5 scored 66.4%, ahead of GPT-6 Astra (57.9%) and Fable 5.1 (55.8%), and 14.1 percentage points above Opus 5 (52.3%). The Opus 5.5 figure is at xhigh, while GPT-6 Astra's is the high setting as reported by OpenAI.

### Against Fable 5.1

| Benchmark | Opus 5.5 | Fable 5.1 |
| :--- | :--- | :--- |
| FrontierCode v1.1 (%) | **54.4** | 50.3 |
| CursorBench 4.0 (%) | <mark>57.8</mark> | 51.8 |
| GDPval-AA v2.1 (Elo) | **1846** | 1735 |
| HLE with tools (%) | **67.7** | 65.6 |
| OSWorld 2.0 (%) | 81.8 | 80.7 |
| Chartography (%) | 89.0 | 88.4 |

The gaps are 6.0 percentage points on CursorBench 4.0, a coding-tool task, and 111 points on GDPval-AA, which pits knowledge work against itself in Elo. Computer use (OSWorld 2.0) and chart reading (Chartography) are within a percentage point, so in that range it is close to even with Fable 5.1, as Anthropic said.

### Against GPT-6 Astra

| Benchmark | Opus 5.5 | GPT-6 Astra |
| :--- | :--- | :--- |
| AutomationBench (%) | 40.0 | **41.4** |
| Terminal-Bench-Science 0.1 (%) | 58.7 | <mark>64.6</mark> |
| HLE with tools (%) | **67.7** | 57.2 |
| GDPval-AA v2.1 (Elo) | **1846** | 1542 |

GPT-6 Astra is higher on workflow automation (AutomationBench) and science terminal tasks (Terminal-Bench-Science). Anthropic evaluated with safeguards on, and noted in a footnote that when safeguards intervene, Opus 4.8 handled cybersecurity tasks and Opus 5 handled biology and LLM (large language model) development tasks instead. Anthropic's explanation is that the science score may have come out lower for this reason.

## Pricing changes

![Change in cache read price per million tokens](/assets/images/ai/claude-opus-55-release/03-chart.webp)
*Change in cache read price per million tokens — Source: self-rendered from Anthropic's price list*

The biggest cut is to cache reads — the charge for storing a long input you sent earlier and reading it again — down 60%, from $0.50 (₩700) to $0.20 (₩280) per million tokens. Anthropic explained that most of the cost of agent and coding work comes from cache reads.

| Per million tokens | Opus 5 | Opus 5.5 |
| :--- | :--- | :--- |
| Input | $5 (₩7,000) | **$4 (₩5,600)** |
| Output | $25 (₩35,000) | <mark>$20 (₩28,000)</mark> |
| Cache write (5 min) | $6.25 (₩8,750) | **$5 (₩7,000)** |

- Cache write (1 hour): $8 (₩11,200)
- Batch processing: half the base rate — $2 (₩2,800) input, $10 (₩14,000) output
- Fast mode: up to 2.5x faster output, $8 (₩11,200) input and $40 (₩56,000) output, available only in the Claude API and Claude Code (not on Bedrock, Google Cloud, or Foundry)

The 40% saving combines the 20% rate cut with fewer tokens used for the same work. It compares default settings, so it also reflects the default effort dropping from Opus 5's high to Opus 5.5's medium. Early adopters put the token reduction in concrete numbers.

- Optiver: matched Opus 5's quality with half the turns, time, and output tokens, cutting costs 40–50%
- Box: used one third the tokens of Opus 5 while maintaining accuracy
- Kiro: solved more tasks than Opus 5 with 40% fewer calls and half the tokens
- Deloitte: found 72% of known bugs at the lowest effort, against 56% for Opus 5 at high

API usage is billed in dollars, so the cost in won for users in Korea depends on the exchange rate.

## What developers have to change

![Concept image of always-on thinking and the effort setting](/assets/images/ai/claude-opus-55-release/04-agy-effort.webp)
*Concept image of always-on thinking and the effort setting — Source: concept image · self-generated with agy*

The model ID is **claude-opus-5-5**, with no date suffix. Simply pointing Opus 5 code at that name produces 400 errors in the four cases below.

| Item | Opus 5 | Opus 5.5 |
| :--- | :--- | :--- |
| Turning thinking off | Possible at high or below | **400 error** |
| Forced tool_choice | Possible | **400 error** |
| computer_20251124 | Possible | <mark>400 error</mark> |
| Resending thinking blocks | Editing earlier content allowed | 400 error if edited |

[Turning thinking off]
Both **thinking: disabled** and manual **budget_tokens** are rejected. Reasoning is always on, and its depth is controlled only by the effort value (low, medium, high, xhigh, max).

[Forced tool_choice]
**any** and **tool** for **tool_choice** are not accepted. Use **auto** with strict tool use or structured outputs, and state in the prompt when to use tools.

[The older computer use tool]
On the Claude API and Google Cloud, you must switch to **computer_toolset_20260801**. On Amazon Bedrock, the existing **computer_20251124** keeps working.

[Thinking blocks]
For accounts created after August 31, 2026, resending thinking blocks after editing the system prompt, tools, or earlier messages produces a 400 error. Continuing the conversation by appending only is fine.

💻 [Source code: Calling Opus 5.5 (Python)]

    client.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        output_config={"effort": "high"},
        messages=messages,
    )

The progress notes the model used to write between tool calls now come back as thinking blocks rather than text blocks, without error, and at default settings their content is empty. Services that displayed progress on screen have to change the **display** value to **updates** (beta) or **summarized** to see it again. Refusal response categories added bio and reasoning_extraction alongside cyber.

In Claude Code, the **/claude-api migrate** command applies the model ID swap and parameter fixes in one go.

## Safeguards and the pacing argument

![Anthropic logo](/assets/images/ai/claude-opus-55-release/05-logo-anthropic.webp)
*Anthropic logo — Source: Anthropic*

Anthropic commissioned outside evaluations from METR and Frontier Design before release, and said Opus 5.5 posted the best results of any model it has tested in its own automated behavioral audits. On a new evaluation looking at the tendency to cross isolation boundaries, circumvention attempts were about 85% fewer than with Opus 5 and Claude Mythos 5.1, all attempts were low severity, and the model reported them itself.

On the cybersecurity side, safeguards similar to Fable 5.1's apply. Finding and fixing bugs during development still works, but most cybersecurity work is routed to Opus 4.8. Security practitioners must go through the Cyber Verification Program, expanding within weeks, to use Opus 5.5, and biology research access is requested through the Life Sciences Verification Program.

Anthropic also noted in its announcement that Opus 5.5 frequently shows signs of suspecting it is being evaluated, making it hard to judge how it will behave in real environments. TechCrunch reported that the safety training approach does not differ much from earlier models.

## The competitive picture and outside evaluations

![OpenAI logo](/assets/images/ai/claude-opus-55-release/06-logo-openai.webp)
*OpenAI logo — Source: OpenAI*

Within Anthropic's lineup, Opus 5.5 sits below Fable 5.1, yet it scored higher than Fable 5.1 on most published benchmarks. On the competitor side, OpenAI's GPT-6 Astra is the comparison: Opus 5.5 leads on HLE and GDPval-AA, while GPT-6 Astra leads on workflow automation and science terminal tasks.

On the Artificial Analysis Intelligence Index, Opus 5.5 came out at 58, five points above Fable 5.1 (53). On the Vals AI composite index, however, it placed 4th of 60 models at 66.16%, slightly below Opus 5 (67.21%), with lower scores on legal, medical coding, and tax agent tasks, as Digital Applied reported.

## Where it's being used

The cases Anthropic and early adopters published concentrate on long-running coding and analysis work.

- Completed a 680,000-line code migration within a day
- Succeeded in 39 of 40 attempts at cutting load times across every page of a web app
- Audited a 200,000-line codebase in 3 hours, against over 20 hours and 2.5x the tokens for Opus 5
- Ported HAProxy from C to Rust in 9.5 hours, 51% cheaper than Fable 5.1 (12 hours)
- Passed quality bars on 16 of 18 quarterly report research tasks, against 0 for Fable 5.1 and Opus 5
- Finished an M&A financial model in 63 minutes, against 93 minutes with errors for Opus 5

Quantium said a coding task that took 4 days and 38 prompts with Opus 5 came down to 3 hours and 11 prompts. On the legal side, LexisNexis and Thomson Reuters Labs cited improved citation accuracy, which points the other way from Vals AI's legal task results.

In Korea, Anthropic opened a Seoul office on June 17, 2026, and said Naver has adopted Claude Code across its entire engineering organization, with LG CNS and Samsung SDS also using Claude. Organizations already on Claude Code can switch to Opus 5.5 by changing the model setting alone. The announcement materials include no Korean-language performance figures.

![Summary card for deciding whether to switch, by task](/assets/images/ai/claude-opus-55-release/07-items.webp)
*Summary card for deciding whether to switch, by task — Source: self-rendered from Anthropic's and Vals AI's announcements*

## What to watch next

- Sonnet 5.5 and Haiku 5.5: announced by Anthropic for release within weeks, described as carrying the same efficiency gains
- Cyber Verification Program: slated to expand to three verification tiers, with the upper tiers including access to Claude Mythos models

## Sources

- [[Anthropic] Introducing Claude Opus 5.5 (2026-09-22, performance, pricing, safeguards, customer cases)](https://www.anthropic.com/claude-opus-5-5)
- [[Claude Platform Docs] What's new in Claude Opus 5.5 (compatibility changes, features, availability, pricing)](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5)
- [[Claude Platform Docs] Migrating to Claude Opus 5.5 (migration checklist)](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)
- [[TechCrunch] Anthropic releases Opus 5.5 with lower prices and Fable-level performance (2026-09-22)](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/)
- [[Artificial Analysis] Claude Opus 5.5 (Intelligence Index)](https://artificialanalysis.ai/models/releases/claude-opus-5-5)
- [[Digital Applied] Claude Opus 5.5: Pricing, Benchmarks and Breaking Changes (citing Vals AI results)](https://www.digitalapplied.com/blog/claude-opus-5-5-launch-pricing-benchmarks-2026)
- [[AI Times] Anthropic unveils Claude Opus 5.5 (2026-09-23, Korean report)](https://www.aitimes.com/news/articleView.html?idxno=215583)
- [[Korea Economic TV] Anthropic opens Seoul office, Korean companies adopt Claude (2026-06-17)](https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202606170449)
- Exchange rate: converted at $1 ≈ ₩1,400
