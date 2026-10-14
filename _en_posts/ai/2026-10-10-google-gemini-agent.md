---
title: "Google Gemini agent — A General-Purpose Work Agent That Also Calls Claude Models"
description: "The features of Gemini agent unveiled at Gemini at Work 2026, how it assigns models, and its agent account structure"
date: 2026-10-10
category: AI
subcategory: News
tags: [google, gemini-agent, ai-agent, enterprise-ai, claude]
image: /assets/og/en-2026-10-10-google-gemini-agent.png
---

On October 8, 2026, at Gemini at Work 2026, Google Cloud unveiled Gemini agent, a general-purpose agent for work. It brings question answering, document work, image and media generation, and code writing and execution into one agent and one API, and for each task it picks the better fit between Gemini and Anthropic's Claude models and assigns the work. It's a private preview, so no general availability date or price has been set.

![Gemini at Work 2026 announcement image](/assets/images/ai/google-gemini-agent/01-hero-gemini-agent.webp)
*Gemini at Work 2026 announcement image — Source: Google*

## What was announced

![Google logo](/assets/images/ai/google-gemini-agent/02-logo-google.webp)
*Google logo*

Google Cloud CEO Thomas Kurian introduced Gemini agent as an agent that returns finished results when you set a goal rather than give instructions. It handles conversation, autonomous work, and code generation in one screen, and can also run tasks on a schedule or in response to specific events.

| Item | Details |
| :--- | :--- |
| Where it's used | Web, mobile, desktop app, CLI |
| Work tools | Google Workspace, Microsoft 365, Slack |
| Connected systems | Jira, Salesforce, BigQuery, and more |
| Extensions | In-house skill registry, MCP servers |
| Availability | **Private preview** |

Tasks run in the cloud, so jobs that take hours or days keep going even if you close your laptop or switch devices. Large tasks are split into parallel and sequential steps by creating several sub-agents on the fly.

## Model routing that can pick Claude

![Anthropic logo](/assets/images/ai/google-gemini-agent/03-logo-anthropic.webp)
*Anthropic logo*

Google said Gemini agent uses both the Gemini family and Anthropic's Claude models, and will add other proprietary and open models in the future. A Smart Routing feature evaluates accuracy and cost for each task to choose the model.

According to Google Cloud release notes, Gemini Enterprise admins can enable Claude Opus 5.5 and Sonnet 5.5 from October 8. No separate Anthropic account is needed — you just accept the terms in the console — but third-party models are disabled by default, and usage is billed pay-as-you-go through Cloud Billing. They're available in the global, us, and eu locations, not in country-specific regional offerings.

Google let its own agent choose a competitor's model, and companies can use both companies' models under a single contract.

## Coworker agents with company accounts

![Concept image of an agent coworker working beside human teammates](/assets/images/ai/google-gemini-agent/04-agy.webp)
*Concept image of an agent coworker working beside human teammates — Source: concept image · self-generated with agy*

Used as a personal assistant, it knows your calendar, team, and project context, so it can handle requests like "reschedule that meeting from last time" without names or email addresses.

A coworker agent, used as a teammate, is created just by describing its role, and gets a Google Workspace account in its own name. It has an agent email address on the company domain, a calendar, and Drive, and is listed in the directory; you can add it to a Google Chat space or assign it work with an @mention, and when it suggests edits in document comments, the version history records them under that agent's name. Its permissions follow only sharing and membership scopes, not the permissions of the person who assigned the task.

Memory is split into four kinds: the context of the current task (session), knowledge accumulated from documents and people (semantic), how to do the work and skills the agent wrote itself (procedural), and the history of past tasks (episodic).

## Security and cost controls

Google said it gives each agent a unique, cryptographically verifiable identity and least privilege, and records every action in audit logs under that agent's name rather than a person's. Agents run in network-isolated sandboxes, and all traffic passes through an Agent Gateway that enforces policies in real time.

Costs are capped with real-time per-project spending limits in the Cloud Billing console. When the limit is reached, agent execution pauses, and it can be re-enabled from the console.

## Customer examples presented

![Chart of task times in customer examples presented by Google Cloud](/assets/images/ai/google-gemini-agent/en/05-chart.webp)
*Chart of task times in customer examples presented by Google Cloud — Source: self-rendered from the Google Cloud blog*

The examples Google gave in the same post are results of adopting Gemini Enterprise overall, not achievements of Gemini agent alone.

Brazilian bank Bradesco was presented as cutting document review time from 1 hour to 5 minutes, and Snap as cutting diagnostic troubleshooting from 30 minutes to 30 seconds. Japan's NTT DOCOMO saved 450,000 hours a year, and at SOMPO, 34,000 employees reportedly built more than 10,000 agents. All are Google's figures, and the measurement criteria weren't disclosed.

## Gemini Code Assist sales end

Around the same time, Google Cloud stopped selling new Gemini Code Assist Standard and Enterprise subscriptions from October 9. Existing subscriptions auto-renew through 2026 and renewals end in 2027; instead, Google is pointing customers to the Antigravity development tool included in Gemini Enterprise subscriptions. Development teams in Korea using Code Assist need to decide which tool to move to before their 2027 renewal.

![Pre-adoption checklist card](/assets/images/ai/google-gemini-agent/en/06-items.webp)
*Pre-adoption checklist card — Source: self-rendered from the Google Cloud blog and release notes*

9to5Google reported that Gemini agent will expand availability starting with Google Workspace customers on some Business and Enterprise plans.

If OpenAI dots, unveiled on October 2, is an agent that works 24 hours a day on its own cloud computer, Gemini agent is designed to be managed within a company's accounts, permissions, and audit framework.

## Sources

- [[Google Cloud Blog] Welcome to Gemini at Work 2026: features, memory, security, customer examples (2026-10-09)](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026)
- [[Google Blog] Gemini agent announcement summary (2026-10-08)](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-at-work/)
- [[Google Cloud] Release notes: enabling Claude Opus 5.5 and Sonnet 5.5, end of Code Assist sales (2026-10-08 to 09)](https://docs.cloud.google.com/release-notes)
- [[9to5Google] Private preview, eligibility, invoking @Gemini (2026-10-08)](https://9to5google.com/2026/10/08/gemini-agent-google-cloud/)
