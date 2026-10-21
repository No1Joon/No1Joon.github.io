---
title: "Meta Muse — A Personal AI Agent That Gets Things Done for You"
description: "The pricing and privacy architecture of Muse, Meta's personal agent that sends email, makes bookings, and even pays, plus its underlying model Muse Spark 1.3"
date: 2026-09-23
category: AI
subcategory: News
tags: [meta, muse, ai-agent, muse-spark, privacy]
image: /assets/og/en-2026-09-23-meta-muse-agent.png
---

Meta unveiled its personal AI agent Muse on September 8, 2026. Rather than a chatbot that answers questions, it is an agent that sends email, books travel, and even gets your bills lowered on your behalf, launching first in the US.

The Muse name has also been used for Muse Spark, a model from Meta Superintelligence Labs (MSL), and Muse Code, the coding tool unveiled on August 5. The agent Muse is the most recent announcement, and a new version of its underlying model, Muse Spark 1.3, came six days earlier on September 2.

![Official Meta Muse introduction image](/assets/images/ai/meta-muse-agent/01-hero-muse.webp)
*Official Meta Muse introduction image — Source: Meta*

## What Muse is

Meta describes Muse as *a secure, private personal AI agent that proactively helps with people's goals* — a personal AI agent that works out what you want and helps with it. The underlying model is Muse Spark, which Meta says is its most capable.

- How you interact: hand off work as if exchanging messages, with the user setting the agent's name, avatar, and tone
- Proactive suggestions: remembers what matters to the user and offers suggestions unprompted
- Long-running work: keeps working after you close the app and notifies you again when circumstances change
- Uses saved content: turning a saved recipe Reel into a shopping list, for example

TechCrunch listed sending email, booking travel, negotiating bills down, filling out forms, planning, and making purchases among the things Muse can do.

## How it works

![Concept image of a dedicated virtual machine for an agent](/assets/images/ai/meta-muse-agent/02-agy.webp)
*Concept image of a dedicated virtual machine for an agent — Source: concept image · self-generated with agy*

Muse runs in a dedicated virtual machine in Meta's cloud called the **Muse Secure VM**. The agent and the user's data live together inside that virtual machine, and the agent opens a built-in browser to fill out forms on websites and negotiate on the user's behalf. The browser screen is visible to the user.

Gmail, calendar, and payment integrations come built in, and for services with no public API, it logs in through the browser using account details the user provides. A record of every action is kept for the user to review.

## How to use it, and pricing

Muse is available on the web at muse.ai, in iOS and Android apps, and in WhatsApp chats, with support for Meta's AI glasses coming soon. The launch region is the US.

| Plan | Monthly price |
| :--- | :--- |
| Free | $0 |
| Power | $20 (₩28,000) |
| Maximum | **$100 (₩140,000)** |

Meta said the free tier is enough for most uses, with paid plans for heavier users. Usage limits per plan are not stated in the published materials.

![Stripe logo](/assets/images/ai/meta-muse-agent/03-logo-stripe.webp)
*Stripe logo — Source: Stripe*

Purchases are handled through Stripe's one-click checkout, Link, and Meta said Shopify's Shop Pay is coming soon as well.

## Privacy and safeguards

Meta said Muse cannot see the user's passwords or payment methods, and that conversations and data are not shared with Meta's advertising systems.

| Safeguard | Details |
| :--- | :--- |
| Connection permissions | User sets per-app connections and access scope |
| Confirmation for sensitive actions | **User confirmation before sending email or purchasing** |
| Action log | A record of every action provided |
| Confidential VM | Planned within 2026 |

A Confidential VM encrypts the entire virtual machine with a key only the user holds, so that not even Meta can see the data and conversations. It was not in place at launch.

TechCrunch noted that Meta settled with the US Federal Trade Commission (FTC) over privacy in 2011 and 2019 and went through the Cambridge Analytica scandal, making the question whether consumers will hand over email and payment permissions.

## The underlying model, Muse Spark 1.3

![Artificial Analysis Intelligence Index comparison](/assets/images/ai/meta-muse-agent/en/04-chart.webp)
*Artificial Analysis Intelligence Index comparison — Source: self-rendered from the Artificial Analysis index*

Meta released Muse Spark 1.3 on September 2, and Mark Zuckerberg said coding ability improved the most. The Artificial Analysis Intelligence Index cited by VentureBeat puts it at 61 on the xhigh setting — the same as Claude Opus 5 and one point below GPT-5.6 Sol (max, 62).

The highest of the scores Meta published came from the max setting, which has not finished safety testing and is available only to select partners. VentureBeat also pointed out that the comparison was against 1.2's xhigh setting, making it hard to read as a pure generational gap.

API pricing is $1.25 (₩1,750) per million input tokens and $4.25 (₩5,950) per million output tokens, the same as 1.2.

## Where this touches Korea

Muse launched in the US only, and Meta has not given a Korean launch date. Users in Korea cannot use muse.ai or the apps.

The Muse Spark 1.3 model is available through the Meta Model API, so developers in Korea can try the model at the listed rates.

Since Stripe Link and Shop Pay, used for payment integration, are not widely used by Korean online shops, the supported payment methods may differ even if it launches in Korea.

## Summary

![Meta Muse summary card](/assets/images/ai/meta-muse-agent/en/05-items.webp)
*Meta Muse summary card — Source: self-rendered from Meta's announcement*

## What to watch next

- Confidential VM: the release of the encrypted virtual machine Meta said it would introduce within 2026
- AI glasses: the AI glasses integration Meta said is coming soon
- Shop Pay: the payment method slated to follow Stripe Link
- The max setting: general availability of Muse Spark 1.3's max setting, still in safety testing

## Sources

- [[Meta] Introducing Muse, the official personal AI agent announcement (2026-09-08)](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
- [[TechCrunch] Muse pricing, integrations, and the trust question (2026-09-08)](https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/)
- [[Axios] Muse's launch and virtual machine architecture (2026-09-08)](https://www.axios.com/2026/09/08/meta-debuts-muse-personal-ai-agent)
- [[VentureBeat] Muse Spark 1.3's performance and the limits of the max setting (2026-09)](https://venturebeat.com/technology/meta-says-muse-spark-1-3-has-frontier-performance-but-its-best-results-come-from-a-model-developers-cant-broadly-use-yet)
- [[CNBC] Muse Code unveiled (2026-08-05)](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html)
- Exchange rate: converted at $1 ≈ ₩1,400
