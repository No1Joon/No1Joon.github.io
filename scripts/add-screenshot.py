#!/usr/bin/env python3
"""
Desktop 최신 스크린샷을 블로그 포스트 이미지로 최적화·배치.

원본(PNG/JPG)은 assets/raw-images/ 에 보존, 포스트 참조용 WebP 는 assets/images/ 에 생성.

Usage:
  python scripts/add-screenshot.py <post-slug> <image-name> [--source PATH]

Examples:
  # 데스크탑 최신 스크린샷 자동 선택
  python scripts/add-screenshot.py 2026-04-22-netflix-household-chrome chrome-settings-filter

  # 특정 파일 지정
  python scripts/add-screenshot.py <slug> <name> --source "~/Downloads/foo.png"

Outputs:
  assets/raw-images/{category-slug}/{post-slug}/{name}.{ext}   # 원본 보존 (png/jpg)
  assets/images/{category-slug}/{post-slug}/{name}.webp        # 포스트 참조용 (WebP)

Requirements:
  brew install webp   # cwebp 바이너리
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path


RAW_EXTS = {".png", ".jpg", ".jpeg"}


def find_latest_screenshot(desktop: Path) -> Path:
    shots = sorted(
        [p for p in desktop.glob("Screenshot *") if p.suffix.lower() in RAW_EXTS],
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not shots:
        sys.exit("Desktop 에 Screenshot 파일이 없습니다.")
    return shots[0]


def find_post(slug: str) -> Path:
    matches = list(Path("_posts").rglob(f"*{slug}*.md"))
    if not matches:
        sys.exit(f"'{slug}' 매칭 포스트 없음. _posts/ 아래 확인하세요.")
    if len(matches) > 1:
        sys.exit(f"여러 포스트가 매치됨: {[str(p) for p in matches]}")
    return matches[0]


def convert(src: Path, dst: Path, width: int, quality: int) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["cwebp", "-q", str(quality), "-resize", str(width), "0", str(src), "-o", str(dst)],
        check=True,
        capture_output=True,
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", help="포스트 slug (파일명 일부 매치)")
    ap.add_argument("name", help="이미지 파일명 (확장자 제외)")
    ap.add_argument("--source", help="원본 이미지 경로. 기본: Desktop 최신 스크린샷")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--quality", type=int, default=85)
    args = ap.parse_args()

    src = Path(args.source).expanduser() if args.source else find_latest_screenshot(Path.home() / "Desktop")
    if src.suffix.lower() not in RAW_EXTS:
        sys.exit(f"지원하지 않는 확장자: {src.suffix} (지원: {', '.join(sorted(RAW_EXTS))})")

    post = find_post(args.slug)
    category = post.parent.name

    raw_dst = Path("assets/raw-images") / category / args.slug / f"{args.name}{src.suffix.lower()}"
    webp_dst = Path("assets/images") / category / args.slug / f"{args.name}.webp"

    raw_dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, raw_dst)
    convert(raw_dst, webp_dst, args.width, args.quality)

    snippet = f"![설명](/{webp_dst})"
    subprocess.run(["pbcopy"], input=snippet.encode())

    src_kb = src.stat().st_size / 1024
    webp_kb = webp_dst.stat().st_size / 1024
    ratio = webp_kb / src_kb * 100
    print(f"raw : {raw_dst} ({src_kb:.0f} KB)")
    print(f"webp: {webp_dst} ({webp_kb:.0f} KB, {ratio:.0f}% of original)")
    print(f"clipboard: {snippet}")


if __name__ == "__main__":
    main()
