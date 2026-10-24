#!/usr/bin/env python3
"""KAYNAKLAR.md dosyasını data/kaynaklar.json ve data/araclar.json içeriğinden üretir.

Kullanım:

    python3 scripts/kaynaklar_md_uret.py
"""

import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dogrula import KAYIT_DOSYASI, KOK, VARSAYILAN_DOSYA, alan_adi  # noqa: E402

HEDEF = KOK / "KAYNAKLAR.md"

GRUPLAR = [
    ("Resmî belgeler ve dava haberleri", ("resmi", "dava-haberi")),
    ("Forumlar", ("forum",)),
    ("Şikâyet platformları, sahip anketleri ve derlemeler", ("sikayet", "anket", "toplayici")),
    ("Editör yazıları ve haberler", ("editoryal", "haber")),
    ("Parça ve atölye rehberleri", ("parca-atolye",)),
]

DENENEN_ADRESLER = [
    "otopark.com",
    "andcetin.com",
    "carcomplaints.com",
    "honestjohn.co.uk",
    "araclo.com",
    "forum.donanimhaber.com",
    "static.nhtsa.gov",
    "planeterenault.com",
    "en.wikipedia.org",
]

EK_KAYNAKLAR = [
    ("KBA (Almanya Federal Motorlu Taşıtlar Dairesi) geri çağırma listesi", "Avrupa'daki resmî geri çağırmalar."),
    ("ADAC arıza istatistikleri", "Marka ve model bazında yolda kalma verisi (Almanya)."),
    ("TÜV Report", "Alman muayene sonuçlarına dayalı arıza oranları."),
    ("Which? ve What Car? güvenilirlik anketleri", "Birleşik Krallık'ta sahip anketleri."),
    ("Fabrika servis bültenleri (TSB) ve VIN ile kampanya sorgusu", "Markanın yetkili servisinden veya NHTSA sayfasından alınabilir."),
]


def kullanim_say(veri):
    sayac = Counter()
    sorunlar = [s for a in veri["arac_listesi"] for s in a["kronik_sorunlar"]]
    sorunlar += [s for f in veri.get("aileler", []) for s in f["kronik_sorunlar"]]
    for sorun in sorunlar:
        for site in {alan_adi(url) for url in sorun["kaynaklar"]}:
            sayac[site] += 1
    return sayac


def tablo(satirlar, kullanim):
    cikti = ["| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |", "| --- | --- | --- | ---: | --- |"]
    for alan, bilgi in satirlar:
        adet = kullanim.get(alan, 0)
        adet_metni = str(adet) if adet else "yalnızca rapor"
        cikti.append(
            f"| [{bilgi['ad']}]({bilgi['ana_sayfa']}) | {bilgi['ulke']} | {bilgi['guven']} | {adet_metni} | {bilgi['not']} |"
        )
    return cikti


def uret():
    kayit = json.loads(KAYIT_DOSYASI.read_text(encoding="utf-8"))
    veri = json.loads(VARSAYILAN_DOSYA.read_text(encoding="utf-8"))
    kullanim = kullanim_say(veri)
    siteler = kayit["siteler"]
    turler = kayit["turler"]

    satir = [
        "# Kaynaklar",
        "",
        "Bu dosya `scripts/kaynaklar_md_uret.py` ile `data/kaynaklar.json` ve `data/araclar.json` içeriğinden üretilir. "
        "Elle düzenlemeyin; siteyi `data/kaynaklar.json` içinde değiştirip betiği yeniden çalıştırın.",
        "",
        "## Kural",
        "",
        "`data/araclar.json` içindeki her kronik sorun (araç kayıtlarındakiler ve motor/şanzıman ailelerinin ortak sorunları), `kaynaklar` alanında **en az iki farklı sitenin** sayfasıyla desteklenir. "
        "Kaynaklardan en az biri deneyime ya da resmî belgeye dayanmalıdır (forum, şikâyet, anket, dava haberi, haber veya resmî belge). "
        "Yalnızca blog, parça satıcısı ya da derleme sitesi olan sorunlar veritabanına alınmaz. "
        "`python3 scripts/dogrula.py` bu kuralı denetler.",
        "",
        "## Nasıl okunmalı",
        "",
        "Her sayfa yalnızca bir ipucudur. Bir forum yazısı tek bir aracı, bir şikâyet tek bir sürücüyü anlatır ve oran göstermez. "
        "Birden fazla bağımsız sitede aynı sorunun görülmesi güven verir; yine de kilometre aralıkları tahmindir ve "
        "satın alma ya da onarım kararından önce aracın yetkili serviste kontrol edilmesi gerekir.",
        "",
        "| Tür | Anlamı |",
        "| --- | --- |",
    ]
    for ad, aciklama in turler.items():
        satir.append(f"| `{ad}` | {aciklama} |")
    satir += [
        "",
        "Güvenilirlik sütunu sitenin türüne ve düzenine göre verilmiş bir değerlendirmedir: `yüksek` resmî belge veya köklü yayın, "
        "`orta` kullanıcı deneyimi içeren kalabalık kaynak, `düşük` ticari ya da zayıf kaynaklı site demektir. "
        "`düşük` kaynaklar tek başına yeterli sayılmaz.",
        "",
        "## Doğrulama yöntemi ve sınırları",
        "",
        "Bu çalışmayı yürüten ortamda dış sitelere doğrudan erişim kapalıydı. Aşağıdaki adreslere sayfa açma denemesi başarısız oldu "
        "(`WebFetch` alan adını çözemedi, `curl` proxy tarafından `403` ile reddedildi):",
        "",
    ]
    satir += [f"- `{adres}`" for adres in DENENEN_ADRESLER]
    satir += [
        "",
        "Bu yüzden kaynaklar web araması sonuçlarından toplandı. Her bağlantı, arama sonucunda göründüğü sayfa başlığı ve özetine göre "
        "ilgili soruna eşlendi; sayfaların tamamı tek tek okunmadı. Bir bağlantıda iddia bulamazsanız `DOGRULAMA_RAPORU.md` içindeki "
        "bilgiyi ve ilgili sorunun diğer kaynaklarını kontrol edin, bulamadığınız maddeyi bildirin. "
        "Ortama ağ erişimi verilirse sayfalar doğrudan okunarak doğrulama derinleştirilebilir.",
        "",
        "İlk istekte \"Mehmet Çetin'in sitesi\" diye anılan kaynak için `andcetin.com` (\"And Mehmet Çetin\") kullanıldı. "
        "Kastedilen site farklıysa `data/kaynaklar.json` güncellenmelidir.",
        "",
        f"Toplam {len(kullanim)} farklı site, {sum(len(a['kronik_sorunlar']) for a in veri['arac_listesi'])} sorun için kullanıldı.",
        "",
    ]

    turkce = sorted(
        ((a, b) for a, b in siteler.items() if b["ulke"] == "TR"),
        key=lambda x: (-kullanim.get(x[0], 0), x[1]["ad"]),
    )
    satir += ["## Türkçe kaynaklar", ""]
    satir += tablo(turkce, kullanim)
    satir.append("")

    satir += ["## Yurtdışı kaynaklar", ""]
    for baslik, turlar in GRUPLAR:
        grup = sorted(
            ((a, b) for a, b in siteler.items() if b["ulke"] != "TR" and b["tur"] in turlar),
            key=lambda x: (-kullanim.get(x[0], 0), x[1]["ad"]),
        )
        if not grup:
            continue
        satir += [f"### {baslik}", ""]
        satir += tablo(grup, kullanim)
        satir.append("")

    satir += [
        "## Denenmeye değer ek kaynaklar",
        "",
        "Bu çalışmada kullanılmadı ve erişilip doğrulanmadı. İleride eklenebilecek kaynak türleri:",
        "",
    ]
    satir += [f"- **{ad}**: {neden}" for ad, neden in EK_KAYNAKLAR]
    satir.append("")
    return "\n".join(satir)


def main():
    HEDEF.write_text(uret(), encoding="utf-8")
    print(f"{HEDEF.name} yazıldı.")


if __name__ == "__main__":
    main()
