"""scripts/dogrula.py kurallarının testleri. Çalıştırmak için: python3 -m unittest discover tests"""

import copy
import json
import sys
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import dogrula  # noqa: E402

KAYIT = json.loads(dogrula.KAYIT_DOSYASI.read_text(encoding="utf-8"))
GERCEK_VERI = json.loads(dogrula.VARSAYILAN_DOSYA.read_text(encoding="utf-8"))
SEMA = json.loads((KOK / "schema" / "araclar.schema.json").read_text(encoding="utf-8"))


def alan_adlari(tur):
    return [a for a, b in KAYIT["siteler"].items() if b["tur"] == tur]


FORUM = alan_adlari("forum")[0]
EDITORYAL = alan_adlari("editoryal")[:2]


def ornek():
    return {
        "arac_listesi": [
            {
                "marka": "Test",
                "model": "Model (2015-2020)",
                "motor": "1.0",
                "uretim_yillari": {"baslangic": 2015, "bitis": 2020},
                "kronik_sorunlar": [
                    {
                        "sorun_adi": "s",
                        "etkilenen_parca": "p",
                        "belirtiler": "b",
                        "tahmini_km_araligi": "10.000 - 20.000 km",
                        "risk_seviyesi": "Orta",
                        "kaynaklar": [f"https://{FORUM}/a", f"https://{EDITORYAL[0]}/b"],
                        "donem_kirilimi": [
                            {"baslangic": 2015, "bitis": 2017, "durum": "Yaygın", "not": "n"},
                            {"baslangic": 2018, "bitis": None, "durum": "Seyrek", "not": "n"},
                        ],
                    }
                ],
            }
        ]
    }


def hatalar(veri):
    return dogrula.dogrula(veri, KAYIT)[0]


def sorun(veri):
    return veri["arac_listesi"][0]["kronik_sorunlar"][0]


class DogrulaTesti(unittest.TestCase):
    def assertHata(self, veri, parca):
        bulunan = hatalar(veri)
        self.assertTrue(any(parca in h for h in bulunan), f"'{parca}' beklendi, bulunan: {bulunan}")

    def test_ornek_gecerli(self):
        self.assertEqual(hatalar(ornek()), [])

    def test_gercek_veri_gecerli(self):
        self.assertEqual(hatalar(GERCEK_VERI), [])

    def test_donem_kirilimi_istege_bagli(self):
        veri = ornek()
        del sorun(veri)["donem_kirilimi"]
        self.assertEqual(hatalar(veri), [])

    def test_uretim_yillari_zorunlu(self):
        veri = ornek()
        del veri["arac_listesi"][0]["uretim_yillari"]
        self.assertHata(veri, "eksik alan(lar): uretim_yillari")

    def test_bitis_baslangictan_kucuk(self):
        veri = ornek()
        veri["arac_listesi"][0]["uretim_yillari"] = {"baslangic": 2020, "bitis": 2015}
        self.assertHata(veri, "bitiş yılı başlangıç yılından küçük")

    def test_yil_sayi_olmali(self):
        veri = ornek()
        veri["arac_listesi"][0]["uretim_yillari"]["baslangic"] = "2015"
        self.assertHata(veri, "arası bir yıl olmalı")

    def test_donemler_cakisamaz(self):
        veri = ornek()
        sorun(veri)["donem_kirilimi"][1]["baslangic"] = 2017
        self.assertHata(veri, "çakışmayan")

    def test_donemler_sirali_olmali(self):
        veri = ornek()
        sorun(veri)["donem_kirilimi"].reverse()
        self.assertHata(veri, "çakışmayan")

    def test_acik_uclu_donemden_sonra_donem_olamaz(self):
        veri = ornek()
        sorun(veri)["donem_kirilimi"].append({"baslangic": 2019, "bitis": None, "durum": "Seyrek", "not": "n"})
        self.assertHata(veri, "çakışmayan")

    def test_donem_uretim_yillari_disinda(self):
        veri = ornek()
        sorun(veri)["donem_kirilimi"] = [{"baslangic": 2005, "bitis": 2010, "durum": "Yaygın", "not": "n"}]
        self.assertHata(veri, "üretim yılları dışında")

    def test_gecersiz_durum(self):
        veri = ornek()
        sorun(veri)["donem_kirilimi"][0]["durum"] = "Çok yaygın"
        self.assertHata(veri, "durum")

    def test_donem_notu_zorunlu(self):
        veri = ornek()
        sorun(veri)["donem_kirilimi"][0]["not"] = " "
        self.assertHata(veri, "boş olmayan metin")

    def test_bos_kirilim_listesi(self):
        veri = ornek()
        sorun(veri)["donem_kirilimi"] = []
        self.assertHata(veri, "en az bir dönem")

    def test_tanimsiz_kirilim_alani(self):
        veri = ornek()
        sorun(veri)["donem_kirilimi"][0]["oran"] = 5
        self.assertHata(veri, "tanımsız alan")

    def test_tek_site_yetmez(self):
        veri = ornek()
        sorun(veri)["kaynaklar"] = [f"https://{FORUM}/a", f"https://{FORUM}/b"]
        self.assertHata(veri, "en az 2 farklı site")

    def test_yalniz_editoryal_yetmez(self):
        veri = ornek()
        sorun(veri)["kaynaklar"] = [f"https://{a}/x" for a in EDITORYAL]
        self.assertHata(veri, "resmî belge, forum")

    def test_kayitsiz_site(self):
        veri = ornek()
        sorun(veri)["kaynaklar"].append("https://kayitsiz-site.example/a")
        self.assertHata(veri, "tanımlı değil")

    def test_alt_alan_adi_kayit_defteriyle_eslesir(self):
        self.assertEqual(dogrula.alan_adi("https://forum.donanimhaber.com/x"), "donanimhaber.com")
        self.assertEqual(dogrula.alan_adi("https://www.honestjohn.co.uk/x"), "honestjohn.co.uk")

    def test_km_bicimi(self):
        veri = ornek()
        sorun(veri)["tahmini_km_araligi"] = "10-20 bin km"
        self.assertHata(veri, "biçimi")

    def test_km_alt_sinir_ustten_buyuk(self):
        veri = ornek()
        sorun(veri)["tahmini_km_araligi"] = "30.000 - 20.000 km"
        self.assertHata(veri, "alt sınır")

    def test_ayni_arac_iki_kez(self):
        veri = ornek()
        veri["arac_listesi"].append(copy.deepcopy(veri["arac_listesi"][0]))
        self.assertHata(veri, "birden fazla kez")


class SemaTesti(unittest.TestCase):
    def test_sema_gercek_veriyi_kabul_eder(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        jsonschema.Draft202012Validator(SEMA).validate(GERCEK_VERI)

    def test_sema_donem_kirilimi_durumunu_denetler(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        veri = ornek()
        sorun(veri)["donem_kirilimi"][0]["durum"] = "Çok yaygın"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(SEMA).validate(veri)


if __name__ == "__main__":
    unittest.main()
