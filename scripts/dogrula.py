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

ARAC_ALANLARI = ("marka", "model", "motor", "uretim_yillari", "kronik_sorunlar")
ISTEGE_BAGLI_ARAC_ALANLARI = ("aileler",)
AILE_ALANLARI = ("id", "ad", "tur", "aciklama", "kronik_sorunlar")
AILE_TURLERI = ("motor", "sanziman", "sistem")
ACIKLAMA_UZUNLUK_UST = 500
KIMLIK_DESENI = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SORUN_ALANLARI = (
    "sorun_adi",
    "etkilenen_parca",
    "belirtiler",
    "tahmini_km_araligi",
    "risk_seviyesi",
    "kaynaklar",
)
ISTEGE_BAGLI_SORUN_ALANLARI = ("donem_kirilimi", "detay")
DETAY_ALANLARI = ("neden", "teshis", "cozum", "maliyet", "onlem")
DETAY_UZUNLUK_UST = 800
KIRILIM_ALANLARI = ("baslangic", "bitis", "durum", "not")
RISK_SEVIYELERI = ("Düşük", "Orta", "Yüksek")
KIRILIM_DURUMLARI = ("Yaygın", "Görülebilir", "Seyrek")
YIL_ARALIGI = (1990, 2100)
KM_DESENI = re.compile(r"^(\d{1,3}(?:\.\d{3})*) - (\d{1,3}(?:\.\d{3})*) km$")
EN_AZ_ALAN_ADI = 2
IKI_PARCALI_UZANTILAR = {"co.uk", "org.uk", "com.au", "co.nz", "com.tr", "org.tr"}


def km_degeri(metin):
    return int(metin.replace(".", ""))


def alan_adi(url):
    """URL'nin kayıt defterindeki alan adını verir (forum.donanimhaber.com -> donanimhaber.com)."""
    parcalar = (urlparse(url).hostname or "").lower().split(".")
    if len(parcalar) >= 3 and ".".join(parcalar[-2:]) in IKI_PARCALI_UZANTILAR:
        return ".".join(parcalar[-3:])
    return ".".join(parcalar[-2:])


def alanlari_kontrol_et(nesne, beklenen, konum, hatalar, istege_bagli=()):
    if not isinstance(nesne, dict):
        hatalar.append(f"{konum}: nesne olmalı")
        return False
    eksik = [alan for alan in beklenen if alan not in nesne and alan not in istege_bagli]
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


def yil_mi(deger, konum, hatalar, bos_olabilir=False):
    if deger is None and bos_olabilir:
        return True
    if isinstance(deger, bool) or not isinstance(deger, int) or not YIL_ARALIGI[0] <= deger <= YIL_ARALIGI[1]:
        hatalar.append(f"{konum}: {YIL_ARALIGI[0]}-{YIL_ARALIGI[1]} arası bir yıl olmalı")
        return False
    return True


def yil_araligini_dogrula(nesne, konum, hatalar):
    """baslangic/bitis çiftini denetler; geçerliyse (baslangic, bitis) döndürür."""
    if not alanlari_kontrol_et(nesne, ("baslangic", "bitis"), konum, hatalar):
        return None
    b_ok = yil_mi(nesne["baslangic"], f"{konum}.baslangic", hatalar)
    e_ok = yil_mi(nesne["bitis"], f"{konum}.bitis", hatalar, bos_olabilir=True)
    if b_ok and e_ok:
        if nesne["bitis"] is not None and nesne["bitis"] < nesne["baslangic"]:
            hatalar.append(f"{konum}: bitiş yılı başlangıç yılından küçük")
            return None
        return nesne["baslangic"], nesne["bitis"]
    return None


def kesisir_mi(a, b):
    """İki (baslangic, bitis|None) aralığı kesişiyor mu?"""
    a_bitis = a[1] if a[1] is not None else YIL_ARALIGI[1]
    b_bitis = b[1] if b[1] is not None else YIL_ARALIGI[1]
    return a[0] <= b_bitis and b[0] <= a_bitis


def kirilimi_dogrula(kirilimlar, konum, arac_yillari, hatalar):
    if not isinstance(kirilimlar, list) or not kirilimlar:
        hatalar.append(f"{konum}: en az bir dönem içeren dizi olmalı")
        return
    onceki = None
    for i, k in enumerate(kirilimlar):
        yer = f"{konum}[{i}]"
        if not alanlari_kontrol_et(k, KIRILIM_ALANLARI, yer, hatalar):
            continue
        aralik = yil_araligini_dogrula({"baslangic": k["baslangic"], "bitis": k["bitis"]}, yer, hatalar)
        if k["durum"] not in KIRILIM_DURUMLARI:
            hatalar.append(f"{yer}.durum: '{k['durum']}' geçersiz, beklenen: {'/'.join(KIRILIM_DURUMLARI)}")
        metin_mi(k["not"], f"{yer}.not", hatalar)
        if not aralik:
            continue
        if onceki is not None:
            if aralik[0] <= (onceki[1] if onceki[1] is not None else YIL_ARALIGI[1]):
                hatalar.append(f"{yer}: dönemler yıla göre sıralı ve birbiriyle çakışmayan olmalı")
        onceki = aralik
        if arac_yillari and not kesisir_mi(aralik, arac_yillari):
            hatalar.append(f"{yer}: dönem, aracın üretim yılları dışında kalıyor")


def detayi_dogrula(detay, konum, hatalar):
    if not isinstance(detay, dict) or not detay:
        hatalar.append(f"{konum}: en az bir alan içeren nesne olmalı")
        return
    fazla = [alan for alan in detay if alan not in DETAY_ALANLARI]
    if fazla:
        hatalar.append(f"{konum}: tanımsız alan(lar): {', '.join(fazla)}")
    for alan in DETAY_ALANLARI:
        if alan in detay and metin_mi(detay[alan], f"{konum}.{alan}", hatalar):
            if len(detay[alan]) > DETAY_UZUNLUK_UST:
                hatalar.append(f"{konum}.{alan}: en fazla {DETAY_UZUNLUK_UST} karakter olmalı")


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


def sorunu_dogrula(sorun, konum, kayit, hatalar, sayilar, arac_yillari=None, ek_alanlar=(), zorunlu_ek_alanlar=()):
    """ek_alanlar: bu bağlamda izin verilen ek alanlar (aile sorunlarında 'id' zorunlu, araç sorunlarında 'aile_sorunu' isteğe bağlı)."""
    isteyerek = ISTEGE_BAGLI_SORUN_ALANLARI + tuple(a for a in ek_alanlar if a not in zorunlu_ek_alanlar)
    if not alanlari_kontrol_et(sorun, SORUN_ALANLARI + ISTEGE_BAGLI_SORUN_ALANLARI + ek_alanlar, konum, hatalar, istege_bagli=isteyerek):
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
    if "donem_kirilimi" in sorun:
        kirilimi_dogrula(sorun["donem_kirilimi"], f"{konum}.donem_kirilimi", arac_yillari, hatalar)
    if "detay" in sorun:
        detayi_dogrula(sorun["detay"], f"{konum}.detay", hatalar)


def aileleri_dogrula(aileler, kayit, hatalar, sayilar):
    """Aile listesini denetler; geçerli 'aile_id/sorun_id' bağlantılarının kümesini döndürür."""
    if not isinstance(aileler, list):
        hatalar.append("aileler: dizi olmalı")
        return set(), set()
    aile_idleri = set()
    sorun_baglari = set()
    for i, aile in enumerate(aileler):
        konum = f"aileler[{i}]"
        if not alanlari_kontrol_et(aile, AILE_ALANLARI, konum, hatalar):
            continue
        kimlik = aile["id"]
        if not isinstance(kimlik, str) or not KIMLIK_DESENI.match(kimlik):
            hatalar.append(f"{konum}.id: küçük harf, rakam ve tire içeren bir kimlik olmalı")
        elif kimlik in aile_idleri:
            hatalar.append(f"{konum}.id: '{kimlik}' birden fazla kez tanımlı")
        else:
            aile_idleri.add(kimlik)
        metin_mi(aile["ad"], f"{konum}.ad", hatalar)
        if aile["tur"] not in AILE_TURLERI:
            hatalar.append(f"{konum}.tur: '{aile['tur']}' geçersiz, beklenen: {'/'.join(AILE_TURLERI)}")
        if metin_mi(aile["aciklama"], f"{konum}.aciklama", hatalar) and len(aile["aciklama"]) > ACIKLAMA_UZUNLUK_UST:
            hatalar.append(f"{konum}.aciklama: en fazla {ACIKLAMA_UZUNLUK_UST} karakter olmalı")
        sorunlar = aile["kronik_sorunlar"]
        if not isinstance(sorunlar, list) or not sorunlar:
            hatalar.append(f"{konum}.kronik_sorunlar: en az bir sorun içeren dizi olmalı")
            continue
        sorun_idleri = set()
        for j, sorun in enumerate(sorunlar):
            yer = f"{konum}.kronik_sorunlar[{j}]"
            sorunu_dogrula(sorun, yer, kayit, hatalar, sayilar, None, ek_alanlar=("id",), zorunlu_ek_alanlar=("id",))
            sid = sorun.get("id") if isinstance(sorun, dict) else None
            if sid is None:
                continue
            if not isinstance(sid, str) or not KIMLIK_DESENI.match(sid):
                hatalar.append(f"{yer}.id: küçük harf, rakam ve tire içeren bir kimlik olmalı")
            elif sid in sorun_idleri:
                hatalar.append(f"{yer}.id: '{sid}' bu ailede birden fazla kez tanımlı")
            else:
                sorun_idleri.add(sid)
                if isinstance(kimlik, str):
                    sorun_baglari.add(f"{kimlik}/{sid}")
    return aile_idleri, sorun_baglari


def dogrula(veri, kayit):
    hatalar = []
    sayilar = []
    if not alanlari_kontrol_et(veri, ("arac_listesi", "aileler"), "kök", hatalar, istege_bagli=("aileler",)):
        return hatalar, sayilar
    araclar = veri["arac_listesi"]
    if not isinstance(araclar, list):
        return hatalar + ["arac_listesi: dizi olmalı"], sayilar

    aile_idleri, sorun_baglari = aileleri_dogrula(veri.get("aileler", []), kayit, hatalar, sayilar)
    kullanilan_aileler = set()

    gorulenler = set()
    for i, arac in enumerate(araclar):
        konum = f"arac_listesi[{i}]"
        if not alanlari_kontrol_et(arac, ARAC_ALANLARI + ISTEGE_BAGLI_ARAC_ALANLARI, konum, hatalar, istege_bagli=ISTEGE_BAGLI_ARAC_ALANLARI):
            continue
        for alan in ("marka", "model", "motor"):
            metin_mi(arac[alan], f"{konum}.{alan}", hatalar)
        arac_yillari = yil_araligini_dogrula(arac["uretim_yillari"], f"{konum}.uretim_yillari", hatalar)

        anahtar = (arac["marka"], arac["model"], arac["motor"])
        if anahtar in gorulenler:
            hatalar.append(f"{konum}: aynı marka/model/motor birden fazla kez tanımlı")
        gorulenler.add(anahtar)

        aile_listesi = arac.get("aileler", [])
        if "aileler" in arac and (not isinstance(aile_listesi, list) or not aile_listesi):
            hatalar.append(f"{konum}.aileler: en az bir aile kimliği içeren dizi olmalı")
            aile_listesi = []
        for kimlik in aile_listesi:
            if kimlik not in aile_idleri:
                hatalar.append(f"{konum}.aileler: '{kimlik}' aileler içinde tanımlı değil")
            elif aile_listesi.count(kimlik) > 1:
                hatalar.append(f"{konum}.aileler: '{kimlik}' birden fazla kez yazılmış")
            kullanilan_aileler.add(kimlik)

        sorunlar = arac["kronik_sorunlar"]
        if not isinstance(sorunlar, list) or (not sorunlar and not aile_listesi):
            hatalar.append(f"{konum}.kronik_sorunlar: en az bir sorun ya da en az bir aile gerekir")
            continue
        for j, sorun in enumerate(sorunlar):
            yer = f"{konum}.kronik_sorunlar[{j}]"
            sorunu_dogrula(sorun, yer, kayit, hatalar, sayilar, arac_yillari, ek_alanlar=("aile_sorunu",))
            bag = sorun.get("aile_sorunu") if isinstance(sorun, dict) else None
            if bag is None:
                continue
            if bag not in sorun_baglari:
                hatalar.append(f"{yer}.aile_sorunu: '{bag}' tanımlı bir aile sorunu değil")
            elif bag.split("/")[0] not in aile_listesi:
                hatalar.append(f"{yer}.aile_sorunu: '{bag.split('/')[0]}' bu aracın aileler listesinde yok")

    for kimlik in sorted(aile_idleri - kullanilan_aileler):
        hatalar.append(f"aileler: '{kimlik}' hiçbir araç kaydına bağlı değil")
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
    aileler = veri.get("aileler", [])
    sorunlar = [s for a in araclar for s in a["kronik_sorunlar"]] + [s for f in aileler for s in f["kronik_sorunlar"]]
    kullanilan = {alan_adi(u) for s in sorunlar for u in s["kaynaklar"]}
    sinirli = sum(1 for n in sayilar if n == EN_AZ_ALAN_ADI)
    kirilimli = sum(1 for s in sorunlar if "donem_kirilimi" in s)
    detayli = sum(1 for s in sorunlar if "detay" in s)
    kendi = sum(len(a["kronik_sorunlar"]) for a in araclar)
    ortak = sum(len(f["kronik_sorunlar"]) for f in aileler)
    print(
        f"Geçerli: {len(araclar)} araç, {kendi} kayda özgü kronik sorun, "
        f"{len(aileler)} aile ({ortak} ortak sorun), {len(kullanilan)} farklı kaynak sitesi."
    )
    print(f"{sinirli} sorun yalnızca {EN_AZ_ALAN_ADI} siteyle destekleniyor (sınırlı doğrulama).")
    print(f"{kirilimli} sorunda üretim yılına göre dönem kırılımı var.")
    print(f"{detayli} sorunda ayrıntı (neden, teşhis, çözüm, maliyet, önlem) var.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
