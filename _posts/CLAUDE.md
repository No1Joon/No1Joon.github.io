# _posts/

Jekyll 블로그 포스트 디렉터리. 카테고리 slug 기준으로 서브폴더에 분리.

## Structure

- `_posts/{category-slug}/` — 각 최상위 카테고리의 포스트.
- 카테고리 slug 목록 (`_data/categories.yml` 기준): `tech`, `ai`, `robot`, `math`, `science`, `daily-dev`.
- Daily Dev 네이밍: `_posts/daily-dev/YYYY-MM-DD-{slug}.md` (subcategory/order prefix 없음).
- Tech / Explainer 네이밍: `_posts/tech/YYYY-MM-DD-{slug}.md`. 한 주제를 깊게 파고드는 단편 또는 시리즈(`-01-`, `-02-` …)로 작성.
- `ai/` `robot/` `math/` `science/` 는 주제 버티컬. 상당수가 `naver-posting` 에서 이식된 글이라 **해요체**다 — 신규 집필 기준(합쇼체)과 다르지만 의도된 것이고, 이식 글의 본문 문장은 손대지 않는다.
- Jekyll 은 `_posts/` 하위를 재귀 스캔 — 서브폴더는 URL 에 영향 없음 (`permalink: /posts/:title/`).

## Skills

- `.claude/skills/post-plan/SKILL.md` — 시리즈로 갈 가치가 있는 주제일 때만 사용 (편수·각 편 핵심 질문 확정).
- `.claude/skills/blog-post/SKILL.md` — Tech / Explainer 등 깊이 있는 단편·시리즈 포스트 작성 규칙, 깊이 기준, front matter 스펙.
- `.claude/skills/daily-post/SKILL.md` — Daily Dev 포스트 작성 규칙, 스크린샷 워크플로.
- `.claude/skills/naver-import/SKILL.md` — 네이버 포스팅 이식 규칙 (마커 변환·카테고리 판정·이미지 파이프라인).
- `.claude/skills/mermaid/SKILL.md` — 포스트 내 다이어그램 규칙.

## References

- `_data/categories.yml` — 카테고리·서브카테고리 정의 (front matter 값의 기준)
