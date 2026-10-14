---
title: "PoeLLM Botnet — 3,400 Exposed AI Servers Hijacked for Cryptomining"
description: "The timeline of the PoeLLM botnet that infected exposed servers such as LiteLLM and Ollama, how it hides its command servers, and what server operators should check"
date: 2026-10-13
category: Tech
subcategory: News
tags: [botnet, cryptomining, ollama, litellm, ai-security]
image: /assets/og/en-2026-10-13-poellm-botnet.png
---

More than 3,400 AI servers left exposed on the internet were infected by PoeLLM, a cryptocurrency mining botnet. The analysis was published in early October by Black Lotus Labs, the security research arm of US carrier Lumen.

The infected targets were LLM servers that individuals and labs run themselves, such as LiteLLM and Ollama, and developer tools such as Gotenberg and Gitea. The command server addresses were hidden in four words of a poem posted to GitHub.

![Key image of Lumen Black Lotus Labs' PoeLLM report](/assets/images/tech/poellm-botnet/01-hero-lumen.webp)
*Key image of Lumen Black Lotus Labs' PoeLLM report — Source: Lumen Black Lotus Labs*

## Timeline

Black Lotus Labs named the campaign Canto Incognito and the malware PoeLLM. The poem was first committed to GitHub on April 13, 2026, and large-scale scanning and attacks began in May. The team first discovered this infrastructure in early June while investigating an Ivanti Sentry breach.

![Graph of daily active PoeLLM-infected servers, May to October 2026](/assets/images/tech/poellm-botnet/02-capture.webp)
*Graph of daily active PoeLLM-infected servers, May to October 2026 — Source: Lumen Black Lotus Labs*

- Cumulative infected servers: 3,400+ (per the report summary)
- Peak daily active infections: about 800 (mid-June)
- Command servers (C2) used: at least 12, 3 active as of October
- Affected regions: concentrated in the US and Western Europe

BleepingComputer first reported 2,100, then corrected it to 3,400 after the team updated its live report, and the report body still mentions about 2,200. The report gives 3,400 as the summary figure but doesn't explain the difference between the two numbers. The daily graph is rising again in early October, so the infections haven't ended.

## Infection routes and targeted software

PoeLLM scans the whole internet on ports 3000 and 4000. Port 3000 is the default for the PDF converter Gotenberg, and port 4000 for LiteLLM, a proxy that unifies multiple LLM APIs behind a single address.

![Diagram of the Canto Incognito campaign](/assets/images/tech/poellm-botnet/03-capture.webp)
*Diagram of the Canto Incognito campaign — Source: Lumen Black Lotus Labs*

The vulnerability used against LiteLLM is **CVE-2026-42271**. It's a flaw in which an endpoint that tests an MCP server's connection before saving it (**/mcp-rest/test/connection**) runs the command in the request on the server as is; versions 1.74.2 through 1.83.6 are affected, and it was fixed in 1.83.7, released May 8, 2026. The endpoint originally required an API key, but security firm Horizon3.ai confirmed that chained with a Starlette Host header validation bypass (**CVE-2026-48710**), it becomes unauthenticated remote code execution (RCE). The US CISA added it to its Known Exploited Vulnerabilities (KEV) catalog on June 9.

| Target | Default port | Route stated in the report |
| :--- | :--- | :--- |
| LiteLLM | 4000 | <mark>CVE-2026-42271</mark> |
| Gotenberg | 3000 | Abuse of external exposure |
| Ollama | 11434 | **Route undisclosed** |
| Gitea | 3000 | Route undisclosed |

Once infected, a Linux executable named **libgcrypt** is installed, containing a remote shell, the XMRig and Iron miners, a scanner, and exploit code. Mining proceeds are paid to the Russian mining service Kryptex. Infected servers in turn scan ports 3000 and 4000 to find the next servers to attack, and some were also used in SSH login brute-force experiments.

## Command server addresses hidden in a poem

Infected servers don't hardcode the command server address; they look it up on GitHub each time. A **dash.css** file in an account that forked the official Node.js website repository contains a poem titled *On the Nature of Connection*.

![The poem On the Nature of Connection hiding C2 addresses (as of September 2026)](/assets/images/tech/poellm-botnet/04-capture.webp)
*The poem On the Nature of Connection hiding C2 addresses (as of September 2026) — Source: Lumen Black Lotus Labs*

The malware extracts four words from set positions in the poem, converts them to numbers with a built-in dictionary, and uses the four numbers as an IPv4 address. In the report's example, driver becomes 92 and diode becomes 119. When the operator changes servers, they just edit words in the poem instead of redeploying the malware, and the poem has been edited 11 times so far.

Because infected servers connect to an ordinary GitHub file, block lists don't catch it, and the malware sample stays the same even when command server IPs change. Noting that several C2 servers were routers with exposed admin pages, the team concluded the operator reused hacked routers as command servers.

The operator hasn't been identified. Because the code comments are in Italian and the management server is in Italy, the team assesses it as a financially motivated Italian-speaking group, with medium confidence.

## Exposure in Korea

The Black Lotus Labs report doesn't separately mention harm in Korea.

![Bar chart of the top 6 countries for Ollama servers exposed without authentication](/assets/images/tech/poellm-botnet/en/05-chart-ollama.webp)
*Bar chart of the top 6 countries for Ollama servers exposed without authentication — Source: self-rendered from LeakIX scan data*

When the security search engine LeakIX scanned the internet in February 2026, 12,269 Ollama servers were exposed externally without authentication, and Korea was fifth with 453. This is not the number of PoeLLM infections but the number of servers exposed so anyone can connect.

By default Ollama accepts connections only from its own computer (127.0.0.1), but the moment you change it to **OLLAMA_HOST=0.0.0.0** to reach it from other devices, it's exposed externally without authentication. In that state, third parties can list models, run inference on the server's GPU, and take model files. The report doesn't say how PoeLLM infected Ollama.

[I Ran Gemma 4 on a MacBook — Speed by Size and One Pitfall (in Korean)](/posts/gemma-4-macbook-local/)

## Checks and actions

There's no public scanning tool that lets an individual reliably tell whether they're infected.

![Summary card of PoeLLM checks and actions](/assets/images/tech/poellm-botnet/en/06-items.webp)
*Summary card of PoeLLM checks and actions — Source: self-rendered from Lumen Black Lotus Labs and LeakIX recommendations*

Mining malware often shows itself through CPU or GPU usage staying high for no reason. If server usage looks unusual, check for an unfamiliar process named **libgcrypt** and outbound connections to external ports 3778, 5001, 5002, and 9999. If you suspect infection, start by changing the API keys stored in the proxy, and you can report it to KISA at 118.

🔗 Link - https://github.com/blacklotuslabs/IOCs

## Sources

- [[Lumen Black Lotus Labs] Canto Incognito: Tracking the PoeLLM Malware (primary report; source of 4 images in the body)](https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware)
- [[BleepingComputer] PoeLLM malware infects exposed AI servers in cryptomining attacks (2026-10-07, infection count corrected)](https://www.bleepingcomputer.com/news/security/poellm-malware-infects-exposed-ai-servers-in-cryptomining-attacks/)
- [[Boan News] PoeLLM botnet report (2026-10-08)](https://www.boannews.com/news/articleView.html?idxno=146255)
- [[Horizon3.ai] CVE-2026-42271 chained with CVE-2026-48710 (authentication bypass chain)](https://www.horizon3.ai/cve-2026-42271-chained-with-cve-2026-48710)
- [[GitLab Advisory Database] CVE-2026-42271 affected and fixed versions](https://advisories.gitlab.com/pypi/litellm/CVE-2026-42271/)
- [[Help Net Security] CISA KEV listing (2026-06)](https://www.helpnetsecurity.com/?p=373845)
- [[LeakIX] 12,000 Ollama Instances Exposed (2026-02-23, exposure by country)](https://blog.leakix.net/2026/02/ollama-exposed/)
