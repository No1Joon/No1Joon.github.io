---
title: "Weverse Leaks 420,000 Records — Its Payment API Was Breached"
description: "The leaked items that matter even without names or contact details, and how the breach only came to light more than a month later through an outside tip"
date: 2026-09-16
category: Tech
subcategory: News
tags: [weverse, data-breach, api-security, privacy, incident]
image: /assets/og/en-2026-09-16-weverse-payment-api-breach.png
---

No names or contact details were leaked, yet 420,000 records were. That's the gist of the notice Weverse posted on September 6.

Weverse Company said the API that processes payment information was breached and data for **422,584** records, counted by account ID, was taken. The company explained that identifying information such as names and contact details wasn't included, so the risk of fraudulent payments is low.

But there are two points in this incident that deserve more attention than its size. The company didn't find it on its own, and it only learned of it well over a month after the first leak.

![Internal identifiers leaked through the payment API](/assets/images/tech/weverse-payment-api-breach/01-agy-hero.webp)
*Internal identifiers leaked through the payment API — Source: concept image · self-generated with agy*

## Timeline of the incident

Putting together reports from Boan News and Edaily, Weverse Company was contacted on September 3 by the Korea Internet & Security Agency (KISA), which said an outside tipster had reported a security vulnerability in the Weverse service. The company began its own investigation, reported a security breach to KISA the next day, September 4, and disclosed the leak in a notice under CEO Yang Joo-il's name on the evening of September 6.

The leaks themselves happened much earlier. The company said leaks occurred twice, **July 27 to 28** and **August 27 to 31**. It took 38 days from the first leak until the tip came in.

The cause identified is the API that processes payment information. Boan News reported it as a bypass attack targeting an externally exposed API, but the specific vulnerability type, such as IDOR, hasn't been disclosed.

- Scale: 422,584 records by account ID
- When: twice, July 27–28 and August 27–31
- How it was discovered: an outside tipster reported to KISA, and KISA passed it to the company on September 3
- Cause: insufficient access control on an externally exposed payment processing API

![Timeline from the leaks to the notice](/assets/images/tech/weverse-payment-api-breach/en/02-chart.webp)
*Timeline from the leaks to the notice — Source: self-rendered based on Boan News and Edaily reports relaying Weverse Company's notice*

## What was leaked and what wasn't

The leaked items Weverse Company disclosed fall into two groups.

| Category | Contents |
| :--- | :--- |
| Leaked | Internal identifier |
| Leaked | <mark>Payment method, PG name, currency</mark> |
| Leaked | <mark>Purchase amount, date and time, status</mark> |
| Leaked | Cancellation amount, refund date and time |
| Not leaked | **Name, contact details** |
| Not leaked | **Card number, account number** |

An **internal identifier** is a number the system creates to distinguish users when they sign up. It isn't a value people use, like a resident registration number or a username, but one that only means something inside Weverse. This is the basis for the company's explanation that fraudulent payments or transfers are difficult.

That explanation is correct as far as it goes. Without a card number, that information alone can't trigger a payment. But looking at the scope precisely, there's a part you can feel safe about and a part you can't.

What remains is **purchase history**. Who bought what amount, when, with which method, and when they canceled is preserved per account. Even without names, combined with information leaked elsewhere, it becomes material for identifying people.

The most immediately usable side is impersonation. A payment-related message sent by someone who knows your actual purchase amounts and dates becomes far more convincing than ordinary smishing.

![Weverse logo](/assets/images/tech/weverse-payment-api-breach/03-weverse-wordmark-color.webp)
*Weverse logo — Source: Weverse*

## Discovery through an outside tip

It wasn't Weverse Company that detected the leak but an outside tipster.

While data was taken twice, in late July and late August, internal monitoring didn't catch it. Even after the second leak ended on August 31, it was several more days before contact came through KISA.

The fact that leaks recurred twice through the same path also means that if the July leak had been detected, the August leak could have been prevented.

Weverse Company said it strengthened access control on the payment information API, removed internal identifiers from responses, and will audit all externally exposed APIs and strengthen monitoring.

![Korea Internet & Security Agency logo](/assets/images/tech/weverse-payment-api-breach/04-kisa-logo-color.webp)
*Korea Internet & Security Agency logo — Source: KISA*

## Weverse Company's third incident

Looking at the history compiled by Ilgan Sports, privacy incidents keep recurring at the same company.

| When | What happened |
| :--- | :--- |
| November 2021 | 137 logins into other accounts due to a development error |
| June 2026 | An employee leaked information on 30 applicants |
| September 2026 | <mark>422,584 payment records</mark> |

The 2021 incident was a development error made during emergency measures for abnormal traffic, causing users to be logged into other people's accounts. The Personal Information Protection Commission issued a corrective order along with a fine of ₩7 million.

The June 2026 incident was an employee in charge of a fan event sharing fan-signing applicants' information in a KakaoTalk group chat. Information on 30 winners was disclosed without authorization.

The three have different causes: a development error, employee misconduct, and an API access control failure. The scale also grew from 137 records to 420,000.

![Weverse Company's three privacy incidents](/assets/images/tech/weverse-payment-api-breach/en/05-chart.webp)
*Weverse Company's three privacy incidents — Source: self-rendered based on Personal Information Protection Commission dispositions and Ilgan Sports reports*

## Five days before the amended Personal Information Protection Act took effect

The amended Personal Information Protection Act, which requires notification within 72 hours even when a leak is only possible, took effect on **September 11**. The Weverse notice was on September 6, so the amended law doesn't apply to this incident.

Judging by outcome alone, the notification itself wasn't late. The company was contacted on September 3 and posted the notice on September 6, three days from when it became aware.

Where disputes could arise is not the timing of notification but before it. What the amended law targets is "the period users don't know until things are confirmed," but in this incident, most of the period users didn't know about ran from late July to early September, when the company didn't know either. Moving the notification duty earlier alone doesn't shorten this stretch.

The Personal Information Protection Commission reportedly isn't at the stage of launching a formal investigation but is looking into the scale of the leak and whether safeguards were implemented. If it moves to an investigation, the issue will likely be whether API access control was properly in place.

[Amended Personal Information Protection Act Takes Effect — Notify Within 72 Hours Even If a Leak Is Only Possible (in Korean)](/posts/privacy-act-breach-possibility-notice/)

## What users should check

- **Check the statements for the payment methods** you used on Weverse. Card numbers weren't leaked, but since purchase and cancellation history was, the first thing is to see whether there are any transactions you don't recognize.
- **Be wary of messages impersonating Weverse**. Impersonation that knows your actual purchase amounts and dates may come. It's safer not to comply with requests to click links and enter information citing refunds or payment errors.
- Check whether you received an individual notice. The company said it is sending individual customer notices.
- If you suspect harm, you can report to the **Personal Information Infringement Report Center (118)** or the Personal Information Protection Commission.

No way for users to look up directly whether their account is among the 422,584 records has been disclosed yet. Not having received an individual notice doesn't mean you can conclude you weren't affected.

🔗 Link - https://privacy.kisa.or.kr

## What to watch next

- Whether the Personal Information Protection Commission launches a formal investigation and whether it finds a breach of the duty to take safeguards
- Whether the vulnerability type and leak path are disclosed as investigation results
- The results of the audit of externally exposed APIs and whether there were additional leaks
- Whether a channel appears for users to check whether their own account was included

![Summary of what to check in this incident](/assets/images/tech/weverse-payment-api-breach/en/06-items.webp)
*Summary of what to check in this incident — Source: summary card of the article · self-rendered*

## Sources

- [[Boan News] Weverse payment API breached, 420,000 records leaked... "sensitive information safe" (09.07, leaked items and measures)](https://www.boannews.com/news/articleView.html?idxno=145683)
- [[Edaily] HYBE's Weverse leaks 420,000 personal records… "internal identifiers and more exposed" (09.07, when the leaks occurred)](https://www.edaily.co.kr/News/Read?newsId=02158246645577824)
- [[Dealsite] HYBE fan platform Weverse leaks 420,000 personal records… discovered through outside tip (09.07, how it was discovered)](https://dealsite.co.kr/articles/168566)
- [[Ilgan Sports] Another 420,000 personal records leaked; HYBE Weverse security incidents "repeated" (09.07, history of past incidents)](https://isplus.com/article/view/isp202609070075)
- [[Segye Ilbo] HYBE Weverse leaks about 420,000 personal records… "payment forgery and fraudulent transfers difficult" (09.07)](https://m.segye.com/ampView/20260907503559)
- [[The Public] Only found out after an outside tip… Weverse leaks 420,000 personal records (09.07, Personal Information Protection Commission developments)](https://www.thepublic.kr/news/articleView.html?idxno=317762)
- [[Personal Information Protection Commission] Guide to reporting privacy infringement (reporting channel)](https://privacy.kisa.or.kr)
- The original Weverse notice requires a community login and couldn't be checked, so this is based on the reports above that quote the notice.
