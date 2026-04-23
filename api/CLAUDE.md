# api/

No1Joon 블로그 댓글용 FastAPI 서비스. Cloud Run 에 배포되고 Firestore 를 데이터 저장소로 사용.

## Structure

- `app/main.py` — FastAPI 앱 팩토리. 미들웨어·라우터 조립.
- `app/config.py` — pydantic-settings 기반 환경설정 (env/CSV 리스트 파싱).
- `app/routers/` — 엔드포인트 (현재: `health`, 추후: `comments`, `admin`).
- `app/security/` — 보안 레이어 (현재: 보안 헤더 미들웨어, 추후: Turnstile 검증·관리자 OAuth·레이트리밋).
- `Dockerfile` — Cloud Run 컨테이너 빌드 (uv sync + uvicorn).
- `.env.example` — 필요한 환경 변수 템플릿.

## Commands

- `uv sync` — 의존성 설치 (`.venv/` 생성).
- `uv run uvicorn app.main:app --reload --port 8000` — 로컬 개발 서버.
- `uv run ruff check .` / `uv run ruff format .` — 린트·포맷.
- `uv run pytest` — 테스트 실행.
- `docker build -t comments-api . && docker run -p 8080:8080 --env-file .env comments-api` — 컨테이너 빌드·실행.

## Environment

- Python 3.12 (`.python-version`).
- 결제 수단 등록된 GCP 프로젝트 필요 (Always Free 초과분은 자동 과금). 예산 알림 설정 권장.
- 로컬 개발 시 Firestore 는 에뮬레이터 사용 (`FIRESTORE_EMULATOR_HOST`).
- Turnstile secret / Google OAuth Client ID / Admin emails allowlist 는 Cloud Run 환경변수로 주입.

## References

See @CLAUDE.md for project-wide overview
