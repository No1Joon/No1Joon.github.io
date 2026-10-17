---
title: "Meta Muse Spark Open — 816B Open Weights Released, Plus Muse Wonder"
description: "The architecture, performance, and license of Meta's first frontier model Muse Wonder and Muse Spark Open, whose weights were released three days later"
date: 2026-10-16
category: AI
subcategory: News
tags: [meta, muse-spark, open-weights, moe, llm]
image: /assets/og/en-2026-10-16-meta-muse-spark-open-816b.png
---

On October 12, Meta launched its first frontier model, **Muse Wonder**, available only through the API and subscriptions, and three days later on October 15 it released the weights of **Muse Spark Open**, a model one tier below. It's a mixture-of-experts (MoE) model that uses 42 billion of its 816 billion total parameters at a time, and Meta announced it as the highest-performing open-weight model from the US.

![Muse Spark Open Weights announcement key visual](/assets/images/ai/meta-muse-spark-open-816b/01-hero-social.webp)
*Muse Spark Open Weights announcement key visual — Source: Meta*

## Two announcements in three days

- October 12: Muse Wonder and Muse Wonder Full unveiled, Meta's first frontier models
- October 15: Muse Spark Open weights released, downloadable from Hugging Face and elsewhere
- Both have a 1-million-token context window (the input length processed at once)
- Wonder is API and subscription only; Spark Open weights are distributed under the Muse Model License

According to TechCrunch, Muse Wonder was trained at Meta's Prometheus data center in central Ohio and is the first frontier model released since Alexandr Wang reorganized Meta's AI organization in August 2025. Muse Spark Open is based on Muse Spark 1.2, released in August, and shares its base model with Muse Spark 1.3.

## Muse Wonder, the top closed-weight model

![Meta logo](/assets/images/ai/meta-muse-spark-open-816b/02-logo-meta.webp)
*Meta logo*

Muse Wonder is available in the Meta Model API and the coding tool Muse Code, while the higher-end Wonder Full isn't offered through the API and is available only to Muse Code subscribers. It takes text, images, video, and audio as input, and Meta highlighted **active memory**, which remembers and reuses information the user provides.

| Item | Muse Wonder | Muse Wonder Full |
| :--- | :--- | :--- |
| Availability | API, Muse Code | Muse Code subscription only |
| Input, 1M tokens | **$4 (₩5,600)** | No API |
| Output, 1M tokens | $20 (₩28,000) | No API |
| AA Intelligence Index | 52 (Max setting) | <mark>56</mark> (reported) |

TechCrunch assessed the API pricing as roughly on par with GPT-6 Sol and Claude Opus 5.5.

On independent evaluator Artificial Analysis's comparison page, Muse Wonder (Max setting) scores 52 on the Intelligence Index, and Claude Opus 5.5 (Max) scores 58. The figure of 56 for Wonder Full comes from secondary reporting and couldn't be confirmed in Artificial Analysis's original data.

Meta said that in its own tests the Wonder family scored similarly to Fable 5.1 and GPT-6 Astra, and on MemoryBench, which evaluates memory performance, scored higher than Fable, Opus, and Astra.

## Muse Spark Open specs

Here's the architecture listed on the Hugging Face model card.

| Item | Value |
| :--- | :--- |
| Total and active parameters | **816B · 42B** |
| Experts | 8 of 256 used |
| Layers | 62 |
| Context | 1M tokens |
| Input | Text, images, video, audio |
| Output | Text |
| Released precisions | BF16, NVFP4 |

Because the mixture-of-experts architecture uses only 8 of 256 experts per token, compute is at the level of a 42-billion-parameter model.

All 816 billion parameters must be loaded into memory, so the model card says it needs 700GB or more of VRAM for NVFP4 and 2TB for BF16. Meta also said it can run the model on two M5 Ultra Mac Studios with 512GB of unified memory linked with MLX.

### Benchmarks

![Benchmark comparison of Muse Spark Open and other open-weight models](/assets/images/ai/meta-muse-spark-open-816b/03-bench-scorecard.webp)
*Benchmark comparison of Muse Spark Open and other open-weight models — Source: Meta*

In the table Meta published, Muse Spark Open scored higher than the comparison models on agentic tasks and knowledge questions. JobBench, which simulates real work, at 61.8; the tool-calling test MCP-Atlas at 89.2; and HLE-Diamond, solved without tools, at 26.1 are the highest among the comparison models.

On the coding test Terminal-Bench 2.1 it scored 76.4, lower not only than Kimi K3 (85.0) and GLM 5.3 (83.9) but also than fellow US model Beam from Reflection AI (80.1).

![Artificial Analysis Intelligence Index of open-weight models](/assets/images/ai/meta-muse-spark-open-816b/en/04-chart-aa.webp)
*Artificial Analysis Intelligence Index of open-weight models — Source: self-rendered from the Meta model card*

The Artificial Analysis Intelligence Index combines results from multiple tests. Muse Spark Open scores 39, below Chinese models such as GLM 5.3 (45), Kimi K3 (44), and Qwen3.8 (40), and above NVIDIA's Nemotron 3 Ultra (23). Meta's "best in the US" claim comes from a comparison that excludes Chinese models. All figures in this table were measured by Meta itself, and no independent evaluation has come out yet.

Safety metrics are something Meta emphasized separately. Because releasing weights means the model can be used without system-level safeguards, it did additional safety training, and on the jailbreak test StrongREJECT v2 it scored 0.5 (lower is better), far apart from the comparison models (62.9–86.4).

## License and distribution

![Hugging Face logo](/assets/images/ai/meta-muse-spark-open-816b/05-logo-huggingface.webp)
*Hugging Face logo*

The weights are available from Hugging Face, Amazon SageMaker AI, Google Cloud Model Garden, and Microsoft Foundry, and seven providers including Baseten, Fireworks AI, Groq, OpenRouter, and Together AI also offer it via API. Downloading the weights from Hugging Face requires submitting a form with your legal name, date of birth, and affiliated organization, which can't be edited after submission.

| Condition | Muse Model License |
| :--- | :--- |
| Commercial use, fine-tuning, distillation | Allowed |
| Attribution requirement | **Built with Muse Spark Open** |
| API provider businesses | Separate agreement above ₩28 billion in annual revenue |
| Age of use | 18 and older |

You must prominently display Built with Muse Spark Open on product screens, documentation, or settings screens, and the same requirement applies to derivative models fine-tuned or distilled from it.

Businesses that offer the model to outside customers via API must notify Meta and sign a separate agreement if 12-month revenue exceeds about $20 million (₩28 billion). Internal use, research, and embedding it in your own products are excluded from this condition. Compared with Reflection AI's Beam, released under Apache 2.0, or Xiaomi MiMo V2.6 under the MIT license, it's a license with strings attached.

## Relevance in Korea

The model card says it was trained on data in more than 100 languages but doesn't explicitly list Korean among supported languages. It also says not all languages in the training data were evaluated and performance may degrade outside the primary languages, so using it for Korean-language services requires testing it yourself.

Korean companies downloading it to internal servers aren't affected by the revenue condition and only need to meet the attribution requirement. Cloud and AI companies selling API access to outside customers with this model need to weigh the ₩28 billion annual revenue threshold. Loading the NVFP4 weights into memory alone takes 700GB of VRAM, so with 80GB-class GPUs you need at least nine, and adding the KV cache brings it to the scale of two servers. Whether the Muse Wonder API is available in Korea couldn't be confirmed from published materials.

## What to watch next

- Evaluation results for Muse Spark Open from independent bodies such as Artificial Analysis
- The full Muse Spark Open safety evaluation report Meta has promised
- Whether Muse Wonder Full opens up via API
- Hands-on measurements of Korean-language performance by Korean developers

## Sources

- [[Meta] Muse Spark Open announcement (2026-10-15, specs, distribution, safety training, source of two images in this post)](https://research.meta.ai/blog/muse-spark-open)
- [[Hugging Face] meta-models/Muse-Spark-Open-816B-A42B model card (architecture, benchmarks, license, memory requirements)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- [[PyTorch] Muse Spark Is Now an Open-Weights Model (2026-10-15, Helion kernels, TorchTitan)](https://pytorch.org/blog/muse-spark-open/)
- [[TechCrunch] Meta releases its first frontier model, Muse Wonder (2026-10-12, pricing, training data center)](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder)
- [[Artificial Analysis] Muse Wonder vs Claude Opus 5.5 comparison (Intelligence Index)](https://artificialanalysis.ai/models/comparisons/muse-wonder-vs-claude-opus-5-5)
- [[MindStudio] Muse Wonder benchmarks vs Opus and GPT-6 (reported Wonder Full score of 56)](https://www.mindstudio.ai/blog/muse-wonder-benchmarks-vs-opus-gpt6)
- Exchange rate: converted at $1 ≈ ₩1,400
