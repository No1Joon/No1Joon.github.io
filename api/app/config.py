from functools import lru_cache
from typing import Annotated, Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    env: Literal["dev", "prod"] = "dev"

    allowed_origins: Annotated[list[str], NoDecode] = Field(default_factory=list)

    admin_emails: Annotated[list[str], NoDecode] = Field(default_factory=list)
    google_oauth_client_id: str = ""

    turnstile_secret_key: str = ""

    mongo_uri: str = ""
    mongo_db: str = "no1joon_comments"
    mongo_pool_size: int = 10

    ip_hash_salt: str = ""

    @field_validator("allowed_origins", "admin_emails", mode="before")
    @classmethod
    def _split_csv(cls, v: object) -> object:
        if isinstance(v, str):
            return [item.strip() for item in v.split(",") if item.strip()]
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()
