---
title: "Hacked Financial Firms Rise to 16 — About 100,000 Personal Records Leaked"
description: "The scope of financial-sector breaches, which more than doubled in nine days, the Financial Services Commission's inspection results, and what customers can do"
date: 2026-10-14
category: Tech
subcategory: News
tags: [data-breach, banking, financial-security, fsc, incident]
image: /assets/og/en-2026-10-14-korea-financial-sector-breaches-16.png
---

Since the Shinhan Bank leak, the number of financial firms with confirmed breaches has risen to 16 as of October 14, 2026. That's more than double the 7 of October 5, nine days earlier, and after banks and savings banks it now spans many parts of the financial sector, including capital companies, online investment-linked finance (P2P lending), virtual asset service providers, and the Korean Federation of Community Credit Cooperatives (MG Saemaeul Geumgo).

The Financial Services Commission (FSC) held its "2nd emergency response meeting" the same day, tallying the leak at **about 100,000 records**, and said that of 555 financial firms inspected, **130** reported security shortcomings.

![First page of the FSC's October 14, 2026 press briefing](/assets/images/tech/korea-financial-sector-breaches-16/01-capture.webp)
*First page of the FSC's October 14, 2026 press briefing — Source: Financial Services Commission*

## Timeline

![Timeline of the serial financial-sector breaches](/assets/images/tech/korea-financial-sector-breaches-16/en/02-chart.webp)
*Timeline of the serial financial-sector breaches — Source: self-rendered from the FSC, company notices, and press reports*

After Shinhan Bank confirmed a leak of information on about 25,000 customers on September 30, breaches were confirmed by October 5 at KB Kookmin, Hana, and BNK Busan banks, Yegaram and Welcome savings banks, and Hyundai Capital. In 5 of those 7, externally exposed business systems used by staff and loan brokers were breached.

The attacks then spread to the secondary financial sector. The Korean Federation of Community Credit Cooperatives was reported to have had the website of its mutual aid business attacked on October 10, leaking information on about 400 members, and the attacker reportedly kept coming back with new IPs even after overseas IPs were blocked. On October 12, KDB Capital and OK Savings Bank reported abnormal access.

P2P lender PFCT posted on its website on September 29 that some user information leaked in an external breach on September 27. That was three days before the Shinhan Bank incident, which is also why the FSC set its counting criterion as "before and after the Shinhan Bank incident."

## The list of 16

![Paragraph in the FSC press briefing confirming 16 firms](/assets/images/tech/korea-financial-sector-breaches-16/03-capture-16.webp)
*Paragraph in the FSC press briefing confirming 16 firms — Source: Financial Services Commission*

In the list the FSC released, 9 firms were added after October 5.

| Sector | Through October 5 | Added October 14 |
| :--- | :--- | :--- |
| Banks | Shinhan, Kookmin, Busan, Hana | - |
| Savings banks | Yegaram, Welcome | **DB, OK** |
| Credit-specialized | Hyundai Capital | **KDB Capital** |
| P2P lending | - | **PFCT, Mouda** |
| Electronic finance | - | **Brightfix** |
| Virtual assets | - | **Streami, Prabang** |
| Mutual finance | - | **Korean Federation of Community Credit Cooperatives** |

![Bar chart of breached financial firms by sector](/assets/images/tech/korea-financial-sector-breaches-16/en/04-chart.webp)
*Bar chart of breached financial firms by sector — Source: self-rendered from the FSC press briefing*

Of the 9 added, four have a known scale from the company or press reports.

| Company | Breach route | Known scale |
| :--- | :--- | :--- |
| KDB Capital | Abnormal external access | **848 customers** |
| Korean Federation of Community Credit Cooperatives | Mutual aid website | About 400 members |
| PFCT | External breach | About 300 users |
| OK Savings Bank | Loan application web page | Reported possible 183 people |

According to reports, the items leaked at KDB Capital are name, resident registration number, and date of birth. DB Savings Bank is on the FSC list, but the company's position is that its security system blocked the attack and no general customer information leaked. Mouda posted a notice that some personal information may have leaked, and the scale and items for Brightfix, Streami, and Prabang hadn't been disclosed as of October 14, 2026.

The FSC said the number of affected firms may rise further as financial firms keep checking themselves against the shared attack IPs.

## What leaked and what didn't

By the FSC's tally, about 100,000 records leaked from the 16 firms. The items include name, contact details, resident registration number, and email; information that could be used immediately for fraudulent payments, such as account passwords and card numbers, hasn't been confirmed.

| Category | Items | Risk |
| :--- | :--- | :--- |
| Leak confirmed | Name, contact, email | Smishing and impersonation |
| Leak confirmed | <mark>Resident registration number</mark> | Identity theft, loan fraud |
| Leak not confirmed | Account password, card number | Immediate fraudulent payment |

When resident registration numbers leak along with contact details, they can be used directly in texts offering compensation that use the leak as bait, or in loan solicitation calls impersonating financial firm staff. The fact that passwords didn't leak doesn't prevent secondary harm.

The Financial Supervisory Service and the Financial Security Institute are investigating whether there's a single attacker and whether AI tools were used. The press release says only that they are "examining in depth the possibility of AI hacking," and doesn't say AI use was confirmed.

## Results of inspecting 555 firms

![Gauge of financial firms that reported shortcomings in the checklist inspection](/assets/images/tech/korea-financial-sector-breaches-16/en/05-chart.webp)
*Gauge of financial firms that reported shortcomings in the checklist inspection — Source: self-rendered from the FSC press briefing*

The FSC received results of the 12-item checklist it sent out at the October 2 meeting from 555 financial firms by October 8. 425 reported being adequate and 130 reported shortcomings, and most of those that reported shortcomings needed fixes on 1–2 items related to security patches and monitoring. Shortcomings were more common among electronic financial businesses and P2P lenders, whose security capabilities are relatively weak.

[Latest security patches not applied]
Systems that haven't fixed vulnerabilities already made public

[Poor management of EOS systems]
Continuing to use equipment and software whose manufacturer support has ended (End of Support)

[No 24-hour monitoring]
No system for real-time attack monitoring at night and on holidays

[Poor attack surface management]
Missing authentication and authorization on external systems; no MFA (multi-factor authentication) on important services

An attack surface is the whole set of systems and touchpoints reachable from outside. Most incidents confirmed through October 5 started not in customer internet banking but on external pages for staff and brokers, and the inspection turned up the same type of shortcomings.

## The FSC's institutional improvement tasks

![Paragraph on vulnerability check frequency in the FSC press briefing](/assets/images/tech/korea-financial-sector-breaches-16/06-capture.webp)
*Paragraph on vulnerability check frequency in the FSC press briefing — Source: Financial Services Commission*

The FSC presented four tasks. It said the specific scope and schedule of the checks will be finalized in consultation with the financial sector, so when they take effect hasn't been set.

| Task | Main content |
| :--- | :--- |
| Full security inspection | Inventory external touchpoints, manage authentication |
| Joint threat response | Share financial firms' detection info on FIRST too |
| Institutionalize ongoing checks | Vulnerability checks **twice a year or more** at large firms |
| Support for small and midsize firms | Consider AI-based joint security monitoring |

The current Electronic Financial Transactions Act and Regulation on Supervision of Electronic Financial Transactions require financial firms to check and assess vulnerabilities once a year (twice a year for external websites). The FSC said it will raise that to twice a year or more starting with large financial firms that have wide attack surfaces and many customers, and add important external touchpoints to the mandatory check list. For places not covered by the Electronic Financial Transactions Act, such as moneylenders and general insurance agencies (GA), it will first circulate response guidance.

FSC Secretary General Shin Jin-chang said cases were found where basics weren't kept despite repeated orders to check following events such as the Lotte Card data leak and the Mythos shock. He also said the FSC will pursue easing network separation regulations.

The state of checks in the banking sector can also be seen in the FSS parliamentary audit material summarized on October 13. Of 4,777 vulnerabilities found in bank penetration tests, 109 still haven't been fixed.

🔗 Link - https://blog.naver.com/rottensweetpotato/224440545245

## What customers can do

This incident isn't the kind customers can prevent by changing passwords. There's also no way for customers to fully check whether their information is included, so the realistic steps are to check notices from your financial firms and block secondary harm using the leaked information.

![Summary card of five customer actions](/assets/images/tech/korea-financial-sector-breaches-16/en/07-items.webp)
*Summary card of five customer actions — Source: self-rendered from FSC and agency guidance*

You can apply for the identity theft prevention service and the personal information exposure accident prevention system below.

🔗 Link - https://www.msafer.or.kr

🔗 Link - https://fine.fss.or.kr

Changing your resident registration number is applied for at your local community service center when a leak raises concern of harm to life, body, or property, and the Resident Registration Number Change Committee reviews it. Don't tap links in texts offering leak compensation or loan limits; it's safer to check directly with the financial firm's main number. Suspicious texts can be reported to KISA at 118.

The circumstances of the 7 incidents through October 5 and the items leaked at each company are covered in the previous post.

🔗 Link - https://blog.naver.com/rottensweetpotato/224432160846

## What to watch next

- Whether more damage turns up at financial firms checking themselves against the shared attack IPs
- Disclosure of the scale and items leaked at Brightfix, Streami, and Prabang
- Investigation results on whether the attacks on the 16 firms share an attacker and whether AI tools were used
- The scope and schedule of the full inspection, and when twice-yearly vulnerability checks at large firms begin
- The Personal Information Protection Commission's investigation and penalty decisions

## Sources

- [[Financial Services Commission] We will fully strengthen the financial security management system to prevent recurrence of financial-sector breaches (2026-10-14; source of 3 images in the body)](https://www.fsc.go.kr/no010101/87927)
- [[Financial News] 16 financial firms confirmed hacked, positions of KDB Capital and DB Savings Bank (2026-10-14)](https://www.fnnews.com/news/202610141843588283)
- [[Money Today] Further attacks on secondary financial sector including Community Credit Cooperatives and OK Savings Bank (2026-10-14)](https://www.mt.co.kr/finance/2026/10/14/2026101415532798160)
- [[Etoday] Scale of leaks at Community Credit Cooperatives and OK Savings Bank (2026-10-14)](https://www.etoday.co.kr/news/view/2635355)
- [[iNews24] Welcome Savings Bank corporate client information, breaches at two P2P lenders (2026-10)](https://inews24.com/view/2011741)
- [[ZDNet Korea] Virtual asset service providers Streami and Prabang included (2026-10-14)](https://zdnet.co.kr/view/?no=20261014161400)
