---
title: "Yoido Full Gospel and SaRang Church Hacked — Signs of About 1.05 Million Member Records Leaked"
description: "The scale of the two churches' member and offering records found on an overseas attacker server, the intrusion routes, and what members should do"
date: 2026-10-07
category: Tech
subcategory: News
tags: [data-breach, web-shell, privacy, erp, incident]
image: /assets/og/en-2026-10-07-church-data-breach.png
---

Member information from Yoido Full Gospel Church in Seoul and SaRang Church in Seocho-gu was found on an overseas attacker server. According to an analysis by security firm Oasis Security, the two churches together account for about 1.05 million member records and about 330,000 offering records, and the churches haven't yet confirmed the scale.

The incident came to light just days after the serial hacking of seven financial firms became known, and this time it includes data that reveals both religion and financial circumstances, such as offering histories.

![Yoido Full Gospel Church and SaRang Church logos](/assets/images/tech/church-data-breach/01-logo.webp)
*Yoido Full Gospel Church and SaRang Church logos — Source: Yoido Full Gospel Church · SaRang Church*

## Timeline

![Timeline of signs of the breach](/assets/images/tech/church-data-breach/en/02-chart.webp)
*Timeline of signs of the breach — Source: self-rendered from Oasis Security's analysis and Yoido Full Gospel Church's statement*

Cyber threat intelligence company Oasis Security found an overseas attacker server while tracing IPs used in hacking attacks, and inside it confirmed the two churches' data along with attack tools, logs, and account information. Based on the server's logs, the data appears to have been stolen in August, and the security firm reported the signs of intrusion to security authorities in September.

The Korea Internet & Security Agency (KISA) then notified the two churches, and it became public through an SBS exclusive on October 6. In a statement, Yoido Full Gospel Church said it **had been notified by KISA of signs of a personal information leak related to the church's information systems** and was confirming the facts with relevant agencies and security experts. Both churches began reporting to the authorities and formed emergency response teams.

- How it was found: a security firm tracing attack infrastructure confirmed it on the attacker's server
- When the attack happened: August (based on the attacker server's logs)
- Church confirmation: Yoido Full Gospel Church acknowledged the KISA notice; scale not confirmed
- Further signs: records of login attempts against 197 other churches; actual leaks confirmed only at the two churches

## Estimated scale of the leak

![Number of church records found on the attacker's server](/assets/images/tech/church-data-breach/en/03-chart.webp)
*Number of church records found on the attacker's server — Source: self-rendered from Oasis Security's analysis*

On the Yoido Full Gospel Church side, it totals 47.3GB, including about 960,000 member records updated over the past two years, about 330,000 offering records, about 68,000 electronic approval documents, and 14,706 internal messenger conversations. SBS reported that the offering history spans 1993 to 2019.

On the SaRang Church side, information on about 89,000 members and 286 staff including the senior pastor was confirmed. These counts were tallied from files on the attacker's server, so the actual number of victims will be set only after deduplication and confirmation by the churches.

| Item | Yoido Full Gospel Church | SaRang Church |
| :--- | :--- | :--- |
| Member records | **About 960,000** | About 89,000 |
| Confirmed items | Name, address, contact, etc. | Name, address, phone number |
| Offering records | <mark>About 330,000</mark> | Not reported |
| Internal documents | Electronic approvals, messenger | Staff information, photos |

### What hasn't been confirmed yet

Reports differ on whether resident registration numbers were included. Financial News and ZDNet Korea wrote that Yoido Full Gospel Church's member records include names and resident registration numbers, while SBS mentioned only name, address, and phone number. No reports say account numbers or card information were included.

## Intrusion routes

![Concept image of an intrusion spreading from an external system inward](/assets/images/tech/church-data-breach/04-agy.webp)
*Concept image of an intrusion spreading from an external system inward — Source: concept image · self-generated with agy*

At both churches, the attacker broke into one internet-accessible system, escalated privileges, and reached connected internal systems.

| Stage | Yoido Full Gospel Church | SaRang Church |
| :--- | :--- | :--- |
| Initial entry | **Web shell** upload | Previously obtained account |
| First system | ERP server | Groupware server |
| Privilege escalation | DB admin privileges | <mark>IDOR vulnerability</mark> |
| Spread | Connected internal services | ERP via single sign-on |

A web shell is a script uploaded to a web server that lets an attacker run server commands with nothing more than browser requests. Yoido Full Gospel Church's enterprise resource planning (ERP) server was analyzed as having been breached this way, after which the attacker obtained database administrator privileges.

At SaRang Church, the attacker logged into the groupware with an account believed to have been obtained beforehand, and used IDOR (an access control flaw where changing just the record number in a request gives access to another user's data) to obtain other users' information and even admin-level accounts. Because the groupware and ERP were linked by single sign-on (SSO), access extended to the ERP.

### Link to a US religious service

Oasis Security found signs that the admin account of an external storage server (MinIO), obtained in the breach of a US religious content and streaming service, was used to store and transfer Korean church data. This supports the possibility of a continuing campaign that reuses infrastructure once obtained to attack other religious institutions. The name of that US service hasn't been disclosed.

## Confirmed versus estimated

![Korea Internet & Security Agency logo](/assets/images/tech/church-data-breach/05-logo-kisa.webp)
*Korea Internet & Security Agency logo — Source: KISA*

The only thing the parties have officially confirmed in this incident is that **KISA notified the churches of signs of a leak**. The counts, items, and intrusion routes are the results of a security firm's analysis of the attacker's server, and the churches' position is that they can't judge unconfirmed details.

| Claim | Basis | Status |
| :--- | :--- | :--- |
| KISA notice of suspected leak | Church statement | **Confirmed** |
| Counts, items, intrusion routes | Security firm analysis | Estimated |
| Use of AI | "Sub-agent" wording | <mark>Estimated</mark> |
| Same attacker as the financial sector | Different methods (officials) | No basis |

The possibility of AI use was raised when SBS reported that the term "sub-agent" and hundreds of analysis documents were found on the attacker's server. On the other hand, Money Today relayed an official's explanation that the methods differ from the recent AI hacking of the financial sector, suggesting a different attacker. It became known the same week as the financial-sector incidents, but there's no basis yet to treat them as the same case.

## Why offering records are sensitive

Article 23 of the Personal Information Protection Act defines information about thought and belief as sensitive information and restricts its processing. A particular church's member list and offering records reveal religion, and the amounts and duration of offerings even hint at household finances. Unlike a leak of only names and contact details, that's why it can be abused for impersonation or blackmail tailored to church members.

Article 34 of the same act and its enforcement decree require a personal information controller that learns of a leak to notify data subjects within 72 hours, and to report to the Personal Information Protection Commission or KISA if 1,000 or more people are affected. Churches are personal information controllers that process member information and carry this obligation. When the two churches will notify members individually hasn't been announced yet.

## What members should do

![Member action summary card](/assets/images/tech/church-data-breach/en/06-items.webp)
*Member action summary card — Source: self-rendered*

There's no way for individuals to check directly whether their information was included. Until the churches send notices, the only option is to assume a leak and be wary of impersonation.

🔗 Link - https://www.msafer.or.kr

🔗 Link - https://privacy.kisa.or.kr

### What church and nonprofit operators should check

In both incidents the initial entry was a single business system exposed to the internet, so operators should start by reviewing the list of ERP and groupware systems reachable from outside. They should monitor whether executable files appear in web servers' upload paths, and check whether the server verifies, for every groupware request, that the requester owns that data (IDOR). For systems linked by single sign-on, they should also separately check how far one account's privileges reach.

## Sources

- [[SBS] Exclusive: signs that 1 million pieces of sensitive information leaked from two megachurches (2026-10-06, offering period, AI signs, login attempts against 197 churches)](https://news.sbs.co.kr/news/endPage.do?news_id=N1008785523)
- [[ZDNet Korea] Two major Korean churches hacked, Oasis Security analysis (2026-10-06, counts, intrusion routes, MinIO)](https://zdnet.co.kr/view/?no=20261006215537)
- [[Money Today] Signs of 1 million Yoido Full Gospel and SaRang Church member records hacked (2026-10-06, church statement, methods different from the financial sector)](https://www.mt.co.kr/society/2026/10/06/2026100622434016162)
- [[Financial News] Yoido Full Gospel and SaRang Church hacked (2026-10-06, report on resident registration numbers, church response)](https://www.fnnews.com/news/202610062216108512)
- [[Seoul Shinmun] After financial firms, signs of cyberattacks on two megachurches too (2026-10-06, intrusion stages)](https://www.seoul.co.kr/news/economy/IT/2026/10/06/20261006800007)
- [[KISA] Guide to reporting personal information leaks (72 hours, 1,000-person threshold)](https://www.kisa.or.kr/1030402)
