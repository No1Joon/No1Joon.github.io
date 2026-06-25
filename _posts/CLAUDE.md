# _posts/

Jekyll 블로그 포스트 디렉터리. 카테고리 slug 기준으로 서브폴더에 분리.

## Structure

- `_posts/{category-slug}/` — 각 최상위 카테고리의 포스트.
- 카테고리 slug 목록 (`_data/categories.yml` 기준): `daily-dev`, `tech`.
- Daily Dev 네이밍: `_posts/daily-dev/YYYY-MM-DD-{slug}.md` (subcategory/order prefix 없음).
- Tech / Explainer 네이밍: `_posts/tech/YYYY-MM-DD-{slug}.md`. 한 주제를 깊게 파고드는 단편 또는 시리즈(`-01-`, `-02-` …)로 작성.
- Jekyll 은 `_posts/` 하위를 재귀 스캔 — 서브폴더는 URL 에 영향 없음 (`permalink: /posts/:title/`).

## Skills

- `.claude/skills/post-plan/SKILL.md` — 시리즈로 갈 가치가 있는 주제일 때만 사용 (편수·각 편 핵심 질문 확정).
- `.claude/skills/blog-post/SKILL.md` — Tech / Explainer 등 깊이 있는 단편·시리즈 포스트 작성 규칙, 깊이 기준, front matter 스펙.
- `.claude/skills/daily-post/SKILL.md` — Daily Dev 포스트 작성 규칙, 스크린샷 워크플로.
- `.claude/skills/mermaid/SKILL.md` — 포스트 내 다이어그램 규칙.

## References

See @_data/categories.yml for category/subcategory definitions
