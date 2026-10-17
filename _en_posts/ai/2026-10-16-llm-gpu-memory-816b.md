---
title: "How to Calculate LLM GPU Memory — How Many GB of VRAM Does an 816B Model Need?"
description: "Calculating weight size from parameter count and precision, then adding the KV cache, to work out the GPU memory Muse Spark Open 816B needs"
date: 2026-10-16
category: AI
subcategory: Explainer
tags: [llm, gpu-memory, vram, quantization, kv-cache]
image: /assets/og/en-2026-10-16-llm-gpu-memory-816b.png
---

Muse Spark Open, released by Meta, has 816 billion (816B) parameters. That one number is enough to roughly calculate the GPU memory it needs.

![Concept image of giant model weights split across multiple GPUs' memory](/assets/images/ai/llm-gpu-memory-816b/01-agy.webp)
*Concept image of giant model weights split across multiple GPUs' memory — Source: concept image · self-generated with agy*

## The basic formula

A model file is data storing each parameter's value as a number, so its size is the parameter count times the size of one number.

**Weight size (bytes) = parameter count × bytes per precision**

| Precision | One number | 816B model |
| :--- | :--- | :--- |
| FP32 | 4 bytes | 3,288GB |
| BF16 | 2 bytes | **1,644GB** |
| FP8 | 1 byte | 822GB |
| FP4 | 0.5 bytes | <mark>411GB</mark> |

Precision means how many bits represent one number. Training is usually done in BF16 (16-bit), and at deployment the size is cut with quantization, reducing bits to FP8 or FP4. Fewer bits mean fewer representable values, which can lower accuracy slightly.

![Weight size by precision for the 816B model](/assets/images/ai/llm-gpu-memory-816b/en/02-chart.webp)
*Weight size by precision for the 816B model — Source: self-rendered from Hugging Face API measurements*

## Checking against the actual files

The Hugging Face API returns, for each repository, the tensor count per precision and the actual storage size. It works without an account.

![Querying the tensor breakdown of the Muse Spark Open NVFP4 version via the Hugging Face API](/assets/images/ai/llm-gpu-memory-816b/03-term-hfapi.webp)
*Querying the tensor breakdown of the Muse Spark Open NVFP4 version via the Hugging Face API — Source: self-rendered Hugging Face API output*

The BF16 version has 822,036,529,664 parameters and 1,644GB of storage, nearly matching the formula (× 2 bytes). The actual parameter count being slightly above the 816B in the model name appears to be due to the added perception encoder that takes images and audio (1.8 billion) and the input and output embeddings (about 3.3 billion).

The NVFP4 version came to 533GB, more than the calculated 411GB.

[Quantization scales]
NVFP4 attaches one FP8 scale to every 16 values, for about 4.5 bits per value — 48.3GB in scales alone

[Parts left in BF16]
48.8 billion parameters were kept in BF16 rather than cut to 4 bits — 97.6GB

The FP4-quantized parameters number 773.1 billion (two per byte, 386.5GB), and adding the scales, the BF16 portion, and 0.5GB of FP32 brings the total to 533GB. For quantized models, it's safer to budget 20–30% above parameters × 0.5 bytes.

## KV cache, memory that grows with conversation length

Loading only the weights into memory isn't enough to run the model. To avoid recomputing earlier parts of a conversation, the model stores Key and Value values for each token — this is the KV cache. It grows with input length.

**KV cache (bytes) = 2 × layers × KV heads × head dimension × bytes × tokens**

Storing the Muse Spark Open structure from the model card (62 layers, 16 KV heads, head dimension 64) as a BF16 cache comes to about 254KB per token.

| Context | KV cache |
| :--- | :--- |
| 32K tokens | 8.3GB |
| 128K tokens | **33.3GB** |
| 1M tokens | <mark>266GB</mark> |

These values are upper bounds assuming every layer sees the full context. They shrink if some layers only look at short windows or the cache is reduced to FP8, and grow by the number of requests when serving several at once.

![Memory needed for NVFP4 weights plus a 128K-token KV cache](/assets/images/ai/llm-gpu-memory-816b/en/04-chart.webp)
*Memory needed for NVFP4 weights plus a 128K-token KV cache — Source: self-rendered from the Hugging Face API and model card*

Adding a 33GB cache for 128K tokens to the 533GB of weights gives 566GB. The model card's recommendation of 700GB or more VRAM for NVFP4 appears to add runtime compute buffers and capacity for multiple requests on top of this. The BF16 version is 1,644GB in weights alone, so the model card lists 2TB as required memory.

## Memory requirements vs compute for MoE models

Muse Spark Open has a mixture-of-experts (MoE) architecture, so each token uses only 8 of 256 experts — about 42 billion (42B) parameters — in computation. Generation speed and compute are therefore close to a 42B-class model.

But since you can't know in advance which token will go to which expert, all 816B parameters must be loaded into memory. The active parameter count in an MoE model's name (A42B) is a gauge of speed; required memory is calculated from the total parameter count.

## Applying it to other open-weight models

![BF16 weight size by open-weight model](/assets/images/ai/llm-gpu-memory-816b/en/05-chart.webp)
*BF16 weight size by open-weight model — Source: self-rendered from each company's published parameter counts and Hugging Face measurements*

Kimi K3, with 2.8 trillion parameters, is 5.6TB in BF16 weights alone, while Meta's own Muse Glimmer 30B is 60GB and fits on a single 80GB GPU. Models around 30 billion parameters shrink to 15–20GB in FP4 and can run on a PC with 32GB of memory. Results of running Gemma 4 at different sizes on a MacBook are in a separate post.

🔗 Link - https://blog.naver.com/rottensweetpotato/224379118246

## Minimum number of GPUs

![Minimum units per device to hold 700GB of VRAM](/assets/images/ai/llm-gpu-memory-816b/en/06-chart.webp)
*Minimum units per device to hold 700GB of VRAM — Source: self-rendered from the model card*

Dividing the model card's 700GB by memory per device gives the minimum count: 9 H100s (80GB), 5 H200s (141GB), 4 B200s (180GB), 3 B300s (288GB), or 2 M5 Ultra Mac Studios with 512GB of unified memory.

Tensor parallelism, which splits a model across multiple GPUs, usually groups them in units of 2, 4, or 8, so an 8× H100 server with 640GB total falls short of the requirement and you need two servers (16 GPUs). H200 fits in a single 8-GPU server (1,128GB). Two Mac Studios is a configuration Meta said can run the model by linking them with Apple MLX.

### Cost converted to won

Korean GPU cloud VESSL Cloud lists H100 80GB pricing on its pricing page from about $2.98 (₩4,170) per GPU per hour. Sixteen H100s cost about ₩66,800 an hour, or about ₩48,060,000 if left on for a full month (720 hours). Naver Cloud shows GPU server pricing only in its pricing calculator, so it couldn't be compared on published rates. Whether using the same model through an API costs less depends on daily throughput.

## Summary

![Four points on calculating GPU memory](/assets/images/ai/llm-gpu-memory-816b/en/07-items.webp)
*Four points on calculating GPU memory — Source: self-rendered*

## Sources

- [[Hugging Face] Muse-Spark-Open-816B-A42B model card (architecture, memory requirements)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- [[Hugging Face API] NVFP4 version tensor breakdown and storage size (queried 2026-10-16)](https://huggingface.co/api/models/meta-models/Muse-Spark-Open-816B-A42B-NVFP4)
- [[Meta] Muse Spark Open announcement (running on two M5 Ultra Mac Studios)](https://research.meta.ai/blog/muse-spark-open)
- [[NVIDIA Research] Pushing Intelligence to 4-bit (NVFP4 16-value blocks, about 4.5 bits)](https://research.nvidia.com/labs/eai/blogs/pushing-intelligence-to-4-bit/)
- [[VESSL] NVIDIA GPU cloud pricing (H100 hourly rate, checked 2026-10-16)](https://vessl.ai/en/gpu/b200)
- Exchange rate: converted at $1 ≈ ₩1,400
