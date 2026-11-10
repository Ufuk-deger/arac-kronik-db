"""YAZIM.md kurallarının veride korunduğunu denetler (sitede görünen sorun adı ve belirtiler)."""
import json
import re
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
VERI = json.loads((KOK / "data" / "araclar.json").read_text(encoding="utf-8"))

# Kaynak ve meta dil: sitede okura "kim ne demiş" anlatılmaz, sorun kendisi anlatılır.
YASAK = [r"\bsahip", r"bildir", r"\bvaka", r"şikâyet", r"şikayet", r"garanti", r"\bkaynak(?!l)", r"iddia",
         r"yazıyor", r"anlatıyor", r"kullanıcı", r"forum", r"reddet", r"tartışmalı", r"\bbelirtil", r"raporla"]


def sorunlar():
    for arac in VERI["arac_listesi"]:
        for s in arac["kronik_sorunlar"]:
            yield f'{arac["marka"]} {arac["model"]} / {s["sorun_adi"]}', s
    for aile in VERI.get("aileler", []):
        for s in aile["kronik_sorunlar"]:
            yield f'aile {aile["id"]} / {s["sorun_adi"]}', s


class YazimTest(unittest.TestCase):
    def test_sorun_adi_kisa(self):
        uzun = [y for y, s in sorunlar() if len(s["sorun_adi"]) > 60]
        self.assertEqual(uzun, [])

    def test_noktali_virgul_zinciri_yok(self):
        hatali = [y for y, s in sorunlar() if ";" in s["sorun_adi"] + s["belirtiler"]]
        self.assertEqual(hatali, [])

    def test_belirti_tam_cumle(self):
        hatali = [y for y, s in sorunlar() if not s["belirtiler"].rstrip().endswith((".", "!", "?"))]
        self.assertEqual(hatali, [])

    def test_kaynak_ve_meta_dil_yok(self):
        hatali = []
        for y, s in sorunlar():
            metin = (s["sorun_adi"] + " " + s["belirtiler"]).lower()
            hatali += [f"{y}: {k}" for k in YASAK if re.search(k, metin)]
        self.assertEqual(hatali, [])


if __name__ == "__main__":
    unittest.main()
