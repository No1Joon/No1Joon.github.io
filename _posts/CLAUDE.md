# _posts/

Jekyll 블로그 포스트 디렉터리. 카테고리 slug 기준으로 서브폴더에 분리.

## Structure

- `_posts/{category-slug}/` — 각 최상위 카테고리의 포스트.
- 시리즈 포스트 네이밍: `YYYY-MM-DD-{subcategory-slug}-{nn}-{topic}.md` (예: `2026-04-08-harness-01-overview.md`).
- Daily Dev 네이밍: `_posts/daily-dev/YYYY-MM-DD-{slug}.md` (subcategory/order prefix 없음).
- 카테고리 slug 목록 (`_data/categories.yml` 기준): `ci-cd`, `container-orchestration`, `cloud-infrastructure`, `observability`, `devops-sre`, `development`, `architecture`, `daily-dev`.
- Jekyll 은 `_posts/` 하위를 재귀 스캔 — 서브폴더는 URL 에 영향 없음 (`permalink: /posts/:title/`).

## Skills

- `.claude/skills/post-plan/SKILL.md` — 새 서브카테고리 시리즈 시작 시 편수·제목 확정.
- `.claude/skills/blog-post/SKILL.md` — 개념·아키텍처 딥다이브 포스트 작성 규칙, front matter 스펙.
- `.claude/skills/daily-post/SKILL.md` — Daily Dev 포스트 작성 규칙, 스크린샷 워크플로.
- `.claude/skills/mermaid/SKILL.md` — 포스트 내 다이어그램 규칙.

## References

See @_data/categories.yml for category/subcategory definitions
