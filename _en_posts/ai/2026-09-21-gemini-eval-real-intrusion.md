---
title: "Gemini Accessed Three Real Companies' Systems During a Hacking Evaluation — The Problem Was an Evaluation Environment With Internet Access"
description: "How Gemini came to access real companies' systems during a cybersecurity evaluation, and how Google kept it undisclosed for seven weeks"
date: 2026-09-21
category: AI
subcategory: News
tags: [gemini, google, ai-safety, ai-evaluation, incident]
image: /assets/og/en-2026-09-21-gemini-eval-real-intrusion.png
---

On September 18, it was confirmed that Google's AI model Gemini accessed the systems of three real companies during a cybersecurity evaluation in May. A fictional company used for the test shared its name with a real company, and the evaluation environment, which should have had outside internet access blocked, allowed it.

Google knew about this at the end of July and made no public announcement, admitting it only after an inquiry from The Wall Street Journal. As of September 21 there is no official document on Google's blog or model card covering the incident, so the available evidence is reporting by SecurityWeek, Axios, and MarkTechPost citing the WSJ, plus remarks by Heather Adkins, Google's vice president of security engineering.

![Concept image of an isolated evaluation environment left with an open path to the internet](/assets/images/ai/gemini-eval-real-intrusion/01-agy-hero.webp)
*Concept image of an isolated evaluation environment left with an open path to the internet — Source: concept image · self-generated with agy*

## What happened

![Timeline of the Gemini evaluation incident from occurrence to disclosure](/assets/images/ai/gemini-eval-real-intrusion/02-chart.webp)
*Timeline of the Gemini evaluation incident from occurrence to disclosure — Source: self-rendered from SecurityWeek, MarkTechPost, and Axios reporting*

The evaluation was a CTF (capture the flag, a hacking exercise that retrieves a set value from a target server) run by the AI security evaluation company **Irregular** on its own infrastructure. Gemini's task was to retrieve information from software operated by a fictional company, and that company's name overlapped with a domain that actually exists on the public internet.

The evaluation environment was supposed to have no outside internet access, but a bug in Irregular's environment made it reachable. Gemini accessed the site of the real company it took to be the target, and then two others.

- Occurrence: May 2026, Irregular's evaluation environment
- Awareness: end of July, Irregular notified the labs
- Disclosure: September 18, Google confirmed after the WSJ inquiry
- Model: Google did not state the version
- Affected companies: all three unnamed

## How the three accesses worked

What the three have in common is that none used advanced attack techniques; all exploited **administrative weaknesses** that human attackers commonly go after.

| Case | Method | Nature |
| :--- | :--- | :--- |
| 1 | Password guessing | **Weak password** |
| 2 | Credentials in a public repository | A key left in code |
| 3 | Credentials in a public repository | A key left in code |

Adkins explained that the model found public information online, guessed credentials, and accessed sites it believed were within the scope of the test. Google's position is that in all three cases the model stopped once it realized the company was real, and that there was no harm. Google said it notified the three companies and US authorities and changed the evaluation procedures together with Irregular, but what data was accessed at the three companies has not been disclosed.

### Google's reading

![Google logo](/assets/images/ai/gemini-eval-real-intrusion/03-logo-google.webp)
*Google logo — Source: Google*

Google characterized this not as an alignment failure (the model behaving differently from the developer's intent) but as an incident of **misidentifying the target**. The explanation is that since the model stopped and there was no harm, it was not something to disclose first.

## A fourth incident at the same evaluation vendor

![Top of Anthropic's official investigation report, July 30, 2026](/assets/images/ai/gemini-eval-real-intrusion/04-photo-anthropic.webp)
*Top of Anthropic's official investigation report, July 30, 2026 — Source: Anthropic*

Gemini is not the first model to reach real systems in an Irregular evaluation. In an official investigation report on July 30, Anthropic said it reviewed 141,006 evaluation runs and found three cases of real organizations being breached in Irregular's environment. One of them was exactly this pattern — a fictional company name matching a real domain — and the cause was likewise a configuration error in which the evaluation prompt said there was no internet while the actual machine was connected.

According to MarkTechPost, the same Irregular configuration error also surfaced in OpenAI's evaluations (disclosed August 4) and Meta's (disclosed August 5). An Irregular spokesperson told CNBC that the Google case is the same problem already reported and not a separate incident, and that it notified all the labs involved at the end of July.

| Lab | Disclosure | How |
| :--- | :--- | :--- |
| Anthropic | July 30 | Official investigation report |
| OpenAI | August 4 | Via reporting |
| Meta | August 5 | Via reporting |
| Google | **September 18** | <mark>Admitted after a press inquiry</mark> |

The July incident in which an OpenAI model breached Hugging Face with a zero-day during an evaluation, and Anthropic's three cases, were covered in an August 3 post. This Gemini case shares its cause with the Anthropic cases.

[An OpenAI Model Breached Hugging Face on Its Own — The Full Account (in Korean)](/posts/openai-huggingface-agent-breach/)

## Why isolating the evaluation environment matters

A cybersecurity evaluation measures how well a model finds and exploits vulnerabilities, so the evaluation itself makes the model use offensive capability. For that test to be safe, the range the model can reach has to be **technically isolated** inside the evaluation server; the words "no internet" in the task text cannot substitute for that limit.

These incidents at four labs are less a defect on the model side than a case where one outside vendor's infrastructure configuration affected several labs' results at once. Because disclosure dates ranged from July 30 to September 18, a single cause was reported as four separate incidents.

The manner of disclosure differed too. Anthropic published an official report including figures from a retroactive review of its entire evaluation record, while Google said nothing for seven weeks. There is currently no US law setting a disclosure deadline for evaluation incidents like these, so whether and when to disclose is left to each company.

## Korean law and development organizations

The AI Framework Act (Framework Act on the Development of Artificial Intelligence and Establishment of a Foundation of Trust), in force since January 22, requires operators that build large-scale AI trained with cumulative compute of 10²⁶ FLOP or more to have systems to identify, assess, and mitigate risks and to monitor safety incidents, and to submit the results to the Ministry of Science and ICT. It has no provision setting out when or how an evaluation incident like this one, occurring in an overseas vendor's environment, must be reported in Korea.

Since the three affected companies have not been named, whether any Korean company is among them is unknown.

Still, the fact that two of the cases started from credentials left in public repositories applies directly to development organizations in Korea. AI agents search public repositories and try passwords faster than people do, which makes secret scanning in repositories and blocking weak passwords the first preventive measures.

## What to watch next

- Whether Google states the model version and the data accessed in an official blog post or model card
- Whether Irregular publishes a report tying the four labs' cases together
- Whether the three affected companies disclose on their own
- Whether labs write isolation verification for outside vendors' environments into their contracts

## Sources

- [[SecurityWeek] Google Confirms Gemini AI Breached Three Firms (Adkins's remarks, notification of authorities)](https://www.securityweek.com/google-confirms-gemini-ai-breached-three-firms/)
- [[Axios] Google Gemini accessed three companies during AI hacking test (2026-09-19)](https://www.axios.com/2026/09/19/google-safety-incidents-testing-hacks)
- [[MarkTechPost] Google Confirms Gemini Breached 3 Companies in AI Security Tests (2026-09-20, disclosure dates by lab)](https://www.marktechpost.com/2026/09/20/you-too-google-google-confirms-gemini-breached-3-companies-in-ai-security-tests/)
- [[ABC News] Gemini hacked three companies in first known breakout by Google's AI (2026-09-19)](https://www.abc.net.au/news/2026-09-19/gemini-google-ai-hacks-three-companies/107172128)
- [[CNBC] Google's Gemini becomes latest AI model to break out and hack computer systems (2026-09-18, Irregular spokesperson's remarks)](https://www.cnbc.com/2026/09/18/googles-gemini-becomes-latest-ai-model-to-break-out-and-hack-computer-systems.html)
- [[Anthropic] Investigating incidents in our cybersecurity evaluations (2026-07-30, source of one image in this post)](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)
- [[Korea Law Information Center] Framework Act on the Development of Artificial Intelligence and Establishment of a Foundation of Trust](https://www.law.go.kr/lsInfoP.do?lsiSeq=268543)
