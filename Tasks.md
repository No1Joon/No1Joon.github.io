# No1Joon Blog — 진행 작업

대량 포스트(69편) 시리즈 작업은 완료됨. 이 파일은 현재 진행 중인 SEO·메타 개선 작업을 추적합니다.

## 스타일 참고 (글 작성·수정 시)

개별 포스트를 건드리기 전에 아래 문서를 우선 확인.

- `.claude/skills/blog-post/SKILL.md` — 포스트 구조·톤·시각화 규칙
- `.claude/skills/post-plan/SKILL.md` — 시리즈 기획·제목 규칙
- `.claude/skills/mermaid/SKILL.md` — mermaid 색상·노드 스타일
- `CLAUDE.md` — 디렉터리·커밋·배포 규칙

---

## 진행 중 — SEO 개선

### 1. 네이버 서치어드바이저 등록

- 상태: **네이버 계정 생성 중 (대기)**
- 계정 준비 후 작업:
  1. <https://searchadvisor.naver.com> 에 사이트 등록 및 소유 확인
  2. 발급받은 메타 태그로 `_layouts/default.html` 의 주석된 `naver-site-verification` 라인 교체하고 주석 해제
  3. sitemap 제출: `https://no1joon.github.io/sitemap.xml`
  4. rss 제출: `https://no1joon.github.io/feed.xml`

- [x] 포스트별 OG 이미지 (빌드 타임 자동 생성)
  - Node.js (Satori + Resvg) 기반 자동 생성 스크립트 구현 완료
  - GitHub Actions 연동 완료
  - 전 포스트 마크다운 `image` 필드 주입 완료

---

## 완료된 개선

- [x] `description` front matter — 95편 전부 존재 (`grep -L "^description:" _posts/**/*.md` 로 확인)
- [x] `tags` front matter — 95편 전부 존재
- [x] `robots.txt` 에 GPTBot / ChatGPT-User / OAI-SearchBot / ClaudeBot / Claude-Web / PerplexityBot / Google-Extended / CCBot 명시 허용
- [x] Bing Webmaster Tools 등록 및 사이트맵 제출
- [x] Google Search Console 소유 확인 (`_layouts/default.html` 의 `google-site-verification` 메타)
- [x] `jekyll-seo-tag` / `jekyll-sitemap` / `jekyll-feed` 플러그인 활성화
