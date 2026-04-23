# No1Joon's Tech Blog

Jekyll 기반 GitHub Pages 블로그 (Claude·Gemini 공통 컨텍스트). 기술 스택·아키텍처·개발 경험 기록용.

## Commands

- `bundle install` — 의존성 설치
- `bundle exec jekyll serve` — 로컬 프리뷰 (http://localhost:4000)

## Architecture

- `_posts/` — 블로그 글 (Markdown). 카테고리 slug 하위 폴더 구조. 상세는 `_posts/CLAUDE.md`.
- `_layouts/` — Jekyll 레이아웃 (`default.html`, `post.html`, `resume.html`).
- `_data/categories.yml` — 카테고리·서브카테고리 정의. front matter 의 category/subcategory 값은 여기 기준.
- `_config.yml` — Jekyll 설정.
- `assets/` — CSS·이미지. 이미지 구조·raw 보존 규칙은 `assets/CLAUDE.md`.
- `scripts/add-screenshot.py` — Desktop 스크린샷 → WebP 변환 및 배치.
- `api/` — 댓글 시스템 FastAPI 서비스 (Cloud Run + Firestore). 상세는 `api/CLAUDE.md`.
- `.claude/skills/` — 작업별 가이드라인 (Skills 섹션).
- `.gemini/` — Gemini CLI 설정 (동일 컨텍스트 공유).
- `Tasks.md` — 진행 중 작업 트래커 (SEO·메타 개선 등).

## Skills

- `.claude/skills/post-plan/SKILL.md` — 서브카테고리 시리즈 시작 시 편수·제목 리스트 먼저 확정.
- `.claude/skills/blog-post/SKILL.md` — 개념·아키텍처 딥다이브 포스트 작성. front matter 스펙 소스 오브 트루스. 톤·길이·시각화·Do-Not 규칙.
- `.claude/skills/daily-post/SKILL.md` — Daily Dev 포스트 (Troubleshooting·Tips & Tools). 스크린샷 워크플로 포함.
- `.claude/skills/mermaid/SKILL.md` — 다이어그램 색상·구조·선 스타일.
- `.claude/skills/smart-commit/SKILL.md` — 커밋 메시지 생성·분할 규칙, `Co-Authored-By` 금지, 커밋 후 자동 푸시.

## Environment

- Ruby + Bundler (Jekyll).
- `main` 브랜치 푸시 시 `.github/workflows/deploy.yml` 가 GitHub Pages 로 자동 배포.
- `assets/raw-images/` 는 `.gitignore` 로 제외 (원본 보존용, 사이트 산출물에 포함되지 않음).

## References

See @Tasks.md for current work tracker
See @_data/categories.yml for category/subcategory definitions
