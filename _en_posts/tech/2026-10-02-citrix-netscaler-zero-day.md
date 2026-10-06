---
title: "Two Citrix NetScaler Zero-Days — Updating Doesn't Remove the Web Shells"
description: "How two NetScaler remote code execution flaws exploited before disclosure unfolded, and why you should check for signs of compromise before you update"
date: 2026-10-02
category: Tech
subcategory: News
tags: [citrix, netscaler, zero-day, rce, webshell]
image: /assets/og/en-2026-10-02-citrix-netscaler-zero-day.png
---

On September 27, 2026, Citrix disclosed eight vulnerabilities in NetScaler ADC and NetScaler Gateway. Two of them, **CVE-2026-88771** and **CVE-2026-88772**, were **zero-days** — exploited in real attacks before the advisory was published.

Both are **RCE (remote code execution)** flaws that let an attacker run commands on the appliance without logging in. The US CISA added both to its Known Exploited Vulnerabilities (KEV) catalog the same day and told federal agencies to act by September 30, and Korea's KISA recommended updating on September 29.

Updating alone doesn't finish the job. Web shells installed by attackers who are already in aren't removed by the update, so analysts are advising operators to check for signs of compromise before updating.

![Citrix logo](/assets/images/tech/citrix-netscaler-zero-day/01-hero-citrix-logo.webp)
*Citrix logo — Source: Wikimedia Commons*

## Timeline

![Timeline of the NetScaler zero-day attacks and response](/assets/images/tech/citrix-netscaler-zero-day/02-chart.webp)
*Timeline of the NetScaler zero-day attacks and response — Source: self-rendered from Unit 42, GTIG, Rapid7, Citrix, CISA, and KISA publications*

According to Unit 42, Palo Alto Networks' threat research team, attempts to fingerprint the versions of more than 100 appliances began around August 21–22. Google Threat Intelligence Group (GTIG) and Mandiant said in an analysis published September 30 that actual attacks had been ongoing since at least early September.

Security firm Rapid7 observed, on customer appliances, a command that compressed the appliance configuration and saved it to a path downloadable over the web on September 20, and a web shell installation on September 24. Citrix's advisory came out three days later, on September 27.

- September 27: Citrix security bulletin CTX697096, CISA alert and KEV listing
- September 29: KISA Boho advisory "Citrix product security update recommended"
- September 30: CISA's deadline for federal agencies; GTIG analysis published
- October 1: Unit 42 analysis updated

## Affected versions

Citrix's advisory lists four supported release lines as affected. Anything below each line's fixed version is affected by all eight.

| Release line | Affected | Fixed |
| :--- | :--- | :--- |
| 14.1 | Before 14.1-73.37 | **14.1-73.37 and later** |
| 13.1 | Before 13.1-64.23 | **13.1-64.23 and later** |
| 14.1 FIPS | Before 14.1-73.37 FIPS | 14.1-73.37 FIPS and later |
| 13.1 FIPS · NDcPP | Before 13.1-37.279 | 13.1-37.279 and later |

Secure Private Access hybrid deployments that use NetScaler are affected too. Citrix has updated the cloud services it runs itself and Adaptive Authentication; the advisory applies only to customer-managed appliances.

## Attack preconditions

![Per-CVE preconditions from the Citrix advisory](/assets/images/tech/citrix-netscaler-zero-day/03-citrix-bulletin.webp)
*Per-CVE preconditions from the Citrix advisory — Source: Citrix (highlighting added)*

The two zero-days have different preconditions. CVE-2026-88771 affects every appliance in its default configuration with no feature that needs to be enabled, so any internet-facing appliance on an affected version should be treated as exposed.

CVE-2026-88772 affects appliances with **DTLS (TLS over UDP)** enabled. That's a condition, but DTLS is on by default for VPN virtual servers, so most NetScaler Gateways used as SSL VPNs fall into it.

| CVE | Type | CVSS v4 |
| :--- | :--- | :--- |
| 88771 | Input validation RCE | <mark>9.5</mark> |
| 88772 | Memory overflow RCE | <mark>9.5</mark> |
| 88773 | HTTP request smuggling | 9.3 |
| 88774 | Policy bypass | 7.0 |
| 88775–88777 | Memory overflow denial of service | 8.8 |
| 88778 | TCP sequence prediction | 8.8 |

Exploitation has been confirmed only for 88771 and 88772; the other six had no reports of exploitation as of the advisory. 88778 is addressed not by updating but by changing TCP settings per Citrix's documentation.

### Checking whether DTLS is in use

![The DTLS configuration line cited in the Citrix advisory](/assets/images/tech/citrix-netscaler-zero-day/04-term-dtls.webp)
*The DTLS configuration line cited in the Citrix advisory — Source: self-rendered from Citrix advisory CTX697096*

Citrix's advisory considers a VPN virtual server affected if the config file doesn't explicitly turn DTLS off. Turning DTLS off avoids only 88772; 88771, which has no precondition, remains.

## What the attacks revealed

The command Rapid7 observed on September 20 compressed the entire appliance configuration and saved it to a web path. Rapid7 explained that this archive contains encrypted passwords, SSL certificates, and SSH keys, and confirmed compromises at two of its customers.

GTIG disclosed two previously unreported tools.

[WHIPSHOT]
A PHP web shell that runs commands hidden in Base64 in HTTP headers and disguises itself with a 404 response

[SLAPSHOT]
A Python tunneling tool that takes commands from WHIPSHOT and relays traffic into the internal network

The attackers modified the web server config file **httpd.conf** so that files with non-script extensions would also run as PHP. The affected sectors GTIG identified were government, finance, technology, education, and legal and professional services, in North America and Europe.

Unit 42 counted 50,277 NetScaler appliances exposed to the internet and potentially vulnerable as of September 27. The published analyses don't mention any Korean victims, and no count of exposed appliances in Korea has been released.

## Why updating isn't enough

In its alert, CISA said to check for indicators of compromise and preserve forensic evidence before updating, because updating can reduce forensic visibility.

Unit 42 noted that updating doesn't revoke the access of attackers who are already inside. The update only closes the vulnerability; an **httpd.conf** modified by the attacker or web shell files they installed stay as they are.

Separately from updating, GTIG called for terminating sessions and rotating credentials. That covers everything stored on the appliance: admin passwords, SSH keys, LDAP-bound accounts, RADIUS secrets, and TLS certificates and private keys.

### Hunting for signs of compromise

![Signs of compromise to check from the NetScaler shell](/assets/images/tech/citrix-netscaler-zero-day/05-term-hunt.webp)
*Signs of compromise to check from the NetScaler shell — Source: self-rendered from GTIG and Rapid7 analyses*

These are the artifact locations GTIG and Rapid7 published. The common recommendation from the analysts is that if you find even one, don't stop at updating — rebuild the appliance from a trusted backup.

## Guidance in Korea

![KISA Citrix product security update advisory](/assets/images/tech/citrix-netscaler-zero-day/06-kisa-notice.webp)
*KISA Citrix product security update advisory — Source: KISA Boho*

On September 29, KISA posted the affected and fixed versions for all eight flaws in a Boho security notice. NetScaler Gateway is used as an SSL VPN for remote work and as the gateway to Citrix virtual desktops, so Korean companies and agencies running these appliances exposed to the internet are affected as well.

If you suspect a compromise, you can report it to KISA's Internet Incident Response Center; the phone number is 118 (no area code).

🔗 Link - https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&menuNo=205020&nttId=72201

## What operators should do

![Summary of operator actions](/assets/images/tech/citrix-netscaler-zero-day/07-items.webp)
*Summary of operator actions — Source: summary of Citrix, CISA, and GTIG guidance · self-rendered*

If you can't update right away, GTIG advises turning DTLS off where operationally possible, blocking inbound UDP port 443 at the perimeter firewall, and restricting allowed source IPs. These measures, too, reduce only the 88772 risk and don't block 88771.

Employees who reach NetScaler through their company VPN have no way to check this themselves. If your company asks you to change your password or log in again, just follow that guidance.

## What to watch next

- Updates to indicators of compromise on Citrix's blog, and the advisory's revision history
- Cases of compromise in Korea and further KISA notices

## Sources

- [[Citrix] CTX697096 NetScaler ADC and Gateway security bulletin (8 CVEs, preconditions, fixed versions; source of one image in this post)](https://support.citrix.com/external/article/697096)
- [[CISA] Critical Zero-Day Vulnerabilities Exploited in Citrix NetScaler ADC, Gateway (2026-09-27)](https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway)
- [[CISA] Known Exploited Vulnerabilities Catalog (date added, due date)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [[Google Threat Intelligence Group] Defending Against Active Exploitation of Citrix NetScaler ADC and Gateway Appliances (2026-09-30)](https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances)
- [[Unit 42] Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 (updated 2026-10-01)](https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/)
- [[Rapid7] Zero-Day Exploitation of Citrix NetScaler ADC and Gateway (observation timeline, web shell paths)](https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772/)
