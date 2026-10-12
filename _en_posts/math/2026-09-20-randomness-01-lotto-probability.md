---
title: "Randomness (1) — One in 8.15 Million for the Lotto Jackpot, and How Far Luck Goes"
description: "The combinatorics behind the lotto jackpot odds, the average return on ₩1,000, and what picking numbers can and cannot change"
date: 2026-09-20
category: Math
subcategory: Explainer
tags: [lottery, probability, expected-value, combinatorics, randomness]
image: /assets/og/en-2026-09-20-randomness-01-lotto-probability.png
---

Draw 1242 of the Korean lotto, held on September 19, produced nine first-prize winners. Each received ₩3,281,030,000.

Someone wins every week, which invites the thought that with a bit of luck it could be you — but this game's probability is far more specific than the word luck. Looking at how the odds are calculated and how ₩1,000 is divided up separates what you can change from what you cannot.

![A path leading to one of 8.15 million branches](/assets/images/math/randomness-01-lotto-probability/01-agy-hero.webp)
*A path leading to one of 8.15 million branches — Source: concept image · self-generated with agy*

## Six from 45, 8.15 million ways

You pick 6 numbers from 1 to 45. Counting order, that is 45 × 44 × 43 × 42 × 41 × 40 = 5,864,443,200 ways.

But the lotto does not care about the order drawn. There are 6 × 5 × 4 × 3 × 2 × 1 = 720 ways to arrange the same six numbers, so you divide by that 720.

5,864,443,200 ÷ 720 = **8,145,060**

One of those 8,145,060 combinations is drawn. The first-prize probability of 1/8,145,060 is not a result of the calculation; it is the rule of the game itself.

## The prize tiers, seen through draw 1242

| Tier | Condition | Probability | Winners in draw 1242 | Prize per winner |
|---|---|---|---|---|
| 1st | 6 matches | <mark>1/8,145,060</mark> | 9 | ₩3,281,030,000 |
| 2nd | 5 + bonus | 1/1,357,510 | 104 | ₩47,320,000 |
| 3rd | 5 matches | 1/35,724 | 3,206 | ₩1,540,000 |
| 4th | 4 matches | 1/733 | 165,377 | **₩50,000 fixed** |
| 5th | 3 matches | 1/45 | 2,729,145 | **₩5,000 fixed** |

![Number of games needed for a win at each tier](/assets/images/math/randomness-01-lotto-probability/02-chart.webp)
*Number of games needed for a win at each tier — Source: self-rendered from Donghaeng Lottery probabilities*

The fourth and fifth tiers pay fixed amounts; the first through third do not. The fourth- and fifth-tier shares come out of the total prize pool first, and what remains is split 75% to first, 12.5% to second, and 12.5% to third, then divided again by the number of winners in each tier.

That is why the same first prize differs from draw to draw. One winner takes the whole tier; ten winners take a tenth each.

## Why there is a jackpot winner every week

The odds are one in 8.15 million, and sales explain why someone still wins every week.

The first-prize total in draw 1242 was ₩29.53 billion. Since that is 75% of the first-through-third pool, the three tiers together came to about ₩39.37 billion.

Add the fourth tier, 165,377 × ₩50,000 ≈ ₩8.27 billion, and the fifth, 2,729,145 × ₩5,000 ≈ ₩13.65 billion, and the draw's total prize pool is about ₩61.29 billion.

Since the total prize pool is 50% of sales, sales were about ₩122.6 billion, and dividing by ₩1,000 per game gives **about 120 million games** sold.

With 8.15 million combinations and 120 million games sold, that is an average of 15 tickets per combination. About 15 first-prize winners is the normal expectation, and draw 1242's nine is in that neighborhood.

A low probability and a rare event are not the same thing. The probability is unchanged, but with more than a hundred million trials, somebody hits it every week.

## The average return per ₩1,000

The proportions sales are split into are published.

![How ₩1,000 of lotto spending is divided](/assets/images/math/randomness-01-lotto-probability/03-chart.webp)
*How ₩1,000 of lotto spending is divided — Source: self-rendered from Donghaeng Lottery's allocation ratios*

- Prizes 50%
- Lottery fund 43.6%
- Retailer commission 5.4%
- Operating costs 1%

Prizes being half of sales means the expected value of one game is **₩500 per ₩1,000**. Whatever numbers you pick and however many tickets you buy, that ratio does not change.

With tax it is lower still. Prizes are other income, so anything up to ₩50,000 per win is untaxed, above ₩50,000 is taxed at 22%, and the portion above ₩300 million at 33%.

Taking draw 1242's first prize of ₩3,281,030,000, 22% is withheld up to ₩300 million and 33% on the remaining ₩2,981,030,000, leaving about **₩2.23 billion** in hand. The fourth tier's ₩50,000 and fifth tier's ₩5,000 are below the taxable threshold and come through intact.

## Number choice, odds, and prize size

There is no way to raise your odds by choosing numbers. 1, 2, 3, 4, 5, 6 and the combination drawn last week are both one in 8.15 million. Quick pick and manual selection have the same odds.

What you can change is how much you receive if you win. Because the first three tiers are split proportionally, **the fewer people who picked the same combination, the more you get**.

The combinations people choose heavily are fairly clear.

- The 1–31 range, from birthdays and anniversaries
- Consecutive runs like 1, 2, 3, 4, 5, 6
- Patterns drawn as diagonals or shapes on the slip

Avoiding these does not raise your odds, but it reduces the number of people you would split with, raising the expected size of what you receive. Mixing in the 32–45 range is an instance of this.

## What "luck" means

### Draws are independent

The draw is an independent trial. The thought that a number that has not come up for a while is due is the gambler's fallacy.

### The sample size behind "frequent number" statistics

Through draw 1242, 7,452 numbers have been drawn excluding bonuses. If the 45 numbers came up evenly, that would be about 166 each, and in a sample this size it is natural to see some in the 140s and some in the 190s. That spread is variation in the sample, not a property of the numbers.

### The law of large numbers and outcomes that never appear

The law says that as trials increase the **proportion** approaches the theoretical value; it does not say an outcome that has not appeared eventually will. Buying one game a week, reaching first prize takes on average 8,145,060 ÷ 52 ≈ **156,636 years**.

## Summary

![Summary of lotto probability](/assets/images/math/randomness-01-lotto-probability/04-items.webp)
*Summary of lotto probability — Source: compiled from this post · self-rendered*

The next post covers how this draw's randomness is produced, and how random the random numbers a computer makes really are.

## Sources

- [Donghaeng Lottery] About Lotto 6/45 (probability by tier, prize allocation ratios, split of sales)
- [MoneyToday] Nine first-prize winners in lotto draw 1242, ₩3,281,030,000 each (2026-09-19, winners and amounts by tier)
- [Wikitree] Lotto draw 1242 winning numbers and ₩29.53 billion first-prize total (2026-09-19)
- [National Tax Service] Withholding on other income (₩50,000 minimum taxable threshold, rate above ₩300 million)

🔗 Link - https://www.dhlottery.co.kr/lt645/intro
