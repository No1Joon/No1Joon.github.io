---
title: "Seven Korean Financial Firms Breached in a Row — The Entry Point Was Staff-Facing Systems"
description: "How the breaches that started at Shinhan Bank spread across the financial sector in five days, the common way in, and what customers can do"
date: 2026-10-05
category: Tech
subcategory: News
tags: [data-breach, banking, financial-security, privacy, incident]
image: /assets/og/en-2026-10-05-korea-financial-sector-breaches.png
---

After data on about 25,000 Shinhan Bank customers leaked on September 30, 2026, breaches were confirmed at seven financial firms over the next five days: KB Kookmin, Hana, and BNK Busan banks, Yegaram and Welcome savings banks, and Hyundai Capital.

What they have in common is that the compromised systems were not the internet banking that customers use, but **internet-exposed work systems used by staff and loan brokers**. Authorities said account passwords and OTPs were not stolen, but some customers' resident registration numbers and connecting information (CI) were leaked.

![First page of the Financial Services Commission's October 2, 2026 press briefing](/assets/images/tech/korea-financial-sector-breaches/01-capture.webp)
*First page of the Financial Services Commission's October 2, 2026 press briefing — Source: Financial Services Commission*

## Timeline

![Timeline of the chain of breaches in the financial sector](/assets/images/tech/korea-financial-sector-breaches/02-chart.webp)
*Timeline of the chain of breaches in the financial sector — Source: self-rendered from FSC and company announcements*

Shinhan Bank detected the leak on September 30 and issued an apology under CEO Jung Sang-hyuk's name on October 1. The attacker bypassed authentication on a mobile web page for loan brokers, then used the customer numbers obtained there to access a service that looks up contact details and dates of birth. Shinhan blocked the IP, shut down the service, and said it would fully compensate any losses.

The same day, KB Kookmin Bank also found abnormal external access to its mobile work-support system for staff. On October 2, Hana Bank and BNK Busan Bank reported additional leaks after running their own checks in light of the Shinhan incident; on October 3, damage was confirmed at Yegaram Savings Bank and Hyundai Capital, followed by Welcome Savings Bank.

The Financial Services Commission (FSC) held an emergency response meeting chaired by its secretary general on October 2, and on October 4 convened the CEOs of the seven affected firms and the heads of the industry associations for another meeting. The police cyber investigation unit is looking into whether the four bank incidents are connected.

According to October 5 reports, signs of intrusion were also found at one or two insurers and brokerages, while the Korean Federation of Community Credit Cooperatives and NH Nonghyup mutual finance blocked access attempts. No evidence of data leaving these companies has been confirmed yet.

## What was leaked

![Chart of people affected by each financial firm](/assets/images/tech/korea-financial-sector-breaches/03-chart.webp)
*Chart of people affected by each financial firm — Source: self-rendered from company announcements and press reports*

Who was affected and what leaked differs by company.

| Company | Affected | Leaked data |
| :--- | :--- | :--- |
| Shinhan Bank | About 25,000 customers | Name, phone, annual income, loan limit |
| Shinhan Bank (subset) | 66 RRNs, 97 CIs | <mark>Resident registration number, CI</mark> |
| KB Kookmin Bank | 119 customers | Name, phone, address, encrypted RRN |
| Hana Bank | 89 customers | **RRN**, address, email, employer |
| Yegaram Savings Bank | About 40,000 customers | Name, date of birth, contact |
| Welcome Savings Bank | Up to 2,200 corporate customer records | Not disclosed |
| Hyundai Capital | 146 loan brokers | Broker personal data |
| BNK Busan Bank | 11 contractor staff | Name, phone, date of birth, email |

Authorities said information that could be used to take money immediately, such as account passwords and OTPs, was not stolen. On the other hand, name, phone number, and date of birth combined with annual income and loan limit can be used as-is in voice-phishing texts that dangle loans as bait.

Connecting information (CI) is a one-way encrypted value derived from the resident registration number, which many online services use to check whether two accounts belong to the same person. CI generally cannot be changed, so it stays the same value even after a leak.

## How they got in

![Concept image of internet-exposed work systems](/assets/images/tech/korea-financial-sector-breaches/04-agy.webp)
*Concept image of internet-exposed work systems — Source: concept image · self-generated with agy*

The attack didn't require installing malware on customer devices or breaking into the internal network — being able to reach work pages exposed to the internet was enough.

| Company | Compromised system | Used by |
| :--- | :--- | :--- |
| Shinhan Bank | Lookup page for loan brokers | Loan brokers |
| KB Kookmin Bank | Mobile work-support system | **Staff** |
| Hana Bank | Sales support system (ODS) | **Staff** |
| BNK Busan Bank | Mobile sales support system | Staff, contractors |
| Hyundai Capital | Lookup page for mortgage brokers | Loan brokers |

The Financial Supervisory Service (FSS) pointed to three flaws by incident type.

[Lookups without identity verification]
Functions remained that let anyone view loan application records without verifying identity

[Missing access control]
Logging in with a staff or broker account allowed viewing customer data beyond the user's job scope

[Known vulnerabilities left unpatched]
Publicly known web vulnerabilities had not been fixed

In the Shinhan case, the attacker reportedly entered other customers' customer numbers at random on the broker page to view loan application results.

According to FSS data, Shinhan, Kookmin, and Hana banks spent ₩123.974 billion on information security in 2025, but that investment was concentrated on customer-facing services, and the peripheral systems used by staff and brokers had been left out of checks.

Financial authorities believe the attacker used AI tools to automatically scan for exposed systems, rotated IPs frequently, and hit several firms at once. This is the authorities' assessment, however, and the attack tools have not been officially confirmed. Kim Seung-joo, a professor at Korea University's Graduate School of Information Security, said AI merely exposed what had been neglected in the past.

> Check every system reachable from outside, whether or not it serves customers (Financial Services Commission, 2026.10.2)

## What authorities and operators are doing

![Paragraph listing the FSC's orders in its press briefing](/assets/images/tech/korea-financial-sector-breaches/05-capture.webp)
*Paragraph listing the FSC's orders in its press briefing — Source: Financial Services Commission*

At its October 2 meeting, the FSC asked the financial sector for three things: identify and check every internet-exposed IT asset, block any path to internal data that doesn't require authentication, and share attacker IPs and techniques between firms immediately.

The FSS distributed attacker IPs and security advisories to about 500 financial firms. Banks and card companies must finish emergency checks by October 6, and brokerages, insurers, savings banks, and electronic financial businesses by October 8. At the October 4 meeting, authorities also said firms that fail to act on the shared attack information will be held strictly accountable.

On October 3, KISA issued a security advisory for companies, noting that breaches against the financial sector and private companies are continuing. It found that initial intrusions are using web and API vulnerabilities and exposed credentials, and recommended the following:

- Retire unused external services, restrict access to admin functions, apply security updates
- Strengthen permission checks and input handling for web and APIs
- Apply multi-factor authentication (MFA), revoke and rotate exposed credentials, follow least privilege
- Restrict download permissions, centralize log management, detect anomalous behavior

## What customers can do

This was not the kind of breach customers could have prevented by changing passwords or deleting apps. Nor is there a way for customers to check everything that leaked on their own, so the practical steps are to check notices from your financial institution and guard against secondary damage using the leaked data.

![Card summarizing five steps for customers](/assets/images/tech/korea-financial-sector-breaches/06-items.webp)
*Card summarizing five steps for customers — Source: self-rendered from FSC and company guidance*

When it launched in August 2024, the credit transaction safety block had to be requested in person at a branch of your bank with ID, and whether it can be requested remotely varies by institution. The identity theft prevention service and the personal-information-exposure accident prevention system can be applied for below.

🔗 Link - https://www.msafer.or.kr

🔗 Link - https://fine.fss.or.kr

For texts impersonating financial firms or public agencies that offer loan limits or breach compensation, don't tap the link — call the institution's main number directly to check.

## What to watch next

- Results of the sector-wide emergency checks due October 6 and 8, and whether more affected firms are disclosed
- Whether the police investigation confirms the four bank attacks were the work of the same group
- Whether the Personal Information Protection Commission opens an investigation and imposes fines
- The institutional improvements the FSC has announced, including whether checks of peripheral work systems become mandatory
- Whether actual leaks are confirmed from the intrusion traces at insurers and brokerages

## Sources

- [[Financial Services Commission] We will respond closely to recent intrusion threats in the financial sector (2026-10-02, source of two images in this post)](https://www.fsc.go.kr/no010101/87869)
- [[KISA Boho] Corporate security advisory against recent cyberattacks (2026-10-03)](https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72207)
- [[ZDNet Korea] Shinhan Bank leak of 25,000 customers, apology (2026-10-01)](https://zdnet.co.kr/view/?no=20261001122309)
- [[Newspim] Leak status by bank in the banking hacks (2026-10-02)](https://www.newspim.com/news/view/20261002001278)
- [[Money Today] FSC emergency meeting with seven financial firms (2026-10-04)](https://www.mt.co.kr/finance/2026/10/04/2026100413213585509)
- [[Newsworks] Leaked items by affected firm and police investigation (2026-10-05)](https://www.newsworks.co.kr/news/articleView.html?idxno=855516)
- [[Digital Today] Damage at savings banks and capital firms (2026-10)](https://www.digitaltoday.co.kr/news/articleView.html?idxno=704955)
- [[Edaily] FSS vulnerability analysis and security spending at the three big banks (2026-10-05)](https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02328806645609968)
- [[Econovill] Intrusion traces at insurers, brokerages, and mutual finance (2026-10-05)](https://www.econovill.com/news/articleView.html?idxno=752724)
- [[Toss Feed] How to apply for the credit transaction safety block](https://toss.im/tossfeed/article/money-policies-26)
