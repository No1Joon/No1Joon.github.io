---
title: "GPT-6 Sol and Luna Released — Half the API Price, and How to Choose Between the Two"
description: "How Sol and Luna, the tiers below GPT-6 Astra, divide the work, what they cost, and how the pricing compares with Claude Opus 5.5"
date: 2026-09-23
category: AI
subcategory: News
tags: [openai, gpt-6-sol, gpt-6-luna, llm-pricing, model-release]
image: /assets/og/en-2026-09-23-gpt-6-sol-luna-release.png
---

OpenAI unveiled GPT-6 Sol and GPT-6 Luna on September 22, 2026. The two models sit below GPT-6 Astra, released earlier in September: Sol takes on complex work such as coding, while Luna handles high-volume work with a clear goal.

API pricing came down 50% from GPT-5.6's discounted rates. GPT-6 Sol's output price of $10 (₩14,000) per million tokens is half that of Anthropic's Claude Opus 5.5, which launched 90 minutes earlier the same day.

![Official key visual for the GPT-6 Sol and Luna announcement](/assets/images/ai/gpt-6-sol-luna-release/01-hero-gpt6-sol-luna.webp)
*Official key visual for the GPT-6 Sol and Luna announcement — Source: OpenAI*

## The gist of the announcement

OpenAI explained that it trained both models in much the same way as GPT-6 Astra, bringing Astra's gains in task handling, factual accuracy, coding, computer use, and alignment to faster and cheaper models. It said the price cut follows from lower serving costs achieved by improving caching and inference efficiency.

- Pricing: Sol $2 input and $10 output; Luna $0.10 input and $0.50 output (per million tokens)
- Factual accuracy: in an internal evaluation built from conversations where users reported errors, Sol's errors were about half those of GPT-5.6 Sol
- Coding: Sol scored 68.8% on DeepSWE v1.1, 1.1 percentage points from Claude Fable 5's best (69.9%)
- Availability: ChatGPT Work and Codex (Plus, Pro, Business, Enterprise, Edu), the API, and GitHub Copilot
- Free use: Free and Go users can use only Luna, in the desktop app
- Most capable model: still GPT-6 Astra

## How Sol and Luna differ

![Concept image of how Sol and Luna divide the work](/assets/images/ai/gpt-6-sol-luna-release/02-agy-sol-luna.webp)
*Concept image of how Sol and Luna divide the work — Source: concept image · self-generated with agy*

OpenAI recommends Sol for complex work such as coding, and Luna for high-volume work with a clear goal, such as summarizing documents, extracting information, and short questions. Both take text and images as input and output text, with six reasoning effort levels — none, low, medium, high, xhigh, max — defaulting to medium.

| Item | GPT-6 Sol | GPT-6 Luna |
| :--- | :--- | :--- |
| Recommended for | Coding, complex work | Summarizing, extraction, short questions |
| Input (per million tokens) | $2 (₩2,800) | **$0.10 (₩140)** |
| Cached input (per million tokens) | $0.20 (₩280) | $0.01 (₩14) |
| Output (per million tokens) | $10 (₩14,000) | <mark>$0.50 (₩700)</mark> |
| Context window | 1.05M tokens | 1.05M tokens |
| Training data cutoff | 2026-04-20 | 2026-05-18 |
| Free and Go plans | Not available | Desktop app |

The context window (how much input it takes at once) is 1.05 million tokens for both, with max output of 128,000 tokens. Of that, Luna accepts up to 922,000 input tokens. Luna's training data cutoff is about a month later.

According to OpenAI, at high reasoning effort Luna matches GPT-5.6 Sol on factual accuracy at about one hundredth the cost, and on DeepSWE it scored 66.6% at the max setting, comparable to Claude Opus 5 and Fable 5 at medium.

## Pricing

![Output price per million tokens by model](/assets/images/ai/gpt-6-sol-luna-release/en/03-chart.webp)
*Output price per million tokens by model — Source: self-rendered from OpenAI's and Anthropic's price lists*

By output price, GPT-6 Astra is 5 times Sol, and Sol is 20 times Luna. Sol's input and output prices ($2 and $10) are exactly half those of Claude Opus 5.5 ($4 and $20), released the same day.

- Cached input: 10% of base input — $0.20 (₩280) for Sol, $0.01 (₩14) for Luna
- Luna cache writes: $0.125 (₩175) per million tokens
- Batch and Flex: 50% of standard rates
- Fast mode: 2x the applicable rate

The cuts are measured against GPT-5.6's discounted prices, not its list prices. GPT-5.6 Sol came down from $4 (₩5,600) input and $20 (₩28,000) output, and GPT-5.6 Luna from $0.20 (₩280) input and $1.20 (₩1,680) output.

OpenAI raised GPT-6's baseline cache hit rate and made earlier caches survive changes to reasoning effort or turning tools on and off mid-conversation. Explicit breakpoints, which let developers decide where a cached span ends, arrived alongside a caching dashboard and diagnostic tools. GitHub said these improvements cut the share of prompt tokens needing fresh processing by more than 50%.

API usage is billed in dollars, so the cost in won for users in Korea depends on the exchange rate.

## Benchmark figures

![AutomationBench cost-per-task multiples](/assets/images/ai/gpt-6-sol-luna-release/en/04-chart.webp)
*AutomationBench cost-per-task multiples — Source: self-rendered from figures in OpenAI's announcement*

AutomationBench is a workflow benchmark covering sales, marketing, operations, customer support, finance, and HR work across 47 tools. GPT-6 Sol at xhigh scored 33.2% at $0.27 (₩378) per task.

| Model (setting) | Score (%) |
| :--- | :--- |
| GPT-6 Sol (xhigh) | <mark>33.2</mark> |
| Claude Fable 5.1 (max) | 31.4 |
| GPT-6 Astra (low) | 30.3 |
| Claude Opus 5 (max) | 26.9 |

Sol beat Astra at low for one 3.9th of the cost, and beat Claude Opus 5 at max for about 9% of the cost. About 40% of Fable 5.1's tasks were routed to Opus 5 and that cost is excluded, so the real cost multiple is larger than 8.9x.

![Best DeepSWE v1.1 scores compared](/assets/images/ai/gpt-6-sol-luna-release/en/05-chart-deepswe.webp)
*Best DeepSWE v1.1 scores compared — Source: self-rendered from figures in OpenAI's announcement*

On DeepSWE v1.1, which solves long software tasks in real codebases, Sol at max scored 68.8%, 1.1 percentage points from Claude Fable 5 at xhigh (69.9%). Cost per task was about 80% lower.

- Agents' Last Exam: Sol (max) 56.4%, above Claude Opus 5's best at 60% lower cost per task
- FrontierCode 1.1: Sol on par with Claude Fable 5.1 at xhigh, at far lower cost
- OSWorld 2.0 offline: Sol (xhigh) 60.5%, comparable to Claude Opus 5 at medium (60.3%) at about 80% lower cost
- AutomationBench: Luna (high) 5.4 percentage points above GPT-5.6 Luna at 58% lower cost per task

## Using them in Codex

![OpenAI logo](/assets/images/ai/gpt-6-sol-luna-release/06-logo-openai.webp)
*OpenAI logo — Source: OpenAI*

Codex supports both models from CLI 0.156.0, released September 22, 2026. In the app you pick them from the model menu; in the CLI you specify the model at launch or switch with **/model** within a session.

💻 [Source code: Specifying the model in Codex CLI]

    codex --model gpt-6-sol
    codex --model gpt-6-luna

The API model IDs are **gpt-6-sol** and **gpt-6-luna**, and they support the Chat Completions and Responses endpoints along with tools such as web_search, file_search, code_interpreter, computer_use, and mcp.

In GitHub Copilot, Sol is included in the Pro+, Max, Business, and Enterprise plans and Luna in plans down to Pro, selectable in VS Code, JetBrains, Xcode, Copilot CLI, and elsewhere.

On the ChatGPT side, Plus subscribers in Korea get the same terms and can use them right away in ChatGPT Work and Codex; they are not yet available in the regular conversation screen (Chat).

OpenAI said it also brought GPT-6 Astra's conversational style to both models. They use less jargon and fewer side explanations, state more clearly what they did and did not verify, and give somewhat shorter answers overall.

## Limits of the comparison

![Anthropic logo](/assets/images/ai/gpt-6-sol-luna-release/07-logo-anthropic.webp)
*Anthropic logo — Source: Anthropic*

The Anthropic models OpenAI compared against are Claude Opus 5 and Fable 5.1 (Fable 5 where no figure exists); Opus 5.5, released 90 minutes earlier, is not included. A footnote says competitors' figures were taken from public reports.

Comparing the two companies' own announced figures directly, Anthropic's stated AutomationBench score for Opus 5.5 is 40.0% against OpenAI's 33.2% for GPT-6 Sol (xhigh). The measuring party and settings differ, so they can't be compared at face value — and Sol costs half as much.

OpenAI stated that its factual accuracy evaluation is built from conversations where users reported errors in earlier models and does not represent typical use. It also wrote that the alignment evaluations deliberately construct difficult situations and do not measure failure rates in everyday use.

## How to choose

![Summary card of what each model is for](/assets/images/ai/gpt-6-sol-luna-release/en/08-items.webp)
*Summary card of what each model is for — Source: self-rendered from OpenAI's announcement*

## What to watch next

- When they reach ChatGPT's regular conversation screen (Chat)
- Competing models: Anthropic's Sonnet 5.5 and Haiku 5.5, announced for release within weeks

## Sources

- [[OpenAI] Introducing GPT-6 Sol and Luna (2026-09-22, pricing, benchmarks, availability)](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- [[OpenAI API Docs] GPT-6 Sol (context, pricing, reasoning effort, tools)](https://developers.openai.com/api/docs/models/gpt-6-sol)
- [[OpenAI API Docs] GPT-6 Luna (context, pricing, cache writes)](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [[OpenAI Codex] Changelog (2026-09-22, CLI 0.156.0, model selection)](https://learn.chatgpt.com/docs/changelog)
- [[GitHub Changelog] OpenAI's GPT-6 Sol and GPT-6 Luna now available (2026-09-22, Copilot plans)](https://github.blog/changelog/2026-09-22-openais-gpt-6-sol-and-gpt-6-luna-now-available/)
- [[TechCrunch] OpenAI launches GPT-6 Sol and Luna (2026-09-22, launch timing and uses)](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)
- [[Anthropic] Introducing Claude Opus 5.5 (2026-09-22, Opus 5.5 pricing and AutomationBench score)](https://www.anthropic.com/claude-opus-5-5)
- Exchange rate: converted at $1 ≈ ₩1,400
