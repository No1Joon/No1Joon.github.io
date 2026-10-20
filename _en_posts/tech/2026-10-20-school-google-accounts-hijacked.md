---
title: "110,000 Korean School Google Accounts Hijacked — Student Names and School Names Possibly Exposed"
description: "The abnormal logins and unauthorized password changes affecting more than 110,000 school Google accounts for remote classes in Korea, the information that may have been exposed, and what to check"
date: 2026-10-20
category: Tech
subcategory: News
tags: [google-workspace, account-takeover, education, data-breach, password]
image: /assets/og/en-2026-10-20-school-google-accounts-hijacked.png
---

**111,052** school Google accounts used for remote classes have been compromised!!
Through abnormal logins or unauthorized password changes, by the Ministry of Education's October 18 count

The account owners' names, grade and class, and school names may also have been exposed
<mark>Whether anything was actually leaked outside</mark> has not been confirmed yet

![Concept shot of student account cards slipping out from between open lockers](/assets/images/tech/school-google-accounts-hijacked/01-agy.webp)
*Concept shot of student account cards slipping out from between open lockers — Source: concept shot, self-generated with agy*

## Timeline

![Timeline of the school Google account compromise from late September to October 18, 2026](/assets/images/tech/school-google-accounts-hijacked/en/02-chart.webp)
*Timeline of the school Google account compromise from late September to October 18, 2026 — Source: self-rendered based on reports by Call News 24, Newsis, Education Plus, and Edupress*

Account problems first appeared in Daejeon
Account problems continued from September 28, and the education office confirmed on October 4 that passwords had been changed without authorization

On October 6, the Daejeon Office of Education said 74,246 accounts at 200 schools and institutions were affected

Seoul blocked access from overseas IPs on September 29
On the 13th, it was disclosed that about 35,500 accounts at 73 schools had been affected

On October 14, unauthorized password changes also occurred on school accounts in South Jeolla
The Ministry of Education began a full survey on the 7th and, as of the 18th, counted <mark>111,052 accounts in five regions nationwide</mark>

## Scale of damage and scope of exposure

![Horizontal bars of affected accounts by region: Daejeon, Seoul, South Jeolla, Gyeonggi, Gwangju](/assets/images/tech/school-google-accounts-hijacked/en/03-chart.webp)
*Horizontal bars of affected accounts by region: Daejeon, Seoul, South Jeolla, Gyeonggi, Gwangju — Source: self-rendered based on the Ministry of Education's full survey (data submitted to lawmaker Kang Kyung-sook's office)*

Daejeon and Seoul together account for **98.8%** of the total
The remaining South Jeolla, Gyeonggi, and Gwangju come to 1,306 combined

### 📂 Information that may have been exposed, by region

The ministry's data lists different information included in accounts depending on the region

| Region | Items possibly exposed |
| :--- | :--- |
| Seoul | Account, encrypted password |
| Daejeon | Account, password, **name** |
| Gyeonggi | Account, password, grade, class |
| South Jeolla, Gwangju | Account, password, <mark>school name, student name</mark> |

Material reachable through the accounts may also have been exposed
The Daejeon Office of Education explained that viewing personal data with a hijacked account is <u>technically possible</u>

What was in class materials, submitted assignments, and mailboxes differs by account, and whether they were viewed is under log analysis

### ✅ Confirmed damage and unconfirmed matters

[Confirmed]
Abnormal logins or unauthorized password changes, 111,052 accounts

[Not confirmed]
Whether personal data was actually leaked outside, and the scope of access

[Not confirmed]
How the accounts were taken over and who the attackers are

## The conditions that made the takeover possible

The Seoul Office of Education believes passwords were changed **after successfully logging in** from overseas IPs with IDs and passwords
Traces of repeated login attempts with automated tools were also found

Education office officials mentioned the possibility that IDs and passwords circulating on the dark web were used

It looks like **credential stuffing**, trying account details leaked elsewhere
But that is not a confirmed cause

This method succeeds when passwords have already leaked outside
and <mark>two-step verification is turned off</mark>

![Google Workspace documentation on enforcing two-step verification for administrators](/assets/images/tech/school-google-accounts-hijacked/04-photo-2.webp)
*Google Workspace documentation on enforcing two-step verification for administrators — Source: Google*

Google makes two-step verification mandatory for **administrator accounts** in Workspace for Education
Student and teacher accounts aren't covered by this requirement, so school administrators have to turn it on separately in the admin console

### 🗂️ Graduate accounts left behind

In Daejeon, accounts of graduates and retired staff had been kept rather than deleted
There was no rule on when to delete accounts, so it was left to **school administrators' discretion**

Long-unused accounts also go a long time without password changes, which can leave them exposed to attacks like this
At a training session on October 8, the Daejeon Office of Education advised deactivating and deleting graduate accounts

## Scale of school accounts and AIEP links

![Gauge of the share of affected accounts among 4.53 million school Google accounts nationwide](/assets/images/tech/school-google-accounts-hijacked/en/05-chart.webp)
*Gauge of the share of affected accounts among 4.53 million school Google accounts nationwide — Source: self-rendered based on the Ministry of Education's full survey (data submitted to lawmaker Kang Kyung-sook's office)*

11,637 schools nationwide use **4,532,766** Google Workspace accounts
The affected accounts are 2.45% of those

**AIEP** (AI-based personalized teaching and learning platform), run jointly by provincial education offices,
is also linked to outside services such as Google

According to Education Plus, there are 1,855,349 AIEP-related Google accounts, used at 6,383 schools

No sign has been confirmed that AIEP accounts or the platform were directly compromised in this incident
But because it logs in to outside services through unified authentication, there were calls for <u>security checks of linked accounts</u>

## What to do now

![Five steps students, parents, and graduates should take now](/assets/images/tech/school-google-accounts-hijacked/en/06-items.webp)
*Five steps students, parents, and graduates should take now — Source: self-rendered based on the Ministry of Education's official letter and Daejeon Office of Education guidance*

The Ministry of Education sent all schools and institutions an official letter asking for a **full password reset** and two-step verification
If your school sends instructions to change your password, just follow them

There is no way yet for individuals to check whether their data was leaked

The South Jeolla Office of Education said it will notify people again once the leaked items are confirmed
Please check <u>school text messages and letters home</u>~

If you use the same password as your school account, your accounts on other services may also become targets of further attacks
You can check whether your password is on a leak list with the method in the post below

🔗 Link - https://blog.naver.com/rottensweetpotato/224378507343

### 🏫 What schools and education offices should do

[Mandate two-step verification]
Apply it in the admin console down to student and teacher organizational units

[Clean up dormant accounts]
Set retention periods and deletion criteria for graduate and retiree accounts

[Login policy]
Restrict overseas logins, review login records regularly

If you suspect personal data damage, you can consult the Personal Information Infringement Report Center (118, no area code)

🔗 Link - https://privacy.kisa.or.kr

## What to watch next

- Results of the joint cause investigation by the Ministry of Education and Google
- Confirmation of the actual scope of the personal data leak and renewed notification
- Whether retention and deletion criteria for education accounts are set
- Results of security checks on AIEP-linked accounts

Lawmaker Kang Kyung-sook asked the Ministry of Education to <mark>establish the scope of the leak and the cause of the incident</mark> and to set up a security management system for education accounts

## Sources

- [[Edupress] 110,000 school Google accounts compromised nationwide (2026-10-19, affected accounts by region, items possibly exposed, 4.53 million accounts)](https://www.edupress.kr/news/articleView.html?idxno=30543)
- [[Education Plus] 110,000 school Google accounts hacked, red light for education security including AIEP (2026-10-19, 1.85 million AIEP-linked accounts, 11,637 schools)](https://www.edpl.co.kr/news/articleView.html?idxno=21820)
- [[Newsis, Nate News] 30,000 Seoul school Google passwords changed without authorization, overseas IPs blocked belatedly (2026-10-16, overseas IP logins, Ministry of Education letter)](https://m.news.nate.com/view/20261016n20605)
- [[Call News 24] There was no rule for deleting graduate accounts (2026-10-14, Daejeon timeline, graduate accounts)](https://www.callnews.co.kr/news/articleView.html?idxno=56903)
- [[Education Plus] Domino hacking of education Google accounts, from Daejeon and Seoul to South Jeolla (South Jeolla case)](https://www.edpl.co.kr/news/articleView.html?idxno=21803)
- [[Google Workspace Help Center] About two-step verification enforcement for administrators (mandatory for education administrator accounts)](https://knowledge.workspace.google.com/admin/security/about-2sv-enforcement-for-admins?hl=ko)
