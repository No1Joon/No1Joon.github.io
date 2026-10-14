---
title: "Windows October Security Update Fixes 1,413 Flaws — 24H2 Reaches End of Support"
description: "The zero-day in the record October monthly update, and what to do about the end of support for Windows 11 24H2 Home and Pro"
date: 2026-10-14
category: Tech
subcategory: News
tags: [windows, patch-tuesday, zero-day, microsoft, windows-11]
image: /assets/og/en-2026-10-14-windows-october-2026-patch.png
---

In its monthly security update on October 13, 2026 (US time), Microsoft fixed **1,413** of its own vulnerabilities. It's another record after September's 999, and six times June's 220 in just four months. One of them is a zero-day (a vulnerability exploited before it's disclosed and patched) that was already being exploited in real attacks.

Support for Windows 11 24H2 Home and Pro also ended the same day. The October update is the last monthly security update for 24H2, so PCs on this version must upgrade to 25H2 or later to keep getting security patches from November.

![Microsoft Security Update Guide October 2026 release notes](/assets/images/tech/windows-october-2026-patch/01-capture-msrc.webp)
*Microsoft Security Update Guide October 2026 release notes — Source: Microsoft*

## The exploited zero-day CVE-2026-96951

The vulnerability Microsoft confirmed as exploited is **CVE-2026-96951** (Windows Shell security feature bypass, CVSS 8.8). Attackers can use it to bypass the MotW (Mark of the Web) defense.

MotW is a mark Windows puts on files downloaded from the internet. With this mark, opening the file first shows a SmartScreen warning or Office's Protected View, but if it's bypassed, the file opens without these warnings.

The attack requires the user to act. According to Microsoft, the attacker has to send a crafted file by email or messenger or lure the user via a link, and if the user doesn't open the file, there's no way to force the attack. Who used it in what attacks hasn't been disclosed.

| Category | CVE | Details |
| :--- | :--- | :--- |
| Exploitation confirmed | <mark>CVE-2026-96951</mark> | Windows Shell MotW bypass |
| Publicly disclosed | CVE-2026-108398 | .NET Framework WDAC bypass |
| Publicly disclosed | CVE-2026-92707 | MessagePack-CSharp denial of service |

CVE-2026-108398 was reported by James Forshaw of Google Project Zero and lets an attacker who already has access to a system bypass enterprise application control (WDAC). Both were publicly disclosed beforehand, but no exploitation has been confirmed.

## What makes up the 1,413

![Chart of October 2026 Microsoft CVEs by impact type](/assets/images/tech/windows-october-2026-patch/en/02-chart.webp)
*Chart of October 2026 Microsoft CVEs by impact type — Source: self-rendered from the Microsoft Security Update Guide*

Nearly half, 677, are elevation of privilege. This type is used by attackers or malware already on a PC to gain administrator rights, so it's abused in multi-stage attacks combined with remote code execution (316) used for initial entry.

| Product family | Vulnerabilities | Updates |
| :--- | :--- | :--- |
| Windows | **1,102** | 39 |
| Office | 134 | 11 |
| Developer tools | 61 | 60 |
| SharePoint Server | 36 | 1 |
| SQL Server | 22 | 8 |
| Azure | 15 | 20 |

Totals differ across outlets — 1,411, 1,413, or 1,760 — because of differences in counting scope. The release notes title says 1,413 Microsoft CVEs, and the table on the same page sums to 1,414. The 1,760 figure adds vulnerabilities in third-party open source that Microsoft redistributes, such as Azure Linux.

## Why the counts grew

![Bar chart of Microsoft CVEs in monthly security updates in 2026](/assets/images/tech/windows-october-2026-patch/en/03-chart.webp)
*Bar chart of Microsoft CVEs in monthly security updates in 2026 — Source: self-rendered from Microsoft Security Update Guide monthly release notes*

Counts that ran 160–220 a month from April to June 2026 rose to 663 in July, 999 in September, and 1,413 in October. Microsoft didn't specifically explain the increase, but wrote on the MSRC blog on October 13 that AI-driven research is contributing to vulnerability discovery and that reviewing many CVEs in groups may become more useful.

Of October's 1,413 Microsoft CVEs, about 70 credit an AI model or AI security company alongside the finder's name. The acknowledgments for the exploited CVE-2026-96951 also include a researcher who used Anthropic's Claude. But the remaining 1,340 or so list only Anonymous or an individual's name, so the acknowledgments alone can't tell you the overall share that used AI.

To handle the larger counts, Microsoft experimentally published risk cohorts that group vulnerabilities with similar checks related to the usage environment, such as 136 in file systems and storage and 135 in Office documents and mail. It said they're not an official classification and don't replace individual assessment.

> Cohorts do not replace careful review of high-severity or actively exploited vulnerabilities. (MSRC, 2026.10.13)

## End of support for Windows 11 24H2

![Microsoft Learn support periods by Windows 11 Home and Pro version](/assets/images/tech/windows-october-2026-patch/04-capture.webp)
*Microsoft Learn support periods by Windows 11 Home and Pro version — Source: Microsoft*

Second-half (H2) versions of Windows 11 Home and Pro get security updates for 24 months after release. 24H2, released in October 2024, reached the end of that period on October 13, 2026 (US Pacific time), and the October cumulative update KB5127648 is its last.

| Version | Released | End of support |
| :--- | :--- | :--- |
| 24H2 | October 2024 | <mark>October 13, 2026</mark> |
| 25H2 | September 2025 | October 12, 2027 |
| 26H2 | September 2026 | October 9, 2028 |

After support ends, the PC still turns on and works, but no new security patches are released. It means that from the November monthly update, vulnerabilities affecting 24H2 won't be fixed even when disclosed. Even on 24H2, Enterprise and Education editions are supported until October 2027.

Windows 10 general support ended in October 2025, and individual users must enroll in Extended Security Updates (ESU) to get patches. Microsoft extended consumer ESU by one year, from October 13, 2026 to October 12, 2027. The October ESU update is KB5126657.

| How to enroll in ESU | Cost |
| :--- | :--- |
| Use PC settings sync (backup) | **Free** |
| Microsoft Rewards | 1,000 points |
| One-time purchase | $30 (₩42,000) |

## Check your PC

![Summary card of five PC checks](/assets/images/tech/windows-october-2026-patch/en/05-items-pc.webp)
*Summary card of five PC checks — Source: self-rendered from Microsoft guidance*

The exploited CVE-2026-96951 bypasses the warning shown when opening downloaded files, so until you've updated, the direct defense is not opening attachments and downloads from unknown sources.

The update from 24H2 to 25H2 enables features on the same base, so it installs quickly. If the feature update doesn't appear on the Windows Update screen, Microsoft may still be rolling it out device by device.

## What to watch next

- Whether the actors who used CVE-2026-96951 in real attacks and their targets are disclosed
- Whether Microsoft CVE counts stay in the 1,000s in the November monthly update
- Whether risk cohorts become an official feature of the Security Update Guide
- Progress of automatic updates to 25H2 and 26H2 on 24H2 Home and Pro devices

## Sources

- [[Microsoft] Security Update Guide October 2026 release notes and CVRF (image source in the body, counts and type tallies)](https://msrc.microsoft.com/update-guide/releaseNote/2026-Oct)
- [[MSRC] Using risk cohorts to prioritize security updates (2026-10-13)](https://www.microsoft.com/en-us/msrc/blog/2026/10/using-risk-cohorts-to-prioritize-security-updates)
- [[Microsoft Learn] Windows 11 Home and Pro lifecycle (image source in the body)](https://learn.microsoft.com/en-us/lifecycle/products/windows-11-home-and-pro)
- [[Microsoft] Windows 10 consumer Extended Security Updates](https://www.microsoft.com/en-us/windows/extended-security-updates)
- [[BleepingComputer] Microsoft October 2026 Patch Tuesday (2026-10-13)](https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2026-patch-tuesday-fixes-1-411-flaws-3-zero-days/)
- Exchange rate: converted at $1 ≈ ₩1,400
