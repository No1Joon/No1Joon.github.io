# AI Agent 가이드 (Claude & Gemini 공통)

## 프로젝트 개요

- Jekyll 기반 GitHub Pages 블로그 (No1Joon's Tech Blog)
- 기술 스택, 아키텍처, 개발 경험 기록용
- 배포: `.github/workflows/deploy.yml` 를 통한 자동 배포

## 디렉터리 구조

- `_posts/` — 블로그 글 (Markdown). **카테고리 slug 하위 폴더에 저장**.
  - 경로 규칙: `_posts/{category-slug}/YYYY-MM-DD-{subcategory-slug}-{nn}-{topic}.md`
  - `{category-slug}` 는 `_data/categories.yml` 의 최상위 `slug` 값을 그대로 사용 (예: `ci-cd`, `container-orchestration`, `cloud-infrastructure`, `observability`, `devops-sre`, `development`, `architecture`).
  - 해당 카테고리의 첫 글이면 서브폴더부터 생성.
  - Jekyll은 `_posts/` 하위를 재귀 탐색하므로 URL·permalink는 영향 없음 (`permalink: /posts/:title/`).
- `_layouts/` — Jekyll 레이아웃 (`post.html` 등)
- `_data/categories.yml` — 카테고리·서브카테고리 정의 (front matter의 category/subcategory는 여기 값을 그대로 사용)
- `_config.yml` — Jekyll 설정
- `.claude/skills/` — 커스텀 스킬 & 세부 작업 가이드라인 (Gemini 포함 모든 AI는 작업 전 이 폴더 참조)
- `.gemini/` — Gemini CLI 설정 (Claude와 동일 컨텍스트 파일 공유)
- `Tasks.md` — 진행 중 대량 포스트 작성 지시서 (Gemini·Claude 공통 진입점)

## AI 에이전트 참고 문서 가이드

Claude나 Gemini가 블로그와 관련된 명령을 수행할 때, 아래 스킬 문서를 우선적으로 탐색하고 지침을 숙지.

- **시리즈 기획:** `.claude/skills/post-plan/SKILL.md` (서브카테고리 시리즈 시작 시 편수·제목 리스트부터 확정)
- **포스트 작성:** `.claude/skills/blog-post/SKILL.md` (블로그 구조·시각화·코드 최소화 등 핵심 규칙)
- **아키텍처/다이어그램:** `.claude/skills/mermaid/SKILL.md` (다이어그램 색상·구조·선 스타일 반드시 참고)
- **대량 포스트 작업:** 루트의 `Tasks.md` (69편 시리즈 작업 지시서, 파일명·제목·다룰 내용 명시)

## 글쓰기 규칙

- 포스트 저장 위치: `_posts/{category-slug}/` (카테고리 slug는 `_data/categories.yml` 기준)
- 포스트 파일명: `YYYY-MM-DD-title.md`
- front matter 필수: `title`, `date`, `order` (정렬용)
- 시리즈 글은 `order` 필드로 순서 지정 (1부터 시작)
- **문장 톤 자유** — 해요체·합쇼체·혼용 모두 허용. 한 포스트 안에서만 일관성 유지.
- **서브카테고리 시리즈를 새로 시작할 때**: `post-plan` 스킬 문서를 참고해 먼저 편수·제목 리스트를 확정. 개별 글 작성은 그 다음에 진행.
- **블로그 단일 포스트 작성·수정 시**: `blog-post` 스킬 문서를 우선 숙지하고 지침에 따라 작성.

## 커밋/배포

- 커밋 메시지에 `Co-Authored-By` 라인 넣지 않기
- 커밋 후 항상 바로 `git push` 실행
- `main` 브랜치 푸시 시 GitHub Actions 로 자동 배포됩니다.

## 로컬 개발

```bash
bundle install
bundle exec jekyll serve
```
