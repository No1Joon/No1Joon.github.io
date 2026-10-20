---
title: "PostgreSQL 19 Pulls Features — Official Release in November After AI Code Review"
description: "The release schedule of PostgreSQL 19, which had 8–10 major features reverted during beta, and the LLM-assisted code review a core committer cited as part of the background"
date: 2026-10-20
category: Tech
subcategory: News
tags: [postgresql, database, code-review, llm, open-source]
image: /assets/og/en-2026-10-20-postgresql-19-features-reverted.png
---

The target date for the official release of PostgreSQL 19 has been set for November 19, 2026

8–10 major features were reverted during the beta!
One core committer cited **LLM-assisted code review** as one of the reasons

![PostgreSQL logo](/assets/images/tech/postgresql-19-features-reverted/01-hero-postgresql.webp)
*PostgreSQL logo*

## Timeline

![Timeline of PostgreSQL 19 feature reverts and release schedule](/assets/images/tech/postgresql-19-features-reverted/en/02-chart.webp)
*Timeline of PostgreSQL 19 feature reverts and release schedule — Source: self-rendered based on PostgreSQL announcements, Command Prompt, and peter.eisentraut.org*

The September 24 Beta 4 announcement expected an RC in early October and the official release during October
RC1 actually came out on October 15

The RC1 announcement said an additional RC2 would be released to include fixes from the November 12 regular update
The official release target is <mark>November 19</mark>

The Register reported that the release was delayed after AI review found many defects

## Reverted features

![Bars showing the number of commits removed along with the reverted features](/assets/images/tech/postgresql-19-features-reverted/en/03-chart.webp)
*Bars showing the number of commits removed along with the reverted features — Source: self-rendered based on Command Prompt data*

This is the revert list in the Beta 4 announcement

| Feature | Description | Outcome |
| :--- | :--- | :--- |
| SQL/PGQ | Property graph queries | **Reverted** |
| Online checksums | Turning checksums on and off while running | Reverted |
| FOR PORTION OF | Updates and deletes by time period | Reverted |
| Partition merge/split | MERGE, SPLIT PARTITIONS | Reverted |
| DDL output functions | Roles, tablespaces, databases | Removed |

The biggest feature is **SQL/PGQ**, the graph query syntax added to the SQL standard in 2023
When it was reverted on September 7, <mark>47</mark> related commits were reverted along with it

The reason stated in the commit message was several design problems hard to fix within the version 19 development period
Tom Lane warned that including it in 19 would bring defects that would be hard to fix before 20 is released

The announcement explained that these features were left out of this version so they could be reintroduced in the next major version

## What AI code review did

![Concept shot of LLM code review](/assets/images/tech/postgresql-19-features-reverted/04-agy.webp)
*Concept shot of LLM code review — Source: concept shot, self-generated with agy*

**Peter Eisentraut**, a committer at EDB, wrote about the background on his blog on October 9
He said there is usually about one revert per cycle, but this time there were <mark>8–10</mark>

He wrote that LLM-assisted code review finds such defects much faster
When about 40 defects are reported against one feature, even small fixes take review time and the development period runs short

The code in question was written before such tools were used in practice
His explanation is that <mark>the quality bar rose after the code was written</mark>

He drew a line, saying it was not the fault of **vibe coding**

He said LLM fuzzing also quickly finds bugs involving domains, composite types, partitions, views, and triggers
So he proposed bringing fuzzing into the feature development process

## Other causes

The causes Eisentraut gave are not just AI review

[Focus on security work]
From April to August, senior developers concentrated on security fixes, cutting time for reviewing beta code

[Design defects]
Some features had structural problems hard to fix during beta

[Range of feature combinations]
Every feature has to be compatible with every other, so there are many combinations to test

He wrote that the community chose <u>to keep the release schedule</u> rather than delay it to fix more
Opinions were also split in LWN reader comments over how much weight to give LLM review

## Features left in 19 and upgrading

Eisentraut still saw 19 as a good release
As evidence, he cited **REPACK CONCURRENTLY**, logical replication of sequences, and pg_plan_advice

RC1 included several fixes related to parallel autovacuum and REPACK
COPY's JSON output now uses the query's column names and aliases as keys

Upgrading from 18 or earlier to 19 requires a major upgrade procedure
You need to move the data with <u>pg_upgrade, or pg_dump and pg_restore</u>

As of October 20, I couldn't find 19 support schedules for managed PostgreSQL on Korean clouds
For production databases, it's safer to consider upgrading after the official release and the first update release are out

## What to watch next

- The update release coming with RC2 on November 12
- Whether the official release on November 19 comes out **on schedule**
- The reverted features' return in PostgreSQL 20 and discussion of introducing an experimental feature status

## Sources

- [[PostgreSQL] PostgreSQL 19 RC 1 Released (RC2, official release schedule, 2026-10-15)](https://www.postgresql.org/about/news/postgresql-19-rc-1-released-3409/)
- [[PostgreSQL] PostgreSQL 19 Beta 4 Released (revert list, 2026-09-24)](https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/)
- [[peter.eisentraut.org] The reverts will continue until morale improves (2026-10-09)](https://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves)
- [[Command Prompt] Two features just left PostgreSQL 19 (commit counts, 2026-09)](https://www.commandprompt.com/blog/two-features-just-left-postgresql-19/)
- [[The Register] Postgres 19 delayed after AI reviewers find more bugs than humans can fix (2026-10-16)](https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471)
- [[LWN.net] Eisentraut: The reverts will continue until morale improves (comment debate)](https://lwn.net/Articles/1100182/)
