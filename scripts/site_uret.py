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
    model geneli kayıtlar nesil çapasıdır; motor kaydı yılları en çok örtüşen çapaya girer, çapasızlar örtüştükçe birleşir."""
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
            for c in capalar:
                d = ortusme(k, c["capa"])
                if d > en_d:
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

def sayfa(ayar, derinlik, baslik, aciklama, govde, kanonik, ekbas=""):
    kok = "../" * derinlik
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{kok}stil.css">
{ekbas}</head>
<body>
<header class="ust"><div class="kap ust-ic">
  <a class="logo" href="{kok}">{e(ayar['ad'])}</a>
  <nav aria-label="Ana menü"><a href="{kok}markalar/">Markalar</a><a href="{kok}hakkinda/">Hakkında</a></nav>
</div></header>
<main class="kap">
{govde}
</main>
<footer class="alt"><div class="kap">
  <p>{e(ayar['ad'])} · Bilgiler kullanıcı bildirimleri ve uzman anlatımları taranarak derlendi ve kendi ifademizle özetlendi; servis görüşü değildir.</p>
  <p><a href="{kok}hakkinda/">Hakkında ve yöntem</a> · <a href="{kok}gizlilik/">Gizlilik</a> · {iletisim_html(ayar)}</p>
</div></footer>
</body>
</html>
"""


def iletisim_html(ayar):
    if ayar.get("eposta"):
        return f'Hata bildirimi ve iletişim: <span class="secilebilir">{e(ayar["eposta"])}</span>'
    return "İletişim adresi yakında eklenecek"


def risk_rozeti(risk):
    return f'<span class="risk" data-risk="{RISK_ANAHTAR[risk]}">{e(risk)} risk</span>'


def km_metni(s):
    km = km_araligi(s.get("tahmini_km_araligi"))
    if km:
        return f'<span class="km">{km[0]:,} – {km[1]:,} km</span>'.replace(",", ".")
    return '<span class="km km-yok">Kilometre bilgisi yok</span>'


def sorun_html(s, aile):
    ek = ""
    if aile:
        ek = f'<p class="aile-not">Ortak sorun: {e(aile["ad"])} kullanan diğer modellerde de görülür.</p>'
    return f"""<li class="sorun" data-risk="{RISK_ANAHTAR[s['risk_seviyesi']]}">
  <div class="sorun-bas"><h4>{e(s['sorun_adi'])}</h4>{risk_rozeti(s['risk_seviyesi'])}</div>
  <p class="belirti">{e(s['belirtiler'])}</p>
  <div class="sorun-alt">{km_metni(s)}</div>
  {ek}
</li>"""


def bolum_html(k, grup_taban):
    arac = k["arac"]
    yil = yil_etiketi(k["yb"], k["ye"])
    if k["genel"]:
        bas = f'<h3>Genel sorunlar <span class="alt-baslik">tüm motorlar · {e(yil)}</span></h3>'
        not_ = '<p class="bolum-not">Kasa, sızdırmazlık, iç mekân, elektronik ve süspansiyon gibi motordan bağımsız sorunlar.</p>'
    else:
        ad = f'{e(k["taban"])} · ' if k["taban"] != grup_taban else ""
        bas = f'<h3>{ad}{e(arac["motor"])} <span class="alt-baslik">{e(yil)}</span></h3>'
        not_ = ""
        if k["aileler"]:
            not_ = '<p class="bolum-not">Motor / şanzıman ailesi: ' + ", ".join(e(f["ad"]) for f in k["aileler"]) + "</p>"
    liste = "\n".join(sorun_html(s, f) for s, f in k["sorunlar"])
    tur = "genel" if k["genel"] else "motor"
    return f'<section class="bolum" data-tur="{tur}">{bas}{not_}<ul class="sorunlar">{liste}</ul></section>'


UYARI = ("Bu sayfadaki bilgiler internetteki kullanıcı bildirimleri, forumlar ve uzman yazıları taranarak derlendi ve "
         "kendi ifademizle özetlendi; servis görüşü değildir. Sorunlar her araçta görülmez, kilometre aralıkları tahminidir. "
         "Satın almadan önce ekspertiz ve yetkili servis kontrolü yaptırın.")


# ---------------------------------------------------------------- üretim

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
        g["sorun_say"] = sum(len(k["sorunlar"]) for k in g["kayitlar"])
        markalar.setdefault(g["marka"], {"yol": m, "gruplar": []})["gruplar"].append(g)

    if hedef.exists():
        shutil.rmtree(hedef)
    hedef.mkdir(parents=True)
    (hedef / "stil.css").write_text(STIL, encoding="utf-8")
    sayfalar = []

    def yaz(yol, icerik):
        p = hedef / yol / "index.html" if yol else hedef / "index.html"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(icerik, encoding="utf-8")
        sayfalar.append(adres + (yol + "/" if yol else ""))

    # model sayfaları
    for g in gruplar:
        ad_tam = f"{g['marka']} {g['taban']} ({g['yil']})"
        baslik = f"{ad_tam} kronik sorunları | {ayar['ad']}"
        ilk_uc = ", ".join(s["sorun_adi"] for k in g["kayitlar"] for s, _ in k["sorunlar"][:1])[:150]
        aciklama = f"{ad_tam} için bilinen {g['sorun_say']} kronik sorun: belirtiler, risk ve tahmini kilometre. {ilk_uc}"[:300]
        motorlar = [k for k in g["kayitlar"] if not k["genel"]]
        genel = [k for k in g["kayitlar"] if k["genel"]]
        risk = {r: sum(1 for k in g["kayitlar"] for s, _ in k["sorunlar"] if s["risk_seviyesi"] == r) for r in RISK_SIRA}
        kardes = [x for x in markalar[g["marka"]]["gruplar"] if x is not g and x["taban"] == g["taban"]]
        kardes_html = ""
        if kardes:
            kardes_html = '<aside class="kardes"><h2>Diğer nesiller</h2><ul>' + "".join(
                f'<li><a href="../../{x["yol"]}/">{e(x["taban"])} {e(x["yil"])}</a></li>' for x in kardes) + "</ul></aside>"
        icindekiler = ""
        if len(g["kayitlar"]) > 1:
            icindekiler = '<nav class="icindekiler" aria-label="Bölümler"><span class="etiket">Bölümler</span>' + "".join(
                f'<a href="#b{i}">{"Genel" if k["genel"] else e(k["arac"]["motor"])}</a>' for i, k in enumerate(g["kayitlar"])) + "</nav>"
        bolumler = "\n".join(bolum_html(k, g["taban"]).replace('<section class="bolum"', f'<section id="b{i}" class="bolum"', 1)
                             for i, k in enumerate(g["kayitlar"]))
        yol_izi = f'<nav class="iz" aria-label="Konum"><a href="../../">Ana sayfa</a> › <a href="../">{e(g["marka"])}</a> › <span>{e(g["taban"])} {e(g["yil"])}</span></nav>'
        ozet = (f'<p class="ozet"><b>{g["sorun_say"]}</b> sorun · '
                + (f"genel sorunlar + {len(motorlar)} motor seçeneği" if genel else f"{len(motorlar)} motor seçeneği")
                + f' · <span class="nokta" data-risk="yuksek"></span>{risk["Yüksek"]} yüksek · <span class="nokta" data-risk="orta"></span>{risk["Orta"]} orta · <span class="nokta" data-risk="dusuk"></span>{risk["Düşük"]} düşük risk</p>')
        govde = f"""{yol_izi}
<h1>{e(g['marka'])} {e(g['taban'])} <span class="h1-yil">{e(g['yil'])}</span> kronik sorunları</h1>
{ozet}
{icindekiler}
{bolumler}
<p class="uyari">{e(UYARI)}</p>
{kardes_html}"""
        iz_ld = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": adres},
            {"@type": "ListItem", "position": 2, "name": g["marka"], "item": adres + markalar[g["marka"]]["yol"] + "/"},
            {"@type": "ListItem", "position": 3, "name": f"{g['taban']} {g['yil']}", "item": adres + g["yol"] + "/"}]}, ensure_ascii=False)
        iz_ld = iz_ld.replace("</", "<\\/")
        yaz(g["yol"], sayfa(ayar, 2, baslik, aciklama, govde, adres + g["yol"] + "/",
                            f'<script type="application/ld+json">{iz_ld}</script>\n'))

    # marka sayfaları
    for marka, b in markalar.items():
        kartlar = "".join(
            f'<li><a class="model-kart" href="../{g["yol"]}/"><span class="mk-ad">{e(g["taban"])}</span>'
            f'<span class="mk-yil">{e(g["yil"])}</span><span class="mk-say">{g["sorun_say"]} sorun</span></a></li>'
            for g in b["gruplar"])
        govde = (f'<nav class="iz" aria-label="Konum"><a href="../">Ana sayfa</a> › <span>{e(marka)}</span></nav>'
                 f'<h1>{e(marka)} kronik sorunları</h1><p class="ozet">{len(b["gruplar"])} model ve nesil</p>'
                 f'<ul class="model-liste">{kartlar}</ul>')
        yaz(b["yol"], sayfa(ayar, 1, f"{marka} kronik sorunları: model ve yıla göre | {ayar['ad']}",
                            f"{marka} modellerinin bilinen kronik sorunları, model ve üretim yılına göre.", govde, adres + b["yol"] + "/"))

    # markalar dizini
    marka_listesi = "".join(
        f'<li><a href="../{b["yol"]}/"><span>{e(m)}</span><span class="mk-say">{len(b["gruplar"])} model</span></a></li>'
        for m, b in sorted(markalar.items(), key=lambda x: x[0].lower()))
    yaz("markalar", sayfa(ayar, 1, f"Markalar | {ayar['ad']}", "Kronik sorunları listelenen tüm markalar.",
                          f'<h1>Markalar</h1><ul class="marka-liste">{marka_listesi}</ul>', adres + "markalar/"))

    # ana sayfa (arama dizini sayfaya gömülü)
    dizin = [{"a": f"{g['marka']} {g['taban']}", "y": g["yil"], "u": g["yol"] + "/", "s": g["sorun_say"],
              "m": " ".join(k["arac"]["motor"] for k in g["kayitlar"] if not k["genel"]) + " " + " ".join(k["arac"]["model"] for k in g["kayitlar"])}
             for g in gruplar]
    marka_kisa = "".join(f'<li><a href="{b["yol"]}/">{e(m)}</a></li>' for m, b in sorted(markalar.items(), key=lambda x: x[0].lower()))
    dizin_json = json.dumps(dizin, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    toplam_sorun = sum(len(a["kronik_sorunlar"]) for a in veri["arac_listesi"]) + sum(len(f["kronik_sorunlar"]) for f in veri.get("aileler", []))
    govde = f"""<section class="kahraman">
  <h1>{e(ayar['slogan'])}</h1>
  <p class="giris">{len(gruplar)} model ve nesilde {toplam_sorun} kronik sorun; motor ve şanzımana göre belirtiler, risk ve tahmini kilometre.</p>
  <label class="ara-kutu"><span class="etiket">Aracınızı arayın</span>
    <input id="ara" type="search" placeholder="Clio 4, Egea, Golf 7, 1.5 dCi…" autocomplete="off" enterkeyhint="search"></label>
  <ul id="sonuclar" class="sonuclar" aria-live="polite"></ul>
</section>
<section><h2>Markalar</h2><ul class="marka-kisa">{marka_kisa}</ul></section>
<script type="application/json" id="dizin">{dizin_json}</script>
<script>{ARA_JS}</script>"""
    yaz("", sayfa(ayar, 0, f"{ayar['ad']}: araçların kronik sorunları", f"{ayar['slogan']}. Model, yıl ve motora göre bilinen sorunlar.", govde, adres))

    # sabit sayfalar
    yaz("hakkinda", sayfa(ayar, 1, f"Hakkında ve yöntem | {ayar['ad']}", "Sorunların nasıl derlendiği ve nasıl okunacağı.", f"""
<h1>Hakkında ve yöntem</h1>
<div class="metin">
<p>{e(ayar['ad'])}, ikinci el ya da sıfır araç bakan biri için Türkiye'de yaygın araçların bilinen kronik sorunlarını tek yerde toplar.</p>
<h2>Sorunlar nasıl belirlendi?</h2>
<p>Kullanıcı şikâyetleri, sürücü forumları, servis duyuruları ve uzman yazıları tarandı. Çoğu sorun en az iki farklı kaynakta tekrar eden bildirimlere dayanır. Her sorun kendi ifademizle yazıldı; kilometre bilgisi kaynaklarda yoksa uydurulmadı.</p>
<h2>Nasıl okunur?</h2>
<ul>
<li><b>Genel sorunlar</b>: kasa, sızdırmazlık, iç mekân, elektronik ve süspansiyon gibi motordan bağımsız sorunlar.</li>
<li><b>Motora özgü sorunlar</b>: belirli bir motor ya da şanzıman sürümüne ait sorunlar. "Ortak sorun" etiketi, aynı motoru ya da şanzımanı kullanan başka modellerde de görüldüğünü belirtir; aracınızın motor kodunu ruhsattan kontrol edin.</li>
<li><b>Risk</b>: yüksek (güvenlik, motor ya da kontrol ünitesi hasarı), orta (onarım gerektiren arıza), düşük (konfor ve kozmetik). Bu bizim değerlendirmemizdir, istatistik değildir.</li>
<li><b>Kilometre</b>: sorunun bildirildiği yaklaşık aralık; kullanım ve bakıma göre değişir.</li>
</ul>
<h2>Sınırlar</h2>
<p>Burada yazan sorunların aracınızda olacağı anlamına gelmez; listede olmayan bir sorunun görülmeyeceği anlamına da gelmez. Karar vermeden önce ekspertiz ve yetkili servis kontrolü yaptırın.</p>
<h2>Hata bildirimi</h2>
<p>{iletisim_html(ayar)}.</p>
</div>""", adres + "hakkinda/"))
    yaz("gizlilik", sayfa(ayar, 1, f"Gizlilik | {ayar['ad']}", "Gizlilik bilgilendirmesi.", f"""
<h1>Gizlilik</h1>
<div class="metin">
<p>Bu site çerez kullanmaz, üyelik istemez ve ziyaretçilerden kişisel veri toplamaz. Arama kutusuna yazdıklarınız yalnızca tarayıcınızda işlenir, bize gönderilmez.</p>
<p>Barındırma hizmeti, tüm web sitelerinde olduğu gibi teknik güvenlik amacıyla standart sunucu kayıtları tutabilir.</p>
<p>{iletisim_html(ayar)}.</p>
</div>""", adres + "gizlilik/"))
    (hedef / "404.html").write_text(sayfa(ayar, 0, f"Sayfa bulunamadı | {ayar['ad']}", "Sayfa bulunamadı.",
                                          '<h1>Sayfa bulunamadı</h1><p><a href="/">Ana sayfaya dönün</a> ve aracınızı arayın.</p>', adres), encoding="utf-8")
    bugun = date.today().isoformat()
    (hedef / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                       + "".join(f"<url><loc>{e(u)}</loc><lastmod>{bugun}</lastmod></url>\n" for u in sayfalar)
                                       + "</urlset>\n", encoding="utf-8")
    (hedef / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {adres}sitemap.xml\n", encoding="utf-8")
    return {"model": len(gruplar), "marka": len(markalar), "sayfa": len(sayfalar)}


ARA_JS = r"""
(() => {
  const dizin = JSON.parse(document.getElementById("dizin").textContent);
  const katla = (s) => s.toLocaleLowerCase("tr-TR").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/ı/g, "i");
  for (const d of dizin) { d.k = katla(d.a + " " + d.y); d.t = katla(d.a + " " + d.y + " " + d.m); }
  const ara = document.getElementById("ara");
  const liste = document.getElementById("sonuclar");
  function ciz() {
    const terimler = katla(ara.value).split(/\s+/).filter(Boolean);
    liste.textContent = "";
    if (!terimler.length) return;
    const yil = terimler.find((t) => /^(19|20)\d\d$/.test(t));
    const kelimeler = terimler.filter((t) => t !== yil);
    let sonuc = dizin.filter((d) => kelimeler.every((t) => d.t.includes(t)));
    if (yil) sonuc = sonuc.filter((d) => { const m = /^(\d{4})(?:–(\d{4}|günümüz))?/.exec(d.y); const b = +m[1], s = m[2] ? (m[2] === "günümüz" ? 9999 : +m[2]) : b; return +yil >= b && +yil <= s; });
    sonuc.sort((a, b) => (b.k.startsWith(kelimeler[0] || "") - a.k.startsWith(kelimeler[0] || "")) || a.a.localeCompare(b.a, "tr"));
    for (const d of sonuc.slice(0, 30)) {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = d.u;
      a.innerHTML = "<span></span><span class=\"mk-yil\"></span><span class=\"mk-say\"></span>";
      a.children[0].textContent = d.a; a.children[1].textContent = d.y; a.children[2].textContent = d.s + " sorun";
      li.append(a); liste.append(li);
    }
    if (!sonuc.length) { const li = document.createElement("li"); li.className = "yok"; li.textContent = "Eşleşen model bulunamadı. Marka ya da model adını farklı yazmayı deneyin."; liste.append(li); }
  }
  ara.addEventListener("input", ciz);
})();
"""

STIL = r""":root {
  --bg: #eef1f4; --surface: #ffffff; --ink: #15202b; --muted: #4a5765; --line: #d5dbe2;
  --accent: #0d5868; --accent-soft: #d9ebef;
  --high: #a8231b; --high-bg: #fae6e3; --high-fill: #d64a3d;
  --mid: #7f4c00; --mid-bg: #fcefd3; --mid-fill: #e09a1f;
  --low: #22653e; --low-bg: #dff0e5; --low-fill: #3e9862;
  --font-display: "Barlow Condensed", "Roboto Condensed", "Arial Narrow", sans-serif;
  --font-body: "Barlow", "Segoe UI", Roboto, system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0e141a; --surface: #151d25; --ink: #e3e8ed; --muted: #a3afbb; --line: #25313b;
    --accent: #5dbdd1; --accent-soft: #123039;
    --high: #ff9d93; --high-bg: #3a1916; --high-fill: #e0584b;
    --mid: #f5c064; --mid-bg: #36280e; --mid-fill: #d89a2c;
    --low: #88d5a6; --low-bg: #12301e; --low-fill: #49a76d;
    color-scheme: dark;
  }
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: var(--font-body); font-size: 17px; line-height: 1.55; }
a { color: var(--accent); }
.kap { max-width: 60rem; margin-inline: auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.ust { background: var(--surface); border-bottom: 1px solid var(--line); }
.ust-ic { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px 20px; padding-block: 12px; }
.logo { font-family: var(--font-display); font-weight: 700; font-size: 1.6rem; color: var(--ink); text-decoration: none; letter-spacing: 0.01em; }
.ust nav { display: flex; gap: 18px; }
.ust nav a { text-decoration: none; font-weight: 600; }
main { padding-block: 20px 48px; }
h1, h2, h3 { font-family: var(--font-display); line-height: 1.12; text-wrap: balance; }
h1 { font-size: clamp(2rem, 5vw, 2.7rem); margin: 8px 0 10px; }
h2 { font-size: 1.6rem; margin: 32px 0 12px; }
.h1-yil { font-family: var(--font-mono); font-weight: 500; font-size: 0.6em; white-space: nowrap; }
.iz { font-size: 0.9rem; color: var(--muted); }
.iz a { color: var(--muted); }
.ozet { color: var(--muted); margin: 0 0 14px; }
.ozet b { color: var(--ink); }
.nokta { display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin: 0 4px 0 6px; vertical-align: 1px; }
.nokta[data-risk="yuksek"] { background: var(--high-fill); }
.nokta[data-risk="orta"] { background: var(--mid-fill); }
.nokta[data-risk="dusuk"] { background: var(--low-fill); }
.etiket { font-size: 0.76rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); }
.icindekiler { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 8px; margin: 6px 0 18px; }
.icindekiler a { padding: 3px 12px; border: 1px solid var(--line); border-radius: 999px; background: var(--surface); text-decoration: none; font-size: 0.92rem; }
.bolum { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 16px 18px 6px; margin-bottom: 16px; scroll-margin-top: 12px; }
.bolum[data-tur="genel"] { border-left: 4px solid var(--accent); }
.bolum h3 { margin: 0 0 4px; font-size: 1.45rem; }
.alt-baslik { font-family: var(--font-mono); font-weight: 400; font-size: 0.62em; color: var(--muted); margin-left: 6px; white-space: nowrap; }
.bolum-not { margin: 0 0 6px; font-size: 0.92rem; color: var(--muted); }
.sorunlar { list-style: none; margin: 0; padding: 0; }
.sorun { border-top: 1px solid var(--line); padding: 12px 0; }
.sorun-bas { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 10px; }
.sorun h4 { margin: 0; font-size: 1.08rem; font-weight: 600; }
.risk { font-size: 0.8rem; font-weight: 600; padding: 1px 10px; border-radius: 999px; white-space: nowrap; }
.risk[data-risk="yuksek"] { color: var(--high); background: var(--high-bg); }
.risk[data-risk="orta"] { color: var(--mid); background: var(--mid-bg); }
.risk[data-risk="dusuk"] { color: var(--low); background: var(--low-bg); }
.belirti { margin: 6px 0 4px; max-width: 70ch; }
.sorun-alt { font-size: 0.9rem; }
.km { font-family: var(--font-mono); font-size: 0.86rem; }
.km-yok { font-family: var(--font-body); color: var(--muted); }
.aile-not { margin: 4px 0 0; font-size: 0.86rem; color: var(--muted); }
.uyari { margin-top: 22px; padding: 12px 16px; border: 1px dashed var(--line); border-radius: 10px; font-size: 0.92rem; color: var(--muted); }
.kardes ul, .model-liste, .marka-liste, .marka-kisa, .sonuclar { list-style: none; padding: 0; margin: 0; }
.kardes li { display: inline-block; margin: 0 10px 8px 0; }
.model-liste, .marka-liste, .sonuclar { display: grid; gap: 8px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 17rem), 1fr)); }
.model-kart, .marka-liste a, .sonuclar a { display: flex; flex-wrap: wrap; align-items: baseline; gap: 2px 10px; padding: 12px 14px; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; text-decoration: none; color: var(--ink); }
.model-kart:hover, .marka-liste a:hover, .sonuclar a:hover { border-color: var(--accent); }
.mk-ad { font-weight: 600; }
.mk-yil { font-family: var(--font-mono); font-size: 0.86rem; }
.mk-say { font-size: 0.86rem; color: var(--muted); margin-left: auto; }
.sonuclar .yok { color: var(--muted); }
.kahraman { padding-block: 12px 8px; }
.kahraman h1 { max-width: 22ch; }
.giris { color: var(--muted); max-width: 60ch; }
.ara-kutu { display: grid; gap: 6px; margin: 18px 0 12px; max-width: 36rem; }
.ara-kutu input { font: inherit; font-size: 1.1rem; padding: 12px 14px; min-height: 48px; border: 1px solid var(--line); border-radius: 10px; background: var(--surface); color: var(--ink); width: 100%; }
.ara-kutu input:focus-visible, a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.marka-kisa { display: flex; flex-wrap: wrap; gap: 8px; }
.marka-kisa a { display: inline-block; padding: 6px 14px; border: 1px solid var(--line); border-radius: 999px; background: var(--surface); text-decoration: none; }
.metin { max-width: 68ch; }
.alt { border-top: 1px solid var(--line); padding-block: 18px 28px; font-size: 0.9rem; color: var(--muted); }
.alt p { margin: 4px 0; }
.secilebilir { user-select: all; }
"""


def main():
    hedef = Path(sys.argv[1]) if len(sys.argv) > 1 else VARSAYILAN_HEDEF
    o = uret(hedef)
    print(f"{hedef} yazıldı: {o['model']} model sayfası, {o['marka']} marka, toplam {o['sayfa']} sayfa.")


if __name__ == "__main__":
    main()
