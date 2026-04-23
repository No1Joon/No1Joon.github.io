# assets/

블로그 정적 자산 디렉터리.

## Structure

- `assets/css/` — 스타일시트.
- `assets/images/{category-slug}/{post-slug}/{name}.webp` — 포스트에서 참조하는 최적화된 WebP. 마크다운에서는 **이 경로만 참조**.
- `assets/raw-images/{category-slug}/{post-slug}/{name}.{png,jpg}` — 원본 스크린샷·이미지 보존용. 포스트 참조 대상 아님. `.gitignore` 로 git 추적 제외 (배포 산출물에 포함되지 않음).

두 트리는 **동일한 `{category-slug}/{post-slug}/` 구조**를 미러링 — 같은 포스트의 원본과 최적화본이 대응되도록 유지.

## Skills

- `.claude/skills/daily-post/SKILL.md` — Daily Dev 포스트의 스크린샷 워크플로. `scripts/add-screenshot.py` 사용이 필수.

## References

See @scripts/add-screenshot.py for the screenshot → WebP conversion tool
