---
title: "Chrome 154 Security Update — 11 Critical Among 108 Fixes"
description: "How the Critical vulnerabilities cluster in the graphics layer, whether they were exploited, and when Chromium-based browsers like Edge and Whale pick up the fixes"
date: 2026-09-23
category: Tech
subcategory: News
tags: [chrome, browser-security, chromium, security-update, cve]
image: /assets/og/en-2026-09-23-chrome-154-security-update.png
---

On September 22, 2026, Google released Chrome 154 to the desktop stable channel along with 108 security fixes. Eleven of them are Critical, the highest severity, and most are concentrated in the graphics layer that draws the screen.

Not one entry in the release notes is marked as used in real attacks. Even so, more than 90% of desktop browsers in Korea run the same Chromium engine, so the impact isn't limited to Chrome users.

![Official Google Chrome introduction image](/assets/images/tech/chrome-154-security-update/01-hero-chrome.webp)
*Official Google Chrome introduction image — Source: Google*

## Update overview

Chrome 154's version numbers are **154.0.8037.57** on Linux and **154.0.8037.57/.58** on Windows and Mac. Google said it would roll out over days to weeks. Chrome 154 for Android (154.0.8037.57), released the same day, carries the same security fixes as the desktop version.

There are 108 security fixes, graded 11 Critical, 25 High, 47 Medium, and 25 Low. The release notes state that bug details and links stay restricted until most users have updated.

## Figures by severity

![Chrome 154 security fixes by severity](/assets/images/tech/chrome-154-security-update/02-chart.webp)
*Chrome 154 security fixes by severity — Source: self-rendered from Google Chrome Releases*

Under Chromium's severity guidelines, Critical means a flaw that lets an attacker **read or write files, the registry, or the network on the device with the user's own privileges**. Flaws where code runs only inside the sandbox (the space that isolates web page execution) are graded High.

| Component | Flaw type | Count |
| :--- | :--- | :--- |
| ANGLE | Buffer overflow | <mark>3</mark> |
| GPU | Out-of-bounds write | 2 |
| WebGL | Buffer overflow, out-of-bounds write | 2 |
| ServiceWorker · Fullscreen | Use-after-free | 2 |
| WindowDialog · AdFilter | Use-after-free | 2 |

ANGLE is the layer that translates a web page's graphics commands into operating system graphics APIs such as Windows' Direct3D, and WebGL is the standard by which a web page draws 3D graphics. The graphics layer — ANGLE, GPU, and WebGL combined — accounts for **7** of the 11 Critical fixes.

The remaining 4 are use-after-free, where a program reuses memory it has already released. Across all 108, use-after-free was the most common type at 23.

## Attack prerequisites and scope

From the published descriptions, the common prerequisite for the Critical flaws is **opening a crafted web page**. The grade is high because the path requires no download or installation by the user. Conversely, with bug details restricted, public materials don't show the conditions under which an attack actually succeeds.

| Status | Item |
| :--- | :--- |
| Confirmed | 108 fixes, 11 Critical |
| Confirmed | Affected versions and rollout start date |
| **Not confirmed** | Whether they were exploited in real attacks |
| Not confirmed | Attack conditions per flaw |

Google puts the phrase **exploit exists in the wild** in the release notes for flaws confirmed to be under attack, and the 154 notes don't contain it. Critical is a grade assessed by how much damage a flaw would do if exploited, so it should be read separately from whether exploitation occurred.

Of the 108, 76 were found internally at Google and 32 were reported by outside researchers. Among the 5 with awards set, the highest is $5,000 (₩7 million), and all 3 ANGLE buffer overflows were reported by researchers at Singapore security firm STAR Labs.

## The two-week release cycle and September's zero-days

![Announcement image for the start of Chrome's two-week release cycle](/assets/images/tech/chrome-154-security-update/03-photo-2.webp)
*Announcement image for the start of Chrome's two-week release cycle — Source: Google*

Starting with Chrome 153 on September 8, 2026, Chrome shortened its major update cycle from four weeks to two. Chrome 154 is the second version on this cycle, and the enterprise Extended Stable channel keeps its eight-week cycle while receiving security fixes weekly.

In the three weeks before Chrome 154, two zero-days (vulnerabilities used in attacks before a fix) were patched.

- September 3: **CVE-2026-85046**, a type confusion flaw in the V8 engine, fixed; exploitation confirmed
- September 8: Chrome 153 shipped 230 security fixes and patched **CVE-2026-87491**, an out-of-bounds write in V8; exploitation confirmed

CVE-2026-87491 was reported on August 6 by researcher Jihyeon Jeong of Seoul National University's Compsec Lab, who received a $2,500 (₩3.5 million) award. By SecurityWeek's count, that flaw brings the number of Chrome zero-days confirmed exploited in 2026 to seven.

## The usage picture in Korea

![Desktop browser market share in Korea](/assets/images/tech/chrome-154-security-update/04-chart.webp)
*Desktop browser market share in Korea — Source: self-rendered from Statcounter Global Stats*

By Statcounter's August 2026 figures, desktop browser share in Korea is Chrome 67.84%, Edge 14.88%, Samsung Internet 8.14%, and Whale 4.16%. All four run on the Chromium engine, so together **95.02%** use the same engine.

For Chromium-based browsers, the fix applies only once each company picks up Google's patched code and ships it in its own product. Microsoft wrote in its September 22 security release notes that it was aware of the recent Chromium security fixes and was preparing a fixed build; at that point the Edge stable version was 153.0.4234.48.

Whale and Samsung Internet did not separately announce when they would pick up the 154 fixes. The only way to check is to update to the latest version from each browser's info screen.

## What users and administrators should do

![Concept image of applying a browser update](/assets/images/tech/chrome-154-security-update/05-agy.webp)
*Concept image of applying a browser update — Source: concept image · self-generated with agy*

[Chrome users]
Enter **chrome://settings/help** in the address bar to check for updates, then press the relaunch button to apply.

[Checking the version]
If the version on that same screen is 154.0.8037.57 or later, these fixes are applied.

[Android users]
Update Chrome in Google Play. Chrome for iOS uses the same WebKit engine as Safari, so its structure differs from this list.

[Edge and Whale users]
Get the latest version from the info screen, and apply again once a build incorporating Chromium 154 ships.

[Enterprise administrators]
Organizations on the Extended Stable channel still receive weekly security fixes. If you have policies set to delay updates, review the rollout schedule.

Security notices and incident reports are handled by KISA's Boho Nara, with phone consultations at 118.

🔗 Link - https://www.boho.or.kr/

## Summary

![Summary card for the Chrome 154 security update](/assets/images/tech/chrome-154-security-update/06-items.webp)
*Summary card for the Chrome 154 security update — Source: self-rendered from Google Chrome Releases*

## What to watch next

- Bug details: Google said it will publish the flaw details it kept restricted once most users have updated
- Awards finalized: decisions on awards for the 27 reports still listed as TBD
- Edge adoption: the release of the Chromium 154 fixed build Microsoft said it was preparing

## Sources

- [[Google Chrome Releases] Stable Channel Update for Desktop, the list of 108 Chrome 154 security fixes (2026-09-22)](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0856730748.html)
- [[Chrome for Developers] Announcement of the two-week release cycle (2026-09-08)](https://developer.chrome.com/blog/chrome-two-week-start)
- [[Chromium] Security severity guidelines (definitions of Critical and High)](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/severity-guidelines.md)
- [[SecurityWeek] Chrome 153 and the seventh zero-day of 2026 (2026-09-09)](https://www.securityweek.com/chrome-153-patches-seventh-zero-day-of-2026/)
- [[Help Net Security] CVE-2026-85046 fixed after confirmed exploitation (2026-09-04)](https://www.helpnetsecurity.com/2026/09/04/google-chrome-zero-day-cve-2026-85046/)
- [[Microsoft Learn] Edge security release notes (2026-09-22 entry)](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
- [[Statcounter] Desktop browser market share in South Korea (August 2026)](https://gs.statcounter.com/browser-market-share/desktop/south-korea)
- Exchange rate: converted at $1 ≈ ₩1,400
