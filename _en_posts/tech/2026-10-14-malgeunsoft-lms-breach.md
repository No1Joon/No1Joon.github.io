---
title: "Malgeunsoft Hacked — 2.37 Million Personal Records Leaked From 22 Training Sites"
description: "How a breach at an outsourced learning management system provider leaked member information from 22 institutions' training sites at once, and how to check"
date: 2026-10-14
category: Tech
subcategory: News
tags: [data-breach, lms, third-party-risk, public-sector, privacy]
image: /assets/og/en-2026-10-14-malgeunsoft-lms-breach.png
---

Online training sites where public institution staff and teachers take mandatory training were hacked all at once. The servers of Malgeunsoft, a company that runs training systems under contract, were breached, leaking member information from 22 sites that used its learning management system (LMS).

The leak Malgeunsoft reported to the Personal Information Protection Commission is **about 2.37 million records**, and the affected institutions include the Anti-Corruption and Civil Rights Commission, the Ministry of National Defense, the Korea Educational Facility Safety Institute, the Korean Commercial Arbitration Board, and the Kia union. Members signed up on each institution's site, but the leak happened at the contractor, so users receive leak notices in the name of a company they've never heard of.

![Malgeunsoft's October 6, 2026 apology and security measures](/assets/images/tech/malgeunsoft-lms-breach/01-capture.webp)
*Malgeunsoft's October 6, 2026 apology and security measures — Source: Malgeunsoft*

## Timeline

![Timeline of the Malgeunsoft breach](/assets/images/tech/malgeunsoft-lms-breach/en/02-chart.webp)
*Timeline of the Malgeunsoft breach — Source: self-rendered from material submitted to the Personal Information Protection Commission, the Anti-Corruption and Civil Rights Commission, and press reports*

The attacker first broke into a training site server on September 19 and took personal information out the next day, September 20. Malgeunsoft only learned of the breach on September 22, when a client contacted it about spam texts sent from the client's SMS account.

The Personal Information Protection Commission received three leak reports on September 22, 24, and 29, and began an investigation on September 30. It reportedly classified the case internally as a major incident. On October 6, the Anti-Corruption and Civil Rights Commission announced a leak of user information from its Integrity Learning Center, and the same day Malgeunsoft posted an apology in the name of CEO Ha Geun-ho and eight security measures on its website.

The full scale became known on October 13, when Rep. Han Chang-min's office on the National Assembly's National Policy Committee released Personal Information Protection Commission material. The 2.37 million is the figure the company reported, and the Commission is confirming the exact scale.

## Affected institutions and leaked items

![Bar chart of known number of people leaked by client](/assets/images/tech/malgeunsoft-lms-breach/en/03-chart.webp)
*Bar chart of known number of people leaked by client — Source: self-rendered from the Anti-Corruption and Civil Rights Commission's announcement and press reports*

According to Malgeunsoft, the 22 affected sites span the public sector, academia, and private sector. As of October 14, 2026, three have a known scale — the Anti-Corruption and Civil Rights Commission's Integrity Learning Center, the Korea Educational Facility Safety Institute, and the Kia Gwangmyeong plant union — and others are confirmed affected without a disclosed scale.

| Institution | Site | Scale |
| :--- | :--- | :--- |
| Ministry of National Defense | Barracks life counselor training | Undisclosed |
| Korean Commercial Arbitration Board | Arbitration training | Undisclosed |
| KOBACO | Advertising Education Center | **Undisclosed** |

The Integrity Learning Center is a site where people affiliated with public-service-related organizations — public institution employees, private school staff, journalists, and others — complete at least 2 hours of integrity training a year. The Korean Commercial Arbitration Board said information on lawyers and corporate legal staff who took arbitration training leaked, including lawyer registration numbers.

Leaked items vary by site, but per the material submitted to the Personal Information Protection Commission, they include the following.

| Category | Items |
| :--- | :--- |
| Account | ID, encrypted password |
| Contact | Mobile number, email, address |
| Personal | Gender, date of birth, guardian information |
| Identity verification | <mark>Connecting information (CI), duplicate sign-up information (DI)</mark> |
| Site-specific | Affiliation, rank, employee number, license number, etc. |

Malgeunsoft said it doesn't store payment information such as credit card or account numbers, so those aren't among the leaked items. CI is a one-way-encrypted value of the resident registration number used by various services to confirm whether users are the same person, and in principle it can't be changed. What's risky about a CI/DI leak is covered in the post written at the time of the TVING leak.

🔗 Link - https://blog.naver.com/rottensweetpotato/224314384302

## One contractor breached, 22 sites leaked

![Concept image of an outsourcing structure where many institutions' data sits on one contractor's servers](/assets/images/tech/malgeunsoft-lms-breach/04-agy.webp)
*Concept image of an outsourcing structure where many institutions' data sits on one contractor's servers — Source: concept image · self-generated with agy*

When institutions hand their training sites to an LMS company instead of building them themselves, many institutions' member information ends up stored in one company's systems. The attacker didn't need to attack 22 institutions one by one; breaching the single contractor was enough. Rep. Han said Malgeunsoft is the industry leader in this field and that leaks at other client institutions can't be ruled out.

The Anti-Corruption and Civil Rights Commission case also exposed a retention problem. The Commission explained that what leaked was the Learning Center's old database, and that Malgeunsoft keeping it instead of destroying it led to the damage. The Commission is surveying personal information destruction across all its outsourced projects over the last three years.

| Provision | Content |
| :--- | :--- |
| Personal Information Protection Act Article 21 | **Destroy without delay** once the purpose is achieved |
| Personal Information Protection Act Article 26 | The delegator trains and supervises the contractor |

The eight measures Malgeunsoft announced include isolating data by client and narrowing access rights, overhauling destruction procedures including deleting data after contracts end, and managing encryption keys separately from service systems. Whether the measures have actually been applied is something the Personal Information Protection Commission's investigation will confirm.

## How to check your information

![Malgeunsoft personal information leak lookup page](/assets/images/tech/malgeunsoft-lms-breach/05-capture.webp)
*Malgeunsoft personal information leak lookup page — Source: Malgeunsoft*

Malgeunsoft has opened a leak lookup page. After verifying your identity with a code sent to your registered email or mobile number, it shows whether your information leaked and which items.

🔗 Link - https://privacy-check.malgnsoft.com/

As of October 14, 2026, members who signed up via social login can't look themselves up, and SMS verification for members who signed up with a phone number only is in preparation. Because phone lines are hard to get through, inquiries are accepted only by email (privacy2@malgnsoft.com).

A full list of sites using Malgeunsoft's LMS hasn't been published. If you've ever taken public institution integrity training, Ministry of National Defense counselor training, or online training from an association or union, checking is the sure way.

## What users should do

![Summary card of five user actions](/assets/images/tech/malgeunsoft-lms-breach/en/06-items.webp)
*Summary card of five user actions — Source: self-rendered from Malgeunsoft guidance and the Personal Information Protection Act*

Passwords were encrypted, but if you used your training site password elsewhere, it's safer to change it there too. ID, email, and mobile number leaked together and can be used in attacks that try the same combination on other services.

This incident came to light when the attacker sent spam from a client's SMS account. Don't tap links in texts or emails about training completion, retaking courses, or leak compensation; check directly on each institution's website.

## What to watch next

- The actual leak scale and full list of 22 sites to be confirmed by the Personal Information Protection Commission's investigation
- Penalties the outsourcing institutions face over responsibility for managing the contractor
- Confirmation of additional harm at other institutions using Malgeunsoft's LMS
- Whether the government-wide survey of online platforms such as LMSs that the National Assembly called for begins

## Sources

- [[Malgeunsoft] Malgeunsoft's pledge to become the most secure LMS (2026-10-06; image source in the body)](https://www.malgnsoft.com/about/news_view.jsp?id=1020)
- [[Malgeunsoft] Personal information leak lookup and FAQ (image source in the body)](https://privacy-check.malgnsoft.com/)
- [[Financial News] Malgeunsoft reports 2.37 million records leaked: affected institutions and circumstances (2026-10-13)](https://www.fnnews.com/news/202610130601397826)
- [[Boan News] Malgeunsoft's 22 clients, leaked items, eight measures (2026-10-13)](https://www.boannews.com/news/articleView.html?idxno=146361)
- [[Money Today] 100,000 users of the Anti-Corruption and Civil Rights Commission's Integrity Learning Center leaked (2026-10-06)](https://www.mt.co.kr/policy/2026/10/06/2026100622062621154)
- [[SBS Biz] Korean Commercial Arbitration Board lawyer registration numbers leaked (2026-10)](https://biz.sbs.co.kr/amp/article/20000338409)
