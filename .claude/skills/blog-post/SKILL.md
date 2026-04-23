---
name: blog-post
description: Use when writing a new post for the No1Joon blog. Creates a Jekyll post under `_posts/` while preserving this blog's tone, voice, and structure.
---

Write a new technical blog post for the No1Joon blog. The critical part is preserving this blog's unique tone, voice, and structure.

## When to use

- When the user asks for an **individual post**, e.g., "write a blog post", "add a post", "write an article about ~".
- Use this for **a single standalone post**. If the user is starting a whole new subcategory series, route through `post-plan` first.

## Language policy

The blog is written in **Korean**. Post body, headings, callouts, and most prose must be in Korean.

- Sentence endings are not flexible — **합쇼체만 허용** (해요체·혼용 금지). 톤은 한 포스트 안에서 일관 유지.
- **모든 문장의 마지막(줄바꿈 직전) 마침표(`.`) 제거**. 문장 중간에 있는 마침표는 평소처럼 찍는다. 이 규칙은 본문, 리스트, 표 등 모든 텍스트에 적용된다.
- 단, `v1.0`, `domain.com`, `...`(말줄임표) 등 한글 종결 어미가 아닌 경우의 마침표는 유지한다.
- Short phrases inside tables and lists may stay in noun form or dictionary form (e.g., "빌드 결과물 전달", "설치", "확인").
- Keep code comments in their original language (usually English).
- The `description` field in front matter is a one-line summary — any natural ending is fine, including noun-form endings ("~를 분석", "~를 정리").
- Technical terms may stay in the original language (often English) alongside a Korean gloss when helpful.

## Structure rules

### Front matter (required)

```yaml
---
title: "A title that captures the core idea"
description: One-line summary for search and sharing
date: YYYY-MM-DD
order: 1
category: CI/CD # one of the categories defined in _data/categories.yml
subcategory: Harness # a subcategory under that category
tags: [kebab-case, tags]
---
```

- `order`: sort order within the same subcategory. Start from 1 for series posts.
- `category` / `subcategory`: always read `_data/categories.yml` first and use valid values. If missing, ask the user.

### Filename & location

Posts live under a category-slug subfolder of `_posts/`:

- Path: `_posts/{category-slug}/YYYY-MM-DD-slug.md`
- Series: `_posts/{category-slug}/YYYY-MM-DD-{series}-{nn}-{topic}.md`
- Example: `_posts/ci-cd/2026-04-08-harness-01-overview.md`

`{category-slug}` is the top-level `slug` defined in `_data/categories.yml` (e.g., `ci-cd`, `container-orchestration`, `cloud-infrastructure`, `observability`, `devops-sre`, `development`, `architecture`). If the subfolder does not yet exist (first post in that category), create it. Jekyll recursively scans `_posts/`, so the subfolder does not affect URLs — `permalink: /posts/:title/` is driven by the title.

### Body structure

1. **Opening**: state the problem or context in one or two paragraphs (e.g., "~팀이라면 공통적으로 겪는 문제가 있어요.").
2. **`##` sections**: concept → structure → real usage. Each section short and purposeful.
3. **Explanation first, code last.** Each section follows the order: concept paragraph → table/diagram → code snippet only if needed. Never lead with code and then explain it.
4. **Use tables aggressively.** Prefer Markdown tables for comparisons, options, and type breakdowns over long prose.
5. **Code blocks**: always specify the language (`yaml`, `bash`, `python`, `rego`, etc.).
6. **Diagrams**: use ` ```mermaid ` blocks for graphs and architecture. No ASCII art.
   - Directory trees and config hierarchies may stay in plain code blocks since they are already textual structures.
7. **Closing paragraph**: tease the next post ("다음 글에서는 ~를 다뤄요.") or summarize the key points.

### Code minimization

The reader needs to understand **what and why**, not the full YAML/code dump. Code is a **supporting aid**, not the main content.

- No full config dumps. Extract **5–15 lines** of the essential fields and replace the rest with `...` or an omission comment.
- Do not repeat the same concept in multiple code blocks. Once shown, follow up with prose or tables.
- Include boilerplate (`runs-on`, `steps`, standard imports, etc.) only when it matters for the point.
- If tables and diagrams already convey the idea, skip code entirely. **Code is optional, not default.**

### Visualization policy

Choose visualization based on each section's **cognitive load**. There is no fixed count rule.

- Sections that are hard to grasp (multi-layer structure, ordered flows, abstract relationships) should get visualization **regardless of count**. Multiple diagrams in one section is fine if needed.
- Plain enumeration or definition sections do not need forced visualization. Leave them as prose if prose is enough.

Choice by purpose:

| Situation                              | Recommended visualization |
| -------------------------------------- | ------------------------- |
| Architecture / component relations     | mermaid `flowchart`       |
| Time-ordered call flow                 | mermaid `sequenceDiagram` |
| State transitions / lifecycle          | mermaid `stateDiagram-v2` |
| Options / types / attribute comparison | Markdown table            |
| Config hierarchy / directory tree      | Plain code block          |
| UI screenshots                         | Image (`assets/images/`)  |

For mermaid, follow the palette, node shapes, and edge style rules in `.claude/skills/mermaid/SKILL.md`.

### Callout box (use sparingly)

```html
<div class="callout why">
  <div class="callout-title">핵심 차이</div>
  Use one paragraph to emphasize the central claim of the post. Do not overuse.
</div>
```

### Sentence style (Korean)

- Keep sentences short. Technical terms may appear in the original language alongside a Korean gloss when helpful.
- Strip unnecessary Korean intensifiers: "매우", "정말", "굉장히", "아주" 등.
- Use `-` for bullet lists; indent sub-items by 2 spaces.
- Use `**bold**` on one or two conceptual words only. Never bold an entire sentence.

### Readability — line-break rules

Long solid paragraphs exhaust the reader. Break text **at semantic boundaries** so the eye can rest.

- Keep a paragraph under **2–4 sentences**. If longer, insert a blank line and split into a new paragraph.
- Force a blank line at concept shifts and at cause → effect transitions.
- Always leave **one blank line** before and after lists, code blocks, tables, diagrams, and callouts. Do not glue them to adjacent paragraphs.
- If a sentence exceeds 80 characters, **split it at commas or conjunctions**. Avoid chained Korean endings like "~하는데, ~하고, ~해서" that run on.
- Callouts and emphasis blocks lose their effect when they are packed tight against surrounding text. Give them breathing room.

## Workflow

1. Read `_data/categories.yml` to confirm category/subcategory values and grab the `{category-slug}`.
2. Read 1–2 existing posts from `_posts/{category-slug}/` as style references.
3. If the user has not specified topic/category/order/tags, ask briefly.
4. Write the file as `_posts/{category-slug}/YYYY-MM-DD-slug.md`. Create the subfolder if it does not exist. Use the `Today's date` value from `CLAUDE.md` for the date.
5. After writing, report only a short summary. Do not paste the body back.

## Prohibitions

- No emojis unless the user explicitly asks for them.
- No Korean marketing superlatives: "최고의", "혁신적인", "압도적인" 등.
- No performance numbers without a source.
- If a single post grows past 10 `##` sections, consider splitting it.
