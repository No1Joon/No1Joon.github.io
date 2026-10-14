---
title: "Anthropic Cyber Mission — Claude Support for Power and Water Security"
description: "The Anthropic Cyber Mission supporting defenders of infrastructure and open source, and the access tiers of the revamped Cyber Verification Program"
date: 2026-10-13
category: AI
subcategory: News
tags: [anthropic, cybersecurity, critical-infrastructure, open-source, claude]
image: /assets/og/en-2026-10-13-anthropic-cyber-mission.png
---

On October 8, 2026, Anthropic launched the Anthropic Cyber Mission, a long-term program that provides models and people to defenders. The first targets are the control systems that run power grids, water, and transportation, and the open-source code that underpins much software.

Two days earlier, on October 6, it revamped the Cyber Verification Program (CVP), which gives security professionals tiered access to Claude's cyber capabilities. If ARTEX AI, covered in the October 7 post, was an autonomous tool on the attack side, this announcement is an attempt to put the same capabilities in defenders' hands first.

![Anthropic Cyber Mission announcement image](/assets/images/ai/anthropic-cyber-mission/01-hero-cybermission.webp)
*Anthropic Cyber Mission announcement image — Source: Anthropic*

## The two programs announced

![Anthropic logo](/assets/images/ai/anthropic-cyber-mission/02-logo-anthropic.webp)
*Anthropic logo*

The first is the Critical Infrastructure Defense Program (CIDP). Operational technology (OT) such as controllers and industrial networks at power plants and water treatment plants is built to last decades, making it hard to shut down for patching, and known vulnerabilities often linger for years. CIDP provides the latest Claude models, embedded engineers, and Anthropic's threat research to the companies and equipment makers that actually manage security in these settings.

There are 11 founding partners, falling into three types.

- Consulting and technical services: Accenture, Booz Allen, Deloitte, PwC
- Security companies: CrowdStrike, Dragos, Insane Cyber, Nozomi Networks, Palo Alto Networks
- Equipment makers: Hitachi, Rockwell Automation

Anthropic said it will start with a small cohort to first find out what actually works. Its cyber defense program for US state and local governments, launched in June, has reportedly already provided models and technical support to more than half of US states.

The second is OSS Scanner. It periodically scans enrolled open-source projects for free with the model Anthropic describes as its most capable, and delivers reports for each vulnerability that include a proof-of-concept (PoC) exploit, an explanation, and, where possible, a suggested fix. It's an opt-in service modeled on Google's OSS-Fuzz.

## Automated reports without human review

The contentious part of OSS Scanner is that reports are sent to maintainers as the model produced them, without human review. Anthropic said it expects a true positive rate (the share that are real vulnerabilities) of 90% or more, and noted in advance that they may contain errors such as wrong severity ratings.

Only projects with the capacity to review a large volume of reports use OSS Scanner; others continue to get coordinated vulnerability disclosure (CVD), in which people verify findings before reporting them privately, as before. The service reportedly started because during Project Glasswing some maintainers asked to receive all vulnerability information the model found, reviewed or not.

![Bar chart of Project Glasswing vulnerability counts by handling stage](/assets/images/ai/anthropic-cyber-mission/en/03-chart.webp)
*Bar chart of Project Glasswing vulnerability counts by handling stage — Source: self-rendered from figures published by Anthropic*

In Project Glasswing, run since April, the 33 partners and Anthropic found 135,610 real vulnerabilities, 33,669 of them rated high or critical, but only 9,333 were reported as patched. More than half the partners didn't disclose patch counts, so the figure undercounts, but Anthropic also noted that it often took months from finding a vulnerability to fixing it.

[ARTEX AI — The Autonomous Pentest Tool That Left Traces in the Serial Bank Hacks](/en/posts/artex-ai-pentest-tool/)

## The three tiers of the Cyber Verification Program

Publicly available Claude models have conservative safeguards that block most cyber tasks. For defenders to use them with those limits relaxed, they have to go through the CVP, and with the October 6 revamp folding Project Glasswing into the CVP, access is now split into three tiers.

![Table comparing Cyber Verification Program tiers by audience, use, and requirements](/assets/images/ai/anthropic-cyber-mission/04-capture-cvp.webp)
*Table comparing Cyber Verification Program tiers by audience, use, and requirements — Source: Anthropic*

| Tier | For | Review |
| :--- | :--- | :--- |
| Defense Access | Security teams, infrastructure operators, individual researchers | <mark>A few days</mark> |
| Red Team Access | Penetration testing firms, red teams (organizations only) | A few weeks |
| Specialized Access | Organizations testing power grids, interbank payment networks, etc. | **Reviewed with the US government** |

All three tiers can use Claude Opus 5.5, Sonnet 5.5, and Mythos 5.1, and blocking is relaxed as the access tier rises. In exchange, data retention is mandatory for misuse monitoring.

![Claude Opus 5.5 solve rates by tier on CyScenarioBench](/assets/images/ai/anthropic-cyber-mission/05-capture-cyscenariobench.webp)
*Claude Opus 5.5 solve rates by tier on CyScenarioBench — Source: Anthropic*

Anthropic tested blocking by tier with CyScenarioBench, an evaluation of multi-stage attack scenarios. The general model was blocked on the first request on all 10 tasks, and under Defense Access 46 of 50 attempts were blocked partway through. Under Red Team Access, 34 of 50 succeeded without blocking, nearly the same as the 67.6% success rate with all safeguards disabled.

Anthropic said that even under Red Team Access, actions that could hurt people or cause large-scale outages — such as deploying ransomware, damaging physical equipment, or penetration testing high-risk safety systems — are blocked in real time. There's also a condition that attack testing is allowed only against authorized targets.

Testing safety systems that affect lives and markets, such as power grids, flight operations systems, and telecom networks, is possible only at the highest tier, Specialized Access, and existing Project Glasswing participants have been moved to this tier.

## Connection to Korea and how to apply

The announcement doesn't mention any Korean institutions or companies, and no Korean company is among CIDP's founding partners. The programs Korean security teams can apply for right away are the CVP and OSS Scanner. The CVP is available on the Claude Platform, Google Cloud Vertex AI, and Microsoft Foundry, and individual researchers are eligible for Defense Access.

![Summary card of Anthropic Cyber Mission application routes](/assets/images/ai/anthropic-cyber-mission/en/06-items.webp)
*Summary card of Anthropic Cyber Mission application routes — Source: self-rendered from Anthropic's announcement*

Korea's power, water, and transportation control systems are designated and managed as critical information and communications infrastructure under the Act on the Protection of Information and Communications Infrastructure. As a rule these facilities run their control networks separated from the outside, so it's unclear whether bringing in external cloud models and embedded engineers, as CIDP does, is possible as is in Korea. I couldn't find public guidelines on standards for introducing generative AI into such networks either.

Anthropic said it will expand CIDP's partners and areas of application within months and share even the approaches that didn't work. The premise of the announcement is that AI will favor defense two years from now, but for the time being the cost of attacking is falling faster.

## Sources

- [[Anthropic] Introducing the Anthropic Cyber Mission (2026-10-08; source of 1 image in the body)](https://www.anthropic.com/news/anthropic-cyber-mission)
- [[Anthropic] Expanding the Cyber Verification Program (2026-10-06, tiers, evaluation, Glasswing figures; source of 2 images in the body)](https://www.anthropic.com/news/cyber-verification-program)
