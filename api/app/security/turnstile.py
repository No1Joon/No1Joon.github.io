import httpx
from fastapi import HTTPException, status

from app.config import Settings

TURNSTILE_VERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"


async def verify_turnstile_token(
    token: str,
    settings: Settings,
    remote_ip: str | None = None,
) -> None:
    """Verify a Cloudflare Turnstile token. Raises HTTPException on failure."""
    # Dev-only local bypass: `dev:ok` passes without calling Cloudflare.
    # Gate is strict — only active when ENV=dev. Never usable in prod.
    if settings.env == "dev" and token == "dev:ok":
        return

    if not settings.turnstile_secret_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Captcha not configured",
        )

    data = {"secret": settings.turnstile_secret_key, "response": token}
    if remote_ip:
        data["remoteip"] = remote_ip

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.post(TURNSTILE_VERIFY_URL, data=data)
            resp.raise_for_status()
            result = resp.json()
    except (httpx.HTTPError, ValueError) as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Captcha verification unreachable",
        ) from e

    if not result.get("success"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Captcha failed",
        )
