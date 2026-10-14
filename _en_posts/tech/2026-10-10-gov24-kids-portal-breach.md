---
title: "Gov24 Kids Portal Hacked — Resident Registration Numbers and Accounts Believed Leaked"
description: "The timeline of the Gov24 Kids Portal breach, which began with a memory dump leak, the items believed leaked, and how the notice was handled"
date: 2026-10-10
category: Tech
subcategory: News
tags: [gov24, data-breach, public-sector, privacy, incident]
image: /assets/og/en-2026-10-10-gov24-kids-portal-breach.png
---

On August 17, 2026, the Kids Portal within Gov24 (정부24, the government's online services portal) was attacked from outside, and 11 server memory dump files leaked. The next day, the Ministry of the Interior and Safety reported to the Personal Information Protection Commission that 36 resident registration numbers, 3 phone numbers, and 55 Gov24 IDs and passwords were believed to have leaked. The ministry put up an apology and notice pop-up on Gov24 on August 20 for 30 days and then took it down, and the incident first became known in detail through National Assembly material on September 29. There's no record of it left in Gov24's notices now.

![Ministry of the Interior and Safety logo](/assets/images/tech/gov24-kids-portal-breach/01-logo-mois.webp)
*Ministry of the Interior and Safety logo*

## Timeline

According to material that Rep. Jung Choon-saeng of the National Assembly's Public Administration and Security Committee obtained from the ministry and released, the attacker broke in through a vulnerable page of the Kids Portal at around 5:29 p.m. on August 17. The ministry confirmed that 11 memory dump files of the Gov24 server, among other things, leaked externally in the process, and submitted a leak report to the Personal Information Protection Commission on the 18th.

- Time of attack: around 5:29 p.m., August 17, 2026
- Route: a vulnerable page of the Gov24 Kids Portal
- Leaked: 11 server memory dump files, among other things
- Report: August 18, Ministry of the Interior and Safety → Personal Information Protection Commission
- Notice: August 20 Gov24 pop-up (deleted after 30 days)
- National Assembly disclosure: September 29

Neither a ministry press release nor public material from the Personal Information Protection Commission has come out. All figures come from the ministry's report as released by the National Assembly and cited by the press, and the final scale of damage is under investigation.

## Items believed leaked

![Estimated counts leaked in the Gov24 Kids Portal hack](/assets/images/tech/gov24-kids-portal-breach/en/02-chart.webp)
*Estimated counts leaked in the Gov24 Kids Portal hack — Source: self-rendered from the Ministry of the Interior and Safety's leak report (released by the National Assembly)*

| Item | In the report | What it means |
| :--- | :--- | :--- |
| Resident registration numbers | 36 | Identity theft risk |
| Phone numbers | 3 | Smishing targets |
| IDs and passwords | <mark>55</mark> | Account takeover risk |
| Number affected | Not finalized | Under investigation |

Resident registration numbers are hard to change, and IDs and passwords are information that can log directly into Gov24 accounts. If the same password is used on other sites, the risk spreads to other services too.

Whether the passwords were plain text or encrypted hasn't been disclosed. If they were extracted from login requests recorded in memory, they may be exactly as users typed them, but that isn't a confirmed fact either.

## What a memory dump contains

![Concept image of data fragments escaping from server memory](/assets/images/tech/gov24-kids-portal-breach/03-agy.webp)
*Concept image of data fragments escaping from server memory — Source: concept image · self-generated with agy*

A memory dump is a file that copies the contents of memory a running program was using, as is. Unlike a database, it isn't an organized table; it's a jumble of fragments of the requests, responses, and session information the server was processing at that moment.

Fragments that look like personal information inside the 11 dump files have to be checked and counted one by one, which is why the ministry's reported figures were classified as "estimated." Dailysecu reported that it hasn't been determined whether the attacker ran commands on the server or broke into other internal systems, and no signs of further intrusion such as web shell installation (a script installed on a server for remote control) or account creation have been reported so far.

If the dump contains only the requests the server was processing at the moment it leaked, the damage is limited to users connected at that time. Conversely, if the attacker could run commands inside the server, the dump is just one of the results, so the investigation needs to determine whether only the requests being processed at the time leaked, or whether the attacker went as far as running commands on the server.

## A 30-day pop-up and no record left

On August 20, the ministry put up a pop-up on Gov24 with an apology and notice about signs of a personal information leak. The pop-up was posted for 30 days and then deleted, and no official record of this incident remains in Gov24's notices. The Kids Portal, the route of the hack, showed only a "System maintenance (service suspension) notice" from August 17.

When Rep. Jung pointed this out at the October 6 parliamentary audit of the ministry, the ministry explained that it couldn't identify the owners of the leaked information, so it posted a general notice instead of individual notifications, and Minister Yun Ho-jung replied regarding individual notification that the ministry "will actively take action in accordance with the regulations." The National Intelligence Service's final breach investigation report wasn't submitted to the National Assembly for security reasons.

The amended Personal Information Protection Act, in force from September 11, 2026, expanded the notification duty so that data subjects must be told as soon as a leak becomes possible, even before it's confirmed. The amended law also requires notices to include remedies such as claiming damages or applying for dispute mediation, and adds forgery, alteration, and damage to loss, theft, and leakage as triggers for notification. This incident happened before the amended law took effect, and the ministry used a pop-up notice instead of individual notification.

On September 21, 2026, following a public announcement order from the Personal Information Protection Commission, the ministry posted the facts of its legal violations in the 2024 and 2025 incidents: a 2024 code change deployed without testing, and an identity verification flaw in the resident registration card issuance status lookup left unfixed from 2017 to 2025. By the time that notice went up, the Kids Portal incident was already a month old, but it wasn't mentioned.

Rep. Jung said stronger information security and a prompt investigation and remedies must come first.

## Gov24's third personal information incident

![Timeline of Gov24 and Ministry of the Interior and Safety personal information incidents](/assets/images/tech/gov24-kids-portal-breach/en/04-chart.webp)
*Timeline of Gov24 and Ministry of the Interior and Safety personal information incidents — Source: self-rendered from the Personal Information Protection Commission's decision and the ministry's leak report*

This is Gov24's first external hack, but not its first personal information incident.

[April 2024 document misissuance]
Information on 1,233 people — 646 on NEIS-linked civil documents and 587 on tax payment certificates — was issued to other people

[May 2025 lookup flaw]
An authentication flaw in the resident registration card issuance status lookup let 4 records be viewed by other people

[May 2026 1365 Volunteer Portal]
A leak at a portal under the ministry, with victims rising from an initial 796 to 8,785

![Personal Information Protection Commission logo](/assets/images/tech/gov24-kids-portal-breach/05-logo-pipc.webp)
*Personal Information Protection Commission logo*

On May 27, 2026, the Personal Information Protection Commission decided to impose a ₩273 million penalty and a ₩3 million fine on the ministry for the first two incidents, along with a corrective recommendation and a public announcement order. The first two were a development error and an authentication flaw; this one is an external attack, so the cause differs.

## What users should do

![User action summary card](/assets/images/tech/gov24-kids-portal-breach/en/06-items.webp)
*User action summary card — Source: self-rendered from the Ministry of the Interior and Safety's leak report (released by the National Assembly)*

The ministry hasn't run a leak lookup service or sent individual notices, so there's no way to check whether your information is among the 36 or 55 records. That's why users who logged in to Gov24 with an ID and password should change their password regardless of whether they're affected.

If you're worried about a resident registration number leak, you can register with the Financial Supervisory Service's FINE personal information exposure accident prevention system. Once registered, participating financial companies strengthen identity verification to block loans and account openings made through identity theft. If a leak has caused actual harm or the concern is serious, there is also a system for applying to change your resident registration number.

🔗 Link - https://fine.fss.or.kr

![Korea Internet & Security Agency logo](/assets/images/tech/gov24-kids-portal-breach/07-logo-kisa.webp)
*Korea Internet & Security Agency logo*

If you suspect a suspicious text or identity theft, you can get help or report it at KISA's Personal Information Infringement Report Center (118, no area code).

🔗 Link - https://privacy.kisa.or.kr

## Sources

- [[Digital Daily] Gov24 hack: 11 memory dumps, estimated leak figures, Kids Portal notice status (2026-09-30)](https://m.ddaily.co.kr/page/view/2026093009383761924)
- [[Dailysecu] Time of attack on the vulnerable Kids Portal page and whether there was further intrusion (2026-09-30)](https://www.dailysecu.com/news/articleView.html?idxno=208642)
- [[Dailian] How the Gov24 hack became known a month later (2026-09-30)](https://www.dailian.co.kr/news/view/1695972/)
- [[News1] Rep. Jung Choon-saeng's remarks, damage scale not yet identified (2026-09-29)](https://www.news1.kr/politics/assembly/6304945)
- [[Byline Network] PIPC imposes ₩273 million penalty on the ministry, details of the 2024 and 2025 incidents (2026-05-28)](https://byline.network/2026/05/28-612/)
- [[Digital Daily] Ministry parliamentary audit: pop-up deleted after 30 days, individual notification, NIS report (2026-10-06)](https://www.ddaily.co.kr/page/view/2026100617335954225)
- [[Edaily] August 20 Gov24 apology and notice](https://www.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01387446645611936)
- [[Newsis] Notification duty and effective date of the amended Personal Information Protection Act (2026-03-09)](https://www.newsis.com/view/NISX20260309_0003540588)
