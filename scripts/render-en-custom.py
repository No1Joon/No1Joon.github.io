#!/usr/local/bin/python3.12
"""영문판 커스텀 차트 생성 — `form: custom` 슬롯은 render-en-images.py 가 못 그리므로 여기서 그린다.

  /usr/local/bin/python3.12 scripts/render-en-custom.py

naver-posting 의 차트 스크립트(scripts/charts/<포스트키>.py)에서 그리는 함수만 빌려 오고, 글자만 영문으로 바꿔
assets/raw-images/<cat>/<slug>/en/ + assets/images/<cat>/<slug>/en/ 에 두고 영문판 경로를 /en/ 으로 교체한다.
"""
import importlib.util
import json
import os
import random
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BLOG = Path('/Users/joon/Documents/projects/naver-posting/naver-posting-it')
sys.path.insert(0, str(BLOG / 'scripts'))

from chart_style import setup, finish, tints, set_lang, _init, bold, safe, INK, MUTE  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from PIL import Image  # noqa: E402


def load(name):
    spec = importlib.util.spec_from_file_location('chart_mod', BLOG / 'scripts/charts' / name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def place(cat, slug, stem, png):
    """raw 는 PNG·GIF 그대로, 게시본은 webp — 애니메이션은 cwebp 가 못 읽어 gif2webp 로."""
    raw = REPO / 'assets/raw-images' / cat / slug / 'en' / f'{stem}{png.suffix}'
    webp = REPO / 'assets/images' / cat / slug / 'en' / f'{stem}.webp'
    raw.parent.mkdir(parents=True, exist_ok=True)
    webp.parent.mkdir(parents=True, exist_ok=True)
    raw.write_bytes(png.read_bytes())
    if png.suffix == '.gif':
        cmd = ['gif2webp', '-q', '82', str(raw), '-o', str(webp)]
    else:
        cmd = ['cwebp', '-q', '82', '-resize', '1280', '0', str(raw), '-o', str(webp)]
    subprocess.run(cmd, check=True, capture_output=True)
    en = next((REPO / '_en_posts').glob(f'*/*-{slug}.md'))
    old, new = f'/assets/images/{cat}/{slug}/{stem}.webp', f'/assets/images/{cat}/{slug}/en/{stem}.webp'
    en.write_text(en.read_text().replace(f'({old})', f'({new})'))
    print('ok', new)


def graph_sandwich(tmp):
    m = load('20260925_그래프_샌드위치추측.py')
    THEME, N = m.THEME, m.N
    pal = tints(THEME, 3)

    # 두 모형 비교 — 원 스크립트와 같은 시드·간선 규칙
    random.seed(7)
    pts = m.ring()
    reg = set()
    for i in range(N):
        reg.add((min(i, (i + 1) % N), max(i, (i + 1) % N)))
    for i in range(N // 2):
        reg.add((i, i + N // 2))
    binom = set()
    for i in range(N):
        for j in range(i + 1, N):
            if random.random() < 3 / (N - 1):
                binom.add((i, j))
    fig, axes = setup('Two random graph models', theme=THEME, figsize=(10.4, 5.6))
    fig.delaxes(axes)
    fig.subplots_adjust(top=.76, bottom=.14)
    ax1, ax2 = fig.add_subplot(1, 2, 1), fig.add_subplot(1, 2, 2)
    m.draw(ax1, pts, sorted(reg), pal[0], 'd-regular graph',
           'Every vertex has the same number of edges\n(shown with degree 3)')
    m.draw(ax2, pts, sorted(binom), pal[1], 'Binomial random graph G(n, p)',
           'Each edge drawn independently with the same probability\n(degree varies by vertex)')
    out1 = tmp / 'sandwich-1.png'
    finish(fig, ax1, 'Illustrative example · not data from the paper', str(out1))

    # 샌드위치 구조
    random.seed(11)
    pts = m.ring()
    lower = {(min(i, (i + 1) % N), max(i, (i + 1) % N)) for i in range(N)}
    mid = set(lower) | {(i, i + N // 2) for i in range(N // 2)}
    upper = set(mid) | {(min(e), max(e)) for e in [(0, 4), (1, 7), (3, 9), (5, 10), (2, 8), (0, 3), (6, 9), (4, 11)]}
    fig, axes = setup('The sandwich structure', 'Left fits entirely inside the middle, the middle inside the right',
                      theme=THEME, figsize=(12.6, 5.2))
    fig.delaxes(axes)
    fig.subplots_adjust(top=.72, bottom=.14)
    specs = [(lower, pal[2], 'G_low ~ G(n, smaller p)', 'Fewest edges'),
             (mid, pal[0], 'G ~ random d-regular', 'The target of analysis'),
             (upper, pal[1], 'G_high ~ G(n, larger p)', 'Most edges')]
    for k, (edges, color, title, note) in enumerate(specs, start=1):
        m.draw(fig.add_subplot(1, 3, k), pts, sorted(edges), color, title, note)
    out2 = tmp / 'sandwich-2.png'
    finish(fig, fig.axes[0], 'Illustrative example · not data from the paper', str(out2))

    place('math', 'graph-sandwich-conjecture', '02-chart', out1)
    place('math', 'graph-sandwich-conjecture', '03-chart', out2)


LAWS_EN = {'민법': 'Civil Act', '행정소송법': 'Administrative Litigation Act', '민사소송법': 'Civil Procedure Act',
           '형법': 'Criminal Act', '형사소송법': 'Criminal Procedure Act', '헌법': 'Constitution',
           '상법': 'Commercial Act', '근로기준법': 'Labor Standards Act'}


def rag_map(tmp):
    """판결 임베딩 3D 지도 GIF — 원 스크립트 main() 의 글자만 영문으로."""
    m = load('20260930_초간단RAG_판결서.py')
    _init()
    set_lang('en')
    d = json.load(open(BLOG / m.SRC, encoding='utf-8'))
    P = np.array(d['points'], dtype=float)
    law = P[:, 4].astype(int)
    total = {k: int((law == k).sum()) for k in range(len(d['laws']))}
    fig = plt.figure(figsize=(m.SIZE_IN, m.SIZE_IN * 1.05), dpi=m.DPI)
    fig.text(0.5, 0.955, 'bge-m3 embedding map of 16,800 rulings', ha='center', fontproperties=bold(17), color=INK)
    fig.text(0.5, 0.925, '*Color = main statute of the referenced provisions · gray = other statutes or none',
             ha='center', fontsize=10, color=MUTE)
    ax = fig.add_axes([-0.08, 0.06, 1.16, 0.90], projection='3d')
    ax.set_axis_off()
    lo, hi = np.percentile(P[:, :3], 1, axis=0), np.percentile(P[:, :3], 99, axis=0)
    keep = np.all((P[:, :3] >= lo) & (P[:, :3] <= hi), axis=1)
    P, law = P[keep], law[keep]
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1]); ax.set_zlim(lo[2], hi[2])
    ax.set_box_aspect((1, 1, 1), zoom=1.25)
    bg = law < 0
    ax.scatter(P[bg, 0], P[bg, 1], P[bg, 2], s=2.0, c='#c9ccd1', alpha=.22, linewidths=0)
    for k, name in enumerate(d['laws']):
        sel = law == k
        ax.scatter(P[sel, 0], P[sel, 1], P[sel, 2], s=5.0, c=m.PALETTE[k], alpha=.9, linewidths=0,
                   label=f'{LAWS_EN[name]} ({total[k]:,})')
    # 영문 법령명이 길어 4열 대신 3열
    leg = fig.legend(loc='lower center', ncol=3, frameon=False, fontsize=8.2, markerscale=3.2,
                     handletextpad=.2, columnspacing=.9, bbox_to_anchor=(0.5, 0.005))
    for t in leg.get_texts():
        t.set_color(INK)
    fig.text(0.99, 0.105, 'Source: AI Hub anonymized court-ruling data · UMAP 3D · points outside the 1st–99th percentile per axis omitted · self-rendered',
             ha='right', fontsize=6.6, color=MUTE)
    frames = []
    for i in range(m.FRAMES):
        ax.view_init(elev=18, azim=i * 360 / m.FRAMES)
        fig.canvas.draw()
        im = Image.frombuffer('RGBA', fig.canvas.get_width_height(), fig.canvas.buffer_rgba()).convert('RGB')
        frames.append(im.convert('P', palette=Image.ADAPTIVE, colors=128))
    out = tmp / 'rag-map.gif'
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=110, loop=0, optimize=True)
    frames[0].convert('RGB').save(tmp / 'rag-map-frame0.png')
    place('ai', 'simple-rag-01-court-rulings', '07-b-chart', out)


if __name__ == '__main__':
    tmp = Path(os.environ.get('TMPDIR', '/tmp')) / 'naver-en-custom'
    tmp.mkdir(parents=True, exist_ok=True)
    set_lang('en')
    graph_sandwich(tmp)
    rag_map(tmp)
