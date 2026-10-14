---
title: "The Condition-Number Barrier in Sparse Least Squares — A Gemini Agent Found the Proof First"
description: "The sparse regression conjecture addressed by a Google paper, and how a Gemini-based agent found the proof first and humans verified it"
date: 2026-10-07
category: Math
subcategory: Explainer
tags: [sparse-regression, least-squares, ai-math, gemini, theorem-proving]
image: /assets/og/en-2026-10-07-sparse-least-squares-ai-proof.png
---

At the end of the abstract of a paper three Google Research researchers posted to arXiv on August 3, there is this sentence: the proof was first derived by a fully automated Gemini-based agent system inside Google, and the authors verified it and edited it for readability.

What it proves is a conjecture left by Axiotis and Sviridenko in 2021: for regression problems that use few variables, there is no polynomial-time algorithm clearly better than the current algorithm.

![Paper title, authors, and abstract, with the AI contribution sentence highlighted](/assets/images/math/sparse-least-squares-ai-proof/01-hero-abstract.webp)
*Paper title, authors, and abstract, with the AI contribution sentence highlighted — Source: arXiv*

## Paper details

| Item | Details |
| :--- | :--- |
| Title | *The Condition-Number Barrier in Sparse Least Squares* |
| Authors | Honghao Lin · Vahab Mirrokni · David P. Woodruff |
| Affiliation | **Google Research**, Carnegie Mellon University |
| Posted | arXiv, August 3, 2026 (cs.DS) |
| Type | <mark>Theoretical proof paper, not yet peer-reviewed</mark> |

It's a purely theoretical paper with no experiments or measurements. It is 17 pages long, and as a preprint that hasn't been through journal or conference review, the correctness of the proof has only been checked as far as the authors' own verification.

## The problem the paper addresses

![The history of research on the number of variables in sparse least squares](/assets/images/math/sparse-least-squares-ai-proof/en/02-chart.webp)
*The history of research on the number of variables in sparse least squares — Source: self-rendered from arXiv 2608.02588 and 2609.15983*

**Least squares** is a method that finds the coefficients that best fit the data by minimizing the sum of squared errors. Adding a **sparse** condition means using at most k nonzero coefficients, which turns it into a variable selection problem: choosing just a few of thousands of variables that explain the result.

Natarajan showed in 1995 that finding the optimal solution with exactly k variables is NP-hard. So researchers relaxed the condition: achieve nearly the same error (within ε) as the optimal k-variable solution, but allow using more than k variables. The question is **how many more variables you need**.

The value that governs the number of variables needed is the **restricted condition number** κ. It describes how similar the variables are to each other and how hard they are to tell apart: 1 means the variables are independent, and larger means harder to distinguish.

| Period | Variables needed | Result |
| :--- | :--- | :--- |
| Around 2010 | k × κ² | Upper bound |
| 2021 | <mark>k × κ</mark> | Axiotis–Sviridenko upper bound |
| 2021 conjecture | k × κ¹⁻ᵞ impossible | Conjecture 27 |

Axiotis and Sviridenko built an algorithm using k × κ variables and conjectured that it can't be done in polynomial time with k × κ¹⁻ᵞ variables, lowering the exponent even slightly below 1 (γ is a constant greater than 0 and at most 1). There were examples where specific algorithms failed, but no lower-bound proof that applies to all polynomial-time algorithms.

## The paper's conclusion

![The paper's main theorem, Theorem 1.1](/assets/images/math/sparse-least-squares-ai-proof/03-theorem.webp)
*The paper's main theorem, Theorem 1.1 — Source: arXiv*

The main theorem proves that this conjecture holds for the least squares problem. It states that no randomized polynomial-time algorithm can, with probability at least 2/3, find a solution that satisfies both conditions below.

**‖Ax − b‖² ≤ (error of the optimal k-variable solution) + ε**

**s ≤ C · k · κ¹⁻ᵞ**

Here s is the number of variables the algorithm uses. However, the proof is **conditional**. It assumes that the **Small-Set Expansion Hypothesis**, which concerns graphs, is true. This hypothesis is an unproven conjecture that you can't distinguish in polynomial time whether a graph has a small subset with few connections to the outside, and it arose from research related to the Unique Games Conjecture.

The proof is a reduction. It reduces the graph problem the hypothesis considers hard to a least squares problem, and shows that if there were an algorithm solving it with fewer variables than the conjecture allows, that graph problem could also be solved, deriving a contradiction. Because each edge of the graph becomes one row of the matrix A, the hard instances are simple matrices with **at most two nonzero values per row**. The conclusion also holds when the coefficients are rational and A has full column rank.

## What the AI did and what the humans did

![The AI contribution sentence in the acknowledgements](/assets/images/math/sparse-least-squares-ai-proof/04-acknowledgements.webp)
*The AI contribution sentence in the acknowledgements — Source: arXiv*

The paper states the contribution in two places. The abstract and the acknowledgements begin with the same sentence, and the acknowledgements add one more phrase.

| Party | Work described in the paper |
| :--- | :--- |
| Gemini-based agent | <mark>Found the proof first (fully automated)</mark> |
| The 3 authors | Verified the proof |
| The 3 authors | Edited it for readability |
| The 3 authors | **Responsible for the final version** |

This paper doesn't say what the agent was. The *Stellar Colosseum* paper the same authors posted to arXiv on September 15 provides related information. Introducing a multi-agent harness for research in mathematics and theoretical computer science, that paper includes this lower-bound proof as one of five research results the harness contributed to.

![Stellar Colosseum's stage-by-stage research flow](/assets/images/math/sparse-least-squares-ai-proof/05-colosseum-workflow.webp)
*Stellar Colosseum's stage-by-stage research flow — Source: arXiv*

Colosseum proceeds in five stages: exploring proof strategies, judging readiness, splitting the proof into sections, solving each section, and verifying the whole. At each stage it produces several candidate answers, a refuter role that looks for counterexamples checks each candidate, and the candidates that pass are merged. The authors ran the harness with Gemini 3.1 Pro and reported 71.0% accuracy on TCS-Bench, a benchmark of research-level theorem proofs drawn from FOCS, STOC, and SODA papers.

Choosing the problem, checking that the proof is correct, and publishing and taking responsibility for the paper were done by humans. Conversely, what the paper's sentence means is that humans didn't intervene in the step of finding the proof's key idea.

## Scope and limitations stated by the authors

The paper doesn't have a separate section on limitations. Instead, the body clearly defines the scope of the result.

- The proof is a conditional result that assumes the Small-Set Expansion Hypothesis
- It covers the least squares objective; the original conjecture covers sparse convex optimization in general
- The lower bound applies to polynomial-time algorithms, not exponential-time algorithms
- It's a worst-case lower bound, unrelated to cases where algorithms do well on real data

From here on is this post's view. The proof hasn't been peer-reviewed, and the fact that an AI found the proof doesn't lighten the verification burden. The Colosseum paper also cites, as a reason for designing the harness, that in long proofs errors in earlier steps can propagate to later steps.

## Connection to Korea

No Korean researchers took part in this paper. The practical connection is sparse regression itself. Korean companies and research institutes use techniques like LASSO and OMP for work that selects a few of thousands of variables, such as genome analysis, financial risk factor selection, and feature selection for recommendation models. This result adds grounds to the claim that, within polynomial time, those algorithms can't avoid selecting more variables in proportion to κ in the worst case.

## What to check next

- Passing conference or journal review and external verification
- Whether the result's scope extends to sparse convex optimization beyond least squares
- Whether a result appears proving the same lower bound without the Small-Set Expansion Hypothesis
- Review outcomes for the other four results Colosseum contributed to

## Sources

- [[arXiv] Lin, Mirrokni, Woodruff, The Condition-Number Barrier in Sparse Least Squares, arXiv:2608.02588 (2026-08-03; source of 3 images in the body)](https://arxiv.org/abs/2608.02588)
- [[arXiv] Lin, Woodruff et al., Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science, arXiv:2609.15983 (2026-09-15; source of 1 image in the body)](https://arxiv.org/abs/2609.15983)
- [[Journal of Machine Learning Research] Axiotis, Sviridenko, Sparse convex optimization via adaptively regularized hard thresholding, 22(122), 2021 (original Conjecture 27)](https://jmlr.org/papers/v22/20-661.html)
