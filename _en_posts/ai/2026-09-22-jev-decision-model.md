---
title: "Jev — A Decision Model That Outputs Probabilities Instead of Sentences"
description: "The structure and benchmarks of Jev, which returns per-option probabilities and a confidence score, and what it gave up for speed and cost"
date: 2026-09-22
category: AI
subcategory: Explainer
tags: [jev, typesafe-ai, decision-model, classification, llm]
image: /assets/og/en-2026-09-22-jev-decision-model.png
---

TypeSafe AI, founded by a researcher who worked on ChatGPT, unveiled a model called Jev on September 15, 2026. Give it a question and it returns not a sentence but **per-option probabilities and a confidence score**.

The company says it is 40–200 times faster and 40–400 times cheaper than existing LLMs (large language models), and on Vercel AI Gateway about 13% of paying teams called the model within 24 hours of release.

![Official TypeSafe AI key visual](/assets/images/ai/jev-decision-model/01-hero-typesafe.webp)
*Official TypeSafe AI key visual — Source: TypeSafe AI*

## What Jev is

![Concept image of a decision model that picks one of a fixed set of options instead of generating sentences](/assets/images/ai/jev-decision-model/02-agy.webp)
*Concept image of a decision model that picks one of a fixed set of options instead of generating sentences — Source: concept image · self-generated with agy*

TypeSafe AI was founded in San Francisco in 2024, and its CEO is Diogo Almeida, who spent about four years at OpenAI working on RLHF (reinforcement learning from human feedback) for InstructGPT, ChatGPT, and GPT-4. Jev is the first model from two years of development with nothing shown publicly, and alongside the release the company announced a **$40 million (₩56 billion)** seed round led by DCVC.

The company calls this family *System One Models*, after Daniel Kahneman's split in *Thinking, Fast and Slow* between the fast, intuitive System 1 and the slow, deliberate System 2. The name Jev comes from William Stanley Jevons, the 19th-century economist behind the Jevons paradox, in which greater efficiency leads to more consumption rather than less.

| Item | Details |
| :--- | :--- |
| Developer | TypeSafe AI (US) |
| Release | September 15, 2026, waitlist |
| Seed round | $40 million (₩56 billion), led by DCVC |
| Input price | **₩59 per million tokens** |
| Output price | Free |
| Input per request | Up to 64k tokens |
| Current version | jev-1.13.0 |

The weights are not published, so you cannot install and run it yourself; you call it through a hosted route such as the TypeSafe API or Vercel AI Gateway.

## How requests and responses are structured

![The security incident workflow TypeSafe published, with questions attached to four stages: classification, handling, isolation, and response](/assets/images/ai/jev-decision-model/03-photo.webp)
*The security incident workflow TypeSafe published, with questions attached to four stages: classification, handling, isolation, and response — Source: TypeSafe AI*

An LLM builds a sentence by appending one token (a piece of text the model processes) after another. Jev does not build sentences; it picks values within an answer template (a schema) the developer wrote in advance. There are three question formats.

| Format | What it asks | What it returns |
| :--- | :--- | :--- |
| Choice | Pick one from a list | <mark>Option, probability, confidence</mark> |
| Score | Rate it on a scale | Grade, probability, confidence |
| Noul | Is this statement true | A probability between 0 and 1 |

Choice takes up to 255 options, and several questions in one request are evaluated in parallel against the same input (**state**). The security incident workflow TypeSafe published splits a single alert into four stages — classification, handling, isolation, and response procedure — with a pick, score, or true/false question at each stage.

The example in the official documentation routes a customer inquiry to the right team. A sentence saying the sneakers came in the wrong size and asking to swap for a size 10 goes into **state**, and descriptions of three teams — returns, shipping, and billing — are given as options.

💻 [Source code: A Jev Choice request (abridged official example)]

    from typesafe_sdk import (
        Choice, TypeSafeClient)

    with TypeSafeClient() as client:
      r = client.system_one(
        state="Wrong size. Swap for 10?",
        questions={"dept": Choice(
          instructions="Which team?",
          criteria={
            "returns": "Exchanges",
            "shipping": "Delivery",
            "billing": "Payments",
          })})
      print(r.answers["dept"].choice)

The official example's response is **choice: returns** with **confidence: 1.0**, and the probabilities were returns 1.0, shipping 0.0, billing 0.0.

Confidence is computed from whether the probability is concentrated on one option or spread out. In an example cited by MarkTechPost, billing led at 0.84 but technical support took 0.159, leaving confidence at just 0.596. Independently of the answer, your code can read this value to decide whether to process automatically or hand off to a human reviewer.

## Speed and cost

![Average time for one pass across four workflows, Jev and seven LLMs](/assets/images/ai/jev-decision-model/en/04-chart.webp)
*Average time for one pass across four workflows, Jev and seven LLMs — Source: self-rendered from TypeSafe AI Workflow Evals*

TypeSafe says a round trip takes **70–500 milliseconds**, while the LLMs it compared took 3 to 329 seconds on the same workflows. The model architecture is not published, but the company explained that instead of generating tokens one at a time (autoregressive), it uses a parallel sampler that produces all output at once. The output is only option names and a few probabilities, so there are no sentences to generate.

Training used synthetic data only, and instead of RLHF the company says it used RLCD (Reinforcement Learning for Calibrated Decisions) to make the probabilities the model reports match actual accuracy. In one official demo reported by The Register, Jev took 0.114 seconds and ₩0.11 while GPT-5.6 Terra took 8.566 seconds and ₩19.4.

| Model | Input (₩ per million tokens) | Output (₩ per million tokens) |
| :--- | :--- | :--- |
| Jev | **59** | <mark>0</mark> |
| GPT-5.6 Luna | 280 | 1,680 |
| GPT-5.6 Terra | 2,800 | 16,800 |
| GPT-5.6 Sol | 7,000 | 42,000 |

Because output is free, cost is set by input length alone. Input per request goes up to 64k tokens, with rate limits of 1,200 requests per minute and 250,000 tokens per second. TypeSafe wrote directly in its announcement that it cannot promise these prices will hold for long.

## The official benchmark figures

![Scatter plot of average accuracy and cost per pass across four workflows, for Jev, OpenAI, Anthropic, and DeepSeek models](/assets/images/ai/jev-decision-model/05-photo.webp)
*Scatter plot of average accuracy and cost per pass across four workflows, for Jev, OpenAI, Anthropic, and DeepSeek models — Source: TypeSafe AI*

TypeSafe compared models on four workflows: security incident classification, reviewing agent execution logs, invoice processing, and customer support. The ground-truth labels came from running GPT-6 Astra and Claude Fable 5.1 at high reasoning settings and taking the answers the two models agreed on.

| Model | Average accuracy (%) | Cost per pass (₩) |
| :--- | :--- | :--- |
| Jev | 67.8 | **0.56** |
| GPT-5.6 Terra | 67.9 | 42.6 |
| GPT-5.6 Luna | 66.8 | 4.6 |
| GPT-5.6 Sol | <mark>74.1</mark> | 117 |
| Claude Opus 5 | 73.1 | 246.5 |
| DeepSeek V4 Flash | 64.4 | 8.3 |

On average accuracy Jev is level with GPT-5.6 Terra, 0.1 percentage points apart, and 6.3 points below the leader GPT-5.6 Sol. A ZDNet Korea column pointed out that the **193.6 times faster and 444.6 times cheaper** figures on the homepage are multiples against the slowest and most expensive comparison; against Terra, which matches it on accuracy, it is **about 25 times faster and 76 times cheaper**.

### Variation by task

![Jev's accuracy gap against the leading LLM by task](/assets/images/ai/jev-decision-model/en/06-chart.webp)
*Jev's accuracy gap against the leading LLM by task — Source: self-rendered from TypeSafe AI Workflow Evals*

On customer support, Jev scored 76.0% against the leader GPT-5.6 Sol's 78.3%, a 2.3-point gap, but on invoice processing Jev scored 61.8% against Sol's 79.1% — a **17.3-point** gap. Security incident classification was 4.5 points behind Claude Opus 5 (66.2%), and agent log review 5.0 points behind Sol (76.6%).

TypeSafe stated in its announcement that these workflows were built by its own model capability staff, that the demo ran on a laptop on the US West Coast, and that the multiples it presented are an optimistic reading of the real gain. It also wrote that since the comparison set is mostly OpenAI and Anthropic models, performance relative to DeepSeek may be understated.

## Adoption and uses

![Paying-team adoption within 24 hours of release on Vercel AI Gateway, Jev against recent models](/assets/images/ai/jev-decision-model/07-photo-vercel.webp)
*Paying-team adoption within 24 hours of release on Vercel AI Gateway, Jev against recent models — Source: Vercel*

In a September 18 blog post, Vercel said Jev reached 10% of paying teams 18 hours after release on AI Gateway and about 13% within 24 hours. That is roughly twice the GPT-5.6 family's rate over the same period and more than six times Claude Fable 5.1's, and it is free on the gateway through September 25.

Vercel CEO Guillermo Rauch wrote on X that he swapped the safety review step that inspects every command in the automatic mode of the company's fx tool from GPT-5.6 Luna to Jev, and saw up to an 18x speedup at p95 along with higher accuracy. The measurement method was not published.

The uses the official documentation and Vercel point to are repeated judgments with a fixed set of answers.

- Routing customer inquiries and tickets to the right team
- Picking the next tool or sub-agent for an agent to call
- Moderating posts and assigning risk scores
- Guardrails that check whether another LLM's output followed the rules

### Branching on confidence

The official documentation recommends using confidence as a criterion separate from the answer: send anything below 0.6 to human review, and raise the bar for automatic processing as the cost of being wrong grows.

| Confidence | Balance inquiry | Money transfer |
| :--- | :--- | :--- |
| Above 0.85 | Automatic | <mark>Automatic</mark> |
| 0.6–0.85 | Automatic | **User confirmation** |
| Below 0.6 | Human review | Human review |

## Limits and counterarguments

![Structured output error rate and tool call error rate, Jev at 0%](/assets/images/ai/jev-decision-model/08-photo.webp)
*Structured output error rate and tool call error rate, Jev at 0% — Source: TypeSafe AI*

### What the 0% hallucination claim covers

TypeSafe reports Jev's structured output error rate and tool call error rate as 0%. That means it cannot produce an answer outside the list or a malformed value; it does not mean the probability of picking the wrong option is zero. MarkTechPost likewise explained that this 0% is not a measurement but a statement that schema conformance is guaranteed — and the same model's average workflow accuracy is 67.8%.

### Verifying the calibration

RLCD's central claim is calibration: that a judgment reported at 0.85 is actually right about 85% of the time. As of release there were no calibration curves, no figures such as ECE (expected calibration error), and no paper, and the question went unanswered in the launch thread on Hacker News.

### How it differs from a classifier

On Hacker News and Reddit the reaction was to ask how this differs from existing zero-shot classification models. A KDnuggets column argued that classification and intent detection are old problems, and what TypeSafe built is a new structure and developer experience for solving them. Within a week of release, an open-source Kev (0.8B, 4B, 9B) built on Qwen3.5 that follows Jev's response format, along with a comparison benchmark JevBench, were also released.

### Bias that scores alone make hard to check

Simon Willison asked, as true/false questions, whether each city in the San Francisco Bay Area is a good city, and Jev rated Cupertino highest and East Palo Alto lowest. Since only a number comes back with no supporting sentence, he said bias review comes first and not to use it for judgments such as hiring. He added that since a call costs less than ₩1, you should run hundreds or thousands of experiments to check it first.

In Korea, the AI Framework Act in force since January 22, 2026 designates hiring and loan screening as high-impact artificial intelligence, and requires operators to have a way to explain the main criteria behind a result and to provide human oversight. Using Jev, which returns only probabilities, for such judgments would require a design that includes human review in the confidence branching.

### Korean-language performance and closed operation

The official documentation states that English is the primary training language and has the highest accuracy, and that Korean and other CJK scripts are handled but not at the same level. Putting it into a Korean service would mean measuring accuracy and calibration again on Korean data.

Since the weights are closed, the fact that the data to be judged must be sent to an outside API is another thing to check before adopting it.

## Summary

![Five key points about Jev](/assets/images/ai/jev-decision-model/en/09-items.webp)
*Five key points about Jev — Source: self-rendered from TypeSafe AI and Vercel materials*

## Sources

- [[TypeSafe AI] Introducing System One Models & Jev (official announcement, benchmarks, limits)](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- [[TypeSafe AI] Workflow Evals (accuracy, cost, and latency by workflow)](https://evals.typesafe.ai/)
- [[TypeSafe AI Docs] Models (pricing, input limits, rate limits, language support)](https://docs.typesafe.ai/models)
- [[TypeSafe AI Docs] Choice (request and response examples)](https://docs.typesafe.ai/primitives/choice.md)
- [[TypeSafe AI Docs] Confidence-gated routing (branching on confidence)](https://docs.typesafe.ai/patterns/confidence-routing.md)
- [[Vercel] Jev is the fastest-adopted model in AI Gateway history (adoption)](https://vercel.com/blog/ai-gateway-jev-model-launch)
- [[X] Guillermo Rauch's post (results of swapping fx's safety review)](https://x.com/rauchg/status/2100307962262872105)
- [[The Register] TypeSafe AI debuts model for machines (demo figures)](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711)
- [[MarkTechPost] TypeSafe AI Releases Jev (confidence calculation, what the 0% means)](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/)
- [[Simon Willison] Jev introduces a new shape of LLM (bias experiment)](https://simonwillison.net/2026/Sep/21/jev/)
- [[KDnuggets] What Everyone Is Getting Wrong About TypeSafe AI's Jev (comparison with classifiers)](https://www.kdnuggets.com/what-everyone-is-getting-wrong-about-typesafe-ais-jev)
- [[ZDNet Korea] Ahn Kwang-seop, AI Synthesis, column on Jev (basis for the multiples)](https://zdnet.co.kr/view/?no=20260920215302)
- [[Wikipedia] Jev (AI model) (founders, funding, origin of the name)](https://en.wikipedia.org/wiki/Jev_(AI_model))
- [[GitHub] jaredpalmer/kev (open-source Kev)](https://github.com/jaredpalmer/kev)
- [[Finout] GPT-5.6 Pricing 2026 (GPT-5.6 pricing)](https://www.finout.io/blog/gpt-5.6-pricing-2026-sol-terra-and-luna-tiers-explained)
- [[Korea Law Information Center] Framework Act on the Development of Artificial Intelligence and Establishment of a Foundation of Trust](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543)
- Exchange rate: converted at $1 ≈ ₩1,400
