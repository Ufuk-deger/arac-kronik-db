# arac-kronik-db

Türkiye'de yaygın olarak kullanılan otomobillerin bilinen kronik sorunlarını
marka, model ve motor bazında listeleyen JSON veritabanı.

> **Uyarı:** Veriler kullanıcı şikâyetleri, servis bültenleri ve geri çağırma
> kampanyaları gibi kamuya açık bilgilerden derlenmiştir ve yalnızca bilgi
> amaçlıdır. Kilometre aralıkları tahminidir; kullanım koşulları, bakım
> geçmişi ve üretim yılına göre büyük ölçüde değişebilir. Satın alma veya
> onarım kararı vermeden önce aracı yetkili bir servise kontrol ettirin.

## Dosyalar

| Dosya | Açıklama |
| --- | --- |
| `data/araclar.json` | Veritabanının kendisi |
| `schema/araclar.schema.json` | Veri yapısını tanımlayan JSON Schema (draft 2020-12) |
| `scripts/dogrula.py` | Veriyi doğrulayan betik (yalnızca Python standart kütüphanesi) |

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
          "risk_seviyesi": "Düşük/Orta/Yüksek"
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

Risk seviyeleri:

- **Düşük:** Konfor veya aşınmaya yönelik, aracı yolda bırakmayan sorunlar.
- **Orta:** Onarım gerektiren, ihmal edilirse büyüyebilecek sorunlar.
- **Yüksek:** Motor/şanzıman hasarına veya aracın yolda kalmasına yol açabilen,
  onarımı pahalı sorunlar.

## Doğrulama

```sh
python3 scripts/dogrula.py
```

Betik; zorunlu alanları, tanımsız alanları, risk seviyesi değerlerini,
kilometre aralığı biçimini (alt sınırın üst sınırdan küçük olması dahil) ve
aynı marka/model/motor üçlüsünün tekrar edilmemesini kontrol eder. Hata
bulunursa sıfırdan farklı bir çıkış koduyla sonlanır.

## Katkı

1. `data/araclar.json` içine yeni aracı marka ve model sırasını koruyarak ekleyin.
2. Aynı motoru paylaşan araçlar (ör. 1.5 dCi kullanan Renault ve Dacia
   modelleri) her biri ayrı kayıt olarak eklenir.
3. `python3 scripts/dogrula.py` komutunun hatasız tamamlandığından emin olun.
