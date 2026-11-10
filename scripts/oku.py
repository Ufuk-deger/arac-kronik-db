"""Araştırma için okuma yardımcısı (yayına girmez): Şikâyetvar ve DonanımHaber sayfalarını düz curl ile indirir, metne çevirir, parça anahtar kelimelerine göre süzer.
Kullanım:
  python3 -I scripts/oku.py svliste <marka-slug>/<model-slug> [sayfa_sayisi]     -> şikâyet başlıkları ve adresleri
  python3 -I scripts/oku.py sv <url> [url ...]                                     -> şikâyet metinleri (başlık, tarih, metin)
  python3 -I scripts/oku.py dh <konu-url> <ilk> <son> [kelime ...]                 -> konu sayfalarında kelime geçen mesaj parçaları
"""
import sys, re, html, subprocess, hashlib, os, json
IND = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.indir')  # git dışı önbellek
os.makedirs(IND, exist_ok=True)

def getir(url):
    ad = os.path.join(IND, hashlib.md5(url.encode()).hexdigest() + '.html')
    if not os.path.exists(ad):
        r = subprocess.run(['curl', '-sSL', '-m', '40', '-A', 'Mozilla/5.0', url, '-o', ad, '-w', '%{http_code}'], capture_output=True, text=True)
        if r.stdout.strip() != '200':
            if os.path.exists(ad): os.remove(ad)
            return None
    return open(ad, encoding='utf-8', errors='ignore').read()

def metin(h):
    h = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', h, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()

def svliste(yol, n=3):
    marka = yol.split('/')[0]
    gor = {}
    for i in range(1, n + 1):
        h = getir(f'https://www.sikayetvar.com/{yol}' + (f'?page={i}' if i > 1 else ''))
        if not h: break
        for u, t in re.findall(r'href="(/' + re.escape(marka) + r'/[a-z0-9-]{25,})"[^>]*>([^<]{15,250})<', h):
            gor.setdefault(u, html.unescape(t).strip())
    for u, t in gor.items(): print(f'https://www.sikayetvar.com{u}\t{t}')
    h = getir(f'https://www.sikayetvar.com/{yol}') or ''
    etiket = sorted(set(re.findall(r'href="/' + re.escape(yol) + r'/([a-z0-9-]{3,40})"', h)))
    print('ETİKETLER:', ' '.join(etiket))

def sv(urls):
    for u in urls:
        h = getir(u)
        if not h: print('YOK', u); continue
        m = re.search(r'"description"\s*:\s*"(.*?)"\s*,\s*"', h)
        tarih = re.search(r'"datePublished"\s*:\s*"([^"]+)"', h)
        baslik = re.search(r'<h1[^>]*>(.*?)</h1>', h, flags=re.S)
        metinler = re.findall(r'"text"\s*:\s*"((?:[^"\\]|\\.)*)"', h)
        metinler = [json.loads('"' + x + '"') for x in metinler]
        g = metinler[0] if metinler else (html.unescape(m.group(1)) if m else '')
        yorumlar = metinler[1:6]
        print('##', metin(baslik.group(1)) if baslik else u, '|', tarih.group(1)[:10] if tarih else '?')
        print(u); print(g[:1500])
        for y in yorumlar: print('   > yorum:', y[:300])
        print()

def svk(urls):
    """Kısa: başlık | tarih | metindeki model yılları | ilk 350 karakter"""
    for u in urls:
        h = getir(u)
        if not h: print('YOK', u); continue
        metinler = [json.loads('"' + x + '"') for x in re.findall(r'"text"\s*:\s*"((?:[^"\\]|\\.)*)"', h)]
        g = metinler[0] if metinler else ''
        tarih = re.search(r'"datePublished"\s*:\s*"([^"]+)"', h)
        yil = sorted(set(re.findall(r'(20[012]\d|199\d)\s*(?:model|yılı|yili)', g, flags=re.I)))
        km = re.findall(r'(\d{1,3}[.,]?\d{3})\s*(?:km|bin)', g, flags=re.I)[:3]
        print(f"{u.rsplit('/',1)[-1][:70]} | {tarih.group(1)[:10] if tarih else '?'} | yıl:{','.join(yil) or '-'} | km:{','.join(km) or '-'} | yorum:{len(metinler)-1}")
        print('   ', re.sub(r'\s+', ' ', g)[:350])

KONULAR = ['kronik', 'boya', 'pas', 'su-aliyor', 'ses', 'elektrik', 'klima', 'far', 'cam', 'kapi', 'direksiyon', 'multimedya', 'ekran', 'aku', 'fren', 'suspansiyon', 'tavan', 'kilit']

def sikayet_oku(u):
    h = getir(u)
    if not h: return None
    metinler = [json.loads('"' + x + '"') for x in re.findall(r'"text"\s*:\s*"((?:[^"\\]|\\.)*)"', h)]
    g = metinler[0] if metinler else ''
    tarih = re.search(r'"datePublished"\s*:\s*"([^"]+)"', h)
    yil = sorted(set(int(y) for y in re.findall(r'(20[012]\d|199\d)\s*(?:model|yılı|yili|yapımı)', g, flags=re.I)))
    return dict(g=re.sub(r'\s+', ' ', g), tarih=tarih.group(1)[:10] if tarih else '?', yil=yil, yorum=len(metinler) - 1)

def tara(yol, yb, ye, konular):
    """Model konu sayfalarındaki şikâyetleri okur; yalnızca model yılı [yb, ye] içinde olanları (yıl yazmayanları ayrıca) yazar."""
    marka = yol.split('/')[0]
    model_kelime = yol.split('/')[1].split('-')[0]
    gor = set()
    for konu in (konular or KONULAR):
        h = getir(f'https://www.sikayetvar.com/{yol}/{konu}')
        if not h: continue
        urls = []
        for u, t in re.findall(r'href="(/' + re.escape(marka) + r'/[a-z0-9-]{25,})"[^>]*>([^<]{15,250})<', h):
            if u not in gor: gor.add(u); urls.append(u)
        icinde, yilsiz = [], 0
        for u in urls[:20]:
            s = sikayet_oku('https://www.sikayetvar.com' + u)
            if not s or model_kelime not in s['g'].lower(): continue
            if s['yil'] and any(yb <= y <= ye for y in s['yil']):
                icinde.append((u, s))
            elif not s['yil']:
                yilsiz += 1
        print(f'=== {konu}: {len(urls)} şikâyet, {len(icinde)} hedef yıl içinde, {yilsiz} yıl yazmıyor')
        for u, s in icinde:
            print(f"  {u.rsplit('/',1)[-1][:60]} | {s['tarih']} | {s['yil']} | y{s['yorum']}")
            print('     ', s['g'][:260])

def dh(url, ilk, son, kelimeler):
    for i in range(int(ilk), int(son) + 1):
        h = getir(url if i == 1 else f'{url}-{i}')
        if not h: print('YOK sayfa', i); continue
        parcalar = re.split(r'Mesaj Linkini Kopyala', metin(h))
        for p in parcalar[1:]:
            p = re.sub(r'^\s*Şikayet\s*', '', p)[:900]
            if any(re.search(k, p, flags=re.I) for k in kelimeler):
                print(f'[s{i}]', p[:700]); print()

if __name__ == '__main__':
    k = sys.argv[1]
    if k == 'svliste': svliste(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 3)
    elif k == 'sv': sv(sys.argv[2:])
    elif k == 'svk': svk(sys.argv[2:])
    elif k == 'tara': tara(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5:])
    elif k == 'dh': dh(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:] or ['.'])
