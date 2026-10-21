---
title: "Anthropic's First Embedded Evaluator Is Accenture — What's Settled and What Isn't"
description: "The terms of the first embedded-evaluator contract, which grants employee-level access, the dispute over its independence, and the operating rules still undecided"
date: 2026-09-25
category: AI
subcategory: News
tags: [anthropic, accenture, embedded-evaluation, ai-safety, ai-governance]
image: /assets/og/en-2026-09-25-anthropic-accenture-embedded-evaluator.png
---

On September 18, 2026, Anthropic named Accenture as its first **embedded evaluator**. The two companies each plan to spend at least $1 billion (₩1.4 trillion) over the next five years building up capability in this area.

Unlike conventional outside evaluation, where a finished model is handed over and tested from outside the company, an embedded evaluator works inside Anthropic with access comparable to an employee's. It is the first organizational implementation of a commitment CEO Dario Amodei put forward on September 12 as step one of pacing the frontier — though the announcement itself says the operating details are still being worked out.

![Lead image from Anthropic's announcement](/assets/images/ai/anthropic-accenture-embedded-evaluator/01-hero-anthropic.webp)
*Lead image from Anthropic's announcement — Source: Anthropic*

[Amodei's Proposal to Pace AI — This Time, Competitors Agreed Too (in Korean)](/posts/amodei-pace-the-frontier/)

## What was announced

![Faculty logo](/assets/images/ai/anthropic-accenture-embedded-evaluator/02-logo-faculty.webp)
*Faculty logo — Source: Faculty*

The evaluation work will be handled by Faculty, Accenture's specialist AI unit. Faculty is a UK AI company that Accenture acquired in January 2026, and it previously built an early-warning system for the UK's National Health Service (NHS) during COVID-19. Faculty CEO Marc Warner doubles as Accenture's chief technology officer.

- Scope of work: model evaluation and red teaming, alignment evaluation, safeguard testing
- Level of access: access comparable to an employee's, observing models during training, interviewing staff directly
- Investment: at least $1 billion (₩1.4 trillion) each from Anthropic and Accenture over five years
- Who pays: Anthropic pays directly for Accenture's evaluation work
- Exclusivity: none — Anthropic will announce further evaluators, and Accenture may do the same work for other AI developers

Anthropic is also in talks to pilot some embedded evaluation with nonprofit evaluators such as METR, where each organization would take part using its own funding. The announcement states that embedded evaluation is not a device for offloading the company's responsibility but a way to make that responsibility verifiable, and that responsibility for model safety remains with Anthropic.

## How it differs from conventional outside evaluation

![METR logo](/assets/images/ai/anthropic-accenture-embedded-evaluator/03-logo-metr.webp)
*METR logo — Source: METR*

| Aspect | Conventional outside evaluation | Embedded evaluation |
| :--- | :--- | :--- |
| Where the work happens | Outside the company | **Inside the company** |
| What is examined | Pre-release models | Models during training too |
| Observing decisions | Not possible | <mark>Tracks development and deployment decisions</mark> |
| Interviewing staff | Limited | Direct interviews |
| Incident reporting | Within contract scope | Can report and explain publicly |

Until now, outside evaluation of frontier models has centered on early access to pre-release models. Representative cases include the UK AI Safety Institute's February 2025 agreement with Anthropic to test unreleased models in advance, and METR's work measuring autonomous task capability on pre-release models. Embedded evaluation differs in observing not the output but the process by which a model is made, and the company decisions that shape that process.

## The essay's commitments and this announcement

![Concept image of an embedded evaluator working inside an AI lab](/assets/images/ai/anthropic-accenture-embedded-evaluator/04-agy.webp)
*Concept image of an embedded evaluator working inside an AI lab — Source: concept image · self-generated with agy*

In his September 12 essay *We Must Pace the Frontier*, Amodei said evaluators would be given office space, badges, and system access comparable to an internal risk assessment team's, with contractual guarantees that they could publish what they find without company editing.

| Item | The essay | September 18 announcement |
| :--- | :--- | :--- |
| First evaluator | Not mentioned | **Accenture (Faculty)** |
| Access level | Employee level | Comparable to an employee's |
| Guaranteed right to publish | Guaranteed by contract | <mark>No rules yet</mark> |
| Reporting method | Incident reporting | No rules yet |
| Funding | Not mentioned | Paid directly by Anthropic |

The announcement acknowledges there are no rules yet on what information evaluators will access or how they will report what they find. Anthropic's position is that in the long run a shared fund or government funding should cover evaluation costs, but it said that since neither exists, funding structures will differ by evaluator. The **unedited right to publish**, the most concrete item in the essay, was not included in the first contract announcement.

## Choosing Accenture and the independence dispute

![Accenture logo](/assets/images/ai/anthropic-accenture-embedded-evaluator/05-logo-accenture.webp)
*Accenture logo — Source: Accenture*

Reactions were mixed over the first evaluator being a consulting firm rather than a nonprofit safety organization such as METR. The two companies already have several business ties. In December 2025 they formed the Accenture Anthropic Business Group, and they agreed to train roughly 30,000 Accenture employees on Claude.

On X, a community note was attached to a post in which Anthropic called Accenture an independent evaluator. It argued that the word "independent" is misleading, given that Anthropic pays for the evaluation and the two companies are already business partners. TechCrunch reported that industry figures who had expected a nonprofit were surprised, and that Accenture's stock rose 8% in after-hours trading following the announcement.

Anthropic cited as reasons for the choice Accenture's experience with actual AI adoption at companies and governments, which it brings to safety evaluation, and that it is a publicly listed company predating the AI era. The announcement does not address whether evaluation results can be published when unfavorable to client companies.

OpenAI has signaled it will take part as well. CEO Sam Altman wrote on X on September 12 that independent evaluators with employee-level access are a good idea and that OpenAI would do it too, but as of September 25 it had not announced an evaluator.

## Compared with AI safety evaluation in Korea

![Models evaluated by the Korea AI Safety Institute vs. frontier models released per month](/assets/images/ai/anthropic-accenture-embedded-evaluator/en/06-chart.webp)
*Models evaluated by the Korea AI Safety Institute vs. frontier models released per month — Source: self-rendered from figures reported by Aju Business Daily*

As of May 2026, a year and a half after its launch, the Korea AI Safety Institute had published 7 reports, but none publicly evaluating an overseas frontier model on its own. It also has no agreements with major AI developers, leaving no route to early access to unreleased models.

| Item | Korea AI Safety Institute |
| :--- | :--- |
| Evaluation GPUs | **16** NVIDIA H200s |
| Time to evaluate one model | 7–10 days |
| Token cost per benchmark run | ₩50–60 million |
| Agreements with overseas developers | <mark>0</mark> |

The number of models evaluated grew from 6 in March to 11 in August, but Aju Business Daily reported that more than 10 frontier models are released each month, making it hard for the institute's equipment to keep pace. The AI Framework Act, which took effect in January 2026, allows operators to conduct impact assessments before deploying high-impact AI, but it has no provision covering outside evaluators stationed inside a developer. Under the current structure, seeing an overseas developer's model before release requires an individual agreement with that developer.

## What to watch next

- The list of additional evaluators Anthropic has signaled, and the scope of the METR pilot
- When Accenture's evaluation team publishes its first report, and whether publication without company editing enters the contract
- Which first embedded evaluator OpenAI picks, and how it is paid for
- Whether talk of a shared fund or government funding takes concrete shape in the US and UK
- Whether the Korea AI Safety Institute signs agreements with overseas developers

## Sources

- [[Anthropic] Partnering with Accenture on embedded evaluation (2026-09-18)](https://www.anthropic.com/news/accenture-embedded-evaluation)
- [[Accenture] Accenture and Anthropic Partner to Build Team of Embedded Evaluators (2026-09-18)](https://newsroom.accenture.com/news/2026/accenture-and-anthropic-partner-to-build-team-of-embedded-evaluators-at-anthropic)
- [[TechCrunch] Anthropic's first embedded evaluator, the Faculty acquisition, and the stock reaction (2026-09-18)](https://techcrunch.com/2026/09/18/anthropics-first-embedded-evaluator-is-accenture/)
- [[TechCrunch] The independence question for embedded evaluators (2026-09-16)](https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/)
- [[OfficeChai] The X community note and the two companies' existing business relationship](https://officechai.com/ai/anthropic-community-noted-on-x-for-calling-accenture-an-independent-evaluator-of-its-ai-despite-their-business-relationship/)
- [[Unite.AI] Altman says OpenAI will match the embedded evaluator pledge](https://www.unite.ai/altman-says-openai-will-match-anthropics-embedded-evaluator-pledge/)
- [[Digital Daily] Korea AI Safety Institute has published no independent frontier model evaluations (2026-05-13)](https://www.ddaily.co.kr/page/view/2026051315321599128)
- [[Aju Business Daily] Korea's AI safety evaluation getting by on 16 H200s (2026-09-16)](https://www.ajunews.com/view/20260916141912494)
- [[Korea Law Information Center] Framework Act on the Development of Artificial Intelligence and Establishment of a Foundation of Trust](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543)
- Exchange rate: converted at $1 ≈ ₩1,400
