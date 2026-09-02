---
name: naver-import
description: Use when importing an already-written Naver blog post from the `naver-posting` project into this Jekyll blog. 네이버 SmartEditor 마커(🔹 ▸ ▶︎ 📷 ==형광펜==)를 마크다운으로 옮기고 Drive 이미지를 배치한다. 새 글을 쓰는 게 아니라 **기존 글을 이식**하는 작업 — 본문 문장은 고치지 않는다.
---

`~/Documents/projects/naver-posting/posts/` 에 이미 완성된 네이버 포스팅을 이 블로그의 Jekyll 포스트로 이식한다.

핵심 원칙 하나: **본문 문장을 고치지 않는다.** 이건 새 글을 쓰는 작업이 아니라 이미 발행된 글을 옮기는 작업이다. 해요체·강조·수치·비유를 그대로 두고 **구조와 자산 경로만** 바꾼다.

## When to use

- "네이버 포스팅 올려줘", "naver-posting 에 있는 글 블로그에 옮겨줘"
- 특정 편만: "벤포드 법칙 글 하나만 옮겨줘"

새 글을 처음부터 쓰는 거라면 `blog-post`(Tech/Explainer 깊이글) 또는 `daily-post`(Daily Dev) 를 쓴다. 이 스킬 아님.

## `blog-post` 스킬과의 관계

| 항목      | `blog-post`                     | `naver-import`                        |
| --------- | ------------------------------- | ------------------------------------- |
| 작업 성격 | 새로 집필                       | 기존 글 이식                          |
| 문체      | 합쇼체 강제                     | **원문 해요체 유지** (고치지 않는다)  |
| 깊이 기준 | 5개 항목 전부 통과해야 발행     | 적용 안 함 (이미 발행된 글)           |
| 이모지    | 금지                            | 구조 마커로만 쓰이므로 변환 후 소멸   |
| 시각화    | mermaid 직접 작성               | 원문의 실제 이미지·표를 그대로 옮김   |

front matter 형식·파일명 규칙·카테고리 정합은 `blog-post` 를 따른다. 문체 정책만 다르다 — 그 차이는 의도된 것이고, 이식한 글에 합쇼체 변환을 적용하지 않는다.

## 동작 방식 — 스크립트가 한다

변환은 손으로 하지 않는다. `scripts/import-naver-post.py` 가 마커 변환과 이미지 파이프라인을 담당하고, **사람(에이전트)이 판단할 것만** `scripts/naver-import-map.yml` 에 적는다.

```bash
python scripts/import-naver-post.py --map scripts/naver-import-map.yml --dry-run   # 먼저 확인
python scripts/import-naver-post.py --map scripts/naver-import-map.yml             # 실행
python scripts/import-naver-post.py --map ... --only benford-law                   # 한 편만
```

`--dry-run` 은 포스트·이미지를 쓰지 않고 배치 결과와 누락 이미지만 출력한다. **항상 먼저 돌린다.**

### 매핑 항목에 적어야 하는 것

한 편당 아래 9개. 나머지(본문·이미지·캡션)는 스크립트가 원문에서 뽑는다.

```yaml
- source: posts/math/26Q2/20260619_벤포드법칙.md   # naver-posting 레포 기준 상대경로
  slug: benford-law                                # 영문 kebab-case
  date: 2026-06-19                                 # 원문 front matter 의 date (파일명 날짜 아님)
  category: Math                                   # _data/categories.yml 의 name
  category_slug: math                              #  같은 항목의 slug
  subcategory: Explainer
  title: "벤포드의 법칙 — 숫자는 왜 1로 시작할 확률이 30%일까"
  description: 한 줄 요약 (명사형 종결 가능)
  tags: [benford-law, statistics, probability, fraud-detection, logarithm]
```

- `date` 는 **원문 front matter 의 `date`** 를 쓴다. 파일명의 `YYYYMMDD` 와 다른 경우가 있고(작성일 vs 기준일), 그때는 front matter 가 맞다.
- `title` 은 원문 `title_candidates` 중 가장 정확한 것을 고르되, 네이버용 낚시 표현(`완전정복`, `[긴급]`, `!`)은 덜어낸다. 시리즈는 `제목 (n) — 부제` 형태로 편수를 드러낸다.
- `tags` 는 원문 `hashtags` 20여 개를 그대로 옮기지 않는다. **영문 kebab-case 4~6개**로 압축 (기존 포스트 관행).
- `slug` 는 한글을 쓰지 않는다. 시리즈면 `series-slug-01-topic` 형태로 순서를 넣는다.

### 카테고리 판정

원문의 폴더가 아니라 **주제**로 판정한다. naver-posting 의 `ai`·`robot` 버티컬은 나중에 생겼기 때문에, 초기 AI 글이 `tech/` 에 들어가 있다. 폴더를 그대로 따르면 오분류된다.

| 주제                                            | category  | subcategory |
| ----------------------------------------------- | --------- | ----------- |
| LLM·생성형 AI·AI 기업/도구·AI 보안              | AI        | Explainer   |
| 위 주제의 단발 릴리스·사건 보도                 | AI        | News        |
| 주간 AI 다이제스트                              | AI        | Weekly      |
| 로봇·휴머노이드·피지컬 AI                       | Robot     | Explainer / News |
| 수학·통계·확률·알고리즘                        | Math      | Explainer   |
| IT 밖 과학·환경·보건                            | Science   | Explainer   |
| 하드웨어·반도체·보안·장애 등 그 외 기술         | Tech      | Explainer / News |

`Explainer` 와 `News` 의 갈림: 시간이 지나도 읽을 값이 있으면 Explainer, 특정 시점 사건 보도면 News.

## 마커 변환 규칙 (스크립트 구현 근거)

| 네이버 원문                                  | 변환 결과                              |
| -------------------------------------------- | -------------------------------------- |
| `🔹 제목`                                    | `## 제목` (항상 헤더)                  |
| `▸ 소제목`                                   | `### 소제목`                           |
| `▶︎ 항목` · `👉 항목` · `• 항목`              | `- 항목` (tight list)                  |
| `📷 [이미지 삽입: alt \| file] 출처 - credit` | `![alt](경로)` + `*alt — 출처: credit*` |
| `==하이라이트==`                             | `<mark>하이라이트</mark>`              |
| `💬 한 줄 요약: …` · `❝ 인용`                 | `> …`                                  |
| `⚠️`·`🎯` + 긴 문장                           | `> …` (주의·핵심 정리 콜아웃)          |
| `─────────────`                              | 삭제 (헤더가 구획을 대신함)            |
| `🏷️ #태그 #태그`                             | 삭제 (front matter `tags` 로 이관)     |
| `🖼️ 이미지 가져오기 …` 블록                   | **블록째 삭제** (작성자용 체크리스트)  |
| `🔗 링크 첨부 - [여기에 N탄 네이버 링크]`     | 매핑 `links:` 가 가리키는 이 블로그 편으로 링크 (없으면 줄째 삭제) |
| `🔗 링크 첨부 - https://…`                    | 그대로 둔다 (실제 참고 링크)           |

### 이모지 선두 줄의 함정

`💰 🔬 📊 ✅ 💡 🛠️` 는 같은 글 안에서 **두 용도로 쓰인다**.

- weekly 의 분야 헤더 — `💰 투자·비즈니스` → `##`
- 문단 첫 줄 장식 — `💡 가장 쉬운 비유부터 갈게요.` → 이모지만 떼고 일반 문단

기계적으로 전부 헤더로 바꾸면 면책 문구가 `## 이 글은 투자 권유가 아닙니다…` 같은 헤더로 승격된다. 스크립트는 **길이 30자 이하 + 종결부호(`.` `!` `?`) 없음** 을 헤더 조건으로 쓴다. 새 글에서 이 판정이 틀리면 `HEADER_MAX_LEN` 이 아니라 해당 줄의 분류를 눈으로 확인하고 고친다.

`🖼️ 이미지 가져오기` 블록은 Drive 경로와 "받는 곳:" 이 적힌 **작성자 메모**다. 절대 발행하지 않는다.

### 이전 편 링크 자리표시자

원문의 `[여기에 6탄 네이버 링크]` 는 작성자가 네이버 링크를 나중에 붙이려고 비워 둔 자리다. 이식본이 이을 곳은 네이버가 아니라 **이 블로그의 해당 편**이므로, 매핑에 `links:` 를 적어 잇는다.

```yaml
  links:
    "6탄": ai-power-06-stalled-buildout       # 자리표시자 라벨 → 이 블로그 포스트 slug
    "CUDA 해자 편": post-nvidia-cuda-moat
```

라벨은 `[여기에 … 네이버 링크]` 사이의 문구를 그대로 쓴다. 링크 문구는 대상 포스트의 `title` 을 스크립트가 읽어 넣으므로 매핑에 적지 않는다. `links:` 가 없거나 대상 포스트가 아직 없으면 **그 줄을 버리고 경고**한다 — 자리표시자를 발행물에 남기지 않는다. 문장 안에 박힌 자리표시자(`… 안 보셨다면: [여기에 1탄 네이버 링크]`)도 같은 규칙을 타고, 이 경우 링크가 빠지면 문장이 끊기므로 줄째로 버린다.

시리즈를 순서대로 이식할 때는 **앞 편이 `_posts/` 에 있어야** 링크가 걸린다. 뒤 편을 먼저 넣었다면 앞 편을 넣은 뒤 뒤 편을 다시 한 번 돌린다.

## 이미지 파이프라인

원본은 Drive 에 있고, 이 레포는 두 트리를 미러링한다 (`assets/CLAUDE.md` 규칙 그대로).

```
Drive assets/postings/<분기>/<포스트키>/  (또는 공유 assets/raw/ 로고 라이브러리)
  → assets/raw-images/{category-slug}/{slug}/NN-name.{png,jpg}   원본 보존 (git 미추적)
  → assets/images/{category-slug}/{slug}/NN-name.webp            포스트가 참조 (1280px, q82)
```

- 파일명은 **ASCII 로 정규화**한다. 원본에 한글 파일명이 섞여 있고(`2_구형유압_darpa_pd.jpg`), 그대로 두면 URL 이 취약해진다. → `02-darpa-pd.webp`
- 번호는 원문 슬롯 번호가 아니라 **실제 배치 순번**. 누락 슬롯이 있어도 번호가 이어지고, 같은 로고를 두 번 써도 충돌하지 않는다.
- 마커의 파일이 Drive 에 없으면 그 이미지 줄만 **버리고 경고를 남긴다**. 본문에 깨진 링크를 남기지 않는다. 원문에서 끝내 수집되지 않은 제품 스크린샷이 실제로 존재한다 — 그건 정상이고, 리포트로만 알린다.
- **OG(`image`) 는 변환기가 쓰지 않는다.** `scripts/generate-og.mjs` 가 소유하는 필드다 — `/assets/og/<slug>.png` 를 만들고 `image:` 줄을 그 경로로 덮어쓴다. 본문 이미지 경로를 넣어봐야 CI 가 갈아치우므로 죽은 메타만 남는다. 대신 이식 후 아래 절차를 밟는다.

  ```bash
  npm run generate-og   # 이식 직후 1회 — OG 카드 생성 + image: 줄 기입
  ```

  PNG 자체는 `.gitignore` 대상(CI 가 매 배포마다 재생성)이고, **`image:` 줄은 커밋한다** — 기존 포스트도 그렇게 되어 있다. 결과 OG 는 1200×630 PNG 인데, WebP OG 는 카카오톡·네이버 공유 미리보기에서 렌더가 안 되는 경우가 많으므로 이쪽이 맞다.

## Workflow

1. 대상 편을 확정한다. 이미 옮긴 글이 있는지 `_posts/` 를 먼저 확인 (같은 slug 재실행은 덮어쓴다).
2. 원문 front matter(`title_candidates`·`date`·`hashtags`·`images`)와 도입부 3~4 단락을 읽어 매핑 9개 항목을 정한다.
3. `_data/categories.yml` 을 읽어 category/subcategory/category_slug 가 실제 값인지 확인. 없는 카테고리가 필요하면 **먼저 categories.yml 에 추가**한다 (nav 는 이 파일로 렌더된다).
4. `scripts/naver-import-map.yml` 에 항목을 추가한다.
5. `--dry-run` → 배치 이미지 수와 누락 목록 확인.
6. 실제 실행 → 잔존 마커 검사 (`🔹 ▸ ▶︎ 📷 ==` 와 `/Users/joon`, `받는 곳:`, `여기에 … 네이버 링크` 가 결과물에 없어야 한다).
7. `npm run generate-og` → OG 카드 생성 + `image:` 줄 기입 (위 이미지 파이프라인 절 참조).
8. `bundle exec jekyll build` 로 렌더 확인. 이미지 참조가 전부 `_site` 에 실재하는지 본다.
9. 사용자에게는 편수·카테고리 분포·누락 이미지 건수만 보고. 본문을 다시 붙여 넣지 않는다.

## Prohibitions

- 본문 문장 재작성·문체 변환 금지. 오탈자조차 손대지 않는다 (원문이 정본).
- 원문에 없는 섹션·설명·mermaid 다이어그램 추가 금지.
- 누락 이미지를 임의 이미지로 대체 금지. 비워두고 보고한다.
- 작성자용 메모(`🖼️ 이미지 가져오기`, Drive 경로, "받는 곳:")를 발행물에 남기는 것 금지.
- 이전 편 링크 자리표시자(`[여기에 N탄 네이버 링크]`)를 발행물에 남기는 것 금지.
- 한글 파일명 이미지 경로 금지.
- 네이버 해시태그 20여 개를 `tags` 에 그대로 옮기는 것 금지.
