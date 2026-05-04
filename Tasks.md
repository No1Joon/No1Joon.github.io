# No1Joon Blog — 진행 작업

대량 포스트(69편) 시리즈 작업은 완료됨. 이 파일은 현재 진행 중인 SEO·메타 및 신규 콘텐츠 작업을 추적합니다.

## 스타일 참고 (글 작성·수정 시)

개별 포스트를 건드리기 전에 아래 문서를 우선 확인.

- `.claude/skills/blog-post/SKILL.md` — 포스트 구조·톤·시각화 규칙
- `.claude/skills/post-plan/SKILL.md` — 시리즈 기획·제목 규칙
- `.claude/skills/mermaid/SKILL.md` — mermaid 색상·노드 스타일
- `CLAUDE.md` — 디렉터리·커밋·배포 규칙

---

## 진행 중 — 신규 포스트 (AI Weekly 05-04 기반)

### 1. Microsoft–OpenAI 비독점 전환과 멀티클라우드 AI 전략 (2편)
- [ ] 1편: 파트너십 재구성의 배경과 'Post-Azure' 시대의 서막 (`Architecture`)
- [ ] 2편: 어떤 클라우드에서도 자유로운 AI 서비스를 위한 아키텍처 설계 (`Architecture`)

### 2. NVIDIA Nemotron 3 Nano Omni: Hybrid MoE 아키텍처 딥다이브 (1편)
- [ ] 1편: 30B 모델을 3B 수준의 가벼움으로 — MoE 최적화와 멀티모달 추론 분석 (`Development`)

### 3. 에이전틱 보안의 시대: Claude Security와 취약점 자동 패치 (2편)
- [ ] 1편: 코드베이스 전체를 이해하는 Opus 4.7 기반 차세대 보안 스캐너 (`DevOps & SRE`)
- [ ] 2편: '발견'에서 '해결'까지 — AI 보안 에이전트를 CI/CD 파이프라인에 이식하기 (`DevOps & SRE`)

---

## 완료된 개선

- [x] 네이버 서치어드바이저 등록 및 소유 확인 (`_layouts/default.html` 에 메타 태그 삽입)
- [x] `description` front matter — 95편 전부 존재 (`grep -L "^description:" _posts/**/*.md` 로 확인)
- [x] `tags` front matter — 95편 전부 존재
- [x] `robots.txt` 에 GPTBot / ChatGPT-User / OAI-SearchBot / ClaudeBot / Claude-Web / PerplexityBot / Google-Extended / CCBot 명시 허용
- [x] Bing Webmaster Tools 등록 및 사이트맵 제출
- [x] Google Search Console 소유 확인 (`_layouts/default.html` 의 `google-site-verification` 메타)
- [x] `jekyll-seo-tag` / `jekyll-sitemap` / `jekyll-feed` 플러그인 활성화
