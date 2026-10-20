---
title: "PostgreSQL 19 기능 철회 — AI 코드 리뷰 뒤 11월 정식 출시"
description: "베타 기간에 주요 기능 8~10개가 철회된 PostgreSQL 19 의 출시 일정과, 핵심 커미터가 배경으로 꼽은 LLM 보조 코드 리뷰를 정리합니다"
date: 2026-10-20
category: Tech
subcategory: News
tags: [postgresql, database, code-review, llm, open-source]
image: /assets/og/2026-10-20-postgresql-19-features-reverted.png
---

PostgreSQL 19 정식판 출시 목표일이 2026년 11월 19일로 정해졌어요

베타 기간에 주요 기능 8~10개가 철회됐어요!
핵심 커미터 한 명은 그 배경 중 하나로 **LLM 보조 코드 리뷰**를 꼽았어요

![PostgreSQL 로고](/assets/images/tech/postgresql-19-features-reverted/01-hero-postgresql.webp)
*PostgreSQL 로고*

## 사건 경과

![PostgreSQL 19 기능 철회와 출시 일정 타임라인](/assets/images/tech/postgresql-19-features-reverted/02-chart.webp)
*PostgreSQL 19 기능 철회와 출시 일정 타임라인 — 출처: PostgreSQL 공지, Command Prompt, peter.eisentraut.org 기반 자가 렌더*

9월 24일 Beta 4 공지에서는 RC를 10월 초에, 정식판을 10월 중에 출시할 것으로 예상했어요
실제 RC1은 10월 15일에 나왔어요

RC1 공지는 11월 12일 정기 업데이트의 수정 사항을 반영하려고 RC2를 추가 배포한다고 밝혔어요
정식판 목표는 <mark>11월 19일</mark>이에요

The Register는 AI 리뷰에서 다수의 결함이 발견돼 출시가 지연됐다고 보도했어요

## 철회된 기능

![철회한 기능과 함께 빠진 커밋 수 막대](/assets/images/tech/postgresql-19-features-reverted/03-chart.webp)
*철회한 기능과 함께 빠진 커밋 수 막대 — 출처: Command Prompt 자료 기반 자가 렌더*

Beta 4 공지에 적힌 철회 목록이에요

| 기능 | 내용 | 처리 |
| :--- | :--- | :--- |
| SQL/PGQ | 속성 그래프 질의 | **철회** |
| 온라인 체크섬 | 운영 중 체크섬 켜고 끄기 | 철회 |
| FOR PORTION OF | 기간 단위 수정, 삭제 | 철회 |
| 파티션 병합/분할 | MERGE, SPLIT PARTITIONS | 철회 |
| DDL 출력 함수 | 역할, 테이블스페이스, DB | 제거 |

가장 큰 기능은 2023년 SQL 표준에 추가된 그래프 질의 문법 **SQL/PGQ**예요
9월 7일 철회하면서 관련 커밋 <mark>47개</mark>가 함께 철회됐어요

커밋 메시지가 밝힌 사유는 19 버전 개발 기간 안에 수정하기 어려운 여러 설계 문제였어요
Tom Lane은 19에 포함하면 20 출시 전까지 수정하기 어려운 결함이 나온다고 경고했어요

공지는 이 기능들을 다음 메이저 버전에서 재도입할 수 있도록 이번 버전에서 제외했다고 설명했어요

## AI 코드 리뷰가 한 일

![LLM 코드 리뷰 개념 컷](/assets/images/tech/postgresql-19-features-reverted/04-agy.webp)
*LLM 코드 리뷰 개념 컷 — 출처: 개념 컷, agy 자가 생성*

EDB 소속 커미터 **피터 아이젠트라우트**가 10월 9일 블로그에 배경을 적었어요
철회는 보통 한 주기에 하나 정도인데 이번엔 <mark>8~10개</mark>라고 했어요

LLM 보조 코드 리뷰로 이런 결함을 훨씬 빨리 찾는다고 썼어요
한 기능에 결함이 약 40건 보고되면 작은 수정에도 검토 시간이 들어 개발 기간이 부족해져요

문제가 된 코드는 그런 도구를 실무에 활용하기 전에 작성됐어요
<mark>품질 기준이 코드를 쓴 뒤에 높아진 셈</mark>이라는 설명이에요

**바이브 코딩** 탓은 아니라고 선을 그었어요

LLM 퍼징도 도메인, 복합 타입, 파티션, 뷰, 트리거가 얽힌 버그를 빨리 찾는다고 했어요
그래서 퍼징을 기능 개발 과정에 도입하자고 제안했어요

## 다른 원인

아이젠트라우트가 든 원인은 AI 리뷰 하나가 아니에요

[보안 작업 집중]
4월부터 8월까지 시니어 개발자가 보안 수정에 집중하면서 베타 코드 검토 시간이 감소함

[설계 결함]
일부 기능은 베타 중에 고치기 어려운 구조 문제가 있었음

[기능 조합 범위]
모든 기능이 서로 호환돼야 해서 시험할 조합이 많음

커뮤니티는 더 고치려고 미루기보다 <u>출시 일정을 유지하는 방안</u>을 선택했다고 적었어요
LWN 독자 댓글에서도 LLM 리뷰의 비중을 두고 의견이 갈렸어요

## 19에 남은 기능과 업그레이드

아이젠트라우트는 19가 여전히 좋은 릴리스라고 봤어요
근거로 **REPACK CONCURRENTLY**, 시퀀스 논리 복제, pg_plan_advice를 들었어요

RC1에는 병렬 autovacuum과 REPACK 관련 수정이 여러 건 들어갔어요
COPY의 JSON 출력은 이제 쿼리의 열 이름과 별칭을 키로 써요

18 이하 버전에서 19로 업그레이드하려면 메이저 업그레이드 절차가 필요해요
<u>pg_upgrade 또는 pg_dump, pg_restore</u>로 데이터를 이전해야 해요

국내 클라우드 매니지드 PostgreSQL의 19 지원 일정은 10월 20일 기준 찾지 못했어요
운영 DB라면 정식판과 첫 업데이트 릴리스가 나온 뒤 업그레이드를 검토하는 편이 안전해요

## 앞으로 주목할 점

- 11월 12일 RC2와 함께 나오는 업데이트 릴리스
- 11월 19일 정식판이 **일정대로** 나오는지
- 철회한 기능의 PostgreSQL 20 복귀와 실험적 기능 상태 도입 논의

## 참고 출처

- [[PostgreSQL] PostgreSQL 19 RC 1 Released (RC2, 정식판 일정, 2026-10-15)](https://www.postgresql.org/about/news/postgresql-19-rc-1-released-3409/)
- [[PostgreSQL] PostgreSQL 19 Beta 4 Released (철회 목록, 2026-09-24)](https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/)
- [[peter.eisentraut.org] The reverts will continue until morale improves (2026-10-09)](https://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves)
- [[Command Prompt] Two features just left PostgreSQL 19 (커밋 수, 2026-09)](https://www.commandprompt.com/blog/two-features-just-left-postgresql-19/)
- [[The Register] Postgres 19 delayed after AI reviewers find more bugs than humans can fix (2026-10-16)](https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471)
- [[LWN.net] Eisentraut: The reverts will continue until morale improves (댓글 논쟁)](https://lwn.net/Articles/1100182/)
