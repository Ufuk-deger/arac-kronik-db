#!/usr/bin/env python3
"""data/araclar.json dosyasını şemaya, kaynak kurallarına ve tutarlılık kurallarına göre doğrular.

Yalnızca standart kütüphaneyi kullanır. Kullanım:

    python3 scripts/dogrula.py [dosya_yolu]

Kaynak alan adları data/kaynaklar.json dosyasındaki kayıtla eşleştirilir.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

KOK = Path(__file__).resolve().parent.parent
VARSAYILAN_DOSYA = KOK / "data" / "araclar.json"
KAYIT_DOSYASI = KOK / "data" / "kaynaklar.json"

ARAC_ALANLARI = ("marka", "model", "motor", "kronik_sorunlar")
SORUN_ALANLARI = (
    "sorun_adi",
    "etkilenen_parca",
    "belirtiler",
    "tahmini_km_araligi",
    "risk_seviyesi",
    "kaynaklar",
)
RISK_SEVIYELERI = ("Düşük", "Orta", "Yüksek")
KM_DESENI = re.compile(r"^(\d{1,3}(?:\.\d{3})*) - (\d{1,3}(?:\.\d{3})*) km$")
EN_AZ_ALAN_ADI = 2
IKI_PARCALI_UZANTILAR = {"co.uk", "org.uk", "com.au", "com.tr", "org.tr"}


def km_degeri(metin):
    return int(metin.replace(".", ""))


def alan_adi(url):
    """URL'nin kayıt defterindeki alan adını verir (forum.donanimhaber.com -> donanimhaber.com)."""
    parcalar = (urlparse(url).hostname or "").lower().split(".")
    if len(parcalar) >= 3 and ".".join(parcalar[-2:]) in IKI_PARCALI_UZANTILAR:
        return ".".join(parcalar[-3:])
    return ".".join(parcalar[-2:])


def alanlari_kontrol_et(nesne, beklenen, konum, hatalar):
    if not isinstance(nesne, dict):
        hatalar.append(f"{konum}: nesne olmalı")
        return False
    eksik = [alan for alan in beklenen if alan not in nesne]
    fazla = [alan for alan in nesne if alan not in beklenen]
    if eksik:
        hatalar.append(f"{konum}: eksik alan(lar): {', '.join(eksik)}")
    if fazla:
        hatalar.append(f"{konum}: tanımsız alan(lar): {', '.join(fazla)}")
    return not eksik


def metin_mi(deger, konum, hatalar):
    if not isinstance(deger, str) or not deger.strip():
        hatalar.append(f"{konum}: boş olmayan metin olmalı")
        return False
    return True


def kaynaklari_dogrula(kaynaklar, konum, kayit, hatalar):
    """Sorunun kaynak listesini denetler ve ayrı alan adlarının sayısını döndürür."""
    if not isinstance(kaynaklar, list):
        hatalar.append(f"{konum}: dizi olmalı")
        return 0
    alanlar = set()
    dayanakli = False
    for url in kaynaklar:
        if not isinstance(url, str) or not url.startswith("https://"):
            hatalar.append(f"{konum}: '{url}' https:// ile başlayan bir adres olmalı")
            continue
        site = alan_adi(url)
        if site not in kayit["siteler"]:
            hatalar.append(f"{konum}: '{site}' data/kaynaklar.json içinde tanımlı değil")
            continue
        alanlar.add(site)
        if kayit["siteler"][site]["tur"] in kayit["dayanak_turleri"]:
            dayanakli = True
    if len(set(kaynaklar)) != len(kaynaklar):
        hatalar.append(f"{konum}: aynı adres birden fazla kez yazılmış")
    if len(alanlar) < EN_AZ_ALAN_ADI:
        hatalar.append(
            f"{konum}: en az {EN_AZ_ALAN_ADI} farklı site gerekir, {len(alanlar)} bulundu"
        )
    elif not dayanakli:
        hatalar.append(
            f"{konum}: kaynaklardan en az biri resmî belge, forum, şikâyet, anket veya haber türünde olmalı"
        )
    return len(alanlar)


def sorunu_dogrula(sorun, konum, kayit, hatalar, sayilar):
    if not alanlari_kontrol_et(sorun, SORUN_ALANLARI, konum, hatalar):
        return
    for alan in SORUN_ALANLARI[:-1]:
        metin_mi(sorun[alan], f"{konum}.{alan}", hatalar)

    km = sorun["tahmini_km_araligi"]
    eslesme = KM_DESENI.match(km) if isinstance(km, str) else None
    if not eslesme:
        hatalar.append(
            f"{konum}.tahmini_km_araligi: '{km}' biçimi '80.000 - 150.000 km' gibi olmalı"
        )
    elif km_degeri(eslesme.group(1)) > km_degeri(eslesme.group(2)):
        hatalar.append(f"{konum}.tahmini_km_araligi: alt sınır üst sınırdan büyük")

    if sorun["risk_seviyesi"] not in RISK_SEVIYELERI:
        hatalar.append(
            f"{konum}.risk_seviyesi: '{sorun['risk_seviyesi']}' geçersiz, "
            f"beklenen: {'/'.join(RISK_SEVIYELERI)}"
        )

    site_sayisi = kaynaklari_dogrula(sorun["kaynaklar"], f"{konum}.kaynaklar", kayit, hatalar)
    sayilar.append(site_sayisi)


def dogrula(veri, kayit):
    hatalar = []
    sayilar = []
    if not alanlari_kontrol_et(veri, ("arac_listesi",), "kök", hatalar):
        return hatalar, sayilar
    araclar = veri["arac_listesi"]
    if not isinstance(araclar, list):
        return hatalar + ["arac_listesi: dizi olmalı"], sayilar

    gorulenler = set()
    for i, arac in enumerate(araclar):
        konum = f"arac_listesi[{i}]"
        if not alanlari_kontrol_et(arac, ARAC_ALANLARI, konum, hatalar):
            continue
        for alan in ("marka", "model", "motor"):
            metin_mi(arac[alan], f"{konum}.{alan}", hatalar)

        anahtar = (arac["marka"], arac["model"], arac["motor"])
        if anahtar in gorulenler:
            hatalar.append(f"{konum}: aynı marka/model/motor birden fazla kez tanımlı")
        gorulenler.add(anahtar)

        sorunlar = arac["kronik_sorunlar"]
        if not isinstance(sorunlar, list) or not sorunlar:
            hatalar.append(f"{konum}.kronik_sorunlar: en az bir sorun içeren dizi olmalı")
            continue
        for j, sorun in enumerate(sorunlar):
            sorunu_dogrula(sorun, f"{konum}.kronik_sorunlar[{j}]", kayit, hatalar, sayilar)
    return hatalar, sayilar


def main():
    dosya = Path(sys.argv[1]) if len(sys.argv) > 1 else VARSAYILAN_DOSYA
    try:
        veri = json.loads(dosya.read_text(encoding="utf-8"))
        kayit = json.loads(KAYIT_DOSYASI.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as hata:
        print(f"HATA: dosya okunamadı: {hata}", file=sys.stderr)
        return 1

    hatalar, sayilar = dogrula(veri, kayit)
    if hatalar:
        for hata in hatalar:
            print(f"HATA: {hata}", file=sys.stderr)
        print(f"{len(hatalar)} hata bulundu.", file=sys.stderr)
        return 1

    araclar = veri["arac_listesi"]
    kullanilan = {alan_adi(u) for a in araclar for s in a["kronik_sorunlar"] for u in s["kaynaklar"]}
    sinirli = sum(1 for n in sayilar if n == EN_AZ_ALAN_ADI)
    print(
        f"Geçerli: {len(araclar)} araç, {len(sayilar)} kronik sorun, "
        f"{len(kullanilan)} farklı kaynak sitesi."
    )
    print(f"{sinirli} sorun yalnızca {EN_AZ_ALAN_ADI} siteyle destekleniyor (sınırlı doğrulama).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
