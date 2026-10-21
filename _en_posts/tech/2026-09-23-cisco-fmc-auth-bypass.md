---
title: "CVSS 10.0 Flaw in Cisco's Firewall Management Server — Exploitation Confirmed"
description: "How the Cisco FMC authentication bypass fixed in March became urgent again in September, plus the confirmed attack tooling, fixed releases, and logs to check"
date: 2026-09-23
category: Tech
subcategory: News
tags: [cisco, firewall, vulnerability, authentication-bypass, ransomware]
image: /assets/og/en-2026-09-23-cisco-fmc-auth-bypass.png
---

On September 16, 2026, Cisco updated its security advisory for **CVE-2026-20079**, an authentication bypass in Secure Firewall Management Center (FMC), its firewall management server. The flaw was disclosed and fixed in March, but urgency rose again when it was confirmed to have been used in real attacks from August.

The CVSS score is a maximum 10.0, and a crafted HTTP request alone, with no authentication, can yield root privileges on the server. Cisco said there is no workaround, and updating to a fixed release is the only remedy.

![Cisco logo](/assets/images/tech/cisco-fmc-auth-bypass/01-logo-cisco.webp)
*Cisco logo — Source: Cisco*

## How it unfolded

![Timeline from the disclosure of CVE-2026-20079 to confirmed exploitation](/assets/images/tech/cisco-fmc-auth-bypass/en/02-chart.webp)
*Timeline from the disclosure of CVE-2026-20079 to confirmed exploitation — Source: self-rendered from Cisco, Cisco Talos, and CISA announcements*

Cisco disclosed the flaw, found in its own security testing, on March 4, saying at the time that there were no cases of exploitation. According to BleepingComputer, it updated the advisory on July 29 to add indicators of compromise, and the earliest log entry matching those indicators was July 23.

Cisco's Product Security Incident Response Team (PSIRT) became aware of real-world exploitation in August and officially confirmed it on September 9. The same day, the US Cybersecurity and Infrastructure Security Agency (CISA) added the flaw to its Known Exploited Vulnerabilities (KEV) catalog and directed federal civilian agencies to remediate by September 12.

Advisory v2.6, updated September 16, replaced the interim hotfixes distributed until then with hardened releases. Those releases also include fixes for other vulnerabilities Cisco found internally.

## Attack prerequisites and scope

FMC is a server that manages the policies and settings of multiple Cisco firewalls from one place. For the attack to work, the attacker must have **network access to FMC's web management interface**; no account or user interaction is needed. Cisco wrote that keeping the management interface off the internet reduces the attack surface.

The flaw originates in a system process that is created incorrectly at boot, which an attacker can use to run scripts on the server as root.

| Status | Product |
| :--- | :--- |
| **Affected** | All configurations of Secure FMC software |
| Affected, fixed automatically | Security Cloud Control firewall management |
| Not affected | Secure Firewall Threat Defense (FTD) |
| Not affected | Secure Firewall ASA |
| Not affected | Firewall Device Manager (FDM) |

The FTD and ASA software on the firewall appliances themselves is unaffected. This incident did confirm, however, that when the management server is compromised, an attacker can see the configurations of the firewalls it manages.

Counts of internet-exposed FMC instances vary by search engine. According to security press reports, Censys found about 300 and FOFA 600–700; per-country figures were not published.

## Confirmed intrusions

![Concept image of an intrusion path into a firewall management server](/assets/images/tech/cisco-fmc-auth-bypass/03-agy.webp)
*Concept image of an intrusion path into a firewall management server — Source: concept image · self-generated with agy*

On September 9, Cisco Talos published intrusion activity targeting FMC, grouped into three clusters.

| Cluster | Vulnerabilities used | Outcome |
| :--- | :--- | :--- |
| UAT-12197 | 20079 | Web shell, credential theft |
| UAT-11823 | 20079 · 20316 | <mark>Cyclops Blink installed</mark> |
| UAT-11988 | 20316 | Qilin ransomware deployed |

UAT-11823 replaced license.tmp, the file left as an indicator of compromise, with a malicious file to open a remote shell, collected the configurations of managed firewalls, and installed a variant of the Cyclops Blink malware. Cyclops Blink is known as a tool of Sandworm, a hacking group linked to the Russian government, and Talos classified this cluster as state-linked with high confidence.

**CVE-2026-20316**, used alongside it, was a flaw in which a low-privilege account had a hardcoded password; it was disclosed on July 29 with a CVSS score of 5.3. The score is low, but Talos explained that combined with other flaws it can be used for privilege escalation.

Cisco did not disclose the target industries and countries of the attacking groups or the number of compromised appliances.

## Where this touches Korea

Qilin is the ransomware group behind the **Korean Leaks** incident of September–October 2025, in which data from 28 financial organizations, including asset management firms, was stolen by way of a single Korean IT management company. By Bitdefender's analysis, the leak amounted to more than 1 million files and 2TB.

On September 17, ahead of the Chuseok holiday, the Korea Internet & Security Agency (KISA) issued security checkup recommendations for companies. The checklist included verifying versions and applying security updates for externally exposed services, enabling multi-factor authentication (MFA) on administrator accounts, and keeping ransomware backups isolated. The FMC incident — an exposed management server, a hardcoded-password account, and ransomware deployment — overlaps with all three.

The number of organizations using FMC in Korea, and any cases of damage, cannot be confirmed from public materials.

## Fixed versions

The first fixed version per release, as announced by Cisco on September 16, is as follows.

| Release train | First fixed version |
| :--- | :--- |
| 7.0 and earlier | 7.0.10 |
| 7.2 | 7.2.12 |
| 7.4 | 7.4.8 |
| 7.6 | 7.6.6 |
| 7.7 | 7.7.13 |
| 10.0 | **10.0.2** |
| 10.1 | 10.1.0 |

Cloud-delivered Security Cloud Control firewall management has already been fixed by Cisco and requires no user action.

## What operators should do

![Korea Internet & Security Agency logo](/assets/images/tech/cisco-fmc-auth-bypass/04-logo-kisa.webp)
*Korea Internet & Security Agency logo — Source: KISA*

[Update the version]
Update to at least the first fixed version in your release train. If you applied only an interim hotfix, you must update again to the hardened release.

[Close off exposure]
Until you update, block internet access to the FMC management interface and limit access to the administrative network.

[Check for compromise]
Cisco's advisory says to search the system logs in expert mode and treat traces of **/var/tmp/license.tmp** as suspected compromise. If traces are found, contact Cisco TAC (Technical Assistance Center).

[If already compromised]
Cisco said the hotfix only blocks future exploitation and does not undo an existing compromise. Check the accounts and configurations of the managed firewalls as well.

[Detection rules]
Apply Snort rules 66075–66080, 66883, and 66960–66961.

Incident reports and consultations are handled by KISA at 118.

🔗 Link - https://www.boho.or.kr/

## Summary

![Summary card for the Cisco FMC vulnerability](/assets/images/tech/cisco-fmc-auth-bypass/en/05-items.webp)
*Summary card for the Cisco FMC vulnerability — Source: self-rendered from Cisco's security advisory*

## What to watch next

- Scale of impact: the number of compromised appliances and target industries Cisco has not disclosed
- Additional flaws: individual disclosure of the internally found vulnerabilities bundled into the hardened releases
- Korean guidance: whether KISA's Boho Nara issues separate FMC guidance
- Spread of attacks: scanning for exposed FMC instances and exploitation reports from other groups

## Sources

- [[Cisco] Secure FMC authentication bypass security advisory v2.6 (updated 2026-09-16)](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2)
- [[Cisco Talos] Real-world exploitation of the FMC vulnerability and the three intrusion clusters (2026-09-09)](https://blog.talosintelligence.com/fmc-ongoing-exploitation/)
- [[BleepingComputer] Exploitation confirmed, with a timeline (2026-09)](https://www.bleepingcomputer.com/news/security/cisco-confirms-cve-2026-20079-secure-fmc-flaw-exploited-in-attacks/)
- [[Help Net Security] Exploitation of 20079 and 20316 and behavior by group (2026-09-10)](https://www.helpnetsecurity.com/2026/09/10/cisco-fmc-exploited-cve-2026-20079-cve-2026-20316/)
- [[The Hacker News] CISA KEV listing and the September 12 deadline (2026-09)](https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html)
- [[KISA Boho Nara] Strengthened corporate security checkups and monitoring ahead of the Chuseok holiday (2026-09-17)](https://www.boho.or.kr/kr/bbs/view.do?bbsId=B0000133&nttId=72189&menuNo=205020)
- [[Bitdefender] Analysis of Korean Leaks and Qilin (2025)](https://www.bitdefender.com/en-us/blog/businessinsights/korean-leaks-campaign-targets-south-korean-financial-services-qilin-ransomware)
