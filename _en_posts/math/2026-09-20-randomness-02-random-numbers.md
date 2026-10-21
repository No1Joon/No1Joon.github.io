---
title: "Randomness (2) — Are Random Numbers Really Random? How Computers Generate Them"
description: "How pseudorandom numbers are computed, the seed problem, why cryptography needs its own random numbers, and quantum random number generation"
date: 2026-09-20
category: Math
subcategory: Explainer
tags: [prng, csprng, randomness, security, quantum-random]
image: /assets/og/en-2026-09-20-randomness-02-random-numbers.png
---

A lotto machine mixes balls with air. The French-made VENUS draw system picks six balls using air mixing and a rotating drum, and the process goes out live every Saturday evening.

A computer has no balls to mix. And yet a random function returns a number. How is that number generated, and how random is it?

![A sequence scattering out of a fixed rule](/assets/images/math/randomness-02-random-numbers/01-agy-hero.webp)
*A sequence scattering out of a fixed rule — Source: concept image · self-generated with agy*

## How pseudorandom numbers are computed

The random numbers programs use are mostly **pseudorandom**. They are a sequence that looks random produced by a fixed formula, so the same starting value gives the same result.

The simplest form, a linear congruential generator, looks like this.

Xₙ₊₁ = (a × Xₙ + c) mod m

With a = 1,664,525, c = 1,013,904,223, m = 2³², and a starting value of 42, the next value is 1,083,814,273. Feed that back into the formula and you get the next one, repeating from there.

The starting value here is **the seed**. The same seed regenerates the same sequence exactly, and that is a feature, not a defect. It is the property you need to rerun a simulation and get the same result, to reproduce a game map from one line of code, or to reproduce a failing test as it was.

Python's random module uses the Mersenne Twister. Its period is 2¹⁹⁹³⁷ − 1, so there is no worry about the sequence repeating.

But a long period and hardness to predict are different things. Collecting **624 outputs is enough to recover the Mersenne Twister's internal state**, after which the next values follow by calculation.

## Incidents caused by predictable random numbers

![Moments where random numbers separated an incident from a technology](/assets/images/math/randomness-02-random-numbers/en/02-chart.webp)
*Moments where random numbers separated an incident from a technology — Source: self-rendered from reporting and presentations*

### Debian OpenSSL, with only 30,000 seeds

In September 2006, part of what fed the random seed in a Debian package was removed by mistake. What was left as random input was effectively just the process ID.

On Linux the default maximum process ID is 32,768. With only about 30,000 seeds, there are only that many keys to generate, so an attacker can generate them all in advance and compare.

Because of this problem (CVE-2008-0166), disclosed in May 2008, every SSL and SSH key made on Debian-derived systems in the meantime had to be discarded and regenerated.

### The PS3, which used the same random number twice

The ECDSA digital signature scheme requires a fresh random number for every signature. If two signatures come out with the same value, the resulting simultaneous equations let you compute the private key.

In analysis published in December 2010, the PlayStation 3 was found to be using a fixed value. Two signatures exposed the console's signing key.

Neither incident was an attack on the cryptographic algorithm itself. It was only that **the random numbers fed into it were predictable**.

## Choosing random numbers by purpose

| Use | Property needed | What to use |
|---|---|---|
| Simulation and statistical sampling | Reproducibility and speed | A PRNG such as the Mersenne Twister |
| Game maps and card shuffles | Speed | PRNG |
| <mark>Cryptographic keys, session tokens, passwords</mark> | <mark>Unpredictability</mark> | <mark>The OS's cryptographic RNG (CSPRNG)</mark> |
| Device authentication and bulk key generation | Physical randomness | Hardware RNG or QRNG |

random is for simulation; secrets is for security.

💻 [Source code: use secrets for security random numbers]

    import secrets

    token = secrets.token_urlsafe(32)
    pin = secrets.randbelow(1000000)

On Linux and macOS this module takes the operating system's random numbers directly. The kernel accumulates hard-to-predict events — keystroke intervals, disk response times, interrupt arrival times — in an entropy pool, then expands them through a cryptographic algorithm on output.

## Random numbers generated from physical phenomena

A computed sequence, however well made, rests on computation. So the source of randomness is taken from physical phenomena.

### Hardware random number generators

A circuit inside the CPU measures an uncontrolled physical signal such as thermal noise and turns it into bits. The RDRAND instruction on Intel and AMD processors works this way.

### Quantum random number generators

Fire a photon at a half-silvered mirror and whether it passes through or reflects is settled only by probability. It is not that some hidden rule makes it look that way — it is not determined in principle, so there is nothing to compute backwards from.

In Korea this technology reached phones first. SK Telecom and ID Quantique put a QRNG chip in the Galaxy Quantum in 2020, and the Galaxy Quantum 5 carries a 2.5 × 2.5 mm chip.

At Quantum Korea in July 2026, a 10Gbps-class QRNG implemented on a 10 × 10 mm chip was presented, along with plans for an integrated quantum key distribution chip putting the transmitter, receiver, and QRNG on one die.

## The bias in random numbers people make

This has all been about machines, but the random numbers people actually produce show heavy bias.

Ask someone to pick any number between 1 and 10 and the choices cluster on 7. Surveys vary, but reports that about one in four picks 7 recur. Avoiding the middle, avoiding the ends, and avoiding even numbers leaves everyone with similar options.

Language models learned the same bias. In one experiment, asked to pick from 1 to 50, several models clustered around 27. Having learned from text people wrote, they reproduce people's bias.

Picking lotto numbers, from part 1, is exactly this case. Numbers people choose overlap with other people's, and when they overlap the prize is split.

[Randomness (1) — One in 8.15 Million for the Lotto Jackpot, and How Far Luck Goes](/en/posts/randomness-01-lotto-probability/)

## Summary

![Summary of random numbers](/assets/images/math/randomness-02-random-numbers/en/03-items.webp)
*Summary of random numbers — Source: compiled from this post · self-rendered*

When you need randomness there is one question to ask: would it be a problem if someone could work this number out backwards? If so, take it from the operating system or a physical device; if not, the fast and reproducible option is better.

## Sources

- [Donghaeng Lottery] How Lotto 6/45 is drawn (the VENUS draw system, air mixing)
- [CERT/CC VU#925211] Debian and Ubuntu OpenSSL packages contain a predictable random number generator (CVE-2008-0166)
- [fail0verflow] Console Hacking 2010, PS3 Epic Fail (ECDSA random number reuse)
- [SK Telecom Newsroom] Quantum cryptography technology shown at Quantum Korea 2026 (10Gbps QRNG chip, integrated QKD chip)
- [Quantum Times] SK Telecom and ID Quantique unveil the Galaxy Quantum 5 (2.5 × 2.5 mm QRNG chipset)
- [Python documentation] secrets, Generate secure random numbers for managing secrets
