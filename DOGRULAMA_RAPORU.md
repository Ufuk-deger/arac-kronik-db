# Doğrulama raporu

Tarih: 2026-10-24

Rapor üç aşamayı kapsar. Aşağıdaki ilk bölümler 1. aşamayı (ilk sürümün doğrulanması) anlatır; [2. aşama](#2-aşama-en-çok-satan-modellerin-motor-grupları-ve-yıl-kırılımı) en çok satan modellerin eklenmesini ve yıl kırılımını, [3. aşama](#3-aşama-sorun-ayrıntıları) her soruna eklenen ayrıntıları anlatır.

## 1. aşama: ilk sürümün doğrulanması

İlk sürüm 31 araç ve 82 kronik sorun içeriyordu. Bu sorunların çoğu hafızadan yazılmıştı ve kaynağı yoktu. Bu çalışmada her sorun web aramasıyla kaynaklara karşı kontrol edildi, desteklenmeyenler çıkarıldı, yeni bulunanlar eklendi.

| | Önce | Sonra |
| --- | ---: | ---: |
| Araç/motor kaydı | 31 | 30 |
| Kronik sorun | 82 | 72 |
| Kaynağı olan sorun | 0 | 72 |
| Farklı kaynak sitesi | 0 | 55 |

Kaldırılan: 14 sorun (bir kayıt tamamen çıktı). Eklenen: 4 sorun. Adı, parçası, belirtisi, kilometre aralığı veya risk seviyesi düzeltilen: aşağıdaki tabloda.

## Yöntem ve sınırlar

- Ölçüt: her sorun için **en az iki farklı sitede** destekleyen sayfa ve bunlardan en az biri deneyime ya da resmî belgeye dayanan türde (forum, şikâyet, anket, dava haberi, haber, resmî belge). `scripts/dogrula.py` bu kuralı denetler.
- Dış sitelere doğrudan erişim bu ortamda kapalıydı (`otopark.com`, `andcetin.com`, `carcomplaints.com` dahil). Kaynaklar web araması sonuçlarından toplandı; bağlantılar sayfa başlığı ve arama özetine göre sorunlarla eşlendi, sayfaların tamamı okunmadı. Bir bağlantıda iddiayı bulamazsanız o maddeyi bildirin.
- Arama özetleri, sayfaları yorumlayan bir araçtan geldi. Rakamlar (kilometre, maliyet, model yılı) ve alıntılar için asıl sayfaya bakmak gerekir.
- Kilometre aralıkları hâlâ tahmindir. Kaynakta rakam varsa ona göre güncellendi, yoksa önceki tahmin korundu.

## K9K 1.5 dCi kol yatağı sarması

**Haklıydınız: bu madde Duster (2010-2017) ve Megane 3 / Fluence (2009-2016) için kaynaklarca desteklenmiyor, kaldırıldı.** Madde benim hafızamdan eklenmişti.

Bulunanlar:

- Planète Renault forumunda bir moderatör, 1.5 dCi'de yatak sorunlarının **2003-2006** arasında görüldüğünü, 2007'den sonra tedarikçi değişikliğiyle motorun çok güvenilir olduğunu yazıyor: [post930116](https://www.planeterenault.com/forum/post930116.html). Tek moderatör görüşü, resmî açıklama değil.
- Macar bir motor yenileyicinin yazısına göre ilk motorlardaki biyel yatakları yeterli kalitede değildi ve Renault bunu kabul etmişti; aynı yazı motorun bakımla "en iyi küçük dizellerden" olduğunu söylüyor: [Autónavigátor](https://www.autonavigator.hu/cikkek/a-renault-remek-1-5-dci-je-a-motorfelujito-szemevel).
- Araclo'nun K9K sayfası biyel yatağı sarmasını yalnızca **2006 öncesi motorlar** için listeliyor: [araclo.com/motorlar/k9k-1-5dci](https://www.araclo.com/motorlar/k9k-1-5dci/kronik-sorunlar).
- arabam.com'un dCi yazısı motorun "büyük bir kronik sorunu yoktur" diyor: [arabam.com](https://www.arabam.com/blog/danisman/renault-dci-motor-nedir-kronik-sorunlari-nelerdir/). Aynı sitede tek bir vaka var: 2013 Fluence, yaklaşık 230.000 km, yağlama kaybıyla ana yatakların sarması: [arabam.com](https://www.arabam.com/blog/genel/renault-fluence-1-5-dci-bir-garip-motor-arizasi/).
- Şikâyetvar'da 1.5 dCi şikâyetleri EDC şanzıman, elektronik el freni, kapı kilidi gibi konularda yoğunlaşıyor; yatak sarması için bir şikâyet örüntüsü çıkmadı.

Sonuç: 2009 sonrası K9K için kol yatağı sarması kronik sorun olarak kanıtlanamadı. Sorun, ilk üretim yıllarına ve bakımsızlığa bağlanıyor. Bu yıllara ait araçlar (Megane 2, Clio 3 vb.) şu an veritabanında yok.

Aynı motorda kaynaklarla desteklenen sorunlar: enjektör arızası, EGR tıkanması, Megane 3'te Delphi yüksek basınç pompası talaşı ve EDC şanzıman.

## Kaldırılan maddeler

| Araç | Sorun | Neden |
| --- | --- | --- |
| Dacia Duster 1.5 dCi | Kol yatağı sarması | Yukarıdaki bölüm. |
| Renault Megane 3 / Fluence 1.5 dCi | Kol yatağı sarması | Yukarıdaki bölüm. |
| Renault Megane 3 / Fluence 1.5 dCi | Çift kütleli volan arızası | Kaynak bulunamadı. EDC'li araçta çift kütleli volan yok; manuelde yalnızca debriyaj seti şikâyetleri çıktı. |
| Fiat Egea 1.3 Multijet | Triger zinciri uzaması | Egea'ya özgü bildirim yok. Zincir kanıtları Panda ve Linea için; Linea'da tutuldu. |
| BMW 320d (N47) | DPF tıkanması | N47'ye özgü kaynak yok, yalnızca genel dizel bilgisi. |
| Chevrolet Cruze 1.6 | Külbütör kapağı contası ve PCV kaçağı | Güçlü kanıtlar ABD'deki 1.4T/1.8 motorlar için. 1.6 için yalnızca "kapağı ayarlı sıkın" uyarısı çıktı. |
| Honda Civic FD6 | Motor takozu yıpranması | Tek bir rehber yazısı ve Consumer Reports'ta "küçük sorun" kaydı; kronik olduğuna dair kaynak yok. |
| Hyundai Tucson 1.6 T-GDI | Emme supaplarında karbon birikimi | Yalnızca genel GDI yazıları, bir Polonya makalesi ve parça siteleri. Hyundai belgesi veya Türkçe kaynak yok. |
| Opel Astra J 1.4 Turbo | Turbo soğutma hattı ve devirdaim kaçağı | Tek bir parça sitesi. Turbo boruları için kaynak yok. |
| VW Golf 6 1.4 TSI | Turbo wastegate çıngırtısı | Belgelenmiş vakalar GTI/GLI/2.0T için. 1.4 TSI (CAXA) için ve Türkçe kaynak yok. |
| VW Passat B6 2.0 TDI (BKP) | Silindir kapağı çatlaması | Kaynak bulunamadı. |
| VW Polo 1.2 3 silindir | Ateşleme bobini arızası | Tek kaynak (Honest John). |
| Toyota Corolla E170 1.6 Valvematic | Devirdaim pompası sızıntısı ve Valvematic aktüatör arızası (kayıt tamamen çıktı) | Devirdaim için tek şikâyet (hibrit modelle karışıyor), Valvematic için yalnızca bir derleme sitesi. |

Bunlar "yanlış" kanıtlanmış değil, "doğrulanamadı". Kaynak bulursanız `data/araclar.json` içine `kaynaklar` ile geri eklenebilir.

## Düzeltilen maddeler

| Araç | Sorun | Değişiklik | Neden |
| --- | --- | --- | --- |
| Audi A4 B8 | PCV valfi | Parça "PCV valfi ve ön krank keçesi" oldu. | Audi'nin 2013 servis bülteni (TSB 17 13 43), 2009-2011 2.0T için aşırı yağ tüketiminde bu iki parçanın değişimini öneriyor ([CarComplaints](https://www.carcomplaints.com/news/2021/audi-oil-consumption-lawsuit-pistons.shtml)). |
| Audi A4 B8 | Multitronic | Kilometre 100-180 bin yerine 80-150 bin. | Araclo mekatronik için 80-120 bin yazıyor. |
| BMW 320d (N47) | EGR soğutucusu ve valfi | Risk Orta yerine Yüksek; geri çağırma notu eklendi. | BMW, 320d dahil birçok model için EGR soğutucusu geri çağırması yürüttü ([CarGuide.PH](https://www.carguide.ph/2018/08/bmw-recalls-42-models-including-320d.html?m=1)). |
| BMW 328i/320i (N20) | Elektrikli devirdaim pompası | Risk Yüksek yerine Orta; "konnektör" eklendi. | Arıza sıklığı kaynaklarda tartışmalı. Bir forum yazısı, BMW'nin pompa konnektörü için geri çağırma (24V-608) yaptığını aktarıyor; resmî sayfa doğrulanmadı. |
| Citroen C-Elysee ve Peugeot 301 | Enjektör | "Enjektör pulu kaçağı" yerine "Enjektör arızası ve enjektör dibi kaçağı". | Pul kaçağının kanıtı Ford 1.6 TDCi için. Bir forum yazarı 301'in 92 bg motorunun kaçırmayabileceğini söylüyor. |
| Dacia Duster | Enjektör | Kilometre 60-180 bin. | L'argus 2011'e kadar enjektör arızası, sonrasında duyarlılık anlatıyor; bir Duster'da 33 bin km'de vaka var. |
| Fiat Egea 1.6 | DCT şanzıman | "Kuru tip" ifadesi çıkarıldı. | Kaynaklar kavrama tipini belirtmiyor. |
| Fiat Linea | Triger zinciri | Risk Yüksek yerine Orta. | Kaynaklar zincir ömrünün yağ bakımına bağlı olduğunu söylüyor, sıklık verisi yok. |
| Ford Focus 3 Powershift | Kavrama silkelemesi | "Kavrama yuvası sızıntısı" eklendi. | Ford'un 2012-2016 Focus servis bülteni silkelemeyi ve bazı araçlarda kavrama yuvasından yağ sızmasını anlatıyor ([NHTSA](https://static.nhtsa.gov/odi/tsbs/2016/SB-10092372-5448.pdf)). |
| Honda Civic FD6 | Arka lastik | "İç kenar aşınması" yerine "düzensiz aşınma (2006-2007 servis bülteni)". | Honda'nın Şubat 2008 bülteni 2006-2007 Civic'te arka üst salıncaklar nedeniyle düzensiz/hızlı aşınmayı anlatıyor. |
| Hyundai Tucson | 7DCT | "Aşırı ısınma" çıkarıldı; ad "kalkışta tereddüt ve silkeleme" oldu. | NHTSA belgeleri kavrama mantığı yazılımını anlatıyor; aşırı ısınma yalnızca tek kullanıcı anlatımı. |
| Mercedes C W204 | Piezo enjektör | Yalnızca C220/C250 CDI; "motorun stop etmesi" çıkarıldı; kilometre 50 bin'den. | AUTO BILD'e göre C200 CDI manyetik enjektörlü olduğundan etkilenmiyor; kaynaklarda uyarı lambası, acil mod ve düzensiz çalışma geçiyor, stop etme geçmiyor. |
| Mercedes 7G-Tronic | İletken plaka | Kilometre 80-150 bin. | Kaynaklardaki mil değerleri kilometreye çevrildi. |
| Nissan Qashqai | Xtronic CVT ve zincir | CVT kilometre 40-150 bin; zincir riski Yüksek yerine Orta. | 2020 model bir araçta 37 bin km'de arıza şikâyeti var. Zincirin kanıtı dolaylı (servis bülteni, tek şikâyet). |
| Opel Astra H | Twinport klape | Ad "klape ve konum sensörü arızası (P1113)" oldu; motor kodu Z16XEP/Z16XER. | Forum yazılarına ve HELLA bültenine göre sensör manifolda entegre; parça komple manifold olarak temin ediliyor. |
| Opel Astra J | PCV | Ad "PCV diyaframı ve emme manifoldu kontrol valfi arızası" oldu. | Forumlar diyaframla birlikte manifolddaki tek yönlü valfi de gösteriyor. |
| Peugeot PureTech | Triger kayışı | Kilometre 40-120 bin. | Yazarlar ve sahipler 40-60 bin km'de değişim öneriyor; bazı kayışlar daha erken bozulmuş. |
| Peugeot THP | Emme supabı karbonu | Kilometre 70-130 bin. | Araclo 70.000 km sonrası diyor. |

## Eklenen maddeler

Başka bir sitede görülüp başka sitelerce doğrulanan sorunlar.

| Araç | Sorun | İlk görüldüğü yer | Doğrulayan |
| --- | --- | --- | --- |
| Renault Megane 3 / Fluence 1.5 dCi | Yüksek basınç yakıt pompası talaşı (Delphi) | Fiches-Auto.fr, Araclo | Honest John forumu |
| Opel Astra H | Yağ soğutucusu sızıntısı (yağ-su karışması) | OTOPARK.COM forumu | DonanımHaber, Astra Owners Network |
| Chevrolet Cruze 1.6 | Ateşleme bobini arızası | OTOPARK.COM forumu | DonanımHaber |
| Fiat Linea | Dualogic kavrama (debriyaj) aşınması | DonanımHaber | Fiat Forum |

## Yalnızca iki siteyle desteklenen maddeler

Bunlar kuralı geçti ama sınırda. Önce bunlara bakılması yararlı olur:

- BMW F30 N20: yağ filtresi yuvası contası kaçağı (Bimmerpost, FCP Euro)
- Chevrolet Cruze: ateşleme bobini arızası (OTOPARK.COM, DonanımHaber)
- Ford Focus 1.6 TDCi: enjektör pulu kaçağı, turbo yağ besleme süzgeci, DPF tıkanması (Ford Owners Club, French Car Forum / Honest John)
- Skoda Octavia: devirdaim pompası ve termostat modülü (BRISKODA, DonanımHaber)
- Toyota Corolla E150: enjektör arızası (Araclo, Şikâyetvar)
- VW Passat B6: DSG (DQ250) mekatronik ve kavrama (Şikâyetvar, AustralianCar.Reviews)
- VW Polo 1.2: triger zinciri uzaması (Honest John, PicoAuto)

Yalnızca yurtdışı kaynaklı 12 madde var (Türkçe kaynak bulunamadı): örneğin BMW N20'nin üç maddesi, Ford Focus 1.6 TDCi, Honda Civic FD6, Mercedes C W204, Astra H Twinport ve Polo. Türkiye'de sık görülmeyen veya yurtdışı ağırlıklı konuşulan sorunlar olabilir.

## Çelişen veya tartışmalı noktalar

- **Honda 1.5 Turbo yağ seyrelmesi:** ABD'de Honda 2016-2018 Civic için kimi motor parçalarında (eksantrik, külbütör, buji) garantiyi 6 yıla ve sınırsız kilometreye uzattı ([Consumer Reports](https://www.consumerreports.org/car-recalls-defects/honda-extends-warranty-on-troubled-turbo-engines/)). Türkçe bir forumda sorunun çoğunlukla CR-V'de görüldüğü yazılıyor.
- **1.2 TCe / DIG-T (H5Ft) yağ tüketimi:** Fransız tüketici örgütü UFC-Que Choisir 2012-2016 arası üretilen motorlarda aşırı yağ tüketimi ve motor arızası riskini bildirdi; Renault kusur olduğunu reddediyor ([The Connexion](https://connexionfrance.com/article/French-news/Renault-cars-have-severe-defect-says-consumer-group)).
- **DQ200 mekatronik:** And Mehmet Çetin 2012 sonrası ikinci nesil ünitede mekatronik arızasının daha az görüldüğünü yazıyor ([andcetin.com](https://andcetin.com/dsg-sorunlar-ve-dq200-kullanmayan-modeller-39/)). Octavia A7 bu gruba giriyor, ama BRISKODA'da 2013-2020 Octavia için mekatronik arızası başlığı var.
- **1.0 EcoBoost kayışı:** Aynı yazıda 2018-2019 sonrası Ford'un zincire geçtiği, yağ pompası kayışının ise yağ içinde kaldığı belirtiliyor. Kaynaklar arasında yıl farkı var.

## Veritabanına alınmayan, kaynaklarda geçen konular

İkinci bir siteden doğrulanamadı veya veritabanındaki araçlarla ilgili değil:

- Ford Focus MK3 direksiyon kutusu yağ kaçağı (OTOPARK.COM forumu)
- Peugeot 307 "Antipollution Fault" (EGR elektrovanası, yakıt filtresi) (OTOPARK.COM forumu)
- Opel Astra K 1.4 Turbo LSPI ve piston kırılması (1. aşamada Astra K veritabanında yoktu; 2. aşamada eklendi)
- Mercedes OM651 zincir gergisi conta geri çağırması, 2015 (tek kaynak, AustralianCar.Reviews)
- Peugeot 3008 (2020) kam zinciri geri çağırması (Şikâyetvar alıntısı; 1.6 THP'yi kapsayıp kapsamadığı belirsiz)
- Ford 1.0 EcoBoost yağ pompası kayışı gergi kolu geri çağırması (ABD pazarındaki Focus ve EcoSport)

## 2. aşama: en çok satan modellerin motor grupları ve yıl kırılımı

Tarih: 2026-10-24

İkinci aşamada kapsam son 10-15 yılın en çok satan araçlarına (yaklaşık 2011 model yılı ve sonrası) genişletildi ve sorunlar üretim yılına göre kırılmaya başlandı. Kapsamın tamamı [KAPSAM.md](KAPSAM.md) dosyasında; plan `data/kapsam.json` içinde.

| | 1. aşama sonu | 2. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 30 | 97 |
| Kronik sorun | 72 | 156 |
| Yıl kırılımı olan sorun | 0 | 32 |
| Marka | 17 | 19 |
| Farklı kaynak sitesi | 55 | 60 |

### Ne yapıldı

- **Marka seti:** 2025 ODMD otomobil satışlarında ilk 15 marka. BYD, Togg, Tesla ve Chery elektrikli ya da 2023 sonrası girmiş markalar olduğu için dışarıda; yerlerine sıradaki markalar (Nissan, Ford, Kia, Dacia) alındı. İlk 10 sıra birden fazla haberde tutarlı, 11. sıradan sonrası rakamlar tek bir tablodan alındı ve doğrulanamadı; ayrıntı KAPSAM.md'de.
- **Genelden özele:** Plan 178 model/motor grubundan oluşuyor ve üç kademeye ayrıldı. Kademe 1'in 85 satırının hepsi işlendi: 74'ü veritabanına girdi, 11'i kanıt yetersiz olduğu için eklenmedi (aşağıda). Kademe 2 ve 3'te 66 satır sırada.
- **Yeni alanlar:** her kayıtta `uretim_yillari`, kaynaklar fark belirtiyorsa sorunda `donem_kirilimi` (dönem, `Yaygın`/`Görülebilir`/`Seyrek` ve not). Eski 30 kayda yıllar eklendi; eski kayıtlardaki 16 soruna, yeni kayıtlardaki 16 soruna yıl kırılımı işlendi.
- **Kural aynı:** her sorun için en az iki farklı site, en az biri forum/şikâyet/haber/resmî türünde. Bu aşamada eklenen 84 sorunun hepsi bu kuralı geçiyor.

### Kaynakların toplanması ve denetimi

- Genel web aramaları çoğunlukla blog ve rehber siteleri döndürdüğü için aramalar şikâyet ve forum sitelerine (Şikâyetvar, DonanımHaber, OTOPARK.COM, Ekşi Sözlük) sınırlanarak tekrarlandı; böylece her sorunun en az bir deneyim kaynağı olması sağlandı.
- Sayfalar yine açılamadı. Bağlantılar arama sonucunda göründüğü başlık ve özete göre sorunlarla eşlendi.
- Yeni eklenen her bağlantının gerçekten arama sonuçlarında geçtiği otomatik denetlendi (uydurma ya da hafızadan yazılmış adres yok). Ardından her kaynağın başlığı ilgili sorunla karşılaştırıldı; bu turda altı zayıf eşleme düzeltildi (aşağıdaki "Düzeltmeler").

### Astra örneği

İstekte Astra J 1.4 Turbo'nun 2019 öncesinde daha sorunlu olduğu, sonrasında güncellendiği belirtilmişti. Kaynaklarda bu tablo **Astra J'de değil Astra K'da** çıkıyor:

- **Astra J (2010-2015) 1.4 Turbo (A14NET)** 1. aşamada kayıtlı (PCV diyaframı ve emme manifoldu kontrol valfi arızası). 2019 gibi bir revizyon yılı bu motor için kaynaklarda çıkmadı; üretim 2015'te bitiyor.
- **Astra K (2015-2021) 1.4 Turbo (B14XFL/B14XFT, 2019 sonrası D14XFL/D14XFT)** için LSPI kaynaklı piston ve segman kırılması 2015-2018 için `Yaygın`, 2019-2021 için `Görülebilir` olarak işlendi. Alman bir ikinci el rehberi 2018 sonundan itibaren OPF'li D10/D14 motorlarda yağ sıyırma segmanlarının yeniden tasarlandığını ve LSPI riskinin belirgin düştüğünü yazıyor. Aynı dönemden 2019-2020 araçlarda da piston kırılması bildiren Şikâyetvar kayıtları var; bu yüzden sorun azaldı ama bitti diye işaretlenmedi. Yıl bazında şikâyet sayısı veren bir kaynak yok; sınıflandırma editoryaldir.

### Yıl kırılımı olan sorunlar

Listelenmeyen yıllar için kaynaklarda ayrı bilgi bulunamadı; bu, sorun olmadığı anlamına gelmez. Dönem notları `data/araclar.json` içinde.

| Model | Motor | Sorun | Dönemler |
| --- | --- | --- | --- |
| Audi A4 (B8, 2008-2015) | 1.8 TFSI / 2.0 TFSI (EA888 Gen2) | Aşırı yağ tüketimi | 2008–2011 Yaygın · 2012–2015 Görülebilir |
| Audi A4 (B8, 2008-2015) | 1.8 TFSI / 2.0 TFSI (EA888 Gen2) | Triger zinciri gergisi arızası | 2008–2011 Yaygın · 2012–2015 Görülebilir |
| BMW 3 Serisi (E90 / F30, 2007-2015) | 320d 2.0 dizel (N47D20) | Triger zinciri uzaması | 2007–2009 Yaygın · 2010–2015 Görülebilir |
| BMW 3 Serisi (F30, 2012-2015) | 320i / 328i 2.0 turbo benzin (N20B20) | Triger zinciri ve plastik kızak arızası | 2012–2014 Yaygın · 2015 Görülebilir |
| Citroen C3 / C3 Aircross (2016-) | 1.2 PureTech 82/110 (EB2) | Yağ banyolu triger kayışının dağılması | 2016–2020 Yaygın · 2021– Görülebilir |
| Citroen C3 / C4 / C5 Aircross (2019-) | 1.5 BlueHDi 100/130 (DV5) | Eksantrik zinciri sesi ve kopması (7 mm zincir) | 2019–2020 Yaygın · 2021–2022 Görülebilir · 2023– Seyrek |
| Ford Fiesta / Focus (2012-2023) | 1.0 EcoBoost | Soğutma sistemi kaçağı ve hararet | 2012–2014 Yaygın · 2015–2016 Görülebilir |
| Ford Fiesta / Focus (2012-2023) | 1.0 EcoBoost | Yağ banyolu triger kayışının aşınması | 2012–2017 Yaygın · 2018–2020 Görülebilir · 2021–2023 Seyrek |
| Ford Focus 3 (2011-2018) | 1.6 Ti-VCT (Powershift DPS6) | Powershift kavrama silkelemesi ve kavrama yuvası sızıntısı | 2012–2016 Yaygın |
| Honda Civic (FC5, 2016-2021) | 1.5 VTEC Turbo (L15B7) | Yağa yakıt karışması | 2016–2018 Yaygın · 2019–2021 Seyrek |
| Honda Civic (FD6, 2006-2011) | 1.6 i-VTEC | Arka lastiklerde düzensiz aşınma (2006-2007 üretimde Honda servis bülteni) | 2006–2007 Görülebilir |
| Hyundai Bayon (2021-) | 1.0 T-GDI 100/120 (7DCT) | Yakıt pompası arızası | 2021–2023 Yaygın · 2024– Seyrek |
| Hyundai Bayon (2021-) | 1.4 MPI 100 | Yakıt pompası arızası | 2021–2023 Yaygın · 2024– Seyrek |
| Hyundai Tucson (TL, 2015-2020) | 1.6 T-GDI (7DCT) | 7DCT kalkışta tereddüt ve silkeleme | 2016–2017 Görülebilir |
| Hyundai i20 (BC3, 2020-) | 1.0 T-GDI 100/120 (7DCT) | Yakıt pompası arızası | 2020–2022 Yaygın · 2023– Seyrek |
| Hyundai i20 (BC3, 2020-) | 1.4 MPI 100 | Yakıt pompası arızası | 2020–2022 Yaygın · 2023– Seyrek |
| Mercedes-Benz C Serisi (W204, 2007-2014) | C220 / C250 CDI 2.1 (OM651) | Delphi piezo enjektör arızası | 2008–2012 Yaygın · 2013–2014 Seyrek |
| Mercedes-Benz E Serisi (W212, 2009-2016) | E250 CDI 2.1 (OM651) | Piezo enjektör arızası | 2009–2011 Yaygın · 2012–2016 Seyrek |
| Opel Astra K (2015-2021) | 1.4 Turbo 125/150 (B14XFL/B14XFT, 2019 sonrası D14XFL/D14XFT) | LSPI kaynaklı piston ve segman kırılması | 2015–2018 Yaygın · 2019–2021 Görülebilir |
| Opel Crossland / Corsa F (2017-) | 1.2 PureTech 83/100/110/130 (EB2) | Yağ banyolu triger kayışının dağılması | 2017–2020 Yaygın · 2021– Görülebilir |
| Peugeot 208 / 2008 / 308 / 3008 / 5008 (2019-) | 1.5 BlueHDi 100/130 (DV5) | Eksantrik zinciri sesi ve kopması (7 mm zincir) | 2019–2020 Yaygın · 2021–2022 Görülebilir · 2023– Seyrek |
| Peugeot 308 / 3008 (2007-2014) | 1.6 THP (EP6) | Yüksek basınç yakıt pompası arızası | 2007–2012 Görülebilir · 2013–2014 Seyrek |
| Peugeot 308 / 3008 / 208 / 2008 (2014-2021) | 1.2 PureTech (EB2) | Yağ banyolu triger kayışının dağılması | 2014–2020 Yaygın · 2021 Görülebilir |
| Renault Clio 4 (2013-2019) | 0.9 TCe 90 (H4Bt) | Triger zinciri ve gergi sesi (ilk üretim) | 2013–2014 Görülebilir · 2015–2019 Seyrek |
| Renault Clio 4 / Captur (2013-2019) | 1.2 TCe (H5Ft) | Aşırı yağ tüketimi | 2013–2016 Yaygın |
| Skoda Octavia (A7, 2013-2020) | 1.4 TSI (EA211, DSG DQ200) | DSG mekatronik arızası | 2013–2020 Görülebilir |
| Toyota Corolla (E210, 2019-) | 1.5 Dynamic Force (M15A-FKS) | Krank ve biyel yatağı sarması | 2021–2022 Yaygın · 2023–2025 Görülebilir |
| Volkswagen Golf 6 / Jetta (2008-2013) | 1.4 TSI (EA111, DSG DQ200) | DSG mekatronik arızası | 2008–2011 Yaygın · 2012–2013 Görülebilir |
| Volkswagen Golf 7 (2012-2019) | 1.4 TSI 122/140 (EA211) | DQ200 kuru kavrama aşınması ve mekatronik arızası | 2013–2019 Görülebilir |
| Volkswagen Polo 6R / 6C (2009-2017) | 1.2 TSI 90/105/110 (EA111 CBZA/CBZB, sonra EA211 CJZ) | Triger zinciri gergisi arızası ve zincir uzaması | 2009–2013 Yaygın · 2014–2017 Seyrek |
| Volkswagen Polo 6R / 6C (2009-2017) | 1.2 TSI 90/105/110 (EA111 CBZA/CBZB, sonra EA211 CJZ) | Aşırı yağ tüketimi ve supap yayı kırılması | 2009–2013 Görülebilir · 2014–2017 Seyrek |
| Volkswagen Tiguan (5N, 2008-2016) | 1.4 TSI 122/150/160 (EA111) | Triger zinciri gergisi arızası | 2008–2011 Yaygın · 2012–2016 Görülebilir |

### Kanıtı yetersiz bulunan gruplar

Aşağıdaki gruplar araştırıldı, iki bağımsız sitede tekrar eden bir sorun bulunamadı ve veritabanına eklenmedi. Bu "sorunsuz" demek değildir; kaynak bulunursa `data/araclar.json` içine eklenebilir.

| Model | Motor | Neden |
| --- | --- | --- |
| BMW 3 Serisi F30 (2015-2019) | 320d (B47) / 320i (B48) | Kaynaklar B47'nin N47 sorunlarını büyük ölçüde çözdüğünü yazıyor ama çelişkili; B48 zincir/turbo yağ terlemesi tek kaynakta kaldı. |
| Dacia Duster (2018-2021) | 1.6 SCe 115 | Kaynaklarda bu motor için öne çıkan bir sorun bulunamadı. |
| Fiat Egea (2016-) | 1.6 E-Torq 110 | Aramalarda öne çıkan kronik sorun bulunamadı. |
| Fiat Linea (2007-2015) | 1.4 Fire / 1.4 T-Jet | Dağınık şikâyetler var, tekrar eden bir sorun için iki bağımsız site bulunamadı. |
| Ford Courier / Tourneo Courier (2014-) | 1.5 TDCi / 1.0 EcoBoost | Şikâyetler fren sesi, gıcırtı ve genel motor arıza lambası gibi dağınık konularda; ortak bir arıza için iki bağımsız site bulunamadı. |
| Ford Fiesta (2008-2023) | 1.25 / 1.4 Duratec | Kullanıcılar 1.25 ve 1.4 benzinlileri sorunsuz olarak anıyor; kronik sorun bulunamadı. |
| Ford Fiesta (2008-2017) | 1.4 / 1.6 TDCi | Enjektör ve turbo anıları genel TDCi başlıklarıyla karışık; Fiesta'ya özgü tekrar eden sorun bulunamadı. |
| Ford Focus 3 (2011-2018) | 1.5 TDCi 95/120 | Enjektör ve DPF şikâyetleri dağınık, DPF şikâyetleri ağırlıkla 2019 sonrası EcoBlue'ya ait; 2015-2018 1.5 TDCi için ortak sorun yok. |
| Ford Puma (2019-) | 1.0 EcoBoost mHEV | Forum görüşleri çelişkili (bazıları en sorunsuz 3 silindirli diyor); tekrar eden bir motor sorunu için kanıt yok. |
| Hyundai Accent Blue (2011-2019) | 1.4 MPI / 1.6 GDI | 1.4 MPI ve 1.6 GDI için tekrar eden sorun bulunamadı (yalnızca tek tek külbütör kapağı yağ kaçağı ve sübap iddiaları). |
| Hyundai Elantra (2011-2020) | 1.6 MPI / 1.6 CRDi | Tek bir 7DCT kalkış titremesi şikâyeti dışında tekrar eden sorun bulunamadı. |
| Hyundai i30 (2012-2020) | 1.6 CRDi | Turbo, DPF ve DCT anıları nesilleri karıştırıyor ve dağınık; model/motor bazında tekrar eden sorun için iki bağımsız site bulunamadı. |
| Kia Rio (2011-2017) | 1.4 MPI 100 | Forumlarda sorunsuz olarak anılıyor; kronik sorun bulunamadı. |
| Mercedes-Benz C Serisi W205 (2014-2021) | C180 / C200 benzinli (M274) | Kaynaklar M274'ü zincir konusunda M271'e göre daha sorunsuz buluyor; belirgin kronik sorun yok (7G-Tronic için dağınık şikâyetler var). |
| Opel Corsa D / E (2006-2019) | 1.2 / 1.4 benzinli (A12XER, A14XER) | Aramalarda A12XER/A14XER için kronik sorun bulunamadı; sonuçlar PureTech'e ait. |
| Opel Mokka (2012-2019) | 1.4 Turbo (A14NET) | Mokka'ya özgü, A14NET'i açıkça belirten tekrar eden bir şikâyet bulunamadı; aynı motor için Astra J ve Astra K kayıtlarına bakın. |
| Peugeot 208 / 2008 / 308 / 3008 (2012-2021) | 1.6 BlueHDi / e-HDi (DV6) | Enjektör, EGR ve turbo anıları dağınık ve tek tek vaka; 301 kaydındaki DV6 sorunları aynı motor ailesi için geçerlidir. |
| Renault Megane 3 / Fluence (2009-2016) | 1.6 16V (K4M, LPG'li dahil) | Aramalarda LPG'li K4M supap oturması anılıyor ama iki bağımsız site bulunamadı. |
| Toyota C-HR (2016-) | 1.2 Turbo (8NR-FTS) | Yağ yakma ve şanzıman anıları motor tipi belirtilmeden, tek tek vaka; iki bağımsız site bulunamadı. |
| Toyota C-HR (2016-) | 1.8 Hybrid (2ZR-FXE) | Hibrit sistem uyarısı dışında tekrar eden mekanik sorun bulunamadı. |
| Toyota Corolla E170 (2013-2018) | 1.6 Valvematic (Multidrive S) | Şikâyet sitelerinde 1.6 Valvematic ve Multidrive S için tekrar eden bir sorun kümesi bulunamadı. |
| Toyota Corolla E210 (2019-) | 1.8 Hybrid (2ZR-FXE) | Şikâyetler ses yalıtımı, fren diski paslanması ve 12V akü gibi mekanik olmayan konularda; tekrar eden mekanik sorun bulunamadı. |

### Yalnızca iki siteyle desteklenen yeni maddeler

Kuralı geçiyor ama sınırda. Önce bunlara üçüncü bir kaynak aranması yararlı olur:

- Audi A3 (8V, 2012-2020): EGR valfi ve DPF tıkanması (araclo.com, donanimhaber.com)
- Audi A4 (B8, 2008-2015): Multitronic şanzıman titremesi ve arızası (araclo.com, donanimhaber.com)
- BMW 1 Serisi (F20 LCI, 2015-2019): Turbo manifoldu çatlaması ve soğutma suyu eksilmesi (andcetin.com, sikayetvar.com)
- Dacia Duster (2018-2021): Enjektör ve yüksek basınç borusu arızası (araclo.com, sikayetvar.com)
- Dacia Sandero / Logan (2013-2020): Enjektör ve yakıt sistemi arızası (araclo.com, donanimhaber.com)
- Fiat Doblo (2010-2022): Enjektör arızası (donanimhaber.com, sikayetvar.com)
- Fiat Doblo (2010-2022): Turbo arızası (donanimhaber.com, sikayetvar.com)
- Fiat Doblo (2010-2022): EGR ve DPF tıkanması (kısa mesafe kullanımında) (donanimhaber.com, eksisozluk.com)
- Ford Fiesta (Mk7, 2011-2017): Powershift kavrama ve şanzıman kontrol modülü (TCM) arızası (donanimhaber.com, sikayetvar.com)
- Ford Kuga 2 / Mondeo (2015-2019): Silindir kapağı çatlağı ve conta yanması (donanimhaber.com, sikayetvar.com)
- Hyundai Bayon (2021-): Yakıt pompası arızası (andcetin.com, sikayetvar.com)
- Hyundai Tucson (NX4, 2021-): DPF tıkanması ve yağa mazot karışması (andcetin.com, sikayetvar.com)
- Hyundai Tucson (NX4, 2021-): 7DCT kavrama titremesi (araclo.com, sikayetvar.com)
- Hyundai Tucson (TL FL, 2018-2020): 7DCT kavrama titremesi (araclo.com, sikayetvar.com)
- Hyundai i20 (BC3, 2020-): Yakıt pompası arızası (andcetin.com, sikayetvar.com)
- Mercedes-Benz C Serisi (W205, 2015-2021): NOx sensörü ve AdBlue sistemi arızası (donanimhaber.com, sikayetvar.com)
- Nissan Juke (F15, 2010-2019): CVT şanzıman sarsıntısı ve çekiş kaybı (donanimhaber.com, sikayetvar.com)
- Nissan Qashqai (J11, 2014-2020): Turbo basınç hortumu patlaması ve turbo arızası (araclo.com, sikayetvar.com)
- Opel Corsa D / E (2006-2019): Triger zinciri uzaması (araclo.com, donanimhaber.com)
- Opel Insignia A (2014-2017): Turbo basınç hortumu patlaması (eksisozluk.com, sikayetvar.com)
- Opel Insignia A (2014-2017): Triger zinciri sesi (eksisozluk.com, sikayetvar.com)
- Renault Clio 4 (2013-2019): Triger zinciri ve gergi sesi (ilk üretim) (araclo.com, donanimhaber.com)
- Renault Clio 5 (2019-): Motor takozu yıpranması (araclo.com, sikayetvar.com)
- Renault Kadjar (2015-2022): Külbütör kapağı çevresinden yağ terlemesi (araclo.com, sikayetvar.com)
- Renault Kadjar (2015-2022): EDC şanzıman vites geçiş sesi ve kavrama silkelemesi (eksisozluk.com, sikayetvar.com)
- Toyota Corolla (E150 FL / E170, 2009-2018): Aşırı yağ tüketimi (donanimhaber.com, sikayetvar.com)
- Volkswagen Passat (B7, 2010-2014): Enjektör şakırtısı ve arızası (araclo.com, donanimhaber.com)
- Volkswagen Passat (B8, 2015-2023): DSG kavrama ve mekatronik arızası (donanimhaber.com, sikayetvar.com)
- Volkswagen Polo 6R / 6C (2009-2017): Triger zinciri gergisi arızası ve zincir uzaması (andcetin.com, donanimhaber.com)
- Volkswagen Polo 6R / 6C (2009-2017): Aşırı yağ tüketimi ve supap yayı kırılması (andcetin.com, donanimhaber.com)
- Volkswagen T-Roc (2018-): Yağ eksiltme ve düşük yağ uyarısı (donanimhaber.com, sikayetvar.com)
- Volkswagen Tiguan (AD1 / CR7, 2018-): Yağ eksiltme ve düşük yağ uyarısı (donanimhaber.com, sikayetvar.com)

### Dikkat edilecek sınırlar

- Şikâyet siteleri sorunlu vakaları öne çıkarır; bir sorunun şikâyet sayfasında görülmesi sıklığı göstermez. Yıl kırılımındaki `Yaygın`/`Görülebilir`/`Seyrek` değerleri bildirim yoğunluğuna dayanan editoryal bir sınıflandırmadır.
- Aynı motoru paylaşan modellerde kaynak aktarımı yapıldı ve kayıtta belirtildi: Bayon kayıtları büyük ölçüde i20 şikâyetlerine, Juke 1.2 DIG-T kaydı kısmen Qashqai şikâyetlerine dayanıyor; PureTech kayıtları (Peugeot, Citroen, Opel) aynı motor ailesinin kaynaklarını kullanıyor.
- Yıl kırılımlarından biri tek kaynağa dayanıyor ve kayıtta "tek kaynak" yazıyor (Hyundai i20/Bayon yakıt pompası makyaj tarihleri, PureTech 2021 kayış malzemesi, Tiguan 5N erken CAV motor notu).
- Honda 1.5 Turbo kampanyası ABD ve Kanada için duyuruldu; Türkiye araçları için kapsamı doğrulanamadı. BMW N20 için 2015 güncellemesi forum ve parça rehberi yorumlarına dayanıyor, BMW belgesi bulunamadı.
- Kilometre aralıkları yine tahmindir; kaynakta rakam varsa ona göre, yoksa benzer vakalara göre yazıldı.
- Dış sitelere doğrudan erişim bu aşamada da kapalıydı; bkz. [KAYNAKLAR.md](KAYNAKLAR.md).

### Düzeltmeler

Bu aşamada kendi eklediğim kayıtlarda yaptığım denetimde şunlar düzeltildi:

- **Tiguan (5N) 1.4 TSI zincir gergisi:** parça açıklamasına kaynaklarda bulunmayan bir "yağ emiş süzgeci tıkanıklığı" notu yazılmıştı, çıkarıldı. Aynı kayda kaynaklardaki erken CAV motor notu yıl kırılımı olarak işlendi.
- **Opel Corsa D/E 1.3 CDTI zincir:** kaynaklar arasına Fiat Linea'ya ait bir forum başlığı girmişti, çıkarıldı.
- **Renault Clio 3 / Symbol 1.5 dCi enjektör:** genel bir "enjeksiyon arızası" şikâyet sayfası dCi'ye özgü olmadığı için çıkarıldı.
- **VW Passat B8 DSG:** B8'in şanzımanının DQ200 olduğu kesin olmadığından DQ200 makalesi yerine B8'e özgü şikâyet ve forum başlıkları kullanıldı.
- **Skoda Octavia 1.6 TDI DSG:** forum başlığı A5 dönemine ait olduğundan kayıt "A5 / A7" olarak adlandırıldı.
- **Bayon:** kaynakların i20'ye ait olduğu kayıt metnine eklendi.
- **Kademe 1 commit mesajı:** "63'ü kayıtlı" yazıyordu, doğrusu 74 (yukarıdaki sayı doğrudur; geçmiş değiştirilmedi).

## 3. aşama: sorun ayrıntıları

Tarih: 2026-10-24

Üçüncü aşamada her soruna, "neden oluyor, nasıl anlaşılır, ne yapılıyor, ne kadar tutuyor, nasıl önlenir" sorularını kaynakların anlattığı kadarıyla yanıtlayan isteğe bağlı bir `detay` bölümü eklendi. Çıkış noktası, BMW N13 için Google'da veritabanında yazandan çok daha fazla bilgi bulunduğu gözlemiydi. Gözlem doğruydu: önce N13 üzerinde bir pilot yapıldı, sonra aynı yöntem motor aileleri sırasıyla bütün kayıtlara uygulandı.

| | 2. aşama sonu | 3. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 97 | 97 |
| Kronik sorun | 156 | 160 |
| Ayrıntısı olan sorun | 0 | 160 |
| Sorunlara bağlı kaynak bağlantısı | 578 | 958 |
| Farklı kaynak sitesi | 60 | 68 |
| Yalnızca iki siteyle desteklenen sorun | 43 | 22 |

### Ne yapıldı

- **Yeni alan:** `detay` (`neden`, `teshis`, `cozum`, `maliyet`, `onlem`). Hepsi isteğe bağlı, her biri en fazla 800 karakter. Şema, doğrulayıcı (yeni birim testleriyle), görüntüleyici ve README güncellendi. Kaynakta karşılığı olmayan alan boş bırakıldı: neden 159, teşhis 143, çözüm 156, maliyet 108, önlem 123 sorunda dolu.
- **N13 pilotu:** 1 Serisi (F20) N13 kaydındaki sorunların ayrıntıları yazıldı ve veritabanında hiç olmayan dört sorun eklendi: turbo soğutma hattı O-ring'i ve motor arkası boru/flanş kaçağı; termostat ve soğutma suyu flanşı arızası; yağ kaçağı (valf kapağı, PCV diyaframı, yağ filtresi yuvası); tahrik arızası uyarısı ve güç kısıtlaması.
- **Aile aile ilerleme** (ayrıntısı olan sorun sayısı, birikimli): N13 pilotu 7; VAG DQ200 DSG ile Renault/Dacia/Nissan 45; Fiat, Ford, Opel ve PureTech 76; VAG TSI/TDI/EA888/Multitronic 95; Hyundai, Kia, Toyota ve Honda 116; BMW, Mercedes ve PSA 153; kalanlar 160.
- **Ek kaynaklar:** ayrıntıları dayandırmak için 380 bağlantı eklendi (21'i yeni dört soruna ait). Bu sayede 21 madde üçüncü bir siteye kavuştu. Kayıt defterine sekiz yeni site girdi: Autopartia, Carsece, Drivisual (editoryal/parça, düşük güven), Volkswagen Yeni Zelanda (resmî), Malay Mail (haber), GoParts, Foreign Automotive (parça/atölye, düşük güven), ElectricVehicleForums (forum, düşük güven). Düşük güvenli siteler yalnızca bir ayrıntının nereden geldiğini gösterir; kaynak kuralındaki deneyim ya da resmî belge koşulunun yerine geçmez.
- **Alan adı düzeltmesi:** `volkswagen.co.nz` adresi doğrulayıcıda ve görüntüleyicide `co.nz` olarak sayılıyordu; ikinci düzey uzantı listesine `co.nz` eklendi (test dahil).

### Ayrıntılar nasıl yazıldı

- Ayrıntılar arama özetlerinde görülen iddialardan yazıldı; kaynağı belirsiz ya da yalnızca hafızadan gelen bilgi bilerek yazılmadı. Kaynağın adı metinde geçer ("Carsece rehberi ... yazıyor", "Şikâyetvar'da bir kullanıcı ..."). Kısa bağlam notları (ör. Egea'nın Avrupa'daki adının Tipo olması) kaynaktan değil genel bilgiden gelir.
- Sayfalar yine açılamadı; bir iddianın hangi sayfadan geldiği başlık ve özet eşlemesine dayanıyor (bkz. Yöntem ve sınırlar).
- **Maliyet** yalnızca kaynakta rakam varsa yazıldı; ülke ve tarih belirtildi, yabancı para birimleri TL'ye çevrilmedi, başka motora ait rakamlar alınmadı. Rakam bulunamayan 52 sorunda alan boş.
- Kaynaklar ayrıştığında değerler tek rakama indirilmedi: N20 pompa arıza sıklığı, Civic FC5 kondenser kapsamı ve bülten numarası, Civic FD6 bülten tarihi, kabul edilebilir yağ eksiltme sınırları gibi.
- Satıcı ve blog kaynaklarının ticari çıkarı metinde belirtildi (BimmerWorld, FCP Euro, Foreign Automotive, CarChecker.pro, Carsece, Autopartia).
- DPF, EGR ve AdBlue iptali forumlarda geçtiği yerde "riskli ya da yasa dışı olabilir, ikinci elde bu tür araçlardan uzak durulmalı" notuyla yazıldı; öneri olarak sunulmadı.
- ABD servis bültenleri, geri çağırmalar ve fiyatlar için "Türkiye kapsamı/fiyatı doğrulanmadı" notu düşüldü.

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **N13 pilotu:** Şikâyetvar'daki "100 bin TL" tamir örneği, motoru N13 değil N20 olabilen bir 3.20i'ye ait olabileceğinden alınmadı. 2017 model 118i (B38) turbo wastegate şikâyetleri N13 kanıtı sayılmadı. And Mehmet Çetin'in N13 sayfası, sınırlı bir aramada genleşme kabı ve zincir iddialarını doğrulamadı; bu iddialar Carsece, Drivisual, Araclo ve OTOPARK.COM'a dayanıyor.
- **Tahrik arızası uyarısı (N13):** kaynaklarda bulunmayan lambda, akü ve manifold maddeleri çıkarıldı.
- **2.0 TDI Multitronic:** çıkarıma dayanan bir neden cümlesi kaynağın söylediğine göre yeniden yazıldı.
- **1.2 TSI:** Polo'ya özgü yağ kapasitesi bilgisi genel 1.2 TSI metninden çıkarıldı.
- **Araclo:** "parça maliyeti düşük" iddiası doğrulanamadığı için çıkarıldı.
- **Passat B6 2.0 TDI (BKP) yağ pompası:** ilk yazılan metin altıgen mil arızasının daha çok sonraki CBEA/CKRA motorlarında belgelendiğini söylüyordu. Son turda bulunan bir bilgiye göre WheelStreet rehberi BKP/BMP sürümünü altıgen tahrik riskiyle anıyor, bir VAG forum başlığı ise aynı motor ailesinde zincirle tahrik edilen denge mili/yağ pompası düzeneğinin bozulmasını ve bunu dişli tahrike çeviren bir seti anlatıyor. Metin buna göre düzeltildi ve `etkilenen_parca` "altıgen tahrik mili" yerine tahrik düzeneğinin iki biçimini yazacak şekilde değiştirildi. Hangi parçanın ne sıklıkla bozulduğu hâlâ net değil.
- **Passat B6 yağ basıncı uyarısı:** DonanımHaber başlığında geçen 22.000 TL'lik yetkili servis faturası, hangi sayfadan ve hangi Passat neslinden geldiği ayırt edilemediği için alınmadı.

### Kanıtı sınırlı ayrıntılar

Bu sorunların ayrıntısı yazıldı ama dayanağı zayıf ya da dolaylı; metinlerinde de bu belirtilmiştir:

- **Cruze 1.6 ateşleme bobini:** tek zayıf kaynak (CarChecker.pro); Cruze bobin rehberlerinin çoğu 1.4/1.8 içindir.
- **Egea 1.6 çift kütleli volan:** Egea'ya özgü doğrudan kanıt sınırlı; Tipo forumu ve genel bir rehbere dayanıyor. Şikâyetvar'daki volan şikâyetlerinin bir kısmı DCT'li araçlara ait ve şanzıman tipi hep belirtilmiyor.
- **Polo 1.2 (3 silindir) zincir:** dolaylı kanıt. Aynı sayfalardaki 1.2 TSI zincir kayıtları bu motor için geçerli değil; Honest John'da silindir kapağı arızası da kayıtlı.
- **Passat B6 BKP yağ pompası:** BKP'ye özgü bülten yok. Güney Kore'deki 2.425 araçlık geri çağırma (2005-2008 üretim) BKP'ye ya da belirli bir arıza moduna bağlanamadı.
- **Passat B6 DQ250:** tek resmî dayanak 2013'te 2008-09 modelleri kapsayan geri çağırma; mekatronik anlatımı bir parça üreticisi (VAICO) kaynaklı makaleye dayanıyor. Kavrama aşınması şikâyetleri çoğunlukla kuru kavramalı DQ200'e ait; DQ250 ıslak kavramalıdır.
- **Kadjar 1.3 TCe külbütör kapağı:** Kadjar'a özgü kayıt bulunamadı; metin aynı motor ailesinin Megane 4 ve Clio kayıtlarına dayanıyor.
- **Qashqai ve Clio 4/Captur 1.2 zincir:** zincir sesinin yağ tüketimiyle ilişkisi net değil; Nissan bülteni (TB EM 15/05) ikinci elden aktarılıyor, Renault kusuru reddediyor.
- **Honda Civic FC5 klima kondenseri ve FD6 arka lastik:** ABD bültenleri ve kampanyaları; Türkiye'deki araçlar için kapsam doğrulanmadı, bülten tarihleri kaynaklarda farklı.
- **BMW N20 pompa/konnektör:** ABD geri çağırma kampanyası (24V-608) bir forum yazısında alıntılanan metne dayanıyor; Türkiye kapsamı doğrulanmadı.
- **Mercedes M271 eksantrik mıknatısı:** M271'e özgü resmî bülten bulunamadı; anılan Nisan 2011 bülteni M112 V6 içindir.

### Yalnızca iki siteyle desteklenen maddeler (3. aşama sonu)

Kuralı geçiyorlar ama sınırda. 2. aşama sonunda doğrulayıcı 43 madde sayıyordu (o raporun 7 + 32 maddelik listeleri bu sayının tamamını göstermiyordu); ayrıntılar için eklenen kaynaklarla 22'ye indi. Üçüncü kaynak aramasında önce bunlara bakılması yararlı olur:

- BMW 3 Serisi (F30, 2012-2015): Yağ filtresi yuvası contası kaçağı (Bimmerpost, FCP Euro)
- Fiat Doblo (2010-2022): Enjektör arızası (DonanımHaber Forum, Şikâyetvar)
- Fiat Doblo (2010-2022): Turbo arızası (DonanımHaber Forum, Şikâyetvar)
- Fiat Doblo (2010-2022): EGR ve DPF tıkanması (kısa mesafe kullanımında) (DonanımHaber Forum, Ekşi Sözlük)
- Ford Focus (2008-2018): Turbo yağ besleme süzgecinin tıkanması (Ford Owners Club, Honest John)
- Ford Focus (2008-2018): DPF tıkanması (Ford Owners Club, Honest John)
- Ford Kuga 2 / Mondeo (2015-2019): Silindir kapağı çatlağı ve conta yanması (DonanımHaber Forum, Şikâyetvar)
- Hyundai Bayon (2021-): Yakıt pompası arızası (And Mehmet Çetin, Şikâyetvar)
- Hyundai Bayon (2021-): Yakıt pompası arızası (And Mehmet Çetin, Şikâyetvar)
- Hyundai Tucson (NX4, 2021-): 7DCT kavrama titremesi (Araclo, Şikâyetvar)
- Hyundai Tucson (TL FL, 2018-2020): 7DCT kavrama titremesi (Araclo, Şikâyetvar)
- Hyundai i20 (BC3, 2020-): Yakıt pompası arızası (And Mehmet Çetin, Şikâyetvar)
- Hyundai i20 (BC3, 2020-): Yakıt pompası arızası (And Mehmet Çetin, Şikâyetvar)
- Mercedes-Benz C Serisi (W205, 2015-2021): NOx sensörü ve AdBlue sistemi arızası (DonanımHaber Forum, Şikâyetvar)
- Opel Corsa D / E (2006-2019): Triger zinciri uzaması (Araclo, DonanımHaber Forum)
- Renault Clio 4 (2013-2019): Triger zinciri ve gergi sesi (ilk üretim) (Araclo, DonanımHaber Forum)
- Renault Clio 5 (2019-): Motor takozu yıpranması (Araclo, Şikâyetvar)
- Renault Kadjar (2015-2022): Külbütör kapağı çevresinden yağ terlemesi (Araclo, Şikâyetvar)
- Toyota Corolla (E150 FL / E170, 2009-2018): Aşırı yağ tüketimi (DonanımHaber Forum, Şikâyetvar)
- Volkswagen Passat (B6, 2005-2010): DSG (DQ250) mekatronik ve kavrama sorunları (AustralianCar.Reviews, Şikâyetvar)
- Volkswagen Passat (B7, 2010-2014): Enjektör şakırtısı ve arızası (Araclo, DonanımHaber Forum)
- Volkswagen Polo (9N / 6R, 2002-2014): Triger zinciri uzaması (Honest John, PicoAuto Forum)

### Dikkat edilecek sınırlar

- Ayrıntılar kaynak anlatımlarının özetidir; üreticinin ya da yetkili servisin talimatı, hukuki ya da mali tavsiye değildir. `neden` alanı kesin teknik tespit olmayabilir.
- Maliyetler tarihlidir ve çoğu başka ülke ve para biriminden gelir; büyüklük sırası olarak okuyun.
- Aynı olay birden fazla sayfada tekrarlandığı için çok sayıda kaynak bağlantısı bağımsız doğrulama anlamına gelmez.
- Doğrulama yine arama özetleriyle yapıldı; rakamlar, alıntılar ve model yılı için asıl sayfaya bakmak gerekir.

## Sonraki adımlar

1. Ağ erişimi verilirse `KAYNAKLAR.md` içindeki sayfalar doğrudan okunarak her bağlantının iddiayı gerçekten içerdiği, ayrıntılardaki rakam ve alıntıların doğru olduğu kontrol edilebilir.
2. Yalnızca iki siteyle desteklenen 22 maddeye (yukarıdaki liste) üçüncü bir kaynak eklenebilir.
3. Kademe 2 ve 3: [KAPSAM.md](KAPSAM.md) içinde `○` ile işaretli 66 model/motor grubu aynı kuralla ve aynı ayrıntı düzeniyle eklenebilir.
4. Kanıtı yetersiz bulunan 22 grup için yeni kaynak çıkarsa eklenebilir.
5. "Kanıtı sınırlı ayrıntılar" listesindeki maddeler Türkçe servis ya da forum kaynağıyla güçlendirilebilir; maliyet alanı boş kalan 52 soruna güncel Türkiye fiyatı bulunursa eklenebilir.
