#!/usr/bin/env python3
"""Tek dosyalık görüntüleyiciyi üretir: viewer/index.html

data/araclar.json, data/kaynaklar.json ve kaydı olmayan plan satırları (data/kapsam.json) viewer/sablon.html
içine gömülür. Çıktıyı tarayıcıda açın; sunucu gerekmez. Kullanım:

    python3 scripts/viewer_uret.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dogrula import KAYIT_DOSYASI, KOK, VARSAYILAN_DOSYA  # noqa: E402
from kapsam_md_uret import PLAN_DOSYASI, eslesen_kayitlar  # noqa: E402

SABLON = KOK / "viewer" / "sablon.html"
HEDEF = KOK / "viewer" / "index.html"
SITE_ALANLARI = ("ad", "ulke", "tur", "guven")

ISKELET_BASI = (
    '<!doctype html><html lang="tr"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
    "<style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style>"
)


def json_metni(nesne):
    # </script> dizisinin gömülü JSON içinde sayfayı bozmasını önler.
    return json.dumps(nesne, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def plan_ozeti(veri):
    """Kaydı olmayan plan satırları: kaynak arandı ama eklenmedi ('elendi') ya da henüz sırada ('sirada')."""
    plan = json.loads(PLAN_DOSYASI.read_text(encoding="utf-8"))["plan"]
    ozet = []
    for oge in plan:
        if eslesen_kayitlar(oge, veri["arac_listesi"]):
            continue
        sirada = oge.get("sonuc") != "yetersiz-kanit"
        ozet.append({
            "marka": oge["marka"], "model": oge["model"], "yillar": oge["yillar"], "motor": oge["motor"],
            "durum": "sirada" if sirada else "elendi", "not": "" if sirada else oge["not"],
        })
    return ozet


def uret():
    veri = json.loads(VARSAYILAN_DOSYA.read_text(encoding="utf-8"))
    kayit = json.loads(KAYIT_DOSYASI.read_text(encoding="utf-8"))
    siteler = {
        alan: {k: bilgi[k] for k in SITE_ALANLARI}
        for alan, bilgi in kayit["siteler"].items()
    }
    sablon = SABLON.read_text(encoding="utf-8")
    for yer in ("__VERI__", "__KAYNAK__", "__PLAN__"):
        if sablon.count(yer) != 1:
            raise SystemExit(f"HATA: şablonda {yer} tam bir kez geçmeli")
    govde = (
        sablon.replace("__VERI__", json_metni(veri))
        .replace("__KAYNAK__", json_metni({"siteler": siteler}))
        .replace("__PLAN__", json_metni(plan_ozeti(veri)))
    )
    return ISKELET_BASI + govde + "</html>\n"


def main():
    HEDEF.write_text(uret(), encoding="utf-8")
    print(f"{HEDEF.relative_to(KOK)} yazıldı.")


if __name__ == "__main__":
    main()
