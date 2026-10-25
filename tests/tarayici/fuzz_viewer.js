// Görüntüleyici rastgele filtre kombinasyonu testi (isteğe bağlı; Node.js ve Playwright gerekir). Arayüz sonucu,
// gömülü veriden bağımsız hesaplanan beklentiyle satır satır karşılaştırılır.
// Kullanım: python3 scripts/viewer_uret.py && node tests/tarayici/fuzz_viewer.js $PWD/viewer/index.html 40 12345
const { chromium } = require('playwright');

const DOSYA = process.argv[2];
const ADET = Number(process.argv[3] || 120);
let tohum = Number(process.argv[4] || 12345);
function rnd() { tohum |= 0; tohum = (tohum + 0x6d2b79f5) | 0; let t = Math.imul(tohum ^ (tohum >>> 15), 1 | tohum); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }
const sec = (dizi) => dizi[Math.floor(rnd() * dizi.length)];

const katla = (s) => s.toLocaleLowerCase('tr-TR').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ı/g, 'i');
const KISA_KOD = /^(?=.*\d)[a-z0-9-]{1,3}$/;
const HARF_RAKAM = /^[a-z]\d$/;
function eslesir(metin, terim) {
  if (!KISA_KOD.test(terim)) return metin.includes(terim);
  const sonrasi = HARF_RAKAM.test(terim);
  for (let i = metin.indexOf(terim); i !== -1; i = metin.indexOf(terim, i + 1)) {
    if (i !== 0 && /[a-z0-9]/.test(metin[i - 1])) continue;
    if (sonrasi && /\d/.test(metin[i + terim.length] || '')) continue;
    return true;
  }
  return false;
}
const modelAdi = (m) => m.replace(/\s*\(\d{4}-(?:\d{4})?\)/, '').replace(/,\s*\d{4}-(?:\d{4})?\)/, ')');
const IKI = new Set(['co.uk', 'org.uk', 'com.au', 'co.nz', 'com.tr', 'org.tr']);
function alanAdi(url) {
  let host = '';
  try { host = new URL(url).hostname.toLowerCase(); } catch (e) { return ''; }
  const p = host.split('.');
  if (p.length >= 3 && IKI.has(p.slice(-2).join('.'))) return p.slice(-3).join('.');
  return p.slice(-2).join('.');
}
const RISK = { 'Yüksek': 'yuksek', 'Orta': 'orta', 'Düşük': 'dusuk' };

(async () => {
  const browser = await chromium.launch();
  const p = await (await browser.newContext({ viewport: { width: 1280, height: 900 } })).newPage();
  const konsol = [];
  p.on('pageerror', (e) => konsol.push(String(e)));
  await p.goto('file://' + DOSYA);
  await p.waitForSelector('.arac');
  const { veri, kaynak, plan } = await p.evaluate(() => ({
    veri: JSON.parse(document.getElementById('veri').textContent),
    kaynak: JSON.parse(document.getElementById('kaynak-veri').textContent).siteler,
    plan: JSON.parse(document.getElementById('plan-veri').textContent),
  }));
  const aile = new Map(veri.aileler.map((f) => [f.id, f]));
  const kayitlar = veri.arac_listesi.map((a) => {
    const aileler = (a.aileler || []).map((id) => aile.get(id)).filter(Boolean);
    const kendi = new Set(a.kronik_sorunlar.map((s) => s.aile_sorunu).filter(Boolean));
    const ham = a.kronik_sorunlar.map((s) => ({ s, f: null }));
    for (const f of aileler) for (const fs of f.kronik_sorunlar) if (!kendi.has(`${f.id}/${fs.id}`)) ham.push({ s: fs, f });
    const ad = modelAdi(a.model);
    const sorunlar = ham.map(({ s, f }) => {
      let bagli = f;
      if (!f && s.aile_sorunu) bagli = aile.get(s.aile_sorunu.split('/')[0]) || null;
      const adlar = s.kaynaklar.map((u) => (kaynak[alanAdi(u)] || {}).ad || alanAdi(u));
      const metin = katla([s.sorun_adi, s.etkilenen_parca, s.belirtiler, s.risk_seviyesi, ...Object.values(s.detay || {}), ...adlar, bagli ? bagli.ad : ''].join(' '));
      const m = s.tahmini_km_araligi && /^([\d.]+) - ([\d.]+) km$/.exec(s.tahmini_km_araligi);
      return { baslik: s.sorun_adi, risk: RISK[s.risk_seviyesi], metin, km: m ? [Number(m[1].replace(/\./g, '')), Number(m[2].replace(/\./g, ''))] : null };
    });
    return { a, ad, sorunlar, marka: a.marka, modelKey: `${a.marka}|${ad}`, yb: a.uretim_yillari.baslangic, ye: a.uretim_yillari.bitis,
      elektrik: a.motor.startsWith('Elektrik'), adMetni: katla(`${a.marka} ${ad}`), kimlik: katla(`${a.marka} ${ad} ${a.motor}`),
      motorEt: a.motor.startsWith('Tüm motorlar') ? 'Tüm motorlar' : a.motor };
  });
  const adSozlugu = [...new Set(kayitlar.map((k) => k.adMetni).concat(plan.map((o) => katla(`${o.marka} ${o.model}`))))];
  const aracTerimi = (t) => adSozlugu.some((m) => eslesir(m, t));

  function beklenen(d) {
    let yil = d.yil; const terimler = [];
    for (const t of katla(d.ara).split(/\s+/).filter(Boolean)) {
      if (/^(19|20)\d{2}$/.test(t) && Number(t) >= 1990 && Number(t) <= 2100) { if (yil == null) yil = Number(t); continue; }
      terimler.push({ t, arac: aracTerimi(t) });
    }
    const aracVar = terimler.some((x) => x.arac);
    const satirlar = []; const riskSay = { '': 0, yuksek: 0, orta: 0, dusuk: 0 };
    let kartSay = 0;
    for (const k of kayitlar) {
      if (yil != null && !(yil >= k.yb && (k.ye == null || yil <= k.ye))) continue;
      if (d.elektrik && !k.elektrik) continue;
      if (aracVar && !terimler.every((x) => !x.arac || eslesir(k.adMetni, x.t))) continue;
      if (d.marka && k.marka !== d.marka) continue;
      if (d.model && k.modelKey !== d.model) continue;
      const adaylar = k.sorunlar.filter((s) => {
        if (!terimler.every((x) => x.arac || eslesir(k.kimlik, x.t) || eslesir(s.metin, x.t))) return false;
        if (d.kmFiltre && d.km != null && s.km) {
          const icinde = d.km >= s.km[0] && d.km <= s.km[1];
          const yakin = d.km < s.km[0] && s.km[0] - d.km <= 20000;
          if (!icinde && !yakin) return false;
        }
        return true;
      });
      for (const s of adaylar) { riskSay[''] += 1; riskSay[s.risk] += 1; }
      const secili = d.risk ? adaylar.filter((s) => s.risk === d.risk) : adaylar;
      if (!secili.length) continue;
      kartSay += 1;
      for (const s of secili) satirlar.push(`${k.marka}|${k.ad}|${k.motorEt}|${s.baslik}`);
    }
    return { satirlar: satirlar.sort(), kartSay, riskSay };
  }

  async function uygula(d) {
    await p.evaluate(() => { const b = document.getElementById('temizle'); if (!b.hidden) b.click(); });
    await p.waitForTimeout(30);
    await p.selectOption('#marka', d.marka || '');
    await p.waitForTimeout(20);
    if (d.marka) await p.selectOption('#model', d.model || '');
    await p.fill('#yil', d.yil ? String(d.yil) : '');
    await p.fill('#km', d.km != null ? String(d.km) : '');
    if (d.kmFiltre) await p.check('#kmfiltre'); else await p.uncheck('#kmfiltre');
    if (d.elektrik) await p.check('#elektrikli'); else await p.uncheck('#elektrikli');
    await p.click(`label${d.risk ? `[data-risk="${d.risk}"]` : ':has(#risk-tumu)'} span`);
    await p.fill('#ara', d.ara);
    await p.waitForTimeout(380);
    for (let i = 0; i < 80; i++) {
      const gor = await p.evaluate(() => !document.getElementById('daha').hidden);
      if (!gor) break;
      await p.click('#daha-btn');
    }
    return p.evaluate(() => {
      const satirlar = []; let marka = ''; let kart = 0;
      for (const e of document.getElementById('liste').children) {
        if (e.matches('h2.marka-baslik')) { marka = e.firstChild.textContent; continue; }
        if (!e.matches('article.arac')) continue;
        kart++;
        const ad = e.querySelector('h3').textContent; const motor = e.querySelector('.motor').textContent;
        for (const h of e.querySelectorAll('li.sorun h4')) satirlar.push(`${marka}|${ad}|${motor}|${h.textContent}`);
      }
      const cip = {}; for (const s of document.querySelectorAll('[data-say]')) cip[s.dataset.say] = Number(s.textContent);
      return { satirlar: satirlar.sort(), kart, cip, sonuc: document.getElementById('sonuc').textContent.trim() };
    });
  }

  const modelKelimeleri = [...new Set(kayitlar.flatMap((k) => k.ad.split(/[\s()/,]+/).filter((w) => w.length >= 2)))];
  const teknik = ['dsg', 'k9k', 'triger', 'dpf', 'adblue', 'zincir', 'turbo', 'edc', 'cvt', 'egr', 'volan', 'enjektör', 'sanziman', 'tsi', 'tdi', 'dci', '1.6', '1.5', '2.0', 'cam tavan', 'multijet', 'puretech', 'ecoboost', 'b47', 'n47'];
  const markalar = [...new Set(kayitlar.map((k) => k.marka))];
  const modelAnahtarlari = new Map(); for (const k of kayitlar) { if (!modelAnahtarlari.has(k.marka)) modelAnahtarlari.set(k.marka, new Set()); modelAnahtarlari.get(k.marka).add(k.modelKey); }

  let hata = 0; let dolu = 0;
  for (let i = 0; i < ADET; i++) {
    const d = { ara: '', marka: '', model: '', yil: null, km: null, risk: '', kmFiltre: false, elektrik: false };
    const r = rnd();
    if (r < 0.35) d.ara = sec(modelKelimeleri);
    else if (r < 0.6) d.ara = sec(teknik);
    else if (r < 0.75) d.ara = `${sec(modelKelimeleri)} ${sec(teknik)}`;
    else if (r < 0.82) d.ara = `${sec(modelKelimeleri)} ${2008 + Math.floor(rnd() * 17)}`;
    if (rnd() < 0.3) { d.marka = sec(markalar); if (rnd() < 0.5) d.model = sec([...modelAnahtarlari.get(d.marka)]); }
    if (rnd() < 0.25) d.yil = 2008 + Math.floor(rnd() * 17);
    if (rnd() < 0.3) { d.km = 5000 * (1 + Math.floor(rnd() * 50)); d.kmFiltre = rnd() < 0.5; }
    if (rnd() < 0.25) d.risk = sec(['yuksek', 'orta', 'dusuk']);
    if (rnd() < 0.08) d.elektrik = true;
    const gor = await uygula(d);
    const bek = beklenen(d);
    if (gor.satirlar.length) dolu++;
    const ayni = JSON.stringify(gor.satirlar) === JSON.stringify(bek.satirlar) && gor.kart === bek.kartSay;
    const cipAyni = ['', 'yuksek', 'orta', 'dusuk'].every((k) => gor.cip[k] === bek.riskSay[k]);
    if (!ayni || !cipAyni) {
      hata++;
      const g = new Set(gor.satirlar); const b = new Set(bek.satirlar);
      console.log(`HATA #${i}`, JSON.stringify(d), `görünen satır=${gor.satirlar.length} kart=${gor.kart} | beklenen satır=${bek.satirlar.length} kart=${bek.kartSay}`, cipAyni ? '' : `çip=${JSON.stringify(gor.cip)} beklenen=${JSON.stringify(bek.riskSay)}`);
      console.log('   fazla:', [...g].filter((x) => !b.has(x)).slice(0, 3), ' eksik:', [...b].filter((x) => !g.has(x)).slice(0, 3));
    } else if (i % 20 === 0) {
      console.log(`#${i} tamam`, JSON.stringify(d), `satır=${gor.satirlar.length}`);
    }
  }
  console.log(`\n${ADET - hata}/${ADET} rastgele durum beklenenle birebir aynı (${dolu} tanesi boş olmayan sonuç); sayfa hataları: ${konsol.length ? konsol.join(' | ') : 'yok'}`);
  await browser.close();
  process.exit(hata || konsol.length ? 1 : 0);
})();
