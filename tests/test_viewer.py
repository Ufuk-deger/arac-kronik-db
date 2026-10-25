"""Görüntüleyici üretiminin temel testleri. Çalıştırmak için: python3 -m unittest discover tests"""

import json
import re
import sys
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import viewer_uret  # noqa: E402
from dogrula import VARSAYILAN_DOSYA  # noqa: E402

VERI = json.loads(VARSAYILAN_DOSYA.read_text(encoding="utf-8"))


class GoruntuleyiciTesti(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = viewer_uret.uret()

    def gomulu(self, kimlik):
        eslesme = re.search(rf'<script type="application/json" id="{kimlik}">(.*?)</script>', self.html, re.S)
        self.assertIsNotNone(eslesme, kimlik)
        return json.loads(eslesme.group(1).replace("<\\/", "</"))

    def test_yer_tutucular_doldurulur(self):
        for yer in ("__VERI__", "__KAYNAK__", "__PLAN__"):
            self.assertNotIn(yer, self.html)

    def test_gomulu_veri_dosyayla_ayni(self):
        veri = self.gomulu("veri")
        self.assertEqual(len(veri["arac_listesi"]), len(VERI["arac_listesi"]))
        self.assertEqual(len(veri["aileler"]), len(VERI["aileler"]))
        self.assertGreater(len(self.gomulu("kaynak-veri")["siteler"]), 0)
        self.assertIsInstance(self.gomulu("plan-veri"), list)

    def test_baslik_ve_dil(self):
        self.assertIn("<title>Araç Kronik DB</title>", self.html)
        self.assertIn('lang="tr"', self.html)

    def test_filtre_alanlari_var(self):
        for kimlik in ("ara", "marka", "model", "yil", "km", "kmfiltre", "elektrikli", "temizle", "liste", "sonuc"):
            self.assertIn(f'id="{kimlik}"', self.html, kimlik)

    def test_koyu_tema_ve_telefon_duzeni_tanimli(self):
        self.assertIn("prefers-color-scheme: dark", self.html)
        self.assertIn(':root[data-theme="dark"]', self.html)
        self.assertIn("max-width: 699px", self.html)
        self.assertIn("safe-area-inset-left", self.html)

    def test_harici_betik_yok(self):
        # Yayın ortamı yalnızca izinli adreslerden betik yükler; görüntüleyici kendi betiğini içerir.
        self.assertEqual(re.findall(r'<script[^>]+src=', self.html), [])


if __name__ == "__main__":
    unittest.main()
