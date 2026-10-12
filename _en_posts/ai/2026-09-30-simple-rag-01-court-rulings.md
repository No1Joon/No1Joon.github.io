---
title: "Dead-Simple RAG (1) — A Local RAG Built on Anonymized Court Rulings, Statute Hits 18%→32%"
description: "How I built a pseudonymized corpus from AI Hub's anonymized court-ruling data and had a local LLM draft rulings grounded in similar cases"
date: 2026-09-30
category: AI
subcategory: Explainer
tags: [rag, legal-tech, local-llm, embedding, ai-hub]
image: /assets/og/en-2026-09-30-simple-rag-01-court-rulings.png
---

I built a court-ruling RAG myself using the **anonymized court-ruling dataset** that AI Hub published in June 2026. The dataset comes with labels for replacing the people, organizations, and addresses that appear in rulings with pseudonyms, and applying those labels produces a training corpus in which the same person is linked to the same pseudonym both within one document and across documents.

I embedded that corpus for search and had a local LLM write draft reasoning for hypothetical rulings, grounded in similar cases. Every step ran on this one PC, and no ruling text was sent anywhere outside it.

![AI Hub anonymized court-ruling dataset page](/assets/images/ai/simple-rag-01-court-rulings/01-hero-aihub.webp)
*AI Hub anonymized court-ruling dataset page — Source: AI Hub*

## What the dataset contains

![Number of JSON files per folder](/assets/images/ai/simple-rag-01-court-rulings/02-term-dataset.webp)
*Number of JSON files per folder — Source: my own count of AI Hub data · self-rendered*

It was built by A-Neut Co., Ltd. as lead, with PCN and the Korea IT Law Institute participating. AI Hub lists 21,000 rulings in total; the released archives hold 16,800 in the training split and 2,100 in the validation split, 18,900 in all.

| Type | Training | Validation |
| :--- | :--- | :--- |
| General rulings | **12,000** | 1,500 |
| 1st·2nd·final instance | 4,800 | 600 |

General rulings are centered on 3,400 civil, 3,200 general administrative, and 2,400 criminal rulings, with 400–600 each of labor, patent, finance and tax, personal information, family, and corporate rulings. The 1st·2nd·final instance set gathers the three rulings of one case — first instance, appeal, and final appeal — in one folder; the training split has 1,600 cases.

Each item is a JSON file in three parts: **info** (case information), **sections** (body sections such as holdings summary, judgment summary, and reasoning), and **annotations** (anonymization labels). In the general-ruling training split, the median body length was 4,531 characters, and the longest ruling ran 283,031 characters.

## Anonymization labels

![Structure of one label](/assets/images/ai/simple-rag-01-court-rulings/03-term-annotation.webp)
*Structure of one label — Source: AI Hub labeling data · self-rendered*

One label records which original text at which position (**span**) in the body should be replaced with which pseudonym (**replacement_text**), along with the rule behind it and the reason for the decision. Every label used a single treatment, **GENERALIZE**.

![Label counts by rule in the general-ruling training split](/assets/images/ai/simple-rag-01-court-rulings/04-chart.webp)
*Label counts by rule in the general-ruling training split — Source: my own count of AI Hub data · self-rendered*

Of the 211,400 labels across the 12,000 general rulings in the training split, 88.5% are organization names (R7). Not only company names but also institutions such as the Supreme Court and the Intellectual Property Trial and Appeal Board are treated as organizations and become pseudonyms like **Organization-4**. Personal names (R1) become role-aware pseudonyms such as **Person-1**, **Plaintiff-1**, and **Victim-1**, and detailed addresses (R3) are reduced to the city/county/district level, like **Eunpyeong-gu, Seoul A**.

### Data quirks I found myself

- About 13% of labels have spans off by one or two characters from the body, so the position has to be re-found using the original string
- Names redacted when rulings were made public are already marked as **#name#** in the original text
- In 15,640 of the 16,800 training rulings, even the heading of the disposition (主文) section is redacted as **#name#**

## Building the pseudonymized corpus

![Before and after applying labels](/assets/images/ai/simple-rag-01-court-rulings/05-term-before-after.webp)
*Before and after applying labels — Source: AI Hub data · self-rendered*

Applying the labels to the body turns two people who were both hidden behind a single **#name#** in the original into **Person-1** and **Person-2**. The distinction between people is preserved even while pseudonymizing.

In my first implementation, I handled misaligned labels with a document-wide string replacement, and every **#name#** ended up replaced with the first pseudonym. I got the result above after changing it so each label replaces only the one occurrence closest to its original position.

When a name labeled at only one position appeared again elsewhere, I replaced it once more with the same pseudonym. There were 1,061 of these second-pass replacements, and after applying them, 0 of the 16,800 training rulings still contained an original name, organization, or address.

### Tracking the same entity across instances

A label's **link_entity_id** is an identifier pointing to the same person or organization. Of the 1,600 cases in the 1st·2nd·final instance training split, 1,476 (92.3%) had identifiers appearing in both the first and second instance, and 1,370 (85.6%) had identifiers appearing in all three.

All 5,150 pairs appearing in both first and second instance received the same pseudonym. **Plaintiff-1** in the first instance is still **Plaintiff-1** in the second and third, so the same person's arguments and the court's findings can be followed across instances.

## The dead-simple RAG setup

| Stage | What I used |
| :--- | :--- |
| Retrieval unit | 1 ruling = 1 vector |
| Embedding | **BAAI/bge-m3** |
| Generation | **Qwen3-4B-Instruct-2507** 4-bit |
| Runtime | Apple M3 Pro 36GB · MLX |

For each ruling, I concatenated the case name, holdings summary, judgment summary, and the beginning of the reasoning, capped it at 1,800 characters, and turned it into one vector. I did no paragraph-level chunking.

bge-m3 is a multilingual embedding model BAAI released in February 2024; it supports more than 100 languages and handles up to 8,192 tokens. The downloaded model file has 567.75 million parameters (float32, 2.27GB), and it is MIT-licensed.

Embedding the 16,800 training rulings took 5,041 seconds (84 minutes). That is a single measurement under a low-load setting — batch size cut to 8 with a 0.5-second pause between batches — so I could keep doing other work.

## Comparing retrieval methods

![Referenced-provision hit rate by retrieval method](/assets/images/ai/simple-rag-01-court-rulings/06-chart.webp)
*Referenced-provision hit rate by retrieval method — Source: my own measurement · self-rendered*

I used the holdings summaries of the 826 validation rulings that had both a holdings summary and referenced provisions as queries, and counted whether the top 5 results from the training split cited the same statutory provisions. The baseline was character 2–3-gram TF-IDF, and the third condition was a hybrid (RRF) combining the two rankings.

| Metric (top 5) | TF-IDF | bge-m3 | Hybrid |
| :--- | :--- | :--- | :--- |
| Share of rulings with the same provision | 20.6% | 17.9% | **20.9%** |
| At least 1 hit | <mark>54.5%</mark> | 48.6% | 53.4% |
| Share in the same field | 69.9% | 69.6% | **71.9%** |

The keyword method hit provisions more often than the embedding. Holdings summaries contain statute names and article numbers verbatim, so a method that finds documents with overlapping characters seems to have had the advantage.

Only 6,579 (39%) of the training rulings list referenced provisions, so whenever a ruling without provisions is retrieved, the hit rate drops accordingly. Search time per query was 71.6ms for bge-m3 and 459.9ms for TF-IDF, making bge-m3 about 6 times faster (median of 5 runs).

### How referenced provisions are distributed in embedding space

![Rotating 3D map of bge-m3 embeddings](/assets/images/ai/simple-rag-01-court-rulings/07-b-chart.webp)
*Rotating 3D map of bge-m3 embeddings — Source: AI Hub data · UMAP 3D · self-rendered*

For each of the 6,579 rulings with referenced provisions, I took its 10 nearest neighbors in the original space and counted the share sharing at least one provision. It was 21.5% for bge-m3 and 24.8% for TF-IDF, against 0.72% for two randomly chosen rulings.

Rulings citing the same provisions cluster about 30 times more than random, but character-level comparison was slightly tighter. On the map reduced to three dimensions, Administrative Litigation Act and Criminal Act rulings form their own clusters, while the 1,040 Civil Act rulings — the largest group — are spread across the whole map.

🔗 Link - https://no1joon.github.io/oh-my-notebooks/legal-rag-map/

## Draft reasoning for hypothetical rulings

I gave the holdings summaries of 50 Supreme Court rulings from the validation split as issues and had the same model write draft reasoning twice for each: once with no grounding, and once with 3 reference rulings retrieved by bge-m3.

![Draft reasoning written without grounding](/assets/images/ai/simple-rag-01-court-rulings/08-term-norag.webp)
*Draft reasoning written without grounding — Source: actual Qwen3-4B output · self-rendered*

The ungrounded draft invented a provision that does not exist and even fabricated its wording in quotation marks. For another issue, it produced a draft citing **Article 12 of the Maritime Transport Act**, which does not exist in Korean law.

![Draft reasoning written with RAG](/assets/images/ai/simple-rag-01-court-rulings/09-term-rag.webp)
*Draft reasoning written with RAG — Source: actual Qwen3-4B output · self-rendered*

With reference rulings in the input, it pointed to the actual referenced provisions: Article 2 of the former River Act and Article 2 of the Act on Special Measures for Compensation for Land Incorporated into Rivers. This issue was an easy retrieval case, because the training split contained a ruling (2011두4336) with an almost identical holdings summary.

![Correct referenced-provision hit rate](/assets/images/ai/simple-rag-01-court-rulings/10-chart.webp)
*Correct referenced-provision hit rate — Source: my own measurement · self-rendered*

| Condition | Provision hits | Drafts with no provisions | Generation time |
| :--- | :--- | :--- | :--- |
| No grounding | 9 | 23 | 5.8s |
| RAG | <mark>16</mark> | 13 | 15.0s |

Of the 50, 8 issues were hit only with RAG and 1 only without grounding. Excluding the one issue with a near-identical ruling, as in the example above, and counting 49, it is still 9 vs. 15.

Retrieval sets the ceiling. The correct provision appeared within the 3 reference rulings for 25 of the 50 issues, so the most RAG could hit in this setup was 50%. Neither condition produced a draft citing a case number absent from the corpus, and RAG took 2.6 times longer to generate because it had to process long reference rulings.

## Terms of use

AI Hub data can be requested only by Korean nationals and downloaded only after approval. The data itself may be used only for AI training, while derivative works built with it (trained services, chatbots, and so on) may be used commercially or non-commercially.

Taking it overseas requires a separate agreement. According to AI Hub's guidance, transmitting it to or storing it on overseas servers or clouds — or training in such environments — also counts as taking it abroad, so it cannot be run on overseas clouds like Colab. That is why I built this exercise on a single local PC.

Providing the data to third parties is also prohibited, so the notebook I'm publishing alongside contains no data. You point it at the folder you requested and downloaded yourself, and run it in local Jupyter.

With the notebook defaults (fp16, batch 16), one run on the same M3 Pro took 55.4 minutes for embedding and 59 minutes end to end, from corpus construction to draft generation.

🔗 Link - https://github.com/No1Joon/oh-my-notebooks/blob/main/notebooks/legal-rag-01.ipynb

## Summary so far

![Part 1 summary](/assets/images/ai/simple-rag-01-court-rulings/11-items.webp)
*Part 1 summary — Source: summary of this post · self-rendered*

## Next

- Part 2: LoRA fine-tuning Qwen3-4B on the same pseudonymized corpus to learn the style of hypothetical rulings
- Part 3: comparing statute hits and generation time for RAG, fine-tuning, and a setup combining both
- Ways to raise the 50% retrieval ceiling: prioritizing judgment summaries and referenced provisions in retrieval, hybrid search

## Sources

- [[AI Hub] Anonymized court-ruling dataset (composition, builders, terms of use)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71968)
- [[AI Hub] Data usage policy (third-party provision, overseas transfer)](https://aihub.or.kr/intrcn/guid/usagepolicy.do?currMenu=151&topMenu=105)
- [[Hugging Face] BAAI/bge-m3 model card (release date, supported languages, max length, license)](https://huggingface.co/BAAI/bge-m3)
- [[arXiv] BGE M3-Embedding (2402.03216)](https://arxiv.org/abs/2402.03216)
- [[Hugging Face] mlx-community/Qwen3-4B-Instruct-2507-4bit (generation model)](https://huggingface.co/mlx-community/Qwen3-4B-Instruct-2507-4bit)
- This post uses the AI Hub anonymized court-ruling dataset, built as a result of a project by the Ministry of Science and ICT and the National Information Society Agency (NIA).
