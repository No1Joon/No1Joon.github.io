---
title: "KT's AI for Everyone — Five Korean Models in One Service, Beta in October"
description: "The makeup of the KT consortium's everyday-service AI \"AI for Everyone,\" built with Upstage, Rebellions, and others, and its beta and launch schedule"
date: 2026-10-07
category: AI
subcategory: News
tags: [kt, korean-ai, upstage, rebellions, ai-service]
image: /assets/og/en-2026-10-07-kt-moduui-ai.png
---

On October 7, KT unveiled **"AI for Everyone" (모두의 AI)**, an AI for everyday services, with a closed beta in October and an official launch in December. It combines domestic models from Upstage, Motif, NC AI, and Saltlux with Rebellions' domestic AI chips in a single service.

It is the KT consortium's result for "AI for Everyone," a government project selected by the Ministry of Science and ICT on August 28. KT said it will connect question answering with real service use such as shopping, reservations, and lookups.

![KT logo](/assets/images/ai/kt-moduui-ai/01-hero-kt-logo.webp)
*KT logo*

## Timeline

Out of six consortia that applied to the "AI for Everyone" project, the government made its final selection of SK Telecom, Kakao, and KT on August 28. Selected operators receive 512 NVIDIA B200 GPUs this year, and from 2027 the government budget will support the operating costs of a nationwide service.

- August 18: Ministry of Science and ICT announces six applicant consortia
- August 28: SK Telecom, Kakao, and KT consortia selected
- September: Agreements signed and working groups formed
- October 7: KT unveils AI for Everyone and starts the closed beta
- December: Official service launch planned

## Division of roles among models

![Upstage logo](/assets/images/ai/kt-moduui-ai/02-logo-upstage.webp)
*Upstage logo*

KT uses five domestic AI models separately depending on the task. When a user's question comes in, KT's **Token Factory** technology analyzes its difficulty and nature and routes the request to the appropriate model.

| Participant | Role |
| :--- | :--- |
| Upstage | <mark>Solar model</mark>, general conversation and long-document analysis |
| Motif | Long-context and large-document analysis |
| NC AI | 3D content, voice, and sound generation |
| Saltlux | Participates with a consortium model |
| Daum | Search service integration |
| Rebellions | **Domestic NPU cluster** |

KT team leader Cha Kyung-hoon explained that splitting work across models this way improved cost and compute efficiency by about 16–20%. Published reports don't specify which function Saltlux handles.

## What the service does

KT calls this approach **Ieum Inside**. Instead of opening a separate AI for Everyone app, the strategy is to add an AI button inside services people already use, so they can ask questions and run functions in that service.

| Connected service | Published example |
| :--- | :--- |
| Musinsa | From wedding outfit recommendations to purchase |
| My KT | Checking monthly bill and data usage |
| Genie TV | Finding content without the exact title |
| Danawa | Follow-up questions on a product page |
| Real estate | Listings and prices matching budget and commute |

When the government project was selected, Daum, Musinsa, Zigbang, EBS, and BC Card joined the KT consortium as connected services. The October closed beta will first check the accuracy and stability of informational questions such as weather, stocks, and content, and features that carry out actions such as reservations and applications will expand at the December launch. In the first half of next year, KT plans to link partner accounts so users can access connected services with a single login.

## Domestic NPU infrastructure

![Rebellions logo](/assets/images/ai/kt-moduui-ai/03-logo-rebellions.webp)
*Rebellions logo*

The inference infrastructure is an NPU (neural processing unit) cluster built with Rebellions' domestic AI chips. Alongside the government-supported B200 GPUs, it becomes a case of domestic chips handling real traffic for a nationwide service.

A KT official said the company is fixing problems caused by misunderstanding usage history or context, and is discussing security governance with the Ministry of Science and ICT. Which personal information goes to which participant's model hasn't been disclosed yet.

## The government project landscape

![SK Telecom logo](/assets/images/ai/kt-moduui-ai/04-logo-sktelecom.webp)
*SK Telecom logo*

| Consortium | Service direction in the government announcement |
| :--- | :--- |
| SK Telecom | Action-taking AI |
| Kakao | Messenger-based reservation and payment AI |
| KT | <mark>Integrated AI for public and everyday services</mark> |

KT chose integration into existing services rather than a separate app, while Kakao chose the KakaoTalk conversation flow. All three aim for an official service within the year, so three domestic AI services will launch around the same time in December.

## What to watch next

- How to join the closed beta and when it opens to general users
- The scope of free use at the December launch
- Disclosure of the personal information sent to participants' models and the security standards
- The size of the operating costs supported by the government budget from 2027

## Sources

- [[Ministry of Science and ICT / KDI Economic Information Center] "AI for Everyone" project operator selection results (2026-08-28, selection, GPU support, service direction)](https://eiec.kdi.re.kr/policy/materialView.do?num=285955)
- [[Ministry of Science and ICT / KDI Economic Information Center] "AI for Everyone" project application results (2026-08-18)](https://eiec.kdi.re.kr/policy/materialView.do?num=285504)
- [[Newspim] KT's AI for Everyone connects everyday services through a Korean AI alliance (2026-10-06, participant roles)](https://www.newspim.com/news/view/20261006001362)
- [[Aju Business Daily] AI connects shopping, finance, and real estate; KT unveils AI for Everyone (2026-10-07, integration examples)](https://www.ajunews.com/view/20261007105459174)
- [[EBN / Investing.com] Beyond search to reservations and applications, KT's AI for Everyone launches in December (Token Factory efficiency remarks)](https://kr.investing.com/news/stock-market-news/article-2118536)
- [[Asia Economy] KT's AI for Everyone moves into everyday action, builds security governance (2026-10-07)](https://view.asiae.co.kr/article/2026100711200610775)
- [[Money Today] SKT, Kakao, and KT selected for AI for Everyone (2026-08-28, KT consortium connected services)](https://www.mt.co.kr/tech/2026/08/28/2026082809264168238)
