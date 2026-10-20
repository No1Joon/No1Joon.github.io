---
title: "NVIDIA RTX Spark Laptops Launch in Korea — Starting in the ₩5 Million Range"
description: "The structure of RTX Spark laptops, which combine CPU and GPU on one chip and share up to 128GB of memory, and their launch prices in Korea"
date: 2026-10-18
category: Tech
subcategory: News
tags: [nvidia, rtx-spark, laptop, unified-memory, windows-on-arm]
image: /assets/og/en-2026-10-18-nvidia-rtx-spark-korea-launch.png
---

NVIDIA's chip for Windows laptops, **RTX Spark**, has launched in Korea

Sales began on October 16, 2026

It combines the CPU and GPU into one chip that shares up to 128GB of memory

In Korea, the 32GB model starts in <mark>the ₩5 million range</mark>

![Hero image from the NVIDIA RTX Spark press release](/assets/images/tech/nvidia-rtx-spark-korea-launch/01-hero-rtxspark.webp)
*Hero image from the NVIDIA RTX Spark press release — Source: NVIDIA*

## What launched

![NVIDIA logo](/assets/images/tech/nvidia-rtx-spark-korea-launch/02-logo-nvidia.webp)
*NVIDIA logo*

On October 16, NVIDIA announced that RTX Spark laptops had gone on sale worldwide

It's four months after the chip was unveiled at Computex 2026 in June

The first wave is nine models from six manufacturers

| Manufacturer | Model |
| :--- | :--- |
| ASUS | ProArt P14, **ProArt P16** |
| Dell | XPS 16 |
| HP | OmniBook Ultra, OmniBook X 14 |
| Lenovo | Yoga Pro 9n |
| Microsoft | Surface Laptop Ultra |
| MSI | Prestige N16 Flip AI+, **Prestige N16** |

In Korea, <u>ASUS and MSI products launched first</u>

The US starting price is $2,599 (₩3.64 million)

## The specs, explained

![RTX Spark laptop and the small desktop due in November](/assets/images/tech/nvidia-rtx-spark-korea-launch/03-rtxspark-laptop-desktop.webp)
*RTX Spark laptop and the small desktop due in November — Source: NVIDIA*

The chip is called **N1X**

It's a version of the **GB10** from the DGX Spark AI workstation, with specs adjusted for Windows laptops

| Item | N1X |
| :--- | :--- |
| CPU | Arm 20 cores (10 X925 + 10 A725) |
| GPU | Blackwell, 6,144 CUDA cores |
| Memory | LPDDR5X <mark>up to 128GB</mark> |
| Memory bandwidth | 300GB/s |
| AI compute | 1 petaflop FP4 |
| Power draw | About 80W |

The CPU was co-designed with MediaTek

It's a unified memory architecture in which the CPU and GPU share memory

The weights of large AI models can all be loaded into the laptop's memory

NVIDIA gave the 74-billion-parameter model Nemotron 3.5 Bolt as an example

It's shrunk to fit in 24GB of memory and run directly on the laptop

There's also a lower-tier N1 chip with 18 cores, but at launch it ships only in laptops

## Prices in Korea

![Bars showing Korean price ranges for RTX Spark laptops by memory](/assets/images/tech/nvidia-rtx-spark-korea-launch/en/04-chart.webp)
*Bars showing Korean price ranges for RTX Spark laptops by memory — Source: self-rendered based on reports by ZDNet Korea and The Elec*

32GB is in the ₩5 million range, 64GB in the ₩7 million range, and 128GB in <mark>the ₩9 million range</mark>

According to The Elec, the MSI Prestige N16 is the lowest price in Korea at ₩5,799,000

That's more than ₩2 million above the US starting price of ₩3.64 million!!

The US starting price is for a 24GB configuration, so it's hard to compare directly with the Korean 32GB model

NVIDIA cited rising memory prices as the reason for the high prices

One official said <u>they didn't expect memory prices to rise this much</u>

## Performance in reviews

![Bar chart comparing 3DMark Time Spy Extreme scores](/assets/images/tech/nvidia-rtx-spark-korea-launch/en/05-chart-3dmark.webp)
*Bar chart comparing 3DMark Time Spy Extreme scores — Source: self-rendered based on the Tech Times review roundup*

Overseas reviews came out all at once on October 15–16

The verdict converged on **strong GPU performance but relatively weak CPU performance**

[Graphics]
3DMark Time Spy Extreme 6,060 points, 29% higher than Ryzen AI Max+ 395

[Games]
Cyberpunk 2077 at about 70fps at 1080p Ultra, about 47fps at QHD

[CPU]
Multi-core at Apple M4 Pro level, single-core below the M5 generation (HotHardware)

[Battery]
14 hours 35 minutes of video playback (HotHardware)

NVIDIA touted 100fps or more in the latest games at 1440p, but review figures are lower than that

The 300GB/s memory bandwidth falls short of the up to 672GB/s of the RTX 5070 laptop GPU

<mark>Graphics scores are higher than the integrated chips compared, but discrete GPUs still lead in gaming performance</mark>

## Compatibility and what's still to come

![Microsoft logo](/assets/images/tech/nvidia-rtx-spark-korea-launch/06-logo-microsoft.webp)
*Microsoft logo*

RTX Spark laptops run on **Windows on Arm**

Programs for x86 run through Microsoft's emulator Prism, with some loss of performance

The main factor limiting games is **anti-cheat compatibility**

Games with Arm anti-cheat on launch day include Counter-Strike 2 and Fortnite

Kernel anti-cheat games without an Arm build won't run even through Prism!!

EA's anti-cheat doesn't support Arm yet either, and Call of Duty is slated for support in 2027

League of Legends and PUBG: Battlegrounds aren't on the announced support list

If there's a game you play often, <u>be sure to check before buying</u>~

For development, a PyTorch-CUDA build for Windows on Arm came out for the first time

97% of the 15,000 most popular Python packages have Arm versions

A small desktop with the same chip launches in November

## Sources

- [[NVIDIA Newsroom] Announcement that RTX Spark PCs are on sale (2026-10-16)](https://nvidianews.nvidia.com/news/nvidia-rtx-spark-pcs-available-today-a-new-beginning-for-windows-pcs)
- [[NVIDIA Developer Blog] RTX Spark development environment, local models, November desktop (2026-10)](https://developer.nvidia.com/blog/code-test-and-deploy-on-one-machine-with-nvidia-rtx-spark)
- [[ZDNet Korea] Korean launch event and price ranges by memory (2026-10-17)](https://zdnet.co.kr/view/?no=20261017092606)
- [[The Elec] Lowest Korean price, MSI Prestige N16 at ₩5,799,000, and N1X specs (2026-10-16)](https://www.thelec.kr/news/articleView.html?idxno=63851)
- [[Tech Times] Overseas review roundup, 3DMark, games, battery, anti-cheat (2026-10-16)](https://www.techtimes.com/articles/329104/20261016/rtx-spark-reviews-are-class-leading-gpu-meets-aging-cpu-cores-launch.htm)
- [[Windows Central] One-week review (2026-10-16)](https://www.windowscentral.com/hardware/nvidia/rtx-spark-review-benchmarks-2026)
- Exchange rate: converted at $1 ≈ ₩1,400
