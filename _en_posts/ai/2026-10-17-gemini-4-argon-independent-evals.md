---
title: "Gemini 4 Argon Independent Evaluations — No. 1 on Vals, 53 on the Intelligence Index"
description: "Independent evaluation results from Vals AI and Artificial Analysis after general availability, and cost per task compared with rival models"
date: 2026-10-17
category: AI
subcategory: News
tags: [google, gemini-4-argon, benchmark, vals-ai, artificial-analysis]
image: /assets/og/en-2026-10-17-gemini-4-argon-independent-evals.png
---

Gemini 4 Argon became generally available on October 13, 2026
Since then, scores from outside evaluators have started coming in
The benchmarks Google published at the September 30 announcement were its own measurements
The results from two independent evaluators diverged
On the Vals AI composite index it ranked **No. 1**
On the Artificial Analysis Intelligence Index it scored <mark>53</mark>, 5 points below the leader's 58

![Gemini 4 Argon's own benchmark table published by Google on September 30](/assets/images/ai/gemini-4-argon-independent-evals/01-photo.webp)
*Gemini 4 Argon's own benchmark table published by Google on September 30 — Source: Google*

## Artificial Analysis Intelligence Index

![Artificial Analysis Intelligence Index comparison by model](/assets/images/ai/gemini-4-argon-independent-evals/en/02-chart.webp)
*Artificial Analysis Intelligence Index comparison by model — Source: self-rendered from the Artificial Analysis leaderboard*

**Artificial Analysis** is an independent evaluator that rolls multiple benchmark results into a single index
Argon scored 53 at the high reasoning setting
Comparing each model's best setting, Claude Opus 5.5 leads with 58
Claude Sonnet 5.5 and Muse Wonder Full tie for second with 56
Argon scores 53, the same as GPT-6 Astra and Claude Fable 5.1

### Cost per task for the 53-point models

![Cost per Intelligence Index task comparison](/assets/images/ai/gemini-4-argon-independent-evals/en/03-chart.webp)
*Cost per Intelligence Index task comparison — Source: self-rendered from the Artificial Analysis leaderboard*

Argon cost about $1.99 (₩2,790) per index task
GPT-6 Astra max, also at 53, cost ₩4,560
Claude Fable 5.1 max cost ₩10,680
<mark>For the same 53 points, it cost 61% of what GPT-6 Astra did</mark>
However, Claude Opus 5.5 at the high setting scored 54 at ₩2,550 per task
Argon isn't the model with the best score for the cost

### Speed

Output speed was 99.5 tokens per second, faster than the comparison median of 86.1 tokens
The first token took **44.7 seconds** to arrive
That's 11 times the comparison median of 3.94 seconds!
It means it spends a long time reasoning before giving an answer

## Vals AI composite index

![Vals AI composite index comparison of the top four models](/assets/images/ai/gemini-4-argon-independent-evals/en/04-chart-vals.webp)
*Vals AI composite index comparison of the top four models — Source: self-rendered from Vals AI model pages*

**Vals AI** evaluates models on work-style tasks such as finance, law, medicine, and coding
Argon ranked <mark>No. 1</mark> with a composite index of 68.90%
Claude Sonnet 5.5 at 67.04% and Opus 5.5 at 66.97% are second and third
Running the full evaluation once with Argon cost about ₩21,950, the lowest
Claude Opus 5.5 cost about ₩45,000

### Rankings by benchmark

| Benchmark | Score | Rank |
| :--- | :--- | :--- |
| Finance Agent v2 | 65.40% | <mark>1st</mark> / 78 |
| IOI (Informatics Olympiad) | 100% | 1st / 44 |
| Code Migration | 68.17% | 2nd / 77 |
| Terminal-Bench 4.0 | 57.58% | 6th / 48 |
| Vibe Code Bench 1-100 | 21.20% | 8th / 25 |
| CUA-bench | 4.83% | **8th** / 9 |

IOI at 100% is the same score as GPT-6 Astra
On **CUA-bench**, which operates a computer by looking at the screen, it placed only 8th of 9 models
Evaluating this benchmark once cost about ₩271,300, also the highest
Sonnet 5.5 scored higher on Code Migration and Vibe Code Bench v1.1

## Google's own numbers vs outside measurements

![Concept image contrasting self-reported benchmarks with independent evaluations](/assets/images/ai/gemini-4-argon-independent-evals/05-agy.webp)
*Concept image contrasting self-reported benchmarks with independent evaluations — Source: concept image · self-generated with agy*

The Terminal-bench 4.0 score Google published for Argon on September 30 was 57.4%
The score Vals AI measured separately was 57.58%, <mark>nearly identical</mark>
In Google's own benchmarks, the leader on this item was Claude Opus 5.5 at 66.4%

🔗 Link - https://blog.naver.com/rottensweetpotato/224429639264

### Real-world reactions

The Kyunghyang Shinmun reported much praise for writing and logical reasoning, with mixed reviews on coding
One Hacker News user said they'd use Argon for every task except coding
There were also complaints that usage limits run out quickly even on simple questions
Google said AI-written code submissions by its internal development teams rose more than 35%
It said cases of reverting code after changes fell by about a third

## Usage in Korea

![Monthly active users of the Gemini app and ChatGPT in Korea](/assets/images/ai/gemini-4-argon-independent-evals/en/06-chart-mau.webp)
*Monthly active users of the Gemini app and ChatGPT in Korea — Source: self-rendered from WiseApp·Retail*

According to WiseApp·Retail, monthly active users of the Gemini app in Korea were 7.72 million in March
By July it had grown by 1.75 million to 9.47 million
Over the following two months it added only 400,000
ChatGPT users in Korea in September were 24.7 million, about <mark>2.5 times</mark> Gemini
In the Gemini app, Argon is available only to Google AI Pro and Ultra subscribers
Google's announcement didn't list the countries where it's available
There are also no public results yet measuring Argon on Korean-language benchmarks (KMMLU and others)

## What to watch next

![Gemini 4 Argon independent evaluation summary card](/assets/images/ai/gemini-4-argon-independent-evals/en/07-items.webp)
*Gemini 4 Argon independent evaluation summary card — Source: self-rendered from Artificial Analysis · Vals AI*

- Cost-per-task rankings after <u>December 1, 2026</u>, when full API pricing applies
- Official results from Arena, a vote-based ranking
- Korean-language benchmarks and the scope of Argon availability in the Gemini app in Korea
- Scores at lower reasoning settings that cut first-token wait time

## Sources

- [[Artificial Analysis] Gemini 4 Argon model page (Intelligence Index, speed, cost)](https://artificialanalysis.ai/models/gemini-4-argon)
- [[Artificial Analysis] Model leaderboard (Intelligence Index and cost per task by model)](https://artificialanalysis.ai/leaderboards/models)
- [[Vals AI] Gemini 4 Argon model page (composite index, rankings by benchmark, cost)](https://www.vals.ai/models/google_gemini-4-argon)
- [[Google] Gemini 4 Argon announcement (own benchmark table, 2026-09-30)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- [[Google] Gemini 4 Argon generally available (2026-10-13)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)
- [[Google] Argon availability in the Gemini app (2026-10-13)](https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/)
- [[Kyunghyang Shinmun] Reactions to Gemini 4 Argon and Korean user numbers (2026-10-14)](https://www.khan.co.kr/article/202610142044005)
- Exchange rate: converted at $1 ≈ ₩1,400
