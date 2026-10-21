---
title: "FANCIM Exposed Reviewers' Real Names — A List of About 2,000 People Was Circulated"
description: "How an update error put real names that were never on screen into browser responses, and why the damage is worst for creators who perform under a stage name"
date: 2026-09-21
category: Tech
subcategory: News
tags: [fancim, data-breach, privacy, api-security, incident]
image: /assets/og/en-2026-09-21-fancim-real-name-exposure.png
---

**FANCIM**, a service that lets fans send gifts to creators without knowing their address, exposed reviewers' real names alongside their nicknames. The cause was an incorrect data column wired into the reviewer display field in a September 18 update, and in the meantime someone collected about 2,044 real names and uploaded them to an anonymous file sharing site.

For creators who perform under a stage name — especially virtual streamers who never show their face — having a real name tied directly to that stage name is itself the harm.

![FANCIM's personal data exposure lookup page — date of occurrence, exposed items, lookup period](/assets/images/tech/fancim-real-name-exposure/01-hero.webp)
*FANCIM's personal data exposure lookup page — date of occurrence, exposed items, lookup period — Source: FANCIM*

## How it unfolded

![Timeline of the FANCIM real-name exposure](/assets/images/tech/fancim-real-name-exposure/en/02-chart.webp)
*Timeline of the FANCIM real-name exposure — Source: self-rendered from Illio's second notice and Korean reporting*

On the night of September 18, a post spread through online broadcasting communities. It said that opening developer tools in a Chrome-based browser let you see the real name of the account behind each review on FANCIM's review screen, and lists of names said to have been collected that way soon spread through communities and X.

**Illio**, which operates FANCIM (and Pokacha), said in a first notice in the early hours of the 19th that the pairing of nicknames and names circulating in communities was unconfirmed, then replaced it the same morning with a notice admitting an update error. The second notice explained the cause this way.

> An incorrect data column was connected to the reviewer display information during a service update

According to the second notice of September 20 reported by Economy Science, the company received its first report around 2 a.m. on the 19th and blocked the exposure path around 3 a.m., then at 9 a.m. emailed the affected users and reported the incident to KISA (Korea Internet & Security Agency). The site switched to a maintenance page from 2 p.m. on the 19th, and as of September 21 visiting it opens only the maintenance notice and the lookup page.

### When the exposure started

Reporting puts the exposure window from 11 p.m. on the 18th to 3 a.m. on the 19th, but the company's second notice says traffic rose from **9 a.m.** on the 18th and that request volume spiked in the early hours of the 19th. The lookup page gives the date of occurrence only as **September 18–19**, so when the error actually began exposing real names will be settled by the investigation.

## What was exposed

The items FANCIM listed on its lookup page are two: **the real name and nickname of people who wrote FANCIM G gift reviews**. Users who did not write a review are unaffected by this path.

| Item | Status | Basis |
| :--- | :--- | :--- |
| Real name | <mark>Exposure confirmed</mark> | FANCIM lookup page |
| Nickname | <mark>Exposure confirmed</mark> | FANCIM lookup page |
| Password | No leak confirmed | Economy Science reporting |
| Address and contact | No company statement | Community claims only |
| People exposed | **About 2,044** | Tally of the circulated file |

The figure of about 2,044 is a community tally of the circulated file, not a company figure. Illio said it is analyzing the accounts and scope accessed together with an outside security firm. There were claims that addresses were exposed as well, but that is not among the items the company stated, and since FANCIM exists precisely so that fans can send gifts without knowing a creator's address, whether delivery information was exposed through this path is something the investigation has to confirm.

### The harm in linking real names to nicknames

A real name and a nickname are of little use separately, but once the two are linked as one account's information, the stage name identifies the person. For a virtual streamer, whose job rests on keeping broadcasting and private life apart, that link is identity exposure, and it can lead to doxxing or stalking. Several virtual streamers announced they were leaving FANCIM after the incident.

## Cause and structure

This was not an outside attacker breaking into a server; it was an incident where the **preconditions** for an attack were essentially absent. No login, no malware, and no administrator privileges were needed — just a review page anyone can open and the browser's built-in tools.

A web page receives data from the server and draws only part of it on screen, so even when only a nickname is visible, if the server put the real name in the response as well, that value has already arrived in the user's browser. Developer tools merely show that response as it is, which makes this exposure equivalent to being public **the moment** it was included in the browser response.

[Excessive response]
An error where the API returns more fields than the screen needs, corresponding to broken object property level authorization in the OWASP API Security Top 10

[Wrong column connected]
The cause the company stated: the reviewer display value was read from the real name column instead of the nickname column

[Automated collection]
Signs that about 2,000 records were gathered by repeatedly requesting the page rather than viewed one person at a time, with the company confirming a spike in requests overnight

The way to prevent this type of incident is to filter fields in the **server response**, not on screen. Automatically checking before release whether API responses include personal data fields, together with blocking bulk requests hitting the same page in a short window, might have kept an exposure from turning into mass collection.

## The amended Personal Information Protection Act and the timing of notice

The amended Personal Information Protection Act, in force since September 11, requires notifying users within 72 hours of learning of a **possibility of a leak**, even when a leak is not confirmed.

| Milestone | Time |
| :--- | :--- |
| Company received first report | Around 2 a.m., Sep 19 |
| User notification email and KISA report | **9 a.m., Sep 19** |
| 72-hour deadline | Around 2 a.m., Sep 22 |

Going by the company's statements, notification and reporting happened about seven hours after it received the report, meeting the 72-hour deadline. But since the company also said it saw traffic rising from the morning of the 18th, the judgment could change depending on **when the company is taken to have known** something was wrong.

In May 2026 the Personal Information Protection Commission named fandom platforms and matchmaking services as targets for focused personal data inspections, but as of September 21 no announcement of a commission investigation into FANCIM has been confirmed.

The amended act was covered in full on September 11.

[The Amended Personal Information Protection Act Takes Effect — Notice Within 72 Hours Even on the Mere Possibility of a Leak (in Korean)](/posts/privacy-act-breach-possibility-notice/)

## What affected people can do

![KISA logo](/assets/images/tech/fancim-real-name-exposure/03-logo-kisa.webp)
*KISA logo — Source: KISA*

If you have written a FANCIM review, check first whether you were exposed. The lookup page takes a FANCIM ID and password, or a name and email, or a social account, and stays open until **November 19**.

🔗 Link - https://fancim.me/security-notice

The company has no way to recall a list that has already spread.

If you find a post containing a real name, request removal through that platform's reporting function, and if harm continues you can report it to KISA's Personal Information Infringement Report Center (118, no area code).

Damages can be pursued through mediation by the Personal Information Dispute Mediation Committee or through litigation, and attorney Kim Hyo-gyeom, a former internet broadcaster, is recruiting participants until September 30 for a class action against Illio on behalf of creators whose real names and nicknames were exposed together.

🔗 Link - https://privacy.kisa.or.kr

Downloading the list file and reposting it, or capturing and sharing the names, widens the harm and in itself amounts to providing personal data to a third party.

No password leak has been confirmed, but if you use your FANCIM password on other services, changing it is the safer course.

![Summary card of what affected people should do](/assets/images/tech/fancim-real-name-exposure/en/04-items.webp)
*Summary card of what affected people should do — Source: self-rendered from FANCIM's lookup page and KISA*

## Sources

- [[FANCIM] Personal data exposure lookup page (date of occurrence, exposed items, lookup period)](https://fancim.me/security-notice)
- [[Economy Science] FANCIM investigates creator real name and nickname exposure, signs of bulk lookups and outside circulation (2026-09-20, times and actions in the second notice)](https://www.e-science.co.kr/news/articleView.html?idxno=135801)
- [[ASEAN Express] FANCIM reports the leak to KISA and opens a lookup site (2026-09-20)](https://www.aseanexpress.co.kr/news/article.html?no=13077)
- [[ASEAN Express] Internet broadcasters rush to leave FANCIM after the leak (service structure, non-reviewers unaffected)](https://www.aseanexpress.co.kr/news/article.html?no=13071)
- [[Top Celeb News] FANCIM admits reviewers' real names were exposed, virtual streamers leave one after another (exposure window, first notice)](https://www.topcelev.co.kr/news/articleView.html?idxno=3974)
- [[OWASP] API Security Top 10 2023, API3 Broken Object Property Level Authorization (the excessive response type)](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)
- [[Nate News] Focused inspections of fandom platforms and matchmaking services to prevent leaks (2026-05-22)](https://news.nate.com/view/20260522n16969)
