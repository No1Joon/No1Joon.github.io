---
title: "Leap Seconds to End in 2027 — The Extra Second Behind Server Outages Stops"
description: "The General Conference on Weights and Measures' resolution to abolish leap seconds, why leap seconds existed, and the server outages they caused"
date: 2026-10-18
category: Tech
subcategory: Explainer
tags: [leap-second, utc, timekeeping, ntp, outage]
image: /assets/og/en-2026-10-18-leap-second-abolished-2027.png
---

On October 15, 2026, the world's timekeeping rules changed

The General Conference on Weights and Measures resolved to abolish **leap seconds**

From May 20, 2027, no more seconds will be added to world standard time

It's a rule the IT industry had long been asking to scrap, since leap seconds have caused server outages

![Concept shot of a one-second fragment slipping out between an atomic clock and the rotating Earth](/assets/images/tech/leap-second-abolished-2027/01-agy-hero.webp)
*Concept shot of a one-second fragment slipping out between an atomic clock and the rotating Earth — Source: concept shot · self-generated with agy*

## What was decided

![Bar chart of leap seconds added by decade](/assets/images/tech/leap-second-abolished-2027/en/02-chart.webp)
*Bar chart of leap seconds added by decade — Source: self-rendered based on the IANA tz database*

The decision was made at the **28th General Conference on Weights and Measures (CGPM)** in Versailles, France

It meets every four years to set units such as the meter, kilogram, and second

| Item | Details |
| :--- | :--- |
| Resolution date | October 15, 2026 |
| Effective date | <mark>May 20, 2027</mark> |
| Tolerance | 1 second → up to 3,600 seconds |
| Original target | By 2035 |

The decision allows the gap between UTC (Coordinated Universal Time) and time based on the Earth's rotation to grow **up to 1 hour**

It's expected to take more than 1,000 years for the gap to reach 1 hour

The leap seconds, added 27 times since the first in 1972, will no longer be added

Scientists had debated this issue for 30 years

## How leap seconds work

![Number of leap seconds and the three most recent ones recorded in macOS tz data](/assets/images/tech/leap-second-abolished-2027/en/03-term-leapseconds.webp)
*Number of leap seconds and the three most recent ones recorded in macOS tz data — Source: run on macOS IANA tz data*

World standard time has adjusted for the gap between atomic time and time based on the Earth's rotation

[Atomic time]
The second measured by cesium atomic clocks, steady without wobble

[Astronomical time UT1]
The time the Earth takes to rotate once, which varies a little every year

UTC follows atomic time but has added one second before its gap with UT1 exceeds 0.9 seconds

That second is the **leap second**

On a day a leap second is added, UTC clocks count <mark>23:59:60</mark> once more after 23:59:59

In Korean time, that's <u>8:59:60 a.m.</u> on January 1 or July 1

The last leap second was added on December 31, 2016 UTC, the morning of January 1, 2017 in Korean time

## Outages caused by leap seconds

![Title and cause paragraph of Cloudflare's 2017 leap second outage write-up](/assets/images/tech/leap-second-abolished-2027/04-cloudflare-2017.webp)
*Title and cause paragraph of Cloudflare's 2017 leap second outage write-up — Source: Cloudflare*

Computers calculate time assuming a minute is 60 seconds

When a 61st second is added, it breaks that assumption

[Reddit, June 2012]
An error in Linux high-resolution timer handling froze CPUs, site unreachable for 30–40 minutes

[Cloudflare, January 2017]
Measured response times went negative, causing errors in DNS servers, up to 0.2% of queries failed

The Cloudflare outage began at 00:00 UTC on January 1 and lasted 6 hours and 45 minutes

The cause was a single line of code that assumed a time measurement could never be smaller than the previous one!

That's why large companies have used **leap smear**, which spreads the one leap second over a day

| Company | Smear method |
| :--- | :--- |
| Google | 24-hour linear, about 11.6μs per second |
| Meta | <mark>17 hours</mark>, quadratic function |

In a 2022 engineering blog post, Meta backed the move to stop adding leap seconds

It was an industry proposal to stop at 27

<mark>A leap second has caused errors because it doesn't fit code's assumption that time never goes backward</mark>

## The negative leap second that moved the schedule up

![Title and abstract of Agnew's 2024 Nature paper, with the 2029 negative leap second prediction highlighted](/assets/images/tech/leap-second-abolished-2027/05-nature-agnew.webp)
*Title and abstract of Agnew's 2024 Nature paper, with the 2029 negative leap second prediction highlighted — Source: Nature*

The original abolition target was 2035

The reason it was moved up is the **negative leap second**

When the Earth's rotation speeds up, a second has to be subtracted rather than added

UTC clocks would jump straight from 23:59:58 to midnight of the next day

It has never happened in the 54-year history of leap seconds, so software has never been tested for it!!

**Duncan Carr Agnew** of the Scripps Institution of Oceanography calculated when this would happen

It's a paper published in Nature in March 2024

[Prediction]
Under the current definition, a negative leap second would be needed by 2029

[Cause]
As the rotation of the Earth's liquid core slows, the rest of the Earth spins faster

[Ice]
Melting ice in Greenland and Antarctica slowed the rotation; without it, it would have come three years earlier

The International Bureau of Weights and Measures (BIPM) put the probability of needing a negative leap second by 2035 at about 30%

Nick Stamatakos of the US Naval Observatory also cited avoiding a negative leap second as a major reason

## What changes and what stays the same

Phone and PC clocks and **Korean Standard Time stay the same**

Korea keeps its system of being 9 hours ahead of UTC, and users don't need to change any settings

What changes are <u>places that use precise time synchronization</u>

That includes telecom networks, datacenters, financial trading, and satellite navigation

But the existing 18-second gap between GPS time and UTC stays as it is

The **Korea Research Institute of Standards and Science**, which manages Korean standard time, distributes UTCk, a program that syncs PC clocks to standard time

As of October 18, 2026, I couldn't find any official guidance from the institute on this decision

![Summary card of what changes and what stays the same with the end of leap seconds](/assets/images/tech/leap-second-abolished-2027/en/06-items.webp)
*Summary card of what changes and what stays the same with the end of leap seconds — Source: self-rendered based on reports of the CGPM resolution*

## Sources

- [[Scientific American] CGPM resolution to abolish leap seconds, effective date, tolerance, and officials' remarks (2026-10-15)](https://www.scientificamerican.com/article/scientists-vote-to-end-leap-seconds-redefining-how-the-world-keeps-time/)
- [[ZDNet Korea] The end of leap seconds, why the 2035 target was moved up, and BIPM's probability estimate (2026-10-16)](https://zdnet.co.kr/view/?no=20261016191813)
- [[BIPM] Resolution 4 of the 27th CGPM, the 2035 target and request to redefine the tolerance (2022)](https://www.bipm.org/en/cgpm-2022/resolution-4)
- [[Nature] Agnew, A global timekeeping problem postponed by global warming (2024, source of an image in this post)](https://www.nature.com/articles/s41586-024-07170-0)
- [[Cloudflare Blog] Write-up of the 2017 leap second DNS outage (2017-01-01)](https://blog.cloudflare.com/how-and-why-the-leap-second-affected-cloudflare-dns/)
- [[Engineering at Meta] It's time to leave the leap second in the past (2022-07-25)](https://engineering.fb.com/2022/07/25/production-engineering/its-time-to-leave-the-leap-second-in-the-past/)
- [[Google Public NTP] Leap Smear method (24-hour linear)](https://developers.google.com/time/smear)
