---
title: "A Third Citrix NetScaler Zero-Day — Devices Updated in September Are Affected Too"
description: "The scope, fixed builds, and check order for CVE-2026-88779, which targets NetScaler devices that use SAML login"
date: 2026-10-07
category: Tech
subcategory: News
tags: [citrix, netscaler, zero-day, saml, vulnerability]
image: /assets/og/en-2026-10-07-citrix-netscaler-saml-zero-day.png
---

Citrix announced **CVE-2026-88779**, a new zero-day in NetScaler ADC and NetScaler Gateway, on October 3 (local time). It came six days after Citrix fixed eight issues including CVE-2026-88771 on September 27, and once again attacks were confirmed before the advisory.

Devices configured to use SAML login are affected, and traffic sent without logging in can bring down the authentication function. Builds updated in September (14.1-73.37 and 13.1-64.23) are also affected, so you need to update **once more, to 14.1-73.41 or 13.1-64.28 or later**.

[Two Citrix NetScaler Zero-Days — Updating Doesn't Remove the Web Shells](/en/posts/citrix-netscaler-zero-day/)

![Citrix logo](/assets/images/tech/citrix-netscaler-saml-zero-day/01-hero-citrix-logo.webp)
*Citrix logo*

## Timeline

![Timeline of NetScaler vulnerability advisories and responses](/assets/images/tech/citrix-netscaler-saml-zero-day/en/02-chart.webp)
*Timeline of NetScaler vulnerability advisories and responses — Source: self-rendered from Citrix, CISA, KISA, and NVD announcements*

In security bulletin **CTX697174**, Citrix described CVE-2026-88779 as a memory overflow vulnerability, said it had observed targeted attacks against unpatched devices, and said it could lead to denial of service. Its severity is **8.7** (high) under CVSS v4.

The next day, October 4, the US CISA added the vulnerability to its Known Exploited Vulnerabilities (KEV) catalog and told federal civilian agencies to act by **October 7**. Following the two September flaws (CVE-2026-88771 and 88772), it was the third vulnerability in the same device added to KEV within ten days.

- October 3 (local time): Citrix security bulletin CTX697174
- October 4: CISA KEV listing, NVD entry
- October 5: Canadian Centre for Cyber Security advisory AV26-996
- October 6: KISA Boho Nara "Citrix product security update advisory"

## Preconditions for the attack

![Commands for checking NetScaler SAML configuration](/assets/images/tech/citrix-netscaler-saml-zero-day/en/03-term-saml.webp)
*Commands for checking NetScaler SAML configuration — Source: self-rendered from Citrix bulletin CTX697174*

This vulnerability applies only when the device is configured as a **SAML SP (service provider) or SAML IdP (identity provider)**. SAML is a single sign-on (SSO) standard that lets one company account log in to many services, and organizations that integrate Gateway with corporate login such as Microsoft Entra ID or Okta fall into this group.

Conversely, devices that don't use SAML aren't affected by this one. Having a precondition is what sets it apart from September's CVE-2026-88771.

| Vulnerability | Condition | Attack result |
| :--- | :--- | :--- |
| CVE-2026-88771 | All default configurations | Remote code execution |
| CVE-2026-88772 | Gateway with DTLS on | Remote code execution |
| CVE-2026-88779 | <mark>SAML SP or IdP configuration</mark> | Denial of service |

If the configuration file has an **add authentication samlAction** line, the device acts as an SP; if it has an **add authentication samlIdPProfile** line, it acts as an IdP. If neither is there, the device doesn't meet this vulnerability's precondition, but it still needs updating because of the September flaws.

## Why the September update doesn't block it

CVE-2026-88779 is a separate flaw from the eight fixed in September, so the September 27 builds don't fix it. The affected-version baseline listed by NVD and KISA sits one step above the September fixed versions.

| Branch | September fixed version | October fixed version |
| :--- | :--- | :--- |
| 14.1 | 14.1-73.37 | **14.1-73.41** |
| 13.1 | 13.1-64.23 | **13.1-64.28** |
| 14.1 FIPS | 14.1-73.37 FIPS | **14.1-73.41 FIPS** |
| 13.1 FIPS/NDcPP | 13.1-37.279 | **13.1-37.282** |

Operators who rushed to update in September will need to schedule maintenance again within a month if they use SAML. If you run a high-availability (HA) pair, both nodes must be updated, and customer-managed devices are the ones affected.

## What was observed in attacks

The impact Citrix has officially stated goes as far as **denial of service**. Sending traffic that triggers the memory overflow stops the process that handles authentication or restarts the device, and VPN access and SSO login are unavailable in the meantime.

BleepingComputer reported that there were reports of devices rebooting for no apparent reason from October 3, and that some researchers found traces of authentication attempts with usernames containing shell commands and records of files downloaded from external servers. Citrix hasn't confirmed whether these observations led to code execution.

There is a precedent: in 2025, CVE-2025-6543 was first announced as a denial of service and later confirmed to have been exploited for remote code execution. That's why security companies recommend not treating devices with reboot records as simple outages, and checking for compromise as well.

Security media reported that the Australian Cyber Security Centre (ACSC) also issued an alert, saying it had received reports of harm from Australian organizations. The number of affected organizations and any cases in Korea haven't been disclosed.

## Advisory in Korea

![KISA Citrix product security update advisory, 2026-10-06](/assets/images/tech/citrix-netscaler-saml-zero-day/04-kisa-notice.webp)
*KISA Citrix product security update advisory, 2026-10-06 — Source: KISA*

On October 6, KISA posted six lines of affected and fixed versions for CVE-2026-88779 in a Boho Nara security notice. It is the second Citrix advisory, following the September 29 notice.

NetScaler Gateway is used as an SSL VPN for remote work and as the gateway to Citrix virtual desktops, so it applies to Korean companies and institutions that expose this device to the internet integrated with SAML login. The number of exposed devices in Korea hasn't been announced.

If you suspect a breach, you can report it to KISA's Internet Incident Response Center; the phone number is **118** with no area code.

🔗 Link - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72209

## What operators should do

![Operator action summary](/assets/images/tech/citrix-netscaler-saml-zero-day/en/05-items.webp)
*Operator action summary — Source: self-rendered from Citrix and KISA notices*

There's nothing individual users need to do directly. If your company VPN suddenly went down in early October, it may be a device problem, so let your internal IT department know.

For operators, the order matters: preserve ns.log and core dumps before updating. Updating reboots the device and wipes traces left in memory, and crash records are the basis for judging whether it was an attack. Checking for signs of compromise from the September flaws (CVE-2026-88771 and 88772) remains necessary separately from this update.

## What to watch next

- Whether Citrix adds impacts beyond denial of service (code execution) to the bulletin
- Exploitation analyses published after the CISA deadline (October 7)
- Additional KISA notices and announcements of cases in Korea
- Whether more vulnerabilities turn up in the same SAML handling code

## Sources

- [[Citrix] CTX697174 NetScaler ADC and Gateway security bulletin (CVE-2026-88779, fixed versions)](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174)
- [[CISA] Known Exploited Vulnerabilities Catalog, CVE-2026-88779 (listed 2026-10-04, deadline 10-07)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [[NVD] CVE-2026-88779 details (affected versions)](https://nvd.nist.gov/vuln/detail/CVE-2026-88779)
- [[KISA Boho Nara] Citrix product security update advisory (2026-10-06; source of 1 image in the body)](https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72209)
- [[Canadian Centre for Cyber Security] Citrix security advisory AV26-996 (2026-10-05)](https://cyber.gc.ca/en/alerts-advisories/citrix-security-advisory-av26-996)
- [[BleepingComputer] Citrix patches NetScaler SAML zero-day exploited in attacks (reboot reports, researcher observations)](https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/)
- [[Tenable] Citrix NetScaler zero-day FAQ (comparison of September and October fixed versions)](https://www.tenable.com/blog/frequently-asked-questions-about-reported-citrix-netscaler-zero-day-vulnerabilities)
