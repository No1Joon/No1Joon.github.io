from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    env: Literal["dev", "prod"] = "dev"

    allowed_origins: list[str] = Field(default_factory=list)

    admin_emails: list[str] = Field(default_factory=list)
    google_oauth_client_id: str = ""

    turnstile_secret_key: str = ""

    gcp_project_id: str = ""
    firestore_emulator_host: str = ""

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
