---
title: "Dead-Simple RAG (2) — LoRA Fine-Tuning on Court Rulings Hits Half as Many Statutes as RAG"
description: "A model LoRA-fine-tuned on the same court-ruling corpus learned only the format, and fell short of RAG at citing the right statutes"
date: 2026-10-02
category: AI
subcategory: Explainer
tags: [lora, fine-tuning, rag, legal-tech, local-llm]
image: /assets/og/en-2026-10-02-simple-rag-02-lora-finetuning.png
---

Using the pseudonymized court-ruling corpus built in Part 1, I **LoRA fine-tuned** Qwen3-4B and had it regenerate draft reasoning for the same 50 legal issues as Part 1. The share of drafts that cited the correct referenced provisions was 12–18% — equal to or lower than Part 1's ungrounded drafts (18%), and about half of RAG (32%).

What it did pick up was the format of the training data. It wrote in the style of a judgment summary, appended a "legal basis" list of provisions at the end, and even included empty tags that existed only in the training data.

[Dead-Simple RAG (1) — A Local RAG Built on Anonymized Court Rulings, Statute Hits 18%→32% (in Korean)](/posts/simple-rag-01-court-rulings/)

![Concept image of fine-tuning on court rulings](/assets/images/ai/simple-rag-02-lora-finetuning/01-hero-agy.webp)
*Concept image of fine-tuning on court rulings — Source: concept image · self-generated with agy*

## Training data

![One training example](/assets/images/ai/simple-rag-02-lora-finetuning/02-term-sft.webp)
*One training example — Source: training set built from AI Hub data · self-rendered*

Of the 16,800 rulings in Part 1's pseudonymized training split, 5,745 had all three of a holdings summary (판시사항), a judgment summary (판결요지), and referenced provisions (참조조문). I randomly picked 2,400 of them and turned each into one question–answer pair.

| Part | Content |
| :--- | :--- |
| System instruction | Same sentence as Part 1 |
| User question | Part 1 instruction + **holdings summary** |
| Answer | First 900 characters of the judgment summary + **referenced provisions** |

The question was built to match Part 1's no-grounding condition down to the character. The 50 Supreme Court rulings from the validation split used for Part 1's evaluation were excluded from both the training data and the 50 validation examples used to measure loss during training.

The instruction asks for a **400-character draft of the reasoning**, but the answer is a judgment summary, so the question and answer formats differed from the start. The median answer length was 704 characters; all 2,400 end with a **legal basis** list, and 359 of them list more than 15 provisions.

## LoRA training

LoRA is a method published by Microsoft researchers in 2021 that freezes the original model's weights and trains only two small matrices added to each layer. The paper reported cutting trainable parameters by 10,000 times and GPU memory to one third, for GPT-3 175B.

| Item | Value |
| :--- | :--- |
| Trainable parameters | **7.34M (0.182%)** |
| Layers applied | Top 16 of 36 |
| rank | 8 |
| Learning rate | 0.0001 |
| Batch | 1 example × 4 accumulation steps |
| Steps | 2,400 (one pass over the data) |
| Max length | 1,024 tokens |

![Running mlx_lm LoRA training](/assets/images/ai/simple-rag-02-lora-finetuning/03-term-train.webp)
*Running mlx_lm LoRA training — Source: actual mlx_lm output · self-rendered*

I trained with MLX on the same Apple M3 Pro 36GB as Part 1. To keep the machine usable for other work, I made it sleep for as long as each step took to compute; with that setting, one training pass took 5 hours 52 minutes.

Peak memory was 3.99GB, and 1.72 million tokens were trained. The resulting adapter file is 29.4MB and is applied on top of the 4-bit base model.

### Loss curve

![Training loss averaged over 400-step windows](/assets/images/ai/simple-rag-02-lora-finetuning/04-chart.webp)
*Training loss averaged over 400-step windows — Source: own measurement · self-rendered*

Validation loss fell from 2.401 to 1.072. Training loss went from an average of 1.264 over the first 400 steps to 1.033 over the last 400, with most of the drop concentrated in the first 400 steps.

By default, mlx_lm includes not just the answer but the question part in the loss (**--mask-prompt** not used). Since all 2,400 examples share the same instruction, part of the loss drop comes from the model learning to predict that same sentence every time.

## Rewriting the same 50

I fed the holdings summaries of the 50 Supreme Court rulings in the validation split with the same instruction as Part 1 and had it write draft reasoning without reference rulings. As in Part 1, decoding was greedy — always choosing the most probable token, no randomness — with a 600-token output limit.

### The repetition problem

![Output cut off while repeating provision numbers](/assets/images/ai/simple-rag-02-lora-finetuning/05-term-loop.webp)
*Output cut off while repeating provision numbers — Source: actual Qwen3-4B + LoRA output · self-rendered*

49 of the 50 hit the 600-token limit. Most of them kept generating "Article n, Paragraph 1, Item 1," with only the number changing in the **legal basis** section until they were cut off at the limit, which pushed the median generation time to 18.5 seconds — three times Part 1's no-grounding condition (5.8 seconds).

This output did include the correct provision, Article 34, in the middle of the list, but it wasn't counted as a hit. As in Part 1, scoring only counts cases where the statute name and article number appear together.

Running the same three issues on the checkpoint at 1,200 steps, midway through training, produced the same repetition.

### Suppressing repetition

I ran the same 50 once more with a **repetition penalty**, which lowers the scores of tokens that have already appeared. This is the method from Salesforce's 2019 CTRL paper, which suggested a value around 1.2 for use with greedy decoding; here I applied 1.1 over the most recent 64 tokens.

Hits on the limit dropped to 26. The 24 that finished had a median length of 341 characters, close to the instruction's 400.

## Statute hits

![Share of drafts citing the correct referenced provisions](/assets/images/ai/simple-rag-02-lora-finetuning/06-chart.webp)
*Share of drafts citing the correct referenced provisions — Source: own measurement · self-rendered*

| Condition | Drafts with no provision | Generation time |
| :--- | :--- | :--- |
| No grounding | 23 | 5.8 s |
| RAG | <mark>13</mark> | 15.0 s |
| LoRA | 31 | 18.5 s |
| LoRA + repetition penalty | 18 | 18.3 s |

The fine-tuned model got 6 issues right, and 9 with the repetition penalty. That is the same 9 as Part 1's ungrounded drafts, but only 6 issues overlap, and 6 of the 9 the penalized run got right were issues RAG also got right.

When a parenthetical like **(prior to the amendment by Act No. 6311 on Dec. 29, 2000)** sits after the statute name, it drops out of scoring; allowing those and recounting gave LoRA 8, repetition penalty 10, no grounding 9, and RAG 16 — the same order.

No draft in either condition cited a case number that isn't in the corpus.

### Confidently citing the wrong law

![Output that attached Criminal Act provisions to a copyright issue](/assets/images/ai/simple-rag-02-lora-finetuning/07-term-wronglaw.webp)
*Output that attached Criminal Act provisions to a copyright issue — Source: actual Qwen3-4B + LoRA output · self-rendered*

The conclusion, which spells out the "(affirmative)" at the end of the holdings summary as "the complaint is lawful," is correct. The judgment summaries in the training data restate the holdings summary's conclusion as a declarative sentence, so this conversion is exactly the form seen in training.

But as its legal basis it cited Criminal Act Articles 297 and 305, which have nothing to do with a copyright case. For the same issue, Part 1's no-grounding condition cited Copyright Act Article 111, outside the correct answer, and the RAG condition cited the correct Copyright Act Article 52.

## The format it learned

| Output feature (out of 50) | LoRA | LoRA + repetition penalty |
| :--- | :--- | :--- |
| Legal basis list | 22 | <mark>39</mark> |
| Issue sentence included verbatim | 27 | 24 |
| Empty think tag | **50** | **50** |
| Hit 600 tokens | 49 | 26 |

In Part 1's two conditions, the legal basis list and empty tags appeared 0 times, and verbatim issue sentences and 600-token hits appeared once each, on the RAG side. "Issue sentence included" means the first 40 characters of the holdings summary appear as-is in the output.

The outputs did not simply copy the training data. Splitting outputs into 20-character chunks and measuring overlap with the 2,400 training answers gave a median of 0–1%.

### The empty think tag

![Empty think tag in the training data](/assets/images/ai/simple-rag-02-lora-finetuning/08-term-think.webp)
*Empty think tag in the training data — Source: actual Qwen3 chat template output · self-rendered*

Qwen3-4B-Instruct-2507's model card says it "operates without thinking mode and does not output **<think></think>** blocks." None of Part 1's 100 outputs had this tag either.

The chat template that converts training data into conversation format added an empty tag before every answer, while the evaluation prompt ends at the **assistant** line with no tag. Having learned it from 2,400 examples, the model started writing the tag itself at the beginning of its output.

## Research on fine-tuning and knowledge

![Gekhman et al., abstract of the paper on fine-tuning and new knowledge](/assets/images/ai/simple-rag-02-lora-finetuning/09-paper-gekhman.webp)
*Gekhman et al., abstract of the paper on fine-tuning and new knowledge — Source: arXiv / Gekhman et al. (CC BY 4.0)*

Researchers at Technion and Google Research reported that examples containing facts the model didn't know from pretraining are learned much later than examples of known facts, and once they are learned, the tendency to hallucinate rises linearly with them (EMNLP 2024). Their conclusion is that factual knowledge comes mainly from pretraining, and fine-tuning teaches how to use that knowledge.

![Ovadia et al., results table for the current-events task](/assets/images/ai/simple-rag-02-lora-finetuning/10-paper-ovadia.webp)
*Ovadia et al., results table for the current-events task — Source: arXiv / Ovadia et al. (CC BY 4.0)*

Microsoft researchers compared fine-tuning and RAG on a multiple-choice task about events after the training cutoff (EMNLP 2024). Mistral 7B's accuracy was 0.481 base, 0.504 fine-tuned, and 0.875 with RAG; adding RAG to the fine-tuned model gave 0.810, lower than RAG alone.

Fine-tuning in that paper means further training on raw Wikipedia text rather than question–answer pairs, so it differs from the setup here. The paper also reported that training on data that restates the same facts in multiple phrasings raises accuracy.

Meta's LIMA study (2023), which tuned a 65B model on 1,000 question–answer pairs, proposed the **superficial alignment hypothesis**: knowledge comes mostly from pretraining, and tuning shapes the response format. What changed after 2,400 court rulings here was likewise the judgment-summary style and the legal basis list.

In Korea, the Supreme Court began a pilot of **trial-support AI** running on the courts' internal infrastructure on February 13, 2026. It searches precedents, statutes, and practice manuals to organize the issues, and shows the supporting precedents and statutes alongside — without relying on public AI services.

## Summary so far

![Part 2 summary](/assets/images/ai/simple-rag-02-lora-finetuning/11-items.webp)
*Part 2 summary — Source: summary of this post · self-rendered*

## Next

- Part 3: statute hits and generation time for a setup combining RAG and LoRA
- Changed training conditions: **--mask-prompt** to exclude the question from the loss, answers in the same format as the instruction, and a template with the empty tag removed

[Dead-Simple RAG (1) — A Local RAG Built on Anonymized Court Rulings, Statute Hits 18%→32% (in Korean)](/posts/simple-rag-01-court-rulings/)

## Sources

- [[arXiv] LoRA: Low-Rank Adaptation of Large Language Models (2106.09685, trainable parameters and memory savings)](https://arxiv.org/abs/2106.09685)
- [[arXiv] Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations? (2405.05904, source of one image in this post)](https://arxiv.org/abs/2405.05904)
- [[arXiv] Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs (2312.05934, source of one image in this post)](https://arxiv.org/abs/2312.05934)
- [[arXiv] LIMA: Less Is More for Alignment (2305.11206, superficial alignment hypothesis)](https://arxiv.org/abs/2305.11206)
- [[arXiv] CTRL: A Conditional Transformer Language Model for Controllable Generation (1909.05858, repetition penalty)](https://arxiv.org/abs/1909.05858)
- [[GitHub] mlx-lm LoRA docs (--mask-prompt default, chat template application)](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md)
- [[Hugging Face] Qwen/Qwen3-4B-Instruct-2507 model card (no thinking mode)](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)
- [[Hankyung] Courts pilot in-house AI trial support (2026-02-13)](https://www.hankyung.com/article/202602134488i)
- [[AI Hub] Anonymized court ruling dataset](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71968)
- This post uses the AI Hub anonymized court ruling dataset, built as a result of a project by the Ministry of Science and ICT and the National Information Society Agency.
