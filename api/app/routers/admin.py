from datetime import UTC, datetime
from typing import Annotated, Any

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, Query, status
from pymongo import DESCENDING, ReturnDocument

from app.deps import DbDep
from app.schemas.admin import (
    BlockIpRequest,
    BlockIpResult,
    CommentAdminView,
    StatusPatch,
)
from app.schemas.comment import CommentStatus
from app.security.admin_auth import AdminDep

router = APIRouter(prefix="/api/admin", tags=["admin"])


def _oid(value: str) -> ObjectId:
    try:
        return ObjectId(value)
    except (InvalidId, TypeError) as e:
        raise HTTPException(status_code=400, detail="Invalid id") from e


def _to_admin_view(doc: dict[str, Any]) -> CommentAdminView:
    return CommentAdminView(
        id=str(doc["_id"]),
        post_slug=doc["post_slug"],
        author_name=doc["author_name"],
        author_email_hash=doc.get("author_email_hash"),
        body=doc["body"],
        status=doc["status"],
        created_at=doc["created_at"],
        ip_hash=doc["ip_hash"],
        user_agent=doc.get("user_agent", ""),
    )


@router.get("/comments", response_model=list[CommentAdminView])
async def list_admin_comments(
    db: DbDep,
    admin: AdminDep,
    status_filter: Annotated[CommentStatus | None, Query(alias="status")] = None,
    limit: Annotated[int, Query(ge=1, le=200)] = 50,
) -> list[CommentAdminView]:
    filt: dict[str, Any] = {}
    if status_filter is not None:
        filt["status"] = status_filter.value
    cursor = db.comments.find(filt).sort("created_at", DESCENDING).limit(limit)
    return [_to_admin_view(d) async for d in cursor]


@router.patch("/comments/{comment_id}", response_model=CommentAdminView)
async def update_comment_status(
    comment_id: str,
    payload: StatusPatch,
    db: DbDep,
    admin: AdminDep,
) -> CommentAdminView:
    oid = _oid(comment_id)
    result = await db.comments.find_one_and_update(
        {"_id": oid},
        {"$set": {"status": payload.status.value}},
        return_document=ReturnDocument.AFTER,
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return _to_admin_view(result)


@router.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(
    comment_id: str,
    db: DbDep,
    admin: AdminDep,
) -> None:
    oid = _oid(comment_id)
    result = await db.comments.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")


@router.post("/block-ip", response_model=BlockIpResult, status_code=status.HTTP_201_CREATED)
async def block_ip(
    payload: BlockIpRequest,
    db: DbDep,
    admin: AdminDep,
) -> BlockIpResult:
    oid = _oid(payload.comment_id)
    comment = await db.comments.find_one({"_id": oid}, {"ip_hash": 1})
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    ip_hash: str = comment["ip_hash"]

    await db.blocked_ips.update_one(
        {"_id": ip_hash},
        {
            "$set": {
                "blocked_at": datetime.now(UTC),
                "blocked_by": admin,
                "source_comment_id": str(oid),
                "reason": payload.reason,
            }
        },
        upsert=True,
    )
    marked = await db.comments.update_many(
        {"ip_hash": ip_hash, "status": CommentStatus.PENDING.value},
        {"$set": {"status": CommentStatus.SPAM.value}},
    )
    return BlockIpResult(ip_hash=ip_hash, marked_as_spam=marked.modified_count)
