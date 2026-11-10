#!/usr/bin/env python3
"""Statik web sitesini üretir: her model için ayrı sayfa, marka sayfaları, arama, site haritası.

Yalnızca yayına uygun alanlar kullanılır: model, yıl, motor, sorun adı, belirtiler, risk ve tahmini kilometre.
Kaynak bağlantıları, site adları ve uzun açıklamalar (detay) siteye girmez; veritabanında dayanak olarak kalır.
Site adı, adresi ve iletişim e-postası data/site.json içindedir. Kullanım:

    python3 scripts/site_uret.py            # çıktı: site/
    python3 scripts/site_uret.py HEDEF_KLASOR
"""

import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dogrula import KOK, MODEL_GENELI_MOTOR, VARSAYILAN_DOSYA  # noqa: E402

AYAR_DOSYASI = KOK / "data" / "site.json"
VARSAYILAN_HEDEF = KOK / "site"
RISK_SIRA = {"Yüksek": 0, "Orta": 1, "Düşük": 2}
RISK_ANAHTAR = {"Yüksek": "yuksek", "Orta": "orta", "Düşük": "dusuk"}
KM_DESENI = re.compile(r"^([\d.]+) - ([\d.]+) km$")
SIMDI = date.today().year
SONSUZ = 10**9
TR_HARF = str.maketrans({"ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u", "â": "a", "î": "i", "û": "u", "ë": "e", "é": "e", "°": ""})

e = html.escape


def kisalt(metin):
    """Sayfa adresi parçası: Türkçe harfler sadeleşir, harf ve rakam dışı karakterler tireye döner."""
    s = metin.lower().replace("İ", "i").translate(TR_HARF)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "model"


def yil_etiketi(b, s):
    return f"{b}–günümüz" if s is None else (str(b) if b == s else f"{b}–{s}")


def taban_adi(model):
    return re.sub(r"\s*\([^()]*\)\s*$", "", model).strip() or model


def ilk_parca(ad):
    return ad.split(" / ")[0].strip()


def km_araligi(metin):
    m = KM_DESENI.match(metin or "")
    return (int(m.group(1).replace(".", "")), int(m.group(2).replace(".", ""))) if m else None


# ---------------------------------------------------------------- veri modeli

def kayitlari_kur(veri):
    """Her kayıt için gösterilecek sorunlar: kayda özgü sorunlar ve ailelerden gelen (kayıtta karşılığı olmayan) ortak sorunlar."""
    aileler = {f["id"]: f for f in veri.get("aileler", [])}
    kayitlar = []
    for arac in veri["arac_listesi"]:
        bagli = {s["aile_sorunu"] for s in arac["kronik_sorunlar"] if "aile_sorunu" in s}
        sorunlar = [(s, None) for s in arac["kronik_sorunlar"]]
        for fid in arac.get("aileler", []):
            f = aileler[fid]
            sorunlar += [(s, f) for s in f["kronik_sorunlar"] if f"{fid}/{s['id']}" not in bagli]
        sorunlar.sort(key=lambda x: (RISK_SIRA[x[0]["risk_seviyesi"]], (km_araligi(x[0].get("tahmini_km_araligi")) or (SONSUZ,))[0]))
        y = arac["uretim_yillari"]
        kayitlar.append({
            "arac": arac, "marka": arac["marka"], "taban": taban_adi(arac["model"]),
            "genel": arac["motor"] == MODEL_GENELI_MOTOR, "yb": y["baslangic"], "ye": y["bitis"],
            "aileler": [aileler[f] for f in arac.get("aileler", [])], "sorunlar": sorunlar,
        })
    return kayitlar


def grupla(kayitlar):
    """Model kartlarıyla aynı kural (viewer/sablon.html): adın ilk parçası aynı olan kayıtlar birlikte ele alınır,
    model geneli kayıtlar nesil çapasıdır; motor kaydı yılları en çok (ve yeterince) örtüşen çapaya girer, çapasızlar örtüştükçe birleşir."""
    markailk = {}
    for k in kayitlar:
        markailk.setdefault(k["marka"], set()).add(ilk_parca(k["taban"]))

    def kok(k):
        ilk = ilk_parca(k["taban"])
        m = re.match(r"^(.*\S)\s+([A-Z]{1,3}\d{1,3})$", ilk)
        return m.group(1) if m and m.group(1) in markailk[k["marka"]] else ilk

    def ortusme(a, b):
        return min(a["ye"] or SIMDI, b["ye"] or SIMDI) - max(a["yb"], b["yb"]) + 1

    kokler = {}
    for k in kayitlar:
        kokler.setdefault((k["marka"], kok(k)), []).append(k)
    gruplar = []
    for liste in kokler.values():
        liste.sort(key=lambda k: (k["yb"], k["ye"] or SONSUZ))
        capalar = [{"capa": k, "kayitlar": [k]} for k in liste if k["genel"]]
        serbest = []
        for k in liste:
            if k["genel"]:
                continue
            en, en_d = None, 0
            kendi = (k["ye"] or SIMDI) - k["yb"] + 1
            for c in capalar:
                d = ortusme(k, c["capa"])
                # sınırda tek yıllık değme yetmez: kaydın yıllarının yarısından fazlası ya da en az 3 yıl çapayla örtüşmeli
                if (d * 2 > kendi or d >= 3) and d > en_d:
                    en, en_d = c, d
            (en["kayitlar"].append(k) if en else serbest.append(k))
        g = None
        for k in serbest:
            if g and k["yb"] < g["son"]:
                g["kayitlar"].append(k)
                g["son"] = max(g["son"], k["ye"] or SONSUZ)
            else:
                g = {"capa": None, "kayitlar": [k], "son": k["ye"] or SONSUZ}
                capalar.append(g)
        gruplar += capalar
    for g in gruplar:
        ks = g["kayitlar"]
        g["marka"] = ks[0]["marka"]
        g["yb"] = min(k["yb"] for k in ks)
        g["ye"] = None if any(k["ye"] is None for k in ks) else max(k["ye"] for k in ks)
        if g["capa"]:
            c = g["capa"]
            g["taban"] = kok(c) if kok(c) != ilk_parca(c["taban"]) else c["taban"]
        else:
            say = {}
            for k in ks:
                say[k["taban"]] = say.get(k["taban"], 0) + 1
            g["taban"] = sorted(say.items(), key=lambda x: (-x[1], len(x[0])))[0][0]
        ks.sort(key=lambda k: (not k["genel"], k["yb"], k["arac"]["motor"]))
    gruplar.sort(key=lambda g: (g["marka"].lower(), dogal(g["taban"]), g["yb"]))
    return gruplar


def dogal(metin):
    return [int(p) if p.isdigit() else p.lower() for p in re.split(r"(\d+)", metin)]


# ---------------------------------------------------------------- HTML parçaları
#
# Tasarım "modern uygulama": beyaz üst şerit + sabit arama, mavi vurgu, yumuşak kartlar. Ana sayfa: arama, çok bakılan modeller,
# logolu marka ızgarası. Model sayfası: görsel + başlık + risk özeti, motor ve kilometre süzgeci, riske göre sıralı sorun kartları.

ONIZLEME = False            # True: bağlantılar klasör yerine açıkça index.html'e gider (dosya olarak gezilebilen önizleme)
LOGOLAR = json.loads((KOK / "data" / "logolar" / "logolar.json").read_text(encoding="utf-8"))
GORSELLER = json.loads((KOK / "data" / "gorseller" / "gorseller.json").read_text(encoding="utf-8"))
GORSEL_KLASORU = KOK / "data" / "gorseller"


def adres_ek(yol):
    """Göreli klasör bağlantısı; önizlemede sonuna index.html eklenir."""
    if not ONIZLEME:
        return yol
    if yol == "" or yol.endswith("/"):
        return yol + "index.html"
    return yol


def logo_html(marka, sinif="logo-m"):
    """Marka logosu (Simple Icons, CC0) ya da logosu olmayan markalarda baş harfler."""
    l = LOGOLAR.get(marka)
    if l:
        return (f'<span class="{sinif}" role="img" aria-label="{e(marka)} logosu"><svg viewBox="0 0 24 24" aria-hidden="true">'
                f'<path d="{l["yol"]}"/></svg></span>')
    harf = "".join(p[0] for p in re.split(r"[\s-]+", marka) if p)[:2].upper()
    return f'<span class="{sinif} harfli" role="img" aria-label="{e(marka)}">{e(harf)}</span>'


# ---- kasa tipi çizimleri (fotoğrafı olmayan modeller için)
KASA_ANAHTAR = [
    ("pikap", r"hilux|amarok|ranger|navara|l200|fullback"),
    ("ticari", r"transit(?! connect)|transporter|sprinter|vito|viano|v-class|master|trafic|boxer|ducato|jumper|crafter|proace(?! city)|expert|jumpy|vivaro|movano"),
    ("hafif-ticari", r"doblo|fiorino|qubo|kangoo|berlingo|partner|rifter|combo|caddy|connect|courier|citan|proace city|nemo|bipper|dokker|lodgy"),
    ("mpv", r"scenic|touran|zafira|meriva|c-max|s-max|galaxy|jogger|picasso|sportsvan|carens|ix20|altea|500l|b serisi|2 serisi active|freemont|note|verso|roomster"),
    ("coupe", r"scirocco|beetle|\btt\b|rx-8|4 serisi|cls|coupe|cabrio|e serisi coupe|giulia|taycan|model 3"),
    ("suv", r"duster|captur|kadjar|austral|arkana|koleos|tucson|sportage|qashqai|x-trail|juke|kuga|ecosport|puma|t-roc|t-cross|tiguan|touareg|taigo|tayron|karoq|kodiaq|kamiq|ateca|arona|formentor|tarraco|q2|q3|q5|q7|q8|q\d e-tron|\bx[1-7]\b|\bix\d?\b|3008|5008|2008|c3 aircross|c5 aircross|crossland|grandland|mokka|frontera|compass|renegade|avenger|cherokee|wrangler|c-hr|rav4|corolla cross|yaris cross|land cruiser|cr-v|hr-v|cx-\d|kona|bayon|santa fe|ix35|stonic|xceed|niro|ev\d|sorento|vitara|s-cross|sx4|forester|xv|hs\b|zs\b|tiggo|t10|evoque|velar|discovery|range rover|gla|glb|glc|glk|gle|ml\b|eqa|eqb|eqc|xc\d0|enyaq|elroq|id\.4|id\.5|tonale|junior|macan|lbx|atto|model y|tavascan|terios|countryman|ds 7|ds 3 crossback|n°8|c4 x|ë-c4|e-c4|tourneo|ioniq 5"),
    ("sedan", r"egea(?! hb)|linea|symbol|taliant|logan|301|c-elysee|jetta|passat|octavia|superb|rapid|toledo|civic|elantra|accent|camry|optima|i40|insignia|mondeo|avensis|corolla|3 serisi|5 serisi|7 serisi|c serisi|e serisi|s serisi|a4|a5|a6|a8|cla|cruze|megane 4 / sedan|fluence|talisman|408|508|407|s40|s60|s80|s90|model s|eqe|eqs|i5|i7|arteon|albea|aveo|accord|cerato|giulietta"),
]


def kasa_tipi(g):
    ad = katla_py(ilk_parca(g["taban"]))
    if "hatchback" in ad:
        return "hatchback"
    for tip, desen in KASA_ANAHTAR:
        if re.search(desen, ad):
            return tip
    return "hatchback"


def katla_py(s):
    return s.lower().replace("İ", "i").replace("ı", "i")


KASA_SVG = {
    # 160x64 kutuda yandan kasa çizgisi: gövde + camlar + iki teker
    "hatchback": ("M14 47 C14 41 17 38 25 37 L44 34 C52 24 60 19 72 18 L118 18 C124 18 128 22 130 28 L134 36 C140 37 144 41 144 47 L144 50 L14 50 Z",
                  "M50 34 C56 26 63 22 72 22 L92 22 L92 34 Z M96 22 L116 22 C120 22 123 25 125 30 L126 34 L96 34 Z", 38, 122, 9, 50),
    "sedan": ("M6 47 C6 42 10 39 18 38 L42 36 C50 27 60 22 74 22 L100 22 C110 22 117 27 124 34 L148 36 C153 37 156 41 156 46 L156 50 L6 50 Z",
              "M48 36 C55 29 63 26 74 26 L92 26 L92 36 Z M96 26 L100 26 C108 26 114 30 118 34 L118 36 L96 36 Z", 34, 128, 9, 50),
    "suv": ("M12 44 L12 33 C12 29 15 27 21 26 L38 24 C44 15 50 10 62 10 L118 10 C126 10 131 14 134 22 L136 26 C144 27 148 30 148 35 L148 46 L12 46 Z",
            "M44 24 C49 17 54 14 62 14 L90 14 L90 24 Z M94 14 L116 14 C123 14 127 18 129 24 L94 24 Z", 38, 122, 10.5, 48),
    "mpv": ("M12 46 L12 36 C12 32 15 30 22 29 L34 27 C42 16 52 11 68 11 L124 11 C132 11 137 15 140 24 L144 30 C148 32 150 35 150 38 L150 50 L12 50 Z",
            "M40 27 C47 18 55 15 68 15 L96 15 L96 27 Z M100 15 L122 15 C128 15 132 19 134 27 L100 27 Z", 38, 124, 9, 50),
    "hafif-ticari": ("M10 46 L10 34 C10 30 13 28 20 27 L30 26 C36 16 44 10 56 10 L140 10 C146 10 150 14 150 20 L150 50 L10 50 Z",
                     "M36 26 C41 18 47 14 56 14 L76 14 L76 26 Z", 36, 124, 9, 50),
    "ticari": ("M8 46 L8 32 C8 28 11 26 18 25 L26 24 C32 12 38 6 50 6 L148 6 C152 6 154 9 154 13 L154 50 L8 50 Z",
               "M32 24 C37 14 42 10 50 10 L66 10 L66 24 Z", 34, 128, 9, 50),
    "pikap": ("M10 45 L10 35 C10 31 13 29 20 28 L36 26 C42 17 48 13 58 13 L88 13 C94 13 98 19 100 26 L100 29 L152 29 L152 47 L10 47 Z",
              "M42 26 C47 19 52 17 58 17 L84 17 C88 17 92 21 94 26 Z", 38, 126, 10.5, 48),
    "coupe": ("M10 47 C10 42 14 39 22 38 L50 36 C60 28 70 25 84 25 L100 25 C112 25 122 29 132 36 L146 38 C152 39 154 42 154 46 L154 50 L10 50 Z",
              "M60 36 C66 31 74 29 84 29 L96 29 L96 36 Z M100 29 C108 29 116 31 124 36 L100 36 Z", 38, 128, 9, 50),
}
KASA_AD = {"hatchback": "hatchback", "sedan": "sedan", "suv": "SUV", "mpv": "MPV", "hafif-ticari": "hafif ticari", "ticari": "ticari",
           "pikap": "pikap", "coupe": "coupe"}


def kasa_svg(tip):
    govde, cam, t1, t2, r, y = KASA_SVG[tip]
    tek = "".join(f'<circle class="kasa-teker" cx="{x}" cy="{y}" r="{r}"/><circle class="kasa-jant" cx="{x}" cy="{y}" r="{r * 0.4:.1f}"/>' for x in (t1, t2))
    return (f'<svg class="kasa" viewBox="0 0 160 64" aria-hidden="true"><path class="kasa-govde" d="{govde}"/>'
            f'<path class="kasa-cam" d="{cam}"/>{tek}</svg>')


def gorsel_html(g, kok, buyuk=False):
    """Modelin fotoğrafı (data/gorseller) ya da kasa tipi çizimi; fotoğrafta lisans gereği yazar ve lisans yazılır."""
    f = GORSELLER.get(g["yol"])
    if f:
        alt = f'{g["marka"]} {g["taban"]} ({g["yil"]})'
        kredi = f'<figcaption class="kredi">Fotoğraf: {e(f["yazar"])}, {e(f["lisans"])}</figcaption>' if buyuk else ""
        return (f'<figure class="gorsel foto"><img src="{kok}img/{e(f["dosya"])}" alt="{e(alt)}" loading="lazy" decoding="async">{kredi}</figure>')
    tip = kasa_tipi(g)
    return f'<figure class="gorsel cizim" data-kasa="{tip}">{kasa_svg(tip)}</figure>'


def sayfa(ayar, derinlik, baslik, aciklama, govde, kanonik, ekbas="", sinif="", ust_ara=True):
    kok = "../" * derinlik
    ara_html = ""
    if ust_ara:
        ara_html = ('<div class="ust-ara" role="search"><label class="gizli" for="ust-ara-kutu">Araç ara</label>'
                    '<svg class="ara-ikon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
                    '<input id="ust-ara-kutu" class="ara-girdi" type="search" placeholder="Marka, model ya da motor ara" '
                    'autocomplete="off" enterkeyhint="search" data-ara>'
                    '<ul class="oneriler" data-oneriler hidden></ul></div>')
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(baslik)}</title>
<meta name="description" content="{e(aciklama)}">
<link rel="canonical" href="{e(kanonik)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(ayar['ad'])}">
<meta property="og:title" content="{e(baslik)}">
<meta property="og:description" content="{e(aciklama)}">
<meta property="og:url" content="{e(kanonik)}">
<meta property="og:locale" content="tr_TR">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{kok}stil.css">
{ekbas}</head>
<body class="{sinif}" data-kok="{kok}" data-onizleme="{'1' if ONIZLEME else ''}">
<header class="ust"><div class="kap ust-ic">
  <a class="logo" href="{adres_ek(kok) or './'}"><span class="logo-isaret" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 13l2-5.5A2 2 0 0 1 8.9 6h6.2a2 2 0 0 1 1.9 1.5L19 13M4 13h16v4a1 1 0 0 1-1 1h-1.5a1 1 0 0 1-1-1v-1h-9v1a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/></svg></span>{e(ayar['ad'])}</a>
  {ara_html}
  <nav class="ust-nav" aria-label="Ana menü"><a href="{adres_ek(kok + 'markalar/')}">Markalar</a><a href="{adres_ek(kok + 'hakkinda/')}">Nasıl okunur</a></nav>
</div></header>
<main class="kap">
{govde}
</main>
<footer class="alt"><div class="kap alt-ic">
  <div><p class="alt-ad">{e(ayar['ad'])}</p>
  <p>Bilgiler kullanıcı bildirimleri ve uzman anlatımları taranarak derlendi ve kendi ifademizle özetlendi; servis görüşü değildir.</p></div>
  <p class="alt-baglanti"><a href="{adres_ek(kok + 'markalar/')}">Markalar</a><a href="{adres_ek(kok + 'hakkinda/')}">Hakkında ve yöntem</a><a href="{adres_ek(kok + 'gizlilik/')}">Gizlilik</a></p>
  <p class="alt-iletisim">{iletisim_html(ayar)}</p>
  <p class="alt-not">Marka adları ve logoları sahiplerinin tescilli markalarıdır; yalnızca aracı tanıtmak için kullanılır.</p>
</div></footer>
<script src="{kok}dizin.js"></script>
<script src="{kok}site.js"></script>
</body>
</html>
"""


def iletisim_html(ayar):
    if ayar.get("eposta"):
        return f'Hata bildirimi ve iletişim: <span class="secilebilir">{e(ayar["eposta"])}</span>'
    return "İletişim adresi yakında eklenecek"


def bildir_html(ayar, ad_tam):
    """Model sayfasının sonunda eksik sorun bildirme çağrısı: bir form adresi varsa bağlantı, yoksa e-posta adresi; ikisi de yoksa hiçbir şey."""
    soru = "Bu modelde listede olmayan bir kronik sorun mu yaşadınız?"
    if ayar.get("bildirim_formu"):
        return (f'<p class="bildir">{e(soru)} <a href="{e(ayar["bildirim_formu"])}" rel="nofollow">Eksik sorunu bildirin</a> '
                f'(model: {e(ad_tam)}).</p>')
    if ayar.get("eposta"):
        return (f'<p class="bildir">{e(soru)} Konu satırına <b>{e(ad_tam)}</b> yazarak '
                f'<span class="secilebilir">{e(ayar["eposta"])}</span> adresine bildirin.</p>')
    return ""


def dizinlenir(g):
    """Arama motorlarına yalnızca modele özgü en az bir sorunu olan sayfalar verilir; yalnızca ortak motor / şanzıman
    sorunlarından oluşan sayfalar başka sayfaların tekrarı olduğu için noindex ve site haritası dışında kalır."""
    return g["ozgu_say"] > 0


def ince_notu(g):
    if g["ozgu_say"] == 0:
        metin = ("Bu model henüz derinlemesine taranmadı. Aşağıdaki sorunlar aynı motoru ya da şanzımanı kullanan "
                 "başka modellerde de görülen ortak sorunlardır; modele özgü sorunlar eklendikçe liste genişleyecek.")
    elif g["ozgu_say"] == 1:
        metin = "Bu model için tarama sürüyor; liste eksik olabilir."
    else:
        return ""
    return f'<p class="ince">{e(metin)}</p>'


def nokta_say(n):
    return f"{n:,}".replace(",", ".")


def km_kisa(km):
    a, b = km
    f = lambda n: f"{n // 1000}" if n % 1000 == 0 else f"{n / 1000:.1f}".replace(".", ",")
    return f"{f(a)}–{f(b)} bin km"


def risk_rozeti(risk):
    return f'<span class="risk" data-risk="{RISK_ANAHTAR[risk]}">{e(risk)}</span>'


def kart_listesi(g):
    """Grubun tüm sorunları tek listede: aynı aile sorunu birden çok motorda görülüyorsa tek kart, motor etiketleri birleşir."""
    motorlar = [k for k in g["kayitlar"] if not k["genel"]]
    motor_no = {id(k): i for i, k in enumerate(motorlar)}
    kartlar, aile_kart = [], {}
    for k in g["kayitlar"]:
        etiket = "genel" if k["genel"] else f"m{motor_no[id(k)]}"
        for s, f in k["sorunlar"]:
            if f is not None:
                anahtar = (f["id"], s["id"])
                if anahtar in aile_kart:
                    aile_kart[anahtar]["etiketler"].append(etiket)
                    continue
                kart = {"s": s, "aile": f, "etiketler": [etiket]}
                aile_kart[anahtar] = kart
            else:
                kart = {"s": s, "aile": None, "etiketler": [etiket]}
            kartlar.append(kart)
    kartlar.sort(key=lambda c: (RISK_SIRA[c["s"]["risk_seviyesi"]], c["aile"] is not None,
                                (km_araligi(c["s"].get("tahmini_km_araligi")) or (SONSUZ,))[0]))
    return motorlar, kartlar


def motor_adi(k, grup_taban):
    ad = k["arac"]["motor"]
    parcalar = [x.strip() for x in grup_taban.split(" / ")]
    return f'{k["taban"]} · {ad}' if k["taban"] != grup_taban and k["taban"] not in parcalar else ad


def kart_html(c, motorlar, grup_taban):
    s = c["s"]
    km = km_araligi(s.get("tahmini_km_araligi"))
    if "genel" in c["etiketler"]:
        yer = '<span class="etk">Tüm motorlar</span>'
    else:
        yer = "".join(f'<span class="etk etk-motor">{e(motor_adi(motorlar[int(t[1:])], grup_taban))}</span>' for t in c["etiketler"])
    km_html = f'<span class="etk etk-km">{km_kisa(km)}</span>' if km else '<span class="etk etk-bos">Kilometre bilgisi yok</span>'
    ortak = ""
    if c["aile"] is not None:
        ortak = (f'<p class="ortak-not">Ortak sorun: {e(c["aile"]["ad"])} kullanan başka modellerde de görülür.</p>')
    veri = (f'data-risk="{RISK_ANAHTAR[s["risk_seviyesi"]]}" data-yer="{" ".join(c["etiketler"])}"'
            + (f' data-kma="{km[0]}" data-kmb="{km[1]}"' if km else ""))
    return f"""<li class="kart" {veri}>
  <div class="kart-bas"><h3>{e(s['sorun_adi'])}</h3>{risk_rozeti(s['risk_seviyesi'])}</div>
  <p class="belirti">{e(s['belirtiler'])}</p>
  <div class="etiketler">{km_html}{yer}<span class="etk etk-uyar" hidden>Kilometrenize uyuyor</span></div>
  {ortak}
</li>"""


def risk_ozeti(kartlar):
    say = {r: sum(1 for c in kartlar if c["s"]["risk_seviyesi"] == r) for r in RISK_SIRA}
    return ('<ul class="ozet" aria-label="Risk dağılımı">' + "".join(
        f'<li data-risk="{RISK_ANAHTAR[r]}"><b>{n}</b><span>{r.lower()} risk</span></li>' for r, n in say.items()) + "</ul>")


def suzgec_html(motorlar, grup_taban):
    motor_dugme = ""
    if len(motorlar) > 1:
        dugmeler = '<button type="button" class="cip" data-motor="" aria-pressed="true">Tüm motorlar</button>' + "".join(
            f'<button type="button" class="cip" data-motor="m{i}" aria-pressed="false">{e(motor_adi(k, grup_taban))}</button>'
            for i, k in enumerate(motorlar))
        motor_dugme = (f'<fieldset class="suz-grup"><legend>Motor</legend><div class="cipler">{dugmeler}</div></fieldset>')
    return f"""<form class="suzgec" data-suzgec hidden>
  {motor_dugme}
  <fieldset class="suz-grup suz-km"><legend>Kilometre</legend>
    <div class="km-girdi"><input id="km-kutu" type="text" inputmode="numeric" placeholder="ör. 120.000" autocomplete="off"><span>km</span></div>
    <label class="kutucuk"><input id="km-yalniz" type="checkbox"> Yalnızca bu kilometreye uyanlar</label>
  </fieldset>
</form>"""


UYARI = ("Bu sayfadaki bilgiler internetteki kullanıcı bildirimleri, forumlar ve uzman yazıları taranarak derlendi ve "
         "kendi ifademizle özetlendi; servis görüşü değildir. Sorunlar her araçta görülmez, kilometre aralıkları tahminidir. "
         "Satın almadan önce ekspertiz ve yetkili servis kontrolü yaptırın.")

NESIL_EKI = re.compile(r"^(\d+(\.\d+)?|[IVX]+|[A-Z]|[A-Z]?\d+[A-Z]?|Mk\d+)$")


def aile_adi(taban):
    """Marka sayfasında ve kardeş bağlantılarında modelleri toplayan ad: nesil eki atılır (Clio 5 -> Clio, Corsa E -> Corsa)."""
    parcalar = ilk_parca(taban).split()
    while len(parcalar) > 1 and NESIL_EKI.match(parcalar[-1]):
        parcalar.pop()
    return " ".join(parcalar)


def populer_gruplar(ayar, gruplar):
    secim = []
    for ad in ayar.get("populer", []):
        marka, taban, *yil = ad.split("|")
        aday = [g for g in gruplar if g["marka"] == marka and (g["taban"] == taban or ilk_parca(g["taban"]) == taban or aile_adi(g["taban"]) == taban)
                and (not yil or g["yb"] == int(yil[0]))]
        if aday:
            secim.append(max(aday, key=lambda g: (g["ozgu_say"] > 0, g["sorun_say"], g["yb"])))
    return secim


def model_karti(g, kok, marka_goster=True):
    marka = f'<span class="mkart-marka">{logo_html(g["marka"], "logo-k")}{e(g["marka"])}</span>' if marka_goster else ""
    return (f'<a class="mkart" href="{adres_ek(kok + g["yol"] + "/")}">{gorsel_html(g, kok)}<span class="mkart-govde">{marka}'
            f'<span class="mkart-ad">{e(g["taban"])}</span><span class="mkart-alt"><span>{e(g["yil"])}</span>'
            f'<span>{g["sorun_say"]} sorun</span></span></span></a>')


def uret(hedef=VARSAYILAN_HEDEF):
    hedef = Path(hedef)
    ayar = json.loads(AYAR_DOSYASI.read_text(encoding="utf-8"))
    adres = ayar["adres"].rstrip("/") + "/"
    veri = json.loads(VARSAYILAN_DOSYA.read_text(encoding="utf-8"))
    gruplar = grupla(kayitlari_kur(veri))

    # adresler
    kullanilan = set()
    markalar = {}
    for g in gruplar:
        m = kisalt(g["marka"])
        yol = f"{m}/{kisalt(g['taban'])}-{g['yb']}-{g['ye'] or 'gunumuz'}"
        aday, n = yol, 2
        while aday in kullanilan:
            aday, n = f"{yol}-{n}", n + 1
        kullanilan.add(aday)
        g["yol"] = aday
        g["yil"] = yil_etiketi(g["yb"], g["ye"])
        g["motorlar"], g["kartlar"] = kart_listesi(g)
        g["sorun_say"] = len(g["kartlar"])
        g["ozgu_say"] = sum(1 for k in g["kayitlar"] for _, f in k["sorunlar"] if f is None)
        markalar.setdefault(g["marka"], {"yol": m, "gruplar": []})["gruplar"].append(g)

    if hedef.exists():
        shutil.rmtree(hedef)
    hedef.mkdir(parents=True)
    (hedef / "stil.css").write_text(STIL, encoding="utf-8")
    (hedef / "site.js").write_text(SITE_JS, encoding="utf-8")
    if any(GORSELLER.values()):
        (hedef / "img").mkdir()
        for f in GORSELLER.values():
            shutil.copy(GORSEL_KLASORU / f["dosya"], hedef / "img" / f["dosya"])
    dizin = [{"a": f"{g['marka']} {g['taban']}", "b": g["marka"], "y": g["yil"], "yb": g["yb"], "ye": g["ye"] or 9999,
              "u": g["yol"] + "/", "s": g["sorun_say"],
              "m": " ".join(k["arac"]["motor"] for k in g["kayitlar"] if not k["genel"]) + " " + " ".join(k["arac"]["model"] for k in g["kayitlar"])}
             for g in gruplar]
    (hedef / "dizin.js").write_text("window.DIZIN=" + json.dumps(dizin, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    sayfalar = []

    def yaz(yol, icerik, dizinle=True):
        p = hedef / yol / "index.html" if yol else hedef / "index.html"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(icerik, encoding="utf-8")
        if dizinle:
            sayfalar.append(adres + (yol + "/" if yol else ""))

    # model sayfaları
    for g in gruplar:
        ad_tam = f"{g['marka']} {g['taban']} ({g['yil']})"
        baslik = f"{ad_tam} kronik sorunları | {ayar['ad']}"
        ilk = ", ".join(c["s"]["sorun_adi"] for c in g["kartlar"][:2])[:150]
        aciklama = f"{ad_tam} için bilinen {g['sorun_say']} kronik sorun: belirtiler, risk ve tahmini kilometre. {ilk}"[:300]
        motorlar, kartlar = g["motorlar"], g["kartlar"]
        kardes = [x for x in markalar[g["marka"]]["gruplar"] if x is not g and aile_adi(x["taban"]) == aile_adi(g["taban"])]
        kardes_html = ""
        if kardes:
            kardes_html = ('<section class="blok"><h2>Diğer nesiller</h2><div class="mkartlar">'
                           + "".join(model_karti(x, "../../", False) for x in sorted(kardes, key=lambda x: -x["yb"])) + "</div></section>")
        meta = [f"<span>{e(g['yil'])}</span>"]
        if motorlar:
            meta.append(f"<span>{len(motorlar)} motor seçeneği</span>")
        meta.append(f"<span>{g['sorun_say']} kronik sorun</span>")
        yol_izi = (f'<nav class="iz" aria-label="Konum"><a href="{adres_ek("../../")}">Ana sayfa</a><span aria-hidden="true">›</span>'
                   f'<a href="{adres_ek("../")}">{e(g["marka"])}</a><span aria-hidden="true">›</span><span>{e(g["taban"])}</span></nav>')
        liste = "\n".join(kart_html(c, motorlar, g["taban"]) for c in kartlar)
        govde = f"""{yol_izi}
<header class="model-bas">
  {gorsel_html(g, "../../", True)}
  <div class="model-bilgi">
    <a class="model-marka" href="{adres_ek("../")}">{logo_html(g['marka'], 'logo-k')}{e(g['marka'])}</a>
    <h1>{e(g['taban'])}</h1>
    <p class="model-meta">{''.join(meta)}</p>
    {risk_ozeti(kartlar)}
  </div>
</header>
{ince_notu(g)}
{suzgec_html(motorlar, g['taban'])}
<div class="liste-bas"><h2>Kronik sorunlar</h2><p class="liste-durum" data-durum aria-live="polite">{g['sorun_say']} sorun · riske göre sıralı</p></div>
<ol class="kartlar" data-kartlar>
{liste}
</ol>
<p class="bos" data-bos hidden>Seçiminize uyan sorun yok. Kilometre süzgecini kaldırmayı ya da başka bir motor seçmeyi deneyin.</p>
{bildir_html(ayar, ad_tam)}
<p class="uyari">{e(UYARI)}</p>
{kardes_html}"""
        iz_ld = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": adres},
            {"@type": "ListItem", "position": 2, "name": g["marka"], "item": adres + markalar[g["marka"]]["yol"] + "/"},
            {"@type": "ListItem", "position": 3, "name": f"{g['taban']} {g['yil']}", "item": adres + g["yol"] + "/"}]}, ensure_ascii=False)
        iz_ld = iz_ld.replace("</", "<\\/")
        ekbas = f'<script type="application/ld+json">{iz_ld}</script>\n'
        if not dizinlenir(g):
            ekbas = '<meta name="robots" content="noindex, follow">\n' + ekbas
        yaz(g["yol"], sayfa(ayar, 2, baslik, aciklama, govde, adres + g["yol"] + "/", ekbas, "s-model"), dizinle=dizinlenir(g))

    # marka sayfaları: modeller adına göre, her modelin nesilleri yeniden eskiye
    for marka, b in markalar.items():
        aileler = {}
        for g in b["gruplar"]:
            aileler.setdefault(aile_adi(g["taban"]), []).append(g)
        sirali = [g for kok_ad in sorted(aileler, key=dogal) for g in sorted(aileler[kok_ad], key=lambda g: -g["yb"])]
        bloklar = '<div class="mkartlar">' + "".join(model_karti(g, "../", False) for g in sirali) + "</div>"
        govde = (f'<nav class="iz" aria-label="Konum"><a href="{adres_ek("../")}">Ana sayfa</a><span aria-hidden="true">›</span><span>{e(marka)}</span></nav>'
                 f'<header class="marka-bas">{logo_html(marka, "logo-b")}<div><h1>{e(marka)}</h1>'
                 f'<p class="model-meta"><span>{len(b["gruplar"])} model ve nesil</span><span>{sum(g["sorun_say"] for g in b["gruplar"])} sorun kaydı</span></p></div></header>'
                 f'<div class="model-bloklar">{bloklar}</div>')
        yaz(b["yol"], sayfa(ayar, 1, f"{marka} kronik sorunları: model ve yıla göre | {ayar['ad']}",
                            f"{marka} modellerinin bilinen kronik sorunları, model ve üretim yılına göre.", govde, adres + b["yol"] + "/"))

    def marka_izgara(kok):
        return '<ul class="markalar">' + "".join(
            f'<li><a href="{adres_ek(kok + b["yol"] + "/")}">{logo_html(m, "logo-m")}<span class="mrk-ad">{e(m)}</span>'
            f'<span class="mrk-say">{len(b["gruplar"])} model</span></a></li>'
            for m, b in sorted(markalar.items(), key=lambda x: x[0].lower())) + "</ul>"

    yaz("markalar", sayfa(ayar, 1, f"Markalar | {ayar['ad']}", "Kronik sorunları listelenen tüm markalar.",
                          f'<header class="sayfa-bas"><h1>Markalar</h1><p class="model-meta"><span>{len(markalar)} marka</span><span>{len(gruplar)} model ve nesil</span></p></header>'
                          f'{marka_izgara("../")}', adres + "markalar/"))

    # ana sayfa
    toplam_sorun = sum(len(a["kronik_sorunlar"]) for a in veri["arac_listesi"]) + sum(len(f["kronik_sorunlar"]) for f in veri.get("aileler", []))
    pop = populer_gruplar(ayar, gruplar)
    cipler = "".join(f'<a class="cip" href="{adres_ek(g["yol"] + "/")}">{e(g["marka"])} {e(g["taban"])}</a>' for g in pop[:6])
    pop_html = ""
    if pop:
        pop_html = (f'<section class="blok"><div class="blok-bas"><h2>Çok bakılan modeller</h2></div>'
                    f'<div class="mkartlar">{"".join(model_karti(g, "") for g in pop)}</div></section>')
    govde = f"""<section class="kahraman">
  <h1>Aracın kronik sorunlarını almadan önce öğren</h1>
  <p class="giris">Model, yıl ve motoruna göre bilinen arızalar; ne kadar ciddi olduğu ve hangi kilometrede çıktığıyla.</p>
  <div class="ana-ara" role="search">
    <label for="ana-ara-kutu" class="gizli">Marka ve model ara</label>
    <svg class="ara-ikon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
    <input id="ana-ara-kutu" class="ara-girdi buyuk" type="search" placeholder="Clio 5, Egea 2018, Golf 7, 1.5 dCi…" autocomplete="off" enterkeyhint="search" data-ara>
    <button type="button" class="ara-dugme" data-ara-git>Ara</button>
    <ul class="oneriler genis" data-oneriler hidden></ul>
  </div>
  <div class="cipler hizli">{cipler}</div>
  <ul class="sayilar"><li><b>{len(gruplar)}</b> model ve nesil</li><li><b>{nokta_say(toplam_sorun)}</b> kronik sorun</li><li><b>{len(markalar)}</b> marka</li></ul>
</section>
{pop_html}
<section class="blok"><div class="blok-bas"><h2>Markalar</h2><a class="blok-link" href="{adres_ek('markalar/')}">Tümünü gör</a></div>{marka_izgara("")}</section>
<section class="blok">
  <h2>Nasıl okunur?</h2>
  <div class="nasil-ic">
    <div><span class="nasil-ikon" aria-hidden="true">1</span><h3>Aracını bul</h3><p>Marka ve modelini yaz ya da markadan seç. Her nesil ayrı sayfadadır.</p></div>
    <div><span class="nasil-ikon" aria-hidden="true">2</span><h3>Motorunu seç</h3><p>Sorunların çoğu belirli bir motora ya da şanzımana aittir. Motor kodu ruhsatta yazar.</p></div>
    <div><span class="nasil-ikon" aria-hidden="true">3</span><h3>Kilometreni gir</h3><p>O kilometrede çıkması beklenen sorunlar işaretlenir. Ekspertizde bunlara özellikle baktır.</p></div>
  </div>
</section>"""
    yaz("", sayfa(ayar, 0, f"{ayar['ad']}: araçların kronik sorunları", f"{ayar['slogan']}. Model, yıl ve motora göre bilinen sorunlar.", govde, adres, "", "s-ana", ust_ara=False))

    # sabit sayfalar
    yaz("hakkinda", sayfa(ayar, 1, f"Hakkında ve yöntem | {ayar['ad']}", "Sorunların nasıl derlendiği ve nasıl okunacağı.", f"""
<header class="sayfa-bas"><h1>Hakkında ve yöntem</h1></header>
<div class="metin">
<p>{e(ayar.get('tanitim') or ayar['ad'] + ", ikinci el ya da sıfır araç bakan biri için Türkiye'de yaygın araçların bilinen kronik sorunlarını tek yerde toplar.")}</p>
<h2>Sorunlar nasıl belirlendi?</h2>
<p>Kullanıcı şikâyetleri, sürücü forumları, servis duyuruları ve uzman yazıları tarandı. Çoğu sorun en az iki farklı kaynakta tekrar eden bildirimlere dayanır. Her sorun kendi ifademizle yazıldı; kilometre bilgisi kaynaklarda yoksa uydurulmadı.</p>
<h2>Nasıl okunur?</h2>
<ul>
<li><b>Tüm motorlar</b> etiketi: kasa, sızdırmazlık, iç mekân, elektronik ve süspansiyon gibi motordan bağımsız sorunlar.</li>
<li><b>Motor etiketi</b>: belirli bir motor ya da şanzıman sürümüne ait sorunlar. "Ortak sorun" notu, aynı motoru ya da şanzımanı kullanan başka modellerde de görüldüğünü belirtir; aracınızın motor kodunu ruhsattan kontrol edin.</li>
<li><b>Risk</b>: yüksek (güvenlik, motor ya da kontrol ünitesi hasarı), orta (onarım gerektiren arıza), düşük (konfor ve kozmetik). Bu bizim değerlendirmemizdir, istatistik değildir.</li>
<li><b>Kilometre</b>: sorunun bildirildiği yaklaşık aralık; kullanım ve bakıma göre değişir.</li>
</ul>
<h2>Sınırlar</h2>
<p>Burada yazan sorunların aracınızda olacağı anlamına gelmez; listede olmayan bir sorunun görülmeyeceği anlamına da gelmez. Karar vermeden önce ekspertiz ve yetkili servis kontrolü yaptırın.</p>
<h2>Görseller</h2>
<p>Marka logoları Simple Icons koleksiyonundan alınmıştır ve markaların tescilli ticari markalarıdır; yalnızca markayı tanıtmak için kullanılır. Fotoğrafı olmayan modellerde kasa tipini gösteren bir çizim kullanılır.</p>
<h2>Hata bildirimi</h2>
<p>{iletisim_html(ayar)}.</p>
</div>""", adres + "hakkinda/"))
    yaz("gizlilik", sayfa(ayar, 1, f"Gizlilik | {ayar['ad']}", "Gizlilik bilgilendirmesi.", f"""
<header class="sayfa-bas"><h1>Gizlilik</h1></header>
<div class="metin">
<p>Bu site çerez kullanmaz, üyelik istemez ve ziyaretçilerden kişisel veri toplamaz. Arama kutusuna ve kilometre alanına yazdıklarınız yalnızca tarayıcınızda işlenir, bize gönderilmez.</p>
<p>Barındırma hizmeti, tüm web sitelerinde olduğu gibi teknik güvenlik amacıyla standart sunucu kayıtları tutabilir.</p>
<p>{iletisim_html(ayar)}.</p>
</div>""", adres + "gizlilik/"))
    (hedef / "404.html").write_text(sayfa(ayar, 0, f"Sayfa bulunamadı | {ayar['ad']}", "Sayfa bulunamadı.",
                                          '<header class="sayfa-bas"><h1>Sayfa bulunamadı</h1></header><p>Aradığınız sayfa taşınmış ya da hiç olmamış olabilir. Yukarıdaki kutudan aracınızı arayın.</p>', adres), encoding="utf-8")
    bugun = date.today().isoformat()
    (hedef / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                       + "".join(f"<url><loc>{e(u)}</loc><lastmod>{bugun}</lastmod></url>\n" for u in sayfalar)
                                       + "</urlset>\n", encoding="utf-8")
    (hedef / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {adres}sitemap.xml\n", encoding="utf-8")
    return {"model": len(gruplar), "marka": len(markalar), "sayfa": len(sayfalar)}


SITE_JS = r"""
(() => {
  const kok = document.body.dataset.kok || "";
  const onizleme = document.body.dataset.onizleme === "1";
  const git = (u) => kok + u + (onizleme ? "index.html" : "");
  const katla = (s) => s.toLocaleLowerCase("tr-TR").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/ı/g, "i");
  const dizin = (window.DIZIN || []).map((d) => {
    const t = katla(d.a + " " + d.m);
    return Object.assign(d, { ad: katla(d.a), t, ts: t.replace(/[\s.\-\/()]/g, "") });
  });

  // ---- arama: her terim adda, motorda ya da boşluksuz yazımda geçmeli; yıl verilirse üretim yıllarına uymalı
  function bul(sorgu) {
    const terimler = katla(sorgu).split(/\s+/).filter(Boolean);
    if (!terimler.length) return [];
    const yil = terimler.find((t) => /^(19|20)\d\d$/.test(t));
    const kel = terimler.filter((t) => t !== yil);
    let s = dizin.filter((d) => kel.every((t) => d.t.includes(t) || d.ts.includes(t.replace(/[.\-\/]/g, ""))));
    if (yil) s = s.filter((d) => +yil >= d.yb && +yil <= d.ye);
    const puan = (d) => (kel.length && d.ad.includes(kel.join(" ")) ? 4 : 0) + kel.filter((t) => d.ad.includes(t)).length * 2 + (d.ad.startsWith(kel[0] || "~") ? 1 : 0);
    return s.sort((a, b) => puan(b) - puan(a) || b.yb - a.yb).slice(0, 12);
  }
  for (const girdi of document.querySelectorAll("[data-ara]")) {
    const kutu = girdi.parentElement;
    const liste = kutu.querySelector("[data-oneriler]");
    let secili = -1, sonuc = [];
    const ciz = () => {
      sonuc = bul(girdi.value); secili = -1; liste.textContent = "";
      if (!girdi.value.trim()) { liste.hidden = true; return; }
      if (!sonuc.length) {
        const li = document.createElement("li"); li.className = "oneri-yok";
        li.textContent = "Eşleşen araç yok. Yalnızca model adını yazmayı deneyin (ör. clio, egea).";
        liste.append(li);
      }
      for (const d of sonuc) {
        const li = document.createElement("li");
        const a = document.createElement("a"); a.href = git(d.u);
        a.innerHTML = '<span class="o-ad"></span><span class="o-yil"></span><span class="o-say"></span>';
        a.children[0].textContent = d.a; a.children[1].textContent = d.y; a.children[2].textContent = d.s + " sorun";
        li.append(a); liste.append(li);
      }
      liste.hidden = false;
    };
    const isaretle = () => liste.querySelectorAll("a").forEach((a, i) => a.classList.toggle("aktif", i === secili));
    const ilkeGit = () => { if (sonuc.length) location.href = git(sonuc[Math.max(0, secili)].u); else { ciz(); girdi.focus(); } };
    girdi.addEventListener("input", ciz);
    girdi.addEventListener("focus", () => { if (girdi.value.trim()) ciz(); });
    girdi.addEventListener("keydown", (ev) => {
      const n = liste.querySelectorAll("a").length;
      if (ev.key === "ArrowDown" && n) { secili = (secili + 1) % n; isaretle(); ev.preventDefault(); }
      else if (ev.key === "ArrowUp" && n) { secili = (secili - 1 + n) % n; isaretle(); ev.preventDefault(); }
      else if (ev.key === "Enter") { ilkeGit(); ev.preventDefault(); }
      else if (ev.key === "Escape") { liste.hidden = true; }
    });
    const dugme = kutu.querySelector("[data-ara-git]");
    if (dugme) dugme.addEventListener("click", () => { sonuc = bul(girdi.value); ilkeGit(); });
    document.addEventListener("click", (ev) => { if (!kutu.contains(ev.target)) liste.hidden = true; });
  }

  // ---- model sayfası: motor ve kilometre süzgeci
  const suz = document.querySelector("[data-suzgec]");
  if (suz) {
    suz.hidden = false;
    const kartlar = [...document.querySelectorAll("[data-kartlar] > li")];
    const durum = document.querySelector("[data-durum]"), bos = document.querySelector("[data-bos]");
    const kmKutu = document.getElementById("km-kutu"), yalniz = document.getElementById("km-yalniz");
    let motor = "";
    const kmOku = () => { const n = parseInt((kmKutu.value || "").replace(/\D/g, ""), 10); return Number.isFinite(n) ? n : null; };
    function uygula() {
      const km = kmOku(); let gorunen = 0, uyan = 0;
      for (const k of kartlar) {
        const yer = k.dataset.yer.split(" ");
        const motorUyar = !motor || yer.includes("genel") || yer.includes(motor);
        const kmUyar = km !== null && "kma" in k.dataset && km >= +k.dataset.kma && km <= +k.dataset.kmb;
        k.querySelector(".etk-uyar").hidden = !kmUyar;
        k.classList.toggle("km-icinde", kmUyar);
        const goster = motorUyar && (!yalniz.checked || km === null || kmUyar);
        k.hidden = !goster; if (goster) gorunen++; if (goster && kmUyar) uyan++;
      }
      durum.textContent = gorunen + " sorun" + (km !== null ? " · " + uyan + " tanesi " + km.toLocaleString("tr-TR") + " km'ye uyuyor" : " · riske göre sıralı");
      bos.hidden = gorunen > 0;
    }
    for (const b of suz.querySelectorAll("[data-motor]")) {
      b.addEventListener("click", () => {
        motor = b.dataset.motor;
        suz.querySelectorAll("[data-motor]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
        uygula();
      });
    }
    kmKutu.addEventListener("input", () => { const n = kmOku(); if (n !== null) kmKutu.value = n.toLocaleString("tr-TR"); uygula(); });
    yalniz.addEventListener("change", uygula);
    suz.addEventListener("submit", (ev) => ev.preventDefault());
  }
})();
"""

STIL = r"""/* Bilmiş Usta: modern uygulama görünümü. Beyaz üst şerit + arama, gri zemin, beyaz kartlar, tek mavi vurgu. */
:root {
  --zemin: #f5f7fa; --yuzey: #ffffff; --yuzey-2: #f2f4f7; --yazi: #101828; --soluk: #667085; --cizgi: #e4e7ec; --cizgi-koyu: #d0d5dd;
  --ana: #2563eb; --ana-koyu: #1d4ed8; --ana-acik: #eef4ff; --ana-yazi: #ffffff;
  --yuksek: #b42318; --yuksek-z: #fef3f2; --yuksek-c: #fda29b;
  --orta: #b54708; --orta-z: #fffaeb; --orta-c: #fec84b;
  --dusuk: #067647; --dusuk-z: #ecfdf3; --dusuk-c: #75e0a7;
  --kasa: #d0d5dd; --kasa-cam: #f2f4f7; --kasa-teker: #475467;
  --golge: 0 1px 2px rgba(16, 24, 40, .05);
  --golge-2: 0 12px 24px -6px rgba(16, 24, 40, .12), 0 2px 6px rgba(16, 24, 40, .05);
  --f-baslik: "Manrope", "Inter", "Segoe UI", system-ui, sans-serif;
  --f-govde: "Inter", "Segoe UI", Roboto, system-ui, sans-serif;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --zemin: #0c111d; --yuzey: #161b26; --yuzey-2: #1f242f; --yazi: #f5f5f6; --soluk: #94969c; --cizgi: #252b37; --cizgi-koyu: #333741;
    --ana: #4f8cff; --ana-koyu: #6ea1ff; --ana-acik: #172554; --ana-yazi: #ffffff;
    --yuksek: #fda29b; --yuksek-z: #3b1210; --yuksek-c: #912018;
    --orta: #fec84b; --orta-z: #3a2606; --orta-c: #93370d;
    --dusuk: #75e0a7; --dusuk-z: #0b2e1e; --dusuk-c: #085d3a;
    --kasa: #333741; --kasa-cam: #1f242f; --kasa-teker: #94969c;
    --golge: 0 1px 2px rgba(0, 0, 0, .3); --golge-2: 0 12px 24px -6px rgba(0, 0, 0, .5);
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --zemin: #0c111d; --yuzey: #161b26; --yuzey-2: #1f242f; --yazi: #f5f5f6; --soluk: #94969c; --cizgi: #252b37; --cizgi-koyu: #333741;
  --ana: #4f8cff; --ana-koyu: #6ea1ff; --ana-acik: #172554; --ana-yazi: #ffffff;
  --yuksek: #fda29b; --yuksek-z: #3b1210; --yuksek-c: #912018;
  --orta: #fec84b; --orta-z: #3a2606; --orta-c: #93370d;
  --dusuk: #75e0a7; --dusuk-z: #0b2e1e; --dusuk-c: #085d3a;
  --kasa: #333741; --kasa-cam: #1f242f; --kasa-teker: #94969c;
  --golge: 0 1px 2px rgba(0, 0, 0, .3); --golge-2: 0 12px 24px -6px rgba(0, 0, 0, .5);
  color-scheme: dark;
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--zemin); color: var(--yazi); font-family: var(--f-govde); font-size: 16px; line-height: 1.6; }
[hidden] { display: none !important; }
a { color: var(--ana); text-decoration: none; }
a:hover { text-decoration: underline; }
:focus-visible { outline: 3px solid color-mix(in srgb, var(--ana) 45%, transparent); outline-offset: 2px; border-radius: 6px; }
.gizli { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.kap { max-width: 72rem; margin-inline: auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
h1, h2, h3 { font-family: var(--f-baslik); line-height: 1.2; letter-spacing: -0.015em; text-wrap: balance; margin: 0; color: var(--yazi); }
h1 { font-size: clamp(1.75rem, 4vw, 2.4rem); font-weight: 800; }
h2 { font-size: 1.3rem; font-weight: 700; }
h3 { font-size: 1.02rem; font-weight: 700; }

/* üst şerit */
.ust { background: var(--yuzey); border-bottom: 1px solid var(--cizgi); position: sticky; top: env(safe-area-inset-top, 0px); z-index: 20; }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 21; background: var(--yuzey); }
.ust-ic { display: flex; align-items: center; gap: 12px 24px; min-height: 64px; flex-wrap: wrap; padding-block: 8px; }
.logo { display: inline-flex; align-items: center; gap: 10px; font-family: var(--f-baslik); font-weight: 800; font-size: 1.15rem; color: var(--yazi); white-space: nowrap; }
.logo:hover { text-decoration: none; }
.logo-isaret { width: 32px; height: 32px; border-radius: 9px; background: var(--ana); display: inline-grid; place-items: center; }
.logo-isaret svg { width: 20px; height: 20px; fill: none; stroke: var(--ana-yazi); stroke-width: 1.8; stroke-linejoin: round; }
.ust-ara { position: relative; flex: 1 1 18rem; min-width: 0; max-width: 28rem; }
.ust-nav { display: flex; gap: 22px; margin-left: auto; font-weight: 600; font-size: 0.93rem; }
.ust-nav a { color: var(--soluk); }
.ust-nav a:hover { color: var(--yazi); text-decoration: none; }
.ara-ikon { position: absolute; left: 12px; top: 50%; width: 18px; height: 18px; transform: translateY(-50%); fill: none; stroke: var(--soluk); stroke-width: 2; stroke-linecap: round; pointer-events: none; }
.ara-girdi { width: 100%; font: inherit; font-size: 0.95rem; padding: 9px 12px 9px 38px; min-height: 42px; border-radius: 10px; border: 1px solid var(--cizgi-koyu); background: var(--yuzey-2); color: var(--yazi); }
.ara-girdi::placeholder { color: var(--soluk); }
.ara-girdi:focus { outline: none; background: var(--yuzey); border-color: var(--ana); box-shadow: 0 0 0 4px color-mix(in srgb, var(--ana) 18%, transparent); }
.oneriler { position: absolute; left: 0; right: 0; top: calc(100% + 6px); list-style: none; margin: 0; padding: 6px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 12px; box-shadow: var(--golge-2); max-height: min(70vh, 30rem); overflow-y: auto; z-index: 30; text-align: left; }
.oneriler a { display: grid; grid-template-columns: 1fr auto; gap: 0 12px; padding: 9px 12px; border-radius: 8px; color: var(--yazi); }
.oneriler a:hover, .oneriler a.aktif { background: var(--ana-acik); text-decoration: none; }
.o-ad { font-weight: 600; }
.o-yil { font-size: 0.84rem; color: var(--soluk); grid-column: 1; }
.o-say { grid-row: 1 / span 2; grid-column: 2; align-self: center; font-size: 0.84rem; color: var(--soluk); }
.oneri-yok { padding: 10px 12px; color: var(--soluk); }

main { padding-block: 24px 64px; display: grid; gap: 28px; }
main > * { min-width: 0; }

/* ana sayfa */
.kahraman { display: grid; gap: 14px; justify-items: center; text-align: center; padding: 40px 24px 34px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 20px; box-shadow: var(--golge); }
.kahraman h1 { font-size: clamp(1.9rem, 5vw, 2.8rem); max-width: 20ch; }
.giris { margin: 0; color: var(--soluk); font-size: 1.08rem; max-width: 52ch; }
.ana-ara { position: relative; width: 100%; max-width: 42rem; margin-top: 8px; }
.ana-ara .ara-ikon { left: 18px; width: 20px; height: 20px; }
.ara-girdi.buyuk { font-size: 1.08rem; min-height: 58px; padding: 14px 108px 14px 48px; border-radius: 14px; background: var(--yuzey); box-shadow: var(--golge); }
.ara-dugme { position: absolute; right: 7px; top: 7px; bottom: 7px; padding: 0 22px; font: inherit; font-weight: 600; border: 0; border-radius: 10px; background: var(--ana); color: var(--ana-yazi); cursor: pointer; }
.ara-dugme:hover { background: var(--ana-koyu); }
.cipler { display: flex; flex-wrap: wrap; gap: 8px; }
.cipler.hizli { justify-content: center; }
.cip { display: inline-flex; align-items: center; font: inherit; font-size: 0.88rem; font-weight: 500; padding: 6px 13px; min-height: 36px; border-radius: 999px; border: 1px solid var(--cizgi-koyu); background: var(--yuzey); color: var(--yazi); cursor: pointer; text-align: left; }
.cip:hover { border-color: var(--ana); color: var(--ana); text-decoration: none; }
.cip[aria-pressed="true"] { background: var(--ana); border-color: var(--ana); color: var(--ana-yazi); }
.sayilar { list-style: none; margin: 8px 0 0; padding: 0; display: flex; flex-wrap: wrap; justify-content: center; gap: 6px 28px; color: var(--soluk); font-size: 0.92rem; }
.sayilar b { color: var(--yazi); font-family: var(--f-baslik); font-size: 1.05rem; margin-right: 4px; font-variant-numeric: tabular-nums; }
.blok { display: grid; gap: 14px; }
.blok-bas { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; }
.blok-link { font-weight: 600; font-size: 0.93rem; }

/* model kartları (görselli) */
.mkartlar { display: grid; gap: 14px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 14.5rem), 1fr)); }
.mkart { display: grid; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 14px; overflow: hidden; color: var(--yazi); box-shadow: var(--golge); transition: box-shadow .15s, transform .15s, border-color .15s; }
.mkart:hover { text-decoration: none; box-shadow: var(--golge-2); transform: translateY(-2px); border-color: var(--cizgi-koyu); }
.mkart-govde { display: grid; gap: 2px; padding: 12px 14px 14px; }
.mkart-marka { display: inline-flex; align-items: center; gap: 6px; font-size: 0.8rem; color: var(--soluk); font-weight: 500; }
.mkart-ad { font-family: var(--f-baslik); font-weight: 700; font-size: 1.05rem; line-height: 1.3; }
.mkart-alt { display: flex; justify-content: space-between; gap: 8px; font-size: 0.84rem; color: var(--soluk); }
.gorsel { margin: 0; background: linear-gradient(180deg, var(--yuzey-2), var(--yuzey)); aspect-ratio: 16 / 9; max-width: 100%; display: grid; place-items: center; overflow: hidden; }
.gorsel img { width: 100%; height: 100%; object-fit: cover; }
.gorsel.cizim .kasa { width: 66%; max-width: 15rem; height: auto; }
.mkartlar .gorsel { aspect-ratio: 2 / 1; }
.kasa-govde { fill: var(--kasa); }
.kasa-cam { fill: var(--kasa-cam); }
.kasa-teker { fill: var(--kasa-teker); }
.kasa-jant { fill: var(--kasa); }
.foto { position: relative; }
.kredi { position: absolute; right: 0; bottom: 0; padding: 2px 8px; font-size: 0.7rem; background: rgba(0,0,0,.55); color: #fff; border-top-left-radius: 6px; }

/* logolar */
.logo-m, .logo-k, .logo-b { display: inline-grid; place-items: center; flex: none; }
.logo-m svg, .logo-k svg, .logo-b svg { fill: currentColor; width: 100%; height: 100%; }
.logo-k { width: 16px; height: 16px; color: var(--soluk); }
.logo-m { width: 40px; height: 40px; color: var(--yazi); }
.logo-b { width: 64px; height: 64px; color: var(--yazi); padding: 12px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 16px; box-shadow: var(--golge); }
.harfli { font-family: var(--f-baslik); font-weight: 800; letter-spacing: .02em; background: var(--yuzey-2); border-radius: 50%; color: var(--soluk); }
.logo-k.harfli { font-size: 0.5rem; }
.logo-m.harfli { font-size: 0.85rem; }
.logo-b.harfli { font-size: 1.25rem; border-radius: 16px; }
.markalar { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 9.5rem), 1fr)); }
.markalar a { display: grid; justify-items: center; gap: 8px; padding: 18px 10px 14px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 14px; color: var(--yazi); text-align: center; box-shadow: var(--golge); transition: border-color .15s, box-shadow .15s; }
.markalar a:hover { text-decoration: none; border-color: var(--ana); box-shadow: var(--golge-2); }
.mrk-ad { font-weight: 600; font-size: 0.93rem; line-height: 1.3; }
.mrk-say { font-size: 0.8rem; color: var(--soluk); margin-top: -6px; }

.nasil-ic { display: grid; gap: 14px; grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); }
.nasil-ic > div { background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 14px; padding: 20px; display: grid; gap: 6px; align-content: start; box-shadow: var(--golge); }
.nasil-ic p { margin: 0; color: var(--soluk); font-size: 0.94rem; }
.nasil-ikon { width: 32px; height: 32px; border-radius: 50%; display: grid; place-items: center; background: var(--ana-acik); color: var(--ana); font-weight: 700; margin-bottom: 4px; }

/* model sayfası */
.iz { display: flex; flex-wrap: wrap; align-items: center; gap: 4px 8px; font-size: 0.88rem; color: var(--soluk); }
.iz a { color: var(--soluk); }
.model-bas { display: grid; grid-template-columns: minmax(0, 22rem) minmax(0, 1fr); gap: 20px 28px; align-items: center; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 20px; padding: 18px; box-shadow: var(--golge); }
.model-bas .gorsel { border-radius: 14px; }
.model-bilgi { display: grid; gap: 8px; align-content: center; }
.model-marka { display: inline-flex; align-items: center; gap: 8px; font-weight: 600; font-size: 0.92rem; color: var(--soluk); justify-self: start; }
.model-marka .logo-k { width: 20px; height: 20px; color: var(--yazi); }
.model-meta { margin: 0; display: flex; flex-wrap: wrap; color: var(--soluk); font-size: 0.95rem; }
.model-meta span + span::before { content: "·"; margin-inline: 8px; }
.ozet { list-style: none; margin: 6px 0 0; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 7.5rem)); gap: 10px; }
.ozet li { min-width: 0; padding: 10px 14px; border-radius: 12px; background: var(--yuzey-2); border: 1px solid var(--cizgi); display: grid; }
.ozet b { font-family: var(--f-baslik); font-size: 1.5rem; line-height: 1.1; font-variant-numeric: tabular-nums; }
.ozet span { font-size: 0.82rem; color: var(--soluk); }
.ozet li[data-risk="yuksek"] b { color: var(--yuksek); }
.ozet li[data-risk="orta"] b { color: var(--orta); }
.ozet li[data-risk="dusuk"] b { color: var(--dusuk); }
.ince { margin: 0; padding: 12px 16px; background: var(--ana-acik); border-radius: 12px; font-size: 0.93rem; color: var(--yazi); }
.suzgec { display: flex; flex-wrap: wrap; gap: 16px 32px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 16px; padding: 16px 18px; box-shadow: var(--golge); }
.suz-grup { border: 0; margin: 0; padding: 0; min-width: 0; display: grid; gap: 8px; align-content: start; flex: 1 1 22rem; }
.suz-km { flex: 0 1 18rem; }
.suz-grup legend { font-weight: 600; font-size: 0.82rem; letter-spacing: .04em; text-transform: uppercase; color: var(--soluk); padding: 0; margin-bottom: 8px; }
.km-girdi { display: flex; align-items: center; border: 1px solid var(--cizgi-koyu); border-radius: 10px; background: var(--yuzey); }
.km-girdi:focus-within { border-color: var(--ana); box-shadow: 0 0 0 4px color-mix(in srgb, var(--ana) 18%, transparent); }
.km-girdi input { flex: 1; min-width: 0; font: inherit; font-variant-numeric: tabular-nums; padding: 9px 12px; border: 0; background: transparent; color: var(--yazi); outline: none; }
.km-girdi span { padding-right: 12px; color: var(--soluk); }
.kutucuk { display: inline-flex; gap: 8px; align-items: center; font-size: 0.9rem; cursor: pointer; }
.kutucuk input { width: 17px; height: 17px; accent-color: var(--ana); }
.liste-bas { display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 4px 16px; margin-bottom: -14px; }
.liste-durum { margin: 0; font-size: 0.9rem; color: var(--soluk); }
.kartlar { list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }
.kart { background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 14px; padding: 16px 18px; display: grid; gap: 8px; box-shadow: var(--golge); }
.kart.km-icinde { border-color: var(--ana); box-shadow: 0 0 0 3px color-mix(in srgb, var(--ana) 18%, transparent); }
.kart-bas { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; }
.kart h3 { font-size: 1.05rem; }
.risk { flex: none; display: inline-flex; align-items: center; gap: 6px; font-size: 0.78rem; font-weight: 600; padding: 3px 10px; border-radius: 999px; white-space: nowrap; }
.risk::before { content: ""; width: 7px; height: 7px; border-radius: 50%; background: currentColor; }
.risk[data-risk="yuksek"] { color: var(--yuksek); background: var(--yuksek-z); }
.risk[data-risk="orta"] { color: var(--orta); background: var(--orta-z); }
.risk[data-risk="dusuk"] { color: var(--dusuk); background: var(--dusuk-z); }
.belirti { margin: 0; color: var(--soluk); max-width: 78ch; }
.etiketler { display: flex; flex-wrap: wrap; gap: 6px; }
.etk { font-size: 0.8rem; padding: 3px 9px; border-radius: 7px; background: var(--yuzey-2); color: var(--soluk); font-variant-numeric: tabular-nums; }
.etk-km { color: var(--yazi); font-weight: 500; }
.etk-bos { font-style: italic; }
.etk-uyar { background: var(--ana); color: var(--ana-yazi); font-weight: 600; }
.ortak-not { margin: 0; font-size: 0.84rem; color: var(--soluk); padding-top: 8px; border-top: 1px dashed var(--cizgi); }
.bos { margin: 0; padding: 20px; text-align: center; color: var(--soluk); background: var(--yuzey); border: 1px dashed var(--cizgi-koyu); border-radius: 14px; }
.bildir { margin: 0; padding: 14px 18px; background: var(--ana-acik); border-radius: 14px; }
.uyari { margin: 0; font-size: 0.85rem; color: var(--soluk); max-width: 90ch; }

/* marka sayfası */
.marka-bas, .sayfa-bas { display: flex; align-items: center; gap: 18px; }
.sayfa-bas { display: grid; gap: 6px; }
.model-bloklar { display: grid; gap: 30px; }
.model-blok { display: grid; gap: 12px; }

/* metin sayfaları ve alt şerit */
.metin { max-width: 70ch; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 16px; padding: 8px 24px 20px; }
.metin h2 { margin: 24px 0 6px; }
.alt { border-top: 1px solid var(--cizgi); background: var(--yuzey); font-size: 0.88rem; color: var(--soluk); }
.alt-ic { padding-block: 28px 36px; display: grid; gap: 10px; }
.alt p { margin: 0; }
.alt-ad { font-family: var(--f-baslik); font-weight: 800; color: var(--yazi); font-size: 1rem; margin-bottom: 4px !important; }
.alt-baglanti { display: flex; flex-wrap: wrap; gap: 6px 20px; }
.alt-baglanti a { color: var(--yazi); font-weight: 500; }
.alt-not { font-size: 0.8rem; }
.secilebilir { user-select: all; }

@media (max-width: 760px) {
  .ust-ara { order: 3; flex-basis: 100%; max-width: none; }
  .ust-nav { gap: 16px; font-size: 0.88rem; }
  .kahraman { padding: 28px 16px 24px; border-radius: 16px; }
  .ara-girdi.buyuk { padding-right: 84px; }
  .ara-dugme { padding: 0 16px; }
  .model-bas { grid-template-columns: minmax(0, 1fr); padding: 14px; }
  .kart { padding: 14px; }
  .kart-bas { flex-direction: column; gap: 6px; }
  .metin { padding: 4px 16px 16px; }
}
@media (prefers-reduced-motion: reduce) { * { transition: none !important; } }
"""


def main():
    global ONIZLEME
    argumanlar = [a for a in sys.argv[1:] if a != "--onizleme"]
    ONIZLEME = "--onizleme" in sys.argv[1:]
    hedef = Path(argumanlar[0]) if argumanlar else VARSAYILAN_HEDEF
    o = uret(hedef)
    print(f"{hedef} yazıldı: {o['model']} model sayfası, {o['marka']} marka; site haritasında (dizinlenen) {o['sayfa']} sayfa.")


if __name__ == "__main__":
    main()
