---
title: "Citizen Lab — First Confirmed Zero-Click Spyware Delivered Just by Viewing an Ad"
description: "How the AdFection attack planted spyware without a click through targeted ad auctions, and what you can do to limit your advertising ID"
date: 2026-10-16
category: Tech
subcategory: News
tags: [spyware, zero-click, malvertising, citizen-lab, ad-tech]
image: /assets/og/en-2026-10-16-adfection-zero-click-ad-spyware.png
---

A device was infected just by having an ad appear on screen. *Exposing AdFection*, a report released on October 15, 2026 by Citizen Lab at the University of Toronto in Canada, is the first to technically confirm an attack that installed spyware without a click through targeted ad auctions. The report named the technique **AdFection** and said at least 45 Al Jazeera devices were attacked through this route in 2024–2025.

![Discover-Tech's structure linking spyware vendors and the ad ecosystem](/assets/images/tech/adfection-zero-click-ad-spyware/01-hero.webp)
*Discover-Tech's structure linking spyware vendors and the ad ecosystem — Source: Citizen Lab*

## What happened

Citizen Lab said Israeli ad company Discover-Tech took part in ad auctions through its own platform, **Controlium**, and sent attack code when an ad was displayed on specific devices. Ad security company Confiant released its own investigation into the same activity on the same day.

- Report number: Citizen Lab Report 195, by six authors including Bill Marczak, John Scott-Railton, and Ron Deibert
- Confirmed victims: at least 45 Al Jazeera devices, attacked in 2024–2025
- Linked spyware: high-confidence link to Candiru (now called Integrity Labs); Bindecy also used Controlium
- Exposure: Discover-Tech ads ran in 75,373 apps and 120,768 websites over four months
- Industry certification: listed on Google and IAB Europe certified vendor lists from 2020 to 2026

TechCrunch reported this as the first confirmed case of government-used zero-click spyware delivered through online ads. Zero-click refers to an attack that infects a device without clicking a link or opening a file.

## Conditions for the attack to work

This attack targets only specific devices. Under the structure the report describes, the attacker must already know the target device's **advertising ID or IP address**. The server checks the device that received the ad and, if it's a target, returns JavaScript code in the response; if not, it returns no code at all. So to non-target users it looks like an ordinary shopping ad, and ad exchanges couldn't detect the malicious code.

| Category | Confirmed | Not confirmed |
| :--- | :--- | :--- |
| Target selection | **Advertising ID, cookie ID, IP** | Part of how identifiers were collected |
| Infected devices | 45, including Al Jazeera Windows machines | Other infections |
| Exposed organizations | NATO, UN, EU agency networks | <mark>Whether exposure = infection</mark> |
| Vulnerabilities used | Candiru's past zero-days | The AdFection attack chain |

The report itself stressed that a record of an ad being shown doesn't mean infection. Ad exposure records turned up at NATO, UN, and EU institutions, government networks in about 20 countries, and semiconductor and defense companies, but actual infection was confirmed only in the Al Jazeera case.

## How spyware was delivered through ad auctions

![The online ad auction structure from advertiser to user](/assets/images/tech/adfection-zero-click-ad-spyware/02-fig.webp)
*The online ad auction structure from advertiser to user — Source: Citizen Lab*

When a webpage or app puts an ad slot up for bidding, real-time bidding (RTB) runs in about 0.1 seconds. During this, the ad exchange sends bidders information such as device type, location, advertising ID, and IP. Discover-Tech used this bid information to find target devices, win the auction, and insert a script tag in the ad that sends requests to its own server (NOAS).

### Time to infection

![Timeline of a Candiru infection from ad display to C&C connection](/assets/images/tech/adfection-zero-click-ad-spyware/03-fig.webp)
*Timeline of a Candiru infection from ad display to C&C connection — Source: Citizen Lab*

Here's the sequence the report reconstructed. At 0 seconds the ad is displayed and the script loads; within 1–2 seconds the target device's browser loads a 1×1 iframe and connects to Candiru's validation server. After 5–10 seconds a device that passes validation connects to the exploit (code attacking a vulnerability) server, and within 1–3 minutes the spyware begins communicating with the C&C (command and control) server. All the user did was open a page with an ad on it.

Citizen Lab found 305 domains and 319 IPs in Candiru's infrastructure between 2022 and 2026. The samples from Al Jazeera shared the infection chain and persistence and obfuscation characteristics Candiru used in 2021.

## The scale in numbers

![Scale from 3.77 billion bids to 45 confirmed infections](/assets/images/tech/adfection-zero-click-ad-spyware/en/04-chart.webp)
*Scale from 3.77 billion bids to 45 confirmed infections — Source: self-rendered from Citizen Lab Report 195*

MyDSP, the bidding platform Discover-Tech used, bid on about 3.77 billion ad impressions from March to June 2026 and won about 11.7% of them. About 19% of bids carried the attack NOAS script tag. By bid count, the countries with the most bid attempts were Yemen, Pakistan, Montenegro, Brazil, and Mexico, in that order, and in Citizen Lab's analysis of MyDSP records, bids per capita were highest in Montenegro.

Citizen Lab estimated that most of the ads were run by Discover-Tech itself without real advertisers. They were dressed up as discount ads for AliExpress and UGREEN, but no actual ad contracts with either company were found, and there wasn't a single purchase conversion.

![Discover-Tech ads on the CBC and Yahoo websites and a sudoku app](/assets/images/tech/adfection-zero-click-ad-spyware/05-fig.webp)
*Discover-Tech ads on the CBC and Yahoo websites and a sudoku app — Source: Citizen Lab*

These ads ran in ordinary places such as the website of Canadian public broadcaster CBC, Yahoo, and an Android sudoku game app.

## Industry response

![Google logo](/assets/images/tech/adfection-zero-click-ad-spyware/06-logo-google.webp)
*Google logo*

Google and IAB Europe removed Discover-Tech from their certified vendor lists in early October 2026, and Google also cut off its ad exchange access. Ad tech company Beeswax stopped Discover-Tech's use of its platform, Vungle (Liftoff) suspended platform access during a review, and Eskimi blocked its account and domains. Bindecy, Intelos, and Xandr hadn't responded by the report's deadline.

Citizen Lab pointed to problems with industry certification. Although Discover-Tech had been linked to spyware for about six years, it was listed among about 2,400 companies on Google's certified external vendor list and about 1,000 on the IAB global vendor list. The report recommended that the ad industry adopt real-time malicious ad detection, mandatory know-your-customer (KYC) checks on counterparties, and external audits of certified vendors.

Candiru was added to the US Commerce Department's sanctions list in November 2021. That year Microsoft counted at least 100 Candiru victims in 10 countries.

## Relevance in Korea

![Personal Information Protection Commission logo](/assets/images/tech/adfection-zero-click-ad-spyware/07-logo-pipc.webp)
*Personal Information Protection Commission logo*

The report doesn't mention any Korean cases or Korean ad networks. In Asia, exposure of government networks in Bhutan, Indonesia, Malaysia, Pakistan, and Thailand was mentioned. Korean users also receive ads through the same global ad exchanges, so structurally they can't be considered unaffected, but no Korean victims have been confirmed.

In Korea, information used for personalized advertising has been treated by the Personal Information Protection Commission as **behavioral information**.

In September 2022, the commission fined Google ₩69.2 billion and Meta ₩30.8 billion for using behavioral information from other sites for personalized ads without consent (in January 2025 the Seoul Administrative Court ruled the penalties lawful), and in January 2024 it announced policy measures to protect behavioral information used for personalized ads.

This regulation deals with collecting and consenting to ad information, not with bid information being used to select attack targets. Citizen Lab recommended that regulators in each country reduce the personal information exchanged in the bidding process and disable advertising IDs on government devices.

## What you can do now

![Five steps to reduce ad-borne attacks](/assets/images/tech/adfection-zero-click-ad-spyware/en/08-items.webp)
*Five steps to reduce ad-borne attacks — Source: self-rendered from Citizen Lab recommendations*

The advertising ID is the first clue for picking targets, so deleting it or limiting its use makes it harder to be singled out through this route. On Android you can delete the advertising ID in the Ads menu in Settings; on Samsung Galaxy it's under Security and privacy > More privacy settings > Ads. On iPhone, go to Settings > Privacy & Security > Tracking and turn off Allow Apps to Request to Track. Menu names vary slightly by device and version.

Citizen Lab recommended trusted ad-blocking extensions, browsers that block tracking, and ad blocking at the router or DNS level. However, since targets can be chosen from an IP address alone, deleting the advertising ID can't block the attack completely. Keeping your operating system and browser up to date to close known vulnerabilities should go along with it.

There's no way for ordinary users to check for themselves whether they've been infected by this attack. The report advised people who may be targets of state-level attacks — journalists, human rights activists, public officials — to ask specialist organizations such as Citizen Lab to inspect their devices. In Korea, if you suspect hacking you can contact the Korea Internet & Security Agency (KISA) 118 counseling center.

🔗 Link - https://www.boho.or.kr/kr/main.do

## What to watch next

- Citizen Lab's announced follow-up report: an analysis of DARK CARTOGRAPHER, which has linked advertising IDs to phone numbers through mobile carrier vulnerabilities
- Positions of Bindecy, Intelos, and Xandr, which didn't respond
- Whether regulators in various countries open investigations into Discover-Tech and Candiru
- Changes to ad exchanges' vetting of certified vendors

## Sources

- [[Citizen Lab] Exposing AdFection, Report 195 (2026-10-15, all figures, structure, and recommendations)](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)
- [[TechCrunch] Citizen Lab says governments are abusing online ads to hack people with zero-click spyware (2026-10-15)](https://techcrunch.com/2026/10/15/citizen-lab-says-governments-are-abusing-online-ads-to-hack-people-with-zero-click-spyware/)
- [[The Register] Spyware vendors found a way to make targeted ads even worse (2026-10-15)](https://www.theregister.com/security/2026/10/15/spyware-vendors-found-a-way-to-make-targeted-ads-even-worse/5303334)
- [[Aju Business Daily] ₩100 billion in fines for Google and Meta, PIPC sanctions unauthorized collection of behavioral information (2022-09-14)](https://www.ajunews.com/view/20220914131004945)
- [[Hankyung Business] Google ₩69.2 billion, Meta ₩30.8 billion fines; Seoul Administrative Court rules penalties lawful (2025-01)](https://magazine.hankyung.com/business/article/202501316327b)
