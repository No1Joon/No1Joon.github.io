---
title: "Hacking Attempts on the Bank of Korea Up 4.5x — 186 Employees' Data Leaked via a Contractor"
description: "The rising trend of hacking attempts on the Bank of Korea, separated from the employee data leak caused by a breach at its e-learning contractor"
date: 2026-10-10
category: Tech
subcategory: News
tags: [bank-of-korea, cyberattack, data-breach, third-party-risk, financial-security]
image: /assets/og/en-2026-10-10-bank-of-korea-hacking-attempts.png
---

136 hacking attempts targeting the Bank of Korea were detected from January to October 2, 2026, about 4.5 times the 30 for all of 2025. The same data also includes an incident in May–June in which the systems of a contractor handling online training for Bank of Korea employees were breached, leaking the personal information of 186 employees. The increased hacking attempts and the actual personal information leak are two incidents with different routes.

![Bank of Korea logo](/assets/images/tech/bank-of-korea-hacking-attempts/01-logo-bok.webp)
*Bank of Korea logo*

## How it came to light

Rep. Lee Jong-wook (People Power Party) released data obtained from the Bank of Korea and the Export-Import Bank of Korea twice, on September 28 and October 7. The September 28 data covered hacking attempts through August and the contractor leak, and the October 7 data extended the counts to early October and included the Export-Import Bank's figures.

- Bank of Korea hacking attempts: 136 from January to October 2, 2026 (135 through August)
- Bank of Korea employee data leak: 186 people, via a contractor's systems
- Export-Import Bank hacking attempts: 283 from January to October 5, 2026
- Actual intrusion, service disruption, or data leak: both banks said none resulted from the hacking attempts

All figures are from data the two banks submitted to the lawmaker's office, as cited by the press. The Bank of Korea didn't issue a separate press release.

## What the 136 hacking attempts mean

![Hacking attempts detected by the Bank of Korea by year](/assets/images/tech/bank-of-korea-hacking-attempts/en/02-chart.webp)
*Hacking attempts detected by the Bank of Korea by year — Source: self-rendered from the Bank of Korea's submission to the National Assembly*

1,557 attempts were detected in 2021, falling to 192 in 2022, 97 in 2023, 52 in 2024, and 30 in 2025 before rising again in 2026. Of the cumulative 2,063 from 2021 through August 2026, 98.1% (2,024) came from abroad; by country, Brazil led with 499, followed by the US with 470, Russia with 162, and China with 126.

| Type | 2021 – August 2026 | Share |
| :--- | :--- | :--- |
| Unauthorized access attempts | **1,951** | 94.6% |
| Malware | 95 | 4.6% |
| Information gathering | 16 | 0.8% |
| DDoS | 1 | 0.05% |

The targets were internet-exposed systems such as the Bank of Korea's main website, its economic statistics website, and its digital library, and the Bank of Korea said none led to information leaks, system privilege acquisition, or website defacement. In December 2023 a DDoS attack intermittently slowed website responses, and in September one more unauthorized access attempt on the website from the Netherlands was confirmed.

"Detected attempts" are accesses that firewalls and security monitoring filtered and logged. An increase in detections signals more attack attempts, but doesn't by itself mean a breach.

## Employee data leaked through a contractor

![Concept image of information leaking out through a contractor's systems](/assets/images/tech/bank-of-korea-hacking-attempts/03-agy.webp)
*Concept image of information leaking out through a contractor's systems — Source: concept image · self-generated with agy*

The actual leak happened not at the Bank of Korea's systems but at an outside contractor. MTN reported that the GitHub system of a company that handled external e-learning training for Bank of Korea employees and processed their personal information was breached from May 9 to June 8, 2026.

| Item | Details |
| :--- | :--- |
| Breach period | May 9 – June 8 |
| Affected | **186 Bank of Korea employees** |
| Leaked items | Name, company name, rank, job, department |
| Contact details | Email, phone number |
| Passwords | Leaked in encrypted form |
| Financial data | Not leaked |

The company notified the Bank of Korea of the incident on June 11, and the next day the Bank of Korea notified the affected employees and reported it to the Personal Information Protection Commission. The company noticed the breach about a month after it began, and data on employees of other member companies using the same service was also leaked, but the total scale hasn't been disclosed. The Bank of Korea said its internal systems weren't hacked and that it will strengthen checks on contractors that process employee information.

What makes it risky is that name, rank, job, and email leaked together. That combination can be abused to craft impersonation work emails targeting specific Bank of Korea employees, so this information is more likely than the encrypted passwords to be exploited in follow-up attacks.

## Hacking attempts at state-run banks

![Top countries originating hacking attempts on the Export-Import Bank](/assets/images/tech/bank-of-korea-hacking-attempts/en/04-chart.webp)
*Top countries originating hacking attempts on the Export-Import Bank — Source: self-rendered from the Export-Import Bank's submission to the National Assembly*

The Export-Import Bank recorded 283 attempts from January to October 5, 2026, about 7.9 times the 36 in 2025. Of these, 96.1% (272) came from abroad, and access from harmful IPs rose sharply to 230 (81.3%) from 19 in 2025.

| Institution | 2025 | 2026 |
| :--- | :--- | :--- |
| Bank of Korea | 30 | 136 (through Oct 2) |
| Export-Import Bank | 36 | **283** (through Oct 5) |
| Industrial Bank of Korea | 863,053 | 854,043 (through August) |
| Korea Development Bank | 66,143 | 43,431 (through June) |

The Industrial Bank of Korea and Korea Development Bank figures come from Rep. Park Jun-tae's office and use different counting criteria, so they can't be compared directly with the Bank of Korea and Export-Import Bank figures. All four institutions said there has been no actual hacking damage recently.

After breaches at seven financial firms including Shinhan, Kookmin, and Hana Bank became known in early October, the number of attack attempts on public financial institutions also drew attention.

[Seven Korean Financial Firms Breached in a Row — The Entry Point Was Staff-Facing Systems](/en/posts/korea-financial-sector-breaches/)

## Outsourced processing and liability

![Personal Information Protection Commission logo](/assets/images/tech/bank-of-korea-hacking-attempts/05-logo-pipc.webp)
*Personal Information Protection Commission logo*

The Personal Information Protection Act requires an organization that outsources personal information processing (the delegator) to train the contractor and inspect and supervise its processing (Article 26), and if the contractor violates the law and causes damage, the contractor is treated as the delegator's employee for purposes of damages. The fact that the system belonged to another company doesn't by itself remove the outsourcing organization's responsibility.

In May 2026, the Personal Information Protection Commission fined the Rural Development Administration ₩168 million for a leak of more than 570,000 records by a personal information contractor. Whether the Bank of Korea case will receive the same judgment depends on the Commission's investigation.

![Outsourced data check summary card](/assets/images/tech/bank-of-korea-hacking-attempts/en/06-items.webp)
*Outsourced data check summary card — Source: self-rendered from the Bank of Korea's submission to the National Assembly*

If your company outsources mandatory training or job training to an external e-learning provider, employees' names, ranks, and company emails are stored on that provider's systems too. If the password for an external site you signed up for with your company email is the same as your internal account, change your internal account password first. If you receive a suspicious email or suffer damage, you can get help from KISA's Personal Information Infringement Report Center (118, no area code).

## Sources

- [[Hankook Ilbo] 136 hacking attempts on the Bank of Korea; Export-Import Bank, IBK, and KDB figures (2026-10-07)](https://www.hankookilbo.com/news/article/A2026100710370003195)
- [[Economic Review] Export-Import Bank origin countries and types, Bank of Korea recent detections (2026-10-07)](https://www.econovill.com/news/articleView.html?idxno=752904)
- [[iNews24] Bank of Korea hacking attempts by year, type, and country; items leaked via the contractor (2026-09-28)](https://inews24.com/view/2009524)
- [[MTN] Contractor GitHub breach period, notification and reporting dates (2026-09-28)](https://news.mtn.co.kr/news-detail/2026092810483660387)
- [[Byline Network] PIPC fines Rural Development Administration over contractor leak (2026-05-28)](https://byline.network/2026/05/28-612/)
- [[Korea Law Information Center] Personal Information Protection Act Article 26 (restrictions on processing personal information under outsourcing)](https://www.law.go.kr/법령/개인정보보호법)
