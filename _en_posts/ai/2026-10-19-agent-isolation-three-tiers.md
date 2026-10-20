---
title: "Isolating AI Agent Code — How Far Do Containers, gVisor, and MicroVMs Protect You?"
description: "Comparing the three tiers of coding agent execution isolation, containers, gVisor, and microVMs, by how directly they reach the host kernel"
date: 2026-10-19
category: AI
subcategory: Explainer
tags: [ai-agent, sandbox, container, gvisor, microvm]
image: /assets/og/en-2026-10-19-agent-isolation-three-tiers.png
---

Coding agents write code and run it themselves too
How much damage an accident causes depends on the environment that code runs in

Agent execution isolation is commonly divided into three tiers: **containers, gVisor, and microVMs**
In the end, the difference among the three is <mark>how directly they reach the host kernel</mark>

![Concept shot of code blocks running inside three transparent isolation layers that get thicker one by one](/assets/images/ai/agent-isolation-three-tiers/01-agy-3.webp)
*Concept shot of code blocks running inside three transparent isolation layers that get thicker one by one — Source: concept shot, self-generated with agy*

## When running code becomes dangerous

Before picking an isolation tier, you have to decide what you're trying to stop
The cases people worry about in agent execution are mostly three

- The agent runs malicious commands from instructions hidden in web pages and issues it reads
- Malicious code inside an installed package runs
- The agent accidentally deletes files or leaks keys

In all three, the code runs with the agent process's permissions
The goal of isolation is to keep that code from reaching <u>files, the network, and the kernel outside the sandbox</u>

## Tier 1: containers

![Terminal showing Alpine and Debian containers printing the same kernel version](/assets/images/ai/agent-isolation-three-tiers/en/02-term.webp)
*Terminal showing Alpine and Debian containers printing the same kernel version — Source: run by me*

Containers use namespaces and cgroups to isolate the files and network a process can reach
The kernel itself is **shared** with the host

On October 19, I launched two containers of different distros in Docker Desktop on a Mac
Both Alpine and Debian had the same kernel version, <mark>6.12.76-linuxkit</mark>

Exploiting just one kernel vulnerability can enable a **container escape** that reaches outside the container

You can reduce the system calls available with seccomp and AppArmor policies
But the gVisor documentation explains that it's hard to write policies precisely fitted to arbitrary code

## Tier 2: gVisor

**gVisor** is a user-space kernel made by Google
Instead of passing a container's system calls directly to the host kernel, Sentry, written in Go, receives and handles them

File access is handled through a separate process, Gofer
Sentry itself runs in a restricted seccomp environment that keeps it from accessing the file system directly

The advantage is that the kinds of system calls the host kernel receives shrink sharply

In exchange, handling system calls adds overhead
Some system calls and /proc and /sys files aren't implemented, so compatibility suffers too

In Docker, you can use it by switching the runtime to **runsc**

## Tier 3: microVMs

![Highlighted memory overhead, boot time, and creation rate figures from the Firecracker NSDI 2020 paper](/assets/images/ai/agent-isolation-three-tiers/03-photo-firecracker.webp)
*Highlighted memory overhead, boot time, and creation rate figures from the Firecracker NSDI 2020 paper — Source: USENIX*

MicroVMs use KVM hardware virtualization to give each task **its own guest kernel**

Even if agent code exploits a kernel vulnerability, what gets compromised first is the guest kernel
There is one more virtualization boundary before the host

The leading implementation, **Firecracker**, was built by AWS for Lambda and Fargate
The figures in its NSDI 2020 paper are below

| Item | Paper figure |
| :--- | :--- |
| Memory overhead | Under 5MB |
| Boot time | **Under 125ms** |
| Creation rate | 150 per second per host |
| Code size | About 50,000 lines of Rust |

The paper says the code is 96% smaller than QEMU
It's a design that cuts features to shrink the attack surface

But because it needs KVM, it can run directly only on Linux hosts
On a Mac or Windows, it has to go through one more Linux virtual machine

## Comparing the three tiers

| Method | Kernel boundary | Cost |
| :--- | :--- | :--- |
| Container | Shares the host kernel | Lightest |
| gVisor | User-space kernel | System call cost |
| MicroVM | **Separate guest kernel** | Requires KVM |

Perplexity chose microVMs for SPACE, the agent sandbox it released in October
It says agents with root privileges tried to escape 108 times but never reached the host

<mark>Even with strong isolation, outbound communication through allowed network paths has to be restricted separately</mark>
In the same tests, the setting that allowed part of the network was bypassed 11 out of 54 times through DNS spoofing and other methods

## When using Claude Code

Claude Code includes a **sandbox** that restricts file and network access using operating system features
macOS uses the built-in Seatbelt, and Linux and WSL2 use bubblewrap and socat

This is process isolation closer to tier 1, sharing the kernel
The official documentation warns that if you isolate only files and leave the network open, files such as SSH keys can get out

Options that skip permission approval only turn off confirmation and add no isolation
I covered the case of widening permissions without a sandbox in an October 7 post

🔗 Link - https://blog.naver.com/rottensweetpotato/224434104966

## How to choose

![Four criteria for choosing an isolation tier based on the kind of code being run](/assets/images/ai/agent-isolation-three-tiers/en/04-items.webp)
*Four criteria for choosing an isolation tier based on the kind of code being run — Source: self-rendered based on gVisor documentation and the Firecracker paper*

Whatever the tier, it's safer to keep API keys and tokens outside the sandbox and <u>pass them into the sandbox only when needed</u>
SPACE also chose a structure that manages credentials outside the sandbox

## Sources

- [[USENIX NSDI 2020] Agache et al., Firecracker: Lightweight Virtualization for Serverless Applications (source of one image in this post)](https://www.usenix.org/conference/nsdi20/presentation/agache)
- [[gVisor] What is gVisor? (Sentry and Gofer architecture, performance and compatibility costs)](https://gvisor.dev/docs/)
- [[Claude Code] Sandboxing documentation (Seatbelt, bubblewrap, network isolation)](https://code.claude.com/docs/en/sandboxing)
- [[Perplexity] Escaping SPACE: Part I (2026-09-23, escape and bypass tests)](https://www.perplexity.ai/hub/blog/escaping-space-part-i)
