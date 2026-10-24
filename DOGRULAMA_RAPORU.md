# Doğrulama raporu

Tarih: 2026-10-24

Rapor altı aşamayı kapsar. Aşağıdaki ilk bölümler 1. aşamayı (ilk sürümün doğrulanması) anlatır; [2. aşama](#2-aşama-en-çok-satan-modellerin-motor-grupları-ve-yıl-kırılımı) en çok satan modellerin eklenmesini ve yıl kırılımını, [3. aşama](#3-aşama-sorun-ayrıntıları) her soruna eklenen ayrıntıları, [4. aşama](#4-aşama-ölçeğin-genişletilmesi-ve-motor-versiyonları) ölçeğin genişletilmesini ve motor versiyonlarını, [5. aşama](#5-aşama-elektrikli-araçlar) elektrikli araçların kapsama alınmasını, [6. aşama](#6-aşama-astra-electric-açığı-ve-diğer-elektrikliler) Astra Electric açığının ve diğer eksik elektrikli modellerin ele alınmasını anlatır.

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

## 4. aşama: ölçeğin genişletilmesi ve motor versiyonları

Tarih: 2026-10-24

Dördüncü aşamada istek şuydu: aynı mantıkla ölçeği genişletmek, daha fazla marka, model ve motor seçeneği eklemek ve aynı motor seçeneğinin farklı versiyonlarını da kayda geçirmek. Kurallar değişmedi: her sorun için en az iki farklı site ve bunlardan en az biri deneyim ya da resmî türünde; ayrıntı yalnızca kaynağı metinde anılan iddialardan; kaynak bulunamayan grup plana `–` olarak işlenir, sorun uydurulmaz. Plan `data/kapsam.json` içinde, ilerleme [KAPSAM.md](KAPSAM.md) dosyasında.

| | 3. aşama sonu | 4. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 97 | 136 |
| Kronik sorun | 160 | 205 |
| Ayrıntısı olan sorun | 160 | 205 |
| Yıl kırılımı olan sorun | 32 | 48 |
| Marka | 19 | 22 |
| Sorunlara bağlı kaynak bağlantısı | 958 | 1161 |
| Farklı kaynak sitesi | 68 | 68 |
| Yalnızca iki siteyle desteklenen sorun | 22 | 44 |
| Plan satırı | 178 | 245 |
| Plan durumu (✓ / – / ○) | 90 / 22 / 66 | 132 / 113 / 0 |

### Ne yapıldı

- **Plan:** 178 satırdan 245'e çıktı (+67). Kademe 2 ve 3'te bekleyen 66 satır ile eklenen 67 satır (toplam 133) işlendi: 42'si veritabanına girdi, 91'i kanıt yetersiz olduğu için eklenmedi. Sırada (○) satır kalmadı. Kademe 2'nin 85 satırından 41'i, kademe 3'ün 75 satırından 17'si ✓.
- **Yeni kayıt:** 39 yeni araç/motor kaydı ve bunlara bağlı 45 yeni sorun. Mevcut kayıtlara yeni sorun eklenmedi; mevcut sorunlarda yalnızca altı dönem kırılımı ve bir metin düzeltmesi yapıldı (aşağıda).
- **Yeni markalar:** Volvo, Subaru ve Mini veritabanına girdi (19 → 22 marka). Plana ayrıca 11 marka girdi ve hiçbirinde ölçütü geçen kaynak bulunamadı: Jeep, Alfa Romeo, Mazda, Suzuki, Mitsubishi, Land Rover, Cupra, MG, Lexus, Isuzu ve Chevrolet'nin Captiva / Aveo / Lacetti modelleri (Chevrolet Cruze kaydı ilk aşamadandır). Bu 14 marka 2. aşamada seçilen ilk-15 marka kümesinin dışındadır; seçimleri editoryaldir, satış adetleri doğrulanamadı ve `data/kapsam.json` içinde `ek` kapsamıyla işaretlidir.
- **Dönem kırılımı:** 32 → 48. Yeni sorunlardan 10'unda kaynaklar yıl farkı verdiği için kırılım var. Altı mevcut soruna ise ayrıntı metninde yıl bilgisi zaten bulunduğu için yapılandırılmış dönem eklendi: A3 ve Octavia DQ200 mekatronik / kavrama, Juke ve Qashqai J11 1.2 DIG-T yağ tüketimi ve zincir, Corolla E150 1.4 D-4D yağ tüketimi.
- **Kaynaklar:** 45 yeni soruna 203 bağlantı eklendi (178 tekil adres, sorun başına ortalama 4,5). Yeni site gerekmedi, kayıt defteri 68 sitede kaldı. Her yeni adresin arama sonuçlarında tam eşleşmeyle geçtiği yazım sırasında ve bitişte otomatik denetlendi: hafızadan yazılmış ya da bulunamayan adres yok. Yeni sorunların 22'si iki, 21'i üç, 2'si dört siteyle destekleniyor.
- **Ayrıntılar:** 45 yeni sorunun hepsinde `detay` var. Alan doluluğu: neden 44, teşhis 43, çözüm 43, maliyet 26, önlem 8. Boş alan, kaynakların o soruya yanıt vermediği anlamına gelir; özellikle `onlem` kaynaklarda anlatılmayıp yalnızca arama özetinin genel tavsiyesi olarak çıktığında yazılmadı.
- **Yöntem aynı:** sayfalar açılamadı; şikâyet ve forum sitelerine (Şikâyetvar, DonanımHaber, OTOPARK.COM, Ekşi Sözlük) sınırlanmış Türkçe aramalar sayfa düzeyinde adresler verdi, ikinci kaynak için ayrıca hedefli aramalar yapıldı. Maliyet yalnızca kaynakta rakam varsa, tarih ve ülke belirtilerek yazıldı.

### Motor versiyonları nasıl ele alındı

İstekteki "aynı motor seçeneğinin farklı versiyonları" şöyle yorumlandı: **kaynaklar iki versiyonu motor kodu, güç, şanzıman ya da kasa/nesil ile ayırt ediyorsa ayrı kayıt açıldı; ayırt etmiyorlarsa kayıt bölünmedi ve fark metinde ya da `donem_kirilimi` içinde anıldı.** Ayrı kayıt, sorun listesi, kilometre aralığı ya da riskin versiyona göre değiştiği yerde açıldı. Bir kaydın içinde yıla göre değişim `donem_kirilimi` ile gösterildi. Kural README'ye ve KAPSAM.md'ye de yazıldı.

- **Motor kodu ve nesil:** Mercedes M271 Kompressor (W203 / W204, 2002-2010: triger zinciri uzaması, eksantrik ayar mıknatısından yağ kaçağı) ile M271 EVO CGI turbo (W204, 2009-2014: eksantrik ayar elemanı, zincir ve dişli aşınması) ayrı kayıtlar. Kompressor kaydındaki mıknatıs yağ kaçağı EVO'ya taşınmadı, çünkü bulunan kanıt Kompressor'a özgüydü.
- **Aynı motor, farklı model:** BMW N47 zincir sorunu 320d (N47D20, E90 / F30), 116d (N47D16, F20) ve 520d (N47D20, F10) için ayrı kayıtlar; kaynaklar modele özgü ve kilometre aralıkları farklı (100-200, 100-160 ve 90-160 bin km). Toyota 1ND-TV: Corolla E150 ve Auris ayrı. PSA DV5 zinciri: Peugeot / Citroën kaydının yanında Opel Grandland X. VW 1.6 TDI (EA189 CAYC): Polo 6R / 6C ve Caddy 2K. Audi 2.0 TFSI: A4 B8 ve Q5 8R.
- **Şanzıman versiyonu:** Nissan Qashqai J11'de 1.5 dCi / 1.6 dCi (K9K / R9M) turbo hortumu, 1.6 dCi 130 Xtronic CVT ve 1.2 DIG-T Xtronic üç ayrı kayıt. Aynı mantıkla Micra K13 1.2 CVT, X-Trail T32 1.6 dCi CVT, Corsa D Easytronic, Peugeot 508 MCP / Auto6R, Renault Captur ve Talisman EDC, Volvo S60 / V40 Powershift ve Kia Stonic 1.4 MPI 6 ileri otomatik.
- **48V hafif hibrit versiyonlar:** Golf 8 (1.0 eTSI / 1.5 eTSI) ve Octavia A8 (1.0 TSI e-TEC / 1.5 TSI), Golf 7'nin 1.2 TSI kaydından ayrı.
- **Bölünmeyenler:** BMW N47'de 177 ve 184 bg sürümleri arasındaki fark (184 bg'de sorun daha az görülüyor) ve "2015'te iyileştirilmiş zincir seti" yalnızca forum yorumlarında geçiyor, resmî kaynakla doğrulanamadı; bu yüzden ayrı kayıt açılmadı, 520d kaydındaki dönem notuna yazıldı. Opel Grandland X'in DV5 kilometre aralığı için Opel'e özgü veri olmadığından aralık Peugeot / Citroën kaydındaki kaynaklardan alındı ve kayıtta belirtildi.

### Eklenen kayıtlar

- **Volkswagen (5):** Golf 7 1.2 TSI (EA211) yağ tüketimi; Golf 8 eTSI 48V (vites kolu modülü, 48V sistem); Polo 6R / 6C 1.6 TDI enjektör; Caddy 2K 1.6 TDI enjektör; Tiguan 2.0 TDI DQ381 DSG mekatronik.
- **Skoda (2):** Kamiq / Scala 1.0 TSI DSG; Octavia A8 1.0 TSI e-TEC / 1.5 TSI 48V (vites kolu, 48V sistem).
- **Seat (1):** Ibiza 6J / 6P 1.2 TSI DQ200 DSG. **Audi (1):** Q5 8R 2.0 TFSI yağ tüketimi.
- **BMW (2):** 1 Serisi F20 116d (N47D16) ve 5 Serisi F10 520d (N47D20) zincir. **Mercedes-Benz (2):** C Serisi W204 M271 EVO; A Serisi / CLA W176 / C117 Pre-Safe ve direksiyon açı sensörü.
- **Opel (4):** Astra J 1.6 atmosferik termostat gövdesi ve yağ soğutucu; Astra K 1.6 CDTI zincir; Corsa D Easytronic; Grandland X 1.5 BlueHDi (DV5) zincir.
- **Peugeot (2):** 301 1.2 EB2F yağ tüketimi ve katalitik konvertör; 508 1.6 e-HDi MCP / Auto6R. **Citroen (1):** C4 Cactus 1.2 PureTech yağ banyolu kayış.
- **Fiat (3):** 500 airbag kapağı; Fiorino / Qubo 1.3 Multijet (enjektör, yağ tüketimi, turbo); Punto Evo / Grande Punto (elektrikli direksiyon, airbag kapağı). **Ford (1):** EcoSport 1.0 EcoBoost yağ banyolu kayış.
- **Renault (2):** Captur 1.5 dCi EDC; Talisman EDC. **Dacia (1):** Jogger 1.0 TCe volan ve debriyaj. **Nissan (3):** Micra K13 1.2 CVT; Qashqai J11 1.6 dCi Xtronic; X-Trail T32 1.6 dCi Xtronic.
- **Toyota (1):** Auris 1.4 D-4D yağ tüketimi. **Honda (1):** CR-V 1.6 i-DTEC turbo hortumu. **Hyundai (2):** i20 PB ve i30 FD elektrikli direksiyon. **Kia (2):** Picanto JA akü / marş; Stonic 1.4 MPI otomatik şanzıman.
- **Yeni markalar (3):** Volvo S60 / V40 1.6 D Powershift; Subaru XV 2.0 yağ tüketimi; Mini Cooper S / Countryman S (R56 / R60) yüksek basınç yakıt pompası.

### Araştırılıp eklenmeyen gruplar

Plana 91 yeni `–` satırı işlendi (toplam 113). Her satırın nedeni [KAPSAM.md](KAPSAM.md) içinde yazılıdır; satır sayıları marka bazında: Hyundai, Kia, Opel, Renault ve Volkswagen altışar; Audi, Mercedes-Benz, Nissan, Skoda ve Toyota beşer; BMW, Ford ve Honda dörder; Citroen ve Peugeot üçer; Dacia, Fiat ve Seat ikişer; Alfa Romeo, Chevrolet, Cupra, Isuzu, Jeep, Land Rover, Lexus, MG, Mazda, Mini, Mitsubishi ve Suzuki birer. Başlıca nedenler:

- **Kanıt tek siteye dayanıyor, ikinci bağımsız kaynak yok** (çoğunlukla yalnızca Şikâyetvar, bazen tek bir rehber sitesi): Hyundai Kona 1.6 CRDi DCT, Opel Mokka 1.6 CDTI, Toyota Hilux, Honda City, Ford Transit Custom ve Ranger, Nissan Navara ve Juke 1.5 dCi, Fiat Ducato, Isuzu D-Max, MG HS, Volkswagen Caddy 2.0 TDI, Skoda Karoq / Kodiaq.
- **Kanıt başka bir model, motor ya da nesle ait ve zaten kayıtlı bir soruna bağlanıyor**, aynı sorun için ikinci bir kayıt açılmadı: Audi A4 B9 (yağ eksiltme şikâyetleri B8 dönemine ait), Audi Q3, BMW X1 / X3 (N47 kayıtlarında), Nissan Qashqai J10 (J11 kaydında), Opel Insignia 2.0 CDTI, VW Passat B7 (B6 kaydında), Dacia Lodgy / Dokker, Mercedes Vito / Sprinter.
- **Yalnızca tekil, dağınık şikâyet var ya da arama sonuç vermedi:** Skoda Fabia ve Superb, Kia Ceed MPI, Toyota Yaris, Honda Civic FB7, Hyundai i30 benzinliler, Lexus IS / CT, Nissan Note, Mini F56.
- **Kilometre ya da model yılı verisi yok, sürüm doğrulanamadı:** Kia Cerato arka stop / bagajdan su alma (Şikâyetvar'da çok ama kilometre ve yıl yok), MG HS (model yılı ve sürüm).

`–` "sorun yok" demek değildir; yalnızca ölçütü geçen kaynak bulunamadığı anlamına gelir.

### Kanıtı sınırlı ayrıntılar

Bu sorunların ayrıntısı yazıldı ama dayanağı zayıf, dolaylı ya da yabancı kaynaklı; metinlerinde de bu belirtilmiştir:

- **Dacia Jogger 1.0 TCe volan ve debriyaj:** yalnızca Ekşi Sözlük ve Şikâyetvar; birkaç kullanıcı anlatımı, kilometre aralığı (10.000-30.000 km) bu anlatımlardan. Resmî Dacia bülteni ya da kampanyası bulunamadı; neden, maliyet ve önlem alanları boş.
- **Opel Grandland X 1.5 BlueHDi (DV5) zincir:** Opel'e özgü kilometre verisi yok, aralık Peugeot / Citroën kaydından alındı. Geri çağırma iddiası tek kullanıcıya dayanıyor ve resmî kaynakla doğrulanamadı; 2023 sonrası daha kalın zincir de doğrulanmadı.
- **Nissan CVT kayıtları (Micra K13, Qashqai J11 1.6 dCi, X-Trail T32):** yalnızca DonanımHaber ve Şikâyetvar. Maliyet rakamları tarihsiz ya da kayıt tarihleri belirsiz; Qashqai'de 2017 sonrası iyileştirilmiş şanzıman beyni iddiası bir kullanıcıdan, doğrulanmadı.
- **Mercedes A Serisi / CLA Pre-Safe:** yalnızca DonanımHaber ve Şikâyetvar; örnekler tek tek sürücülerden. GLA'yı da anan başlıklar var ama GLA ayrı eklenmedi.
- **BMW N47 (116d F20, 520d F10):** 2015'te iyileştirilmiş zincir seti, 177 / 184 bg farkı ve BMW'nin 90.000-110.000 km değişim önerisi kullanıcı beyanı; resmî kaynakla doğrulanmadı. 116d'deki toplam maliyet aralığının (15.000-150.000 TL) tarihi ve kapsamı belirsiz.
- **Mini Cooper S / Countryman S yüksek basınç pompası:** yalnızca bir kilometre verisi (110.000 km) var; 70.000-130.000 km aralığı bu veriye ve kullanıcı anlatımlarına dayanan kaba bir tahmin. N14 ve N18 ayrımı ikinci elden aktarım. Fiyat tarihsiz.
- **Subaru XV 2.0 yağ tüketimi:** dönem sınırları (2012-2014 ve 2015-2017) kullanıcı yorumlarına dayanıyor, sıklık bilgisi yok; resmî servis bülteni ya da kampanya bulunamadı.
- **Volvo S60 / V40 Powershift:** kaynaklardan biri Araclo (düşük güven); fiyatlar yaklaşık 2014-2017 dönemine ait, enflasyon öncesi.
- **Ford EcoSport 1.0 EcoBoost:** ABD'deki geri çağırma sayıları ve Avrupa / ABD müşteri memnuniyeti programı kullanıcı aktarımı; Türkiye kapsamı ve resmî kaynak doğrulanmadı.
- **Toyota Auris ve Corolla 1.4 D-4D yağ tüketimi:** Toyota servis bülteninin içeriği (üç neden) bir forum yazarından aktarılıyor, bülten doğrulanmadı; "2009'daki motor değişikliği" kullanıcı anlatımı.
- **Audi Q5 2.0 TFSI yağ tüketimi:** servis bülteni (TSB 17 13 43) ve piston segmanı davası ABD dava özetlerinden; Türkiye'deki araçlar için kapsam doğrulanmadı. Dönem kırılımı bu ABD belgelerine dayanıyor.
- **Mercedes C Serisi M271 EVO:** kaynaklar ağırlıkla ABD'den (MBWorld, CarComplaints); Kasım 2020 uzatılmış garanti mektubu ve dolar fiyatları ABD'ye ait.
- **Maliyet rakamları:** Captur EDC, Corsa D Easytronic, Fiorino, Polo 6R, Hyundai i20 / i30 EPS ve benzerlerinde tarihleri farklı ya da belirsiz kullanıcı beyanları; güncel fiyat olarak okunmamalı. Ayrıntısı olan 45 yeni sorundan 19'unda maliyet alanı boş.
- **Kia Picanto akü:** servislerin teşhisi çelişkili (kimi aküyü normal buluyor, kimi akü sensörünü değiştiriyor); kök neden belirsiz.
- **Fiat 500 ve Punto Evo airbag kapağı:** sorunun Fiat'a genel olduğu bir DonanımHaber başlığına dayanıyor; ücretsiz değişim anlatıları ikinci elden.

### Yalnızca iki siteyle desteklenen yeni maddeler

Kuralı geçiyorlar ama sınırda. 3. aşama sonundaki 22 maddeye (yukarıdaki listede) bu aşamada 22 yeni madde eklendi; toplam 44. Yeni 22'nin 19'unda iki site DonanımHaber Forum ve Şikâyetvar, yani ikisi de kullanıcı deneyimi aktaran siteler; ikisinde (Jogger ve Peugeot 301 yağ tüketimi) Ekşi Sözlük (kayıt defterinde düşük güven) ve Şikâyetvar; birinde (Volvo S60 / V40) Araclo (düşük güven) ve DonanımHaber Forum:

- Dacia Jogger (2022-): Volan ve debriyaj arızası (Ekşi Sözlük, Şikâyetvar)
- Fiat 500 (2008-): Yolcu airbag kapağı (torpido göğüs kısmı) şişmesi ve çatlaması (DonanımHaber Forum, Şikâyetvar)
- Fiat Fiorino / Qubo (2008-2020): Enjektör arızası ve enjektör pulu kaçağı (DonanımHaber Forum, Şikâyetvar)
- Fiat Punto Evo / Grande Punto (2009-2018): Elektrikli direksiyon (EPS) açı ve tork sensörü arızası (DonanımHaber Forum, Şikâyetvar)
- Fiat Punto Evo / Grande Punto (2009-2018): Yolcu airbag kapağı (torpido göğüs kısmı) şişmesi ve çatlaması (DonanımHaber Forum, Şikâyetvar)
- Hyundai i20 (PB, 2009-2014): Elektrikli direksiyon (EPS) sertleşmesi ve arızası (DonanımHaber Forum, Şikâyetvar)
- Hyundai i30 (FD, 2008-2012): Elektrikli direksiyon (EPS) sertleşmesi ve arızası (DonanımHaber Forum, Şikâyetvar)
- Kia Picanto (JA, 2017-): Akü boşalması ve soğuk havada marş sorunu (DonanımHaber Forum, Şikâyetvar)
- Mercedes-Benz A Serisi / CLA (W176 / C117, 2012-2019): Pre-Safe uyarısı, ESP ve direksiyon açı sensörü arızası (DonanımHaber Forum, Şikâyetvar)
- Nissan Micra (K13, 2010-2017): CVT şanzıman arızası (P173A / P173C) (DonanımHaber Forum, Şikâyetvar)
- Nissan Qashqai (J11, 2014-2020): Xtronic CVT şanzıman beyni arızası (P17F1) ve silkeleme (DonanımHaber Forum, Şikâyetvar)
- Nissan X-Trail (T32, 2014-2021): Xtronic CVT silkelemesi, P17F1 kodu ve şanzıman değişimi (DonanımHaber Forum, Şikâyetvar)
- Peugeot 301 (2012-): Aşırı yağ tüketimi (Ekşi Sözlük, Şikâyetvar)
- Peugeot 301 (2012-): Katalitik konvertör arızası ve motor arıza lambası (DonanımHaber Forum, Şikâyetvar)
- Skoda Kamiq / Scala (2019-): DSG kavrama ısınması, sarsıntı ve mekatronik arızası (DonanımHaber Forum, Şikâyetvar)
- Skoda Octavia (A8, 2020-): 48V hafif hibrit (e-TEC) sistem ve alternatör arızası (DonanımHaber Forum, Şikâyetvar)
- Subaru XV (2012-2017): Aşırı yağ tüketimi (DonanımHaber Forum, Şikâyetvar)
- Toyota Auris (E150 / E180, 2007-2018): Aşırı yağ tüketimi (DonanımHaber Forum, Şikâyetvar)
- Volkswagen Caddy (2K, 2010-2015): Enjektör arızası (DonanımHaber Forum, Şikâyetvar)
- Volkswagen Golf 8 (2020-): 48V hafif hibrit sistem ve alternatör-marş jeneratörü arızası (DonanımHaber Forum, Şikâyetvar)
- Volkswagen Polo 6R / 6C (2009-2017): Enjektör arızası (DonanımHaber Forum, Şikâyetvar)
- Volvo S60 / V40 (2011-2018): Powershift kuru kavrama titremesi ve kavrama değişimi (Araclo, DonanımHaber Forum)

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **MG HS 1.5 T DCT:** taslağa alınan kayıt, model yılı, güç (143-170 bg) ve DCT sürümü doğrulanamadığı için çıkarıldı, plana `–` olarak işlendi.
- **Kia Cerato:** su alma şikâyetleri çok ama kilometre ve yıl verisi olmadığı için eklenmedi.
- **Mercedes M271 EVO:** Kompressor kaydındaki mıknatıs yağ kaçağı EVO'ya taşınmadı (kanıt Kompressor'a özgü).
- **Dacia Jogger:** önlem alanı, kaynağı olmayan genel tavsiye olacağı için yazılmadı.
- **Nissan Qashqai J11 turbo hortumu:** Şikâyetvar'daki örneklerden birinin 2012 model araca (J10 dönemi) ait olduğu ayrıntı metnine eklendi; kayıt J11 (2014 sonrası) içindir ve J10 için ayrı kayıt açılamadı.
- **Hyundai Kona `–` notu:** 7DCT kavrama titremesinin ele alındığı kayıtlar yanlışlıkla i20 / i30 yazılmıştı; Tucson, Bayon, i20 (BC3) ve Sportage olarak düzeltildi.
- **Bayat plan satırları:** iki `–` satırı yeni kayıtlarla eşleştiği için birim testi (`test_elenen_satir_kayitla_eslesmez`) hata verdi: Opel Corsa D / E benzinli satırı motor kodlarına (A12XER, A14XER) daraltıldı, Toyota Auris satırı benzinli motorlara indirildi ve 1.4 D-4D ayrı satır oldu.

### Dikkat edilecek sınırlar

- Yeni kayıtların çoğu iki ya da üç siteyle, ağırlıkla DonanımHaber ve Şikâyetvar ile destekleniyor. Bu siteler sorunlu vakaları öne çıkarır; bir sorunun orada görünmesi sıklığı göstermez. Aynı olay birden fazla sayfada tekrarlandığı için çok sayıda bağlantı bağımsız doğrulama anlamına gelmez.
- Yeni dönem kırılımları kullanıcı beyanlarına ve yabancı bülten / dava özetlerine dayanıyor; `Yaygın` / `Görülebilir` / `Seyrek` editoryal bir sınıflandırmadır. Q5, Auris ve Qashqai J11 şanzıman beyni notlarında bülten ya da iyileştirme iddiaları doğrulanmadı.
- Kilometre aralıkları, özellikle az bildirimli kayıtlarda (Mini, Jogger, Grandland X), kaba tahmindir.
- Ayrı kayıt açılması o versiyonun diğerlerinden daha sorunlu olduğunu göstermez; kaynakların versiyonu ayırt ettiğini gösterir. Ayrı kayıt olmaması da "sorunsuz" anlamına gelmez.
- Doğrulama yine arama özetleriyle yapıldı; rakamlar, alıntılar ve model yılı için asıl sayfaya bakmak gerekir.

## 5. aşama: elektrikli araçlar

Tarih: 2026-10-24

Beşinci aşamanın isteği, elektrikli araçların da kapsama alınmasıydı. Önceki aşamalarda BYD, Togg, Tesla ve Chery "motor grubu ve ikinci el geçmişi yok" gerekçesiyle dışarıda bırakılmıştı; bu bir kullanıcı talebi değil, planlama sırasında alınmış bir karardı ve kaldırıldı. Kurallar aynı kaldı: her sorun için en az iki farklı site ve bunlardan en az biri deneyim ya da resmî türünde; ayrıntı yalnızca kaynağı metinde anılan iddialardan; kaynak bulunamayan grup plana `–` olarak işlenir.

| | 4. aşama sonu | 5. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 136 | 148 |
| Kronik sorun | 205 | 220 |
| Ayrıntısı olan sorun | 205 | 220 |
| Yıl kırılımı olan sorun | 48 | 52 |
| Marka | 22 | 27 |
| Sorunlara bağlı kaynak bağlantısı | 1161 | 1281 |
| Farklı kaynak sitesi | 68 | 71 |
| Yalnızca iki siteyle desteklenen sorun | 44 | 46 |
| Plan satırı | 245 | 276 |
| Plan durumu (✓ / – / ○) | 132 / 113 / 0 | 144 / 132 / 0 |

### Ne yapıldı

- **Kapsam kararı:** BYD, Togg ve Tesla kapsama alındı; Chery `ek` kademesine geçti (Omoda E5 arandı, bulunamadı); Smart ve Porsche `ek` kademeyle eklendi. `KAPSAM.md` ölçütü, `README.md` ve plan notları buna göre güncellendi. Yalnızca tam elektrikliler kapsamda; hibrit ve plug-in hibritler (ör. BYD Seal U DM-i) dahil değil.
- **Plan:** 245 satırdan 276'ya çıktı (+31): 12'si veritabanına girdi, 19'u kanıt yetersiz olduğu için eklenmedi. Sırada (○) satır yok.
- **Yeni kayıt:** 12 yeni araç/motor kaydı ve 15 yeni sorun; beş yeni marka (BYD, MG, Porsche, Tesla, Togg). Yeni sorunların 9'u `Yüksek`, 5'i `Orta`, 1'i `Düşük` risk seviyesinde.
- **Kaynaklar:** 120 bağlantı eklendi. Kayıt defterine üç site girdi: SpeakEV (forum), InsideEVs ve electrive.com (haber). Her adresin arama sonuçlarında tam eşleşmeyle geçtiği yazım sırasında otomatik denetlendi. Resmî belge olarak NHTSA geri çağırma dosyaları, haber olarak electrive ve InsideEVs, deneyim olarak Şikâyetvar, DonanımHaber, Ekşi Sözlük ve SpeakEV kullanıldı.
- **Dönem kırılımı:** dört yeni sorunda geri çağırma kapsamına göre (Ioniq 5 / 6, EV6, EQA / EQB, Taycan).
- **Ayrıntılar:** 15 yeni sorunun hepsinde `detay` var; alan doluluğu: neden 15, teşhis 15, çözüm 15, maliyet 4, önlem 5.
- **Görüntüleyici:** filtre kutusuna "Yalnızca elektrikli araçlar" seçeneği eklendi.
- **Yöntem aynı:** sayfalar açılamadı (bu oturumda `WebFetch` ağ hatası veriyor); Türkçe aramalar Şikâyetvar, DonanımHaber, OTOPARK.COM ve Ekşi Sözlük'e, geri çağırma aramaları NHTSA, CarComplaints, InsideEVs, Electrek ve electrive'e sınırlandı.

### Elektrikli araçlar nasıl ele alındı

- **`motor` alanı:** `Elektrik` ile başlar, batarya ya da sürüm parantez içinde yazılır (ör. `Elektrik (52,4 kWh ve 88,5 kWh)`). Sorunlar elektrikli araca özgü parçalara ait: batarya hücreleri, dahili şarj cihazı (OBC), entegre şarj kontrol ünitesi (ICCU), 12V yardımcı akü, elektrik tahrik sistemi ve yazılım.
- **Aynı platformu paylaşan modeller ayrı kayıt:** Peugeot e-208 / e-2008, Opel Corsa-e / Mokka-e ve Citroën ë-C4 aynı platformun ürünleri ve aynı "elektrik tahrik sistemi arızası" uyarısını veriyor; her marka kendi Şikâyetvar kayıtlarıyla ayrı kayıt oldu, nedenler SpeakEV ve electrive'deki ortak kaynaklara bağlandı (4. aşamadaki PSA DV5 zincir kayıtlarıyla aynı mantık).
- **Geri çağırma kayıtlarının Türkiye kapsamı:** geri çağırmaların çoğu ABD (NHTSA) ya da Avrupa (KBA) kaynaklı. Kayıt yalnızca Türkiye'den bağımsız bir sahip bildirimi de varsa açıldı: Ioniq 5 (ICCU ve 12V akü uyarıları), Kia EV6 (12V akü), Mercedes EQB (Mercedes-Benz Türkiye'den geri çağırma e-postası ve "riskli batarya" SMS'i), Taycan (batarya modülü sıcaklık sensörü ve modül değişimi). Türkiye bildirimi olmayanlar `–` olarak plana yazıldı (Mini Cooper SE, BMW iX / i4, Audi e-tron GT, Nissan Leaf).
- **Geri çağırma pencereleri Türkiye'ye uymayanlar:** Hyundai Kona Electric batarya yangını geri çağırması 2017-2020 üretimini kapsıyor, Türkiye'de elektrikli Kona'nın resmî satışı Eylül 2021'de başladı; Volvo EX30 hücre geri çağırması Avrupa'da yalnızca sağ direksiyonlu 69 kWh modeller için yazılıyor; VW'nin Ekim 2026 ID. batarya geri çağırması belirli partileri kapsıyor ve ABD'deki ID.4 geri çağırmaları Zwickau ve Emden üretimi Avrupa araçlarını kapsamıyor. Bunların hiçbiri Türkiye için doğrulanamadı; üçü de nedeniyle `–`.
- **Versiyonlar:** Togg V1 / V2 donanımı ve 52,4 / 88,5 kWh bataryalar, MG4 Comfort / Luxury ve Ioniq 5'in iki bataryası kayıt adında anıldı ama ayrı kayıt açılmadı, çünkü kaynaklar sorunları versiyona göre ayırmıyor (MG4'te V1 / V2 farkı bir forum yorumundan, doğrulanmadı). Geri çağırma kapsamı model yılına göre değiştiğinde `donem_kirilimi` kullanıldı.

### Eklenen kayıtlar

- **Tesla Model Y (2):** cam tavanın kendiliğinden çatlaması; alt takımdan gıcırtı ve metalik vuruntu.
- **Togg T10X (3):** AC şarjın kesilmesi (OBC); "Enerji Sistemi Arızası" uyarısı ve 12V akü; ekran kapanması ve güncelleme sonrası aksaklıklar.
- **BYD Atto 3 (1):** 12V akü arızası ve "güç sistemi arızası". **MG4 Electric (1):** DC hızlı şarj alamama.
- **Hyundai Ioniq 5 / Ioniq 6 (1)** ve **Kia EV6 (1):** ICCU arızası, 12V akünün şarj olmaması ve güç kaybı (geri çağırma).
- **Mercedes-Benz EQA / EQB (1):** yüksek gerilim batarya hücre kusuru ve yangın riski (geri çağırma, batarya değişimi).
- **Peugeot e-208 / e-2008, Opel Corsa-e / Mokka-e, Citroën ë-C4 (1'er):** elektrik tahrik sistemi arızası ve yolda kalma.
- **Renault Zoe (1):** şarj hatası mesajları ve şarjın kesilmesi. **Porsche Taycan (1):** yüksek gerilim batarya modülü kısa devre riski (geri çağırma).

### Araştırılıp eklenmeyen gruplar

Plana 19 yeni `–` satırı işlendi (toplam 132). Her satırın nedeni [KAPSAM.md](KAPSAM.md) içinde yazılıdır. Başlıca nedenler:

- **Kanıt tek siteye dayanıyor (çoğunlukla Şikâyetvar):** Renault Megane E-Tech, Fiat 500e, Kia Niro EV / EV3, BYD Dolphin / Seal, MG ZS EV, Dacia Spring, Audi Q4 e-tron, Skoda Enyaq / Elroq.
- **Geri çağırma var ama Türkiye kapsamı ya da Türkiye bildirimi yok:** Hyundai Kona Electric, Volvo EX30, VW ID.4 / ID.3 / ID.7, Cupra Born, BMW iX / i4, Audi e-tron GT, Nissan Leaf, Mini Cooper SE.
- **Modele özgü kaynak çıkmadı ya da yanlış model:** Tesla Model 3 (sonuçlar Model Y ve Wall Connector'a ait), BMW i3 (Türkiye'de range extender yok), Chery Omoda E5 (çıkanlar benzinli Omoda 5), Smart #1.

### Kanıtı sınırlı ayrıntılar

- **Kilometre aralıkları:** elektrikli şikâyetlerin çoğunda kilometre yazmıyor. Kilometre kaynakta olmayan kayıtlarda (Model Y gıcırtı, Togg ekran, BYD Atto 3, MG4, Zoe, EQA / EQB, Taycan, Opel Corsa-e / Mokka-e, Citroën ë-C4) aralık araçların yaşına ya da aynı kaynaklardaki diğer kilometrelere göre kaba tahmin edildi ve bu ilgili `detay` metninde söylendi.
- **Togg T10X:** Togg'un resmî açıklaması ya da servis bülteni bulunamadı; güncelleme ve sorun arasındaki ilişkiler kullanıcı yorumu. Dönem kırılımı eklenmedi, çünkü "v1 / v2" donanım seviyesini mi model yılını mı kastettiği net değil.
- **Tesla Model Y cam tavan:** Tesla'nın teknik açıklaması yok; nedenler kullanıcı teorileri, servisin "darbe kaynaklı" gerekçesi de kullanıcı aktarımı. Fiyatlar tarihsiz.
- **BYD Atto 3 12V akü:** Şikâyetvar dışındaki iki kaynak tek vaka (Malezya'dan bir haber, İngiltere'den bir SpeakEV konusu); Türkiye'den kilometre yok.
- **MG4:** V1 / V2 ve "r66 yazılımı" iddiaları tek kullanıcıya dayanıyor, doğrulanmadı.
- **Ioniq 5 / 6 ve EV6:** geri çağırma kapsamı ABD'ye ait; Türkiye'de DonanımHaber'de paylaşılan "41D033" güncellemesi resmî belgeyle doğrulanmadı. EV6'da Türkiye şikâyetleri 12V akü ve garanti kapsamı üzerine; ICCU ile bağlantısı kaynaklarda kurulmuyor.
- **EQA / EQB:** Türkiye'de değişim takvimi belirsiz; batarya garantisinin bakım gecikmesi gerekçesiyle iptal edildiği iddiası doğrulanmadı.
- **Peugeot / Opel / Citroën:** uyarının nedeni araca göre değişiyor (12V akü, OBC, şanzıman kontrolcüsü, klima kompresörü, kablo demeti); SpeakEV ağırlıklı olarak İngiltere'den. Citroën ë-C4 yalnızca iki siteyle (Şikâyetvar, electrive) destekleniyor.
- **Renault Zoe:** Türkiye'den birkaç şikâyet; ayrıntılar ağırlıkla SpeakEV'den. Bir Ekşi Sözlük kullanıcısının "istasyonlar bozuk" aktarımı tek vaka.
- **Porsche Taycan:** DonanımHaber'deki modül değişimi tek kullanıcı; Şikâyetvar'daki elektrik sistemi uyarısının geri çağırmayla ilişkisi kurulamadı.

### Yalnızca iki siteyle desteklenen yeni maddeler

- MG MG4 Electric (2023-): DC hızlı şarj istasyonlarında şarj alamama (DonanımHaber Forum, Şikâyetvar)
- Citroen ë-C4 / ë-C4 X (2021-): Elektrikli çekiş sistemi arızası ve yolda kalma (electrive.com, Şikâyetvar)

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **Togg ekran çözümü:** arama özetinin "menüden sıfırlayın, Togg Care'den talep açın" tavsiyesi kaynağı gösterilmediği için çıkarıldı; yerine kaynaktaki ifadeler (yeniden başlatma, güncelleme ve sıfırlama yapılmamasının bir yazarca suçlanması, randevu ve onarım süreleri) yazıldı.
- **Model Y cam tavan:** forum başlıklarındaki tek bir kullanıcının anlatımı "kullanıcılar" diye çoğul yazılmıştı, tek kullanıcı olarak düzeltildi.
- **Hyundai Kona Electric:** ilk taslakta batarya yangını geri çağırmasıyla eklenmesi düşünüldü; Türkiye'de resmî satışın Eylül 2021'de başladığı (geri çağırma penceresinin 2017-2020 olduğu) görülünce çıkarıldı.
- **Volvo EX30 ve VW ID. geri çağırmaları:** Türkiye kapsamı doğrulanamadığı için kayıt açılmadı, plan notuna yazıldı.
- **Zoe başlangıç yılı:** Türkiye'de Z.E. 50 Aralık 2020'de satışa çıktı, ama bir şikâyet 2019 model araca ait; kayıt "2019-" olarak açıldı.

### Dikkat edilecek sınırlar

- Elektrikli filo genç ve küçük; "kronik" burada "birkaç bağımsız kullanıcı aynı arızayı tekrar bildiriyor" düzeyinde. Şikâyetvar ağırlığı yüksek; bu site sorunlu vakaları öne çıkarır, bir sorunun orada görünmesi sıklığı göstermez.
- Şikâyetlerin büyük kısmı servis gecikmesi, parça beklemesi ve garanti tartışması üzerine; bunlar teknik arıza olmadığı için ancak bir arızanın bağlamı olarak kayıtlara girdi.
- Geri çağırma bilgileri ABD, Avrupa ve Çin kayıtlarına dayanıyor; kapsam için şasi numarasıyla yetkili servise ya da Ticaret Bakanlığı'nın geri çağırma kayıtlarına bakmak gerekir.
- Doğrulama yine arama özetleriyle yapıldı; rakamlar, alıntılar ve model yılı için asıl sayfaya bakmak gerekir.

## 6. aşama: Astra Electric açığı ve diğer elektrikliler

Tarih: 2026-10-24

Altıncı aşama bir kullanıcı sorusundan çıktı: Opel Astra Electric (54 kWh, 115 kW / 156 PS) listede yoktu ve neden alınmadığı soruldu. Dürüst cevap, Astra Electric'in kanıt yetersizliği yüzünden elenmediği, hiç aranmadığıdır: 5. aşamada elektrikli model listesi satış ve şikâyet hacmine göre elle kurulmuştu (Tesla, Togg, BYD, MG, Hyundai / Kia, Mercedes EQA / EQB, Peugeot e-208 / e-2008 gibi) ve Stellantis'in 54 kWh / 156 PS sürücü paketli yeni modelleri (Astra Electric, e-308, Avenger Electric, Fiat 600e, Alfa Romeo Junior) plana hiç girmemişti. Eksiklik kanıt eşiğinden değil, kapsamın kuruluşundan kaynaklandı. Bu aşamada Türkiye'de satılan elektrikli modellerden planda olmayanlar sistematik olarak arandı. Kurallar aynı kaldı.

| | 5. aşama sonu | 6. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 148 | 154 |
| Kronik sorun | 220 | 227 |
| Ayrıntısı olan sorun | 220 | 227 |
| Yıl kırılımı olan sorun | 52 | 59 |
| Marka | 27 | 28 |
| Sorunlara bağlı kaynak bağlantısı | 1281 | 1321 |
| Farklı kaynak sitesi | 71 | 78 |
| Yalnızca iki siteyle desteklenen sorun | 46 | 48 |
| Plan satırı | 276 | 295 |
| Plan durumu (✓ / – / ○) | 144 / 132 / 0 | 150 / 145 / 0 |

### Ne yapıldı

- **Yeni kayıt:** 6 yeni araç/motor kaydı ve 7 yeni sorun; bir yeni marka (Jeep). Yeni sorunların 6'sı `Yüksek`, 1'i `Orta` risk seviyesinde. Hepsinde `detay` var; alan doluluğu: neden 7, teşhis 7, çözüm 7, maliyet 2.
- **Sürüm notları:** Peugeot e-208 / e-2008, Opel Corsa-e / Mokka-e ve Citroën ë-C4 kayıtlarının `motor` alanı artık iki sürümü söylüyor (50 kWh / 136 PS ve 2024 sonrası 54 kWh / 156 PS); ana sorunlara bu iki dönemi açıklayan `donem_kirilimi` eklendi.
- **Plan:** 276 satırdan 295'e çıktı (+19): 6'sı veritabanına girdi, 13'ü kanıt yetersiz olduğu için eklenmedi. Zeekr, Xpeng ve Leapmotor `ek` kademeyle marka listesine girdi; Jeep ve Alfa Romeo notları güncellendi. Dört mevcut `–` satırı genişletildi (Kia Niro EV, Smart, BYD, Hyundai Kona / Inster).
- **Kaynaklar:** 40 bağlantı eklendi (37'si yeni sorunlarda, 3'ü sürüm notlarında). Kayıt defterine yedi site girdi: auto motor und sport, autohaus.de, ÖAMTC, Que Choisir, SıfırAraçAl, Stellantis Medya ve Testcoches. Her adresin arama sonuçlarında tam eşleşmeyle geçtiği yazım sırasında otomatik denetlendi.
- **Yöntem aynı:** sayfalar açılamadı (bu oturumda `WebFetch` ağ hatası veriyor); Türkçe aramalar Şikâyetvar, DonanımHaber, OTOPARK.COM ve Ekşi Sözlük'e sınırlandı; geri çağırma ve yabancı kaynak aramaları kısıtsız ya da NHTSA, CarComplaints, SpeakEV, InsideEVs, electrive ve Alman otomotiv sitelerine sınırlandırılarak yapıldı.

### Eklenen kayıtlar

- **Opel Astra Electric (2023-2025), 54 kWh, 115 kW / 156 PS (2 sorun):** elektrik çekiş sistemi arızası uyarısı ve yolda kalma; yokuşta kalkışta aracın ters yönde hareket etmesi (motor ve gövde kontrol ünitesi yazılımı geri çağırması, Mart-Ağustos 2023 üretimi).
- **Peugeot e-308 (2023-2025), aynı 54 kWh / 115 kW sürücü paketi (1 sorun):** elektrik çekiş sistemi arızası uyarısı ve yolda kalma (Şikâyetvar, DonanımHaber).
- **Jeep Avenger Electric (2023-) (1 sorun):** elektrikli çekiş sistemi arızası ve ani güç kaybı; KBA'nın 15947R numaralı geri çağırması elektrikli park kilidi bağlantılarındaki korozyonu neden gösteriyor.
- **Fiat 600e (2024-) (1 sorun):** elektrikli çekiş sistemi arızası ve ani motor kesilmesi (Şikâyetvar, Que Choisir soruşturması).
- **Kia EV3 (2024-) (1 sorun):** ICCU arızası, AC şarj almama, 12V akü sorunu ve yolda kalma (Şikâyetvar, DonanımHaber, Ekşi Sözlük, Testcoches).
- **Mercedes-Benz EQC (2019-2023) (1 sorun):** yüksek gerilim batarya arızası ve pahalı onarım; 2019 üretimi batarya gövdesi sızdırmazlığı geri çağırması (KBA 010923).

### Astra Electric'in kanıt durumu

- **Astra'ya özgü bağımsız ikinci site yok.** Çekiş sistemi arızası şikâyetleri yalnızca Şikâyetvar'da (2024 ve 2025 model GS ile Ultimate araçlar). Ekşi Sözlük'teki "opel astra elektrik" başlığı ağırlıkla olumlu; arıza olarak çekiş sistemi değil, servislerin elektrikli araçlara pek hâkim olmadığı yorumu öne çıkıyor. Bu yüzden Astra kaydı, aynı 54 kWh batarya ve 115 kW / 270 Nm motor değerlerine sahip Peugeot e-308 sahiplerinin DonanımHaber başlığını da kaynak olarak kullanıyor ve bunu `detay` metninde açıkça söylüyor. Bu bağlantı kayıt kuralını (iki site) sağlar, ancak Astra için doğrudan kanıt değildir.
- **Geri çağırma:** auto motor und sport'a göre KBA kaydı 1.466 aracı (843'ü Almanya'da) kapsıyor; Türkiye'deki araçların kapsamı doğrulanamadı. İkinci kaynak Araclo (düşük güvenli); kayıt bu yüzden "yalnızca iki siteyle desteklenen" listesinde.
- **Sürüm sınırı:** Astra Electric ve e-308 2025 sonunda / 2026 başında 58 kWh bataryalı güncel sürüme geçti (electrive, ev-database; Türkiye'de e-308 için satış Şubat 2026 olarak bekleniyordu). Bu sürüm için kaynak yok; kayıtlar 2023-2025 ile sınırlandı.
- **Kullanılmayan kaynak:** Araclo'nun "Astra-e Ultimate" sayfası (termal yönetim, OBC arızası) kullanılmadı: sayfa Astra L'nin STLA Medium platformunda olduğunu yazıyor (doğru değil) ve arıza listesi şablon gibi.

### 50 kWh / 136 PS ve 54 kWh / 156 PS sürümleri

- Peugeot e-208 / e-2008, Opel Mokka (Electric) ve Citroën ë-C4 Avrupa'da 2024'te 54 kWh / 115 kW (156 PS) sürüme geçti. Türkiye'de e-2008'in 156 PS sürümü (haber), Mokka Electric'in 54 kWh sürümü (Stellantis Türkiye bülteni) ve 2025 model ë-C4 X Max (156 HP) ikinci el ilanı var; Corsa Electric'in Türkiye'deki güncel sürümü doğrulanamadı.
- Şikâyetvar kayıtları batarya kapasitesi yazmadığı için bu üç ailenin sorunları sürüme göre ayrılamıyor. Kural gereği kayıtlar bölünmedi; `motor` alanı iki sürümü anıyor, `donem_kirilimi` hangi dönemin hangi sürüme denk geldiğini açıklıyor (durum her iki dönemde `Görülebilir`).

### Araştırılıp eklenmeyen gruplar

Plana 13 yeni `–` satırı işlendi (toplam 145). Her satırın nedeni [KAPSAM.md](KAPSAM.md) içinde yazılıdır. Başlıca nedenler:

- **Kanıt tek siteye dayanıyor (Şikâyetvar):** Peugeot e-3008 / e-5008, Alfa Romeo Junior Elettrica, Togg T10F, Kia EV9, Opel Frontera Electric, Citroën ë-C3, Fiat Grande Panda, Ford Puma Gen-E, Leapmotor T03, Hyundai Inster. Stellantis modellerinde (e-3008, Junior, ë-C3) Şikâyetvar'da "elektrikli çekiş sistemi arızası" şikâyetleri tekrar ediyor; ikinci bağımsız site bulunamadığı için kayıt açılmadı.
- **Modele özgü kayıt çıkmadı:** Zeekr, Xpeng, Renault Scenic E-Tech / 5 E-Tech, Ford Mustang Mach-E ve Explorer Electric, Smart #3.
- **Geri çağırma var ama belirtisi Türkiye şikâyetleriyle uyuşmuyor:** Mercedes EQE / EQS (NHTSA 24V372 sürüş gücü kaybı; Türkiye'de şarj almama ve menzil şikâyetleri).
- **Derinlik notu:** Frontera Electric, ë-C3, Grande Panda, Puma Gen-E ve Inster için tek bir tarama sorgusuyla bakıldı; ayrıca ikinci site araması yapılmadı. Daha derin aramayla kayıt açılabilir.

### Kanıtı sınırlı ayrıntılar

- **Kilometre aralıkları:** Astra Electric, e-308, Avenger Electric, 600e, EV3 ve EQC kayıtlarında kilometre çoğu şikâyette yok; aralıklar kaba tahmin ve ilgili `detay` metninde söylendi. Astra geri çağırması yazılım hatası olduğu için kilometreyle ilişkili değil, aralık biçim gereği verildi.
- **Avenger Electric:** geri çağırmanın yalnızca tam elektrikli Avenger'ları kapsadığı auto motor und sport'un araştırmasına dayanıyor; Jeep doğrulamadı. Türkiye kapsamı doğrulanamadı. Aynı marka için başka bir yazılım geri çağırması (Fiat 600e, Avenger Electric ve Alfa Romeo Junior için rejeneratif fren yazılımı, 13.458 araç) arıza kaydı olarak eklenmedi: etkisi yüksek enerji tüketimi, güvenlik riski yok.
- **Fiat 600e:** Que Choisir soruşturmasının tam metni açılamadı (arama özeti); veriler Fransa'dan. Şikâyetvar'ın "Fiat Genel Merkez" sayfası bir araç değişimi talebini listeliyor, 600 Hybrid sayfasındaki 600e yorumu tek vaka.
- **Kia EV3:** ICCU geri çağırması EV3'ü kapsamıyor (ABD listeleri EV6, Ioniq 5 / 6 ve Genesis); MOSFET açıklaması bir kullanıcı tahmini, Testcoches İspanyol haber sitesi sorunun E-GMP ailesinde görüldüğünü yazıyor ve kendi bilgisinin sınırlı olduğunu söylüyor.
- **Mercedes EQC:** geri çağırma yalnızca 2019 üretimini kapsıyor; Şikâyetvar vakaları 2020 model. Bir şikâyette garanti, aracın gri piyasadan gelmesi nedeniyle reddedilmiş; Ekşi Sözlük'teki "kronik batarya sorunu" yorumu tek kullanıcı.
- **Peugeot e-308:** hangi şikâyetin hangi sahibe ait olduğu özetlerde tam ayrılamadı; "son 6 ayda 4 kez yolda kaldı" ve "87 gün serviste" bilgileri aynı sahibe ait yazıldı.

### Yalnızca iki siteyle desteklenen yeni maddeler

- Opel Astra Electric (2023-2025): Yokuşta kalkışta aracın ters yönde hareket etmesi (auto-motor-und-sport.de, Araclo)
- Peugeot e-308 (2023-2025): Elektrik çekiş sistemi arızası uyarısı ve yolda kalma (DonanımHaber Forum, Şikâyetvar)
- Fiat 600e (2024-): Elektrikli çekiş sistemi arızası ve ani motor kesilmesi (Que Choisir, Şikâyetvar)
- Citroën ë-C4, sürüm notuna eklenen bir ikinci el ilanı sayesinde üç siteye çıktı ve bu listeden çıktı (Şikâyetvar, electrive.com, arabam.com).

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **Peugeot e-308:** taslaktaki "aynı uyarı e-3008 sahiplerinden de bildiriliyor" cümlesi, ilgili sayfa kaynak listesinde olmadığı için çıkarıldı.
- **Mercedes EQC:** "Şikâyetvar'daki arızalar 2020 model araçlara ait" genellemesi, yalnızca iki şikâyetin model yılı bilindiği için yumuşatıldı.
- **Astra Electric:** Araclo sayfasındaki termal yönetim ve OBC başlıkları arıza kanıtı olarak alınmadı (yukarıya bakın).

### Dikkat edilecek sınırlar

- Elektrikli filo genç ve küçük; "kronik" burada "birkaç bağımsız kullanıcı aynı arızayı tekrar bildiriyor" düzeyinde. Şikâyetvar ağırlığı yüksek; bu site sorunlu vakaları öne çıkarır, bir sorunun orada görünmesi sıklığı göstermez.
- Stellantis'in 54 kWh / 156 PS ailesinde (Astra Electric, e-308, Avenger Electric, 600e, Junior, Mokka, e-2008) Şikâyetvar'da aynı "elektrikli çekiş sistemi arızası" belirtisi tekrar ediyor; nedenler modele göre farklı (Avenger'da park kilidi bağlantıları, 600e'de 12V akü ve invertör ipuçları, diğerlerinde kaynaklarda açık neden yok). Ortak belirtiyi ortak neden saymak doğrulanmadı.
- Geri çağırma bilgileri Almanya (KBA), ABD ve Çin kayıtlarına dayanıyor; kapsam için şasi numarasıyla yetkili servise ya da Ticaret Bakanlığı'nın geri çağırma kayıtlarına bakmak gerekir.
- Doğrulama yine arama özetleriyle yapıldı; rakamlar, alıntılar ve model yılı için asıl sayfaya bakmak gerekir.

## Sonraki adımlar

1. Ağ erişimi verilirse `KAYNAKLAR.md` içindeki sayfalar doğrudan okunarak her bağlantının iddiayı gerçekten içerdiği, ayrıntılardaki rakam ve alıntıların doğru olduğu kontrol edilebilir.
2. Yalnızca iki siteyle desteklenen 48 maddeye (3. aşama sonundaki 22, 4. aşamada eklenen 22, 5. aşamada eklenen 2; 6. aşamada üç madde eklendi, Citroën ë-C4 üçüncü kaynak alarak listeden çıktı) üçüncü bir kaynak eklenebilir.
3. Kanıtı yetersiz bulunan 145 grup için [KAPSAM.md](KAPSAM.md) içinde nedenleriyle yazılı; yeni kaynak çıkarsa eklenebilir. Nedeni "ikinci bağımsız kaynak yok" olanlar (ör. Hyundai Kona, Opel Mokka 1.6 CDTI, Honda City, Ford Transit Custom ve Ranger, Nissan Navara, Isuzu D-Max, Toyota Hilux, Fiat Ducato, Renault Megane E-Tech, Fiat 500e, Kia Niro EV, Peugeot e-3008, Alfa Romeo Junior Elettrica, Togg T10F, Kia EV9) için Şikâyetvar dışında bir forum ya da haber kaynağı bulunması yeterli olur.
4. "Kanıtı sınırlı ayrıntılar" listelerindeki maddeler Türkçe servis ya da forum kaynağıyla güçlendirilebilir; maliyet alanı boş kalan 87 soruna güncel Türkiye fiyatı bulunursa eklenebilir.
5. Elektrikli araçlarda geri çağırma kaydı bulunan ama Türkiye kapsamı doğrulanamayan aileler (Volvo EX30, VW ID. serisi, Mini Cooper SE, BMW iX / i4, Audi e-tron GT) için Türkiye distribütörlerinin duyuruları ya da Ticaret Bakanlığı geri çağırma kayıtları bulunursa kayıt açılabilir.
6. Hibrit ve plug-in hibrit araçlar (Toyota hibritleri, BYD Seal U DM-i gibi) bu aşamada kapsam dışı bırakıldı; istenirse aynı kurallarla eklenebilir.
7. Kaynaklar ayırt ettikçe yeni motor versiyonları ayrı kayıt olabilir (ör. N47 177 / 184 bg); eklemek istenen yeni marka, model ve motor için plana satır eklenip aynı döngü uygulanır.
