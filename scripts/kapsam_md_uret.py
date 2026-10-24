#!/usr/bin/env python3
"""KAPSAM.md dosyasını data/kapsam.json ve data/araclar.json içeriğinden üretir.

Plandaki her satır (marka, model, motor grubu) araçlar dosyasındaki kayıtlarla eşleştirilir
ve durumu hesaplanır. Kullanım:

    python3 scripts/kapsam_md_uret.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dogrula import KOK, VARSAYILAN_DOSYA  # noqa: E402

PLAN_DOSYASI = KOK / "data" / "kapsam.json"
HEDEF = KOK / "KAPSAM.md"

SIRALI_MARKA_SAYISI = 10  # birden fazla haberde tutarlı çıkan ilk 10 marka
KAPSAM_BASLIKLARI = {"kapsamda": "Kapsamda", "ek": "Ek kademe", "dışarıda": "Kapsam dışı"}


def eslesen_kayitlar(oge, araclar):
    modeller = oge["eslesme"]["model"]
    motorlar = oge["eslesme"]["motor"]
    return [
        arac
        for arac in araclar
        if arac["marka"] == oge["marka"]
        and any(m in arac["model"] for m in modeller)
        and any(m in arac["motor"] for m in motorlar)
    ]


def durum_metni(oge, kayitlar):
    if kayitlar:
        sorun = sum(len(a["kronik_sorunlar"]) for a in kayitlar)
        kirilim = sum(1 for a in kayitlar for s in a["kronik_sorunlar"] if "donem_kirilimi" in s)
        metin = f"✓ {sorun} sorun"
        if kirilim:
            metin += f", {kirilim} yıl kırılımı"
        return metin
    if oge.get("sonuc") == "yetersiz-kanit":
        return f"– eklenmedi: {oge['not']}"
    return "○ sırada"


def sayi(adet):
    return f"{adet:,}".replace(",", ".") if adet else "—"


def uret():
    plan = json.loads(PLAN_DOSYASI.read_text(encoding="utf-8"))
    araclar = json.loads(VARSAYILAN_DOSYA.read_text(encoding="utf-8"))["arac_listesi"]
    markalar = plan["pazar"]["markalar"]
    bilinen = {m["marka"] for m in markalar}

    hatalar = [o["marka"] for o in plan["plan"] if o["marka"] not in bilinen]
    if hatalar:
        raise SystemExit(f"HATA: planda tanımsız marka: {sorted(set(hatalar))}")

    eslesmeler = [(oge, eslesen_kayitlar(oge, araclar)) for oge in plan["plan"]]
    eslesen_idler = {id(a) for _, kayitlar in eslesmeler for a in kayitlar}

    toplam = len(eslesmeler)
    tamam = sum(1 for _, k in eslesmeler if k)
    elenen = sum(1 for o, k in eslesmeler if not k and o.get("sonuc"))
    kalan = toplam - tamam - elenen
    kademe1 = [(o, k) for o, k in eslesmeler if o["kademe"] == 1]
    kademe1_islenen = sum(1 for o, k in kademe1 if k or o.get("sonuc"))

    satir = [
        "# Kapsam ve ilerleme",
        "",
        "Bu dosya `scripts/kapsam_md_uret.py` ile `data/kapsam.json` (plan) ve `data/araclar.json` (veri) içeriğinden üretilir. "
        "Elle düzenlemeyin; planı `data/kapsam.json` içinde değiştirip betiği yeniden çalıştırın.",
        "",
        "## Ölçüt",
        "",
        "- **Zaman penceresi:** Son 10-15 yılın araçları, yani yaklaşık 2011 model yılı ve sonrası. "
        "Daha eski yıllar yalnızca ilk aşamada eklenmiş kayıtlarda kaldı (aşağıda ayrıca listelenir).",
        "- **Marka seçimi:** Türkiye'de en çok satılan markalar (aşağıdaki tablo). İlk dört aşamada elektrikli ya da 2023 sonrası girmiş markalar "
        "(BYD, Togg, Tesla, Chery) \"motor grubu ve ikinci el geçmişi yok\" gerekçesiyle dışarıda bırakılmıştı; 5. aşamada elektrikli araçlar kapsama alındı ve bu markalar plana girdi. "
        "Bu listenin dışındaki markalar (`ek` kapsamı) ikinci el yaygınlığı ve kaynak bulunabilirliği gözetilerek editoryal olarak eklendi; satış adetleri doğrulanamadı.",
        "- **Elektrikli araçlar:** `motor` alanı elektrik motoru ve batarya sürümünü gösterir (ör. `Elektrik (52,4 kWh ve 88,5 kWh)`). Sorunlar batarya, şarj (OBC, ICCU), 12V akü ve yazılım gibi "
        "elektrikli araca özgü parçalara aittir. Geri çağırma kaydı olan sorunlarda Türkiye kapsamı doğrulanamıyorsa bu kayıtta ve plan notunda belirtilir. "
        "Aynı batarya ve motor değerlerine sahip kardeş modelin kaynağı yalnızca ilgili kayıtta açıkça belirtilerek kullanılabilir (ör. Astra Electric ve Peugeot e-308). Plug-in hibritler (ör. BYD Seal U DM-i) bu aşamada kapsam dışıdır.",
        "- **Sıralama:** Genelden özele gidilir. Önce her markanın en çok satılan ve en çok sorgulanan modelleri ile ana motor grupları "
        "(kademe 1), sonra yaygın ama daha az sorgulananlar (kademe 2), en son niş gruplar (kademe 3).",
        "- **Yıl kırılımı:** Kaynaklar üretim yılına göre fark belirtiyorsa sorun `donem_kirilimi` ile yıl aralıklarına ayrılır "
        "(ör. revizyon öncesi ve sonrası).",
        "- **Motor versiyonları:** Kaynaklar iki versiyonu motor kodu, güç, şanzıman ya da kasa/nesil ile ayırt ediyorsa ayrı kayıt açılır "
        "(ör. M271 Kompressor ve M271 EVO; N47D16 ve N47D20; Qashqai J11 1.5 dCi ve 1.6 dCi Xtronic). "
        "Ayırt etmiyorlarsa kayıt bölünmez, fark metinde ya da `donem_kirilimi` içinde belirtilir ([README](README.md#motor-versiyonları)).",
        "- **İlan sayısı kontrolü:** 7. aşamada plan, arabam.com'un aylık ilan sıralamaları ve Cardata listeleriyle karşılaştırıldı "
        "(sahibinden.com'un canlı model sayıları okunamadı) ve en çok ilanlı modellerin motor boşlukları kapatıldı. \"Çok ilanlı\" olmak tek başına "
        "kayıt gerekçesi değildir: tekrar eden bir kronik sorun için iki bağımsız kaynak bulunamazsa grup `–` olarak kalır.",
        "- **Kanıt eşiği:** Her sorun için en az iki farklı site ve en az bir deneyim/resmî türünde kaynak gerekir "
        "([README](README.md#kaynak-kuralı)). Kaynak bulunamayan gruplar plana `–` olarak işlenir; sorun uydurulmaz.",
        "",
        "Kademeler:",
        "",
    ]
    for no, aciklama in plan["kademeler"].items():
        satir.append(f"- **Kademe {no}:** {aciklama}")
    satir += [
        "",
        "Model ve motor seçimi 2025 satış sıralaması ve ikinci el pazarındaki yaygınlık gözetilerek editoryal olarak yapılmıştır; "
        "kademe atamaları kesin bir sıralama değil, çalışma sırasıdır.",
        "",
        "## İlerleme",
        "",
        f"- Plan: **{toplam}** model/motor grubu",
        f"- Tamamlanan (✓): **{tamam}**",
        f"- Araştırılıp eklenmeyen (–): **{elenen}**",
        f"- Sırada (○): **{kalan}**",
        f"- Kademe 1: **{kademe1_islenen}/{len(kademe1)}** işlendi (✓ ya da –)",
        f"- Veritabanı: **{len(araclar)}** kayıt, **{sum(len(a['kronik_sorunlar']) for a in araclar)}** kronik sorun",
        "",
        "| Marka | Plan | ✓ | – | ○ | Kademe 1 işlenen |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    marka_sirasi = [m["marka"] for m in markalar if m["kapsam"] != "dışarıda"]
    for marka in marka_sirasi:
        oge = [(o, k) for o, k in eslesmeler if o["marka"] == marka]
        if not oge:
            continue
        t = sum(1 for _, k in oge if k)
        e = sum(1 for o, k in oge if not k and o.get("sonuc"))
        k1 = [(o, k) for o, k in oge if o["kademe"] == 1]
        satir.append(
            f"| {marka} | {len(oge)} | {t} | {e} | {len(oge) - t - e} | {sum(1 for o, k in k1 if k or o.get('sonuc'))}/{len(k1)} |"
        )

    satir += [
        "",
        "## Markalar",
        "",
        f"{plan['pazar']['yil']} yılında Türkiye'de satılan sıfır otomobil sayısı **{sayi(plan['pazar']['toplam_otomobil'])}**. "
        f"Aşağıdaki sıralama {plan['pazar']['olcut']}.",
        "",
        "| Sıra* | Marka | 2025 otomobil satışı | Kapsam | Not |",
        "| :---: | --- | ---: | --- | --- |",
    ]
    for i, m in enumerate(markalar, 1):
        sira = str(i) if i <= SIRALI_MARKA_SAYISI else "11+"
        satir.append(
            f"| {sira} | {m['marka']} | {sayi(m['adet'])} | {KAPSAM_BASLIKLARI[m['kapsam']]} | {m['not']} |"
        )
    satir += [
        "",
        "\\* İlk 10 sıra birden fazla haberde tutarlıdır (Volkswagen ve Toyota için küçük rakam farkları notlandı). "
        "11. sıradan sonrası rakamlar tek bir tablodan alınmış ve ikinci bir kaynakta doğrulanamamıştır; bu yüzden sıra numarası verilmedi ve liste adet sırasındadır. "
        "Ford'un otomobil adedi bulunamadı. Kapsamdaki " + str(sum(1 for m in markalar if m["kapsam"] == "kapsamda")) + " marka bu belirsizliklerden etkilenmez, ancak 11-20. sıradaki markaların kendi aralarındaki sırası kesin değildir. "
        "Resmî tablo için ODMD'nin yıllık bülteni esas alınmalıdır.",
        "",
        "Pazar verisi kaynakları:",
        "",
    ]
    satir += [f"- <{url}>" for url in plan["pazar"]["kaynaklar"]]
    satir += ["- <https://www.odmd.org.tr> (Otomotiv Distribütörleri ve Mobilite Derneği, aylık basın bültenleri)", ""]

    satir += [
        "## Plan ve durum",
        "",
        "Durum: **✓** veritabanında kayıtlı, **○** sırada, **–** araştırıldı ama iki bağımsız site bulunamadığı için eklenmedi. "
        "Yıllar yaklaşık üretim ya da Türkiye satış yıllarıdır.",
        "",
    ]
    for marka in marka_sirasi:
        oge = [(o, k) for o, k in eslesmeler if o["marka"] == marka]
        if not oge:
            continue
        etiket = " (ek kademe)" if next(m for m in markalar if m["marka"] == marka)["kapsam"] == "ek" else ""
        satir += [
            f"### {marka}{etiket}",
            "",
            "| Kademe | Model | Yıllar | Motor grubu | Durum |",
            "| :---: | --- | --- | --- | --- |",
        ]
        for o, k in sorted(oge, key=lambda x: (x[0]["kademe"], x[0]["model"])):
            satir.append(
                f"| {o['kademe']} | {o['model']} | {o['yillar']} | {o['motor']} | {durum_metni(o, k)} |"
            )
        satir.append("")

    disarida = [a for a in araclar if id(a) not in eslesen_idler]
    if disarida:
        satir += [
            "## Plan dışı kayıtlar",
            "",
            "İlk aşamada eklenen ve 2011 öncesi üretime ağırlık veren ya da plandaki satırlarla eşleşmeyen kayıtlar. "
            "Silinmedi; doğrulanmış veri olarak durur.",
            "",
            "| Marka | Model | Motor |",
            "| --- | --- | --- |",
        ]
        for a in disarida:
            satir.append(f"| {a['marka']} | {a['model']} | {a['motor']} |")
        satir.append("")
    return "\n".join(satir)


def main():
    HEDEF.write_text(uret(), encoding="utf-8")
    print(f"{HEDEF.name} yazıldı.")


if __name__ == "__main__":
    main()
