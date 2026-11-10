"""Statik site üreticisi: sayfa sayısı, model gruplaması ve kaynak bilgisinin siteye sızmaması."""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import site_uret  # noqa: E402

# Kaynak sitelerin adları (alan adları kaynaklar.json'dan ayrıca denetlenir).
YASAK_ADLAR = ("şikâyetvar", "şikayetvar", "donanımhaber", "ekşi sözlük", "and çetin", "andcetin", "bimmerpost", "honest john")


class SiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gecici = tempfile.TemporaryDirectory()
        cls.hedef = Path(cls.gecici.name) / "site"
        cls.ozet = site_uret.uret(cls.hedef)
        cls.sayfalar = {p: p.read_text(encoding="utf-8") for p in cls.hedef.rglob("*.html")}
        cls.veri = json.loads(site_uret.VARSAYILAN_DOSYA.read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls.gecici.cleanup()

    def test_her_model_grubu_icin_bir_sayfa(self):
        gruplar = site_uret.grupla(site_uret.kayitlari_kur(self.veri))
        self.assertEqual(self.ozet["model"], len(gruplar))
        model_sayfalari = [p for p in self.sayfalar if len(p.relative_to(self.hedef).parts) == 3]
        self.assertEqual(len(model_sayfalari), len(gruplar))

    def test_her_kayit_tam_bir_gruba_girer(self):
        kayitlar = site_uret.kayitlari_kur(self.veri)
        gruplar = site_uret.grupla(kayitlar)
        self.assertEqual(sum(len(g["kayitlar"]) for g in gruplar), len(self.veri["arac_listesi"]))

    def test_tum_sorunlar_sitede(self):
        govde = "\n".join(self.sayfalar.values())
        for arac in self.veri["arac_listesi"]:
            for s in arac["kronik_sorunlar"]:
                self.assertIn(site_uret.e(s["sorun_adi"]), govde, s["sorun_adi"])

    def test_kaynak_bilgisi_siteye_sizmaz(self):
        alanlar = list(json.loads((KOK / "data" / "kaynaklar.json").read_text(encoding="utf-8"))["siteler"])
        for yol, metin in self.sayfalar.items():
            kucuk = metin.lower()
            for alan in alanlar:
                self.assertNotIn(alan, kucuk, f"{yol}: {alan}")
            for ad in YASAK_ADLAR:
                self.assertNotIn(ad, kucuk, f"{yol}: {ad}")
            ayar = site_uret.json.loads(site_uret.AYAR_DOSYASI.read_text(encoding="utf-8"))
            izinli = ("https://fonts.googleapis.com", "https://fonts.gstatic.com", ayar["adres"]) + ((ayar["bildirim_formu"],) if ayar.get("bildirim_formu") else ())
            disari = [u for u in re.findall(r'href="(https?://[^"]+)"', metin) if not u.startswith(izinli)]
            self.assertEqual(disari, [], yol)

    def test_ayrintilar_siteye_girmez(self):
        govde = "\n".join(self.sayfalar.values())
        ornek = [s["detay"]["neden"] for a in self.veri["arac_listesi"] for s in a["kronik_sorunlar"] if s.get("detay", {}).get("neden")][:50]
        for metin in ornek:
            self.assertNotIn(site_uret.e(metin[:80]), govde)

    def test_adresler_benzersiz_ve_kisa(self):
        yollar = [p.parent.relative_to(self.hedef).as_posix() for p in self.sayfalar if p.name == "index.html"]
        self.assertEqual(len(yollar), len(set(yollar)))
        for y in yollar:
            self.assertRegex(y, r"^[a-z0-9/-]*$|^\.$")

    def test_site_haritasi(self):
        harita = (self.hedef / "sitemap.xml").read_text(encoding="utf-8")
        self.assertEqual(harita.count("<loc>"), self.ozet["sayfa"])

    def test_eksik_sorun_bildirimi(self):
        """Ayar boşken çağrı çıkmaz; form adresi verilince bağlantı, yalnız e-posta verilince adres yazılır."""
        self.assertEqual(site_uret.bildir_html({"bildirim_formu": "", "eposta": ""}, "Renault Clio 5"), "")
        form = site_uret.bildir_html({"bildirim_formu": "https://forms.example/x", "eposta": ""}, "Renault Clio 5")
        self.assertIn('href="https://forms.example/x"', form)
        self.assertIn("Renault Clio 5", form)
        eposta = site_uret.bildir_html({"bildirim_formu": "", "eposta": "bilgi@ornek.com"}, "Renault Clio 5")
        self.assertIn("bilgi@ornek.com", eposta)
        self.assertNotIn("href", eposta)
        ayar = json.loads(site_uret.AYAR_DOSYASI.read_text(encoding="utf-8"))
        if not ayar.get("bildirim_formu") and not ayar.get("eposta"):
            self.assertFalse(any('class="bildir"' in h for h in self.sayfalar.values()))

    def test_ince_sayfalar_dizinlenmez(self):
        """Modele özgü sorunu olmayan sayfa noindex taşır ve site haritasında yer almaz; diğerleri tersine."""
        harita = (self.hedef / "sitemap.xml").read_text(encoding="utf-8")
        gruplar = site_uret.grupla(site_uret.kayitlari_kur(self.veri))
        ince = 0
        for p, html in self.sayfalar.items():
            parca = p.relative_to(self.hedef).parts
            if len(parca) != 3:
                continue
            yol = "/".join(parca[:2]) + "/"
            noindex = 'name="robots" content="noindex' in html
            self.assertEqual(noindex, f"/{yol}</loc>" not in harita, p)
            self.assertEqual(noindex, 'class="ince"' in html and "derinlemesine taranmadı" in html, p)
            ince += noindex
        self.assertEqual(ince, sum(1 for g in gruplar if not any(f is None for k in g["kayitlar"] for _, f in k["sorunlar"])))


if __name__ == "__main__":
    unittest.main()
