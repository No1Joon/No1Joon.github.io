---
title: "AI's Electricity (9) — Google Suncatcher Puts Four TPUs in Orbit"
description: "The makeup of Google's Suncatcher prototype satellite, which aims to solve AI chips' power and cooling in orbit, and the cost assumptions in its paper"
date: 2026-10-07
category: Tech
subcategory: Explainer
tags: [google, suncatcher, space-data-center, tpu, ai-power]
image: /assets/og/en-2026-10-07-ai-power-09-suncatcher.png
---

Through Part 8, we looked at ways to supply electricity to AI data centers on the ground. Google has started testing another option: putting AI chips in an orbit where sunlight is almost never interrupted, to see whether power and cooling can be solved in space.

[AI's Electricity (8) — Google Bought Half a Finnish Nuclear Plant's Output for 22 Years (in Korean)](/posts/ai-power-08-loviisa-ppa/)

![Official Project Suncatcher key art](/assets/images/tech/ai-power-09-suncatcher/01-hero.webp)
*Official Project Suncatcher key art — Source: Google*

## Timeline

On October 1, Google announced that the first prototype satellite of Project Suncatcher had reached orbit. Built with satellite imaging company Planet, it launched on a Falcon 9 from Vandenberg Space Force Base as part of SpaceX's rideshare mission Transporter-18. Google said it made contact with the satellite and confirmed it is working normally.

- The satellite is internally called MVP and is the size of a refrigerator
- Carries four Trillium-generation TPUs and about 1kW of solar cells
- Measures for several weeks whether the TPUs withstand launch shock, radiation, and temperature changes
- The underlying research was peer-reviewed and published in the journal Joule

A TPU (tensor processing unit) is a chip Google designs in-house for AI computation. Trillium is the sixth-generation TPU, offered on Google Cloud as TPU v6e.

## The numbers

![Chart of cumulative dose in the Trillium TPU radiation test](/assets/images/tech/ai-power-09-suncatcher/en/02-chart.webp)
*Chart of cumulative dose in the Trillium TPU radiation test — Source: self-rendered from Google's Suncatcher paper*

What affects chips in low Earth orbit is cumulative radiation. Google's research team fired a 67MeV proton beam at Trillium TPUs at UC Davis while running AI workloads.

The high-bandwidth memory (HBM) showed anomalies only at about 2.7 times the expected 5-year dose, and even at the maximum test dose there were no failures that stopped the chip. However, memory errors occurred about once every 50 rad under test conditions, and the paper notes that this is manageable for inference but its impact on training needs more study.

The orbit Google chose is a dawn-dusk sun-synchronous orbit at an altitude of about 650km. In this orbit solar cells receive light almost continuously and produce up to 8 times more power than on the ground.

## The economics

![Suncatcher paper Figure 4, trend in SpaceX launch prices](/assets/images/tech/ai-power-09-suncatcher/03-capture.webp)
*Suncatcher paper Figure 4, trend in SpaceX launch prices — Source: Google*

The value that drives the cost of a space data center is the launch price. The paper's analysis is that each time the cumulative mass SpaceX has launched doubles, the price per kg falls by about 20%. The lowest Falcon Heavy price is still around $1,600 (about ₩2.24 million) per kg.

If this trend continues, the paper calculates that the price of launching to low Earth orbit could fall below $200 (₩280,000) per kg around 2035. That would require Starship to launch about 180 times a year.

![Chart comparing the one-year power cost of 1kW on the ground and in space](/assets/images/tech/ai-power-09-suncatcher/en/04-chart.webp)
*Chart comparing the one-year power cost of 1kW on the ground and in space — Source: self-rendered from Google's Suncatcher paper*

At a launch price of $200 (₩280,000) per kg, the cost of putting 1kW of solar cells in orbit and using it for a year comes to about $810 (₩1.13 million). What a US ground data center pays for 1kW of electricity for a year ranges from $570 to $3,000 (₩0.8–4.2 million) depending on region and power efficiency. The calculation is that the space cost overlaps with the range of ground costs, not that it's cheaper.

## Remaining challenges

### Links between satellites

In ground data centers, chips are connected by fiber-optic cables. In space, satellites must be linked by lasers, and Google recorded 1.6Tbps bidirectional in the lab. Getting that much bandwidth requires the satellites to fly 100–200m apart, and the paper calculated a configuration of 81 satellites gathered within a 1km radius.

### Heat and design

There's no air in space, so heat can be shed only by radiation. The paper names heat rejection and system integration as major engineering challenges, and notes that in the long run a design that integrates many components on a single chip, as in smartphones, may be needed.

### Scale

The Register summarized that meeting the paper's cost targets would require about 1,800 Starship launches and 100-fold reuse of components. The research team also acknowledged that challenges at several stages need to be solved.

## Background and connection to Korea

As we saw in Part 1, US data centers wait years for grid connections, and in Part 8 Google secured existing nuclear power on a 22-year basis. Suncatcher is testing an option that bypasses the grid altogether. Google first revealed the concept in November 2025, saying it would launch prototype satellites with Planet by early 2027, and it launched the first satellite ahead of schedule.

In Korea, Hanwha announced on July 3 that it will invest ₩55 trillion in aerospace and AI through 2040, and Hanwha Systems said it would spend about ₩20 trillion of that on securing space AI data centers along with SAR satellites and a low-orbit communications network. The specific schedule and scale of the space data center haven't been disclosed.

## What to watch next

- Orbital data due within weeks: whether the TPUs show the same results in real space radiation and temperatures as in ground tests
- The next two satellites: when the inter-satellite laser link test Google mentioned will launch
- The number of Starship launches: the value that drives the paper's cost assumptions

[AI's Electricity (8) — Google Bought Half a Finnish Nuclear Plant's Output for 22 Years (in Korean)](/posts/ai-power-08-loviisa-ppa/)

## Sources

- [[Google] Our Project Suncatcher prototype satellite is in orbit (2026-10-01, launch and contact confirmed)](https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-prototype/)
- [[Google Research] Exploring a space-based, scalable AI infrastructure system design (orbit, radiation, 81-satellite configuration; source of 1 image in the body)](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/)
- [[Joule] Toward a future space-based, highly scalable AI infrastructure system design (published paper)](https://www.cell.com/joule/fulltext/S2542-4351(26)00362-4)
- [[Google] Suncatcher paper PDF (launch price and power cost figures; source of 1 image in the body)](https://services.google.com/fh/files/misc/suncatcher_paper.pdf)
- [[The Register] Google launches first datacenter satellite (1,800 Starship launches, remaining challenges)](https://www.theregister.com/systems/2026/10/02/google-launches-first-datacenter-satellite-and-research-that-finds-orbiting-bit-barns-can-work/5300721)
- [[Smithsonian Magazine] Google wants to send data centers to space (four TPUs, refrigerator size)](https://www.smithsonianmag.com/smart-news/google-wants-to-send-data-centers-to-space-and-just-launched-a-satellite-to-test-whether-its-ambitious-plan-will-work-180989613/)
- [[Newsis] Hanwha announces mid- to long-term strategy to become an AI space power (₩55 trillion, Hanwha Systems ₩20 trillion)](https://mobile.newsis.com/view/NISX20260703_0003695284)
- Exchange rate: converted at $1 ≈ ₩1,400
