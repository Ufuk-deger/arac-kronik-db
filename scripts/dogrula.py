#!/usr/bin/env python3
"""data/araclar.json dosyasını şemaya ve tutarlılık kurallarına göre doğrular.

Yalnızca standart kütüphaneyi kullanır. Kullanım:

    python3 scripts/dogrula.py [dosya_yolu]
"""

import json
import re
import sys
from pathlib import Path

VARSAYILAN_DOSYA = Path(__file__).resolve().parent.parent / "data" / "araclar.json"

ARAC_ALANLARI = ("marka", "model", "motor", "kronik_sorunlar")
SORUN_ALANLARI = (
    "sorun_adi",
    "etkilenen_parca",
    "belirtiler",
    "tahmini_km_araligi",
    "risk_seviyesi",
)
RISK_SEVIYELERI = ("Düşük", "Orta", "Yüksek")
KM_DESENI = re.compile(r"^(\d{1,3}(?:\.\d{3})*) - (\d{1,3}(?:\.\d{3})*) km$")


def km_degeri(metin):
    return int(metin.replace(".", ""))


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


def sorunu_dogrula(sorun, konum, hatalar):
    if not alanlari_kontrol_et(sorun, SORUN_ALANLARI, konum, hatalar):
        return
    for alan in SORUN_ALANLARI:
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


def dogrula(veri):
    hatalar = []
    if not alanlari_kontrol_et(veri, ("arac_listesi",), "kök", hatalar):
        return hatalar
    araclar = veri["arac_listesi"]
    if not isinstance(araclar, list):
        return hatalar + ["arac_listesi: dizi olmalı"]

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
            sorunu_dogrula(sorun, f"{konum}.kronik_sorunlar[{j}]", hatalar)
    return hatalar


def main():
    dosya = Path(sys.argv[1]) if len(sys.argv) > 1 else VARSAYILAN_DOSYA
    try:
        veri = json.loads(dosya.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as hata:
        print(f"HATA: {dosya} okunamadı: {hata}", file=sys.stderr)
        return 1

    hatalar = dogrula(veri)
    if hatalar:
        for hata in hatalar:
            print(f"HATA: {hata}", file=sys.stderr)
        print(f"{len(hatalar)} hata bulundu.", file=sys.stderr)
        return 1

    araclar = veri["arac_listesi"]
    sorun_sayisi = sum(len(arac["kronik_sorunlar"]) for arac in araclar)
    print(f"Geçerli: {len(araclar)} araç, {sorun_sayisi} kronik sorun.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
