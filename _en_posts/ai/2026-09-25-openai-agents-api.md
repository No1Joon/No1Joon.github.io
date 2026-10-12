---
title: "OpenAI Agents API — A Managed Harness for Entire Multi-Day Runs"
description: "What the Agents API, which turns the Codex harness into an API, handles for you, how it differs from a loop you build yourself, and its pricing and constraints"
date: 2026-09-25
category: AI
subcategory: Explainer
tags: [openai, agents-api, ai-agent, codex, developer-tools]
image: /assets/og/en-2026-09-25-openai-agents-api.png
---

On September 10, 2026, OpenAI began offering the Agents API in public beta. It exposes the harness that runs its own coding tool, Codex, as an API, so rather than calling a model once, you hand off the execution of a task that can run for days.

Building an agent yourself meant implementing everything: summarizing the conversation history when it hits the context limit, managing tool calls, splitting work across multiple agents, and resuming when a run is interrupted. The Agents API runs and manages that bundle of features on OpenAI's side.

![Agents API overview diagram](/assets/images/ai/openai-agents-api/01-hero-agentsapi.webp)
*Agents API overview diagram — Source: OpenAI*

## What the managed harness does

![OpenAI logo](/assets/images/ai/openai-agents-api/02-logo-openai.webp)
*OpenAI logo — Source: OpenAI*

The official documentation lists seven things the managed harness does.

- Runs commands and code in a sandbox
- Applies skills and instructions suited to the situation
- Connects external data through tools or MCP
- Lets you steer an agent mid-task
- Manages the context window by summarizing earlier work
- Splits work and delegates it to subagents
- Resumes interrupted sessions

It comes down to four components: the **agent**, which bundles model, instructions, and tools; the **environment**, which handles files and commands; the **session**, in which work continues; and **events and items**, the inputs and outputs exchanged.

Once created, a session's state is stored on OpenAI's side. You don't need to resend the conversation history with the next task, and deleting the session deletes its outputs too.

## Three execution environments

![Agents API architecture diagram](/assets/images/ai/openai-agents-api/03-photo.webp)
*Agents API architecture diagram — Source: OpenAI*

The **environment.type** value decides where the agent runs commands.

| Setting | Where it runs |
| :--- | :--- |
| **none** | No computer; answers questions and calls tools only |
| **openai_hosted** | <mark>A Linux sandbox provided by OpenAI</mark> |
| **self_hosted** | A runner attached to your own server or container |

The hosted sandbox is a Linux workspace with Python, Node.js, and command-line tools, and the working folder is **/workspace**. You install packages with **packages**, run commands before starting with **setup_commands**, and upload input files with **files**. For networking, **network.access** chooses between allow all, block all, and allow specified hosts only; the specified mode takes 1 to 100 exact host names.

The documentation explicitly says not to put secrets directly in **env**. Code the agent writes can read those values, so it advises using the secrets management feature that stores the actual values separately. Reserved names such as **PATH** and **OPENAI_API_KEY** are rejected outright.

If you choose self_hosted, you provision the compute yourself and connect the runner to the session. A session can outlive its environment, so deciding when to start and stop resources is your responsibility.

## Subagents

Turning on **agent.multi_agent.enabled** makes the harness automatically provide tools for creating subagents, sending them messages, waiting on them, and stopping them. You don't declare these tools yourself.

| Item | Rule |
| :--- | :--- |
| Default concurrency | **6** (excluding the coordinator) |
| Setting | max_concurrent_subagents |
| Inherited | MCP tools, credentials, web search |
| Not available | <mark>Function tools</mark> |
| File system | Shared with the coordinator |

The documentation recommends using them only for independent work. Reviewing several documents separately or investigating an outage cause by cause fits; for short tasks or steps that depend on an earlier step's result, it says the main agent is better off doing the work itself. Agents editing the same files have to coordinate their changes.

## Choosing among three APIs

OpenAI lays out three ways to build agents.

| Option | Where the loop runs |
| :--- | :--- |
| **Agents API** | OpenAI's managed Codex harness |
| Agents SDK | Inside your application |
| Responses API | Your application, with optional hosted orchestration |

The Agents API takes the least integration work and the Responses API the most. Conversely, the Responses API gives the most control and the Agents API the least. State management differs too: the Agents API stores session settings and exchange history on OpenAI's side, while with the Responses API you manage the conversation history yourself.

**Does the work run for days**, and **is it acceptable to store intermediate state with an outside service**? If both are yes, the Agents API; if either is no, one of the other two.

The older Assistants API was shut down on August 26, 2026. The Responses API and Conversations API replaced it, and the Agents API is a separate option that runs on top of them.

## Pricing and constraints

![Price per 20 minutes for OpenAI-hosted containers](/assets/images/ai/openai-agents-api/04-chart.webp)
*Price per 20 minutes for OpenAI-hosted containers — Source: self-rendered from OpenAI's price list*

There is no extra charge for the Agents API itself. Three items are billed by usage.

- Model tokens: the chosen model's API rate as is (GPT-6 Astra is $10 (₩14,000) per million input tokens and $50 (₩70,000) per million output)
- Tool use: web search is $10 (₩14,000) per 1,000 calls, with tokens read through search billed separately
- Hosted containers: $0.03 (₩42) to $1.92 (₩2,688) per 20-minute session depending on memory size

Containers are billed by the minute, with a 5-minute minimum per session. The longer a task runs, the more you should work out the container cost structure before the tokens.

Data residency is **US only**, and zero data retention (ZDR) is not supported. The documentation states that running the sandbox on your own infrastructure does not make it eligible for zero retention either.

On April 20, 2026, Korea's Financial Services Commission amended the enforcement rules of the Electronic Financial Supervisory Regulations to allow SaaS that passes the Financial Security Institute's assessment to be used on internal business networks, and it is also pursuing a full lifting of network separation and a new Digital Financial Security Act. Even with looser regulations, however, session records are still stored in the US and zero retention is still unavailable, so for work involving personal credit information or customer data, a review of overseas data transfer comes first.

## Summary

![Summary of criteria for choosing the Agents API](/assets/images/ai/openai-agents-api/05-items.webp)
*Summary of criteria for choosing the Agents API — Source: summary of this post · self-rendered*

## Sources

- [[OpenAI] Agents API overview docs (components, sessions, managed harness)](https://developers.openai.com/api/docs/guides/agents-api/overview)
- [[OpenAI] Agents API architecture docs (three environments, streaming, webhooks)](https://developers.openai.com/api/docs/guides/agents-api/architecture)
- [[OpenAI] OpenAI-hosted sandbox configuration docs (packages, network.access, env)](https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted)
- [[OpenAI] Multi-agent docs (max_concurrent_subagents default of 6)](https://developers.openai.com/api/docs/guides/agents-api/multi-agent)
- [[OpenAI] Runtime comparison table (Agents API, Agents SDK, Responses API)](https://developers.openai.com/api/docs/guides/agents)
- [[OpenAI] Pricing (model rates, web search, containers)](https://developers.openai.com/api/docs/pricing)
- [[OpenAI] Deprecations (Assistants API shut down 2026-08-26)](https://developers.openai.com/api/docs/deprecations)
- [[Digital Daily] Push for full lifting of network separation in finance (2026-07-15)](https://www.ddaily.co.kr/page/view/2026071517443276094)
- [[ZDNet Korea] Amended enforcement rules of the Electronic Financial Supervisory Regulations take effect (2026-04-20)](https://zdnet.co.kr/view/?no=20260420161504)
- Exchange rate: converted at $1 ≈ ₩1,400
