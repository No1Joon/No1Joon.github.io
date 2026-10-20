---
title: "Where the NIST P-256 Seed Came From — A Random Number Seeded With a 1997 Timestamp, Found by Claude"
description: "Anthropic's analysis and reproduction showing that the P-256 seed, long suspected of a backdoor because its origin was unknown, was a random number seeded with a 1997 timestamp"
date: 2026-10-19
category: Math
subcategory: Explainer
tags: [p-256, elliptic-curve, nist, random-number-generator, cryptography]
image: /assets/og/en-2026-10-19-nist-p256-seed-origin.png
---

The elliptic curve **P-256**, widely used in website certificates and passkeys, contained one number of unknown origin
It is the 20-byte **seed** provided by the US National Security Agency (NSA)

On October 16, Anthropic revealed that this number was <mark>a random number seeded with a 1997 timestamp</mark>
The output of its published reproduction code matched the seed value in the standard

![Curve P-256 parameters and SEED value from the FIPS 186-4 appendix, highlighted](/assets/images/math/nist-p256-seed-origin/01-hero-fips.webp)
*Curve P-256 parameters and SEED value from the FIPS 186-4 appendix, highlighted — Source: NIST*

## Why the seed was suspected

![Concept shot of examining a mysterious number seed through a magnifying glass](/assets/images/math/nist-p256-seed-origin/02-agy.webp)
*Concept shot of examining a mysterious number seed through a magnifying glass — Source: concept shot · self-generated with agy*

An elliptic curve is defined by an equation of the form **y² = x³ + ax + b**
In P-256, the coefficient b is made from the value obtained by applying the SHA-1 hash function to the seed

It is hard to work backward from a hash value to the original input
So once the seed is fixed, it is hard to choose b arbitrarily

A number that proves there was no tampering by showing its origin is called a *nothing-up-my-sleeve* number

The problem was that there was no public material explaining how the seed itself was chosen

NIST included the P-192 to P-521 curves in FIPS 186-2 in 2000
The seeds the NSA provided were printed as is, without explanation

By repeatedly changing the seed and computing the hash, you could pick a curve with particular properties
This suspicion grew after the 2013 allegations of an NSA backdoor in Dual_EC_DRBG

NSA mathematician Jerry Solinas reportedly said in 2015 that the seeds were **hashes of a joke phrase**
With his death in 2023, it became hard to confirm directly with him

A bounty was even offered to whoever found the seed

## A random number generator called lrand48

The answer was not a hash
It was the output of **lrand48**, a random number function provided by C libraries in the 1990s

lrand48 is a **linear congruential generator** (LCG)
It keeps updating a single 48-bit state value with the formula below

**Xₙ₊₁ = (25,214,903,917 × Xₙ + 11) mod 2⁴⁸**

The starting state is set by **srand48(t)**
It shifts the time t (seconds counted from January 1, 1970) left by 16 bits and fills the low 16 bits with 0x330E

### 🔢 How the P-256 seed came out

The starting value is 01:52:34 UTC on August 16, 1997
In Korean time, that is 10:52:34 a.m.

That time converted to seconds, 871,696,354, is t

Each time the state is updated, the top 8 bits are taken and used as one byte
Collecting 20 bytes gives one seed candidate

The P-256 seed was <mark>the 1,842nd candidate</mark> of this run, by which point lrand48 had run 36,840 times

![Bar chart comparing which candidate in each run the published seeds of the five NIST prime-field curves were](/assets/images/math/nist-p256-seed-origin/en/03-chart.webp)
*Bar chart comparing which candidate in each run the published seeds of the five NIST prime-field curves were — Source: self-rendered based on running Anthropic's reproduction code*

All 10 prime-field curve seeds were seeded with times between May 1997 and April 1998
P-224 was the 7,026th candidate of a run on April 3, 1998

## How Claude found it

An Anthropic employee asked an internal research model about the seed's origin without giving it the joke-phrase clue
Claude found the origin of the five NIST prime-field curve seeds in <mark>under 30 minutes</mark>

### 🔍 The top bits were all 0

Claude first wrote a scanner looking for traces of 1990s C library random number generator output
It checked 34 combinations of generator and output truncation method against the seeds, shifting one bit at a time

Splitting each seed into five 32-bit words, in 4 of the 10 seeds the leading bit of all 20 words was 0
The probability of that happening by chance is **1 in 5,810**

lrand48 returns only the top 31 bits of its 48-bit state, so the leading bit of a 32-bit word is always 0

It tried all 2¹⁷ = 131,072 possibilities for the 17 unknown bits
The following words then matched the generator's output

### 🧮 The LLL lattice algorithm

The prime-field curve seeds kept only some bits of the output, so the method above didn't work
The problem of recovering an LCG's internal state from truncated output can be solved as a lattice problem

Claude recovered the state with the **LLL** (Lenstra–Lenstra–Lovász) basis reduction algorithm
All 5 NIST seeds and all 5 ANSI X9.62 seeds were of the form **lrand48() >> 23**

Since an LCG can be run backward to earlier states, it traced back to the point where the low 16 bits were 0x330E
Reading the upper 32 bits at that point as a date gave times in 1997–1998 for all of them

<mark>All 10 seeds matching the same generator with plausible dates is hard to explain as coincidence</mark>

## Running the reproduction myself

![Terminal regenerating the seeds of the five NIST prime-field curves by running Anthropic's published code](/assets/images/math/nist-p256-seed-origin/en/04-term.webp)
*Terminal regenerating the seeds of the five NIST prime-field curves by running Anthropic's published code — Source: Anthropic's published code, run by me*

Anthropic released the reproduction code under CC0 (public domain)
Running it on Python 3.14 finished in under 0.2 seconds

I compared the printed seeds character by character against the values in the appendix of the NIST standard FIPS 186-4

| Curve | Compared with FIPS 186-4 seed |
| :--- | :--- |
| P-192, 224, 256, 384, 521 | **All 5 match** |
| B-233, 283, 409, 571 | All 4 match |
| B-163 | <mark>Not in the code</mark> |

The binary-field curves B-233 through B-571 match the case seeded with the time divided by 2
Read as is, it gives February 1984; doubled, it gives April 17, 1998

I also checked, following the FIPS 186-4 appendix procedure, whether the curve coefficient b comes out of the seed
The value r made by feeding the P-256 seed into SHA-1 satisfied **r × b² ≡ −27 (mod p)**

## The backdoor suspicion and remaining questions

Anthropic said this result is not a weakness in ECDSA or a new attack
Its explanation is that if the seeds were made with a common random number generator seeded with the time, there is less room to pick a curve and hide it

- Skipped candidate: <mark>the 876th candidate</mark> of the P-256 run also gave a qualifying curve but was not used
- B-163 seed: not reproduced by any method
- Base points: how the base points G of P-224, 256, 384, and 521 were made is unconfirmed
- Number of runs: how many runs were made with different times can't be determined from the seed values

The origin of the base points of P-192 and the five ANSI X9.62 example curves was confirmed
They came from Arjen Lenstra's FreeLIP random number generator

The seed bounty of about $36,864 (₩51.61 million) is being donated to ISRG
ISRG is the nonprofit that runs the free certificate authority Let's Encrypt

## Where P-256 is used in Korea

![Terminal using openssl to check that the www.naver.com certificate's public key is prime256v1](/assets/images/math/nist-p256-seed-origin/en/05-term.webp)
*Terminal using openssl to check that the www.naver.com certificate's public key is prime256v1 — Source: run by me*

P-256 is the same curve also called **secp256r1** or **prime256v1**, depending on the standard
ES256, the default signature scheme for passkeys (WebAuthn), is also P-256 ECDSA

On October 19, 2026, I checked the certificates of major Korean sites with openssl

| Site | Certificate public key |
| :--- | :--- |
| www.naver.com | **P-256 (EC)** |
| www.google.com | P-256 (EC) |
| www.daum.net | RSA 2048 |
| www.kakaocorp.com | RSA 2048 |
| www.gov.kr | RSA 2048 |
| www.kbstar.com | RSA 2048 |
| toss.im, www.coupang.com | RSA 2048 |

Naver's servers use P-256 ECDSA for signatures during the connection
For key exchange, Naver, Google, and Coupang all negotiated X25519MLKEM768 rather than P-256

Anthropic said there is nothing readers need to change
This result does not lower the security of services that use P-256

## Sources

- [[Anthropic] Claude reveals ECDSA curve origins (2026-10-16, reproduction code under CC0, source of one image in this post)](https://www.anthropic.com/research/ecdsa-curve-origins)
- [[NIST] FIPS 186-4 Digital Signature Standard Appendix D (curve parameters and SEED, source of one image in this post)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf)
- [[Koblitz & Menezes] A Riddle Wrapped in an Enigma (overview of the NIST curve seed debate, 2015)](https://eprint.iacr.org/2015/1018)
- Exchange rate: converted at $1 ≈ ₩1,400
