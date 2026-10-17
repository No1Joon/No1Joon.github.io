---
title: "GPT-4o and GPT-4.1 API Shut Down January 14, 2027 — What Switching to GPT-6 Luna Costs"
description: "The phased shutdown schedule for major OpenAI API models and the monthly cost difference for the same workload after moving to GPT-6 Luna"
date: 2026-10-15
category: AI
subcategory: News
tags: [openai, gpt-4o, api-deprecation, gpt-6-luna, pricing]
image: /assets/og/en-2026-10-15-gpt-4o-api-shutdown.png
---

On October 14, OpenAI notified developers that API support for GPT-4o, GPT-4o mini, GPT-4.1, and GPT-4.1 mini ends on **January 14, 2027**. If you run a chatbot or internal tool on these models, you need to change the model name within three months. Some models shut down even earlier, on October 23.

The API is the connection other companies use to plug OpenAI models into their own services. Users who only chat in the ChatGPT app or on the web have nothing to change; this schedule applies to those running chatbots, customer service, and internal tools built with ChatGPT models.

![OpenAI logo](/assets/images/ai/gpt-4o-api-shutdown/01-logo-openai.webp)
*OpenAI logo*

## Shutdown schedule

![OpenAI API model shutdown schedule](/assets/images/ai/gpt-4o-api-shutdown/en/02-chart.webp)
*OpenAI API model shutdown schedule — Source: self-rendered from the OpenAI Deprecations page*

The October 14 entry on OpenAI's Deprecations page lists five dated snapshots (model versions frozen at a specific point in time).

| Model | Snapshots being shut down |
| :--- | :--- |
| GPT-4o | **gpt-4o-2024-08-06**, **gpt-4o-2024-11-20** |
| GPT-4o mini | **gpt-4o-mini-2024-07-18** |
| GPT-4.1 | **gpt-4.1-2025-04-14** |
| GPT-4.1 mini | **gpt-4.1-mini-2025-04-14** |

The recommended replacement for all five is <mark>gpt-6-luna</mark>. The page also says that models fine-tuned from these models lose support on the same day as the originals. What happens to undated aliases such as **gpt-4o** isn't stated in this entry.

Requests sent to a model after its shutdown aren't processed. The page explains that at shutdown "the model or endpoint is no longer accessible." This schedule is separate from the models used in the ChatGPT app and applies only to services calling the API directly.

## Models losing support first on October 23

Shutdowns announced on April 22 take effect on October 23. That's three months ahead of January, so if you still use the models below, moving off them is more urgent.

| Model being shut down | Recommended replacement |
| :--- | :--- |
| GPT-4, GPT-4 Turbo | gpt-5.6-sol |
| GPT-3.5 Turbo | gpt-5.6-terra |
| <mark>gpt-4.1-nano</mark> | gpt-5.6-luna |
| gpt-4o-2024-05-13 | gpt-5.6-sol |
| o1, o3-mini | gpt-5.6-sol |
| o4-mini | gpt-5.6-terra |

It's easy to miss that within the GPT-4.1 family, only nano shuts down on October 23 rather than in January. On that date, fine-tuned models based on GPT-3.5 Turbo and GPT-4 and the image model gpt-image-1 also lose support.

## Price comparison

![Monthly cost for the same workload](/assets/images/ai/gpt-4o-api-shutdown/en/03-chart.webp)
*Monthly cost for the same workload — Source: self-rendered from the OpenAI pricing page*

| Model | Input (1M tokens) | Output (1M tokens) |
| :--- | :--- | :--- |
| GPT-4o | $2.50 (₩3,500) | $10 (₩14,000) |
| GPT-4.1 | $2 (₩2,800) | $8 (₩11,200) |
| GPT-4.1 mini | $0.40 (₩560) | $1.60 (₩2,240) |
| GPT-4o mini | $0.15 (₩210) | $0.60 (₩840) |
| GPT-6 Luna | <mark>$0.10 (₩140)</mark> | <mark>$0.50 (₩700)</mark> |

On OpenAI's Standard pricing, GPT-6 Luna costs $0.10 (₩140) for input and $0.50 (₩700) for output, cheaper than all four models shutting down in January. Compared with GPT-4o mini, common in Korean services, input is two-thirds the price and output about 83%.

The gap becomes clear for a service using 100 million input tokens and 20 million output tokens. GPT-4o costs about $450 (₩630,000) a month, GPT-4o mini about $27 (₩37,800), and GPT-6 Luna about $20 (₩28,000). Moving from GPT-4o cuts the bill for the same workload to about 1/22.

This calculation assumes reasoning effort is set to none. Reasoning effort is the setting that decides how much more the model deliberates internally before answering, and the tokens used in that process are billed as output. Added reasoning tokens raise output costs, so check the settings below first.

## What to check when switching

![Settings to check when switching](/assets/images/ai/gpt-4o-api-shutdown/04-agy.webp)
*Settings to check when switching — Source: concept image · self-generated with agy*

### Reasoning effort

GPT-6 Luna's **reasoning_effort** has six levels — none, low, medium, high, xhigh, and max — and defaults to **medium** if unset. If you only swap the model name in place of GPT-4o mini, reasoning tokens are generated and billed as extra output. OpenAI's help article on migrating from GPT-4.x recommends starting at none and comparing against your existing results.

### Function calling

In the Chat Completions API, function calling (the model invoking external functions such as weather lookups or bookings) works only when reasoning effort is none. To use tools while raising reasoning effort, you need to switch to the Responses API.

### Fine-tuned models

The GPT-6 Luna model page doesn't list fine-tuning among supported features, and the fine-tuning endpoint is marked as unsupported. Services that fine-tuned GPT-4o mini or GPT-4.1 mini lose those models on January 14 as well, and can't rebuild them the same way on Luna. Test first whether prompts and examples can take their place.

### Long-input pricing

Requests with more than 272,000 input tokens are billed at 2x input and cache rates and 1.5x output rates for the whole request. The context window is 1.05 million tokens, but services that send long documents in one go need to calculate this tier separately.

## Summary

![GPT-4 family API shutdown summary](/assets/images/ai/gpt-4o-api-shutdown/en/05-items.webp)
*GPT-4 family API shutdown summary — Source: summary of this post · self-rendered*

The January 14, 2027 shutdown covers five dated snapshots and models fine-tuned from them, while older models such as GPT-4, GPT-3.5 Turbo, and gpt-4.1-nano lose support first on October 23. The replacement, GPT-6 Luna, has lower token prices, but to avoid extra charges from reasoning tokens you should set reasoning effort to none and match it against existing results before moving traffic.

## Sources

- [[OpenAI] Deprecations page (2026-10-14 GPT-4 family shutdown notice, October 23 shutdown list from the 2026-04-22 notice, no access after shutdown)](https://developers.openai.com/api/docs/deprecations)
- [[OpenAI] API pricing (Standard pricing for GPT-6 Luna, GPT-4o, GPT-4o mini, GPT-4.1, GPT-4.1 mini)](https://developers.openai.com/api/docs/pricing)
- [[OpenAI] GPT-6 Luna model page (reasoning effort default, function calling conditions, no fine-tuning, pricing above 272K)](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [[OpenAI Help Center] Migrating from GPT-4.x to GPT-6 Luna (recommends starting at reasoning effort none)](https://help.openai.com/en/articles/20001600-migrating-from-gpt-4x-to-gpt-6-luna)
- Exchange rate: converted at $1 ≈ ₩1,400
