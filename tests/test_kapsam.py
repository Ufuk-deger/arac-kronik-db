"""data/kapsam.json planının tutarlılık testleri. Çalıştırmak için: python3 -m unittest discover tests"""

import json
import sys
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import kapsam_md_uret  # noqa: E402
from dogrula import VARSAYILAN_DOSYA  # noqa: E402

PLAN = json.loads(kapsam_md_uret.PLAN_DOSYASI.read_text(encoding="utf-8"))
ARACLAR = json.loads(VARSAYILAN_DOSYA.read_text(encoding="utf-8"))["arac_listesi"]


class KapsamTesti(unittest.TestCase):
    def test_planin_markalari_tanimli(self):
        tanimli = {m["marka"] for m in PLAN["pazar"]["markalar"]}
        self.assertEqual({o["marka"] for o in PLAN["plan"]} - tanimli, set())

    def test_kademe_degerleri(self):
        self.assertTrue(all(str(o["kademe"]) in PLAN["kademeler"] for o in PLAN["plan"]))

    def test_elenen_satirlarin_nedeni_var(self):
        for o in PLAN["plan"]:
            if "sonuc" in o:
                self.assertEqual(o["sonuc"], "yetersiz-kanit")
                self.assertTrue(o.get("not"), f"{o['marka']} {o['model']}: neden yazılmamış")

    def test_elenen_satir_kayitla_eslesmez(self):
        # Eklenmemiş diye işaretlenen bir grup için kayıt varsa plan bayat kalmıştır.
        for o in PLAN["plan"]:
            if "sonuc" in o:
                self.assertEqual(kapsam_md_uret.eslesen_kayitlar(o, ARACLAR), [], f"{o['marka']} {o['model']}")

    def test_kayitli_satirda_her_eslesme_parcasi_bir_kayda_denk_gelir(self):
        # Birleşik motor/model satırı ("1.4 TSI / 1.6 TDI") yalnızca bir parçası kayıtlıysa ✓ görünüp
        # diğer parçayı gizler. Eşleşme parçalarının her biri, satırın eşleşen kayıtlarından en az birinde bulunmalı;
        # bulunmayan parça ayrı bir satır olmalı (kayıtsızsa '–' ya da '○').
        for o in PLAN["plan"]:
            kayitlar = kapsam_md_uret.eslesen_kayitlar(o, ARACLAR)
            if not kayitlar:
                continue
            for parca in o["eslesme"]["model"]:
                self.assertTrue(any(parca in a["model"] for a in kayitlar),
                                f"{o['marka']} {o['model']} / {o['motor']}: model parçası kayıtlarda yok: {parca!r}")
            for parca in o["eslesme"]["motor"]:
                self.assertTrue(any(parca in a["motor"] for a in kayitlar),
                                f"{o['marka']} {o['model']} / {o['motor']}: motor parçası kayıtlarda yok: {parca!r}")

    def test_kapsam_disi_markalar_planda_yok(self):
        disarida = {m["marka"] for m in PLAN["pazar"]["markalar"] if m["kapsam"] == "dışarıda"}
        self.assertEqual({o["marka"] for o in PLAN["plan"]} & disarida, set())

    def test_md_uretilir(self):
        metin = kapsam_md_uret.uret()
        self.assertIn("## Plan ve durum", metin)
        self.assertIn("Renault", metin)


if __name__ == "__main__":
    unittest.main()
