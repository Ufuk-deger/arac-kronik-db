# arac-kronik-db

Türkiye'de yaygın olarak kullanılan otomobillerin bilinen kronik sorunlarını
marka, model ve motor bazında listeleyen, her maddesi kaynaklı JSON veritabanı.
Kapsam son 10-15 yılın araçlarıdır (yaklaşık 2011 model yılı ve sonrası); elektrikli
araçlar da kapsamdadır. Sorunlar, kaynaklar destekliyorsa üretim yılına göre kırılır
(ör. revizyon öncesi ve sonrası). Motor ve şanzıman sorunlarının yanında, motordan bağımsız
modele (nesle) özgü sorunlar da (cam tavandan su alma, kapı kilidi, boya vb.) "model geneli" kayıtlarda toplanır.

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
| `data/kapsam.json` | Kapsam planı: markalar, modeller, motor grupları ve kademeleri |
| `schema/araclar.schema.json` | Veri yapısını tanımlayan JSON Schema (draft 2020-12) |
| `scripts/dogrula.py` | Veriyi ve kaynak kurallarını doğrulayan betik (yalnızca Python standart kütüphanesi) |
| `scripts/kaynaklar_md_uret.py` | `KAYNAKLAR.md` dosyasını üretir |
| `scripts/kapsam_md_uret.py` | `KAPSAM.md` dosyasını plan ve veriden üretir |
| `scripts/viewer_uret.py` | Tarayıcıda açılan tek dosyalık görüntüleyiciyi (`viewer/index.html`) üretir |
| `viewer/sablon.html` | Görüntüleyicinin şablonu (arama, marka, model yılı, kilometre ve risk filtreleri) |
| `tests/test_dogrula.py` | Doğrulayıcının birim testleri (aile kuralları dahil) |
| `tests/test_kapsam.py` | Plan satırlarının kayıtlarla eşleşme kuralları ve `KAPSAM.md` üretimi testleri |
| `KAYNAKLAR.md` | Kullanılan forum ve sitelerin listesi, türleri ve güvenilirlik notları |
| `KAPSAM.md` | Hangi marka, model ve motor gruplarının planlandığı, hangilerinin tamamlandığı |
| `DOGRULAMA_RAPORU.md` | Hangi maddelerin doğrulandığı, kaldırıldığı, düzeltildiği ve eklendiği |

## Veri yapısı

```json
{
  "arac_listesi": [
    {
      "marka": "...",
      "model": "...",
      "motor": "...",
      "uretim_yillari": { "baslangic": 2015, "bitis": 2021 },
      "kronik_sorunlar": [
        {
          "sorun_adi": "...",
          "etkilenen_parca": "...",
          "belirtiler": "...",
          "tahmini_km_araligi": "...",
          "risk_seviyesi": "Düşük/Orta/Yüksek",
          "detay": {
            "neden": "...", "teshis": "...", "cozum": "...", "maliyet": "...", "onlem": "..."
          },
          "kaynaklar": ["https://...", "https://..."],
          "donem_kirilimi": [
            { "baslangic": 2015, "bitis": 2018, "durum": "Yaygın", "not": "..." },
            { "baslangic": 2019, "bitis": null, "durum": "Seyrek", "not": "..." }
          ]
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
| `motor` | Motor adı; motor kodu ve gerekiyorsa şanzıman parantez içinde (ör. `1.5 dCi (K9K, EDC)`). Elektrikli araçlarda `Elektrik` ile başlar ve batarya ya da sürüm bilgisi parantez içinde yazılır (ör. `Elektrik (52,4 kWh ve 88,5 kWh)`) |
| `uretim_yillari` | Bu model ve motor kombinasyonunun üretim veya Türkiye satış yılları. `bitis` değeri `null` ise üretim sürüyor |
| `sorun_adi` | Sorunun kısa adı |
| `etkilenen_parca` | Arızanın kaynaklandığı parça veya sistem |
| `belirtiler` | Sürücünün fark edebileceği belirtiler, virgülle ayrılmış |
| `tahmini_km_araligi` | `80.000 - 150.000 km` biçiminde tahmini kilometre aralığı. Motor kayıtlarında zorunludur; yalnızca model geneli kayıtlarda kaynaklarda kilometre yoksa yazılmaz ([Model geneli kayıtlar](#model-geneli-kayıtlar)) |
| `risk_seviyesi` | `Düşük`, `Orta` veya `Yüksek` |
| `kaynaklar` | Sorunu destekleyen sayfaların adresleri (en az iki farklı site) |
| `detay` | İsteğe bağlı. Sorunun nedeni, nasıl anlaşıldığı, yaygın çözümü, bildirilen maliyeti ve önlemi; aşağıya bakın |
| `donem_kirilimi` | İsteğe bağlı. Sorunun üretim yılına göre durumu; aşağıya bakın |

Risk seviyeleri:

- **Düşük:** Konfor veya aşınmaya yönelik, aracı yolda bırakmayan sorunlar (model geneli kayıtlarda kozmetik sorunlar).
- **Orta:** Onarım gerektiren, ihmal edilirse büyüyebilecek sorunlar.
- **Yüksek:** Motor/şanzıman hasarına veya aracın yolda kalmasına yol açabilen,
  onarımı pahalı sorunlar (elektrikli araçlarda batarya, şarj ünitesi ya da 12V akü kaynaklı güç kaybı dahil).

## Ortak motor ve şanzıman aileleri (`aileler`)

Aynı motoru ya da şanzımanı kullanan modeller aynı sorunları paylaşır (ör. 1.5 dCi K9K enjektörü Clio'da da Duster'da da,
DQ200 DSG mekatroniği Polo'da da Octavia'da da). Bu sorunları her modelde baştan yazmak yerine kökte bir `aileler`
listesi tutulur ve kayıtlar aileye bağlanır:

```json
{
  "aileler": [
    {
      "id": "renault-k9k", "ad": "Renault K9K 1.5 dCi (common rail dizel)", "tur": "motor",
      "aciklama": "...",
      "kronik_sorunlar": [ { "id": "enjektor", "sorun_adi": "...", "kaynaklar": ["...", "..."] } ]
    }
  ],
  "arac_listesi": [
    { "marka": "Nissan", "model": "Note (E12, 2013-2017)", "motor": "1.5 dCi 90 (K9K)",
      "aileler": ["renault-k9k"], "kronik_sorunlar": [] },
    { "marka": "Renault", "model": "Clio 4 (2013-2019)", "motor": "1.5 dCi 75/90 (K9K)",
      "aileler": ["renault-k9k"],
      "kronik_sorunlar": [ { "sorun_adi": "Enjektör arızası", "aile_sorunu": "renault-k9k/enjektor", "...": "..." } ] }
  ]
}
```

| Alan | Açıklama |
| --- | --- |
| `aileler[].id` | Küçük harf, rakam ve tirelerden oluşan benzersiz kimlik |
| `aileler[].tur` | `motor`, `sanziman` ya da `sistem` (ör. AdBlue, 48V hafif hibrit, xDrive aktarma) |
| `aileler[].aciklama` | Ailenin hangi modellerde ve hangi yıllarda kullanıldığı (en fazla 500 karakter) |
| `aileler[].kronik_sorunlar[]` | Kayda özgü sorunlarla aynı yapı ve aynı kaynak kuralı (en az iki site); ek olarak aile içinde benzersiz `id` |
| `arac_listesi[].aileler` | Kaydın bağlı olduğu aile kimlikleri |
| `kronik_sorunlar[].aile_sorunu` | `aile_id/sorun_id`. Kaydın kendi sorununun, o aile sorununun bu modelde de bildirildiğini gösterir; görüntüleyicide aile sorunu yerine bu kayıt gösterilir |

Kurallar:

- Bir kaydın en az bir kayda özgü sorunu **ya da** en az bir ailesi olmalıdır. Kayda özgü sorunu olmayıp yalnızca ailesi
  olan kayıt **◐ (yalnızca ortak aile kaynağıyla)** sayılır: o modele özgü bir şikâyet doğrulanmamıştır, gösterilen sorunlar
  aynı motoru ya da şanzımanı kullanan diğer modellerin kaynaklarına dayanır. Görüntüleyicide bu sorunlar kesik
  çerçeveli "Ortak aile" etiketiyle, kayda özgü bildirimi de olanlar "Aile: ... · bu modelde de bildirilmiş" etiketiyle gösterilir.
- Aile bağı otomatik kurulmaz: her bağ modelin, üretim yılının ve motor kodunun eşleştiği bilinen bir kombinasyona
  dayanır; emin olunmayan eşleşme eklenmez. Kanıt yalnızca bir motor sürümü için varsa aile o sürüme göre daraltılır
  (ör. VAG 1.2 TSI ve 1.4 TSI ayrı aileler; 1.6 TDI enjektörü ayrı, EGR / DPF ayrı).
- Hangi modelin hangi motor ya da şanzımanla (hangi yıllarda, Türkiye'de) satıldığı bilgisi kaynaklarla tek tek doğrulanmamıştır; editoryal bilgiye dayanır ve
  yalnızca ◐ kayıtlarında değil tüm aile bağlarında geçerlidir. Hatalı bir eşleşme görürseniz kaydı ya da aile bağını düzeltin; satın almadan önce
  aracın motor kodunu ruhsattan ya da şasi numarasından kontrol edin.
- Her aile en az bir kayıtta kullanılmalıdır; bilinmeyen aileye ya da aile sorununa işaret eden ya da kaydın bağlı olmadığı
  aileden `aile_sorunu` yazan kayıt doğrulayıcı hatasıdır.
- Aile sorunlarının kaynakları da `KAYNAKLAR.md` site ve kullanım sayımlarına dahildir.

## Model geneli kayıtlar

Her sorun motor ya da şanzımandan gelmez: cam tavandan su alma, kapı kilidi arızası, boya atması, multimedya
donması, ön takım sesi gibi sorunlar modelin kendisine (kasaya, nesle) bağlıdır ve motor sürümüne göre değişmez.
Bunlar motor kayıtlarına tek tek yazılmak yerine, aynı modelin **model geneli** kaydında bir kez toplanır:

```json
{ "marka": "Volkswagen", "model": "Golf 7 / 7.5 (2012-2020)", "motor": "Tüm motorlar (model geneli)",
  "uretim_yillari": { "baslangic": 2012, "bitis": 2020 },
  "kronik_sorunlar": [ { "sorun_adi": "Cam tavan çerçevesinde çatlak ve içeri su sızması", "risk_seviyesi": "Orta",
                         "kaynaklar": ["https://...", "https://..."] } ] }
```

- `motor` alanı sabit olarak `Tüm motorlar (model geneli)` yazılır; görüntüleyicide koyu kenarlı, "Model geneli" etiketli ayrı kart olarak görünür.
  Model geneli kayıt motor/şanzıman ailesine bağlanamaz (`aileler` yazılamaz) ve en az bir sorunu olmalıdır.
- Sorunlar aynı kaynak kuralına uyar: en az iki farklı site ve en az biri deneyim ya da resmî türünde (şikâyet, forum, anket, haber, dava haberi).
- **`tahmini_km_araligi` bu kayıtlarda isteğe bağlıdır.** Sızdırmazlık, boya, iç mekân ve elektronik sorunları yaşa ve kullanıma bağlıdır;
  kaynaklar genellikle kilometre yazmaz. Kilometre yoksa aralık uydurulmaz, alan boş bırakılır ve görüntüleyici çubuk yerine
  "Kaynaklarda kilometre bilgisi yok" yazar. Kaynak kilometre veriyorsa (ör. "ilk 30 bin km'de") yine yazılır. Kilometre filtresi
  kilometresi olmayan sorunları elemez.
- Bir sorun yalnızca belli motor sürümlerinde bildiriliyorsa bu sorun adında söylenir (ör. "1.4 sürümlerde bildirildi").
  Yalnızca bir motora bağlı sorunlar yine motor kaydına ya da ailesine yazılır.
- Risk seviyesi bu kayıtlarda da aynı ölçekle verilir: **Düşük** kozmetik ya da konfor sorunları (boya, döşeme, ses), **Orta** onarım gerektiren
  ya da iç mekâna su sızdıran sorunlar, **Yüksek** güvenliği (fren, direksiyon, hava yastığı, aydınlatma) ya da elektroniği tehlikeye atan sorunlar.
- Model geneli taraması modelden modele yapılır ve `KAPSAM.md` içinde ayrı izlenir: ✓ sorun bulunan, – aranıp iki bağımsız site bulunamayan
  (nedeniyle; ör. yalnızca Şikâyetvar'da geçen sorunlar). Satırı olmayan bir modelde bu sorunlar henüz aranmamıştır; satırı olmaması
  "sorun yok" demek değildir.

## Dönem kırılımı

Aynı motor her üretim yılında aynı sorunu yaşamaz: bir revizyon sorunu azaltabilir,
bir parti sorunu artırabilir. `donem_kirilimi` bu farkı yıl aralıklarıyla gösterir.
Örneğin Astra K 1.4 Turbo'da piston ve segman kırılması 2015-2018 üretiminde
`Yaygın`, 2019 sonrasında (yeniden tasarlanan segmanlar ve yeni motor kodlarıyla)
`Görülebilir` olarak işaretlidir.

| `durum` | Anlamı |
| --- | --- |
| `Yaygın` | Kaynaklar bu dönem için sorunu sık ve tekrar eden biçimde bildiriyor |
| `Görülebilir` | Bildirimler var ama sık değil ya da dönem sınırı net değil |
| `Seyrek` | Kaynaklar sorunun azaldığını ya da düzeltildiğini yazıyor; risk sıfır demek değildir |

Okurken dikkat edilecekler:

- `durum`, kaynaklardaki bildirim yoğunluğuna dayanan editoryal bir sınıflandırmadır; istatistik değildir.
- Listelenmeyen yıllar için kaynaklarda ayrı bir bilgi bulunamamıştır. Bu, "sorun yok" anlamına gelmez.
- Dönemler yıla göre sıralı ve birbiriyle çakışmayan olmalı, aracın `uretim_yillari` aralığı içinde kalmalıdır.
- Revizyon yıllarını kaynaklar farklı verebilir (ör. 7 mm zincirden 8 mm zincire geçiş). Bu durumda `not` alanında belirtilir; şasi numarasıyla kontrol edin.

## Motor versiyonları

Aynı motor adı altında birden fazla versiyon olabilir: farklı motor kodu, güç, şanzıman, kasa/nesil ya da
makyaj. Veritabanı bunları şu kurala göre ele alır:

- **Kaynaklar versiyonları ayırt ediyorsa ayrı kayıt açılır.** Sorun listesi, kilometre aralığı ya da risk
  versiyona göre değişiyorsa tek kayıtta birleştirmek yanıltır. Örnekler: Mercedes M271 Kompressor (W203 / W204,
  2002-2010) ile M271 EVO CGI turbo (W204, 2009-2014); BMW N47 zincir sorunu için 320d (N47D20), 116d (N47D16) ve
  520d (N47D20); Nissan Qashqai J11'de 1.5 dCi / 1.6 dCi (K9K / R9M) turbo hortumu, 1.6 dCi Xtronic CVT ve
  1.2 DIG-T Xtronic CVT; aynı 1ND-TV motorlu Toyota Corolla E150 ile Auris.
- **Versiyon kayıt içinde yıla göre değişiyorsa `donem_kirilimi` kullanılır** (yukarıya bakın).
- **Kaynaklar ayırt etmiyorsa kayıt bölünmez.** Örneğin N47'de 177 ve 184 bg sürümleri arasındaki fark yalnızca
  forum yorumlarında geçiyor ve doğrulanmadı; bu yüzden ayrı kayıt yok, fark ilgili `donem_kirilimi` notunda.
- Aynı motoru paylaşan modeller ayrı kayıt olarak durur (ör. 1.6 TDI CAYC: Polo ve Caddy). Bir kaydın verisi başka
  bir modelin kayıtlarından alındıysa bu metinde belirtilir (ör. Opel Grandland X DV5 kilometre aralığı Peugeot / Citroën
  kaydındaki kaynaklardan).
- Motor ve şanzıman kaynaklı sorunlar (ör. 1.5 TSI yağ eksiltmesi, 48V hafif hibrit sistem arızası, K9K enjektörü) ortak
  aileye yazılır ([Ortak motor ve şanzıman aileleri](#ortak-motor-ve-şanzıman-aileleri-aileler)). Modele özgü şikâyeti de
  olan kayıtlar kendi sorununu `aile_sorunu` ile aileye bağlar; modele özgü kaynağı olmayanlar ◐ olarak yalnızca aile
  sorunlarını gösterir ve planda notla belirtilir. Aile sorunu başka bir modelin kaynağına dayandığı için bu kayıtlar
  doğrudan kanıtı sınırlı sayılır.

## Elektrikli araçlar

Elektrikli araçlar (yalnızca tam elektrikliler; hibrit ve plug-in hibritler dahil değildir) diğer kayıtlarla aynı
kurallarla eklenir: her sorun için en az iki site, bunlardan en az biri deneyim ya da resmî türünde. Elektrikli
araçlara özgü noktalar:

- `motor` alanı `Elektrik` ile başlar; sorunlar batarya, şarj (dahili şarj cihazı OBC, entegre şarj kontrol ünitesi ICCU), 12V yardımcı akü, elektrik tahrik sistemi ve yazılım gibi parçalara aittir.
- Filtre kutusundaki "Yalnızca elektrikli araçlar" seçeneği ya da arama kutusuna `elektrik` yazmak yalnızca bu kayıtları gösterir.
- Filo genç olduğu için (Türkiye'de çoğu 2022 sonrası) kilometre verisi azdır; şikâyet sahipleri çoğu zaman kilometre yazmaz. Kaynakta kilometre yoksa aralık araçların yaşına göre kaba tahmin edilir ve bu ilgili `detay` metninde söylenir.
- Aynı batarya ve motor değerlerine sahip kardeş modellerde (ör. Opel Astra Electric ve Peugeot e-308: 54 kWh, 115 kW / 156 PS) modele özgü ikinci site bulunamazsa kardeş modelin kaynağı kullanılabilir; bu durum ilgili kaydın `detay` metninde açıkça yazılır ve o kayıt doğrudan kanıtı sınırlı sayılır (Astra Electric gibi).
- Bir model iki batarya / güç sürümüyle satılıyorsa (ör. Peugeot e-208 / e-2008, Opel Mokka, Citroën ë-C4: 50 kWh / 136 PS ve 2024 sonrası 54 kWh / 156 PS) ve kaynaklar sürümleri ayırt etmiyorsa kayıt bölünmez; `motor` alanı iki sürümü söyler, `donem_kirilimi` hangi dönemin hangi sürüme denk geldiğini açıklar.
- Geri çağırma kayıtlarının çoğu ABD (NHTSA) ya da Avrupa (KBA) kaynaklıdır. Türkiye'deki araçların kapsamı doğrulanamıyorsa bu kayıtta belirtilir; doğrulanamayan aileler `KAPSAM.md` içinde nedenleriyle `–` olarak durur.

## Ayrıntılar (`detay`)

Sorun satırı "ne bozulur, hangi belirtiyi verir" sorusunu yanıtlar; `detay` ise sonrasındaki soruları
kaynakların anlattığı kadarıyla yanıtlar. Beş alanı vardır; hepsi isteğe bağlıdır (en az biri dolu
olmalı, her biri en fazla 800 karakter):

| Alan | İçerik |
| --- | --- |
| `neden` | Kaynaklarda öne sürülen neden ya da nedenler |
| `teshis` | Nasıl anlaşılır: ayırt edici belirti, kontrol sırası, karıştırılan benzer arızalar |
| `cozum` | Kullanıcı ve ustaların bildirdiği yaygın çözüm; tartışmalı olanlar belirtilir |
| `maliyet` | Yalnızca kaynakta geçen rakamlar, kaynağı ve dönemi belirtilerek. Rakam bulunamadıysa alan yazılmaz |
| `onlem` | Rehber ve kullanıcıların önerdiği önlemler, kaynakların verdiği kontrol aralıkları |

Okurken dikkat edilecekler:

- Kaynak anlatımlarının özetidir; üreticinin ya da yetkili servisin talimatı değildir.
- `neden` alanı kaynaklarda öne sürülen açıklamaları verir, kesin teknik tespit olmayabilir.
- Maliyetler bildirim tarihine göre eskir; güncel fiyat değil büyüklük sırası olarak okuyun. Tarihi belli olmayan ya da başka motora ait rakamlar alınmaz.
- Bilgi tek bir kaynaktan geliyorsa metinde kaynağın adı geçer (ör. "Carsece rehberi ... tahmin ediyor"); bilgi yalnızca bir parça satıcısı ya da blogdan geliyorsa bu belirtilir.
- Kaynakların ayrıştığı noktalar (ör. kabul edilebilir yağ eksiltme sınırı) tek bir değere indirilmez, değerler kaynaklarıyla birlikte sıralanır.
- Başka bir model, motor ya da pazarın (ör. ABD servis bülteni, geri çağırma ya da fiyatı) bilgisi kullanıldıysa bu metinde söylenir; Türkiye için geçerliliği doğrulanmadıysa o da belirtilir.
- Kaynakta bulunmayan alan yazılmaz: bütün sorunların ayrıntısı vardır ama her sorunda beş alanın hepsi dolu değildir.

## Kaynak kuralı

Bir sorun veritabanına ancak şu koşullarla girer:

1. `kaynaklar` içinde **en az iki farklı sitenin** sayfası bulunur.
2. Kaynaklardan en az biri deneyime ya da resmî belgeye dayanır: forum, şikâyet
   platformu, sahip anketi, dava haberi, haber veya resmî belge. Yalnızca blog,
   parça satıcısı veya derleme sitesiyle desteklenen sorunlar alınmaz.
3. Her sitenin `data/kaynaklar.json` içinde tanımlı olması gerekir.

Kullanılan sitelerin listesi ve güvenilirlik notları için
[KAYNAKLAR.md](KAYNAKLAR.md), doğrulama sırasında yapılan değişiklikler için
[DOGRULAMA_RAPORU.md](DOGRULAMA_RAPORU.md), kapsam ve ilerleme için [KAPSAM.md](KAPSAM.md)
dosyalarına bakın.

## Görüntüleme

```sh
python3 scripts/viewer_uret.py
```

`viewer/index.html` oluşur; veriler dosyanın içine gömülür, sunucu gerekmez. Sayfada marka, model, motor
koduna göre arama yapabilir, model yılı ve kilometre girerek o yıl ve kilometre için geçerli sorunları
görebilirsiniz. Yıl kırılımı olan sorunlarda girdiğiniz model yılının hangi döneme düştüğü işaretlenir.
Ayrıntısı olan sorunlarda "Ayrıntılar" bölümü açılır; "Tüm ayrıntıları aç" kutusu hepsini birden açar ve
arama kutusu ayrıntı metinlerinde de arar.

Sayfanın altındaki "Kayıt açılmayan gruplar" bölümü, `data/kapsam.json` içinde kaydı olmayan satırları gösterir:
**Arandı** işaretlilerde kaynak arandı ama iki siteyle desteklenen, o motora özgü bir sorun bulunamadı (nedeni yazılıdır);
**Sırada** işaretliler listeye alındı ama henüz araştırılmadı. Arama kutusu, marka, model yılı ve elektrikli filtresi bu
bölüme de uygulanır; sayfanın üstündeki bağlantı bölümü açar. Bir araç ne kayıtlarda ne de bu bölümde yoksa planda hiç
yer almıyordur. "Q3", "X5" gibi kısa model kodları kelime başında aranır (ör. "DQ381" içindeki "q3" eşleşmez).

## Doğrulama

```sh
python3 scripts/dogrula.py
python3 -m unittest discover tests
```

Betik; zorunlu alanları, tanımsız alanları, risk seviyesi değerlerini,
kilometre aralığı biçimini (alt sınırın üst sınırdan küçük olması dahil),
üretim yıllarını ve dönem kırılımı kurallarını (sıralı, çakışmayan, üretim yılları
içinde), `detay` alanlarını (tanımlı beş alan, boş olmayan, en fazla 800 karakter), aynı marka/model/motor üçlüsünün tekrar edilmemesini, aile kurallarını
(benzersiz kimlik, bilinen ve kullanılan aile, geçerli `aile_sorunu` bağı, en az bir sorun ya da aile) ve kaynak kuralını
kontrol eder. Hata bulunursa sıfırdan farklı bir çıkış koduyla sonlanır; başarılı
çalışmada yalnızca iki siteyle desteklenen (sınırlı doğrulamalı) madde sayısını da yazar.

## Katkı

1. `data/araclar.json` içine yeni aracı marka ve model sırasını koruyarak ekleyin.
2. Her sorun için en az iki farklı sitede destekleyici sayfa bulun ve adreslerini
   `kaynaklar` alanına yazın. Yeni bir site kullanıyorsanız `data/kaynaklar.json`
   içine ekleyin.
3. Aynı motoru paylaşan araçlar (ör. 1.5 dCi kullanan Renault ve Dacia
   modelleri) her biri ayrı kayıt olarak eklenir. Kaynakların motor kodu, güç, şanzıman ya da
   nesil bakımından ayırt ettiği versiyonlar da ayrı kayıttır; ayırt edilmeyenler bölünmez
   ([Motor versiyonları](#motor-versiyonları)).
4. `python3 scripts/dogrula.py` komutunun hatasız tamamlandığından emin olun,
   ardından `python3 scripts/kaynaklar_md_uret.py` ve `python3 scripts/kapsam_md_uret.py` ile
   `KAYNAKLAR.md` ve `KAPSAM.md` dosyalarını yenileyin.
5. Kaynak bulunamayan bir model/motor grubu için sorun uydurmayın; `data/kapsam.json`
   içinde ilgili satıra `"sonuc": "yetersiz-kanit"` ve nedenini yazın.
6. `data/kapsam.json` satırlarında birleşik etiket (ör. `1.4 TSI / 1.6 TDI`) kullanıyorsanız her
   alternatif `eslesme` içinde ayrı parça olmalı ve en az bir kayda denk gelmelidir; yalnızca bir
   kısmı kayıtlıysa satırı bölün (testler denetler).
7. Bir motor ya da şanzıman sorunu en az iki modelde bildiriliyorsa onu `aileler` içine alın; aynı motoru kullandığı
   kesin olan modelleri aileye bağlayın (kayıt yoksa `kronik_sorunlar: []` ile yalnızca aileli kayıt açın) ve plan
   satırına modele özgü kaynak aranmadığını ya da bulunmadığını not edin. Motor kodu, model yılı ya da piyasa
   (Türkiye'de satılıp satılmadığı) belirsizse bağ kurmayın.
