---
title: "Kakao Golf Booking and Golfmon Data Leaks — Down to Booking and Payment History"
description: "The leaks at two golf booking apps within three days, how the leaked items differ, and the contacts users should be wary of"
date: 2026-10-10
category: Tech
subcategory: News
tags: [data-breach, kakao, privacy, phishing, incident]
image: /assets/og/en-2026-10-10-golf-booking-app-data-breach.png
---

Personal information leaks were confirmed at two golf course booking apps within three days. Golfmon announced on the 8th that names, phone numbers, and nicknames leaked externally on October 4–5, 2026, and Kakao Golf Booking, run by Kakao VX, confirmed on the 7th that the booking, accommodation, and payment history of about 34,000 domestic tour booking customers had leaked. A leak of only names and phone numbers and a leak that includes payment history call for wariness about different kinds of contact.

![Kakao VX logo](/assets/images/tech/golf-booking-app-data-breach/01-logo-kakaovx.webp)
*Kakao VX logo*

## Timeline

![Timeline of the leaks at two golf booking apps](/assets/images/tech/golf-booking-app-data-breach/en/02-chart.webp)
*Timeline of the leaks at two golf booking apps — Source: self-rendered from Golfmon and Kakao VX notices*

According to Boan News, Golfmon noticed abnormal external access to its website on October 6, and an internal investigation confirmed that customer information had leaked over two days, the 4th and 5th. It sent members a "Personal information leak notice and apology" on the 8th and reported it to the Korea Internet & Security Agency (KISA) and the cyber investigation unit.

Kakao VX confirmed on the 7th that an unauthorized outsider had stolen customer information from Kakao Golf Booking by abnormal means, and posted a notice on its website on the 8th. According to Chosun Biz, it also reported to the Personal Information Protection Commission and KISA.

- Golfmon leak period: October 4–5, noticed on the 6th, notice sent on the 8th
- Kakao Golf Booking leak confirmed: October 7, notice on the 8th
- Kakao Golf Booking affected: about 34,000 customers who booked domestic tour products from January 2025 to October 2026
- Golfmon affected: not confirmed, as the company hasn't disclosed it

Neither company has disclosed the intrusion route. Whether the same attacker targeted both hasn't been confirmed either.

## Leaked items compared

The two incidents differ far more in **what leaked** than in scale. Golfmon's was limited to names, phone numbers, and nicknames, while Kakao Golf Booking's extended to when, at which golf course, and for how much people booked.

| Item | Golfmon | Kakao Golf Booking |
| :--- | :--- | :--- |
| Name, phone number | Leaked | Leaked |
| Nickname | Leaked | Not applicable |
| Product name, round date | Not applicable | **Leaked** |
| Accommodation details | Not applicable | **Leaked** |
| Payment amount, order number | Not applicable | **Leaked** |
| Payment and cancellation times | Not applicable | **Leaked** |
| Virtual account number | Not applicable | <mark>Leaked</mark> |
| Password | Excluded (company statement) | Not among announced items |

Kakao VX said unique identifiers such as card numbers and resident registration numbers weren't included. On Kakao Golf Booking's side, passwords simply aren't listed in the notice; whether they were included wasn't stated separately.

A virtual account number is a deposit number issued to each customer at payment, so the number alone can't be used to withdraw money from a customer's account. But if an attacker knows the number you actually received and the amount you paid, contacts like "your deposit hasn't been confirmed" or "please send the difference" can look like genuine notices.

## Golfmon's second leak in two years

![Golfmon logo](/assets/images/tech/golf-booking-app-data-breach/03-logo-golfmon.webp)
*Golfmon logo*

Golfmon also had member information leaked in a hack in mid-October 2024. That time passwords were included, and the company's position was that they were encrypted and couldn't be decrypted.

| Item | October 2024 | October 2026 |
| :--- | :--- | :--- |
| Name, phone number | Leaked | Leaked |
| Gender | Leaked | Not applicable |
| Password | **Leaked (encrypted)** | Excluded |
| Nickname | Not applicable | Leaked |
| Number affected | Undisclosed | Undisclosed |

The passwords leaked in 2024 were encrypted, but if you use that password on other sites too, you should change it.

## An incident within the scope of ISMS certification

![Kakao VX information security management system (ISMS) certificate, with Kakao Golf Booking in scope](/assets/images/tech/golf-booking-app-data-breach/04-isms-kakaovx.webp)
*Kakao VX information security management system (ISMS) certificate, with Kakao Golf Booking in scope — Source: Kakao VX*

The information security management system (ISMS) certificate posted at the bottom of Kakao VX's website shows certification number **ISMS-KISA-2023-154**, with a scope of operating online services including Friends Screen, Kakao Golf Booking, Kakao Friends Golf, and Smart Home Training. It's valid from November 1, 2023 to October 31, 2026, so this incident occurred during the certification period in a service within its scope.

ISMS is a management system certification audited by KISA that checks whether set protection procedures are in place; it's not a guarantee that breaches won't happen. Going by the validity period on the certificate, Kakao VX's certification expires on October 31, 2026.

Kakao VX also had 10,020 personal information records leaked in a website hack in February 2020, and in January 2021 the Personal Information Protection Commission fined it ₩6 million for violating its duty to take safety measures.

## The repeat-violation penalty question

The amended Personal Information Protection Act, in force from September 11, 2026, raised the penalty cap, previously around 3% of revenue, to **up to 10% of total revenue** for repeated violations through intent or gross negligence within the last three years, for incidents affecting 10 million or more people, and for incidents caused by failing to follow corrective orders.

Golfmon had two incidents within two years, in October 2024 and October 2026, but that alone doesn't make it subject to an aggravated penalty. The Personal Information Protection Commission has to judge separately for each incident whether the duty to take safety measures was violated and whether there was intent or gross negligence, and the results haven't been announced yet.

Kakao VX's previous penalty was in January 2021, outside the three-year window.

The amended law also changed the obligation so that users must be notified as soon as a leak becomes possible, even before it's confirmed. Golfmon posted its notice two days after noticing, and Kakao VX one day after confirming.

## Types of secondary harm

![Concept image of smishing using booking details as bait](/assets/images/tech/golf-booking-app-data-breach/05-agy.webp)
*Concept image of smishing using booking details as bait — Source: concept image · self-generated with agy*

This leak doesn't directly let money be withdrawn from accounts. The risk lies in contacts built on the leaked information.

[Booking change texts]
"Tee time changed" texts with links that get the round date and golf course name exactly right

[Refund or difference payment requests]
Mentioning the actual payment amount and virtual account number to steer transfers to another account

[Accommodation confirmation calls]
Citing the tour product's accommodation details and asking for a verification code to confirm identity

[Spam targeting Golfmon members]
Ads and gambling texts personalized with name, phone number, and nickname

Contacts to Kakao Golf Booking users may match their real booking history, so the details being right doesn't mean it's a legitimate notice. Both companies urged users not to click links from unclear sources and not to respond to requests for personal information or verification codes.

## What users and operators should do

![User action summary card](/assets/images/tech/golf-booking-app-data-breach/en/06-items.webp)
*User action summary card — Source: self-rendered from Kakao VX and Golfmon notices*

Kakao Golf Booking users can check whether their information leaked on the Kakao Golf Booking website; Kakao VX runs a dedicated help center, and the Kakao Golf Booking customer center number listed on Kakao VX's website is **1668-3819**. Golfmon hasn't announced a separate lookup menu, and the notice email sent to members is the way to confirm.

![Korea Internet & Security Agency logo](/assets/images/tech/golf-booking-app-data-breach/07-logo-kisa.webp)
*Korea Internet & Security Agency logo*

If you receive a suspicious text or suffer damage, you can get help or report it at KISA's Personal Information Infringement Report Center (118, no area code).

🔗 Link - https://privacy.kisa.or.kr

Neither company has disclosed the intrusion route, and Golfmon hasn't disclosed the number affected either. Kakao VX said it has completed emergency measures such as blocking external IPs and applying new security policies, and Golfmon said it has blocked the access route and is running a server security check. The intrusion route and number affected are expected to be confirmed by the Personal Information Protection Commission's investigation.

## Sources

- [[Boan News] Golfmon leaks personal information again after two years: leak period, items, reports (2026-10-08)](https://www.boannews.com/news/articleView.html?idxno=146281)
- [[Boan News] Kakao VX Kakao Golf Booking leak: affected users, items, measures (2026-10-09)](https://www.boannews.com/news/articleView.html?idxno=146291)
- [[Chosun Biz] 34,000 Kakao Golf Booking users leaked: notice content, agencies notified (2026-10-08)](https://biz.chosun.com/it-science/ict/2026/10/08/4IRDWMFYJJDSVGYIVUGCHIE6FY/)
- [[iNews24] Kakao Golf Booking leak confirmation and notice dates (2026-10-08)](https://www.inews24.com/view/2013146)
- [[Money Today Network] Golfmon's 2024 incident and the repeat-violation sanction question (2026-10-08)](https://news.mtn.co.kr/news-detail/2026100816185743501)
- [[Kakao VX] Company website: ISMS certification scope, validity, customer center number](https://www.kakaovx.com/)
- [[Newsis] Aggravated penalty conditions and notification duty under the amended Personal Information Protection Act (2026-03-09)](https://www.newsis.com/view/NISX20260309_0003540588)
- [[Etoday] Kakao VX 2020 leak and ₩6 million fine (2021-01-13)](https://www.etoday.co.kr/news/view/1984050)
