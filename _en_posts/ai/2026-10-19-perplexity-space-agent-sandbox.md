---
title: "Perplexity Open-Sources SPACE — 0 of 108 Agent Sandbox Escape Attempts Succeeded"
description: "The structure of Perplexity SPACE, which runs agent code in a microVM per task, and the results of its in-house escape tests"
date: 2026-10-19
category: AI
subcategory: News
tags: [perplexity, agent-sandbox, firecracker, microvm, ai-security]
image: /assets/og/en-2026-10-19-perplexity-space-agent-sandbox.png
---

On October 15, Perplexity open-sourced **SPACE**, its execution environment for agents
It is a sandbox platform that runs code written by AI agents inside a small virtual machine for each task

In its own security tests, attempts to break isolation and reach the host succeeded <mark>0 out of 108 times</mark>
The same tests did find bypasses of network blocking, which the company says it has fixed

![Isometric key art of the SPACE architecture from the Escaping SPACE report](/assets/images/ai/perplexity-space-agent-sandbox/01-hero-space.webp)
*Isometric key art of the SPACE architecture from the Escaping SPACE report — Source: Perplexity*

## What was announced

![Terminal checking the license and language of the perplexityai/SPACE repository via the GitHub API](/assets/images/ai/perplexity-space-agent-sandbox/en/02-term.webp)
*Terminal checking the license and language of the perplexityai/SPACE repository via the GitHub API — Source: run by me*

SPACE stands for *Sandboxed Platform for Agentic Code Execution*

It was posted to the GitHub repository perplexityai/SPACE under the **Apache-2.0** license
The code is written in Rust

- Isolation: one **Firecracker microVM** per task
- Control: create, run, pause, resume, and delete through an HTTP API
- Credentials: managed outside the sandbox and injected only when needed
- State: file snapshots and runtime checkpoints saved as diffs only
- Operation: handling every Perplexity Computer session since July 2026

Perplexity says it creates **millions** of sandboxes a day

It said creation was 3–5 times faster than with its previous commercial provider
It did not name that provider

## The VM escape test

![Perplexity chart summarizing sandbox escape 0/108 and network bypass 11/54 and 0/54](/assets/images/ai/perplexity-space-agent-sandbox/03-photo.webp)
*Perplexity chart summarizing sandbox escape 0/108 and network bypass 11/54 and 0/54 — Source: Perplexity*

On September 23, Perplexity published its test method in the report *Escaping SPACE: Part I*
It gave two tasks to AI agents with **root privileges** inside the virtual machine

| Task | Goal |
| :--- | :--- |
| Sandbox escape | Obtain an AWS honeytoken on the host |
| Network bypass | Obtain a flag from a blocked address |

It used nine model configurations across four settings combining whether source code was provided and how much network access was allowed
Each setting was tested three times

The escape task <mark>failed all 108 times</mark>

## Bypassing network blocking

![Perplexity results table of successes per setting for the nine model configurations](/assets/images/ai/perplexity-space-agent-sandbox/04-photo.webp)
*Perplexity results table of successes per setting for the nine model configurations — Source: Perplexity*

In the setting with the network fully blocked, it was 0 out of 54
In the setting that allowed only some addresses, <mark>11 out of 54</mark> succeeded in reaching a blocked address

| Model | Source provided | No source |
| :--- | :--- | :--- |
| Claude Opus 5.0 | **3/3** | 0/3 |
| GPT-5.6 Sol | **3/3** | 2/3 |
| Kimi K3 | 2/3 | 0/3 |
| GPT-5.6 Cyber | 0/3 | 1/3 |

One method was **DNS spoofing**, using fake DNS responses to point an allowed domain name at a blocked IP

The other went through a different service sharing the same CDN IP as an allowed site

On August 26, Perplexity reproduced the bypasses and fixed the vulnerability
It says that when it retested with the easiest setting to attack, bypasses succeeded 0 times

## Other sandbox services

![Table verifying HTTP, HTTPS, and TCP network policy bypasses on nine other sandbox platforms](/assets/images/ai/perplexity-space-agent-sandbox/05-photo.webp)
*Table verifying HTTP, HTTPS, and TCP network policy bypasses on nine other sandbox platforms — Source: Perplexity*

Perplexity also tested bypasses the same way on 10 other sandbox platforms
It says network policy bypass worked on <mark>8</mark> of them

Of the nine it disclosed, seven were affected, including E2B, Modal, Vercel, Daytona, and Fly.io
No bypass was confirmed on Cloudflare Sandbox or NVIDIA OpenShell

Each company was notified on September 1, and the results are as of September 10
Whether each is still in the same state may differ by company

### 🤝 Partners after the release

Akamai tested SPACE on its own cloud and launched it

Crusoe decided to adopt SPACE for its managed AI services
CoreWeave published a guide to deploying it on its Kubernetes

## What it means for users in Korea

More companies in Korea are also using coding agents such as Claude Code at the company level

If you run code written by an agent directly on your PC, you <u>depend heavily on the permission approval process</u>

My October 7 post covered permission issues when using Claude Code without a sandbox

🔗 Link - https://blog.naver.com/rottensweetpotato/224434104966

SPACE, by contrast, is a platform that confines code written by agents inside a virtual machine to run it
Deploying it on your own servers requires a Linux host that can use KVM

## What to watch next

- Follow-up reports: <mark>only Part I</mark> of *Escaping SPACE* is out
- Fixes by others: public responses from the seven where bypasses were confirmed
- Cloud offerings: pricing and regions of the Akamai and Crusoe commercial services
- Korean clouds: whether Korean providers will offer it

🔗 Link - https://github.com/perplexityai/SPACE

## Sources

- [[Perplexity] Open-sourcing SPACE (2026-10-15, scale, speed, partners)](https://www.perplexity.ai/hub/blog/open-sourcing-space)
- [[Perplexity] Escaping SPACE: Part I (2026-09-23, test method and results, source of three images in this post)](https://www.perplexity.ai/hub/blog/escaping-space-part-i)
- [[Perplexity] SPACE documentation](https://space.docs.perplexity.ai/guide/index.html)
- [[Runtime Wire] Perplexity open-sources SPACE (2026-10-15)](https://runtimewire.com/article/perplexity-open-sources-space-agent-sandbox)
