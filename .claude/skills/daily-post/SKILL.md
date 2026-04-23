---
name: daily-post
description: Use when writing a Daily Dev post for the No1Joon blog — short, honest notes from everyday dev life. Covers two subcategories: Troubleshooting (problem → attempts → fix) and Tips & Tools (short setup / discovery notes). Creates a Jekyll post under `_posts/daily-dev/` with fixed structures that do not inflate a short real story into a fake deep-dive.
---

Write a Daily Dev post for the No1Joon blog. 이 장르는 **짧고 정직한 기록**이다. 실제로 겪은 증상, 실제로 시도한 것, 실제로 통한 해결 — 또는 실제로 내가 쓰는 세팅·알게 된 팁 — 만 적는다. 추측을 사실처럼 쓰지 않는다.

## When to use

- "이 에러를 블로그로", "해결기 써줘", "오늘 이런 문제가 있었는데 정리해줘" → **Troubleshooting** 서브카테고리
- "이 도구 세팅 기록", "오늘 알게 된 팁 정리", "이 단축키 어떻게 쓰는지" → **Tips & Tools** 서브카테고리
- 개념·아키텍처 딥다이브가 주제라면 `blog-post` 스킬 사용 (이 스킬 아님)

## 이 스킬과 `blog-post` 스킬의 차이

| 항목        | `blog-post`               | `daily-post`                            |
| ----------- | ------------------------- | --------------------------------------- |
| 장르        | 개념·아키텍처 정리        | 문제 해결 경험담 · 팁·설정 메모         |
| 기본 길이   | 250~450 줄                | 100~200 줄                              |
| 핵심 시각화 | mermaid 다이어그램·표     | 표·스크린샷·순서 목록                   |
| 톤          | 일반 서술                 | 1인칭 경험 허용 ("내 환경에선 ~")       |
| 코드 블록   | 개념 보조용으로 종종 등장 | 터미널 명령·설정 경로 위주로만          |
| 추측        | 근거 기반 설명            | **확실한 것만**, 추측은 명시적으로 표시 |

공통 규칙(front matter 형식·언어 정책·이모지 금지·과장 금지)은 `.claude/skills/blog-post/SKILL.md` 를 그대로 따른다. 아래는 이 장르에서만 달라지는 부분.

## 서브카테고리 선택

| 글 성격                                  | subcategory       |
| ---------------------------------------- | ----------------- |
| "문제 → 해결" 서사 중심                  | `Troubleshooting` |
| "이렇게 세팅·쓴다 / 알게 됐다" 기록 중심 | `Tips & Tools`    |

애매하면 Troubleshooting 쪽으로. "정리해두면 다음에 같은 삽질을 피할 수 있다" 성격이면 Troubleshooting 이다.

## Front matter 특이사항

```yaml
---
title: "본질이 드러나는 짧은 제목 (15자 내외)"
description: 무엇에 대한 기록인지 한 줄 요약
date: YYYY-MM-DD
order: 1
category: Daily Dev
subcategory: Troubleshooting # 또는 "Tips & Tools"
tags: [troubleshooting, 대상-도구, 플랫폼, 5~8개]
---
```

- 제목은 "크롬 넷플릭스 가구 오류" 처럼 **무엇에 대한 글인지** 가 바로 드러나야 함. "어제의 해결기" 같은 모호한 제목 금지.
- 파일 경로: `_posts/daily-dev/YYYY-MM-DD-slug.md`

## 본문 구조

### Troubleshooting 템플릿 (고정 순서)

1. **오프닝** — 한 문단. "어느 날 무엇이 안 되기 시작했다" 수준의 맥락.
2. **`## 증상`** — 한 문단. "무엇이 / 어떤 조건에서 / 어떻게" 안 되는지. 스크린샷 있으면 여기.
3. **`## 환경`** — 표. OS·브라우저·앱 버전·칩 등 재현 조건. 모르면 "확인 불가" 로 기록.
4. **`## 시도한 것`** — 표 또는 순서 목록. 각 시도에 **결과(통함 / 실패 / 미시도)** 명시.
5. **`## 해결`** (해결이 안 되었을 경우 생략 가능) — 실제로 통한 방법의 **재현 가능한 단계**. 핵심 한 줄 굵게.
6. **`## 원인 추정`** (선택) — 확실한 근거가 있을 때만. 근거 없으면 생략하거나 "원인 불명" 한 문장으로.
7. **`## 아직 모르는 것`** (선택) — 재발 가능성, 남은 질문.

### Tips & Tools 템플릿 (느슨한 순서)

1. **오프닝** — 한 문단. 왜 이 기록이 유용한가, 언제 쓰는지.
2. **`## 방법`** — 핵심 단계. 순서 목록 또는 짧은 설명 + 명령·설정.
3. **`## 옵션 / 변형`** (선택) — 대안 경로, 주의할 점.
4. **`## 참고`** (선택) — 공식 문서 링크, 더 읽을 거리.

### 두 템플릿 공통

- `## 정리` 같은 총평 섹션은 **넣지 않는다**. 이 장르는 요약보다 "실제로 무엇을 했고 무엇이 통했나" 가 우선.
- 섹션별 한 문단 이상 억지로 늘리지 않는다. 짧으면 짧은 대로.

## 길이·밀도

- 100~200줄. 150줄 넘어가면 "이거 개념 글 아닌가" 의심할 것.
- Tips & Tools 는 100~100줄대가 자연스럽다.

## 이미지·스크린샷 워크플로

스크린샷을 포함하려면 **반드시** `scripts/add-screenshot.py` 를 사용한다.

### 전제

사용자는 스크린샷을 찍을 때 **의미 있는 이름으로 rename 해서 Desktop 에 둔다.** 예: `chrome-settings-filter.png`, `rectangle-shortcut-panel.png`. 파일명이 곧 `<image-name>` 인자로 쓰이므로 AI 가 이름을 임의로 바꾸지 말고 사용자가 준 이름 그대로 사용한다.

### 실행

포스트 slug 와 이미지 이름을 인자로 전달.

```bash
python scripts/add-screenshot.py <post-slug> <image-name>
```

예:

```bash
python scripts/add-screenshot.py 2026-04-22-netflix-household-chrome chrome-settings-filter
```

### 스크립트가 처리하는 것

| 단계            | 결과                                                                                |
| --------------- | ----------------------------------------------------------------------------------- |
| 원본 보존       | `assets/raw-images/{category-slug}/{post-slug}/{image-name}.{ext}` 로 복사          |
| WebP 변환       | `assets/images/{category-slug}/{post-slug}/{image-name}.webp` 생성 (폭 1920px, q85) |
| 마크다운 스니펫 | 클립보드에 `![설명](/assets/images/...)` 자동 복사                                  |

### 포스트 삽입 규칙

- 마크다운에서는 **WebP 경로만 참조**. `/assets/raw-images/...` 는 절대 참조하지 않는다.
- alt 텍스트는 "무엇이 보이는지" 구체적으로 작성 (SEO·접근성·AI 검색 모두에 도움). 클립보드 스니펫의 "설명" 을 실제 설명으로 교체.
- 이미지는 해당 단계가 설명된 문단·목록 바로 뒤에 한 줄 띄우고 삽입.

### AI 가 처음부터 해야 하는 일

사용자가 "스크린샷 X 넣어줘" 라고 하면

1. 위 명령 실행 안내 (이미 실행했다면 건너뜀)
2. 파일이 `assets/images/...` 경로에 생겼는지 확인
3. 포스트의 관련 섹션에 WebP 경로로 마크다운 삽입 + alt 텍스트 작성

## 정직성 규칙 (특히 Troubleshooting)

- **추측을 사실처럼 쓰지 않는다.** Gemini·ChatGPT·블로그 검색 답변에는 "~로 인해 발생할 수 있다" 류 **검증되지 않은 원인 설명**이 자주 섞여 있음. 그대로 옮기지 말 것.
- AI 답변·다른 블로그를 **그대로 붙여넣지 않는다.** 실제 시도·통한 것만.
- 통하지 않은 시도도 기록한다. 독자가 같은 삽질을 줄일 수 있다.
- 원인을 모르면 **"원인 불명"** 이라고 솔직하게 쓴다. 이게 이 블로그가 긴 검색 결과 속에서 가치 있는 이유.

## 시각화

- mermaid 거의 불필요. 이 장르엔 상태 전이·컴포넌트 관계가 없음.
- 비교·옵션·환경은 표.
- 스크린샷은 위 "이미지·스크린샷 워크플로" 섹션 규칙 준수.

## 금지

- 이모지 (명시 요청 없는 한)
- 과장 ("완벽히 해결", "놀랍게도", "혁신적인" 등)
- 근거 없는 인과 설명
- AI 답변 복붙
- `## 정리` 식 총평 섹션
- raw-images 를 포스트 마크다운에서 참조

## Workflow

1. `_data/categories.yml` 에서 `Daily Dev` 카테고리·서브카테고리 확인.
2. 글 성격에 맞는 서브카테고리 결정 (Troubleshooting / Tips & Tools).
3. 사용자에게 필요한 정보 확보 — Troubleshooting 이면 증상·환경·시도·통한 방법, Tips & Tools 면 세팅 단계·동기.
4. **검증 안 된 주장 필터링 패스**를 반드시 한 번 돌린다.
5. 스크린샷 있으면 `scripts/add-screenshot.py` 실행 안내 → 파일 생성 확인.
6. `_posts/daily-dev/YYYY-MM-DD-slug.md` 에 작성. 서브폴더 없으면 만든다.
7. 작성 후 짧게 파일 경로와 다룬 내용 한 줄만 보고. 본문 다시 붙여넣지 않는다.
