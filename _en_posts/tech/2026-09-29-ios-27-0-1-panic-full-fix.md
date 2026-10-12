---
title: "iOS 27.0.1 Released — Fixing the iPhone 18 Pro Panic-Full Reboots"
description: "What iOS 27.0.1 fixes — the panic-full reboots plus camera and touch bugs — and the iOS 26.7.1 update released alongside it"
date: 2026-09-29
category: Tech
subcategory: News
tags: [ios-27, iphone-18-pro, panic-full, apple, software-update]
image: /assets/og/en-2026-09-29-ios-27-0-1-panic-full-fix.png
---

Apple released **iOS 27.0.1** early on September 29, Korea time. The update fixes what came to be called the panic-full issue, in which the iPhone 18 Pro and iPhone 18 Pro Max would freeze and restart after a failed Face ID authentication.

The same update includes fixes for camera color problems and touch unresponsiveness, and **iOS 26.7.1** was released separately for users staying on iOS 26.

![iPhone 18 Pro and iPhone 18 Pro Max](/assets/images/tech/ios-27-0-1-panic-full-fix/01-hero-iphone18pro.webp)
*iPhone 18 Pro and iPhone 18 Pro Max — Source: Apple*

[iPhone 18 Pro Reboots: Apple Reveals the Cause — A Face ID Software Issue](/en/posts/iphone-18-pro-panic-full-cause/)

## Fixes in the release notes

Apple's release notes list three fixes. The wording says **including**, so the update may contain additional bug fixes that aren't listed.

| Fix | Affected |
| :--- | :--- |
| <mark>Restart on Face ID failure</mark> | 18 Pro · 18 Pro Max |
| Color problems in 2x photos | Some 18 Pro · Pro Max |
| Touch unresponsive with Notification and Control Center | No model specified |

It was released at 10:09 a.m. Pacific time on September 28, which is 2:09 a.m. on September 29 in Korea. It is the first fix release, two weeks after iOS 27 shipped, and iPadOS 27.0.1 and visionOS 27.0.1 were released the same day.

Apple's security document states that iOS 27.0.1 has **no published CVE entries**. This is a bug-fix release, not a security update.

## The Face ID reboot fix

![Timeline of the iPhone 18 Pro panic-full response](/assets/images/tech/ios-27-0-1-panic-full-fix/02-chart.webp)
*Timeline of the iPhone 18 Pro panic-full response — Source: self-rendered from Apple's release notes and combined reporting*

The first item in the release notes is **an issue where iPhone 18 Pro and iPhone 18 Pro Max could restart unexpectedly after failing Face ID authentication**. This covers the symptom where failing authentication while opening a locked app would freeze the screen for a few seconds and then restart the device.

Because the device's diagnostic records showed a log named **panic-full**, it was called "panic-full" in Korea. Reports began the day after the September 18 Korean launch, and on September 24, Korea time, Apple said it was a software issue that would be resolved by an update, without replacing devices.

It took five days from official confirmation to release. Apple also kept to the timeline it had announced: early in the week of September 28.

Apple has not elaborated on the cause. The iPhone 18 Pro moved the Face ID infrared camera under the display, and MacRumors took the fact that an update can fix it to mean the component itself is not defective.

## Camera and touch fixes

![Example shot with the iPhone 18 Pro's variable aperture](/assets/images/tech/ios-27-0-1-panic-full-fix/03-photo-aperture.webp)
*Example shot with the iPhone 18 Pro's variable aperture — Source: Apple*

The second item is the camera. It fixes an issue where a small number of iPhone 18 Pro and Pro Max units could show color problems under certain lighting when taking **2x** photos at the **f/1.48** aperture.

The iPhone 18 Pro replaced the main camera's fixed f/1.78 aperture with a four-step variable aperture: f/1.48, f/1.8, f/2.8, and f/4.0. According to MacObserver, 2x photos use part of the main sensor rather than a separate lens, so they follow the main camera's aperture setting.

The third item is **an issue where the touchscreen could become unresponsive when Notification Center and Control Center were opened at the same time**. iDrop News reported that this bug, reproduced by timing a particular swipe gesture, spread on social media as a prank.

Apple did not say whether this is the same as the touch unresponsiveness Macworld reported right after the iPhone 18 Pro launched.

## iOS 26.7.1, released the same day

![Apple logo](/assets/images/tech/ios-27-0-1-panic-full-fix/04-logo-apple.webp)
*Apple logo — Source: Apple*

Devices that haven't updated to iOS 27 got a separate **iOS 26.7.1**. It covers iPhone 11 and later and is a security update fixing one vulnerability that was exploited in real attacks.

| Item | Details |
| :--- | :--- |
| Vulnerability | **CVE-2026-86950** |
| Location | CoreGraphics |
| Type | Out-of-bounds write |
| Impact | Code execution via a crafted file |
| Reported by | Meta Product Security |

Apple said it was aware of a report that this vulnerability may have been exploited in an extremely sophisticated attack against specific individuals on **versions of iOS before iOS 27**. The same fix is included in iPadOS 26.7.1, macOS Tahoe 26.7.1, and macOS Sequoia 15.8.1.

MacRumors concluded that iOS 27 is not affected by this vulnerability. If your device is on iOS 26, it is safer to install 26.7.1 right away, even if you don't update to iOS 27.

## Symptoms outside the fix

This fix is limited to reboots that follow a failed Face ID authentication. Electronic Times (전자신문) reported that there were also reports of reboots while charging or while running apps, but their relation to this patch has not been confirmed.

Financial News (파이낸셜뉴스) also pointed out that the only cause Apple confirmed is Face ID authentication failure, and that it has not been verified whether every reported panic-full shares that cause. If restarts keep repeating after the update with no connection to authentication, it may be a different problem from this bug.

In Korea, Apple Korea told the office of lawmaker Kim Jang-kyum on September 23 that a software update was planned and that individual cases would be handled through AppleCare. As of September 29, no separate guidance had been confirmed for users who had their devices exchanged early in the panic-full reports.

## Summary so far

![iOS 27.0.1 panic-full fix summary](/assets/images/tech/ios-27-0-1-panic-full-fix/05-items.webp)
*iOS 27.0.1 panic-full fix summary — Source: summary of this post · self-rendered*

## What to watch next

- Whether reboot reports continue after installing iOS 27.0.1
- A separate explanation from Apple about reboots while charging or running apps
- Whether Apple Korea issues guidance for users who exchanged their devices
- Whether the official iOS 27.1 release includes further stability fixes

## Sources

- [[Apple] iOS 27.0.1 and 26.7.1 security releases list (confirms no CVEs for 27.0.1)](https://support.apple.com/en-us/100100)
- [[Apple] iOS 26.7.1 security document (CVE-2026-86950, supported devices)](https://support.apple.com/en-us/149226)
- [[MacRumors] Original iOS 27.0.1 release notes and release time (2026-09-28)](https://www.macrumors.com/2026/09/28/apple-releases-ios-27-0-1/)
- [[9to5Mac] iOS 27.0.1 fixes (2026-09-28)](https://9to5mac.com/2026/09/28/apple-releases-ios-27-0-1-for-iphone-heres-whats-new/)
- [[MacRumors] iOS 26.7.1 fixes exploited vulnerability (2026-09-28)](https://www.macrumors.com/2026/09/28/ios-26-7-1-active-exploit-fixed/)
- [[iDrop News] How the touch unresponsiveness bug is reproduced (2026-09-28)](https://www.idropnews.com/news/apple-releases-ios-27-0-1-iphone-18-pro-face-id-fix/268975)
- [[Electronic Times] Korean release and symptoms outside the fix (2026-09-29)](https://www.etnews.com/20260929000291)
- [[Financial News] Scope of the confirmed cause and remaining questions (2026-09-29)](https://www.fnnews.com/news/202609290854105354)
- [[MacRumors] The iPhone 18 Pro's four variable aperture steps](https://www.macrumors.com/how-to/iphone-18-pro-using-variable-aperture/)
- [[MacObserver] Which lens the variable aperture applies to, and 2x shots](https://www.macobserver.com/tips/round-ups/iphone-18-pro-variable-aperture-one-lens-shot-list-four-stops/)
- [[Electronic Times] Apple Korea's position in Korea, AppleCare handling (2026-09-24)](https://www.etnews.com/20260924000017)
