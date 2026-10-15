---
title: "College Application System Outage — UwayApply Froze 10 Minutes Before the Deadline"
description: "How the application system froze on the last day of early-admission applications, the deadline extension, and the fairness controversy over relief requests and published competition ratios"
date: 2026-09-18
category: Tech
subcategory: News
tags: [outage, server-down, college-admissions, korea, incident]
image: /assets/og/en-2026-09-18-university-application-outage.png
---

On September 11, 2026, the last day of applications for early admission (susi) for the 2027 university entrance cycle, the application system of agency **UwayApply** froze 10 minutes before the deadline. The server came back about 30 minutes later and the deadline was pushed back by an hour, but 1,588 relief requests and a fairness controversy over published competition ratios followed.

What it means technically for a server to go down is covered separately.

[What Is a Server Outage — Why Servers Stop When Traffic Surges](/en/posts/server-down-explained/)

![Concept image of an application screen that froze just before the deadline](/assets/images/tech/university-application-outage/01-agy-hero.webp)
*Concept image of an application screen that froze just before the deadline — Source: concept image · self-generated with agy*

## Timeline of the incident

![Timeline of the UwayApply outage](/assets/images/tech/university-application-outage/en/02-chart.webp)
*Timeline of the UwayApply outage — Source: self-rendered based on Korea University Newspaper and KCUE announcement reports*

Applicants can submit applications to every university by signing up as a unified member with one of two agencies, UwayApply or JinhakApply. In 2026, early-admission applications to four-year universities ran from September 7 to 11, for at least three days per university.

According to the Hankook Ilbo, **140** universities were scheduled to close applications at 6 p.m. on the 11th. Ten minutes before that, **around 5:50 p.m.**, the UwayApply server failed, and some applicants could not finish submitting applications and paying application fees. Service was restored **around 6:20 p.m.**

The Korean Council for University Education (KCUE) extended the 6 p.m. deadline **by 1 hour to 7 p.m.** in line with its outage response manual. By the Ministry of Education's count, **100** universities actually extended their deadlines. Universities that originally closed after 6 p.m. were not subject to the extension.

The Ministry of Education estimated that **about 1,200** applicants still could not finish within the extra hour. The Hankook Ilbo reported this figure alongside the scale of all early-admission applications, **about 2.61 million** (including duplicates).

## The cause Uway gave

![Concept image of a server that froze under concentrated traffic after an equipment move](/assets/images/tech/university-application-outage/03-agy.webp)
*Concept image of a server that froze under concentrated traffic after an equipment move — Source: concept image · self-generated with agy*

Uway CEO Seong Yun-seok issued an apology on September 14 in KCUE's main conference room. The cause as reported by Korea University Newspaper was that **bug checks were insufficient during a recent equipment move and program upgrade**. The Hankook Ilbo summarized the findings as **overload from a surge of users and conflict errors between programs**.

| Time (September 11) | Situation on Uway's side |
| :--- | :--- |
| Around 17:48 | Abnormal increase in sessions detected |
| Around 17:50 | **Outage confirmed** |
| 18:05–18:10 | Reported to KCUE |
| 18:30 | KCUE requests extension to 19:00 |

The same symptoms also appeared **between 11:40 and 11:50 p.m. on the 10th**, the night before the deadline, and Uway said the cause was the same. A Uway official explained that they could not analyze the cause sufficiently in the short time, and KCUE said it requested emergency measures that night and asked for another inspection the next day.

## Relief review results

![Relief requests, approvals, and final applications](/assets/images/tech/university-application-outage/en/04-chart.webp)
*Relief requests, approvals, and final applications — Source: self-rendered based on Ministry of Education and KCUE announcements*

The Ministry of Education and KCUE accepted relief requests from 9 a.m. on September 14 to 6 p.m. on the 16th, and eligible applicants could submit applications until 10 p.m. on the 16th.

The relief criteria were system records.

[Error record]
An error log must remain from the time of the outage at 5:50 p.m. on the 11th

[Application history]
There must be a record of attempts to write, save, submit, or pay for an application to the university requested

[Multiple applications]
If several were written, only the last one written or edited is recognized

Applicants who couldn't apply through UwayApply and applied to a different university through JinhakApply were also eligible for relief if there was a record for the university they originally meant to apply to.

According to the results announced on September 17, **414** of the **1,588** requests were approved and **354** were actually submitted. The 354 applications were spread across **306 recruitment units and admission tracks at 40 universities**, and the average competition ratio of the 40 universities changed from 9.634 to 1 to 9.635 to 1.

## Distribution by university and the competition-ratio controversy

![Top 7 universities by relief applications](/assets/images/tech/university-application-outage/en/05-chart.webp)
*Top 7 universities by relief applications — Source: self-rendered based on Ministry of Education and KCUE announcements*

The universities with the most relief applications were **Kyungpook National University with 72**, followed by Kyung Hee University with 51 and Chung-Ang University with 48. The Ministry of Education explained that 9 recruitment units had 3 or more applicants granted relief, and that there was no concentration in any particular unit.

In early admission, applicants often choose a department after seeing the competition ratios published just before the deadline, and of the 100 universities that extended the deadline, **17 published competition ratios between 6 and 7 p.m.** These include Sungkyunkwan University, Hanyang University (ERICA), and Sejong University.

| Review stage | Count |
| :--- | :--- |
| Universities that published ratios during the extension | 17 |
| Applications to those universities after publication | 39 |
| Applications submitted after viewing the ratios | <mark>3</mark> |

The Ministry of Education and KCUE decided to recommend that the universities concerned cancel these **3** applications. Among applicants who had already applied before 6 p.m., there were complaints that they had been disadvantaged compared with applicants who could see the ratios during the extension and then apply.

## Next steps and open issues

![Summary of next steps](/assets/images/tech/university-application-outage/en/06-items.webp)
*Summary of next steps — Source: summary of the article · self-rendered*

The Ministry of Education acknowledged a blind spot because the application system runs on contracts between universities and agencies. It said it has no legal authority to investigate a private company but would proceed with an investigation given the seriousness of the matter, and a special investigation team is conducting an on-site investigation of UwayApply **through September 23**.

- Problems confirmed in the investigation will be acted on after reviewing the relevant laws and contractual relationships
- The Ministry of Education said that starting with **regular admission (jeongsi) for the 2027 cycle** it will improve the stability of the application system and its management and oversight, and will also consider reorganizing it into a **public application system**. Whether that means direct government operation, KCUE-led operation, or keeping private agencies with stronger oversight has not been disclosed
- Minister of Education Choi Kyo-jin answered during National Assembly interpellation on September 14 that he would also consider having the Ministry of Education and KCUE manage the application system directly

## Sources

- [[Financial News] Server froze just before early-admission deadline; relief for applicants who couldn't apply under scrutiny (outage time, recovery, extension, 2026-09-12)](https://www.fnnews.com/news/202609120841339656)
- [[Herald Economy] Server froze 10 minutes before early-admission deadline, extended by 1 hour (KCUE announcement, 2026-09-11)](https://biz.heraldcorp.com/article/10871013)
- [[Hankook Ilbo] About 1,200 applicants estimated unable to apply due to server freeze (140 universities, cause, relief criteria, 2026-09-13)](https://www.hankookilbo.com/news/article/A2026091312460004834)
- [[Korea University Newspaper] Uway, whose early-admission system froze, was unstable the day before too (Uway response times, cause, 2026-09-14)](https://news.unn.net/news/articleView.html?idxno=597438)
- [[Financial News] UwayApply CEO apologizes for early-admission application outage (2026-09-14)](https://www.fnnews.com/news/202609141729570249)
- [[Nate News] Ministry of Education inspects Uway and Jinhak systems after application outage (ministry briefing, 2026-09-14)](https://m.news.nate.com/view/20260914n23732)
- [[Korea NGO News] Deadline extended 1 hour after application outage; students who applied first are the victims (fairness controversy)](https://www.ngonews.kr/news/articleView.html?idxno=237958)
- [[Seoul Shinmun] Relief recipients confirmed; 17 universities including Sungkyunkwan published ratios (relief conditions, special investigation team, 2026-09-17)](https://www.seoul.co.kr/news/society/education-news/2026/09/17/20260917010010)
- [[Financial News] 354 final applications after outage; cancellation recommended for 3 submitted after viewing ratios (relief and review results, 2026-09-17)](https://www.fnnews.com/news/202609171541045419)
- [[The Edu] 354 relieved after outage; Ministry of Education considers overhauling application system](https://www.te.co.kr/news/article.html?no=29405)
