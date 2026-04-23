from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.comment import CommentStatus


class CommentAdminView(BaseModel):
    id: str
    post_slug: str
    author_name: str
    author_email_hash: str | None = None
    body: str
    status: CommentStatus
    created_at: datetime
    ip_hash: str
    user_agent: str


class StatusPatch(BaseModel):
    status: CommentStatus


class BlockIpRequest(BaseModel):
    comment_id: str = Field(min_length=1)
    reason: str | None = Field(default=None, max_length=200)


class BlockIpResult(BaseModel):
    ip_hash: str
    marked_as_spam: int
