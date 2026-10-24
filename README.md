# arac-kronik-db

Türkiye'de yaygın olarak kullanılan otomobillerin bilinen kronik sorunlarını
marka, model ve motor bazında listeleyen, her maddesi kaynaklı JSON veritabanı.

> **Uyarı:** Veriler kullanıcı şikâyetleri, forumlar, servis bültenleri ve geri
> çağırma kampanyaları gibi kamuya açık bilgilerden derlenmiştir ve yalnızca
> bilgi amaçlıdır. Kilometre aralıkları tahminidir; kullanım koşulları, bakım
> geçmişi ve üretim yılına göre büyük ölçüde değişebilir. Satın alma veya
> onarım kararı vermeden önce aracı yetkili bir servise kontrol ettirin.

## Dosyalar

| Dosya | Açıklama |
| --- | --- |
| `data/araclar.json` | Veritabanının kendisi |
| `data/kaynaklar.json` | Kaynak sitelerin kayıt defteri (ad, ülke, tür, güvenilirlik) |
| `schema/araclar.schema.json` | Veri yapısını tanımlayan JSON Schema (draft 2020-12) |
| `scripts/dogrula.py` | Veriyi ve kaynak kurallarını doğrulayan betik (yalnızca Python standart kütüphanesi) |
| `scripts/kaynaklar_md_uret.py` | `KAYNAKLAR.md` dosyasını üretir |
| `KAYNAKLAR.md` | Kullanılan forum ve sitelerin listesi, türleri ve güvenilirlik notları |
| `DOGRULAMA_RAPORU.md` | Hangi maddelerin doğrulandığı, kaldırıldığı, düzeltildiği ve eklendiği |

## Veri yapısı

```json
{
  "arac_listesi": [
    {
      "marka": "...",
      "model": "...",
      "motor": "...",
      "kronik_sorunlar": [
        {
          "sorun_adi": "...",
          "etkilenen_parca": "...",
          "belirtiler": "...",
          "tahmini_km_araligi": "...",
          "risk_seviyesi": "Düşük/Orta/Yüksek",
          "kaynaklar": ["https://...", "https://..."]
        }
      ]
    }
  ]
}
```

| Alan | Açıklama |
| --- | --- |
| `marka` | Üretici adı (ör. `Renault`) |
| `model` | Model adı; kasa kodu ve üretim yılları parantez içinde (ör. `Megane 3 / Fluence (2009-2016)`) |
| `motor` | Motor adı; motor kodu ve gerekiyorsa şanzıman parantez içinde (ör. `1.5 dCi (K9K, EDC)`) |
| `sorun_adi` | Sorunun kısa adı |
| `etkilenen_parca` | Arızanın kaynaklandığı parça veya sistem |
| `belirtiler` | Sürücünün fark edebileceği belirtiler, virgülle ayrılmış |
| `tahmini_km_araligi` | `80.000 - 150.000 km` biçiminde tahmini kilometre aralığı |
| `risk_seviyesi` | `Düşük`, `Orta` veya `Yüksek` |
| `kaynaklar` | Sorunu destekleyen sayfaların adresleri (en az iki farklı site) |

Risk seviyeleri:

- **Düşük:** Konfor veya aşınmaya yönelik, aracı yolda bırakmayan sorunlar.
- **Orta:** Onarım gerektiren, ihmal edilirse büyüyebilecek sorunlar.
- **Yüksek:** Motor/şanzıman hasarına veya aracın yolda kalmasına yol açabilen,
  onarımı pahalı sorunlar.

## Kaynak kuralı

Bir sorun veritabanına ancak şu koşullarla girer:

1. `kaynaklar` içinde **en az iki farklı sitenin** sayfası bulunur.
2. Kaynaklardan en az biri deneyime ya da resmî belgeye dayanır: forum, şikâyet
   platformu, sahip anketi, dava haberi, haber veya resmî belge. Yalnızca blog,
   parça satıcısı veya derleme sitesiyle desteklenen sorunlar alınmaz.
3. Her sitenin `data/kaynaklar.json` içinde tanımlı olması gerekir.

Kullanılan sitelerin listesi ve güvenilirlik notları için
[KAYNAKLAR.md](KAYNAKLAR.md), doğrulama sırasında yapılan değişiklikler için
[DOGRULAMA_RAPORU.md](DOGRULAMA_RAPORU.md) dosyalarına bakın.

## Doğrulama

```sh
python3 scripts/dogrula.py
```

Betik; zorunlu alanları, tanımsız alanları, risk seviyesi değerlerini,
kilometre aralığı biçimini (alt sınırın üst sınırdan küçük olması dahil),
aynı marka/model/motor üçlüsünün tekrar edilmemesini ve kaynak kuralını kontrol
eder. Hata bulunursa sıfırdan farklı bir çıkış koduyla sonlanır; başarılı
çalışmada yalnızca iki siteyle desteklenen (sınırlı doğrulamalı) madde sayısını da yazar.

## Katkı

1. `data/araclar.json` içine yeni aracı marka ve model sırasını koruyarak ekleyin.
2. Her sorun için en az iki farklı sitede destekleyici sayfa bulun ve adreslerini
   `kaynaklar` alanına yazın. Yeni bir site kullanıyorsanız `data/kaynaklar.json`
   içine ekleyin.
3. Aynı motoru paylaşan araçlar (ör. 1.5 dCi kullanan Renault ve Dacia
   modelleri) her biri ayrı kayıt olarak eklenir.
4. `python3 scripts/dogrula.py` komutunun hatasız tamamlandığından emin olun,
   ardından `python3 scripts/kaynaklar_md_uret.py` ile `KAYNAKLAR.md` dosyasını yenileyin.
