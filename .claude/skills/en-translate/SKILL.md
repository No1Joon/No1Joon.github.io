---
name: en-translate
description: 이 블로그의 한국어 포스트를 영문판(`_en_posts/`)으로 번역할 때 사용. "영문 번역", "영문판 만들어", "영어로 옮겨줘", "en 버전 추가" 같은 요청에 쓴다. 새 글 집필이 아니라 기존 글의 충실한 번역 — 구조·수치·이미지는 그대로 둔다.
---

# en-translate — 영문판 번역

한국어 포스트를 `_en_posts/` 로 옮긴다. 원문이 정본이고 번역은 내용을 더하거나 빼지 않는다.

## 파일·짝

- 경로는 `_en_posts/<category-slug>/<한국어 글과 같은 파일명>.md` — 파일명(slug)이 같아야 언어 전환·hreflang 이 걸린다.
- URL 은 `/en/posts/<slug>/` 로 자동 결정된다 (`_config.yml` 의 `en_posts` 컬렉션).
- `_en_posts/` 안에 날짜 없는 `.md`(CLAUDE.md 등)를 두지 않는다 — 컬렉션 문서로 발행된다.

## front matter

- `title`·`description` 만 번역하고 `date`·`category`·`subcategory`·`tags` 는 원문 값 그대로.
- `image:` 는 쓰지 않는다 — `npm run generate-og` 가 `/assets/og/en-<파일명>.png` 로 넣는다.
- 시리즈 표기는 `제목 (n) — 부제` 를 `Title (n) — Subtitle` 로 유지한다.

## 본문

- 헤더 구조·표·목록·`<mark>`·인용·이미지 순서를 원문과 1:1 로 맞춘다.
- 이미지 경로는 한국어 글 것을 그대로 쓰고, alt 와 캡션만 번역한다 (`출처:` → `Source:`, `자가 렌더` → `self-rendered`, `agy 자가 생성` → `self-generated with agy`).
- 금액은 달러가 원 수치면 `$10 (₩14,000)`, 원화만 있으면 `₩299,000` — 원문의 환산 기준 줄은 `Exchange rate: converted at $1 ≈ ₩1,400` 로 옮긴다.
- 한국 고유 용어는 영어로 풀되 오해 소지가 있으면 원어를 괄호로 남긴다 (예: `holdings summary (판시사항)`).
- 해요체 어조는 평이한 영어 서술로 옮기고 원문에 없는 설명·결론을 붙이지 않는다.
- `## 참고 출처` → `## Sources`, `## 앞으로 주목할 점` → `## What to watch next`; 출처 링크 URL 은 그대로, 링크 문구만 번역한다.
- `🔗 링크 첨부 - URL` 줄은 `🔗 Link - URL` 로 옮긴다.
- `💻 [소스코드: 설명]` 은 `💻 [Source code: Description]` 으로 옮기고 아래 코드 블록은 손대지 않는다.
- 대괄호만 있는 줄(`[항목명]`)은 라벨이라 번역하고, 뒤에 이어지는 설명 줄도 번역한다.
- 국내 매체·기관명은 영문 표기로 옮긴다 (전자신문 → Electronic Times, 아주경제 → Aju Business Daily, 한국인터넷진흥원 → Korea Internet & Security Agency).

## 내부 링크

- 대상 글의 영문판이 있으면 `/en/posts/<slug>/` 와 영문 제목으로 잇는다.
- 영문판이 없으면 `/posts/<slug>/` 를 유지하고 번역한 제목 뒤에 ` (in Korean)` 을 붙인다.
- 나중에 그 대상 글을 번역하면 이 링크를 영문판으로 고친다.

## 순서

1. 대상 선정 — 따로 지정이 없으면 영문판이 없는 글 중 최신순.
2. 원문을 끝까지 읽고 번역 파일을 쓴다.
3. `npm run generate-og` → 영문 글마다 `image: /assets/og/en-…` 가 들어갔는지, 한국어 글이 바뀌지 않았는지 `git status` 로 확인.
4. `bundle exec jekyll build` 후 확인 — 이미지·내부 링크가 `_site` 에 실재하는지, `/en/posts/<slug>/` 에 `hreflang="ko"`, 한국어 글에 `/en/posts/<slug>/` 링크가 생겼는지.
5. 커밋은 `smart-commit` 규칙(커밋 후 자동 푸시 → 배포)을 따른다.
