import fs from 'fs-extra';
import path from 'path';
import { fileURLToPath } from 'url';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import matter from 'gray-matter';
import { glob } from 'glob';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const POSTS_DIR = path.join(__dirname, '../_posts');
const OUTPUT_DIR = path.join(__dirname, '../assets/og');
const FONT_PATH = path.join(__dirname, '../assets/fonts/Pretendard-Bold.ttf');

fs.ensureDirSync(OUTPUT_DIR);

async function generateOG() {
  if (!fs.existsSync(FONT_PATH)) {
    console.log('Downloading font...');
    fs.ensureDirSync(path.dirname(FONT_PATH));
    const fontUrl = 'https://github.com/orioncactus/pretendard/raw/refs/heads/main/packages/pretendard/dist/public/static/alternative/Pretendard-Bold.ttf';
    const response = await fetch(fontUrl);
    const buffer = await response.arrayBuffer();
    fs.writeFileSync(FONT_PATH, Buffer.from(buffer));
  }
  const fontData = fs.readFileSync(FONT_PATH);

  const posts = await glob(path.join(POSTS_DIR, '**/*.md'));
  console.log(`Found ${posts.length} posts. Generating OG images...`);

  for (const postPath of posts) {
    const fileContent = fs.readFileSync(postPath, 'utf-8');
    const { data } = matter(fileContent);
    const slug = path.basename(postPath, '.md');
    const outputPath = path.join(OUTPUT_DIR, `${slug}.png`);

    const title = data.title || 'No1Joon Tech Blog';
    const category = data.category || 'Development';
    const subcategory = data.subcategory || '';
    const imagePath = `/assets/og/${slug}.png`;

    // 2.5 Update front matter surgically to preserve formatting
    if (data.image !== imagePath) {
      const lines = fileContent.split('\n');
      let secondDashedLineIndex = -1;
      let count = 0;
      for (let i = 0; i < lines.length; i++) {
        if (lines[i].trim() === '---') {
          count++;
          if (count === 2) {
            secondDashedLineIndex = i;
            break;
          }
        }
      }

      if (secondDashedLineIndex !== -1) {
        // Remove existing image line if any
        const filteredLines = lines.filter((line, idx) => {
          return idx >= secondDashedLineIndex || !line.startsWith('image:');
        });
        
        // Find new second dashed line index after filtering
        let newSecondIndex = filteredLines.findIndex((line, idx) => idx > 0 && line.trim() === '---');
        
        // Insert image: path before the second ---
        filteredLines.splice(newSecondIndex, 0, `image: ${imagePath}`);
        fs.writeFileSync(postPath, filteredLines.join('\n'));
        console.log(`Updated front matter for: ${slug}`);
      }
    }

    // 3. Generate SVG using Satori
    const svg = await satori(
      {
        type: 'div',
        props: {
          style: {
            display: 'flex',
            height: '100%',
            width: '100%',
            alignItems: 'center',
            justifyContent: 'center',
            flexDirection: 'column',
            backgroundImage: 'linear-gradient(to bottom right, #1a1a1a, #2d3436)',
            fontSize: 60,
            letterSpacing: '-0.02em',
            fontWeight: 700,
            color: 'white',
            padding: '80px',
            position: 'relative',
          },
          children: [
            {
              type: 'div',
              props: {
                style: { position: 'absolute', top: 40, left: 40, fontSize: 24, color: '#00d2ff', fontWeight: 500 },
                children: 'No1Joon.github.io',
              },
            },
            {
              type: 'div',
              props: {
                style: { display: 'flex', backgroundColor: '#00d2ff', color: '#1a1a1a', padding: '8px 20px', borderRadius: '50px', fontSize: 24, marginBottom: 30, fontWeight: 800 },
                children: `${category}${subcategory ? ` > ${subcategory}` : ''}`,
              },
            },
            {
              type: 'div',
              props: { style: { textAlign: 'center', lineHeight: 1.2, wordBreak: 'keep-all' }, children: title },
            },
            {
              type: 'div',
              props: {
                style: { position: 'absolute', bottom: 40, display: 'flex', alignItems: 'center', fontSize: 20, color: '#a0a0a0' },
                children: [
                  { type: 'div', props: { style: { marginRight: 10, width: 12, height: 12, borderRadius: '50%', backgroundColor: '#00d2ff' } } },
                  'Technical Record & Deep Dive'
                ],
              },
            },
          ],
        },
      },
      {
        width: 1200,
        height: 630,
        fonts: [{ name: 'Pretendard', data: fontData, weight: 700, style: 'normal' }],
      }
    );

    const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } });
    const pngData = resvg.render();
    fs.writeFileSync(outputPath, pngData.asPng());
    console.log(`Generated: ${slug}.png`);
  }
}

generateOG().catch(console.error);
