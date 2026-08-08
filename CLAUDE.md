# No1Joon's Tech Blog

Jekyll 기반 GitHub Pages 블로그 (Claude·Gemini 공통 컨텍스트). 기술 스택·아키텍처·개발 경험 기록용.

## Commands

- `bundle install` — 의존성 설치
- `bundle exec jekyll serve` — 로컬 프리뷰 (http://localhost:4000)
- `npm run generate-og` — 포스트 OG 이미지 생성 (`assets/og/`)
- `npm run generate-brand` — 파비콘·기본 OG 이미지 생성

## Architecture

- `_posts/` — 블로그 글. Jekyll 기본과 달리 **카테고리 slug 하위 폴더**로 나뉜다 (URL 에는 영향 없음). 상세는 `_posts/CLAUDE.md`.
- `_data/categories.yml` — 포스트 front matter 의 category/subcategory 유효값을 규정하는 단일 출처.
- `assets/` — 최적화본 `images/` 와 원본 `raw-images/` 가 같은 구조를 미러링. 상세는 `assets/CLAUDE.md`.
- `scripts/add-screenshot.py` — Desktop 스크린샷을 WebP 로 변환해 위 두 트리에 배치.
- `scripts/generate-og.mjs` → `assets/og/` — OG 이미지 생성물 (원본은 포스트 front matter).
- `scripts/generate-brand.mjs` → `favicon.ico` · `assets/favicon.png` · `assets/apple-touch-icon.png` · `assets/og-default.png` — 브랜드 자산 생성물. 색은 `assets/css/style.css` 의 `:root` 토큰과 맞춘다.
- `scripts/import-naver-post.py` + `scripts/naver-import-map.yml` — `naver-posting` 프로젝트의 네이버 포스팅을 Jekyll 포스트로 이식. 규칙은 `.claude/skills/naver-import/SKILL.md`.
- `api/` — 댓글 시스템 FastAPI 서비스. 사이트와 별개로 배포된다. 상세는 `api/CLAUDE.md`.
- `docs/design/` — UI 를 만지기 전에 읽는다. `design.md` 가 방향·제외 항목·접근성 기준, `wireframes-blog.html` 이 화면 배치와 그 근거.
- `.gemini/` — Gemini CLI 설정. 이 CLAUDE.md 와 같은 컨텍스트를 공유한다.
- `Tasks.md` — 진행 중 작업 트래커.

## Skills

- `.claude/skills/post-plan/SKILL.md` — 한 주제를 시리즈로 갈 가치가 있다고 판단했을 때만 사용 (편수·각 편 핵심 질문 확정).
- `.claude/skills/blog-post/SKILL.md` — Tech / Explainer 등 깊이 있는 단편·시리즈 작성. front matter 스펙·깊이 기준·톤·시각화·Do-Not 규칙.
- `.claude/skills/daily-post/SKILL.md` — Daily Dev 포스트 (Troubleshooting·Tips & Tools). 스크린샷 워크플로 포함.
- `.claude/skills/naver-import/SKILL.md` — `naver-posting` 의 완성 포스팅을 이 블로그로 이식 (새 집필 아님 — 본문 문장은 고치지 않고 구조·자산 경로만 변환).
- `.claude/skills/mermaid/SKILL.md` — 다이어그램 색상·구조·선 스타일.
- `.claude/skills/smart-commit/SKILL.md` — 커밋 메시지 생성·분할 규칙, `Co-Authored-By` 금지, 커밋 후 자동 푸시.

## Environment

- Ruby + Bundler (Jekyll). Node (OG 이미지 생성). CI 는 Ruby 3.3 / Node 20.
- `main` 브랜치 푸시 시 `.github/workflows/deploy.yml` 가 GitHub Pages 로 자동 배포.
- `assets/raw-images/` 는 `.gitignore` 로 제외 (원본 보존용, 사이트 산출물에 포함되지 않음).
