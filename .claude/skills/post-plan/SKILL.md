---
name: post-plan
description: Use when the user starts a new subcategory series on the No1Joon blog. Drafts the post count and titles up front so the whole series is planned before any post is written.
---

Plan a subcategory series before writing any individual post. The goal is to agree on **how many posts** and **what each title will be** with the user first, and only then hand off to `blog-post` for actual writing.

## When to use

Trigger when the user asks for a whole subcategory series. Typical Korean phrasings:

- "~에 대한 포스팅해"
- "~ 시리즈 써줘"
- "~ 관련해서 글 써보자"
- e.g., "Kubernetes에 대해 써줘", "AWS 포스팅 시작하자"

Also trigger when the target subcategory has no posts yet, or the user clearly opens a new series within it.

Skip this skill when:

- The user asks for **one specific post** with a concrete topic (e.g., "CSRF 공격에 대해 한 편 써줘"). Use `blog-post` directly.
- The user is editing or improving an existing post.

## Workflow

1. **Confirm the subcategory.** Read `_data/categories.yml` and map the user's topic to a valid `category` / `subcategory`. Record the category's `slug` — it becomes the target folder under `_posts/`. If ambiguous, ask.
2. **Check existing posts** under `_posts/{category-slug}/` for that subcategory. If some exist, the plan should extend (not duplicate) them — continue `order` numbering from the last one. If the folder does not exist yet (first post in this category), plan to create it.
3. **Draft the plan.** Decide the post count and titles based on the topic's scope. Default to **3–5 posts** for a typical subcategory. Fewer if the topic is narrow, more only when the user explicitly signals depth.
4. **Show the plan in the format below and wait for confirmation.** Do not create files yet.
5. **After the user approves** (or gives edits), hand off to the `blog-post` skill for each post. Write one post at a time unless the user asks for bulk generation.

## Plan output format

Present the plan as a compact Markdown table plus a one-line rationale. This output is shown to a Korean-speaking user, so keep user-facing labels in Korean. Keep it short — the point is fast agreement, not a document.

````markdown
## 시리즈 계획 — {Category} / {Subcategory}

| order | 경로                                                                   | 제목                                |
| ----- | ---------------------------------------------------------------------- | ----------------------------------- |
| 1     | `_posts/{category-slug}/YYYY-MM-DD-{sub-slug}-01-overview.md`          | "{구조와 개념을 잡는 개요 글 제목}" |
| 2     | `_posts/{category-slug}/YYYY-MM-DD-{sub-slug}-02-{topic}.md`           | "{두 번째 글 제목}"                 |
| 3     | `_posts/{category-slug}/YYYY-MM-DD-{sub-slug}-03-{topic}.md`           | "{세 번째 글 제목}"                 |
| 4     | `_posts/{category-slug}/YYYY-MM-DD-{sub-slug}-04-advanced.md`          | "{고급·운영 관점 마무리 글 제목}"   |

**구성 의도**: {왜 이 순서·이 개수로 나눴는지 한 문장}
````

Always append the confirmation prompt in Korean, verbatim:

> 이 구성으로 진행할까요? 개수·제목·순서 바꾸고 싶으면 알려주세요.

## Title rules (Korean output)

- **Keep titles concise.** One line, core keyword only. Ideal around 15 Korean characters, never over 25.
- **No subtitle.** Do not append an em-dash description. Put details in the `description` field.
  - ❌ "GitHub Actions 핵심 구조 — Workflow·Job·Step·Action이 맞물리는 방식"
  - ✅ "GitHub Actions 핵심 구조"
- Middle-series posts must **stand alone** as topics. Avoid vague titles like "Part 2" or "계속".

## Date policy

- All posts in one series share the same `date` (e.g., all `2026-04-15`).
- Sorting is driven by `order`, so date differences are unnecessary.
- Use the `Today's date` value from `CLAUDE.md` as the source of truth.

## Slug policy

- Filename slug: `{subcategory-slug}-{nn}-{short-topic}` — use the `slug` defined in `_data/categories.yml` as-is.
- `nn` is two-digit zero-padded (`01`, `02`, ...).

## Prohibitions

- Do not create any file before the user approves the plan. Stop after presenting the plan.
- Do not mass-generate multiple posts automatically. Default is **one post at a time**.
- Do not oversize a series. If it exceeds 10 posts, split into two subcategories/series.

## Example

User: "Kubernetes에 대한 포스팅해"

Skill response:

````
## 시리즈 계획 — Container & Orchestration / Kubernetes

| order | 경로 | 제목 |
|-------|------|------|
| 1 | `_posts/container-orchestration/2026-04-15-kubernetes-01-overview.md` | "Kubernetes 핵심 구조" |
| 2 | `_posts/container-orchestration/2026-04-15-kubernetes-02-workloads.md` | "Pod와 Workload 오브젝트" |
| 3 | `_posts/container-orchestration/2026-04-15-kubernetes-03-networking.md` | "Kubernetes 네트워킹" |
| 4 | `_posts/container-orchestration/2026-04-15-kubernetes-04-operations.md` | "프로덕션 운영 패턴" |

**구성 의도**: 구조 → 워크로드 → 네트워킹 → 운영 순으로 현업에서 접하는 순서대로 쌓아요.

이 구성으로 진행할까요? 개수·제목·순서 바꾸고 싶으면 알려주세요.
````
