// Görüntüleyici tarayıcı testi (isteğe bağlı; Node.js ve Playwright gerekir). Arayüzü gerçek tarayıcıda sürer ve
// sonuçları gömülü veriden bağımsız hesaplanan beklentiyle karşılaştırır.
// Kullanım: python3 scripts/viewer_uret.py && node tests/tarayici/test_viewer.js $PWD/viewer/index.html
const { chromium } = require('playwright');

const DOSYA = process.argv[2];
const sonuclar = [];
function kontrol(ad, kosul, ayrinti) {
  sonuclar.push({ ad, ok: Boolean(kosul), ayrinti: kosul ? '' : (ayrinti || '') });
  if (!kosul) console.log('  BAŞARISIZ:', ad, '|', ayrinti || '');
}

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

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const p = await ctx.newPage();
  const konsol = [];
  p.on('console', (m) => { if (m.type() === 'error') konsol.push(m.text()); });
  p.on('pageerror', (e) => konsol.push(String(e)));
  await p.goto('file://' + DOSYA);
  await p.waitForSelector('.arac');

  const veri = await p.evaluate(() => ({
    veri: JSON.parse(document.getElementById('veri').textContent),
    plan: JSON.parse(document.getElementById('plan-veri').textContent),
  }));
  const aileHaritasi = new Map((veri.veri.aileler || []).map((f) => [f.id, f]));
  const kayitlar = veri.veri.arac_listesi.map((a) => {
    const aileler = (a.aileler || []).map((id) => aileHaritasi.get(id)).filter(Boolean);
    const kendi = new Set(a.kronik_sorunlar.map((s) => s.aile_sorunu).filter(Boolean));
    const sorunlar = a.kronik_sorunlar.map((s) => ({ s, aile: null }));
    for (const f of aileler) for (const fs of f.kronik_sorunlar) if (!kendi.has(`${f.id}/${fs.id}`)) sorunlar.push({ s: fs, aile: f });
    const ad = modelAdi(a.model);
    return { a, ad, sorunlar, adMetni: katla(`${a.marka} ${ad}`), kimlik: katla(`${a.marka} ${ad} ${a.motor}`) };
  });
  const adSozlugu = [...new Set(kayitlar.map((k) => k.adMetni).concat(veri.plan.map((o) => katla(`${o.marka} ${o.model}`))))];
  const aracTerimi = (t) => adSozlugu.some((m) => eslesir(m, t));
  const toplamSatir = kayitlar.reduce((t, k) => t + k.sorunlar.length, 0);

  // ---------- yardımcılar ----------
  const bekle = (ms) => p.waitForTimeout(ms);
  async function sifirla() {
    await p.evaluate(() => {
      const b = document.getElementById('temizle');
      if (!b.hidden) b.click();
    });
    await bekle(60);
  }
  async function yaz(sel, deger) { await p.fill(sel, deger); await bekle(330); }
  async function hepsiniYukle() {
    for (let i = 0; i < 60; i++) {
      const gorunur = await p.evaluate(() => !document.getElementById('daha').hidden);
      if (!gorunur) break;
      await p.click('#daha-btn');
    }
  }
  async function oku() {
    return p.evaluate(() => {
      const cikti = { kartlar: [], sonuc: document.getElementById('sonuc').textContent.trim(), cipler: {} };
      let marka = '';
      for (const e of document.getElementById('liste').children) {
        if (e.matches('h2.marka-baslik')) { marka = e.firstChild.textContent; continue; }
        if (!e.matches('article.arac')) continue;
        const satirlar = [...e.querySelectorAll('li.sorun')].map((li) => ({
          baslik: li.querySelector('h4').textContent,
          risk: li.dataset.risk,
          km: li.querySelector('.km-etiket').textContent,
          durum: (li.querySelector('.durum') || {}).textContent || '',
          acik: li.querySelector('details').open,
        }));
        cikti.kartlar.push({ marka, ad: e.querySelector('h3').textContent, motor: e.querySelector('.motor').textContent,
          yil: e.querySelector('.arac-yil').textContent, tur: e.dataset.tur || 'motor', satirlar });
      }
      for (const s of document.querySelectorAll('[data-say]')) cikti.cipler[s.dataset.say] = Number(s.textContent);
      return cikti;
    });
  }
  const satirSay = (o) => o.kartlar.reduce((t, k) => t + k.satirlar.length, 0);

  // ---------- 1. İlk yükleme ----------
  console.log('1. İlk yükleme');
  {
    const dom = await p.evaluate(() => document.getElementsByTagName('*').length);
    kontrol('ilk DOM boyutu küçük (< 12.000 düğüm)', dom < 12000, `dom=${dom}`);
    const o = await oku();
    kontrol('ilk sayfada en çok 24 kart', o.kartlar.length > 0 && o.kartlar.length <= 24, `kart=${o.kartlar.length}`);
    kontrol('sonuç satırı tüm kayıtları söylüyor', o.sonuc.startsWith(`${kayitlar.length} kayıt · ${toplamSatir} sorun satırı`), o.sonuc);
    await hepsiniYukle();
    const t = await oku();
    kontrol('sayfalama sonunda tüm kartlar yüklenir', t.kartlar.length === kayitlar.length, `kart=${t.kartlar.length}`);
    kontrol('sayfalama sonunda tüm satırlar yüklenir', satirSay(t) === toplamSatir, `satir=${satirSay(t)} beklenen=${toplamSatir}`);
    kontrol('satırlar kapalı gelir', t.kartlar.every((k) => k.satirlar.every((s) => !s.acik)));
    kontrol('risk çipi sayıları toplamı tüm satırlar', t.cipler[''] === toplamSatir && t.cipler.yuksek + t.cipler.orta + t.cipler.dusuk === toplamSatir, JSON.stringify(t.cipler));
    const ozet = await p.textContent('#ozet');
    const ozgSay = veri.veri.arac_listesi.reduce((t, a) => t + a.kronik_sorunlar.length, 0);
    const ortSay = (veri.veri.aileler || []).reduce((t, f) => t + f.kronik_sorunlar.length, 0);
    kontrol('özet benzersiz sayıları gösterir', ozet.includes(`${ozgSay + ortSay} sorun (${ozgSay} kayda özgü + ${ortSay} ortak aile)`), ozet);
  }

  // ---------- 2. Araç adı araması: yalnızca araç kimliği ----------
  console.log('2. Araç adı araması');
  const modelSorgulari = ['egea', 'golf', 'passat', 'megane', 'clio', 'corolla', 'qashqai', 'duster', 'astra', 'focus', 'fiesta', 'polo', 'a3', 'x5', 'tucson', 'sportage', 'civic', 'doblo', 'octavia', 'leon', '308', 'c3', 'yaris', 'juke', 'kuga', 'tiguan', 'insignia', 'corsa', 'i20', 'ceed', 'fiat', 'ford', 'bmw', 'volkswagen egea', 'golf 1.4', 'renault clio dci'];
  for (const q of modelSorgulari) {
    await sifirla();
    await yaz('#ara', q);
    await hepsiniYukle();
    const o = await oku();
    const terimler = katla(q).split(/\s+/).filter(Boolean);
    const aracT = terimler.filter(aracTerimi);
    const genelT = terimler.filter((t) => !aracTerimi(t));
    const beklenen = kayitlar.filter((k) => aracT.every((t) => eslesir(k.adMetni, t)) &&
      k.sorunlar.some(({ s, aile }) => {
        const metin = katla([s.sorun_adi, s.etkilenen_parca, s.belirtiler, s.risk_seviyesi, ...Object.values(s.detay || {}), aile ? aile.ad : ''].join(' '));
        return genelT.every((t) => eslesir(k.kimlik, t) || eslesir(metin, t));
      }));
    const gorunenAdlar = o.kartlar.map((k) => `${k.marka}|${k.ad}|${k.motor}`).sort();
    const beklenenAdlar = beklenen.map((k) => `${k.a.marka}|${k.ad}|${k.a.motor.startsWith('Tüm motorlar') ? 'Tüm motorlar' : k.a.motor}`).sort();
    kontrol(`"${q}": sonuçlar beklenen kayıt kümesiyle aynı (${beklenen.length})`, JSON.stringify(gorunenAdlar) === JSON.stringify(beklenenAdlar),
      `görünen=${gorunenAdlar.length} beklenen=${beklenenAdlar.length}`);
    if (aracT.length) {
      const yabanci = o.kartlar.filter((k) => !aracT.every((t) => eslesir(katla(`${k.marka} ${k.ad}`), t)));
      kontrol(`"${q}": başka araç görünmez`, yabanci.length === 0, yabanci.slice(0, 3).map((k) => k.marka + ' ' + k.ad).join(' ## '));
    }
  }

  // ---------- 3. Motor / parça / belirti araması ----------
  console.log('3. Motor, parça ve belirti araması');
  for (const q of ['dsg', 'k9k', 'triger', 'dpf', 'adblue', 'cam tavan', 'zincir', 'turbo', 'dq200', '7dct', 'adblue sensör', 'egr valfi', 'şanzıman', 'sanziman', 'volan', 'direksiyon']) {
    await sifirla();
    await yaz('#ara', q);
    await hepsiniYukle();
    const o = await oku();
    const terimler = katla(q).split(/\s+/).filter(Boolean);
    let beklenenSatir = 0; let beklenenKart = 0;
    for (const k of kayitlar) {
      let n = 0;
      for (const { s, aile } of k.sorunlar) {
        const metin = katla([s.sorun_adi, s.etkilenen_parca, s.belirtiler, s.risk_seviyesi, ...Object.values(s.detay || {}), aile ? aile.ad : ''].join(' '));
        const kaynakAdlari = katla(s.kaynaklar.map((u) => u).join(' '));
        void kaynakAdlari;
        if (terimler.every((t) => eslesir(k.kimlik, t) || eslesir(metin, t))) n++;
      }
      if (n) { beklenenSatir += n; beklenenKart++; }
    }
    // Kaynak site adları da arama metnine dahil olduğundan sayfa beklenenden fazla olabilir; eksik olmamalı.
    kontrol(`"${q}": beklenen tüm kayıtlar var (≥ ${beklenenKart})`, o.kartlar.length >= beklenenKart, `kart=${o.kartlar.length} beklenen>=${beklenenKart}`);
    kontrol(`"${q}": satır sayısı beklenenden az değil (≥ ${beklenenSatir})`, satirSay(o) >= beklenenSatir, `satir=${satirSay(o)} beklenen>=${beklenenSatir}`);
    kontrol(`"${q}": sonuç var`, o.kartlar.length > 0, 'boş');
  }

  // ---------- 4. Metninde geçen kayıtlar bölümü ----------
  console.log('4. Metninde geçen kayıtlar');
  {
    await sifirla();
    await yaz('#ara', 'tucson');
    const gorunur = await p.evaluate(() => !document.getElementById('ikincil').hidden);
    const say = await p.textContent('#ikincil-say');
    kontrol('"tucson": ikincil bölüm görünür ve sayı gösterir', gorunur && /^\d+ kayıt$/.test(say.trim()), say);
    const kapali = await p.evaluate(() => ({ acik: document.getElementById('ikincil').open, ic: document.querySelectorAll('#ikincil-liste .arac').length }));
    kontrol('"tucson": ikincil bölüm kapalı ve içi boş gelir', !kapali.acik && kapali.ic === 0, JSON.stringify(kapali));
    await p.click('#ikincil > summary');
    await bekle(100);
    const ic = await p.evaluate(() => [...document.querySelectorAll('#ikincil-liste .arac')].map((e) => e.querySelector('h3').textContent));
    kontrol('"tucson": bölüm açılınca kartlar yüklenir', ic.length > 0, `kart=${ic.length}`);
    kontrol('"tucson": ikincil kartlar Tucson değil', ic.every((a) => !/tucson/i.test(a)), ic.slice(0, 5).join(' | '));
    const beklenenIkincil = kayitlar.filter((k) => !eslesir(k.adMetni, 'tucson') && k.sorunlar.some(({ s, aile }) => {
      const metin = katla([s.sorun_adi, s.etkilenen_parca, s.belirtiler, s.risk_seviyesi, ...Object.values(s.detay || {}), aile ? aile.ad : ''].join(' '));
      return eslesir(k.kimlik, 'tucson') || eslesir(metin, 'tucson');
    })).length;
    kontrol('"tucson": ikincil sayı beklenenden az değil', Number(say.trim().split(' ')[0]) >= beklenenIkincil, `${say} beklenen>=${beklenenIkincil}`);
    // olmayan araç adı: birincil boş, ikincil ya da boş durum
    await sifirla();
    await yaz('#ara', 'zzzzqq');
    const bosGorunur = await p.evaluate(() => !document.getElementById('bos').hidden);
    kontrol('olmayan terim boş durumu gösterir', bosGorunur);
  }

  // ---------- 5. Model yılı ----------
  console.log('5. Model yılı');
  for (const yil of [2012, 2015, 2018, 2021, 2024]) {
    await sifirla();
    await yaz('#yil', String(yil));
    await hepsiniYukle();
    const o = await oku();
    const beklenen = kayitlar.filter((k) => yil >= k.a.uretim_yillari.baslangic && (k.a.uretim_yillari.bitis == null || yil <= k.a.uretim_yillari.bitis) && k.sorunlar.length);
    kontrol(`yıl ${yil}: kart sayısı beklenenle aynı (${beklenen.length})`, o.kartlar.length === beklenen.length, `kart=${o.kartlar.length}`);
    const disinda = o.kartlar.filter((k) => {
      const m = /Üretim (\d{4})(?:–(\d{4}|günümüz))?/.exec(k.yil);
      const b = Number(m[1]); const e = m[2] && m[2] !== 'günümüz' ? Number(m[2]) : (m[2] === 'günümüz' ? null : b);
      return !(yil >= b && (e == null || yil <= e));
    });
    kontrol(`yıl ${yil}: kapsam dışı kart yok`, disinda.length === 0, disinda.slice(0, 3).map((k) => k.ad).join(' | '));
  }
  {
    await sifirla();
    await yaz('#ara', 'egea 2018');
    const o = await oku();
    const chip = await p.evaluate(() => [...document.querySelectorAll('#aktif .aktif-cip')].map((b) => b.textContent));
    const beklenen = kayitlar.filter((k) => eslesir(k.adMetni, 'egea') && 2018 >= k.a.uretim_yillari.baslangic && (k.a.uretim_yillari.bitis == null || 2018 <= k.a.uretim_yillari.bitis)).length;
    kontrol('"egea 2018": yıl aramadan okunur', chip.some((c) => c.startsWith('2018 modeli')) && o.kartlar.length === beklenen, JSON.stringify(chip) + ` kart=${o.kartlar.length} beklenen=${beklenen}`);
    // chip kaldırınca yıl temizlenir ama arama kalır
    await p.click('#aktif .aktif-cip:nth-child(2)').catch(() => {});
    await bekle(330);
    const arama = await p.inputValue('#ara');
    kontrol('yıl çipi kaldırılınca arama metninden de çıkar', !/2018/.test(arama), arama);
  }

  // ---------- 6. Risk ----------
  console.log('6. Risk');
  for (const r of ['yuksek', 'orta', 'dusuk']) {
    await sifirla();
    const beklenenSatir = kayitlar.reduce((t, k) => t + k.sorunlar.filter(({ s }) => ({ 'Yüksek': 'yuksek', 'Orta': 'orta', 'Düşük': 'dusuk' }[s.risk_seviyesi]) === r).length, 0);
    const cip = await p.evaluate((r) => Number(document.querySelector(`[data-say="${r}"]`).textContent), r);
    kontrol(`risk ${r}: çip sayısı veriyle aynı`, cip === beklenenSatir, `çip=${cip} beklenen=${beklenenSatir}`);
    await p.click(`label[data-risk="${r}"] span`);
    await bekle(60);
    await hepsiniYukle();
    const o = await oku();
    kontrol(`risk ${r}: görünen satır sayısı çipe eşit`, satirSay(o) === beklenenSatir, `satir=${satirSay(o)} beklenen=${beklenenSatir}`);
    kontrol(`risk ${r}: yalnızca bu riskte satır var`, o.kartlar.every((k) => k.satirlar.every((s) => s.risk === r)));
  }
  await sifirla();

  // ---------- 7. Marka ve model ----------
  console.log('7. Marka ve model');
  {
    const markalar = [...new Set(kayitlar.map((k) => k.a.marka))];
    for (const marka of ['Fiat', 'Volkswagen', 'BMW', 'Toyota', 'Renault']) {
      await sifirla();
      await p.selectOption('#marka', marka);
      await bekle(60);
      await hepsiniYukle();
      const o = await oku();
      const beklenen = kayitlar.filter((k) => k.a.marka === marka && k.sorunlar.length).length;
      kontrol(`marka ${marka}: kart sayısı (${beklenen})`, o.kartlar.length === beklenen && o.kartlar.every((k) => k.marka === marka), `kart=${o.kartlar.length}`);
      const seceneklerToplam = await p.evaluate(() => {
        const m = document.getElementById('model');
        return { devre: m.disabled, say: [...m.options].filter((o) => o.value).reduce((t, o) => t + Number(/\((\d+)\)$/.exec(o.textContent)[1]), 0), adet: [...m.options].filter((o) => o.value).length };
      });
      kontrol(`marka ${marka}: model seçeneği etkin ve sayıları toplamı kart sayısı`, !seceneklerToplam.devre && seceneklerToplam.say === beklenen, JSON.stringify(seceneklerToplam));
      // bir model seç
      const modelDegeri = await p.evaluate(() => { const m = document.getElementById('model'); return m.options[Math.min(2, m.options.length - 1)].value; });
      await p.selectOption('#model', modelDegeri);
      await bekle(60);
      await hepsiniYukle();
      const o2 = await oku();
      const beklenen2 = kayitlar.filter((k) => `${k.a.marka}|${k.ad}` === modelDegeri && k.sorunlar.length).length;
      kontrol(`marka ${marka}, model ${modelDegeri.split('|')[1]}: kart sayısı (${beklenen2})`, o2.kartlar.length === beklenen2, `kart=${o2.kartlar.length}`);
      // markayı değiştirince model sıfırlanır
      await p.selectOption('#marka', '');
      await bekle(60);
      const modelDurum = await p.evaluate(() => ({ devre: document.getElementById('model').disabled, deger: document.getElementById('model').value }));
      kontrol(`marka ${marka}: markayı kaldırınca model sıfırlanır ve devre dışı kalır`, modelDurum.devre && modelDurum.deger === '', JSON.stringify(modelDurum));
    }
    void markalar;
    // marka sayıları: marka sayısı toplamı kart sayısı
    await sifirla();
    const toplam = await p.evaluate(() => [...document.getElementById('marka').options].filter((o) => o.value).reduce((t, o) => t + Number(/\((\d+)\)$/.exec(o.textContent)[1]), 0));
    kontrol('marka seçenekleri sayıları toplamı tüm kayıtlar', toplam === kayitlar.length, `toplam=${toplam}`);
    // marka + arama
    await p.selectOption('#marka', 'Fiat');
    await yaz('#ara', 'dpf');
    const o = await oku();
    kontrol('marka + arama: yalnızca Fiat ve içinde dpf geçen kartlar', o.kartlar.length > 0 && o.kartlar.every((k) => k.marka === 'Fiat'), `kart=${o.kartlar.length}`);
    // marka sayıları arama ile güncellenir
    const sayilar = await p.evaluate(() => [...document.getElementById('marka').options].filter((o) => o.value).map((o) => o.textContent));
    kontrol('marka sayıları aramaya göre güncellenir (bazı markalar 0)', sayilar.some((s) => /\(0\)$/.test(s)) && sayilar.some((s) => !/\(0\)$/.test(s)), sayilar.slice(0, 5).join(' | '));
  }
  await sifirla();

  // ---------- 8. Kilometre ----------
  console.log('8. Kilometre');
  {
    const km = 120000;
    await sifirla();
    await yaz('#km', String(km));
    await hepsiniYukle();
    const o = await oku();
    const icindeBeklenen = kayitlar.reduce((t, k) => t + k.sorunlar.filter(({ s }) => {
      const m = s.tahmini_km_araligi && /^([\d.]+) - ([\d.]+) km$/.exec(s.tahmini_km_araligi);
      if (!m) return false;
      const a = Number(m[1].replace(/\./g, '')); const b = Number(m[2].replace(/\./g, ''));
      return km >= a && km <= b;
    }).length, 0);
    const yakinBeklenen = kayitlar.reduce((t, k) => t + k.sorunlar.filter(({ s }) => {
      const m = s.tahmini_km_araligi && /^([\d.]+) - ([\d.]+) km$/.exec(s.tahmini_km_araligi);
      if (!m) return false;
      const a = Number(m[1].replace(/\./g, ''));
      return km < a && a - km <= 20000;
    }).length, 0);
    const icindeGor = o.kartlar.reduce((t, k) => t + k.satirlar.filter((s) => s.durum === 'Bu kilometrede').length, 0);
    const yakinGor = o.kartlar.reduce((t, k) => t + k.satirlar.filter((s) => s.durum === 'Yaklaşıyor').length, 0);
    kontrol('km 120.000: "Bu kilometrede" sayısı beklenenle aynı', icindeGor === icindeBeklenen, `görünen=${icindeGor} beklenen=${icindeBeklenen}`);
    kontrol('km 120.000: "Yaklaşıyor" sayısı beklenenle aynı', yakinGor === yakinBeklenen, `görünen=${yakinGor} beklenen=${yakinBeklenen}`);
    kontrol('km 120.000: sonuç satırı sayıları söyler', o.sonuc.includes(`${icindeBeklenen} bu kilometrede`) && o.sonuc.includes(`${yakinBeklenen} yaklaşıyor`), o.sonuc);
    // sıralama: kartlarda "Bu kilometrede" olanlar önde
    const siraBozuk = o.kartlar.filter((k) => {
      const rank = (s) => (s.durum === 'Bu kilometrede' ? 0 : s.durum === 'Yaklaşıyor' ? 1 : s.km.startsWith('Kaynaklarda') ? 2 : 3);
      for (let i = 1; i < k.satirlar.length; i++) if (rank(k.satirlar[i]) < rank(k.satirlar[i - 1])) return true;
      return false;
    });
    kontrol('km girilince satırlar kilometreye göre sıralanır', siraBozuk.length === 0, siraBozuk.slice(0, 2).map((k) => k.ad).join(' | '));
    const isaret = await p.evaluate(() => document.querySelectorAll('#liste .isaret').length);
    kontrol('km işareti çizilir', isaret > 0, `isaret=${isaret}`);
    // Filtre
    await p.check('#kmfiltre');
    await bekle(80);
    await hepsiniYukle();
    const f = await oku();
    const hepsiUygun = f.kartlar.every((k) => k.satirlar.every((s) => s.durum !== '' || s.km.startsWith('Kaynaklarda')));
    kontrol('km filtresi: kalan her satır içinde/yaklaşıyor ya da kilometresiz', hepsiUygun);
    const beklenenFiltreli = icindeBeklenen + yakinBeklenen + kayitlar.reduce((t, k) => t + k.sorunlar.filter(({ s }) => !s.tahmini_km_araligi).length, 0);
    kontrol('km filtresi: satır sayısı beklenenle aynı', satirSay(f) === beklenenFiltreli, `satir=${satirSay(f)} beklenen=${beklenenFiltreli}`);
    // km silinince filtre etkisizleşir, ipucu görünür
    await yaz('#km', '');
    const ipucu = await p.evaluate(() => !document.getElementById('km-ipucu').hidden);
    const t = await oku();
    kontrol('km boşken filtre uygulanmaz ve ipucu görünür', ipucu && t.sonuc.startsWith(`${kayitlar.length} kayıt`), t.sonuc);
    await sifirla();
    // km olmadan filtreyi işaretlemek km alanına odaklanır
    await p.check('#kmfiltre');
    await bekle(60);
    const odak = await p.evaluate(() => document.activeElement && document.activeElement.id);
    kontrol('km yokken filtreyi işaretlemek km alanına odaklanır', odak === 'km', String(odak));
    await sifirla();
    // km biçimlendirme
    await p.fill('#km', '120000');
    await p.dispatchEvent('#km', 'change');
    await bekle(60);
    const biçim = await p.inputValue('#km');
    kontrol('km alanı binlik ayraçla biçimlenir', biçim === '120.000', biçim);
    // bin biriminde yazılan değer
    await sifirla();
    await p.fill('#km', '90');
    await p.dispatchEvent('#km', 'change');
    await bekle(100);
    const bin = await p.inputValue('#km');
    kontrol('"90" yazılıp alandan çıkılınca 90.000 km olarak okunur', bin === '90.000', bin);
    await sifirla();
  }

  // ---------- 9. Elektrikli ----------
  console.log('9. Elektrikli');
  {
    await sifirla();
    await p.check('#elektrikli');
    await bekle(60);
    await hepsiniYukle();
    const o = await oku();
    const beklenen = kayitlar.filter((k) => k.a.motor.startsWith('Elektrik') && k.sorunlar.length).length;
    kontrol('elektrikli filtre: kart sayısı beklenenle aynı', o.kartlar.length === beklenen && o.kartlar.every((k) => k.motor.startsWith('Elektrik')), `kart=${o.kartlar.length} beklenen=${beklenen}`);
    await sifirla();
  }

  // ---------- 10. Birleşik filtreler ve temizleme ----------
  console.log('10. Birleşik filtreler');
  {
    await sifirla();
    await p.selectOption('#marka', 'Volkswagen');
    await yaz('#yil', '2016');
    await p.click('label[data-risk="yuksek"] span');
    await yaz('#km', '90000');
    await bekle(100);
    const chip = await p.evaluate(() => [...document.querySelectorAll('#aktif .aktif-cip')].map((b) => b.textContent));
    kontrol('etkin filtre çipleri listelenir', chip.length === 4, JSON.stringify(chip));
    const temizleGorunur = await p.evaluate(() => !document.getElementById('temizle').hidden);
    kontrol('filtreleri temizle düğmesi görünür', temizleGorunur);
    await hepsiniYukle();
    const o = await oku();
    kontrol('birleşik filtre: tüm kartlar VW ve yalnızca yüksek risk', o.kartlar.every((k) => k.marka === 'Volkswagen' && k.satirlar.every((s) => s.risk === 'yuksek')), `kart=${o.kartlar.length}`);
    await p.click('#temizle');
    await bekle(100);
    const t = await oku();
    const durumlar = await p.evaluate(() => ({ ara: document.getElementById('ara').value, marka: document.getElementById('marka').value, yil: document.getElementById('yil').value, km: document.getElementById('km').value, risk: document.querySelector('input[name=risk]:checked').value }));
    kontrol('temizle her filtreyi sıfırlar', t.sonuc.startsWith(`${kayitlar.length} kayıt`) && Object.values(durumlar).every((v) => v === ''), JSON.stringify(durumlar) + t.sonuc);
    // çip ile tek filtre kaldırma
    await p.selectOption('#marka', 'Fiat');
    await yaz('#yil', '2018');
    await p.click('#aktif .aktif-cip:first-child');
    await bekle(100);
    const m = await p.evaluate(() => document.getElementById('marka').value);
    const y = await p.inputValue('#yil');
    kontrol('çipe tıklamak yalnızca o filtreyi kaldırır', m === '' && y === '2018', `marka=${m} yil=${y}`);
    await sifirla();
  }

  // ---------- 11. Satır açma, ayrıntılar, klavye ----------
  console.log('11. Satırlar');
  {
    await sifirla();
    await yaz('#ara', 'k9k');
    const ilk = await p.$('details.sorun-d > summary');
    await ilk.focus();
    await p.keyboard.press('Enter');
    await bekle(80);
    const durum = await p.evaluate(() => {
      const d = document.querySelector('details.sorun-d');
      return { acik: d.open, govde: !!d.querySelector('.sorun-govde'), kaynak: d.querySelectorAll('.kaynaklar a').length, onizlemeGizli: getComputedStyle(d.querySelector('.sorun-onizleme')).display === 'none' };
    });
    kontrol('Enter ile satır açılır, gövde kurulur, kaynaklar listelenir', durum.acik && durum.govde && durum.kaynak >= 2, JSON.stringify(durum));
    kontrol('açık satırda önizleme gizlenir', durum.onizlemeGizli);
    // yeniden çizimde açık satır korunur (başka filtreye geçip geri dönünce)
    await p.check('#elektrikli');
    await bekle(100);
    await p.uncheck('#elektrikli');
    await bekle(100);
    const korunur = await p.evaluate(() => document.querySelector('details.sorun-d').open);
    kontrol('filtre değişip geri dönünce açık satır açık kalır', korunur);
    // km yazdıktan sonra hemen satıra tıklamak yeniden çizimle kaybolmaz
    await sifirla();
    await p.fill('#km', '120000');
    await bekle(400);
    await p.click('details.sorun-d > summary');
    await bekle(100);
    const tikla = await p.evaluate(() => document.querySelector('details.sorun-d').open);
    kontrol('km yazılıp kutudan çıkılırken satır tıklaması kaybolmaz', tikla);
    await p.click('#hepsini-kapat');
    await sifirla();
    await yaz('#ara', 'k9k');
    await p.click('#hepsini-ac');
    await bekle(80);
    const hepsiAcik = await p.evaluate(() => [...document.querySelectorAll('details.sorun-d')].every((d) => d.open && d.querySelector('.sorun-govde')));
    kontrol('"Ayrıntıları aç" hepsini açar ve gövdeleri kurar', hepsiAcik);
    await p.click('#hepsini-kapat');
    await bekle(80);
    const hepsiKapali = await p.evaluate(() => [...document.querySelectorAll('details.sorun-d')].every((d) => !d.open));
    kontrol('"Ayrıntıları kapat" hepsini kapatır', hepsiKapali);
    await sifirla();
    // Ayrıntı açıkken yeni sayfa da açık gelir
    await p.click('#hepsini-ac');
    await p.click('#daha-btn');
    await bekle(100);
    const yeni = await p.evaluate(() => { const l = [...document.querySelectorAll('#liste details.sorun-d')]; return l.length > 0 && l.every((d) => d.open); });
    kontrol('Ayrıntılar açıkken sayfalamayla gelen satırlar da açık', yeni);
    await p.click('#hepsini-kapat');
    await sifirla();
  }

  // ---------- 12. Kaydı açılmayan gruplar ----------
  console.log('12. Kaydı açılmayan gruplar');
  {
    await sifirla();
    await yaz('#ara', 'prado');
    const o = await oku();
    const kapsam = await p.evaluate(() => ({ gor: !document.getElementById('kapsam').hidden, say: document.getElementById('kapsam-say').textContent }));
    kontrol('"prado": kayıt ve kapsam grubu birlikte bulunur', o.kartlar.length > 0 && kapsam.gor, JSON.stringify(kapsam));
    await sifirla();
    await yaz('#ara', 'fullback');
    const o2 = await oku();
    const bosGor = await p.evaluate(() => ({ bos: !document.getElementById('bos').hidden, git: !document.getElementById('kapsam-git').hidden, say: document.getElementById('kapsam-say').textContent }));
    kontrol('"fullback": kayıt yok, kaydı açılmayan grup önerilir', o2.kartlar.length === 0 && bosGor.bos && bosGor.git, JSON.stringify(bosGor));
    await p.click('#kapsam-git');
    await bekle(200);
    const acik = await p.evaluate(() => document.getElementById('kapsam').open);
    kontrol('kapsam düğmesi bölümü açar', acik);
    // risk açıkken kapsam gizlenir
    await sifirla();
    await p.click('label[data-risk="yuksek"] span');
    await bekle(60);
    const gizli = await p.evaluate(() => document.getElementById('kapsam').hidden);
    kontrol('risk filtresi açıkken kapsam bölümü gizlenir', gizli);
    await sifirla();
  }

  // ---------- 13. Hız ----------
  console.log('13. Hız');
  {
    const sureler = await p.evaluate(async () => {
      const sel = document.getElementById('marka');
      const olc = [];
      for (const m of ['Fiat', 'Volkswagen', '', 'BMW', '']) {
        sel.value = m;
        const t = performance.now();
        sel.dispatchEvent(new Event('change', { bubbles: true }));
        document.body.getBoundingClientRect();
        olc.push(Math.round(performance.now() - t));
      }
      const risk = document.getElementById('risk-yuksek');
      for (const r of [true, false]) {
        const t = performance.now();
        document.getElementById(r ? 'risk-yuksek' : 'risk-tumu').checked = true;
        (r ? risk : document.getElementById('risk-tumu')).dispatchEvent(new Event('change', { bubbles: true }));
        document.body.getBoundingClientRect();
        olc.push(Math.round(performance.now() - t));
      }
      return olc;
    });
    kontrol('filtre değişimi 200 ms altında', Math.max(...sureler) < 200, JSON.stringify(sureler));
  }

  // ---------- 13b. Kaydırma: filtre değişince sonuçların başına dön ----------
  console.log('13b. Kaydırma');
  {
    await sifirla();
    await p.evaluate(() => window.scrollTo(0, 2600));
    await bekle(100);
    const once = await p.evaluate(() => window.scrollY);
    await p.selectOption('#marka', 'BMW');
    await bekle(150);
    const sonra = await p.evaluate(() => ({ y: window.scrollY, bar: Math.round(document.getElementById('sonuc-bar').getBoundingClientRect().top), filtre: Math.round(document.getElementById('filtre').offsetHeight) }));
    kontrol('listenin ortasında filtre değişince sonuçların başına dönülür', once > 1500 && sonra.bar >= 0 && sonra.bar <= sonra.filtre + 40, JSON.stringify({ once, ...sonra }));
    await sifirla();
    await p.evaluate(() => window.scrollTo(0, 0));
  }

  // ---------- 14. Düzen: yatay taşma, sticky, mobil panel ----------
  console.log('14. Düzen');
  for (const [ad, w, h] of [['masaüstü', 1280, 800], ['tablet', 820, 1000], ['telefon', 400, 800], ['dar telefon', 340, 700]]) {
    const c = await browser.newContext({ viewport: { width: w, height: h } });
    const q = await c.newPage();
    const e = [];
    q.on('pageerror', (x) => e.push(String(x)));
    await q.goto('file://' + DOSYA);
    await q.waitForSelector('.arac');
    await q.fill('#ara', 'golf');
    await q.waitForTimeout(330);
    await q.click('#hepsini-ac');
    await q.waitForTimeout(100);
    const tasma = await q.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: window.innerWidth }));
    kontrol(`${ad}: yatay taşma yok`, tasma.sw <= tasma.iw, JSON.stringify(tasma));
    const arama = await q.evaluate(() => { const r = document.getElementById('ara').getBoundingClientRect(); return { ust: Math.round(r.top), alt: Math.round(r.bottom) }; });
    kontrol(`${ad}: arama kutusu ilk ekranda`, arama.alt < h, JSON.stringify(arama));
    if (w < 700) {
      const panel = await q.evaluate(() => getComputedStyle(document.getElementById('filtre-panel')).display);
      kontrol(`${ad}: filtre paneli kapalı başlar`, panel === 'none', panel);
      await q.click('#filtre-ac');
      await q.waitForTimeout(80);
      const acik = await q.evaluate(() => ({ d: getComputedStyle(document.getElementById('filtre-panel')).display, a: document.getElementById('filtre-ac').getAttribute('aria-expanded') }));
      kontrol(`${ad}: Filtreler düğmesi paneli açar`, acik.d !== 'none' && acik.a === 'true', JSON.stringify(acik));
      const t2 = await q.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: window.innerWidth }));
      kontrol(`${ad}: panel açıkken taşma yok`, t2.sw <= t2.iw, JSON.stringify(t2));
      await q.selectOption('#marka', 'Fiat');
      await q.waitForTimeout(100);
      const rozet = await q.evaluate(() => ({ g: !document.getElementById('filtre-say').hidden, t: document.getElementById('filtre-say').textContent }));
      kontrol(`${ad}: etkin filtre sayısı düğmede görünür`, rozet.g && rozet.t === '1', JSON.stringify(rozet));
    } else {
      const panel = await q.evaluate(() => getComputedStyle(document.getElementById('filtre-panel')).display);
      kontrol(`${ad}: filtre alanları görünür`, panel !== 'none', panel);
      await q.evaluate(() => window.scrollTo(0, 1800));
      await q.waitForTimeout(100);
      const yapis = await q.evaluate(() => Math.round(document.getElementById('filtre').getBoundingClientRect().top));
      kontrol(`${ad}: filtre çubuğu kaydırınca yapışık kalır`, yapis <= 2 || h < 650, `top=${yapis}`);
    }
    kontrol(`${ad}: sayfa hatası yok`, e.length === 0, e.join(' | '));
    await c.close();
  }

  // ---------- 15. Koyu tema ----------
  console.log('15. Koyu tema');
  {
    const c = await browser.newContext({ viewport: { width: 1280, height: 800 }, colorScheme: 'dark' });
    const q = await c.newPage();
    await q.goto('file://' + DOSYA);
    await q.waitForSelector('.arac');
    const renkler = await q.evaluate(() => ({ bg: getComputedStyle(document.body).backgroundColor, ink: getComputedStyle(document.body).color }));
    kontrol('koyu temada arka plan koyu, yazı açık', renkler.bg === 'rgb(14, 20, 26)' && renkler.ink === 'rgb(227, 232, 237)', JSON.stringify(renkler));
    await c.close();
  }

  kontrol('konsol hatası yok', konsol.length === 0, konsol.join(' | '));
  const basarisiz = sonuclar.filter((s) => !s.ok);
  console.log(`\n${sonuclar.length - basarisiz.length}/${sonuclar.length} kontrol geçti`);
  if (basarisiz.length) { console.log('Başarısızlar:'); for (const b of basarisiz) console.log(' -', b.ad, '|', b.ayrinti); }
  await browser.close();
  process.exit(basarisiz.length ? 1 : 0);
})();
