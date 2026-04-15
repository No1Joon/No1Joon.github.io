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
3. **설명 우선, 코드는 최소한**: 각 섹션은 `개념 한 문단 → 표·다이어그램 → 필요하면 코드 발췌` 순으로 써요. 코드를 먼저 던지고 해석을 붙이지 않아요.
4. **Use tables aggressively**: prefer Markdown tables for comparisons, options, type breakdowns over long prose.
5. **Code blocks**: always specify the language (`yaml`, `bash`, `python`, `rego`, etc.).
6. **Diagrams**: use ```` ```mermaid ```` blocks for graphs and architecture. No ASCII art.
   - Directory trees and config hierarchies can stay in plain code blocks since they are already textual structures.
7. **Closing paragraph**: tease the next post ("다음 글에서는 ~를 다뤄요.") or summarize the key points.

### 코드 최소화 원칙

읽는 사람이 이해해야 할 건 **"무엇을 왜 하는가"** 이지 YAML·코드 전문이 아니에요. 코드는 개념을 **보조하는 용도로만** 넣어요.

- 전체 설정 덤프 금지. 핵심 필드 **5~15줄** 만 발췌하고 나머지는 `...` 또는 생략 주석.
- 같은 개념을 여러 번 코드로 반복하지 않아요. 한 번 보여줬으면 그 다음은 문장·표로.
- 반복되는 보일러플레이트(`runs-on`, `steps`, 표준 import 등)는 맥락상 필요할 때만 포함.
- 코드 없이 표와 다이어그램만으로 전달되면 그렇게 해요. 코드는 **기본값이 아니라 선택**이에요.

### 시각화 방침

시각화 도구 선택은 섹션의 **이해 난이도** 에 맞춰요. 고정된 개수 규칙은 없어요.

- **이해가 어려운 섹션**(구조가 여러 겹, 흐름에 순서가 있음, 추상적 관계 등)에는 **개수 상관없이** 시각화를 넣어요. 필요하면 한 섹션에 여러 개도 괜찮아요.
- **단순 열거·정의** 섹션에는 시각화를 억지로 넣지 않아요. 산문만으로 충분하면 그대로 둬요.

용도별 선택:

| 상황 | 권장 시각화 |
|------|-------------|
| 아키텍처·컴포넌트 관계 | mermaid `flowchart` |
| 시간 순 호출 흐름 | mermaid `sequenceDiagram` |
| 상태 전이·라이프사이클 | mermaid `stateDiagram-v2` |
| 옵션·타입·속성 비교 | 표 (Markdown table) |
| 설정 계층·디렉토리 트리 | plain code block |
| UI 스크린샷 등 실제 화면 | 이미지 (`assets/images/`) |

mermaid 작성 시에는 `.claude/skills/mermaid.md` 의 색상 팔레트·노드 모양·선 스타일 규칙을 따라요.

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
