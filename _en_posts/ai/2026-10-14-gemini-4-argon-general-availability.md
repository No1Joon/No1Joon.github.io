---
title: "Gemini 4 Argon Generally Available — API Prices Double From December"
description: "Where Gemini 4 Argon is available, the confirmed end date of introductory pricing, and API prices from December"
date: 2026-10-14
category: AI
subcategory: News
tags: [google, gemini-4-argon, llm, pricing, api]
image: /assets/og/en-2026-10-14-gemini-4-argon-general-availability.png
---

Google made Gemini 4 Argon generally available on October 13, 2026. At the September 30 announcement it only said cyber defense organizations would get it first, but two weeks later it began rolling out to Google AI Pro and Ultra subscribers in the Gemini app and to paid API users.

The end date of introductory pricing, not announced at launch, has also been confirmed. API prices are $2 (₩2,800) for input and $10 (₩14,000) for output per million tokens through **November 30, 2026**, and from December 1 input, output, and cache prices all double.

![Google official blog post on Gemini 4 Argon coming to the app](/assets/images/ai/gemini-4-argon-general-availability/01-capture.webp)
*Google official blog post on Gemini 4 Argon coming to the app — Source: Google*

## Where it's generally available

![Official Gemini 4 Argon key art](/assets/images/ai/gemini-4-argon-general-availability/02-photo-keyart.webp)
*Official Gemini 4 Argon key art — Source: Google*

| Channel | Who | Note |
| :--- | :--- | :--- |
| Gemini app | **AI Pro and Ultra subscribers** | Some countries |
| Gemini API | Paid tier | Not on free tier |
| Antigravity, AI Studio | AI Ultra, enterprises | Coding agent |
| Fairwind program | Cyber defense organizations | Since September 30 |

At the September 30 announcement Google said it would come first to the paid API and AI Ultra subscribers, but at actual launch AI Pro subscribers, a tier below Ultra, can also use it in the app. In the US, AI Pro costs $19.99 (₩28,000) a month.

Whether Argon is available in the Gemini app in Korea hasn't been confirmed. The Google One plans page says only that it's "available to Google AI Pro and Ultra subscribers in select countries," without listing the countries.

[Switching to Tasks]
Turn on Tasks with a toggle in the chat box and Gemini keeps working even while you're away (some countries and languages)

[Antigravity coding view]
Switch directly to Google Antigravity's agent coding view inside the macOS Gemini app

[40-plus app integrations]
Connects with outside apps such as Instacart, OpenTable, Adobe, and Shopify

Google explained that Argon answers more directly, doesn't repeat itself, and gives more frequent progress updates on long tasks.

## API prices double from December 1

![Gemini 4 Argon entry in the Gemini API price list](/assets/images/ai/gemini-4-argon-general-availability/03-capture-api.webp)
*Gemini 4 Argon entry in the Gemini API price list — Source: Google*

![Chart comparing Gemini 4 Argon API introductory and December list prices](/assets/images/ai/gemini-4-argon-general-availability/en/04-chart.webp)
*Chart comparing Gemini 4 Argon API introductory and December list prices — Source: self-rendered from the Gemini API price list*

The output price includes thinking tokens, which the model uses for internal reasoning before generating an answer. The harder the problem, the more thinking tokens may exceed the answer itself, so estimating cost from the length of the visible answer alone undercounts the actual bill.

Using 100 million input tokens and 20 million output tokens a month, the bill rises from $400 (₩560,000) to $800 (₩1.12 million).

| Item | Through November 30 | From December 1 |
| :--- | :--- | :--- |
| 100M input tokens | $200 (₩280,000) | $400 (₩560,000) |
| 20M output tokens | $200 (₩280,000) | $400 (₩560,000) |
| Monthly total | $400 (₩560,000) | <mark>$800 (₩1.12 million)</mark> |

Implicit caching applies automatically to prompts over 4,096 tokens, and input that hits the cache is 95% off. For services that repeatedly send the same system prompt or documents, input costs will be much lower than in the example. On the other hand, explicit caching, where you create the cache yourself, isn't supported.

For non-urgent work, Batch and Flex cost half of Standard, and Priority, which guarantees response speed, costs 1.8 times Standard. From December, the Batch price equals today's Standard price.

The GPT-6 Astra and Claude Opus 5.5 prices and benchmarks compared in the September 30 announcement summary are in the post below.

🔗 Link - https://blog.naver.com/rottensweetpotato/224429639264

## Changes for API users

![Concept image of a model producing a very long output at once](/assets/images/ai/gemini-4-argon-general-availability/05-agy.webp)
*Concept image of a model producing a very long output at once — Source: concept image · self-generated with agy*

Argon's input, thinking, and output share a total context limit of 1 million tokens. The output limit for normal requests is 65,536 tokens, and with background execution turned on, a single response can run up to 1 million tokens. In that case the response is sent split across several stages, so you need to join each stage's output.

The thinking level (thinking_level) has three settings — low, medium, and high — with medium as the default. Google recommended testing all three and choosing the lowest that clears your quality bar.

On October 8, support for Gemini 3.7 Flash and 3.5 Flash ended and requests are automatically routed to 3.8 Flash, and the December 2025 preview version of the Deep Research agent ends on October 23.

![Summary card of five things for API users to check](/assets/images/ai/gemini-4-argon-general-availability/en/06-items-api.webp)
*Summary card of five things for API users to check — Source: self-rendered from Google Gemini API documentation*

## What to watch next

- Whether Korea is among the countries where Argon is available in the Gemini app, and Korean-language Tasks support
- The share of users moving to Batch and Flex after the December 1 switch to list prices
- Whether availability widens to the free tier and the AI Plus plan
- Whether OpenAI and Anthropic adjust prices in line with Argon's switch to list prices

## Sources

- [[Google] Gemini 4 Argon comes to the Gemini app (2026-10-13; image source in the body)](https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/)
- [[Google] Gemini 4 Argon: Built to solve your hardest problems (2026-09-30; image source in the body)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)
- [[Google AI for Developers] Gemini Developer API pricing (image source in the body)](https://ai.google.dev/gemini-api/docs/pricing)
- [[Google AI for Developers] What's new in Gemini 4 Argon, model documentation](https://ai.google.dev/gemini-api/docs/latest-model)
- [[Google AI for Developers] Gemini API changelog (2026-10-06 to 13)](https://ai.google.dev/gemini-api/docs/changelog)
- [[Google One] Google AI plans (wording on available countries)](https://one.google.com/intl/ko_kr/about/google-ai-plans/)
- Exchange rate: converted at $1 ≈ ₩1,400
