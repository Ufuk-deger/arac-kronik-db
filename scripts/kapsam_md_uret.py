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
MODEL_GENELI_ONEKI = "Tüm motorlar"  # model geneli plan satırlarının ve kayıtlarının motor alanı bununla başlar


def model_satiri_mi(oge):
    """Plan satırı motor grubunu değil, modelin motordan bağımsız sorunlarını (11. aşama) kapsıyorsa True."""
    return any(m.startswith(MODEL_GENELI_ONEKI) for m in oge["eslesme"]["motor"])


def eslesen_kayitlar(oge, araclar):
    """Motor satırları yalnızca motor kayıtlarıyla, model geneli satırlar yalnızca model geneli kayıtlarla eşleşir."""
    modeller = oge["eslesme"]["model"]
    motorlar = oge["eslesme"]["motor"]
    model_satiri = model_satiri_mi(oge)
    return [
        arac
        for arac in araclar
        if arac["marka"] == oge["marka"]
        and any(m in arac["model"] for m in modeller)
        and any(m in arac["motor"] for m in motorlar)
        and arac["motor"].startswith(MODEL_GENELI_ONEKI) == model_satiri
    ]


def aile_haritasi(veri):
    return {f["id"]: f for f in veri.get("aileler", [])}


def sorun_sayilari(kayit, aileler):
    """Kayıtta gösterilen sorunlar: kayda özgü olanlar ve ailelerden gelen (kayıtta karşılığı olmayan) ortak sorunlar."""
    ozgu = kayit["kronik_sorunlar"]
    paylasilan = {s["aile_sorunu"] for s in ozgu if "aile_sorunu" in s}
    ortak = [s for f in kayit.get("aileler", []) for s in aileler[f]["kronik_sorunlar"] if f"{f}/{s['id']}" not in paylasilan]
    return ozgu, ortak


def durum_metni(oge, kayitlar, aileler):
    if kayitlar:
        ozgu, ortak = [], []
        for a in kayitlar:
            o, k = sorun_sayilari(a, aileler)
            ozgu += o
            ortak += k
        kirilim = sum(1 for s in ozgu + ortak if "donem_kirilimi" in s)
        if ozgu:
            metin = f"✓ {len(ozgu)} sorun"
            if ortak:
                metin += f" (+{len(ortak)} ortak aile)"
        else:
            metin = f"◐ {len(ortak)} ortak aile sorunu"
        if kirilim:
            metin += f", {kirilim} yıl kırılımı"
        if oge.get("not"):
            metin += f" — {oge['not']}"
        return metin
    if oge.get("sonuc") == "yetersiz-kanit":
        return f"– eklenmedi: {oge['not']}"
    return "○ sırada"


def ozgu_kaynakli(kayitlar):
    """Satırın eşleşen kayıtlarından en az biri kendi sorununa sahip mi (✓) yoksa yalnızca ailesine mi (◐) dayanıyor?"""
    return any(a["kronik_sorunlar"] for a in kayitlar)


def sayi(adet):
    return f"{adet:,}".replace(",", ".") if adet else "—"


def uret():
    plan = json.loads(PLAN_DOSYASI.read_text(encoding="utf-8"))
    veri = json.loads(VARSAYILAN_DOSYA.read_text(encoding="utf-8"))
    araclar = veri["arac_listesi"]
    markalar = plan["pazar"]["markalar"]
    bilinen = {m["marka"] for m in markalar}

    hatalar = [o["marka"] for o in plan["plan"] if o["marka"] not in bilinen]
    if hatalar:
        raise SystemExit(f"HATA: planda tanımsız marka: {sorted(set(hatalar))}")

    eslesmeler = [(oge, eslesen_kayitlar(oge, araclar)) for oge in plan["plan"]]
    eslesen_idler = {id(a) for _, kayitlar in eslesmeler for a in kayitlar}
    aileler = aile_haritasi(veri)

    model_eslesmeleri = [(o, k) for o, k in eslesmeler if model_satiri_mi(o)]
    eslesmeler = [(o, k) for o, k in eslesmeler if not model_satiri_mi(o)]
    toplam = len(eslesmeler)
    tamam = sum(1 for _, k in eslesmeler if k and ozgu_kaynakli(k))
    yalniz_aile = sum(1 for _, k in eslesmeler if k and not ozgu_kaynakli(k))
    elenen = sum(1 for o, k in eslesmeler if not k and o.get("sonuc"))
    kalan = toplam - tamam - yalniz_aile - elenen
    kademe1 = [(o, k) for o, k in eslesmeler if o["kademe"] == 1]
    kademe1_islenen = sum(1 for o, k in kademe1 if k or o.get("sonuc"))
    model_tamam = sum(1 for _, k in model_eslesmeleri if k)
    model_elenen = sum(1 for o, k in model_eslesmeleri if not k and o.get("sonuc"))
    model_kalan = len(model_eslesmeleri) - model_tamam - model_elenen
    motor_kayitlari = [a for a in araclar if not a["motor"].startswith(MODEL_GENELI_ONEKI)]
    model_kayitlari = [a for a in araclar if a["motor"].startswith(MODEL_GENELI_ONEKI)]
    taranan = sum(1 for a in motor_kayitlari
                  if any(o["marka"] == a["marka"] and any(m in a["model"] for m in o["eslesme"]["model"]) for o, _ in model_eslesmeleri))

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
        "Aynı batarya ve motor değerlerine sahip kardeş modelin kaynağı yalnızca ilgili kayıtta açıkça belirtilerek kullanılabilir (ör. Astra Electric ve Peugeot e-308).",
        "- **Hibrit ve plug-in hibrit araçlar (14. aşamadan itibaren):** Tam hibritler (ör. Toyota 1.8 Hybrid), hafif hibritler (48V) ve plug-in hibritler "
        "(PHEV; ör. Volvo T8, Passat GTE, Kuga PHEV) kapsamdadır. `motor` alanı içten yanmalı motoru ve hibrit sistemi birlikte söyler; plug-in sürümlerde `PHEV` ibaresi ve varsa batarya kapasitesi yer alır. "
        "Sorunlar içten yanmalı motora ve şanzımana, hibrit sisteme özgü parçalara (yüksek voltlu batarya, inverter, DC-DC dönüştürücü, şarj girişi ve şarj cihazı, 12V akü) ve yazılıma ayrılır; "
        "aynı içten yanmalı motoru kullanan sürümler o motorun ailesine bağlanır. Kanıt kuralı değişmez: her sorun için iki bağımsız site, bunlardan biri deneyim ya da resmî türünde.",
        "- **Sıralama:** Genelden özele gidilir. Önce her markanın en çok satılan ve en çok sorgulanan modelleri ile ana motor grupları "
        "(kademe 1), sonra yaygın ama daha az sorgulananlar (kademe 2), en son niş gruplar (kademe 3).",
        "- **Yıl kırılımı:** Kaynaklar üretim yılına göre fark belirtiyorsa sorun `donem_kirilimi` ile yıl aralıklarına ayrılır "
        "(ör. revizyon öncesi ve sonrası).",
        "- **Motor versiyonları:** Kaynaklar iki versiyonu motor kodu, güç, şanzıman ya da kasa/nesil ile ayırt ediyorsa ayrı kayıt açılır "
        "(ör. M271 Kompressor ve M271 EVO; N47D16 ve N47D20; Qashqai J11 1.5 dCi ve 1.6 dCi Xtronic). "
        "Ayırt etmiyorlarsa kayıt bölünmez, fark metinde ya da `donem_kirilimi` içinde belirtilir ([README](README.md#motor-versiyonları)).",
        "- **Aynı motoru ya da şanzımanı paylaşan modeller (10. aşamadan itibaren):** Motor ve şanzıman kaynaklı sorunlar ortak ailelere yazılır "
        "([README](README.md#ortak-motor-ve-şanzıman-aileleri-aileler)); aynı motoru ya da şanzımanı kullandığı bilinen modeller aileye bağlanır. "
        "Modele özgü kaynağı olan kayıtlar kendi sorununu aile sorununa bağlar (✓); modele özgü kaynağı olmayanlar yalnızca ortak aile kaynağıyla kayıtlıdır (◐) "
        "ve plan notunda modele özgü kaynağın aranmadığı ya da bulunmadığı yazılır. Bu kayıtlar doğrudan kanıtı sınırlı sayılır ve görüntüleyicide \"Ortak aile\" etiketiyle ayrılır. "
        "Aile bağı yalnızca model, yıl ve motor kodunun eşleştiği bilinen kombinasyonlar için kurulur.",
        "- **İlan sayısı kontrolü:** 7. aşamada plan, arabam.com'un aylık ilan sıralamaları ve Cardata listeleriyle karşılaştırıldı "
        "(sahibinden.com'un canlı model sayıları okunamadı) ve en çok ilanlı modellerin motor boşlukları kapatıldı. \"Çok ilanlı\" olmak tek başına "
        "kayıt gerekçesi değildir: tekrar eden bir kronik sorun için iki bağımsız kaynak bulunamazsa grup `–` olarak kalır.",
        "- **Çok kullanılan araç denetimi:** 9. aşamada plan, trafikteki araç sayıları (TÜİK verisine dayanan yaklaşık 2024 listeleri) ve ikinci el satış sıralamalarıyla "
        "model, nesil ve motor düzeyinde yeniden karşılaştırıldı. Bir satırın `eslesme` parçalarından her biri en az bir kayda denk gelmelidir (test denetler); "
        "\"1.4 TSI / 1.6 TDI\" gibi birleşik bir satırın yalnızca bir parçası kayıtlıysa satır bölünür, böylece ✓ kayıtsız bir motoru gizleyemez. "
        "Aranıp eklenmeyen (–) gruplar ile sıraya alınmış (○) gruplar görüntüleyicide \"Kayıt açılmayan gruplar\" bölümünde gösterilir.",
        "- **Model geneli sorunlar (11. aşamadan itibaren):** Motordan bağımsız, modele (nesle) özgü sorunlar (cam tavan ve bagajdan su alma, far, kapı kilidi, multimedya, boya, "
        "ön takım gibi kasa, sızdırmazlık, iç mekân, elektronik ve süspansiyon sorunları) `motor` alanı \"Tüm motorlar (model geneli)\" olan ayrı bir kayıtta toplanır "
        "([README](README.md#model-geneli-kayıtlar)). Bu sorunlar yaşa ve kullanıma bağlı olduğundan kaynaklarda çoğunlukla kilometre bilgisi yoktur; "
        "kilometre aralığı uydurulmaz, boş bırakılır. Model geneli plan satırları yalnızca işlendikçe eklenir (✓ ya da –); satırı olmayan bir modelde bu sorunlar henüz taranmamıştır.",
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
        f"- Plan: **{toplam}** model/motor grubu (motor ve şanzıman düzeyi)",
        f"- Tamamlanan (✓, modele özgü kaynaklı sorun var): **{tamam}**",
        f"- Yalnızca ortak aile kaynağıyla kayıtlı (◐): **{yalniz_aile}**",
        f"- Araştırılıp eklenmeyen (–): **{elenen}**",
        f"- Sırada (○): **{kalan}**",
        f"- Kademe 1: **{kademe1_islenen}/{len(kademe1)}** işlendi (✓, ◐ ya da –)",
        f"- Model geneli taraması: **{len(model_eslesmeleri)}** model nesli arandı (sorun bulunan ✓ **{model_tamam}**, kanıt yetersiz – **{model_elenen}**"
        + (f", sırada ○ **{model_kalan}**" if model_kalan else "")
        + f"); {len(motor_kayitlari)} motor kaydından **{taranan}**'i taranmış bir modele ait, **{len(motor_kayitlari) - taranan}**'i henüz taranmadı",
        f"- Veritabanı: **{len(araclar)}** kayıt (**{len(motor_kayitlari)}** motor, **{len(model_kayitlari)}** model geneli), "
        f"**{sum(len(a['kronik_sorunlar']) for a in araclar)}** kayda özgü kronik sorun, "
        f"**{len(aileler)}** motor/şanzıman ailesi (**{sum(len(f['kronik_sorunlar']) for f in aileler.values())}** ortak sorun)",
        "",
        "| Marka | Plan | ✓ | ◐ | – | ○ | Kademe 1 işlenen | Model geneli (✓ / –) |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    marka_sirasi = [m["marka"] for m in markalar if m["kapsam"] != "dışarıda"]
    for marka in marka_sirasi:
        oge = [(o, k) for o, k in eslesmeler if o["marka"] == marka]
        if not oge:
            continue
        t = sum(1 for _, k in oge if k and ozgu_kaynakli(k))
        y = sum(1 for _, k in oge if k and not ozgu_kaynakli(k))
        e = sum(1 for o, k in oge if not k and o.get("sonuc"))
        k1 = [(o, k) for o, k in oge if o["kademe"] == 1]
        mt = sum(1 for o, k in model_eslesmeleri if o["marka"] == marka and k)
        me = sum(1 for o, k in model_eslesmeleri if o["marka"] == marka and not k and o.get("sonuc"))
        model_hucre = f"{mt} / {me}" if (mt or me) else "—"
        satir.append(
            f"| {marka} | {len(oge)} | {t} | {y} | {e} | {len(oge) - t - y - e} | {sum(1 for o, k in k1 if k or o.get('sonuc'))}/{len(k1)} | {model_hucre} |"
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
        "Durum: **✓** veritabanında kayıtlı ve modele özgü kaynaklı sorunu var, **◐** kayıtlı ama yalnızca motor/şanzıman ailesinin ortak kaynaklarına dayanıyor "
        "(bu modele özgü bildirim ayrıca doğrulanmadı), **○** sırada, **–** araştırıldı ama iki bağımsız site bulunamadığı için eklenmedi. "
        "Motor grubu \"Tüm motorlar (model geneli)\" olan satırlar modelin motordan bağımsız sorunlarını gösterir (✓ sorun bulundu, – kanıt yetersiz). "
        "Yıllar yaklaşık üretim ya da Türkiye satış yıllarıdır.",
        "",
    ]
    for marka in marka_sirasi:
        oge = [(o, k) for o, k in eslesmeler + model_eslesmeleri if o["marka"] == marka]
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
                f"| {o['kademe']} | {o['model']} | {o['yillar']} | {o['motor']} | {durum_metni(o, k, aileler)} |"
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
