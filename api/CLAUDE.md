# api/

No1Joon 블로그 댓글용 FastAPI 서비스. Cloud Run 에 배포되고 MongoDB Atlas (M0, GCP us-central1) 를 데이터 저장소로 사용.

## Structure

- `app/main.py` — FastAPI 앱 팩토리, lifespan 으로 DB 연결·인덱스 보장.
- `app/config.py` — pydantic-settings 환경설정 (env/CSV 리스트 파싱).
- `app/db.py` — pymongo `AsyncMongoClient` 싱글톤, 인덱스 생성.
- `app/deps.py` — FastAPI DI (요청 스코프 DB 핸들).
- `app/schemas/` — Pydantic 입출력 모델 (현재: `comment`).
- `app/routers/` — 엔드포인트 (`health`, `comments` 공개, `admin` 관리자).
- `app/security/` — 보안 레이어 (보안 헤더, Google ID 토큰 검증, Turnstile CAPTCHA 검증; 추후: 레이트리밋).
- `docker-compose.yml` — 로컬 개발용 mongo:7.
- `Dockerfile` — Cloud Run 컨테이너 빌드 (uv sync + uvicorn).
- `.env.example` — 필요한 환경 변수 템플릿.

## Commands

- `docker compose up -d` — 로컬 mongo 기동 (`mongodb://localhost:27017`).
- `uv sync` — 의존성 설치.
- `uv run uvicorn app.main:app --reload --port 8000` — 로컬 개발 서버.
- `uv run ruff check .` / `uv run ruff format .` — 린트·포맷.
- `uv run pytest` — 테스트 실행.
- `docker build -t comments-api . && docker run -p 8080:8080 --env-file .env comments-api` — 컨테이너 빌드·실행.

## Environment

- Python 3.12 (`.python-version`).
- 로컬: `docker compose up` 후 `MONGO_URI=mongodb://localhost:27017`, `MONGO_DB=no1joon_comments_dev`.
- 프로덕션: Atlas SRV URI 를 **GCP Secret Manager** 에 저장, Cloud Run 이 Secret 바인딩으로 주입.
- Cloud Run 설정: `max-instances=1`, `concurrency=80`, `mongo_pool_size=10` (Atlas M0 100 연결 한도 내).
- Turnstile secret / Google OAuth Client ID / Admin emails allowlist 는 Cloud Run 환경변수로 주입.
- Atlas M0 은 초과분 자동 과금 없음 (하드 캡). 별도 kill-switch 불필요.

## References

See @CLAUDE.md for project-wide overview
