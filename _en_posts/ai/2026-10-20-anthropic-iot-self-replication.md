---
title: "Anthropic's AI Self-Replication Experiment — Running a Model on 15 TV Boxes"
description: "Anthropic's Frontier Red Team research that spread an open model across 15 cheap Android TV boxes to evaluate whether AI could self-replicate without a datacenter"
date: 2026-10-20
category: AI
subcategory: News
tags: [anthropic, self-replication, ai-safety, red-team, iot]
image: /assets/og/en-2026-10-20-anthropic-iot-self-replication.png
---

On October 12, 2026, Anthropic's Frontier Red Team published research on self-replicating AI

It spread a single open model across 15 Android TV boxes!
Each box costs about $55 (₩77,000)

It was an experiment evaluating whether AI can copy itself to other devices without a datacenter

![Flowchart of the four stages of self-replication](/assets/images/ai/anthropic-iot-self-replication/01-hero.webp)
*Flowchart of the four stages of self-replication — Source: Anthropic*

## Research overview

![Anthropic logo](/assets/images/ai/anthropic-iot-self-replication/02-logo-anthropic.webp)
*Anthropic logo*

It tested whether a small **open-weight model** could spread itself to cheap IoT devices
An open-weight model is one whose weights are released so anyone can download and run it

The team divided replication into four stages

[Network discovery]
Finding devices to infect

[Intrusion and payload delivery]
Breaking into a device and transferring the model files

[Inference setup]
Building a server on that device to run model inference

[Replication]
Trying to replicate again from the replicated device to other devices

The research focused on <mark>the third stage, inference setup</mark>
It said the first two stages are hacking techniques, so it deliberately kept them simple

## Experimental figures

![Bars showing the range of inference setup time by model](/assets/images/ai/anthropic-iot-self-replication/en/03-chart.webp)
*Bars showing the range of inference setup time by model — Source: self-rendered based on Anthropic data*

### 📺 Demo on 15 TV boxes

Google's **Gemma4-26B-A4B** was split and deployed across 15 TV boxes
Each has 4GB of RAM and is a cheap unbranded product

It uses **pipeline parallelism**, in which several devices share the model's layer-by-layer computation
The speed was <mark>0.39 tokens per second</mark>

### 🧰 Inference setup success rate

The 9B model got an inference server running on <mark>8 of the 9</mark> hardware types tested
The targets included NVIDIA Jetson Nano, Orange Pi, Mac, and RTX 4090

One setup takes 28–51 hours for Qwen3.5-9B
For Gemma4-26B-A4B, it was estimated at 71–150 hours

### 🔁 The model that replicated all the way

The full replication process was tested in an environment of eight Android 15 emulators
The only open model that succeeded all the way was **GLM-5.2**

In 4 of 5 runs it replicated to <mark>all 8</mark>, and in the remaining run to 7
The other open models tested failed every time

Results changed when inference setup was handled by a script
Even a 3B model spread to nearly half of a 17-device network

### 🧬 Inference setup success rate by replication generation

Success rates rose when parent replicas passed code and notes to the next generation of replicas
Qwen3.5-9B's inference setup success rate went from 45% in the first generation to <mark>61–84%</mark> afterward

Having it take advice from the stronger Claude Opus 4.8 didn't raise success rates much

## Preconditions and remaining gaps

![Camera admin screen found by a device search engine, with identifying details masked](/assets/images/ai/anthropic-iot-self-replication/04-photo.webp)
*Camera admin screen found by a device search engine, with identifying details masked — Source: Anthropic*

Device search engines turn up camera admin screens exposed to the internet
The team judged that the first stage of finding infection targets is already not hard

But this intrusion experiment was run with outside access allowed to <mark>an unauthenticated ADB port</mark>
**ADB** (Android Debug Bridge) is the channel developers use to control Android devices remotely

The team itself said the results should be read as <u>an upper bound on real-world success rates</u>
No experiment infected an actual TV box!

| Stage | Experimental condition | Verdict |
| :--- | :--- | :--- |
| Finding devices | 8 targets specified in advance | [Unverified] |
| Intrusion | Unauthenticated ADB port | [Unverified] |
| Inference setup | 8 of 9 hardware types | **Verified** |
| Replication | GLM-5.2, 4 of 5 runs | **Verified** |
| Infecting real devices | Not tested | [Unverified] |

## The scale seen through the Kimwolf botnet

![Horizontal bars estimating the scale of Kimwolf](/assets/images/ai/anthropic-iot-self-replication/en/05-chart.webp)
*Horizontal bars estimating the scale of Kimwolf — Source: self-rendered based on Anthropic data*

The team calculated using the scale of a real botnet, **Kimwolf**, as a baseline
Kimwolf is a botnet that mainly infected cheap Android TV boxes and set-top boxes

![Android logo](/assets/images/ai/anthropic-iot-self-replication/06-logo-android.webp)
*Android logo*

It is known to have infected <mark>more than 2 million</mark> devices at its peak
Assuming one replica consists of 15 devices, that gives about 133,000

Even so, the combined compute is about the level of **40 H100s**
The team pointed to <mark>the difficulty of stopping every replica without a central server</mark> as the risk, rather than compute

It judged spread to be slow, taking several days for the number of replicas to double

### 📈 The end of 2026 as a milestone

The capability index (ECI) of open models at 30B or below rose 13.7 points a year
On this trend, the calculation is that small models will reach GLM-5.2's level by the end of 2026

The team also said ECI is a rough metric that only indirectly gauges replication capability

## Points of contact in Korea

![KISA logo](/assets/images/ai/anthropic-iot-self-replication/07-logo-kisa.webp)
*KISA logo*

Boan News reported that Kimwolf-infected devices were found in Brazil, India, the US, and elsewhere
Korea was not named among the countries where infections were concentrated

Cheap TV boxes of the same kind are easy to buy from overseas direct-purchase shopping sites
Model names such as **X96Q** have been reported as infected devices

Korea's KISA **IoT security certification** criteria include a ban on shared common passwords
As of April 2026, there are <mark>249</mark> certified products

Certification is not mandatory; manufacturers apply for it
The same report said only 2 home cameras were certified!!

## What you can do now

### 🏠 Users

![Summary card of steps for users](/assets/images/ai/anthropic-iot-self-replication/en/08-items.webp)
*Summary card of steps for users — Source: self-rendered summary card of this post*

🔗 Link - https://www.boho.or.kr

### 🏭 Manufacturers and carriers

The team said the goal is to bring the number of new infections caused by one infected device below 1
Since devices exchange several GB with each other, it judged that carriers monitoring traffic flows could detect it

When carriers isolated and notified infected subscribers, <mark>92%</mark> of Mirai infections were resolved within 14 days
Without notification, it was 74%

The UK has made IoT devices with default passwords a regulatory violation
The team called on manufacturers to <u>strengthen default security settings when devices ship</u>

## What to watch next

- Whether small open models reach GLM-5.2's level by the end of 2026
- A follow-up experiment that includes the intrusion stage the team left out
- Whether calls to make **IoT security certification** mandatory turn into regulation

## Sources

- [[Anthropic] AI models may be capable of self-replicating without access to a datacenter (original research, 2026-10-12)](https://www.anthropic.com/research/self-replicating-ai)
- [[Boan News] Kimwolf takes over 1.8 million Android TVs and abuses them for DDoS attacks (2025-12-21)](https://www.boannews.com/news/articleView.html?idxno=141082)
- [[The Hacker News] Kimwolf Android botnet infects over 2 million devices (2026-01)](https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html)
- [[MTN] Standards exist but don't work: the home camera security gap (249 IoT security certifications, 2026-04-24)](https://news.mtn.co.kr/news-detail/2026042416401853507)
- [[CE Pro] BADBOX 2.0, a botnet targeting cheap Android TV devices (reports of factory-level backdoors)](https://www.cepro.com/news/badbox-2-botnet-targetting-android-tv-devices-projectors/147345)
- Exchange rate: converted at $1 ≈ ₩1,400
