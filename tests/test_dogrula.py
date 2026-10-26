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


GUVENILIR = [a for a, b in KAYIT["siteler"].items() if b.get("tek_basina_yeterli")]


def alan_adlari(tur):
    """Tek başına yeterli sayılan siteler hariç: iki site kuralı testleri sıradan sitelerle yazılır."""
    return [a for a, b in KAYIT["siteler"].items() if b["tur"] == tur and not b.get("tek_basina_yeterli")]


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


def aileli_ornek():
    """Bir aile, ona bağlı yalnızca-aile kaydı ve aile sorununa kendi kaynağını bağlayan bir kayıt."""
    veri = ornek()
    aile_sorunu = copy.deepcopy(sorun(veri))
    aile_sorunu["id"] = "ortak-sorun"
    aile_sorunu.pop("donem_kirilimi")
    veri["aileler"] = [{
        "id": "test-motor",
        "ad": "Test motoru",
        "tur": "motor",
        "aciklama": "Test modellerinde kullanılan motor ailesi.",
        "kronik_sorunlar": [aile_sorunu],
    }]
    veri["arac_listesi"][0]["aileler"] = ["test-motor"]
    veri["arac_listesi"][0]["kronik_sorunlar"][0]["aile_sorunu"] = "test-motor/ortak-sorun"
    yalniz = copy.deepcopy(veri["arac_listesi"][0])
    yalniz["model"] = "Kardeş Model (2016-2021)"
    yalniz["uretim_yillari"] = {"baslangic": 2016, "bitis": 2021}
    yalniz["kronik_sorunlar"] = []
    veri["arac_listesi"].append(yalniz)
    return veri


def model_geneli_ornek():
    """Motor kaydı ve aynı modelin motordan bağımsız (model geneli) kaydı; ikincide kilometre bilgisi yok."""
    veri = ornek()
    model = copy.deepcopy(veri["arac_listesi"][0])
    model["motor"] = dogrula.MODEL_GENELI_MOTOR
    model["kronik_sorunlar"][0].pop("tahmini_km_araligi")
    veri["arac_listesi"].append(model)
    return veri


def aile(veri):
    return veri["aileler"][0]


def aile_sorunu(veri):
    return veri["aileler"][0]["kronik_sorunlar"][0]


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

    def test_detay_gecerli(self):
        veri = ornek()
        sorun(veri)["detay"] = {"neden": "n", "teshis": "t", "cozum": "c", "maliyet": "m", "onlem": "o"}
        self.assertEqual(hatalar(veri), [])

    def test_detay_tek_alan_yeter(self):
        veri = ornek()
        sorun(veri)["detay"] = {"cozum": "c"}
        self.assertEqual(hatalar(veri), [])

    def test_detay_bos_olamaz(self):
        veri = ornek()
        sorun(veri)["detay"] = {}
        self.assertHata(veri, "en az bir alan")

    def test_detay_tanimsiz_alan(self):
        veri = ornek()
        sorun(veri)["detay"] = {"fiyat": "x"}
        self.assertHata(veri, "tanımsız alan")

    def test_detay_metin_olmali(self):
        veri = ornek()
        sorun(veri)["detay"] = {"neden": " "}
        self.assertHata(veri, "boş olmayan metin")

    def test_detay_uzunluk_siniri(self):
        veri = ornek()
        sorun(veri)["detay"] = {"neden": "a" * (dogrula.DETAY_UZUNLUK_UST + 1)}
        self.assertHata(veri, "en fazla")

    def test_tek_site_yetmez(self):
        veri = ornek()
        sorun(veri)["kaynaklar"] = [f"https://{FORUM}/a", f"https://{FORUM}/b"]
        self.assertHata(veri, "en az 2 farklı site")

    def test_yalniz_editoryal_yetmez(self):
        veri = ornek()
        sorun(veri)["kaynaklar"] = [f"https://{a}/x" for a in EDITORYAL]
        self.assertHata(veri, "resmî belge, forum")

    def test_tek_basina_yeterli_site_tek_kaynak_yeter(self):
        self.assertTrue(GUVENILIR, "kayıt defterinde tek_basina_yeterli işaretli site yok")
        veri = ornek()
        sorun(veri)["kaynaklar"] = [f"https://{GUVENILIR[0]}/yazi-1/"]
        self.assertEqual(hatalar(veri), [])

    def test_tek_basina_yeterli_sitede_km_istege_bagli(self):
        veri = ornek()
        sorun(veri)["kaynaklar"] = [f"https://{GUVENILIR[0]}/yazi-1/"]
        del sorun(veri)["tahmini_km_araligi"]
        self.assertEqual(hatalar(veri), [])

    def test_sirada_site_icin_km_zorunlu_kalir(self):
        veri = ornek()
        del sorun(veri)["tahmini_km_araligi"]
        self.assertHata(veri, "tahmini_km_araligi")

    def test_tek_basina_yeterli_bayragi_yalniz_true_sayilir(self):
        kayit = copy.deepcopy(KAYIT)
        kayit["siteler"][GUVENILIR[0]]["tek_basina_yeterli"] = "evet"
        veri = ornek()
        sorun(veri)["kaynaklar"] = [f"https://{GUVENILIR[0]}/yazi-1/"]
        self.assertTrue(dogrula.dogrula(veri, kayit)[0])

    def test_kayitsiz_site(self):
        veri = ornek()
        sorun(veri)["kaynaklar"].append("https://kayitsiz-site.example/a")
        self.assertHata(veri, "tanımlı değil")

    def test_alt_alan_adi_kayit_defteriyle_eslesir(self):
        self.assertEqual(dogrula.alan_adi("https://forum.donanimhaber.com/x"), "donanimhaber.com")
        self.assertEqual(dogrula.alan_adi("https://www.honestjohn.co.uk/x"), "honestjohn.co.uk")
        self.assertEqual(dogrula.alan_adi("https://www.volkswagen.co.nz/x"), "volkswagen.co.nz")

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


class AileTesti(unittest.TestCase):
    def assertHata(self, veri, parca):
        bulunan = hatalar(veri)
        self.assertTrue(any(parca in h for h in bulunan), f"'{parca}' beklendi, bulunan: {bulunan}")

    def test_aileli_ornek_gecerli(self):
        self.assertEqual(hatalar(aileli_ornek()), [])

    def test_aileler_istege_bagli(self):
        self.assertEqual(hatalar(ornek()), [])

    def test_aile_sorunu_icin_iki_site_gerekir(self):
        veri = aileli_ornek()
        aile_sorunu(veri)["kaynaklar"] = [f"https://{FORUM}/a", f"https://{FORUM}/b"]
        self.assertHata(veri, "en az 2 farklı site")

    def test_aile_sorununda_id_zorunlu(self):
        veri = aileli_ornek()
        del aile_sorunu(veri)["id"]
        self.assertHata(veri, "eksik alan(lar): id")

    def test_aile_sorun_idsi_tekrar_edemez(self):
        veri = aileli_ornek()
        aile(veri)["kronik_sorunlar"].append(copy.deepcopy(aile_sorunu(veri)))
        self.assertHata(veri, "birden fazla kez tanımlı")

    def test_aile_idsi_tekrar_edemez(self):
        veri = aileli_ornek()
        veri["aileler"].append(copy.deepcopy(aile(veri)))
        self.assertHata(veri, "birden fazla kez tanımlı")

    def test_aile_kimligi_deseni(self):
        veri = aileli_ornek()
        aile(veri)["id"] = "Test Motoru"
        self.assertHata(veri, "kimlik olmalı")

    def test_aile_turu_gecersiz(self):
        veri = aileli_ornek()
        aile(veri)["tur"] = "kasa"
        self.assertHata(veri, "tur")

    def test_aile_aciklamasi_zorunlu_ve_sinirli(self):
        veri = aileli_ornek()
        aile(veri)["aciklama"] = " "
        self.assertHata(veri, "boş olmayan metin")
        veri = aileli_ornek()
        aile(veri)["aciklama"] = "a" * (dogrula.ACIKLAMA_UZUNLUK_UST + 1)
        self.assertHata(veri, "en fazla")

    def test_aile_sorunsuz_olamaz(self):
        veri = aileli_ornek()
        aile(veri)["kronik_sorunlar"] = []
        self.assertHata(veri, "en az bir sorun")

    def test_tanimsiz_aileye_baglanti(self):
        veri = aileli_ornek()
        veri["arac_listesi"][1]["aileler"] = ["yok"]
        self.assertHata(veri, "tanımlı değil")

    def test_yalniz_aile_kaydi_gecerli(self):
        veri = aileli_ornek()
        self.assertEqual(veri["arac_listesi"][1]["kronik_sorunlar"], [])
        self.assertEqual(hatalar(veri), [])

    def test_sorunsuz_ve_ailesiz_kayit_gecersiz(self):
        veri = aileli_ornek()
        del veri["arac_listesi"][1]["aileler"]
        self.assertHata(veri, "en az bir sorun ya da en az bir aile")

    def test_bos_aileler_listesi_gecersiz(self):
        veri = aileli_ornek()
        veri["arac_listesi"][1]["aileler"] = []
        self.assertHata(veri, "en az bir aile kimliği")

    def test_ayni_aile_iki_kez_yazilamaz(self):
        veri = aileli_ornek()
        veri["arac_listesi"][1]["aileler"] = ["test-motor", "test-motor"]
        self.assertHata(veri, "birden fazla kez yazılmış")

    def test_kullanilmayan_aile_hata_verir(self):
        veri = aileli_ornek()
        veri["aileler"].append({**copy.deepcopy(aile(veri)), "id": "bos-aile"})
        self.assertHata(veri, "hiçbir araç kaydına bağlı değil")

    def test_aile_sorunu_baglantisi_tanimli_olmali(self):
        veri = aileli_ornek()
        sorun(veri)["aile_sorunu"] = "test-motor/yok"
        self.assertHata(veri, "tanımlı bir aile sorunu değil")

    def test_aile_sorunu_baglantisi_aracin_ailesinde_olmali(self):
        veri = aileli_ornek()
        veri["aileler"].append({**copy.deepcopy(aile(veri)), "id": "diger-motor"})
        veri["arac_listesi"][1]["aileler"] = ["diger-motor"]
        veri["arac_listesi"][0]["aileler"] = ["diger-motor"]
        self.assertHata(veri, "aileler listesinde yok")

    def test_aile_sorunu_alani_arac_disinda_kullanilamaz(self):
        veri = aileli_ornek()
        aile_sorunu(veri)["aile_sorunu"] = "test-motor/ortak-sorun"
        self.assertHata(veri, "tanımsız alan")

    def test_aile_sorununun_donem_kirilimi_denetlenir(self):
        veri = aileli_ornek()
        aile_sorunu(veri)["donem_kirilimi"] = [{"baslangic": 2018, "bitis": 2016, "durum": "Yaygın", "not": "n"}]
        self.assertHata(veri, "bitiş yılı başlangıç yılından küçük")

    def test_model_geneli_kayit_gecerli(self):
        self.assertEqual(hatalar(model_geneli_ornek()), [])

    def test_model_geneli_kayitta_km_istege_bagli(self):
        veri = model_geneli_ornek()
        self.assertNotIn("tahmini_km_araligi", veri["arac_listesi"][1]["kronik_sorunlar"][0])
        self.assertEqual(hatalar(veri), [])

    def test_model_geneli_kayitta_verilen_km_yine_denetlenir(self):
        veri = model_geneli_ornek()
        veri["arac_listesi"][1]["kronik_sorunlar"][0]["tahmini_km_araligi"] = "50.000 civarı"
        self.assertHata(veri, "biçimi")
        veri["arac_listesi"][1]["kronik_sorunlar"][0]["tahmini_km_araligi"] = "90.000 - 40.000 km"
        self.assertHata(veri, "alt sınır üst sınırdan büyük")

    def test_motor_kaydinda_km_zorunlu(self):
        veri = ornek()
        del sorun(veri)["tahmini_km_araligi"]
        self.assertHata(veri, "eksik alan(lar): tahmini_km_araligi")

    def test_aile_sorununda_km_zorunlu(self):
        veri = aileli_ornek()
        del aile_sorunu(veri)["tahmini_km_araligi"]
        self.assertHata(veri, "eksik alan(lar): tahmini_km_araligi")

    def test_model_geneli_motor_adi_sabit(self):
        veri = model_geneli_ornek()
        veri["arac_listesi"][1]["motor"] = "Tüm motorlar"
        self.assertHata(veri, "model geneli kayıtta motor tam olarak")

    def test_model_geneli_kayit_aileye_baglanamaz(self):
        veri = aileli_ornek()
        model = copy.deepcopy(veri["arac_listesi"][0])
        model["motor"] = dogrula.MODEL_GENELI_MOTOR
        model["aileler"] = ["test-motor"]
        veri["arac_listesi"].append(model)
        self.assertHata(veri, "model geneli kayıt motor/şanzıman ailesine bağlanamaz")

    def test_model_geneli_kayit_sorunsuz_olamaz(self):
        veri = model_geneli_ornek()
        veri["arac_listesi"][1]["kronik_sorunlar"] = []
        self.assertHata(veri, "en az bir sorun ya da en az bir aile")

    def test_model_geneli_kayitta_en_az_iki_site_gerekir(self):
        veri = model_geneli_ornek()
        veri["arac_listesi"][1]["kronik_sorunlar"][0]["kaynaklar"] = [f"https://{FORUM}/a"]
        self.assertHata(veri, "en az 2 farklı site gerekir")

    def test_ayni_model_iki_kez_model_geneli_olamaz(self):
        veri = model_geneli_ornek()
        veri["arac_listesi"].append(copy.deepcopy(veri["arac_listesi"][1]))
        self.assertHata(veri, "aynı marka/model/motor birden fazla kez tanımlı")


class SemaTesti(unittest.TestCase):
    def test_sema_gercek_veriyi_kabul_eder(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        jsonschema.Draft202012Validator(SEMA).validate(GERCEK_VERI)

    def test_sema_detay_tanimsiz_alani_reddeder(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        veri = ornek()
        sorun(veri)["detay"] = {"fiyat": "x"}
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(SEMA).validate(veri)

    def test_sema_donem_kirilimi_durumunu_denetler(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        veri = ornek()
        sorun(veri)["donem_kirilimi"][0]["durum"] = "Çok yaygın"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(SEMA).validate(veri)

    def test_sema_aileli_veriyi_kabul_eder(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        jsonschema.Draft202012Validator(SEMA).validate(aileli_ornek())

    def test_sema_aile_sorununda_id_ister(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        veri = aileli_ornek()
        del aile_sorunu(veri)["id"]
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(SEMA).validate(veri)

    def test_sema_sorunsuz_ve_ailesiz_kaydi_reddeder(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        veri = aileli_ornek()
        del veri["arac_listesi"][1]["aileler"]
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(SEMA).validate(veri)

    def test_sema_model_geneli_kayitta_km_olmadan_kabul_eder(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        jsonschema.Draft202012Validator(SEMA).validate(model_geneli_ornek())

    def test_sema_motor_kaydinda_km_zorunlulugu_dogrulayiciya_birakilir(self):
        """Şema kayıt defterini bilmediği için km'yi zorlamaz (tek başına yeterli kaynakta km boş olabilir); doğrulayıcı zorlar."""
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        veri = ornek()
        del sorun(veri)["tahmini_km_araligi"]
        jsonschema.Draft202012Validator(SEMA).validate(veri)
        self.assertTrue(any("tahmini_km_araligi" in h for h in hatalar(veri)))

    def test_sema_model_geneli_kayit_aileye_baglanamaz(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema kurulu değil")
        veri = aileli_ornek()
        model = copy.deepcopy(veri["arac_listesi"][0])
        model["motor"] = dogrula.MODEL_GENELI_MOTOR
        model["aileler"] = ["test-motor"]
        veri["arac_listesi"].append(model)
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.Draft202012Validator(SEMA).validate(veri)


if __name__ == "__main__":
    unittest.main()
