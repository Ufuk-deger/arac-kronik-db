#!/usr/bin/env python3
"""Sosyal medya için dikey (1080x1920, 30 kare/sn) sorun videoları üretir: arka planda araç görseli, yazı animasyonu.

Her video bir sorunu anlatır: marka ve model, risk, sorun adı (yazılarak gelir), belirtiler, kilometre ve motor, kapanışta site.
Yanında paylaşım metni (açıklama + etiketler) aynı adla .txt olarak yazılır. Kullanım:

    python3 scripts/video_uret.py renault/clio-5-2019-gunumuz            # o modelin en riskli sorunu
    python3 scripts/video_uret.py renault/clio-5-2019-gunumuz --sira 3   # sıradaki 3. sorun
    python3 scripts/video_uret.py renault/clio-5-2019-gunumuz --hepsi    # modelin tüm sorunları
Çıktı: videolar/<marka>/<model>/NN-<sorun>.mp4 (git'e eklenmez).
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_uret as su  # noqa: E402
import seslendirme as ses  # noqa: E402

KOK = su.KOK
CIKTI = KOK / "videolar"


def gruplar_ve_yollar():
    veri = json.loads(su.VARSAYILAN_DOSYA.read_text(encoding="utf-8"))
    gruplar = su.grupla(su.kayitlari_kur(veri))
    kullanilan = set()
    for g in gruplar:
        yol = f"{su.kisalt(g['marka'])}/{su.kisalt(g['taban'])}-{g['yb']}-{g['ye'] or 'gunumuz'}"
        aday, n = yol, 2
        while aday in kullanilan:
            aday, n = f"{yol}-{n}", n + 1
        kullanilan.add(aday)
        g["yol"], g["yil"] = aday, su.yil_etiketi(g["yb"], g["ye"])
        g["motorlar"], g["kartlar"] = su.kart_listesi(g)
    return {g["yol"]: g for g in gruplar}


def cumlelere_bol(metin, en_cok=3):
    cumleler = [c.strip() for c in re.split(r"(?<=[.!?])\s+", metin.strip()) if c.strip()]
    if len(cumleler) > en_cok:
        cumleler = cumleler[:en_cok]
    return [c if c.endswith((".", "!", "?")) else c + "." for c in cumleler]


def ozellik(g, kart, ayar):
    s = kart["s"]
    km = su.km_araligi(s.get("tahmini_km_araligi"))
    cipler = []
    if km:
        cipler.append({"yazi": f"{km[0]:,} – {km[1]:,} km".replace(",", "."), "km": True})
    if "genel" in kart["etiketler"]:
        cipler.append({"yazi": "Tüm motorlar"})
    else:
        cipler += [{"yazi": su.motor_adi(g["motorlar"][int(t[1:])], g["taban"])} for t in kart["etiketler"]]
    cumleler = cumlelere_bol(s["belirtiler"])
    foto = su.GORSELLER.get(g["yol"])
    if foto:
        arka = f'<img src="file://{su.GORSEL_KLASORU / foto["dosya"]}">'
        kredi = f'Fotoğraf: {foto["yazar"]}, {foto["lisans"]}'
    else:
        arka, kredi = su.kasa_svg(su.kasa_tipi(g)), ""
    logo = su.LOGOLAR.get(g["marka"])
    yazma = min(2.4, 0.045 * len(s["sorun_adi"]) + 0.6)
    z = {"etiket": 0.9, "baslik": 1.5, "yazma": yazma}
    z["belirti"] = z["baslik"] + yazma + 0.4
    z["cumle_arasi"] = 1.3
    z["cip"] = z["belirti"] + len(cumleler) * z["cumle_arasi"] + 0.2
    z["son"] = z["cip"] + 2.6 + 0.6 * len(cumleler)
    z["toplam"] = round(z["son"] + 2.8, 2)
    adres = ayar["adres"].replace("https://", "").rstrip("/")
    return {
        "model": f'{g["marka"]} {g["taban"]}', "yil": g["yil"], "logo": logo["yol"] if logo else "",
        "harf": "".join(p[0] for p in re.split(r"[\s-]+", g["marka"]) if p)[:2].upper(),
        "risk": s["risk_seviyesi"], "risk_anahtar": su.RISK_ANAHTAR[s["risk_seviyesi"]],
        "baslik": s["sorun_adi"], "cumleler": cumleler, "cipler": cipler, "arka": arka, "kredi": kredi,
        "site": ayar["ad"], "cagri": f'{g["marka"]} {g["taban"]} için bilinen tüm kronik sorunlar', "adres": adres,
        "zaman": z,
    }


def seslendir(g, kart, oz, klasor, ad, ayar):
    """Cümle cümle seslendirir, görüntü zamanlarını sese göre yeniden kurar ve birleşik WAV yazar."""
    s = kart["s"]
    model = f'{g["marka"]} {su.ilk_parca(g["taban"])}'
    km = su.km_araligi(s.get("tahmini_km_araligi"))
    if "genel" in kart["etiketler"]:
        yer = "tüm motorlarda"
    else:
        adlar = [re.sub(r"\s*\(.*", "", su.motor_adi(g["motorlar"][int(e[1:])], g["taban"])) for e in kart["etiketler"]]
        yer = (", ".join(adlar[:2])) + " motorda"
    km_cumle = (f"Genelde {km[0]:,} – {km[1]:,} km arasında, {yer} görülüyor.".replace(",", ".") if km
                else f"{yer[0].upper() + yer[1:]} görülüyor.")
    metinler = [f"{model} bakıyorsan şuna dikkat et.", s["sorun_adi"].rstrip(".") + "."] + oz["cumleler"] + [km_cumle,
                f"{model} için bilinen tüm kronik sorunlar {ayar.get('ad_bulunma', ayar['ad'])}."]
    wavlar = [ses.sentezle(ses.okunur(m)) for m in metinler]
    sureler = [ses.sure(w) for w in wavlar]
    bas, t0, ara = [], 0.5, 0.35
    for d in sureler:
        bas.append(t0); t0 += d + ara
    n = len(oz["cumleler"])
    z = oz["zaman"]
    z["etiket"] = bas[0] + 0.3
    z["baslik"], z["yazma"] = bas[1], max(0.8, sureler[1] * 0.9)
    z["belirti_t"] = bas[2:2 + n]
    z["belirti"] = bas[2]
    z["cip"] = bas[2 + n]
    z["son"] = bas[3 + n] - 0.2
    z["toplam"] = round(bas[-1] + sureler[-1] + 1.0, 2)
    wav = klasor / f"{ad}.wav"
    ses.birlestir(list(zip(bas, wavlar)), wav, z["toplam"])
    return wav


def paylasim_metni(g, kart, ayar):
    s = kart["s"]
    etiket = lambda x: "#" + re.sub(r"[^0-9a-zçğıöşü]", "", x.lower().replace("İ", "i"))
    etiketler = " ".join(dict.fromkeys([etiket(g["marka"]), etiket(g["marka"] + su.ilk_parca(g["taban"])), etiket(su.ilk_parca(g["taban"])),
                                        "#kroniksorun", "#ikinciel", "#arabaalırken", "#" + ayar["ad"].lower()]))
    return (f'{g["marka"]} {g["taban"]} ({g["yil"]}) bakıyorsan bunu bil: {s["sorun_adi"]}.\n\n'
            f'{s["belirtiler"]}\n\n'
            f'Modelin bilinen tüm kronik sorunları {ayar["adres"].replace("https://", "")} adresinde. '
            f'Bilgiler sürücü deneyimleri ve usta yazılarından derlendi. Ekspertiz yerine geçmez.\n\n{etiketler}\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model", help="model sayfasının yolu, ör. renault/clio-5-2019-gunumuz")
    ap.add_argument("--sira", type=int, default=1, help="riske göre sıradaki sorun (1 = en riskli)")
    ap.add_argument("--hepsi", action="store_true")
    ap.add_argument("--ses", action="store_true", help="Google Cloud Text-to-Speech ile seslendir")
    a = ap.parse_args()
    ayar = json.loads(su.AYAR_DOSYASI.read_text(encoding="utf-8"))
    gruplar = gruplar_ve_yollar()
    if a.model not in gruplar:
        aday = [y for y in gruplar if a.model in y]
        sys.exit("Model bulunamadı. Benzerler: " + ", ".join(aday[:10]))
    g = gruplar[a.model]
    siralar = range(1, len(g["kartlar"]) + 1) if a.hepsi else [a.sira]
    klasor = CIKTI / g["yol"]
    klasor.mkdir(parents=True, exist_ok=True)
    for i in siralar:
        kart = g["kartlar"][i - 1]
        ad = f"{i:02d}-{su.kisalt(kart['s']['sorun_adi'])[:60]}"
        oz = ozellik(g, kart, ayar)
        wav = seslendir(g, kart, oz, klasor, ad, ayar) if a.ses else None
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(oz, f, ensure_ascii=False)
        sessiz = klasor / f"{ad}.sessiz.mp4" if wav else klasor / f"{ad}.mp4"
        subprocess.run(["node", str(KOK / "scripts" / "video" / "kaydet.js"), f.name, str(sessiz)], check=True)
        if wav:
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(sessiz), "-i", str(wav), "-c:v", "copy", "-c:a", "aac",
                            "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(klasor / f"{ad}.mp4")], check=True)
            sessiz.unlink(); wav.unlink()
        (klasor / f"{ad}.txt").write_text(paylasim_metni(g, kart, ayar), encoding="utf-8")
        print(klasor / f"{ad}.mp4")


if __name__ == "__main__":
    main()
