from typing import Annotated

from fastapi import Depends, Header, HTTPException, status
from google.auth.transport import requests as grequests
from google.oauth2 import id_token

from app.config import Settings, get_settings


def verify_google_id_token(token: str, settings: Settings) -> str:
    """Verify a Google ID token; return the verified email on success."""
    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            grequests.Request(),
            settings.google_oauth_client_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid ID token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e

    if not idinfo.get("email_verified"):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email not verified")

    email = idinfo.get("email", "")
    if email not in settings.admin_emails:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")

    return email


async def get_current_admin(
    authorization: Annotated[str | None, Header()] = None,
) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = authorization.removeprefix("Bearer ").strip()
    settings = get_settings()

    # Dev-only local bypass: `Bearer dev:<email>` skips Google verification.
    # Gate is strict — only active when ENV=dev. Never usable in prod.
    if settings.env == "dev" and token.startswith("dev:"):
        email = token.removeprefix("dev:")
        if email not in settings.admin_emails:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not in admin allowlist",
            )
        return email

    if not settings.google_oauth_client_id:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Admin auth not configured",
        )

    return verify_google_id_token(token, settings)


AdminDep = Annotated[str, Depends(get_current_admin)]
