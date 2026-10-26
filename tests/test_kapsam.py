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

    def test_tarama_parcalari_gercek_motor_kaydina_denk_gelir(self):
        # `eslesme.tarama` yalnızca model geneli satırlarda, aynı markanın bir motor kaydının model adında bulunan parçalarla kullanılır;
        # bayat ya da yanlış yazılmış parça, gerçekte taranmamış bir modeli "taranmış" gösterir.
        motor_kayitlari = [a for a in ARACLAR if not a["motor"].startswith(kapsam_md_uret.MODEL_GENELI_ONEKI)]
        for o in PLAN["plan"]:
            parcalar = o["eslesme"].get("tarama")
            if parcalar is None:
                continue
            self.assertTrue(kapsam_md_uret.model_satiri_mi(o), f"{o['marka']} {o['model']}: tarama yalnızca model geneli satırda olur")
            for parca in parcalar:
                self.assertTrue(any(a["marka"] == o["marka"] and parca in a["model"] for a in motor_kayitlari),
                                f"{o['marka']} {o['model']}: tarama parçası hiçbir motor kaydında yok: {parca!r}")

    def test_kapsam_disi_markalar_planda_yok(self):
        disarida = {m["marka"] for m in PLAN["pazar"]["markalar"] if m["kapsam"] == "dışarıda"}
        self.assertEqual({o["marka"] for o in PLAN["plan"]} & disarida, set())

    def test_motor_satiri_model_geneli_kayitla_eslesmez(self):
        # "" gibi her motoru yakalayan bir parça, model geneli kaydı motor kaydı sayıp ✓ göstermemeli.
        model = {"marka": "Test", "model": "Model (2015-2020)", "motor": "Tüm motorlar (model geneli)",
                 "uretim_yillari": {"baslangic": 2015, "bitis": 2020}, "kronik_sorunlar": []}
        motor = {**model, "motor": "1.0"}
        motor_satiri = {"marka": "Test", "model": "Model", "eslesme": {"model": ["Model"], "motor": [""]}}
        model_satiri = {"marka": "Test", "model": "Model", "eslesme": {"model": ["Model"], "motor": ["Tüm motorlar"]}}
        self.assertEqual(kapsam_md_uret.eslesen_kayitlar(motor_satiri, [model, motor]), [motor])
        self.assertEqual(kapsam_md_uret.eslesen_kayitlar(model_satiri, [model, motor]), [model])

    def test_model_geneli_satir_gercek_motor_kaydina_denk_gelmez(self):
        for o in PLAN["plan"]:
            if kapsam_md_uret.model_satiri_mi(o):
                for a in kapsam_md_uret.eslesen_kayitlar(o, ARACLAR):
                    self.assertTrue(a["motor"].startswith(kapsam_md_uret.MODEL_GENELI_ONEKI))

    def test_md_uretilir(self):
        metin = kapsam_md_uret.uret()
        self.assertIn("## Plan ve durum", metin)
        self.assertIn("Renault", metin)


if __name__ == "__main__":
    unittest.main()
