from datetime import UTC, datetime
from hashlib import md5, sha256

from fastapi import APIRouter, HTTPException, Query, Request, status

from app.config import get_settings
from app.deps import DbDep
from app.schemas.comment import (
    POST_SLUG_PATTERN,
    CommentCreate,
    CommentCreated,
    CommentPublic,
    CommentStatus,
)

router = APIRouter(prefix="/api/comments", tags=["comments"])


@router.get("", response_model=list[CommentPublic])
async def list_comments(
    db: DbDep,
    post: str = Query(min_length=1, max_length=200, pattern=POST_SLUG_PATTERN),
    limit: int = Query(100, ge=1, le=500),
) -> list[CommentPublic]:
    cursor = (
        db.comments.find(
            {"post_slug": post, "status": CommentStatus.APPROVED.value},
            {
                "_id": 1,
                "post_slug": 1,
                "author_name": 1,
                "author_email_hash": 1,
                "body": 1,
                "created_at": 1,
            },
        )
        .sort("created_at", 1)
        .limit(limit)
    )
    results: list[CommentPublic] = []
    async for doc in cursor:
        results.append(
            CommentPublic(
                id=str(doc["_id"]),
                post_slug=doc["post_slug"],
                author_name=doc["author_name"],
                author_email_hash=doc.get("author_email_hash"),
                body=doc["body"],
                created_at=doc["created_at"],
            )
        )
    return results


@router.post("", response_model=CommentCreated, status_code=status.HTTP_201_CREATED)
async def create_comment(
    payload: CommentCreate,
    db: DbDep,
    request: Request,
) -> CommentCreated:
    settings = get_settings()
    client_ip = request.client.host if request.client else "unknown"
    ip_hash = sha256(f"{settings.ip_hash_salt}:{client_ip}".encode()).hexdigest()

    if await db.blocked_ips.find_one({"_id": ip_hash}, {"_id": 1}) is not None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Blocked")

    email_hash: str | None = None
    if payload.author_email:
        email_hash = md5(payload.author_email.strip().lower().encode()).hexdigest()

    doc = {
        "post_slug": payload.post_slug,
        "author_name": payload.author_name.strip(),
        "author_email_hash": email_hash,
        "body": payload.body,
        "status": CommentStatus.PENDING.value,
        "created_at": datetime.now(UTC),
        "ip_hash": ip_hash,
        "user_agent": request.headers.get("user-agent", "")[:500],
    }
    result = await db.comments.insert_one(doc)
    return CommentCreated(id=str(result.inserted_id), status=CommentStatus.PENDING)
