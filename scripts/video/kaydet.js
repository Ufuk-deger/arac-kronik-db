// Kullanım: node scripts/video/kaydet.js ozellik.json cikti.mp4
// Şablonu açar, her kare için ciz(t) çağırıp ekran görüntüsünü ffmpeg'e akıtır (30 kare/sn, H.264, yuv420p).
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'); const path = require('path');
(async () => {
  const [ozellikYolu, cikti] = process.argv.slice(2);
  const V = JSON.parse(fs.readFileSync(ozellikYolu, 'utf8'));
  const FPS = 30, kare = Math.round(V.zaman.toplam * FPS);
  const tarayici = await chromium.launch();
  const sayfa = await tarayici.newPage({ viewport: { width: 1080, height: 1920 } });
  await sayfa.addInitScript((v) => { window.VIDEO = v; }, V);
  await sayfa.goto('file://' + path.join(__dirname, 'sablon.html'));
  await sayfa.evaluate(() => document.fonts.ready);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '20', '-movflags', '+faststart', cikti]);
  for (let i = 0; i < kare; i++) {
    await sayfa.evaluate((t) => window.ciz(t), i / FPS);
    const g = await sayfa.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(g)) await new Promise((r) => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await new Promise((r, h) => ff.on('close', (c) => (c === 0 ? r() : h(new Error('ffmpeg ' + c)))));
  await tarayici.close();
})();
