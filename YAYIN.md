# Caronic'i yayına alma

Site tamamen statik: `python3 scripts/site_uret.py` komutu `site/` klasörünü üretir, bu klasör olduğu gibi yayınlanır.
Sunucu, veritabanı ya da üyelik yok. Aşağıdaki adımlar Cloudflare Pages içindir (ücretsiz). Netlify de aynı `_headers` dosyasını okur.

## Yayından önce senin karar vermen gerekenler

| Konu | Durum | Ne yapılmalı |
|---|---|---|
| Alan adı | `data/site.json` → `adres` şu an `https://caronic.com`. Bu adresin boş olup olmadığı kontrol edilmedi. | Alan adını al. Başka bir adres alınırsa yalnızca `adres` satırını değiştir. |
| İletişim e-postası | `eposta` boş, sitede "İletişim adresi yakında eklenecek" yazıyor. | Örneğin `iletisim@caronic.com` aç ve `eposta` alanına yaz. |
| Eksik sorun bildirimi | `bildirim_formu` boş, model sayfalarında çağrı görünmüyor. | Bir Google Forms adresi verirsen her model sayfasının sonunda "Eksik sorunu bildirin" bağlantısı çıkar. |
| Model fotoğrafları | Yok, kasa tipi çizimleri gösteriliyor. | Yalnızca lisanslı fotoğraf eklenebilir (`data/gorseller/BENIOKU.md`). |
| Video seslendirmesi | Google Cloud TTS anahtarı yok. | Anahtar hazır olunca söyle, oturuma güvenli biçimde eklenir. |

## Cloudflare Pages kurulumu (bir kez)

1. Cloudflare hesabında **Workers & Pages → Create → Pages → Connect to Git** ile bu depoyu seç.
2. Dal: yayınlanacak dal (örneğin `main`; bu çalışma şu an `claude/fervent-goldberg-0vaev1` dalında).
3. Derleme ayarları:
   - Framework preset: **None**
   - Build command: `python3 scripts/site_uret.py`
   - Build output directory: `site`
   - Ortam değişkeni: `PYTHON_VERSION` = `3.12` (betik yalnızca Python standart kütüphanesini kullanır, paket kurulmaz)
4. İlk derleme bitince `*.pages.dev` adresinde site açılır. Kontrol listesi aşağıda.
5. **Custom domains** bölümünden `caronic.com` ve `www.caronic.com` ekle. Alan adı Cloudflare'de değilse sağlayıcıda
   gösterilen CNAME kaydını gir. `www` adresini **Rules → Redirect Rules** ile `https://caronic.com` adresine 301 yönlendir.
6. Google Search Console'a `https://caronic.com` ekle ve `https://caronic.com/sitemap.xml` site haritasını gönder.

Her push'ta Cloudflare siteyi kendiliğinden yeniden üretir. Veri değişince ayrıca bir şey yapmak gerekmez.

## Siteyle gelen dosyalar

- `_headers`: güvenlik başlıkları (CSP yalnızca kendi dosyalarına izin verir, çerçeve içine alınmayı engeller) ve önbellek süreleri.
- `robots.txt`, `sitemap.xml` (yalnızca dizinlenen sayfalar), `404.html`, `site.webmanifest`, favicon ve `og.png` paylaşım görseli.
- `fontlar/`: Inter ve Manrope yazı tipleri siteden verilir, ziyaretçi Google'a bağlanmaz (lisans: `data/fontlar/LISANS.txt`).

## Yayından sonra kontrol listesi

- [ ] Ana sayfada arama kutusuna "clio 5" yazınca öneri çıkıyor ve tıklayınca model sayfası açılıyor.
- [ ] Bir model sayfasında motor seçimi ve kilometre süzgeci çalışıyor.
- [ ] Olmayan bir adres (`/deneme`) 404 sayfasını gösteriyor.
- [ ] Tarayıcı konsolunda CSP hatası yok (Geliştirici Araçları → Console).
- [ ] Bağlantıyı WhatsApp'ta paylaşınca Caronic görseli ve başlığı çıkıyor.
- [ ] `https://caronic.com/sitemap.xml` açılıyor.

## Yerelde deneme

```bash
python3 scripts/site_uret.py
python3 -m http.server 8000 --directory site    # http://localhost:8000
python3 -m unittest discover -s tests           # yayın öncesi testler (kırık bağlantı, kaynak sızıntısı, yazım kuralları)
```
