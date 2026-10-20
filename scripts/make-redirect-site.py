#!/usr/bin/env python3
"""github.io 용 리다이렉트 사이트 생성.

  python3 scripts/make-redirect-site.py [_site] [_redirect]

블로그 본체는 cailmeal.com(Firebase Hosting)에서 서빙한다. GitHub Pages(no1joon.github.io)에는
빌드 결과의 HTML 페이지마다 같은 경로의 cailmeal.com 으로 즉시 넘기는 페이지만 배포한다.
GitHub Pages 에 커스텀 도메인을 걸지 않는 이유 — 걸면 같은 계정의 프로젝트 페이지
(/quickglot/ 등)까지 그 도메인으로 끌려간다.
"""
import html
import sys
from pathlib import Path

NEW = "https://cailmeal.com"

STUB = """<!doctype html>
<html><head><meta charset="utf-8">
<title>Moved to cailmeal.com</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<script>location.replace({js} + location.search + location.hash)</script>
</head><body><p><a href="{url}">{url}</a></p></body></html>
"""

# 목록에 없는 경로는 같은 경로의 cailmeal.com 으로 넘긴다
NOT_FOUND = """<!doctype html>
<html><head><meta charset="utf-8"><title>Moved to cailmeal.com</title>
<script>location.replace("{new}" + location.pathname + location.search + location.hash)</script>
</head><body><p><a href="{new}/">{new}</a></p></body></html>
"""


def target(rel: Path) -> str:
    parts = rel.as_posix()
    if parts == "index.html":
        return NEW + "/"
    if parts.endswith("/index.html"):
        return f"{NEW}/{parts[:-len('index.html')]}"
    return f"{NEW}/{parts}"


def main() -> None:
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
    dst = Path(sys.argv[2] if len(sys.argv) > 2 else "_redirect")
    count = 0
    for page in src.rglob("*.html"):
        rel = page.relative_to(src)
        url = target(rel)
        out = dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(STUB.format(url=html.escape(url), js='"' + url.replace('"', '\\"') + '"'))
        count += 1
    (dst / "404.html").write_text(NOT_FOUND.format(new=NEW))
    (dst / "robots.txt").write_text("User-agent: *\nAllow: /\n")
    print(f"redirect pages: {count}")


if __name__ == "__main__":
    main()
