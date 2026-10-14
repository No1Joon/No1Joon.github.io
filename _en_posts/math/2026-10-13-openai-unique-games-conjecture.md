---
title: "An OpenAI Internal Model's Proof of the Unique Games Conjecture — Lean Passed, Human Verification Pending"
description: "What the Unique Games Conjecture proof among OpenAI's released math manuscripts claims, and how far it has been verified"
date: 2026-10-13
category: Math
subcategory: Explainer
tags: [unique-games-conjecture, ai-math, lean, complexity-theory, openai]
image: /assets/og/en-2026-10-13-openai-unique-games-conjecture.png
---

On October 6, 2026, OpenAI released a large batch of math manuscripts produced by an unreleased internal model, and among them is a proof of the Unique Games Conjecture, a flagship open problem in theoretical computer science.

The proof comes with formalization in Lean, a proof assistant in which a computer checks the logic line by line. But it hasn't yet reached the stage where human experts have reviewed the manuscript and confirmed it correct. Scott Aaronson wrote on his blog that almost no humans have properly understood the proof yet.

![Abstract on the first page of OpenAI's manuscript The Unique Games Theorem](/assets/images/math/openai-unique-games-conjecture/01-capture.webp)
*Abstract on the first page of OpenAI's manuscript The Unique Games Theorem — Source: OpenAI*

## What was released

The release is the openai/math repository on GitHub. As of October 7, 2026, it holds 719 manuscripts divided into 372 result families, and about 4,000 problems were given to the model. OpenAI said each result used, on average, compute equivalent to ChatGPT Pro reasoning for about 3 hours.

- Family 102: 5 manuscripts including the Unique Games Conjecture proof and approximation limits for Max-Cut and Vertex Cover
- Family 105: proof of Khot's 2-to-1 games conjecture (perfect completeness version)
- Others include the matrix multiplication exponent, zero-free regions of the Riemann zeta function, and special cases of the Hodge conjecture
- According to OpenAI's repository notes, most manuscripts are raw model output not edited by humans

The numbers differ across reports because of when they were counted. There were 722 manuscripts at first release, and 3 were withdrawn a day later, leaving 719. The 372 is the number of families, not manuscripts.

## What the Unique Games Conjecture asks

Suppose you assign one color (label) to each vertex of a graph, and each edge carries a rule like "if this end is color a, the other end must be color b." Once one end's color is set, the other end's color is uniquely determined, hence the name unique games.

![Timeline from the 2002 conjecture to OpenAI's 2026 release](/assets/images/math/openai-unique-games-conjecture/en/02-chart.webp)
*Timeline from the 2002 conjecture to OpenAI's 2026 release — Source: self-rendered from Khot's original paper, Quanta Magazine, and openai/math*

The conjecture Subhash Khot proposed in 2002 as a graduate student is this: even distinguishing problems where 99% of the rules can be satisfied from problems where not even 1% can be satisfied is impossible in polynomial time (NP-hard). It means that even for problems where almost all rules can be satisfied, telling so is hard.

For Max-Cut, the problem of splitting a graph's vertices into two sets to maximize the number of edges between them, the Goemans–Williamson algorithm developed in 1995 guarantees up to about **87.8%** of the optimum. Research in 2004 established that if the Unique Games Conjecture is true, there's no better polynomial-time algorithm, and likewise Vertex Cover's factor-2 approximation can't be improved.

In 2018, Khot, Dor Minzer, and Muli Safra proved the 2-to-2 theorem, the first major step toward proving this conjecture. Still, the conjecture itself went unproven for 24 years.

## Lean verification and human verification

The Lean documentation for family 102 states the formalized statement as follows: for any ε and δ between 0 and 1/2, there is a deterministic polynomial-time reduction from 3SAT to unique games such that satisfiable inputs have value at least 1−ε and unsatisfiable inputs have value at most δ.

![Gauge of the share of openai/math representative results formalized in Lean](/assets/images/math/openai-unique-games-conjecture/en/03-chart-lean.webp)
*Gauge of the share of openai/math representative results formalized in Lean — Source: self-rendered from the openai/math repository*

Lean mechanically checks whether the proof logically derives that statement. If the proof assistant accepted it, the chance of a logical error in the proof is greatly reduced. What remains to review is the formal statement.

| Question | Does Lean answer it |
| :--- | :--- |
| Does the proof derive the formal statement | <mark>Yes</mark> |
| Is the formal statement the same as Khot's conjecture | **Checked by humans** |
| Is the definition of polynomial time standard | Checked by humans |
| Does the manuscript's explanation match the Lean proof | Checked by humans |

The formal statement has to formalize the encoding of 3SAT inputs, the machine model, and the time bounds as Lean definitions, so it is long and detailed. If even one definition differs subtly from the standard, Lean verification can pass while the result is a different theorem from the conjecture mathematicians mean. As with the Astra case covered on August 13, formalization is the first verification step, and the conclusion comes only after the statement is reviewed.

[AI Solved a 27-Year-Old Math Problem — Anyone Can Verify It (in Korean)](/posts/astra-math-lean-proofs/)

Across the whole repository, only 300 of the 719 representative results, about 42%, have Lean formalizations. The remaining 58% are manuscripts only, and OpenAI also notes in the repository guide that unformalized results may have problems.

## How mathematicians reacted

In a blog post the day after the release, Aaronson called it one of the biggest days in the history of mathematics, but wrote that hardly any humans understand the proof and that a race to understand it has just begun. His spouse Dana Moshkovitz, who has long studied the Unique Games Conjecture, said the manuscript was written so roughly that it was hard to read without AI help, and reportedly understood most of the proof with AI assistance.

According to Quanta Magazine, MIT's Dor Minzer heard rumors on September 11 that OpenAI had found a proof, and three days later, with graduate students Yumou Fei and Shuo Wang, posted a 95-page paper on a 4-to-1 form weaker than the 2-to-1 conjecture. Minzer said they rushed so much that after Section 6 there isn't a single connecting sentence.

Princeton's Mark Braverman said announcing mathematical results by press release isn't healthy, and that even AI proofs aren't verified by a single announcement.

On October 7, OpenAI withdrew 3 manuscripts — one on abelian varieties with a sign error and 2 built on it — and revised 14 others to patch their proofs. It's a different field from the unique games manuscripts, but it shows how hard it is to trust unformalized manuscripts as they are.

## What to check next

![Summary card of the Unique Games Conjecture proof claim](/assets/images/math/openai-unique-games-conjecture/en/04-items.webp)
*Summary card of the Unique Games Conjecture proof claim — Source: self-rendered from openai/math and Quanta Magazine*

- A human-rewritten exposition of the unique games manuscript and the results of external expert review
- Review of whether the definitions in the Lean formal statement match the standard definitions
- Whether it's submitted to a conference or journal, and whether family 102 appears in the revision history OpenAI mentioned
- Clarifying the relationship between the Minzer team's 4-to-1 paper and OpenAI's 2-to-1 result

## Sources

- [[OpenAI] openai/math repository README and history (manuscript count, Lean share, withdrawals; source of 1 image in the body)](https://github.com/openai/math)
- [[OpenAI] Scope of the Lean formalization for family 102](https://github.com/openai/math/blob/main/lean/docs/102.md)
- [[OpenAI Developer Community] First look at mathematics manuscripts from an internal frontier model (2026-10-06)](https://community.openai.com/t/first-look-at-mathematics-manuscripts-from-an-internal-frontier-model-at-openai/1403886)
- [[Quanta Magazine] As AI Closed In on Unique Games Proof, Researchers Raced to Beat the Machines (2026-10-07)](https://www.quantamagazine.org/as-ai-closed-in-on-unique-games-proof-researchers-raced-to-beat-the-machines-20261007/)
- [[Shtetl-Optimized] Scott Aaronson, The Mathocalypse (2026-10-07)](https://scottaaronson.blog/?p=10169)
- [[Wikipedia] Unique games conjecture (background, connection to Max-Cut)](https://en.wikipedia.org/wiki/Unique_games_conjecture)
