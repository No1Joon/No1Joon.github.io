#!/usr/bin/env python3
"""영문판 자가 렌더 이미지 생성.

  python3 scripts/render-en-images.py <slug> [<slug> ...]
입력: scripts/naver-en-slots/<slug>.yml — 번역한 슬롯 목록(원 슬롯과 같은 file 키).
      이 파일이 없으면 원문 슬롯에 이미 들어 있는 en: 블록을 그대로 쓴다(2026-10-15 이후 원문은 chart·items 에 en: 을 직접 씀).
chart·items 는 en: 블록(naver-posting 렌더러가 <stem>_en.png 로 그림), terminal 은 글자 키를 직접 덮어씀.
1) 원문 frontmatter 의 슬롯을 번역본으로 바꾼 임시 md 를 만들어 naver-posting 렌더 스크립트로 PNG 생성 (출력은 scratch)
2) 원문 📷 마커 순서 ↔ 한국어 포스트 이미지 참조 순서로 짝을 지어, 같은 stem 으로
   assets/raw-images/<cat>/<slug>/en/*.png + assets/images/<cat>/<slug>/en/*.webp 배치
3) _en_posts 영문판이 있으면 해당 이미지 경로를 /en/ 경로로 교체
"""
import re, subprocess, sys, shutil, tempfile
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parent.parent
SLOTS = REPO / 'scripts/naver-en-slots'
OUT = Path(tempfile.gettempdir()) / 'naver-en-render'
NP = Path('/Users/joon/Documents/projects/naver-posting')
BLOG = NP / 'naver-posting-it'

def run(slug):
    mp = yaml.safe_load((REPO / 'scripts/naver-import-map.yml').read_text())
    ent = next(e for e in mp if e['slug'] == slug)
    src = NP / ent['source']
    text = src.read_text()
    m = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S)
    fm = yaml.safe_load(m.group(1))
    if (SLOTS / f'{slug}.yml').exists():
        over = {s['file']: s for s in yaml.safe_load((SLOTS / f'{slug}.yml').read_text())}
    else:
        over = {s['file']: {'file': s['file'], 'en': s['en']} for s in fm.get('images') or [] if isinstance(s, dict) and s.get('en')}
    if not over:
        print(f'{slug}: 영문 슬롯 없음 — 자가 렌더 이미지가 없는 편이면 정상, 건너뜀')
        return

    out = OUT / slug
    shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    fm2 = dict(fm); fm2['image_dir'] = str(out)
    def merge(s):
        o = over[s['file']]
        if 'en' in o:          # chart·items: 렌더러가 en: 블록으로 <stem>_en.png 를 함께 그린다
            return {**s, 'en': o['en']}
        return {**s, **o}      # terminal: 글자 키를 직접 덮어쓴다
    fm2['images'] = [merge(s) for s in fm.get('images') or [] if isinstance(s, dict) and s.get('file') in over]
    missing = set(over) - {s['file'] for s in fm2['images']}
    if missing: raise SystemExit(f'원문에 없는 file: {missing}')
    tmp = out / 'post.md'
    tmp.write_text('---\n' + yaml.dump(fm2, allow_unicode=True, sort_keys=False) + '---\n')
    for sc in ('render_charts.py', 'render_items.py', 'render_terminal.py'):
        if not any(s.get('type') == {'render_charts.py': 'chart', 'render_items.py': 'items', 'render_terminal.py': 'terminal'}[sc] for s in fm2['images']):
            continue
        r = subprocess.run(['/usr/local/bin/python3.12', f'scripts/{sc}', str(tmp), '--force'], cwd=BLOG, capture_output=True, text=True)
        print(r.stdout.strip()); 
        if r.returncode: raise SystemExit(r.stderr)

    # 마커 순서 ↔ 한국어 포스트 참조 순서
    files = [mm.group(1).strip() for mm in re.finditer(r'📷 \[이미지 삽입:[^|\]]*\|\s*([^\]|]+?)\s*(?:\|[^\]]*)?\]', m.group(2))]
    kr = next((REPO / '_posts').glob(f'*/*-{slug}.md'))
    refs = re.findall(r'\(/assets/images/[^)]+\.webp\)', kr.read_text())
    refs = [r[1:-1] for r in refs]
    if len(files) != len(refs): raise SystemExit(f'마커 {len(files)} ≠ 참조 {len(refs)}')
    cat = ent['category_slug']
    pairs = {}
    for f, ref in zip(files, refs):
        if f not in over: continue
        png = out / (f'{Path(f).stem}_en.png' if 'en' in over[f] else f)
        if not png.exists(): raise SystemExit(f'렌더 결과 없음: {f}')
        stem = Path(ref).stem
        raw = REPO / 'assets/raw-images' / cat / slug / 'en' / f'{stem}.png'
        webp = REPO / 'assets/images' / cat / slug / 'en' / f'{stem}.webp'
        raw.parent.mkdir(parents=True, exist_ok=True); webp.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(png, raw)
        subprocess.run(['cwebp', '-q', '82', '-resize', '1280', '0', str(raw), '-o', str(webp)], check=True, capture_output=True)
        pairs[ref] = f'/assets/images/{cat}/{slug}/en/{stem}.webp'
    print(f'{slug}: EN 이미지 {len(pairs)}장')
    en = list((REPO / '_en_posts').glob(f'*/*-{slug}.md'))
    if en:
        t = en[0].read_text()
        for a, b in pairs.items(): t = t.replace(f'({a})', f'({b})')
        en[0].write_text(t); print('  영문판 경로 교체 완료')


for s in sys.argv[1:]:
    run(s)
