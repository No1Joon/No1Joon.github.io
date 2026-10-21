---
title: "Meta Revises Its Commercial Terms — Crawling of Linked Websites Allowed From October 30"
description: "The revision to Meta's Commercial Terms that lets it automatically collect websites linked to Instagram and Facebook business accounts and use them to train Meta products"
date: 2026-10-18
category: AI
subcategory: News
tags: [meta, commercial-terms, web-crawling, ai-training-data, instagram]
image: /assets/og/en-2026-10-18-meta-commercial-terms-web-crawling.png
---

If you run a business account on Instagram or Facebook, the terms change on October 30, 2026

Meta added a clause to its Commercial Terms saying it will **collect linked websites with automated software**

It states that the collected content can be used to develop, research, and train Meta products

If you don't agree, the only option is to stop using it for business purposes!!

![Meta wordmark](/assets/images/ai/meta-commercial-terms-web-crawling/01-logo-meta.webp)
*Meta wordmark*

## What changes in the terms

![Notice at the top of the Korean version of Meta's Commercial Terms saying they apply from October 30, 2026](/assets/images/ai/meta-commercial-terms-web-crawling/en/02-terms-notice.webp)
*Notice at the top of the Korean version of Meta's Commercial Terms saying they apply from October 30, 2026 — Source: Meta*

The document being changed is the **Meta Commercial Terms**

These are the terms that apply to commercial activity such as running ads, managing Pages, and using Meta Business Suite

The revised version applies from <mark>October 30, 2026</mark>

Meta announced the revision in early October through its blog and Business Suite notifications

The Korean version of the terms carries the same date and the same clause

The revised terms only say that <u>if you don't agree, you stop using them for commercial purposes</u>

There is no separate setting to opt out

## The new clause, explained

![Clause on automated software and test credentials in the Commercial Terms (highlighted)](/assets/images/ai/meta-commercial-terms-web-crawling/en/03-terms-crawling.webp)
*Clause on automated software and test credentials in the Commercial Terms (highlighted) — Source: Meta*

The new paragraph went into the second paragraph of the section "License and rights you give to Meta"

| Clause element | Wording in the terms |
| :--- | :--- |
| Collection tools | Web scrapers, bots, spiders, crawlers |
| Collection target | **Domains and URLs associated with** products and services |
| Collection actions | Indexing, caching, analyzing, collecting, crawling |
| Additional right | <mark>Creating test credentials</mark> |
| Purpose | Providing, developing, improving, researching, training |

It leaves room to be read as applying not only to landing pages used in ads but to every domain linked to the account

The word **train** in the English version was rendered as **education (교육)** in the Korean version

Read in English, it is the word for training AI models

Test credentials are read as meaning Meta can create test accounts on a site to access it

## Lawyers' readings and Meta's rebuttal

![Concept shot of crawlers reaching out from a business account to linked websites](/assets/images/ai/meta-commercial-terms-web-crawling/04-agy-crawl.webp)
*Concept shot of crawlers reaching out from a business account to linked websites — Source: concept shot · self-generated with agy*

On October 15, the US journalism research outlet Nieman Lab had three lawyers review the clause

[James Grimmelmann]
Cornell Law School professor; sees test credentials as giving access even to content that opens only after signing up

[Matt Topic]
Attorney at Loevy & Loevy; sees millions of dollars (billions of won) worth of content at stake

[Benjamin Sobel]
University of Wisconsin Law School professor; compares it to tying under antitrust law, which binds other conditions to using a product

All three said it is uncertain whether courts would uphold the clause

Still, Topic advised that <u>news organizations should assume it will be enforced and prepare</u>

Almost every news organization has at least one Meta business account, so it is hard to fall outside its scope!

A Meta spokesperson explained that it had merely consolidated crawling language that was in several terms

It said the way it crawls publishers **does not change**

Meta communications lead Andy Stone also posted on X on October 16 that it is **not true**

The explanation is that the revision is meant to accurately collect product information from external sites

Meta did not answer whether test credentials could be used to access content only paying subscribers can see

## What robots.txt can block

![Meta developer documentation describing Meta-ExternalAgent and Meta-ExternalFetcher, with a robots.txt example](/assets/images/ai/meta-commercial-terms-web-crawling/en/05-crawler-doc.webp)
*Meta developer documentation describing Meta-ExternalAgent and Meta-ExternalFetcher, with a robots.txt example — Source: Meta*

The alternative Meta points to is **robots.txt**

It is a file placed at the top-level path of a site, and it can allow or block access per crawler

Meta's developer documentation lists five crawlers

| Crawler | Purpose |
| :--- | :--- |
| **Meta-ExternalAgent** | <mark>Training foundation AI models</mark>, indexing |
| Meta-WebIndexer | Citations in Meta AI search |
| Meta-ExternalAds | Ads and business products |
| Meta-ExternalFetcher | Fetching links users request |
| FacebookExternalHit | Link previews |

To block AI training, you name and block Meta-ExternalAgent

![robots.txt example that blocks only meta-externalagent and allows the link-preview crawler](/assets/images/ai/meta-commercial-terms-web-crawling/en/06-term-robots.webp)
*robots.txt example that blocks only meta-externalagent and allows the link-preview crawler — Source: self-rendered based on Meta developer documentation*

If you also block FacebookExternalHit, previews of shared links may disappear

Meta states that robots.txt changes <u>take up to 24 hours to take effect</u>

The documentation itself says **Meta-ExternalFetcher** can bypass robots.txt!

That's because it is the crawler that fetches links users request

The lawyers thought Meta could argue, based on agreement to the terms, that the contract takes precedence over robots.txt

<mark>robots.txt is a technical block, and whether the terms override it has not yet been decided</mark>

## What businesses in Korea should check

In December 2025, Meta signed **AI content deals** with CNN, Fox News, Le Monde, and others

They are deals under which Meta AI links to those articles when answering news questions

Through the Commercial Terms, Meta also receives rights to use the content of linked sites

As of October 18, 2026, I <u>couldn't find</u> official positions from Korean press associations or government agencies

Businesses running **Instagram ads**, such as online shops, clinics, and private academies, receive the same terms

![Summary card of the Meta Commercial Terms revision](/assets/images/ai/meta-commercial-terms-web-crawling/en/07-items.webp)
*Summary card of the Meta Commercial Terms revision — Source: self-rendered based on Meta Commercial Terms and developer documentation*

## Sources

- [[Meta] Commercial Terms revision preview (applies October 30, 2026, Korean version)](https://www.facebook.com/legal/commercial_terms_preview)
- [[Meta for Developers] Meta web crawlers (five crawlers, robots.txt example)](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers)
- [[Nieman Lab] Three lawyers' readings of the clause and the Meta spokesperson's reply (2026-10-15)](https://www.niemanlab.org/2026/10/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say/)
- [[Relevant Audience] English clause wording and Andy Stone's post (2026-10-17)](https://www.relevantaudience.com/meta/meta-commercial-terms-crawling-ai-training-october-30-2026/)
- [[ZDNet Korea] Report on concerns from Korean news organizations (2026-10-17)](https://zdnet.co.kr/view/?no=20261017091913)
- [[Reuters via MarketScreener] Meta's AI content deals with news publishers (2025-12-05)](https://uk.marketscreener.com/news/meta-strikes-multiple-ai-deals-with-news-publishers-ce7d51dcdf81ff24)
- Exchange rate: converted at $1 ≈ ₩1,400
