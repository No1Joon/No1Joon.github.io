// 브랜드 자산 생성 — favicon(png·ico·apple-touch) + 기본 OG 이미지
// 색은 assets/css/style.css 의 :root 토큰과 맞춘다.
import fs from 'fs-extra';
import path from 'path';
import { fileURLToPath } from 'url';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, '..');
const ASSETS = path.join(ROOT, 'assets');
const FONT_PATH = path.join(ASSETS, 'fonts/Pretendard-Bold.ttf');

const BG = '#0b0b0d';
const TEXT = '#fafafa';
const MUTED = '#a1a1aa';
const PRIMARY = '#f5b78f';

const SITE_NAME = 'No1Joon';
const SITE_SUFFIX = '.dev';
const SITE_DESC = '기술 스택, 아키텍처, 개발 경험을 기록하는 블로그';

async function loadFont() {
  if (!fs.existsSync(FONT_PATH)) {
    fs.ensureDirSync(path.dirname(FONT_PATH));
    const url =
      'https://github.com/orioncactus/pretendard/raw/refs/heads/main/packages/pretendard/dist/public/static/alternative/Pretendard-Bold.ttf';
    const res = await fetch(url);
    fs.writeFileSync(FONT_PATH, Buffer.from(await res.arrayBuffer()));
  }
  return fs.readFileSync(FONT_PATH);
}

const render = (svg, width) =>
  new Resvg(svg, { fitTo: { mode: 'width', value: width } }).render().asPng();

// 어두운 탭 바에서 묻히지 않도록 primary 를 바탕, 글자를 어둡게 둔다
function markSvg(fontData) {
  return satori(
    {
      type: 'div',
      props: {
        style: {
          display: 'flex',
          width: '100%',
          height: '100%',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: PRIMARY,
          color: BG,
          // 16px 로 줄었을 때도 형태가 남도록 글자를 캔버스의 70% 가까이 채운다
          fontSize: 470,
          fontWeight: 700,
          letterSpacing: '-0.04em',
          // 광학 중심 보정 — J 는 아래로 뻗고 오른쪽에 치우쳐 보인다
          paddingBottom: 30,
          paddingRight: 12,
        },
        children: 'J',
      },
    },
    { width: 512, height: 512, fonts: [{ name: 'Pretendard', data: fontData, weight: 700, style: 'normal' }] }
  );
}

function ogSvg(fontData) {
  const row = (children, style) => ({ type: 'div', props: { style: { display: 'flex', ...style }, children } });
  return satori(
    {
      type: 'div',
      props: {
        style: {
          display: 'flex',
          flexDirection: 'column',
          width: '100%',
          height: '100%',
          justifyContent: 'center',
          backgroundColor: BG,
          padding: '0 90px',
          fontWeight: 700,
        },
        children: [
          row(
            [
              { type: 'div', props: { style: { color: TEXT }, children: SITE_NAME } },
              { type: 'div', props: { style: { color: PRIMARY }, children: SITE_SUFFIX } },
            ],
            { fontSize: 104, letterSpacing: '-0.03em' }
          ),
          row([{ type: 'div', props: { children: SITE_DESC } }], {
            marginTop: 28,
            fontSize: 40,
            color: MUTED,
            letterSpacing: '-0.02em',
          }),
          row(
            [{ type: 'div', props: { style: { width: 120, height: 8, backgroundColor: PRIMARY, borderRadius: 4 } } }],
            { marginTop: 56 }
          ),
        ],
      },
    },
    { width: 1200, height: 630, fonts: [{ name: 'Pretendard', data: fontData, weight: 700, style: 'normal' }] }
  );
}

// ICO 컨테이너 — 각 엔트리에 PNG 를 그대로 담는다 (Vista 이후 표준)
function buildIco(pngs) {
  const header = Buffer.alloc(6);
  header.writeUInt16LE(0, 0);
  header.writeUInt16LE(1, 2);
  header.writeUInt16LE(pngs.length, 4);

  const entries = [];
  let offset = 6 + pngs.length * 16;
  for (const { size, data } of pngs) {
    const e = Buffer.alloc(16);
    e.writeUInt8(size >= 256 ? 0 : size, 0);
    e.writeUInt8(size >= 256 ? 0 : size, 1);
    e.writeUInt8(0, 2);
    e.writeUInt8(0, 3);
    e.writeUInt16LE(1, 4);
    e.writeUInt16LE(32, 6);
    e.writeUInt32LE(data.length, 8);
    e.writeUInt32LE(offset, 12);
    entries.push(e);
    offset += data.length;
  }
  return Buffer.concat([header, ...entries, ...pngs.map((p) => p.data)]);
}

async function main() {
  const fontData = await loadFont();

  const mark = await markSvg(fontData);
  const sizes = [16, 32, 48, 180, 512];
  const rendered = Object.fromEntries(sizes.map((s) => [s, render(mark, s)]));

  fs.writeFileSync(path.join(ASSETS, 'favicon.png'), rendered[512]);
  fs.writeFileSync(path.join(ASSETS, 'apple-touch-icon.png'), rendered[180]);
  fs.writeFileSync(
    path.join(ROOT, 'favicon.ico'),
    buildIco([16, 32, 48].map((size) => ({ size, data: rendered[size] })))
  );

  fs.writeFileSync(path.join(ASSETS, 'og-default.png'), render(await ogSvg(fontData), 1200));

  console.log('생성 완료: assets/favicon.png · assets/apple-touch-icon.png · favicon.ico · assets/og-default.png');
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
