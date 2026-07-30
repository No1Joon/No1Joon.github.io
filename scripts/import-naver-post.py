#!/usr/bin/env python3
"""
네이버 블로그 포스팅(md) → Jekyll 포스트로 변환·배치.

네이버 원문은 SmartEditor 붙여넣기용이라 마크다운이 아닌 자체 마커를 쓴다
(🔹 헤더 · ▸ 소제목 · ▶︎ 불릿 · 📷 이미지 슬롯 · ─── 구분선 · ==형광펜== · 🏷️ 해시태그).
이 스크립트는 그 마커를 마크다운으로 옮기고, Drive 에 있는 본문 이미지를
assets/raw-images(원본) + assets/images(WebP) 두 트리에 배치한다.

**본문 문장은 손대지 않는다** — 해요체·강조·수치 그대로. 구조만 바꾼다.
변환 규칙 전체는 `.claude/skills/naver-import/SKILL.md` 참조.

Usage:
  python scripts/import-naver-post.py --map scripts/naver-import-map.yml            # 전체
  python scripts/import-naver-post.py --map ... --only benford-law                  # 일부 slug
  python scripts/import-naver-post.py --map ... --dry-run                           # 미리보기

Requirements:
  brew install webp   # cwebp
  pip install pyyaml
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
NAVER_REPO = Path.home() / "Documents/projects/naver-posting"
DRIVE_ROOT = Path.home() / "Library/CloudStorage/GoogleDrive-no1jhj97@gmail.com/My Drive/assets"
DRIVE_ASSETS = DRIVE_ROOT / "postings"
# 공유 자산(브랜드 로고 등) 원본 트리. 포스트 전용 폴더에 복사되지 않은 로고를 여기서 찾는다.
DRIVE_RAW = DRIVE_ROOT / "raw"

WEBP_WIDTH = 1280
WEBP_QUALITY = 82

# 원문의 이모지 선두 줄은 세 가지로 갈린다 — 판정은 아래 classify_emoji_line().
#  🔹      : 항상 대주제 헤더
#  ⚠ 🎯 ❗ : 콜아웃(주의·핵심 정리). 짧으면 헤더, 길면 인용 블록
#  나머지  : weekly 분야 헤더로도 쓰이고 문단 첫 줄 장식으로도 쓰인다 — 길이·종결부호로 가른다
HEADER_EMOJI = "🔹"
CALLOUT_EMOJI = "⚠🎯❗"
AMBIGUOUS_EMOJI = "💰🔬📊✅⚖🌐🚨🛠💡📌🏁📈🧪🔎🗂"
# 헤더로 볼 최대 길이. 이보다 길거나 종결부호로 끝나면 본문 문장으로 본다.
HEADER_MAX_LEN = 30

RE_IMG = re.compile(
    r"^📷\s*\[이미지\s*삽입:\s*(?P<alt>[^|\]]*?)\s*(?:\|\s*(?P<file>[^\]]*?)\s*)?\]"
    r"\s*(?:->)?\s*(?:출처\s*[-–—:]\s*(?P<credit>.*))?$"
)
RE_SECTION = re.compile(
    rf"^(?P<emoji>[{HEADER_EMOJI}{CALLOUT_EMOJI}{AMBIGUOUS_EMOJI}])️?\s*(?P<text>\S.*)$"
)
# 작성자용 이미지 수집 체크리스트 — Drive 경로가 그대로 적혀 있어 발행 대상이 아니다. 블록째로 버린다.
RE_DROP_BLOCK = re.compile(r"^🖼️?\s*이미지\s*가져오기")
RE_LEAD_EMOJI = re.compile(
    r"^(?:[\U0001F300-\U0001FAFF☀-➿←-⇿⬀-⯿]️?\s*)+"
)
RE_SUB = re.compile(r"^▸\s*(?P<text>\S.*)$")
RE_BULLET = re.compile(r"^▶︎\s*(?P<text>\S.*)$")
RE_ARROW = re.compile(r"^👉\s*(?P<text>\S.*)$")
RE_SUMMARY = re.compile(r"^💬\s*(?P<text>\S.*)$")
RE_QUOTE = re.compile(r"^❝\s*(?P<text>\S.*)$")
RE_HASHTAGS = re.compile(r"^🏷️")
RE_DIVIDER = re.compile(r"^[─—–\-]{5,}$")
RE_DOT_BULLET = re.compile(r"^•\s*(?P<text>\S.*)$")
RE_HIGHLIGHT = re.compile(r"==(?P<text>[^=\n]+)==")
RE_BARE_URL = re.compile(r"^https?://\S+$")


def strip_bold(text: str) -> str:
    """헤더 텍스트의 감싸는 ** 만 제거 (문장 중간 강조는 유지)."""
    t = text.strip()
    if t.startswith("**") and t.endswith("**") and t.count("**") == 2:
        t = t[2:-2].strip()
    return t


def classify_emoji_line(emoji: str, text: str) -> str:
    """이모지 선두 줄의 정체를 판정 — 'header' | 'callout' | 'paragraph'.

    원문에서 같은 이모지가 weekly 분야 헤더(`💰 투자·비즈니스`)로도 쓰이고
    문단 첫 줄 장식(`💡 가장 쉬운 비유부터 갈게요.`)으로도 쓰인다.
    헤더는 종결부호 없는 짧은 명사구라는 점으로 가른다.
    """
    if emoji in HEADER_EMOJI:
        return "header"
    looks_like_title = len(text) <= HEADER_MAX_LEN and not text.rstrip().endswith((".", "!", "?"))
    if looks_like_title:
        return "header"
    return "callout" if emoji in CALLOUT_EMOJI else "paragraph"


class Converter:
    def __init__(self, entry: dict, dry_run: bool = False, verbose: bool = False):
        self.entry = entry
        self.dry_run = dry_run
        self.verbose = verbose
        self.slug: str = entry["slug"]
        self.cat_slug: str = entry["category_slug"]
        self.src = NAVER_REPO / entry["source"]
        self.warnings: list[str] = []
        self.image_count = 0
        self.first_image: str | None = None

        src_fm = yaml.safe_load(self.src.read_text(encoding="utf-8").split("---\n")[1])
        # image_dir 은 naver-posting 레포 기준 상대경로(assets/postings/<분기>/<키>/)
        rel = str(src_fm.get("image_dir", "")).strip().rstrip("/")
        rel = re.sub(r"^assets/postings/", "", rel)
        self.drive_dir = DRIVE_ASSETS / rel if rel else None

    # ── 이미지 ────────────────────────────────────────────────────────────
    def resolve_source(self, filename: str) -> Path | None:
        """마커의 파일명을 Drive 실제 파일로 해석.

        1) 절대경로 그대로 (원문이 공유 로고 원본을 직접 가리키는 경우)
        2) 포스트 전용 image_dir
        3) 공유 자산 raw/ 트리 이름 검색 (로고가 전용 폴더에 복사 안 된 경우)
        """
        p = Path(filename)
        if p.is_absolute():
            return p if p.is_file() else None
        if self.drive_dir is not None and (self.drive_dir / filename).is_file():
            return self.drive_dir / filename
        if DRIVE_RAW.is_dir():
            for hit in DRIVE_RAW.rglob(filename):
                if hit.is_file():
                    return hit
        return None

    def safe_stem(self, filename: str) -> str:
        """URL 안전한 ASCII 파일명. 원본은 한글 파일명이 섞여 있다.

        `4_agy_hand.png` → `04-agy-hand` · `2_구형유압_darpa_pd.jpg` → `02-darpa-pd`.
        선두 숫자는 원본의 슬롯 번호라 버리고, 실제 배치 순번을 다시 붙인다
        (누락 슬롯이 있어도 번호가 이어지고, 같은 로고를 두 번 써도 충돌하지 않는다).
        """
        ascii_part = re.sub(r"[^A-Za-z0-9]+", "-", Path(filename).stem).strip("-").lower()
        ascii_part = re.sub(r"^\d+-?", "", ascii_part)
        idx = f"{self.image_count + 1:02d}"
        return f"{idx}-{ascii_part}"[:60].rstrip("-") if ascii_part else idx

    def place_image(self, filename: str) -> str | None:
        """Drive 원본 → raw-images(원본) + images(WebP). 포스트가 참조할 경로를 반환."""
        if not filename:
            return None
        src = self.resolve_source(filename)
        if src is None:
            self.warnings.append(f"이미지 없음: {filename}")
            return None

        stem = self.safe_stem(filename)
        raw = REPO / "assets/raw-images" / self.cat_slug / self.slug / f"{stem}{src.suffix.lower()}"
        webp = REPO / "assets/images" / self.cat_slug / self.slug / f"{stem}.webp"
        ref = f"/assets/images/{self.cat_slug}/{self.slug}/{stem}.webp"

        if not self.dry_run:
            raw.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, raw)
            webp.parent.mkdir(parents=True, exist_ok=True)
            try:
                subprocess.run(
                    ["cwebp", "-q", str(WEBP_QUALITY), "-resize", str(WEBP_WIDTH), "0",
                     str(raw), "-o", str(webp)],
                    check=True, capture_output=True,
                )
            except subprocess.CalledProcessError as exc:
                self.warnings.append(f"cwebp 실패({filename}): {exc.stderr.decode()[:120]}")
                return None

        self.image_count += 1
        if self.first_image is None:
            self.first_image = ref
        return ref

    # ── 본문 ──────────────────────────────────────────────────────────────
    def convert_body(self, body: str) -> str:
        out: list[str] = []
        in_code = False
        in_refs = False  # '참고 출처' 섹션 — • 항목 + 그 아래 URL 을 링크로 합친다

        def push(line: str) -> None:
            """빈 줄 중복을 막으면서 append."""
            if line == "" and (not out or out[-1] == ""):
                return
            out.append(line)

        def push_bullet(line: str) -> None:
            """불릿을 append. 원문은 불릿 사이에 빈 줄을 두는데, 그대로 두면
            kramdown 이 loose list(항목마다 <p>)로 렌더해 간격이 벌어진다.
            바로 앞 항목과 빈 줄만으로 떨어져 있으면 그 빈 줄을 걷어내 tight list 로 만든다."""
            j = len(out)
            while j > 0 and out[j - 1] == "":
                j -= 1
            if j > 0 and out[j - 1].startswith("- "):
                del out[j:]
            out.append(line)

        lines = body.split("\n")
        i = 0
        while i < len(lines):
            raw = lines[i]
            s = raw.strip()
            i += 1

            if s.startswith("```"):
                in_code = not in_code
                push(raw)
                continue
            if in_code:
                out.append(raw)
                continue

            if not s:
                push("")
                continue
            if RE_DIVIDER.match(s):
                continue  # 헤더가 구획을 대신한다
            if RE_HASHTAGS.match(s):
                continue  # 해시태그는 front matter tags 로 이관

            # 작성자용 이미지 수집 체크리스트 — 다음 구획/헤더/해시태그까지 통째로 버린다
            if RE_DROP_BLOCK.match(s):
                self.warnings.append("작성자용 '이미지 가져오기' 블록 제외")
                while i < len(lines):
                    nxt = lines[i].strip()
                    if RE_DIVIDER.match(nxt) or RE_HASHTAGS.match(nxt) or RE_SECTION.match(nxt):
                        break
                    i += 1
                continue

            # 이미지 슬롯
            m = RE_IMG.match(s)
            if m:
                alt = (m.group("alt") or "").strip()
                fname = (m.group("file") or "").strip()
                credit = (m.group("credit") or "").strip().rstrip(".")
                ref = self.place_image(fname)
                if ref is None:
                    continue
                push("")
                push(f"![{self.inline(alt)}]({ref})")
                caption = self.inline(alt)
                if credit:
                    caption = f"{caption} — 출처: {credit}" if caption else f"출처: {credit}"
                if caption:
                    out.append(f"*{caption}*")
                push("")
                continue

            # 참고 출처 섹션의 • 항목: 다음 줄이 URL 이면 링크로 합침
            m = RE_DOT_BULLET.match(s)
            if m:
                text = self.inline(m.group("text"))
                nxt = lines[i].strip() if i < len(lines) else ""
                if in_refs and RE_BARE_URL.match(nxt):
                    push_bullet(f"- [{text}]({nxt})")
                    i += 1
                else:
                    push_bullet(f"- {text}")
                continue

            # 이모지 선두 줄 — 헤더 / 콜아웃 / 일반 문단 중 하나
            m = RE_SECTION.match(s)
            if m:
                text = strip_bold(RE_LEAD_EMOJI.sub("", m.group("text")).strip())
                kind = classify_emoji_line(m.group("emoji"), text)
                if kind == "header":
                    in_refs = "참고" in text and ("출처" in text or "자료" in text)
                    push("")
                    push(f"## {self.inline(text)}")
                    push("")
                elif kind == "callout":
                    push("")
                    push(f"> {self.inline(text)}")
                    push("")
                else:
                    push(self.inline(text))
                continue

            m = RE_SUB.match(s)
            if m:
                push("")
                push(f"### {self.inline(strip_bold(m.group('text')))}")
                push("")
                continue

            m = RE_BULLET.match(s)
            if m:
                push_bullet(f"- {self.inline(m.group('text'))}")
                continue

            m = RE_ARROW.match(s)
            if m:
                push_bullet(f"- {self.inline(m.group('text'))}")
                continue

            m = RE_SUMMARY.match(s) or RE_QUOTE.match(s)
            if m:
                push("")
                push(f"> {self.inline(m.group('text'))}")
                push("")
                continue

            # 표·리스트·일반 문단은 그대로 (들여쓰기 보존)
            out.append(self.inline(raw.rstrip()))

        text = "\n".join(out)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        return text + "\n"

    @staticmethod
    def inline(text: str) -> str:
        """인라인 표기 변환. ==형광펜== → <mark>."""
        return RE_HIGHLIGHT.sub(lambda m: f"<mark>{m.group('text')}</mark>", text)

    # ── front matter ──────────────────────────────────────────────────────
    def front_matter(self) -> str:
        e = self.entry
        fields: list[tuple[str, str]] = [
            ("title", yaml_str(e["title"])),
            ("description", yaml_str(e["description"])),
            ("date", str(e["date"])),
            ("category", e["category"]),
            ("subcategory", e["subcategory"]),
            ("tags", "[" + ", ".join(e["tags"]) + "]"),
        ]
        image = e.get("image") or self.first_image
        if image:
            fields.append(("image", image))
        if e.get("series"):
            fields.append(("series", yaml_str(e["series"])))
            fields.append(("part", str(e["part"])))
        body = "\n".join(f"{k}: {v}" for k, v in fields)
        return f"---\n{body}\n---\n"

    def run(self) -> Path:
        text = self.src.read_text(encoding="utf-8")
        parts = text.split("---\n", 2)
        if len(parts) < 3:
            raise SystemExit(f"front matter 파싱 실패: {self.src}")
        converted = self.convert_body(parts[2])
        dest = REPO / "_posts" / self.cat_slug / f"{self.entry['date']}-{self.slug}.md"
        content = self.front_matter() + "\n" + converted
        if not self.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
        return dest


def yaml_str(value: str) -> str:
    return '"' + str(value).replace('"', '\\"') + '"'


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", required=True, help="변환 매핑 YAML")
    ap.add_argument("--only", nargs="*", help="이 slug 들만 변환")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    entries = yaml.safe_load(Path(args.map).read_text(encoding="utf-8"))
    if args.only:
        entries = [e for e in entries if e["slug"] in args.only]
        if not entries:
            sys.exit("--only 에 매칭되는 slug 가 없습니다.")

    total_warn = 0
    for e in entries:
        conv = Converter(e, dry_run=args.dry_run, verbose=args.verbose)
        dest = conv.run()
        flag = "" if not conv.warnings else f"  ⚠ {len(conv.warnings)}"
        print(f"{dest.relative_to(REPO)}  (이미지 {conv.image_count}){flag}")
        for w in conv.warnings:
            total_warn += 1
            print(f"    - {w}")
    print(f"\n{len(entries)}편 변환 완료 · 경고 {total_warn}건" + (" (dry-run)" if args.dry_run else ""))


if __name__ == "__main__":
    main()
