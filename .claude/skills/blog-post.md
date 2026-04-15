---
name: blog-post
description: Use when writing a new post for the No1Joon blog. Creates a Jekyll post under `_posts/` while preserving this blog's tone, voice, and structure.
---

Write a new technical blog post for the No1Joon blog. The critical part is preserving this blog's unique tone, voice, and structure.

## When to use

- When the user asks for an **individual post**, e.g. "write a blog post", "add a post", "write an article about ~".
- Use this for **a single standalone post**, not when splitting a whole tech stack into per-category posts (that's the `/tech-blog` skill).

## Voice rules (strict)

**Use 해요체 (polite informal). Never use 합쇼체 (formal).**

The blog is written in Korean. All prose must follow 해요체.

- ❌ "있습니다.", "발생합니다.", "사용합니다.", "됩니다." → ✅ "있어요.", "발생해요.", "사용해요.", "돼요."
- ❌ "~할 수 있습니다." → ✅ "~할 수 있어요."
- ❌ "~입니다." → ✅ "~이에요." / "~예요."
- ❌ "권장합니다." → ✅ "권장해요." or "권장드려요."
- ❌ "~를 다룹니다." → ✅ "~를 다뤄요."

Exceptions:
- Short phrases inside tables and lists may stay in noun form or dictionary form ("빌드 결과물 전달", "설치", "확인", etc.).
- Keep code comments in their original style.
- The `description` field in front matter is a one-line summary — prefer 해요체, and if it sounds awkward, fall back to noun-form endings ("~를 분석", "~를 정리").

## Structure rules

### Front matter (required)

```yaml
---
title: "A title that captures the core idea"
description: One-line summary for search and sharing
date: YYYY-MM-DD
order: 1
category: CI/CD            # one of the categories defined in _data/categories.yml
subcategory: Harness       # a subcategory under that category
tags: [kebab-case, tags]
---
```

- `order`: sort order within the same category. Start from 1 for series posts.
- `category` / `subcategory`: always read `_data/categories.yml` first and use valid values. If missing, ask the user.

### Filename

`_posts/YYYY-MM-DD-slug.md`. For series, use `_posts/YYYY-MM-DD-{series}-{nn}-{topic}.md` (e.g., `2026-04-08-harness-01-overview.md`).

### Body structure

1. **Opening**: state the problem or context in one or two paragraphs. e.g., "~팀이라면 공통적으로 겪는 문제가 있어요."
2. **`##` sections**: concept → structure → real usage. Each section short and purposeful.
3. **Use tables aggressively**: prefer Markdown tables for comparisons, options, type breakdowns over long prose.
4. **Code blocks**: always specify the language (`yaml`, `bash`, `python`, `rego`, etc.).
5. **Diagrams**: use ```` ```mermaid ```` blocks for graphs and architecture. No ASCII art.
   - Directory trees and config hierarchies can stay in plain code blocks since they are already textual structures.
6. **Closing paragraph**: tease the next post ("다음 글에서는 ~를 다뤄요.") or summarize the key points.

### Diagrams

When including mermaid blocks, follow `.claude/skills/mermaid.md`. It defines the color palette, line styles, and node-shape conventions.

### Callout box (use sparingly)

```html
<div class="callout why">
  <div class="callout-title">핵심 차이</div>
  Use one paragraph to emphasize the central claim of the post. Do not overuse.
</div>
```

### Sentence style

- Keep sentences short. Technical terms may appear in the original language alongside a Korean gloss.
- Strip unnecessary intensifiers ("매우", "정말", "굉장히", etc.).
- Use `-` for lists; indent sub-items by 2 spaces.
- Use `**bold**` only on one or two conceptual words. Never bold an entire sentence.

## Workflow

1. Read `_data/categories.yml` to confirm category/subcategory values.
2. Read 1–2 existing posts from `_posts/` as style references.
3. If the user has not specified topic/category/order/tags, ask briefly.
4. Write the file as `_posts/YYYY-MM-DD-slug.md`. Use the `Today's date` value from `CLAUDE.md` for the date.
5. After writing, report only a short summary — do not paste the body back.

## Prohibitions

- No 합쇼체 (`~습니다`, `~합니다`).
- No emojis unless the user explicitly asks for them.
- No marketing superlatives ("최고의", "혁신적인", etc.).
- No performance numbers without a source.
- If a single post grows past 10 `##` sections, consider splitting it.
