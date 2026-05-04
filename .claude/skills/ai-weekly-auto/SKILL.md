---
name: ai-weekly-auto
description: Use when generating a fresh weekly AI news brief from scratch (web research) for the No1Joon blog — typically invoked by the weekly schedule. Gathers Tier-1 source headlines (Bloomberg, Reuters, TechCrunch, CNBC, CNN, Crunchbase, VentureBeat, official gov/research releases), categorizes into 5 sections, and writes a Jekyll post directly under `_posts/news/YYYY-MM-DD-ai-weekly.md`. Different from `news-post` which only saves a user-provided brief verbatim.
---

이 스킬은 **AI 가 직접 그 주의 AI 업계 뉴스를 수집·분류·작성** 해서 Jekyll 포스트로 저장한다. 사용자가 브리핑 원문을 들고 오는 케이스가 아니다 — 그건 `news-post` 스킬.

## When to use

- 매주 정해진 스케줄(routine) 이 자동으로 호출.
- 사용자가 "이번 주 AI 위클리 만들어줘", "AI Weekly 자동 생성" 식으로 요청.

원문 브리핑을 사용자가 들고 오면 이 스킬 아님 → `news-post` 로.

## Inputs (none required)

스케줄 호출 시 인자 없음. 실행 시점의 **오늘 날짜** 를 기준으로 그 주를 정의한다.

- 발행일 = 실행 시점 KST 날짜 (`date '+%Y-%m-%d'`)
- 수집 범위 = 발행일 기준 직전 7일

## 카테고리 (이 순서 고정, 빈 카테고리는 통째로 생략)

1. 💰 투자·비즈니스
2. 🔬 모델·기술
3. ⚖️ 규제·정책
4. 🌐 산업·사회 영향
5. 🚨 보안

## 출처 규칙

- **Tier-1 매체 또는 공식 발표만**. 예: Bloomberg, Reuters, TechCrunch, CNBC, CNN, Crunchbase, VentureBeat, The Verge, FT, WSJ, Holland & Knight, 정부·연구기관 (NIST, EU Commission, FTC 등) 공식 발표.
- 출처 URL 을 모르면 그 항목을 **빼거나 표시** — 임의 URL 생성 절대 금지.
- WebSearch / WebFetch 로 검색·확인. 한 기사당 출처 1개로 충분.
- 분석 리포트 인용은 출처가 있을 때만 인용 형태로.

## 본문 톤

- 짧은 합쇼체와 명사형 자유 혼용 (뉴스 장르). 한 기사 블록 안에서는 톤 일관 유지.
- 핵심 포인트는 **사실만**, 1~3개. 과장·마케팅 어휘 금지.

## 절대 넣지 않는 것

### 1. 본문 첫 줄 H1 금지

front matter 의 `title` 만 사용. 본문에 `# 🤖 AI Weekly — ...` 가 들어가면 layout 의 `<h1>{{ page.title }}</h1>` 와 겹쳐 H1 이 두 번 나온다.

### 2. AI 메타 문구 금지

독자에게 보이는 글에 **AI 가 자기 작업 품질·정체성을 어필하는 류 멘트** 가 절대 들어가지 않게 한다:

- `Tier-1 출처 기준` (브리핑 어디에도 등장 X)
- `(Bloomberg / TechCrunch / ... 등)` 류 출처 매체 나열 메타 (개별 기사의 출처 라인은 OK)
- `AI 가 선별한 / 정리한 / 요약한` 류 자기 호칭
- `오늘 자 브리핑입니다`, `참고하세요`, `도움이 되셨으면 합니다` 류 인사·맺음말

## Front matter

```yaml
---
title: "{핵심 토픽 1} · {핵심 토픽 2} · {핵심 토픽 3}"
description: YYYY년 M월 D일 주간 AI 업계 핵심 소식 N건
date: YYYY-MM-DD
order: <YYYYMMDD 정수>
category: News
subcategory: AI Weekly
tags: [news, ai, ai-weekly, weekly]
---
```

| 필드        | 값                                                                                              |
| ----------- | ----------------------------------------------------------------------------------------------- |
| title       | 그 주 헤드라인 중 가장 주목도 높은 2~4개를 골라 압축 키워드로 조합 (아래 규칙)                   |
| description | `YYYY년 M월 D일 주간 AI 업계 핵심 소식 N건` — N 은 본문 ⭐ 기사 총 개수                          |
| date        | 발행일 `YYYY-MM-DD`                                                                             |
| order       | `YYYYMMDD` 정수 (예: `20260504`)                                                                |
| category    | 항상 `News`                                                                                     |
| subcategory | 항상 `AI Weekly`                                                                                |
| tags        | 고정 `[news, ai, ai-weekly, weekly]`                                                            |

### Title 생성 규칙

- "AI Weekly", "이번 주 뉴스" 같은 라벨·날짜는 title 에 **넣지 않는다**.
- 헤드라인 중 **숫자·고유명사가 박힌 것** 우선 (`$40B`, `GPT-5.5`, `8,000명 감원` 등).
- 같은 분야 헤드라인이 여러 개면 가장 큰 쪽 하나만. **투자/모델/규제/사회/보안** 중 2~4개 영역에서 균형 있게.
- 각 토픽은 5~15자 (영문·숫자·한글). 구분자는 ` · ` (가운뎃점 양옆 한 칸).
- 전체 길이 30~55자 권장, **60자 초과 금지**.
- 이모지·따옴표·괄호 금지.

예시:

- `GPT-5.5 · Anthropic $40B · Meta 8천명 감원 · 멕시코 150GB 유출`
- `GPT-5.5 출시 · Anthropic $40B · Meta 8,000명 감원`

## File path

- `_posts/news/YYYY-MM-DD-ai-weekly.md`
- 같은 날짜 파일이 이미 있으면 **덮어쓰기 금지** — 사용자(또는 스케줄 로그) 에 알리고 종료. 자동 모드에서는 `_posts/news/YYYY-MM-DD-ai-weekly-2.md` 로 suffix 붙여 저장.

## 출력 템플릿 (이 구조 그대로)

```markdown
---
title: "{핵심 토픽 1} · {핵심 토픽 2} · {핵심 토픽 3}"
description: YYYY년 M월 D일 주간 AI 업계 핵심 소식 N건
date: YYYY-MM-DD
order: <YYYYMMDD 정수>
category: News
subcategory: AI Weekly
tags: [news, ai, ai-weekly, weekly]
---

> 이번 주 핵심 소식 N건

## 📌 헤드라인

- [투자·비즈니스] 한 줄 요약
- [모델·기술] 한 줄 요약
- [규제·정책] 한 줄 요약
- [산업·사회 영향] 한 줄 요약
- [보안] 한 줄 요약

---

## 💰 투자·비즈니스

### ⭐ 기사 제목

2~3문장 요약

- 핵심 포인트 1
- 핵심 포인트 2

📰 [출처명](URL) · MM.DD 또는 HH:MM KST
🏷️ `태그1` `태그2`

---

### ⭐ (같은 카테고리 두 번째 기사가 있으면 같은 패턴, 사이에 `---`)

---

## 🔬 모델·기술

(같은 패턴)

## ⚖️ 규제·정책

(같은 패턴)

## 🌐 산업·사회 영향

(같은 패턴)

## 🚨 보안

(같은 패턴)

---

## 📊 이번 주 한 줄

한 주를 관통하는 흐름 코멘트 한 문단 (사실 나열 X, 짧고 강한 흐름).
```

빈 카테고리는 헤더·구분선 모두 생략 (헤더만 남기지 않는다).

## Workflow

1. **날짜 확정** — `date '+%Y-%m-%d'` 로 발행일, `date '+%Y%m%d'` 로 order 산출.
2. **뉴스 수집** — WebSearch / WebFetch 로 직전 7일 AI 업계 헤드라인 검색. 5개 카테고리 각각에 대해 Tier-1 출처 1~3건씩 후보 수집. 최소 4개 카테고리는 채우는 걸 목표로.
   - 검색 쿼리 예: `AI funding billion site:bloomberg.com 2026`, `AI model release site:techcrunch.com`, `AI regulation EU site:reuters.com`, `AI layoffs site:cnbc.com`, `AI security breach site:reuters.com`.
   - URL 을 직접 본문에 인용하므로 **반드시 검색 결과의 실제 URL 만 사용**. 검색 결과를 못 얻으면 그 항목 제외.
3. **카테고리 분류** — 위 5개 카테고리에 매핑. 한 카테고리에 1~3건. 어디에도 안 맞으면 제외.
4. **Title 추출** — 위 "Title 생성 규칙" 대로 가장 주목도 높은 2~4개 토픽 선정.
5. **본문 작성** — 출력 템플릿 그대로. 톤 규칙·메타 문구 금지 규칙 지킴.
6. **자가 검증** — 아래 체크리스트 통과 확인.
7. **저장** — `_posts/news/YYYY-MM-DD-ai-weekly.md` 로 Write. 같은 파일 존재하면 suffix 처리.
8. **보고** — 파일 경로 + 카테고리별 기사 수 + title 선택 근거 한두 줄.

## 자가 검증 (저장 직전)

- [ ] 첫 줄이 `---` 로 시작 (front matter)
- [ ] `title` 에 라벨·날짜·이모지·따옴표·괄호 없음, 60자 이내
- [ ] `date`·`order` 가 같은 날짜 기반 (`2026-05-04`, `20260504`)
- [ ] `description` N 값 = ⭐ 기사 총 개수 = 인용구 N
- [ ] 본문에 `# 🤖 AI Weekly — ...` H1 없음
- [ ] "Tier-1 출처 기준" 등 AI 메타 문구 없음
- [ ] 카테고리 섹션 순서 고정 (투자→모델→규제→사회→보안), 빈 카테고리는 통째로 생략
- [ ] 모든 출처 URL 이 실제 매체 도메인 (만든 URL 없음)
- [ ] 헤드라인 리스트 항목 수 = 사용된 카테고리 수 (각 카테고리 대표 1줄)

## After-save

배포는 `main` 브랜치 푸시 시 GitHub Actions 가 자동 처리. 이 스킬은 **commit·push 를 수행하지 않는다** — 스케줄 prompt 에서 `smart-commit` 으로 위임.

## Edge cases

- 검색 결과가 너무 적어 4개 카테고리도 못 채우면 → 채워진 카테고리만으로 발행 (헤드라인·기사 수 일치 유지). 최소 1개 카테고리는 있어야 함.
- 같은 날짜 파일이 이미 있으면 → 자동 모드에서는 `-2.md`, `-3.md` suffix 로 저장 후 보고.
- WebSearch/WebFetch 가 실패하면 → 실패 사유와 함께 종료. **fake URL 절대 생성 금지**.
