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
# Yerleşim: üstte her sayfada arama; ana sayfada arama + marka seçici + çok bakılanlar; model sayfasında özet çubuğu,
# motor ve kilometre süzgeci ve risk sırasına dizilmiş tek sorun listesi (her kartta hangi motorda görüldüğü ve km sayacı).

KM_OLCEK = 250_000          # km sayacının sağ ucu
ONIZLEME = False            # True: bağlantılar klasör yerine açıkça index.html'e gider (dosya olarak gezilebilen önizleme)


def adres_ek(yol):
    """Göreli klasör bağlantısı; önizlemede sonuna index.html eklenir."""
    if not ONIZLEME:
        return yol
    if yol == "" or yol.endswith("/"):
        return yol + "index.html"
    return yol


def sayfa(ayar, derinlik, baslik, aciklama, govde, kanonik, ekbas="", sinif="", ust_ara=True):
    kok = "../" * derinlik
    ara_html = ""
    if ust_ara:
        ara_html = ('<div class="ust-ara" role="search"><label class="gizli" for="ust-ara-kutu">Araç ara</label>'
                    '<input id="ust-ara-kutu" class="ara-girdi" type="search" placeholder="Araç ara: Clio 5, Egea 2018…" '
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="{kok}stil.css">
{ekbas}</head>
<body class="{sinif}" data-kok="{kok}" data-onizleme="{'1' if ONIZLEME else ''}">
<header class="ust"><div class="kap ust-ic">
  <a class="logo" href="{adres_ek(kok) or './'}"><span class="logo-lamba" aria-hidden="true"></span>{e(ayar['ad'])}</a>
  {ara_html}
  <nav class="ust-nav" aria-label="Ana menü"><a href="{adres_ek(kok + 'markalar/')}">Markalar</a><a href="{adres_ek(kok + 'hakkinda/')}">Nasıl okunur</a></nav>
</div></header>
<main class="kap">
{govde}
</main>
<footer class="alt"><div class="kap alt-ic">
  <p class="alt-ad">{e(ayar['ad'])}</p>
  <p>Bilgiler kullanıcı bildirimleri ve uzman anlatımları taranarak derlendi ve kendi ifademizle özetlendi; servis görüşü değildir.</p>
  <p><a href="{adres_ek(kok + 'hakkinda/')}">Hakkında ve yöntem</a> · <a href="{adres_ek(kok + 'gizlilik/')}">Gizlilik</a> · {iletisim_html(ayar)}</p>
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


def risk_rozeti(risk):
    return f'<span class="risk" data-risk="{RISK_ANAHTAR[risk]}"><span class="lamba" aria-hidden="true"></span>{e(risk)} risk</span>'


def km_sayaci(km):
    """Kilometre sayacı: 0-250.000 km çizgisi üzerinde sorunun bildirildiği aralık."""
    if not km:
        return '<div class="km km-yok">Kilometre bilgisi yok</div>'
    a, b = km
    sol = min(a, KM_OLCEK) / KM_OLCEK * 100
    gen = max(1.5, (min(b, KM_OLCEK) - min(a, KM_OLCEK)) / KM_OLCEK * 100)
    tasma = ' <span class="km-tasma">(250.000 km üstüne uzanıyor)</span>' if b > KM_OLCEK else ""
    return (f'<div class="km"><div class="km-yazi"><span class="km-sayi">{nokta_say(a)} – {nokta_say(b)}</span> km{tasma}</div>'
            f'<div class="km-cizgi" aria-hidden="true"><span class="km-aralik" style="left:{sol:.1f}%;width:{gen:.1f}%"></span>'
            f'<span class="km-isaret" hidden></span></div>'
            f'<div class="km-olcek" aria-hidden="true"><span>0</span><span>50</span><span>100</span><span>150</span><span>200</span><span>250 bin</span></div></div>')


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
        yer = '<span class="yer yer-genel">Tüm motorlar</span>'
    else:
        yer = "".join(f'<span class="yer">{e(motor_adi(motorlar[int(t[1:])], grup_taban))}</span>' for t in c["etiketler"])
    ortak = ""
    if c["aile"] is not None:
        ortak = (f'<p class="ortak-not"><span class="ortak-etiket">Ortak sorun</span> {e(c["aile"]["ad"])} kullanan '
                 f'başka modellerde de görülür.</p>')
    veri = (f'data-risk="{RISK_ANAHTAR[s["risk_seviyesi"]]}" data-yer="{" ".join(c["etiketler"])}"'
            + (f' data-kma="{km[0]}" data-kmb="{km[1]}"' if km else ""))
    return f"""<li class="kart" {veri}>
  <div class="kart-ust">{risk_rozeti(s['risk_seviyesi'])}<span class="km-uyar" hidden>Bu kilometrede</span></div>
  <h3>{e(s['sorun_adi'])}</h3>
  <p class="belirti">{e(s['belirtiler'])}</p>
  <div class="kart-alt"><div class="yerler">{yer}</div>{km_sayaci(km)}</div>
  {ortak}
</li>"""


def risk_cubugu(kartlar):
    say = {r: sum(1 for c in kartlar if c["s"]["risk_seviyesi"] == r) for r in RISK_SIRA}
    top = max(1, len(kartlar))
    parcalar = "".join(f'<span class="rc-parca" data-risk="{RISK_ANAHTAR[r]}" style="flex-grow:{n}"></span>' for r, n in say.items() if n)
    etiket = "".join(f'<li><span class="lamba" data-risk="{RISK_ANAHTAR[r]}" aria-hidden="true"></span><b>{n}</b> {r.lower()} risk</li>'
                     for r, n in say.items())
    return (f'<div class="risk-ozet"><div class="rc" role="img" aria-label="{len(kartlar)} sorun: '
            f'{say["Yüksek"]} yüksek, {say["Orta"]} orta, {say["Düşük"]} düşük risk">{parcalar}</div>'
            f'<ul class="rc-etiket">{etiket}</ul></div>') if top else ""


def suzgec_html(motorlar, grup_taban):
    motor_dugme = ""
    if len(motorlar) > 1:
        dugmeler = '<button type="button" class="cip" data-motor="" aria-pressed="true">Tümü</button>' + "".join(
            f'<button type="button" class="cip" data-motor="m{i}" aria-pressed="false">{e(motor_adi(k, grup_taban))}</button>'
            for i, k in enumerate(motorlar))
        motor_dugme = (f'<fieldset class="suz-grup"><legend>Motorunuz</legend><div class="cipler">{dugmeler}</div>'
                       f'<p class="suz-not">Motor kodu ruhsatta ve motor etiketinde yazar. Tüm motorlar için geçerli sorunlar her zaman gösterilir.</p></fieldset>')
    return f"""<form class="suzgec" data-suzgec hidden>
  {motor_dugme}
  <fieldset class="suz-grup suz-km"><legend>Kilometreniz</legend>
    <div class="km-girdi"><input id="km-kutu" type="text" inputmode="numeric" placeholder="ör. 120.000" autocomplete="off" aria-describedby="km-not"><span>km</span></div>
    <label class="kutucuk"><input id="km-yalniz" type="checkbox"> Yalnızca bu kilometreye uyanlar</label>
    <p class="suz-not" id="km-not">Girdiğiniz kilometrenin içine düştüğü sorunlar işaretlenir.</p>
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
        marka, taban = ad.split("|")
        aday = [g for g in gruplar if g["marka"] == marka and (g["taban"] == taban or aile_adi(g["taban"]) == taban)]
        if aday:
            secim.append(max(aday, key=lambda g: (g["ozgu_say"] > 0, g["sorun_say"], g["yb"])))
    return secim


def model_karti(g, kok):
    return (f'<a class="mkart" href="{adres_ek(kok + g["yol"] + "/")}"><span class="mkart-marka">{e(g["marka"])}</span>'
            f'<span class="mkart-ad">{e(g["taban"])}</span><span class="mkart-yil">{e(g["yil"])}</span>'
            f'<span class="mkart-say">{g["sorun_say"]} sorun</span></a>')


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
            kardes_html = ('<section class="kardes"><h2>Diğer nesiller ve kardeş modeller</h2><div class="mkartlar">'
                           + "".join(model_karti(x, "../../") for x in sorted(kardes, key=lambda x: -x["yb"])) + "</div></section>")
        motor_say = len(motorlar)
        meta = []
        if motor_say:
            meta.append(f"<span>{motor_say} motor seçeneği</span>")
        meta.append(f"<span>{g['sorun_say']} kronik sorun</span>")
        yol_izi = (f'<nav class="iz" aria-label="Konum"><a href="{adres_ek("../../")}">Ana sayfa</a><span aria-hidden="true">/</span>'
                   f'<a href="{adres_ek("../")}">{e(g["marka"])}</a><span aria-hidden="true">/</span><span>{e(g["taban"])} {e(g["yil"])}</span></nav>')
        liste = "\n".join(kart_html(c, motorlar, g["taban"]) for c in kartlar)
        govde = f"""{yol_izi}
<header class="model-bas">
  <p class="model-marka">{e(g['marka'])}</p>
  <h1>{e(g['taban'])} <span class="h1-yil">{e(g['yil'])}</span></h1>
  <p class="model-meta">{''.join(meta)}</p>
</header>
{risk_cubugu(kartlar)}
{ince_notu(g)}
{suzgec_html(motorlar, g['taban'])}
<p class="liste-durum" data-durum aria-live="polite">{g['sorun_say']} sorun, riske göre sıralı</p>
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
        bloklar = ""
        for kok_ad in sorted(aileler, key=dogal):
            nesiller = sorted(aileler[kok_ad], key=lambda g: -g["yb"])
            satirlar = "".join(
                f'<li><a class="nesil" href="{adres_ek("../" + g["yol"] + "/")}"><span class="nesil-ad">{e(g["taban"])}</span>'
                f'<span class="nesil-yil">{e(g["yil"])}</span><span class="nesil-say">{g["sorun_say"]} sorun</span>'
                f'<span class="nesil-ok" aria-hidden="true">›</span></a></li>' for g in nesiller)
            bloklar += f'<section class="model-blok"><h2>{e(kok_ad)}</h2><ul class="nesiller">{satirlar}</ul></section>'
        govde = (f'<nav class="iz" aria-label="Konum"><a href="{adres_ek("../")}">Ana sayfa</a><span aria-hidden="true">/</span><span>{e(marka)}</span></nav>'
                 f'<header class="model-bas"><p class="model-marka">Marka</p><h1>{e(marka)}</h1>'
                 f'<p class="model-meta"><span>{len(b["gruplar"])} model ve nesil</span><span>{sum(g["sorun_say"] for g in b["gruplar"])} sorun kaydı</span></p></header>'
                 f'<div class="model-bloklar">{bloklar}</div>')
        yaz(b["yol"], sayfa(ayar, 1, f"{marka} kronik sorunları: model ve yıla göre | {ayar['ad']}",
                            f"{marka} modellerinin bilinen kronik sorunları, model ve üretim yılına göre.", govde, adres + b["yol"] + "/"))

    # markalar dizini
    marka_listesi = "".join(
        f'<li><a href="{adres_ek("../" + b["yol"] + "/")}"><span class="mrk-ad">{e(m)}</span><span class="mrk-say">{len(b["gruplar"])} model</span></a></li>'
        for m, b in sorted(markalar.items(), key=lambda x: x[0].lower()))
    yaz("markalar", sayfa(ayar, 1, f"Markalar | {ayar['ad']}", "Kronik sorunları listelenen tüm markalar.",
                          f'<header class="model-bas"><h1>Markalar</h1><p class="model-meta"><span>{len(markalar)} marka</span><span>{len(gruplar)} model ve nesil</span></p></header>'
                          f'<ul class="markalar">{marka_listesi}</ul>', adres + "markalar/"))

    # ana sayfa
    toplam_sorun = sum(len(a["kronik_sorunlar"]) for a in veri["arac_listesi"]) + sum(len(f["kronik_sorunlar"]) for f in veri.get("aileler", []))
    pop = populer_gruplar(ayar, gruplar)
    pop_html = ""
    if pop:
        pop_html = f'<section class="blok"><h2>Çok bakılanlar</h2><div class="mkartlar">{"".join(model_karti(g, "") for g in pop)}</div></section>'
    marka_sec = "".join(f'<option value="{e(m)}">{e(m)}</option>' for m in sorted(markalar, key=str.lower))
    sayac = "".join(f'<span class="tek">{c}</span>' if c.isdigit() else f'<span class="ayr">{c}</span>' for c in nokta_say(toplam_sorun))
    govde = f"""<div class="ana-ust"><section class="kahraman">
  <h1>Almadan önce <span class="vurgu">ustaya sor.</span></h1>
  <p class="giris">Türkiye'de yaygın araçların bilinen kronik sorunları: hangi motorda, kaç kilometrede, ne kadar ciddi.</p>
  <div class="ana-ara" role="search">
    <label for="ana-ara-kutu" class="ana-ara-etiket">Aracınızın marka ve modelini yazın</label>
    <input id="ana-ara-kutu" class="ara-girdi buyuk" type="search" placeholder="Clio 5, Egea 2018, Golf 7, 1.5 dCi…" autocomplete="off" enterkeyhint="search" data-ara data-genis>
    <ul class="oneriler genis" data-oneriler hidden></ul>
  </div>
  <div class="sayac-satir"><div class="sayac" aria-label="{nokta_say(toplam_sorun)} kronik sorun">{sayac}</div><p>kronik sorun · {len(gruplar)} model ve nesil · {len(markalar)} marka</p></div>
</section>
<section class="secici" data-secici hidden>
  <h2>Ya da markadan seçin</h2>
  <label class="gizli" for="marka-sec">Marka</label>
  <select id="marka-sec" class="marka-sec"><option value="">Marka seçin</option>{marka_sec}</select>
  <div class="secici-liste" data-secici-liste><p class="suz-not">Marka seçince modelleri ve nesilleri burada listelenir.</p></div>
</section></div>
{pop_html}
<section class="blok nasil">
  <h2>Nasıl okunur?</h2>
  <div class="nasil-ic">
    <div><span class="lamba buyuk" data-risk="yuksek" aria-hidden="true"></span><h3>Risk</h3><p>Kırmızı: güvenlik ya da motor hasarı. Sarı: onarım gerektiren arıza. Yeşil: konfor ve kozmetik.</p></div>
    <div><span class="mini-sayac" aria-hidden="true"><span class="tek">8</span><span class="tek">0</span><span class="ayr">.</span><span class="tek">0</span><span class="tek">0</span><span class="tek">0</span></span><h3>Kilometre</h3><p>Sorunun bildirildiği yaklaşık aralık. Kendi kilometrenizi girin, o aralığa düşenler işaretlensin.</p></div>
    <div><span class="motor-ikon" aria-hidden="true">1.5 dCi</span><h3>Motor</h3><p>Sorunların çoğu belirli bir motora ya da şanzımana aittir. Model sayfasında motorunuzu seçin.</p></div>
  </div>
</section>
<section class="blok"><h2>Tüm markalar</h2><ul class="markalar kisa">{"".join(f'<li><a href="{adres_ek(b["yol"] + "/")}"><span class="mrk-ad">{e(m)}</span><span class="mrk-say">{len(b["gruplar"])}</span></a></li>' for m, b in sorted(markalar.items(), key=lambda x: x[0].lower()))}</ul></section>"""
    yaz("", sayfa(ayar, 0, f"{ayar['ad']}: araçların kronik sorunları", f"{ayar['slogan']}. Model, yıl ve motora göre bilinen sorunlar.", govde, adres, "", "s-ana", ust_ara=False))

    # sabit sayfalar
    yaz("hakkinda", sayfa(ayar, 1, f"Hakkında ve yöntem | {ayar['ad']}", "Sorunların nasıl derlendiği ve nasıl okunacağı.", f"""
<header class="model-bas"><h1>Hakkında ve yöntem</h1></header>
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
<h2>Hata bildirimi</h2>
<p>{iletisim_html(ayar)}.</p>
</div>""", adres + "hakkinda/"))
    yaz("gizlilik", sayfa(ayar, 1, f"Gizlilik | {ayar['ad']}", "Gizlilik bilgilendirmesi.", f"""
<header class="model-bas"><h1>Gizlilik</h1></header>
<div class="metin">
<p>Bu site çerez kullanmaz, üyelik istemez ve ziyaretçilerden kişisel veri toplamaz. Arama kutusuna ve kilometre alanına yazdıklarınız yalnızca tarayıcınızda işlenir, bize gönderilmez.</p>
<p>Barındırma hizmeti, tüm web sitelerinde olduğu gibi teknik güvenlik amacıyla standart sunucu kayıtları tutabilir.</p>
<p>{iletisim_html(ayar)}.</p>
</div>""", adres + "gizlilik/"))
    (hedef / "404.html").write_text(sayfa(ayar, 0, f"Sayfa bulunamadı | {ayar['ad']}", "Sayfa bulunamadı.",
                                          '<header class="model-bas"><h1>Sayfa bulunamadı</h1></header><p>Aradığınız sayfa taşınmış ya da hiç olmamış olabilir. Yukarıdaki kutudan aracınızı arayın.</p>', adres), encoding="utf-8")
    if ONIZLEME:
        for p in hedef.rglob("*.html"):
            p.write_text(p.read_text(encoding="utf-8").replace('href="/"', 'href="index.html"'), encoding="utf-8")
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
    const liste = girdi.parentElement.querySelector("[data-oneriler]");
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
    girdi.addEventListener("input", ciz);
    girdi.addEventListener("focus", () => { if (girdi.value.trim()) ciz(); });
    girdi.addEventListener("keydown", (ev) => {
      const n = liste.querySelectorAll("a").length;
      if (ev.key === "ArrowDown" && n) { secili = (secili + 1) % n; isaretle(); ev.preventDefault(); }
      else if (ev.key === "ArrowUp" && n) { secili = (secili - 1 + n) % n; isaretle(); ev.preventDefault(); }
      else if (ev.key === "Enter" && sonuc.length) { location.href = git(sonuc[Math.max(0, secili)].u); ev.preventDefault(); }
      else if (ev.key === "Escape") { liste.hidden = true; }
    });
    document.addEventListener("click", (ev) => { if (!girdi.parentElement.contains(ev.target)) liste.hidden = true; });
  }

  // ---- ana sayfa: markadan seç
  const secici = document.querySelector("[data-secici]");
  if (secici) {
    secici.hidden = false;
    const sec = secici.querySelector("select"), hedef = secici.querySelector("[data-secici-liste]");
    sec.addEventListener("change", () => {
      hedef.textContent = "";
      for (const d of dizin.filter((x) => x.b === sec.value).sort((a, b) => a.a.localeCompare(b.a, "tr", { numeric: true }) || b.yb - a.yb)) {
        const a = document.createElement("a"); a.className = "mkart"; a.href = git(d.u);
        a.innerHTML = '<span class="mkart-ad"></span><span class="mkart-yil"></span><span class="mkart-say"></span>';
        a.children[0].textContent = d.a.slice(d.b.length + 1); a.children[1].textContent = d.y; a.children[2].textContent = d.s + " sorun";
        hedef.append(a);
      }
    });
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
        const a = +k.dataset.kma, b = +k.dataset.kmb, kmVar = "kma" in k.dataset;
        const kmUyar = km !== null && kmVar && km >= a && km <= b;
        k.querySelector(".km-uyar").hidden = !kmUyar;
        k.classList.toggle("km-icinde", kmUyar);
        const isaret = k.querySelector(".km-isaret");
        if (isaret) { isaret.hidden = km === null; if (km !== null) isaret.style.left = Math.min(100, km / 2500) + "%"; }
        const goster = motorUyar && (!yalniz.checked || km === null || kmUyar);
        k.hidden = !goster; if (goster) gorunen++; if (goster && kmUyar) uyan++;
      }
      durum.textContent = gorunen + " sorun gösteriliyor" + (km !== null ? " · " + uyan + " tanesi " + km.toLocaleString("tr-TR") + " km'ye uyuyor" : ", riske göre sıralı");
      bos.hidden = gorunen > 0;
    }
    for (const b of suz.querySelectorAll("[data-motor]")) {
      b.addEventListener("click", () => {
        motor = b.dataset.motor;
        suz.querySelectorAll("[data-motor]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
        uygula();
      });
    }
    kmKutu.addEventListener("input", () => {
      const n = kmOku(); if (n !== null) { kmKutu.value = n.toLocaleString("tr-TR"); }
      uygula();
    });
    yalniz.addEventListener("change", uygula);
    suz.addEventListener("submit", (ev) => ev.preventDefault());
  }
})();
"""

STIL = r"""/* Bilmiş Usta: gösterge paneli lambaları ve usta sarısı. Yerleşim: üst şerit + arama, tek sütun içerik (en fazla 68rem). */
:root {
  --zemin: #f3f4f1; --yuzey: #ffffff; --yuzey-2: #e9ebe6; --murekkep: #14181b; --soluk: #565e64; --cizgi: #d9ddd6;
  --usta: #f2b200; --usta-yazi: #7a5800; --usta-zemin: #fff4cc;
  --yuksek: #b3261e; --yuksek-z: #fbe4e1; --yuksek-l: #e0402f;
  --orta: #8f5a00; --orta-z: #fff0d1; --orta-l: #eea021;
  --dusuk: #23693f; --dusuk-z: #e1f1e6; --dusuk-l: #35a061;
  --golge: 0 1px 2px rgba(20, 24, 27, .06), 0 4px 16px rgba(20, 24, 27, .06);
  --ust-zemin: #14181b; --ust-yazi: #f3f4f1;
  --f-baslik: "Archivo", "Arial Narrow", "Helvetica Neue", Arial, sans-serif;
  --f-govde: "Inter", "Segoe UI", Roboto, system-ui, sans-serif;
  --f-sayi: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --zemin: #101315; --yuzey: #181c1f; --yuzey-2: #22272b; --murekkep: #eceee9; --soluk: #a5acb1; --cizgi: #2c3236;
    --usta: #f2b200; --usta-yazi: #f5c94a; --usta-zemin: #2e2508;
    --yuksek: #ff9a8f; --yuksek-z: #3a1714; --yuksek-l: #f05a48;
    --orta: #f7c35f; --orta-z: #33260b; --orta-l: #eea021;
    --dusuk: #86d6a5; --dusuk-z: #112c1c; --dusuk-l: #3fb36d;
    --golge: 0 1px 2px rgba(0, 0, 0, .3);
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --zemin: #101315; --yuzey: #181c1f; --yuzey-2: #22272b; --murekkep: #eceee9; --soluk: #a5acb1; --cizgi: #2c3236;
  --usta: #f2b200; --usta-yazi: #f5c94a; --usta-zemin: #2e2508;
  --yuksek: #ff9a8f; --yuksek-z: #3a1714; --yuksek-l: #f05a48;
  --orta: #f7c35f; --orta-z: #33260b; --orta-l: #eea021;
  --dusuk: #86d6a5; --dusuk-z: #112c1c; --dusuk-l: #3fb36d;
  --golge: 0 1px 2px rgba(0, 0, 0, .3);
  color-scheme: dark;
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--zemin); color: var(--murekkep); font-family: var(--f-govde); font-size: 17px; line-height: 1.6; }
[hidden] { display: none !important; }
a { color: inherit; text-decoration-color: color-mix(in srgb, currentColor 35%, transparent); text-underline-offset: 3px; }
a:hover { text-decoration-color: currentColor; }
:focus-visible { outline: 3px solid var(--usta); outline-offset: 2px; border-radius: 4px; }
.gizli { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.kap { max-width: 68rem; margin-inline: auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
h1, h2, h3 { font-family: var(--f-baslik); line-height: 1.1; text-wrap: balance; margin: 0; }
h1 { font-size: clamp(2.1rem, 6vw, 3.4rem); font-weight: 800; font-stretch: 112%; letter-spacing: -0.01em; }
h2 { font-size: clamp(1.35rem, 3vw, 1.7rem); font-weight: 750; font-stretch: 108%; }
h3 { font-size: 1.15rem; font-weight: 700; }

/* üst şerit */
.ust { background: var(--ust-zemin); color: var(--ust-yazi); position: sticky; top: env(safe-area-inset-top, 0px); z-index: 20; }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 21; background: var(--ust-zemin); }
.ust-ic { display: flex; align-items: center; gap: 12px 20px; padding-block: 10px; flex-wrap: wrap; }
.logo { display: inline-flex; align-items: center; gap: 10px; font-family: var(--f-baslik); font-weight: 800; font-stretch: 115%; font-size: 1.35rem; text-decoration: none; color: inherit; white-space: nowrap; }
.logo-lamba { width: 14px; height: 14px; border-radius: 50%; background: var(--usta); box-shadow: 0 0 0 3px color-mix(in srgb, var(--usta) 30%, transparent), 0 0 14px var(--usta); }
.ust-ara { position: relative; flex: 1 1 18rem; min-width: 0; max-width: 30rem; }
.ust-nav { display: flex; gap: 18px; margin-left: auto; font-weight: 600; font-size: 0.95rem; }
.ust-nav a { text-decoration: none; opacity: .85; }
.ust-nav a:hover { opacity: 1; }
.ara-girdi { width: 100%; font: inherit; font-size: 1rem; padding: 9px 14px; min-height: 42px; border-radius: 10px; border: 1px solid transparent; background: color-mix(in srgb, var(--ust-yazi) 12%, transparent); color: inherit; }
.ust .ara-girdi::placeholder { color: color-mix(in srgb, var(--ust-yazi) 60%, transparent); }
.ust .ara-girdi:focus { background: var(--yuzey); color: var(--murekkep); outline: none; border-color: var(--usta); }
.oneriler { position: absolute; left: 0; right: 0; top: calc(100% + 6px); list-style: none; margin: 0; padding: 6px; background: var(--yuzey); color: var(--murekkep); border: 1px solid var(--cizgi); border-radius: 12px; box-shadow: var(--golge), 0 12px 32px rgba(0,0,0,.14); max-height: min(70vh, 30rem); overflow-y: auto; z-index: 30; }
.oneriler a { display: grid; grid-template-columns: 1fr auto; gap: 0 12px; padding: 9px 12px; border-radius: 8px; text-decoration: none; }
.oneriler a:hover, .oneriler a.aktif { background: var(--usta-zemin); }
.o-ad { font-weight: 600; }
.o-yil { font-family: var(--f-sayi); font-size: 0.85rem; color: var(--soluk); grid-column: 1; }
.o-say { grid-row: 1 / span 2; grid-column: 2; align-self: center; font-size: 0.85rem; color: var(--soluk); }
.oneri-yok { padding: 10px 12px; color: var(--soluk); }

main { padding-block: 24px 56px; display: grid; gap: 20px; }
main > * { min-width: 0; }

/* ana sayfa */
.kahraman { padding-block: 28px 8px; display: grid; gap: 16px; }
.kahraman h1 { font-size: clamp(2.4rem, 8vw, 4.6rem); max-width: 14ch; }
.vurgu { background: linear-gradient(transparent 62%, var(--usta) 62%, var(--usta) 92%, transparent 92%); padding-inline: 2px; }
.giris { font-size: 1.15rem; color: var(--soluk); max-width: 52ch; margin: 0; }
.ana-ara { position: relative; max-width: 44rem; display: grid; gap: 8px; margin-top: 4px; }
.ana-ara-etiket { font-weight: 600; font-size: 0.95rem; }
.ara-girdi.buyuk { font-size: 1.2rem; min-height: 60px; padding: 14px 18px; background: var(--yuzey); border: 2px solid var(--murekkep); color: var(--murekkep); box-shadow: 4px 4px 0 var(--usta); }
.ara-girdi.buyuk:focus { outline: none; box-shadow: 4px 4px 0 var(--usta), 0 0 0 4px color-mix(in srgb, var(--usta) 35%, transparent); }
.sayac-satir { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; color: var(--soluk); margin-top: 6px; }
.sayac-satir p { margin: 0; }
.sayac, .mini-sayac { display: inline-flex; gap: 2px; font-family: var(--f-sayi); font-weight: 500; }
.sayac .tek, .mini-sayac .tek { background: var(--murekkep); color: var(--zemin); padding: 2px 6px; border-radius: 3px; font-size: 1.05rem; }
.sayac .ayr, .mini-sayac .ayr { align-self: end; padding-inline: 1px; color: var(--murekkep); }
.blok { display: grid; gap: 14px; padding-top: 12px; }
.ana-ust { display: grid; gap: 24px 40px; grid-template-columns: minmax(0, 1fr); align-items: start; }
@media (min-width: 960px) { .ana-ust { grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); } .secici { margin-top: 40px; } }
.secici { background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 14px; padding: 18px; display: grid; gap: 12px; }
.secici-liste { display: grid; gap: 0; max-height: 26rem; overflow-y: auto; }
.secici-liste .mkart { border: 0; border-top: 1px solid var(--cizgi); border-radius: 0; padding: 10px 4px; grid-template-columns: minmax(0, 1fr) auto; }
.secici-liste .mkart:hover { transform: none; background: var(--usta-zemin); }
.secici-liste .mkart-ad { font-size: 1.05rem; }
.secici-liste .mkart-yil { grid-row: 2; }
.secici-liste .mkart-say { grid-column: 2; grid-row: 1 / span 2; align-self: center; margin: 0; }
.marka-sec { width: 100%; font: inherit; padding: 10px 14px; min-height: 46px; border-radius: 10px; border: 1px solid var(--cizgi); background: var(--yuzey); color: var(--murekkep); max-width: 22rem; }
.mkartlar { display: grid; gap: 10px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 14rem), 1fr)); }
.mkart { display: grid; gap: 2px; padding: 14px 16px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 12px; text-decoration: none; transition: border-color .15s, transform .15s; }
.mkart:hover { border-color: var(--murekkep); transform: translateY(-1px); }
.mkart-marka { font-size: 0.8rem; font-weight: 600; letter-spacing: .05em; text-transform: uppercase; color: var(--soluk); }
.mkart-ad { font-family: var(--f-baslik); font-weight: 750; font-stretch: 108%; font-size: 1.2rem; line-height: 1.2; }
.mkart-yil { font-family: var(--f-sayi); font-size: 0.85rem; color: var(--soluk); }
.mkart-say { font-size: 0.85rem; font-weight: 600; margin-top: 4px; }
.nasil-ic { display: grid; gap: 14px; grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr)); }
.nasil-ic > div { background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 12px; padding: 18px; display: grid; gap: 8px; align-content: start; }
.nasil-ic p { margin: 0; color: var(--soluk); font-size: 0.97rem; }
.motor-ikon { justify-self: start; font-family: var(--f-sayi); font-size: 0.85rem; border: 2px solid var(--murekkep); border-radius: 6px; padding: 1px 8px; }
.markalar { list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 12rem), 1fr)); }
.markalar a { display: flex; justify-content: space-between; align-items: baseline; gap: 10px; padding: 12px 14px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 10px; text-decoration: none; font-weight: 600; }
.markalar a:hover { border-color: var(--murekkep); }
.mrk-say { font-family: var(--f-sayi); font-size: 0.85rem; color: var(--soluk); font-weight: 500; }

/* lambalar ve risk */
.lamba { display: inline-block; width: 10px; height: 10px; border-radius: 50%; flex: none; background: var(--soluk); }
.lamba.buyuk { width: 18px; height: 18px; }
[data-risk="yuksek"] .lamba, .lamba[data-risk="yuksek"] { background: var(--yuksek-l); box-shadow: 0 0 8px color-mix(in srgb, var(--yuksek-l) 60%, transparent); }
[data-risk="orta"] .lamba, .lamba[data-risk="orta"] { background: var(--orta-l); box-shadow: 0 0 8px color-mix(in srgb, var(--orta-l) 55%, transparent); }
[data-risk="dusuk"] .lamba, .lamba[data-risk="dusuk"] { background: var(--dusuk-l); }
.risk { display: inline-flex; align-items: center; gap: 7px; font-size: 0.82rem; font-weight: 700; letter-spacing: .02em; padding: 3px 10px 3px 8px; border-radius: 999px; white-space: nowrap; }
.risk[data-risk="yuksek"] { color: var(--yuksek); background: var(--yuksek-z); }
.risk[data-risk="orta"] { color: var(--orta); background: var(--orta-z); }
.risk[data-risk="dusuk"] { color: var(--dusuk); background: var(--dusuk-z); }

/* model sayfası */
.iz { display: flex; flex-wrap: wrap; gap: 4px 8px; font-size: 0.9rem; color: var(--soluk); }
.model-bas { display: grid; gap: 6px; }
.model-marka { margin: 0; font-weight: 700; font-size: 0.85rem; letter-spacing: .08em; text-transform: uppercase; color: var(--usta-yazi); }
.h1-yil { font-family: var(--f-sayi); font-weight: 500; font-size: 0.42em; letter-spacing: 0; color: var(--soluk); white-space: nowrap; vertical-align: middle; }
.model-meta { margin: 0; display: flex; flex-wrap: wrap; gap: 4px 0; color: var(--soluk); }
.model-meta span + span::before { content: "·"; margin-inline: 10px; }
.model-meta:empty { display: none; }
.risk-ozet { display: grid; gap: 10px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 12px; padding: 16px; }
.rc { display: flex; height: 12px; border-radius: 6px; overflow: hidden; gap: 3px; }
.rc-parca { flex-basis: 0; min-width: 6px; }
.rc-parca[data-risk="yuksek"] { background: var(--yuksek-l); }
.rc-parca[data-risk="orta"] { background: var(--orta-l); }
.rc-parca[data-risk="dusuk"] { background: var(--dusuk-l); }
.rc-etiket { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px 20px; font-size: 0.95rem; }
.rc-etiket li { display: inline-flex; align-items: center; gap: 8px; }
.ince { margin: 0; padding: 12px 16px; background: var(--usta-zemin); border-radius: 10px; font-size: 0.95rem; }
.suzgec { display: grid; gap: 14px 28px; grid-template-columns: minmax(0, 2fr) minmax(0, 1fr); background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 12px; padding: 16px 18px; }
.suzgec:not(:has(.suz-grup + .suz-grup)) { grid-template-columns: minmax(0, 28rem); }
.suz-grup { border: 0; margin: 0; padding: 0; min-width: 0; display: grid; gap: 8px; align-content: start; }
.suz-grup legend { font-weight: 700; font-size: 0.95rem; padding: 0; margin-bottom: 8px; }
.cipler { display: flex; flex-wrap: wrap; gap: 8px; }
.cip { font: inherit; font-size: 0.92rem; padding: 7px 14px; min-height: 38px; border-radius: 999px; border: 1px solid var(--cizgi); background: var(--zemin); color: var(--murekkep); cursor: pointer; text-align: left; }
.cip:hover { border-color: var(--murekkep); }
.cip[aria-pressed="true"] { background: var(--murekkep); color: var(--zemin); border-color: var(--murekkep); }
.suz-not { margin: 0; font-size: 0.85rem; color: var(--soluk); }
.km-girdi { display: flex; align-items: center; border: 1px solid var(--cizgi); border-radius: 10px; background: var(--zemin); max-width: 16rem; }
.km-girdi:focus-within { border-color: var(--murekkep); }
.km-girdi input { flex: 1; min-width: 0; font-family: var(--f-sayi); font-size: 1.05rem; padding: 9px 12px; border: 0; background: transparent; color: var(--murekkep); outline: none; }
.km-girdi span { padding-right: 12px; color: var(--soluk); }
.kutucuk { display: inline-flex; gap: 8px; align-items: center; font-size: 0.92rem; cursor: pointer; }
.kutucuk input { width: 18px; height: 18px; accent-color: var(--murekkep); }
.liste-durum { margin: 0; font-size: 0.92rem; color: var(--soluk); }
.kartlar { list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }
.kart { background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 14px; padding: 18px 20px; display: grid; gap: 10px; }
.kart.km-icinde { border-color: var(--usta); box-shadow: 0 0 0 2px var(--usta); }
.kart-ust { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.km-uyar { font-size: 0.8rem; font-weight: 700; padding: 3px 10px; border-radius: 999px; background: var(--usta); color: #1c1600; }
.kart h3 { font-size: clamp(1.1rem, 2.4vw, 1.3rem); }
.belirti { margin: 0; max-width: 72ch; }
.kart-alt { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 18rem); gap: 10px 24px; align-items: end; padding-top: 10px; border-top: 1px solid var(--cizgi); }
.yerler { display: flex; flex-wrap: wrap; gap: 6px; }
.yer { font-size: 0.82rem; font-family: var(--f-sayi); padding: 2px 8px; border-radius: 6px; background: var(--yuzey-2); }
.yer-genel { font-family: var(--f-govde); font-weight: 600; }
.km { display: grid; gap: 4px; }
.km-yazi { font-size: 0.88rem; color: var(--soluk); }
.km-sayi { font-family: var(--f-sayi); color: var(--murekkep); font-weight: 500; }
.km-tasma { font-size: 0.8rem; }
.km-cizgi { position: relative; height: 8px; border-radius: 4px; background: repeating-linear-gradient(90deg, var(--cizgi) 0 1px, var(--yuzey-2) 1px 20%); }
.km-aralik { position: absolute; top: 0; bottom: 0; border-radius: 4px; background: var(--murekkep); }
.kart[data-risk="yuksek"] .km-aralik { background: var(--yuksek-l); }
.kart[data-risk="orta"] .km-aralik { background: var(--orta-l); }
.kart[data-risk="dusuk"] .km-aralik { background: var(--dusuk-l); }
.km-isaret { position: absolute; top: -4px; bottom: -4px; width: 3px; margin-left: -1px; background: var(--murekkep); border-radius: 2px; }
.km-olcek { display: flex; justify-content: space-between; font-family: var(--f-sayi); font-size: 0.7rem; color: var(--soluk); }
.km-yok { font-size: 0.88rem; color: var(--soluk); }
.ortak-not { margin: 0; font-size: 0.88rem; color: var(--soluk); }
.ortak-etiket { font-weight: 700; color: var(--murekkep); margin-right: 4px; }
.bos { margin: 0; padding: 18px; text-align: center; color: var(--soluk); background: var(--yuzey); border: 1px dashed var(--cizgi); border-radius: 12px; }
.bildir { margin: 0; padding: 14px 18px; background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 12px; }
.uyari { margin: 0; font-size: 0.88rem; color: var(--soluk); max-width: 80ch; }
.kardes { display: grid; gap: 12px; padding-top: 8px; }

/* marka sayfası */
.model-bloklar { display: grid; gap: 14px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 20rem), 1fr)); align-items: start; }
.model-blok { background: var(--yuzey); border: 1px solid var(--cizgi); border-radius: 12px; padding: 14px 16px; display: grid; gap: 8px; }
.model-blok h2 { font-size: 1.35rem; }
.nesiller { list-style: none; margin: 0; padding: 0; }
.nesil { display: grid; grid-template-columns: minmax(0, 1fr) auto auto; gap: 0 12px; align-items: baseline; padding: 9px 4px; border-top: 1px solid var(--cizgi); text-decoration: none; }
.nesil:hover .nesil-ad { text-decoration: underline; }
.nesil-ad { font-weight: 600; }
.nesil-yil { font-family: var(--f-sayi); font-size: 0.85rem; color: var(--soluk); grid-row: 2; }
.nesil-say { font-size: 0.85rem; color: var(--soluk); grid-row: 1 / span 2; align-self: center; }
.nesil-ok { grid-row: 1 / span 2; align-self: center; font-size: 1.3rem; color: var(--soluk); }

/* metin sayfaları ve alt şerit */
.metin { max-width: 68ch; }
.metin h2 { margin: 28px 0 8px; }
.alt { border-top: 1px solid var(--cizgi); background: var(--yuzey); font-size: 0.9rem; color: var(--soluk); }
.alt-ic { padding-block: 24px 32px; }
.alt p { margin: 4px 0; }
.alt-ad { font-family: var(--f-baslik); font-weight: 800; font-stretch: 112%; color: var(--murekkep); font-size: 1.05rem; }
.secilebilir { user-select: all; }

@media (max-width: 720px) {
  body { font-size: 16px; }
  .ust-ara { order: 3; flex-basis: 100%; max-width: none; }
  .ust-ic { gap: 10px 14px; }
  .ust-nav { gap: 14px; font-size: 0.88rem; }
  .logo { font-size: 1.2rem; }
  .suzgec { grid-template-columns: minmax(0, 1fr); }
  .kart { padding: 16px; }
  .kart-alt { grid-template-columns: minmax(0, 1fr); }
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
