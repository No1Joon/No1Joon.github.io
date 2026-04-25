from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, EmailStr, Field


class CommentStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    SPAM = "spam"


POST_SLUG_PATTERN = r"^[a-z0-9\-]+$"


class CommentCreate(BaseModel):
    post_slug: str = Field(min_length=1, max_length=200, pattern=POST_SLUG_PATTERN)
    author_name: str = Field(min_length=1, max_length=50)
    author_email: EmailStr | None = None
    body: str = Field(min_length=1, max_length=4000)
    turnstile_token: str = Field(min_length=1, max_length=2048)


class CommentPublic(BaseModel):
    id: str
    post_slug: str
    author_name: str
    author_email_hash: str | None = None
    body: str
    created_at: datetime


class CommentCreated(BaseModel):
    id: str
    status: CommentStatus
