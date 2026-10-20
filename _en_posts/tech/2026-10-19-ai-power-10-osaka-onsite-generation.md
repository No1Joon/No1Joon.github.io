---
title: "AI's Electricity (10) — Anthropic's 500MW Osaka Datacenter, On-Site Power Instead of the Grid"
description: "Following NTT DATA's negotiations to build a dedicated Anthropic datacenter in Osaka, this covers generating power on site instead of waiting for a grid connection"
date: 2026-10-19
category: Tech
subcategory: Explainer
tags: [anthropic, ntt-data, data-center, onsite-generation, ai-power]
image: /assets/og/en-2026-10-19-ai-power-10-osaka-onsite-generation.png
---

Up through part 9, we looked at how datacenters get electricity from the grid, nuclear plants, or orbit
This time it's the side that generates power on site instead of waiting for a grid connection

🔗 Link - https://blog.naver.com/rottensweetpotato/224434111541

On October 13, Nikkei reported that NTT DATA will build a **datacenter dedicated to Anthropic** in Osaka
Power intake is up to <mark>500MW</mark>, and the two companies are in final negotiations

The report says that because a grid connection takes a long time, on-site generation and fuel cells are being considered first

![Anthropic and NTT DATA logos](/assets/images/tech/ai-power-10-osaka-onsite-generation/01-hero.webp)
*Anthropic and NTT DATA logos*

## What was reported

Reuters and others carried the Nikkei report, and both companies declined to comment
Everything below is as reported

| Item | Reported details |
| :--- | :--- |
| Location | Osaka, Japan |
| Power intake | **Up to 500MW** |
| Construction cost | Up to ¥1 trillion (about ₩8.8 trillion) |
| Signing target | End of March 2027 |
| Partial operation | As early as 2028 |

The construction cost of about ¥1 trillion (₩8.8 trillion) does not include GPU servers
Nikkei estimated that including servers, the total cost would reach <mark>several trillion yen</mark>

If it goes through, it will be Anthropic's **first dedicated datacenter in Japan**
Nikkei reported that Anthropic is also considering new datacenters in other Asian countries

## How big 500MW is

![Bar chart comparing the power scale of the Google TPU expansion, Osaka, and River Bend](/assets/images/tech/ai-power-10-osaka-onsite-generation/en/02-chart.webp)
*Bar chart comparing the power scale of the Google TPU expansion, Osaka, and River Bend — Source: self-rendered based on Anthropic, Hut 8, and Nikkei reports*

In October 2025, Anthropic said it would expand its Google TPU capacity
It's a scale that brings more than 1GW online in 2026

In December of the same year, Hut 8 disclosed a 245MW lease at River Bend in Louisiana
The tenant is Fluidstack, and the facility is used for Anthropic inference

Osaka's 500MW is about <mark>twice</mark> River Bend

Mordor Intelligence estimated Japan's datacenter power capacity at 3.57GW in 2026
The single Osaka site is 14% of that

## On-site generation instead of the grid

![Concept shot of fuel cell modules lined up next to a datacenter](/assets/images/tech/ai-power-10-osaka-onsite-generation/03-agy.webp)
*Concept shot of fuel cell modules lined up next to a datacenter — Source: concept shot, self-generated with agy*

As we saw in part 1, connecting a large load to the grid means building new transmission lines and substations and waiting years

Nikkei reports that getting 500MW from the grid would take a long time
So it said **on-site generation and fuel cells** are being considered first

Generating power on site like this, behind the grid meter, is called *behind-the-meter*
US datacenters also use on-site generation

### ⚡ Fuel cell deal examples

In November 2024, the US utility AEP signed a deal with Bloom Energy for **up to 1GW** of fuel cells
The first order was 100MW

The solid oxide fuel cells (SOFC) are placed on site to supply power until the grid connection

In October 2025, Bloom Energy also announced a partnership with Brookfield
It commits up to $5 billion (₩7 trillion) to fuel cells for AI datacenters

These fuel cells mainly run on **natural gas**

<mark>They can come online faster than a grid connection, but it means placing fuel-burning generation next to the datacenter</mark>

## How Korea differs

Anthropic opened its Seoul office in June 2026

With Claude, you can choose data residency in Korea through Amazon Bedrock and Vertex AI
But Japan comes first for a dedicated Anthropic datacenter

I covered the grid impact assessment for Korean datacenters of 10MW or more in part 1

The **AI Datacenter Special Act**, passed by the National Assembly in May 2026, is set to take effect in February 2027
Datacenters below a certain size outside the capital region are exempt from this assessment

How far on-site generation can be used while waiting for a grid connection will be set in subordinate regulations

## What to watch next

- Signing: target of <mark>end of March 2027</mark>, not yet officially confirmed by either company
- Power source: whether the on-site fuel is gas, and how large the fuel cells are
- More Asian sites: the other Asian countries Nikkei reported as under consideration
- Korea: special provisions for self-generation and direct power trading in the AI Datacenter Special Act's subordinate regulations

🔗 Link - https://blog.naver.com/rottensweetpotato/224434111541

## Sources

- [[The Star, Reuters] NTT Data in final talks to build Anthropic's first data centre in Japan, Nikkei reports (2026-10-13)](https://www.thestar.com.my/tech/tech-news/2026/10/13/ntt-data-in-final-talks-to-build-anthropic039s-first-data-centre-in-japan-nikkei-reports)
- [[The Next Web] NTT Data reportedly nears deal to build Anthropic's first Japan data centre (total cost including servers, power alternatives)](https://thenextweb.com/news/ntt-data-anthropic-osaka-data-centre)
- [[W.Media] NTT Data in talks with Anthropic (signing target, Japan datacenter power capacity estimate)](https://w.media/?p=44256)
- [[Anthropic] Expanding our use of Google Cloud TPUs (2025-10-23)](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
- [[SEC] Hut 8 Corp. 10-K FY2025 (River Bend 245MW lease)](https://www.sec.gov/Archives/edgar/data/1964789/000110465926019392/hut-20251231x10k.htm)
- [[Utility Dive] AEP and Bloom Energy deal for up to 1GW of fuel cells (2024-11)](https://www.utilitydive.com/news/aep-bloom-energy-fuel-cell-data-center/733150/)
- [[Data Center Dynamics] Bloom Energy's $5 billion partnership with Brookfield (2025-10)](https://www.datacenterdynamics.com/en/news/bloom-energy-signs-5bn-partnership-with-brookfield-to-deploy-fuel-cell-tech-across-ai-data-centers/)
- [[Anthropic] Regional data residency guide](https://claude.com/ko/regional-compliance)
- [[Smart City] AI Datacenter Special Act passes plenary session, takes effect February 2027 (2026-05-08)](https://smartcity.go.kr/2026/05/08/ai데이터센터-규제-확-푼다인허가-절차-대폭-단축/)
- Exchange rate: converted at $1 ≈ ₩1,400 and ¥1 trillion ≈ $6.3 billion (as converted in reports)
