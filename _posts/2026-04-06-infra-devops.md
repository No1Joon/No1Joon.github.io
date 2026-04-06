---
layout: post
title: "인프라 · DevOps — Docker Compose · pnpm · uv"
description: "로컬 개발 환경 구성과 pnpm 모노레포, uv 패키지 매니저 선택 이유"
date: 2026-04-06
category: Infra
tags: [Docker, Docker-Compose, pnpm, uv, monorepo]
---

## 기술 목록

| 기술 | 용도 |
|------|------|
| Docker Compose | 로컬 개발 환경 (PostgreSQL + Backend + Frontend) |
| pnpm | Frontend 패키지 관리 (workspace monorepo) |
| uv | Backend 패키지 관리 (pyproject.toml 기반) |

---

## Docker Compose 구성

로컬 환경에서 세 서비스를 단일 명령으로 기동한다.

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: showmearch
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  backend:
    build: ./backend
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql+asyncpg://dev:dev@db/showmearch
    depends_on:
      - db

  frontend:
    build: ./frontend
    command: pnpm dev --host
    ports:
      - "5173:5173"
    depends_on:
      - backend

volumes:
  pgdata:
```

```bash
# 전체 기동
docker compose up -d

# 로그 확인
docker compose logs -f backend

# DB 마이그레이션 실행
docker compose exec backend alembic upgrade head
```

---

## pnpm workspaces (모노레포)

```
root/
├── package.json          # workspace 루트
├── pnpm-workspace.yaml
├── frontend/
│   └── package.json
└── packages/
    └── shared-types/     # 공유 타입 패키지
```

```yaml
# pnpm-workspace.yaml
packages:
  - "frontend"
  - "packages/*"
```

```bash
# 특정 패키지에 의존성 추가
pnpm --filter frontend add zustand

# 전체 워크스페이스 설치
pnpm install

# 빌드 (turbo 없이)
pnpm --filter frontend build
```

---

## uv — Python 패키지 관리

<div class="callout why">
<div class="callout-title">왜 uv인가</div>

pip / poetry 대비 resolver 속도가 **10–100× 빠르다**. `pyproject.toml` 표준을 그대로 따르면서도 lock 파일 관리가 단순하다.

```bash
# 의존성 설치 (lock 파일 기반)
uv sync

# 패키지 추가
uv add fastapi

# 개발 의존성 추가
uv add --dev pytest pytest-asyncio

# 가상환경 자동 관리 — .venv/에 생성됨
uv run pytest
```
</div>

### pip vs poetry vs uv 비교

| 항목 | pip | poetry | uv |
|------|-----|--------|----|
| Resolver 속도 | 기준 | 느림 | **10–100× 빠름** |
| lock 파일 | 없음 | poetry.lock | uv.lock |
| pyproject.toml | 부분 지원 | 완전 지원 | 완전 지원 |
| 가상환경 관리 | 수동 | 자동 | 자동 |
| Rust 기반 | — | — | ✓ |

---

## 개발 플로우

```bash
# 처음 셋업
git clone ...
docker compose up -d
docker compose exec backend uv sync
docker compose exec backend alembic upgrade head

# 일상 개발
docker compose up -d          # 서비스 기동
# 코드 수정 → HMR/--reload 자동 반영

# 테스트
docker compose exec backend uv run pytest
docker compose exec frontend pnpm test
```
