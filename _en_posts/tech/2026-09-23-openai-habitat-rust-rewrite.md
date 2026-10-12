---
title: "ChatGPT's Storage Layer From Python to Rust — 6x CPU and 15x Memory Efficiency"
description: "How OpenAI rewrote its storage layer Habitat in Rust, and why Python hit its limit in coordination between requests rather than in throughput"
date: 2026-09-23
category: Tech
subcategory: Explainer
tags: [rust, python, openai, backend, performance]
image: /assets/og/en-2026-09-23-openai-habitat-rust-rewrite.png
---

In September 2026, OpenAI published how it rewrote Habitat, the storage platform handling ChatGPT user data, from Python to Rust. It said the new Rust service handles 95% of production requests, with 6 times the CPU efficiency and 15 times the memory efficiency of the Python version.

The interesting part is that Python hit its limit not because of throughput but because of coordination problems between requests. Part 1 of the Habitat series on OpenAI's engineering blog also covers how the team judged when to switch languages in a large-scale service.

![OpenAI logo](/assets/images/tech/openai-habitat-rust-rewrite/01-logo-openai.webp)
*OpenAI logo — Source: OpenAI*

## What Habitat does

Habitat is a layer that sits between ChatGPT products and the actual storage (Azure Cosmos DB, caches, blob storage). Requests that read user settings or fetch conversation history pass through it, and it handles routing, permission checks, encryption, caching, data residency (storing data within a specific country), and rate limiting.

![Habitat requests per second](/assets/images/tech/openai-habitat-rust-rewrite/02-chart.webp)
*Habitat requests per second — Source: self-rendered from figures in OpenAI Engineering's announcement*

- Scale: more than 500PB (petabytes), about 40 regions
- Throughput: more than 70 million requests per second
- Growth: more than 10x per year for three straight years
- Peak in the Python era: more than 20 million per second

## Four places Python got stuck

![Concept image of an event loop bottleneck](/assets/images/tech/openai-habitat-rust-rewrite/03-agy.webp)
*Concept image of an event loop bottleneck — Source: concept image · self-generated with agy*

Every failure OpenAI cited came not from a shortage of CPU or servers, but from tasks competing for execution time inside a single event loop (the repeating structure that processes asynchronous work in turn).

| Problem | Cause | Symptom |
| :--- | :--- | :--- |
| Scheduling delay | Background work such as parsing settings JSON | Processing delayed after the response arrived |
| Synchronized polling | Feature flag lookups every 60 seconds, no jitter | **8 processes stalling at once** |
| LIFO connection pool | Reusing the most recently returned connection first | Requests piling onto slow servers |
| Connection multiplication | A separate connection pool per process | 18 connections for 6 concurrent requests |

### Scheduling delay

Even when the backend's response had already arrived, the event loop couldn't pick it up and process it while running background work. OpenAI wrote that this was hard to diagnose because dashboards showed the backend responding quickly.

### Synchronized polling

The feature flag SDK refetched settings every 60 seconds, and the 8 processes on a single pod moved at the same instant with no random offset (jitter). At each of those instants, latency spiked across all processes together.

### LIFO connection pool

aiohttp's connection pool reuses the most recently returned connection first. The slower a server is, the later it returns its connection and so the sooner it receives the next request, creating a vicious cycle that concentrated requests on already loaded pods.

### Connection multiplication

Because Python keeps a separate connection pool per process, handling 6 concurrent requests grew to as many as 18 connections.

## The rewrite and its results

![Resource efficiency after the Rust rewrite](/assets/images/tech/openai-habitat-rust-rewrite/04-chart.webp)
*Resource efficiency after the Rust rewrite — Source: self-rendered from figures in OpenAI Engineering's announcement*

OpenAI said it deliberately stayed on Python for a while, even knowing that Python's inefficiency would be unacceptable at 100x scale and that a rewrite would eventually be necessary. It explained that it took on the technical debt strategically, expecting the cost of a rewrite to fall as its in-house coding models improved.

In the second quarter of 2026, two engineers rewrote the entire service in Rust using Codex and GPT-5.5. OpenAI said the Rust version handles 95% of production requests, with 6x CPU and 15x memory efficiency and substantially lower average and tail latency (the response time of the slowest subset of requests).

Part 1 gives no concrete latency figures or details of how the rewrite was validated (parallel operation, output comparison, and so on). All figures come from OpenAI itself, and explainx argued that the "two engineers" framing carries a promotional flavor and should be read separately from the technical lessons.

## When to switch languages

Three criteria can be read out of the Habitat case.

[Is the scale growing 10x at a time]
Growing 10x a year means today's architecture has to handle 100x the load within two or three years. That growth rate is why OpenAI considered a rewrite inevitable.

[Is the bottleneck computation or coordination]
If computation is heavy, a C extension or moving a few modules may suffice, but coordination problems in the event loop and connection pools arise from the runtime's structure and are hard to fix piecemeal.

[Has the cost of rewriting fallen]
OpenAI said coding models let two people finish it in a single quarter.

## Where this touches Korea

OpenAI offers data residency in Korea, Japan, India, and Singapore, letting conversations and files in ChatGPT Enterprise and Edu workspaces be stored in those countries. Enforcing such region-specific storage rules along the request path is exactly the job of a storage layer like Habitat.

No Korean service has been confirmed to have published a full rewrite of a Python backend in Rust.

## Summary

![Summary card for the Habitat Rust rewrite](/assets/images/tech/openai-habitat-rust-rewrite/05-items.webp)
*Summary card for the Habitat Rust rewrite — Source: self-rendered from OpenAI Engineering's announcement*

OpenAI said a follow-up Part 2 will cover the storage layer that holds more than 500PB of data.

## Sources

- [[OpenAI] Rapidly scaling online storage to serve over 1 billion ChatGPT users, Part 1 (2026-09)](https://openai.com/index/scaling-storage-one-billion-users-part-one/)
- [[OpenAI Developers] Post summarizing Habitat's throughput and the rewrite (X, 2026-09)](https://x.com/OpenAIDevs/status/2098502006935814272)
- [[HackerNoon] The four Habitat failures](https://hackernoon.com/your-load-test-wont-find-these-four-gaps-learnings-from-openais-habitat)
- [[explainx] On the rewrite figures and the absence of outside validation (2026-09)](https://explainx.ai/blog/openai-habitat-python-rust-rewrite-two-engineers-2026)
- [[OpenAI] Introducing data residency in Asia (including Korea)](https://openai.com/index/introducing-data-residency-in-asia/)
