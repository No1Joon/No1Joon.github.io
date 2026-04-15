---
name: post-plan
description: Use when the user starts a new subcategory series on the No1Joon blog. Drafts the post count and titles up front so the whole series is planned before any post is written.
---

Plan a subcategory series before writing any individual post. The goal is to agree on **how many posts** and **what each title is** with the user first, and only then hand off to `blog-post` for actual writing.

## When to use

- The user says something like "~에 대한 포스팅해", "~ 시리즈 써줘", "~ 관련해서 글 써보자" for a whole subcategory (e.g., "Kubernetes에 대해 써줘", "AWS 포스팅 시작하자").
- The subcategory has no posts yet, or the user is clearly starting a new series within it.

Skip this skill when:
- The user asks for **one specific post** with a concrete topic ("CSRF 공격에 대해 한 편 써줘"). Use `blog-post` directly.
- The user is editing or improving an existing post.

## Workflow

1. **Confirm the subcategory.** Read `_data/categories.yml` and match the user's topic to a valid `category` / `subcategory`. If ambiguous, ask.
2. **Check existing posts** under `_posts/` for that subcategory. If some exist, the plan should extend (not duplicate) them — continue `order` numbering from the last one.
3. **Draft the plan.** Decide the post count and titles based on the topic's scope. Default to **3–5 posts** for a typical subcategory. Fewer if the topic is narrow, more only when the user explicitly signals depth.
4. **Show the plan in the format below and wait for confirmation.** Do not create files yet.
5. **After the user approves** (or gives edits), hand off to `blog-post` skill for each post. Write one post at a time unless the user asks for bulk generation.

## Plan output format

Present the plan as a compact Markdown table plus a one-line rationale. Keep it short — the point is fast agreement, not a document.

```markdown
## 시리즈 계획 — {Category} / {Subcategory}

| order | 파일명 | 제목 |
|-------|--------|------|
| 1 | `YYYY-MM-DD-{slug}-01-overview.md` | "{구조와 개념을 잡는 개요 글 제목}" |
| 2 | `YYYY-MM-DD-{slug}-02-{topic}.md` | "{두 번째 글 제목}" |
| 3 | `YYYY-MM-DD-{slug}-03-{topic}.md` | "{세 번째 글 제목}" |
| 4 | `YYYY-MM-DD-{slug}-04-advanced.md` | "{고급·운영 관점 마무리 글 제목}" |

**구성 의도**: {왜 이 순서·이 개수로 나눴는지 한 문장}
```

확인 문구는 항상 같이 띄워요: "이 구성으로 진행할까요? 개수·제목·순서 바꾸고 싶으면 알려주세요."

## Title 작성 원칙

- **간결하게.** 제목은 한 줄로 핵심 키워드만. 15자 내외가 이상적, 길어도 25자를 넘기지 않아요.
- **부제 금지.** `—` 로 설명을 덧붙이지 말고 한 구절로 끝내요. 상세 설명은 `description` 에 담아요.
  - ❌ "GitHub Actions 핵심 구조 — Workflow·Job·Step·Action이 맞물리는 방식"
  - ✅ "GitHub Actions 핵심 구조"
- **해요체를 유지**하되, 제목은 명사형·체언 종결도 허용. 예: "Harness 파이프라인 설계".
- 01편은 개요/왜 쓰는가, 마지막 편은 고급·운영·보안 같은 마무리 주제로 두는 게 일반적.
- 중간 편들은 **독립적으로도 읽히도록** 주제를 분리. "Part 2", "계속" 같은 모호한 제목 금지.

## 날짜 정책

- 같은 시리즈 글의 `date` 는 동일하게 맞춰요 (예: 전부 `2026-04-15`).
- `order` 로 정렬되므로 날짜 차이는 불필요해요.
- 날짜는 `CLAUDE.md` 의 `Today's date` 기준.

## Slug 정책

- 파일명 slug: `{subcategory-slug}-{nn}-{short-topic}` — `_data/categories.yml` 의 `slug` 를 그대로 써요.
- `nn`은 두 자리 패딩 (`01`, `02`, ...).

## 금지 사항

- 승인 전에 파일 생성하지 않아요. 플랜만 제시하고 멈춰요.
- 한 번에 여러 포스트를 자동으로 쏟아내지 않아요. 기본은 **한 편씩** 작성.
- 시리즈 규모를 과도하게 크게 잡지 않아요. 10편 넘어가면 두 개의 subcategory·시리즈로 분할 고려.

## 실행 예시

사용자: "Kubernetes에 대한 포스팅해"

스킬 응답:

```
## 시리즈 계획 — Container & Orchestration / Kubernetes

| order | 파일명 | 제목 |
|-------|--------|------|
| 1 | `2026-04-15-kubernetes-01-overview.md` | "Kubernetes 핵심 구조" |
| 2 | `2026-04-15-kubernetes-02-workloads.md` | "Pod와 Workload 오브젝트" |
| 3 | `2026-04-15-kubernetes-03-networking.md` | "Kubernetes 네트워킹" |
| 4 | `2026-04-15-kubernetes-04-operations.md` | "프로덕션 운영 패턴" |

**구성 의도**: 구조 → 워크로드 → 네트워킹 → 운영 순으로 현업에서 접하는 순서대로 쌓아요.

이 구성으로 진행할까요? 개수·제목·순서 바꾸고 싶으면 알려주세요.
```
