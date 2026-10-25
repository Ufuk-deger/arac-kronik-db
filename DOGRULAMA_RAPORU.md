# Doğrulama raporu

Tarih: 2026-10-24

Rapor on iki aşamayı kapsar. Aşağıdaki ilk bölümler 1. aşamayı (ilk sürümün doğrulanması) anlatır; [2. aşama](#2-aşama-en-çok-satan-modellerin-motor-grupları-ve-yıl-kırılımı) en çok satan modellerin eklenmesini ve yıl kırılımını, [3. aşama](#3-aşama-sorun-ayrıntıları) her soruna eklenen ayrıntıları, [4. aşama](#4-aşama-ölçeğin-genişletilmesi-ve-motor-versiyonları) ölçeğin genişletilmesini ve motor versiyonlarını, [5. aşama](#5-aşama-elektrikli-araçlar) elektrikli araçların kapsama alınmasını, [6. aşama](#6-aşama-astra-electric-açığı-ve-diğer-elektrikliler) Astra Electric açığının ve diğer eksik elektrikli modellerin ele alınmasını anlatır, [7. aşama](#7-aşama-çok-ilanlı-modellerin-kapsam-kontrolü) çok ilanlı modellerin kapsam kontrolünü ve motor boşluklarının kapatılmasını, [8. aşama](#8-aşama-15-tsi-ve-etsi-motoru-ve-kullanan-modeller) 1.5 TSI ve eTSI motorunu ve onu kullanan modellerin ele alınmasını anlatır, [9. aşama](#9-aşama-çok-kullanılan-araçlarda-kaçırılanların-taraması) çok kullanılan araçlarda kaçırılanların taranmasını ve eksik nesil ve motor boşluklarının kapatılmasını anlatır, [10. aşama](#10-aşama-motor-ve-şanzıman-aileleri-ve-model-kataloğu) motor ve şanzıman ailelerinin kurulmasını, bu ailelerle eklenen kardeş model kayıtlarını ve eksik popüler modellerin kataloğunu anlatır, [11. aşama](#11-aşama-model-geneli-sorunlar-motordan-bağımsız) motordan bağımsız, modele (nesle) bağlı sorunların (cam tavandan su alma, kapı kilidi, boya atması, EPB arızası gibi) kaydedilmesini ve listede hiç olmayan modellerin plana eklenmesini, [12. aşama](#12-aşama-model-geneli-taramasının-sürdürülmesi) ise bu taramanın VAG, Renault / Stellantis / Ford grubu, Asya, premium ve elektrikli markalara genişletilmesini anlatır.

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

## 7. aşama: çok ilanlı modellerin kapsam kontrolü

Tarih: 2026-10-24

Yedinci aşamanın sorusu şuydu: sahibinden.com'da çok ilan sayısına ulaşmış her araç listede var mı? Dürüst cevap, tam olarak kontrol edilemediğidir: sahibinden.com'un canlı model sayıları bu oturumdan okunamıyor (`WebFetch` ağ hatası veriyor; arama sonuçlarına düşen sahibinden sayfaları 2020-2025 arası önbellek görüntüleri ve tarihleri karışık). Bu yüzden kontrol vekil verilerle yapıldı:

- **arabam.com** aylık ve yıllık ilan sıralamaları (Motor1, CNN Türk ve GZT aktarımıyla): Haziran 2026'da en çok ilan verilen on model Renault Clio, Renault Megane, Fiat Egea, Opel Astra, Toyota Corolla, Ford Focus, Volkswagen Passat, Honda Civic, Opel Corsa ve Volkswagen Polo; 2025 Ocak-Kasım ortalamasında bunlara Volkswagen Golf eklenmiş ve SUV'larda Nissan Qashqai, Dacia Duster, Peugeot 3008, Hyundai Tucson, Fiat Egea Cross ve Volkswagen Tiguan öne çıkmış. En çok ilanlı markalar Fiat / Renault, Volkswagen, Ford, Opel, Hyundai, Peugeot, Toyota, Citroën ve BMW.
- **Araclo'nun sahibinden verisine dayanan aylık ilan raporu:** metin olarak yalnızca marka payı veriyor (Haziran 2026'da Renault yüzde 14, Volkswagen yüzde 11, Fiat yüzde 8); model sıralaması grafikte, metne düşmüyor.
- **Cardata / Capital / CNN Türk listeleri (2020-2024):** Egea, Megane, Passat, Symbol, Linea, Clio, Polo, Golf, Focus ve Astra üst sıralarda.
- **Sahibindex'in eski raporları (2020 ve 2022):** Clio, Megane, Passat, Astra ve Focus.

Bunlar ilan sayısı değil sıralama; motor düzeyinde sayı hiçbir kaynakta yok. Tek istisna: Araclo, arabam.com'da yalnızca "Opel Astra 1.3 CDTI" filtresiyle 22.08.2026'da 1.441 aktif ilan göründüğünü aktarıyor.

### Sonuç

- **Model düzeyinde:** yukarıdaki on bir otomobil modelinin, altı SUV'un (Egea Cross, Egea kayıtlarının içinde) ve on markanın hepsi veritabanında var. Clio 5, Megane 3, Egea 3, Corolla 3, Astra 8, Focus 4, Passat 3, Civic 3, Polo 4, Corsa 4, Golf 6, Qashqai 3, Duster 4, Peugeot 3008 4, Tucson 3 ve Tiguan 3 kayıtla temsil ediliyor.
- **Motor düzeyinde:** boşluk vardı. Dört grup planda yok ya da kanıtı yetersiz sayılmıştı, ama çok ilanlı modellere aitti:
  - **Opel Astra H / J 1.3 CDTI:** planda hiç yoktu (Corsa 1.3 CDTI kaydı vardı). Eklendi.
  - **Ford Fiesta Mk7 1.4 / 1.6 TDCi:** kademe 1 olduğu halde `–` idi (Fiesta'ya özgü kaynaklar genel TDCi başlıklarıyla karışıktı). Bu aşamada Türkçe ve İngiliz forumlarında ortak bir enjektör, turbo ve EGR kümesi bulundu; eklendi.
  - **VW Golf 6 / Jetta 1.6 TDI:** planda yoktu (Golf 6 yalnızca 1.4 TSI idi). Eklendi.
  - **Peugeot 208 / 2008 / 308 / 3008 1.6 HDi / BlueHDi (DV6):** kademe 1 `–` idi, çünkü model düzeyindeki anılar dağınıktı ve ortak motor sorunları 301 ve C-Elysée kayıtlarında duruyordu; bu yüzden 308 / 3008 aramasında çıkmıyordu. 308 / 3008 için ayrı kayıt açıldı; üç DV6 sorunu ortak kaynaklarla taşındı, yeni olan AdBlue (SCR) arızası da eklendi ve aynı sorun 1.5 BlueHDi kaydına yazıldı.

| | 6. aşama sonu | 7. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 154 | 158 |
| Kronik sorun | 227 | 241 |
| Ayrıntısı olan sorun | 227 | 241 |
| Yıl kırılımı olan sorun | 59 | 59 |
| Marka | 28 | 28 |
| Sorunlara bağlı kaynak bağlantısı | 1321 | 1406 |
| Farklı kaynak sitesi | 78 | 78 |
| Yalnızca iki siteyle desteklenen sorun | 48 | 49 |
| Plan satırı | 295 | 296 |
| Plan durumu (✓ / – / ○) | 150 / 145 / 0 | 154 / 142 / 0 |

### Eklenen kayıtlar

- **Opel Astra H / J (2005-2015), 1.3 CDTI (4 sorun):** triger zinciri sesi ve uzaması; EGR kurumlanması ve DPF tıkanması (DPF yenilemesinde yakıtın yağa karışması dahil); turbo basınç hatası (selenoid valf, aktüatör, hortum kaçağı); Easytronic robotize şanzıman sarsıntısı.
- **Ford Fiesta Mk7 (2008-2017), 1.4 / 1.6 TDCi (3 sorun):** enjektör arızası ve enjektör contası sızıntısı; turbo arızası (kurum ve yağlama); EGR valfi kurumlanması ve DPF tıkanması.
- **Volkswagen Golf 6 / Jetta (2008-2013), 1.6 TDI CAYC (2 sorun):** EGR valfi ve DPF tıkanması; enjektör arızası.
- **Peugeot 208 / 2008 / 308 / 3008 (2012-2021), 1.6 e-HDi / BlueHDi DV6 (4 sorun):** AdBlue (SCR) arızası; enjektör dibi kaçağı; turbo yağ besleme süzgeci; EGR valfi tıkanması. Peugeot 1.5 BlueHDi (DV5) kaydına AdBlue sorunu eklendi (1 sorun).
- Yeni 13 sorunun 11'i `Orta`, 2'si `Yüksek` risk; hepsinde `detay` var (neden 13, teşhis 13, çözüm 13, maliyet 6, önlem 2). 85 bağlantı eklendi, yeni site girmedi.

### Çok ilanlı olduğu halde eksik ya da `–` kalan gruplar

Bunların çoğu "araştırıldı ama tekrar eden bir kronik sorun için iki bağımsız kaynak çıkmadı" anlamına geliyor; nedenleri [KAPSAM.md](KAPSAM.md) içinde yazılıdır. Bu aşamada yeniden arananlar:

- **Ford Focus 3 1.5 TDCi:** Türkçe kaynaklar 1.6 TDCi ve 2019 sonrası EcoBlue'ya ait; yalnızca Ford Owners Club'da (İngiltere) DPF, EGR ve çalışma sorunu konuları var.
- **Hyundai Accent Blue 1.4 CVT:** Şikâyetvar'da kalkışta çıtırdama ve çözülemeyen şanzıman arızası şikâyetleri var, ancak forumlar aynı motoru taksilerde 400-500 bin km sorunsuz buluyor; ikinci bağımsız doğrulama yok.
- **Hyundai i30 1.6 CRDi:** İngiltere forumlarında EGR tereddüdü ve çift kütleli volan, Türkçe kaynaklarda "kronik sorun yok" yorumları; ortak sorun bulunamadı.
- **Opel Mokka 1.4 Turbo:** şikâyetler motoru belirtmiyor ya da 1.2 PureTech'e ait.
- **VW Passat B7 / B8 2.0 TDI:** kaynaklar PD motorlu B6 ve DSG'ye ait.
- **Daha önce aranıp `–` kalanlar (bu aşamada yeniden aranmadı):** Renault Clio 4 / Symbol 1.2 16V, Megane 1.6 16V, Opel Corsa 1.2 / 1.4 benzinli, Fiat Linea 1.4, Egea 1.6 E-Torq, Toyota Corolla E170 1.6, Honda Civic FB7, BMW F30 B47 / B48, Mercedes W205 M274.

Planın dışında kalan çok ilanlı gruplar:

- **2011 öncesi model yılları** (Şahin / Kartal / Doğan, Albea / Palio, Clio 2, Megane 2, Passat B5, Astra G, BMW E46 gibi): zaman penceresi kuralıyla dışarıda; sahibinden'de ilan sayıları yüksek olabilir.
- **Hibritler** (Toyota Corolla ve C-HR hibrit, Honda City hibrit): elektrikli aşamasındaki kuralla kapsam dışı.
- **Hafif ticariler:** Doblo ve Fiorino / Qubo var; Ford Courier ve Transit, Renault Kangoo, Peugeot Partner ve Citroën Berlingo `–` ya da yok.
- **Planda hiç geçmeyen modeller:** Opel Meriva ve Zafira, VW Touran, Ford Fusion, Honda Accord, Renault Taliant.

### Kanıtı sınırlı ayrıntılar

- **Kilometre aralıkları:** Astra 1.3 CDTI, Fiesta TDCi, Golf 6 1.6 TDI ve Peugeot AdBlue kayıtlarında kaynaklar çoğunlukla kilometre yazmıyor; aralıklar kaba tahmin ve ilgili `detay` metninde söyleniyor.
- **Astra 1.3 CDTI:** kaynaklar H ve J kasayı birlikte anıyor; motor kodu (Z13DTH / A13DTC) kaynaklarda yok, kayıt adına yazılmadı. Zincir değişim aralığı konusunda kaynaklar çelişiyor (DonanımHaber 120-150 bin km, Vauxhall Owners Network'te 40.000 milde kopma vakası). Easytronic sorunu yalnızca iki siteye (DonanımHaber, Ekşi Sözlük) dayanıyor.
- **Fiesta TDCi:** İngiliz forumlarına (Ford Owners Club, Honest John) ağırlık veriyor; enjektör contası sızıntısı kaynaklı turbo arızası anlatımı birkaç sahibin teorisi.
- **Golf 6 1.6 TDI:** DSG'nin kendi sorunu Golf 6 1.4 TSI kaydında; bu kayıtta ayrıca ele alınmadı.
- **Peugeot DV6:** üç sorun 301 ve C-Elysée kayıtlarıyla ortak kaynaklara dayanıyor (aynı motor ailesi), 308 / 3008'e özgü ayrı bir şikâyet kümesi yok; bu `detay` metninde yazılı. AdBlue vakalarının bir kısmı 1.5 BlueHDi'ye ait olabilir; kaynaklar motoru her zaman belirtmiyor.

### Yalnızca iki siteyle desteklenen yeni maddeler

- Opel Astra H / J (2005-2015): Easytronic robotize şanzıman sarsıntısı ve arızası (DonanımHaber Forum, Ekşi Sözlük)

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **Astra 1.3 CDTI:** bir arama özetinde "5 yıl / 160.000 km gibi zincir rakamları Fiat Multijet'e ait, Opel motoru farklı" deniyordu; bu iddia doğrulanamadığı ve kayıtlardaki "Multijet" etiketiyle çeliştiği için taşınmadı. Zincir değişiminin maliyetinin yüksek olabileceğini söyleyen yorumun DonanımHaber'e mi Ekşi Sözlük'e mi ait olduğu arama özetinden ayrılamadığı için "forumlarda (DonanımHaber, Ekşi Sözlük)" diye genelleştirildi.
- **Golf 6 1.6 TDI:** bir DPF yorumunun ve bir rölanti anlatımının kaynağı Otopark yerine DonanımHaber olarak düzeltildi; yazılım güncellemesiyle sesin bittiği anlatımı marka belirtmeyen genel bir Şikâyetvar kaydı olduğu için öyle yazıldı.
- **Peugeot DV6:** bir enjektör `neden` metni 800 karakter sınırını aşınca kısaltıldı.
- **Peugeot AdBlue:** 1.5 BlueHDi'ye ait olabilecek yeni araç vakaları (2022-2023) 1.6 kaydında bu belirsizlikle anıldı, ayrıca 1.5 BlueHDi kaydına yazıldı.

### Dikkat edilecek sınırlar

- Sıralamalar sahibinden.com'dan değil arabam.com ve Cardata'dan; ilan sayısı değil sıra bilgisi. Sahibinden'in model sayıları paylaşılırsa karşılaştırma kesinleştirilebilir.
- "Çok ilanlı" ile "çok kronik sorunlu" aynı şey değil: ilanı çok olan bir motorun veritabanında olmaması çoğu zaman o motorda tekrar eden bir sorun bulunamadığı anlamına geliyor (örn. Mercedes M274, Honda Civic FB7).
- Doğrulama yine arama özetleriyle yapıldı; rakamlar, alıntılar ve model yılı için asıl sayfaya bakmak gerekir.

## 8. aşama: 1.5 TSI ve eTSI motoru ve kullanan modeller

Tarih: 2026-10-24

Sekizinci aşamanın isteği şuydu: 1.5 eTSI motorunu ve onu kullanan modelleri de ele almak. Bu motor VW grubunun 1.5 TSI (EA211 evo) ailesi: iki ve üçüncü silindiri kapatan ACT sürümü ile 48V hafif hibrit sürümü (VW'de eTSI, Skoda'da e-TEC ya da MHEV, Audi'de 35 TFSI). Önceki aşamalarda yalnızca Golf 8 ve Octavia A8 (vites kolu ve 48V), T-Roc ve Tiguan (yağ eksiltme) kayıtlıydı. Bu aşamada motoru kullanan diğer modeller tek tek arandı: Şikâyetvar, DonanımHaber, Otopark ve Ekşi Sözlük'te model ve motor adıyla; yabancı kaynaklarda geri çağırma ve forum taraması. `WebFetch` bu aşamada da kapalıydı, her şey arama özetleriyle yapıldı.

### Sonuç

Motorun iki tekrar eden sorunu var ve her ikisi de birçok modelde Türkçe kaynaklarda geçiyor: **48V hafif hibrit sistem ve alternatör-marş jeneratörü arızası** (eTSI, e-TEC, MHEV, 35 TFSI) ve **yağ eksiltme / düşük yağ uyarısı** (ACT'li 1.5 TSI). ACT'nin düşük devirde titreşimi üçüncü bir konu ama kanıtı daha zayıf. Altı model kayıt eşiğini geçti; bu modellerin her birinde yalnızca modele ait şikâyeti olan sorunlar yazıldı:

| Model | Motor | Kayıtlı sorunlar |
| --- | --- | --- |
| Volkswagen Golf 8 | 1.0 / 1.5 eTSI | vites kolu, 48V (önceki aşamalar) |
| Skoda Octavia A8 | 1.0 e-TEC / 1.5 TSI | vites kolu, 48V (önceki aşamalar) |
| Volkswagen T-Roc, Tiguan | 1.5 TSI | yağ eksiltme (önceki aşamalar) |
| **Seat Leon (KL, 2020-)** | 1.0 / 1.5 eTSI | 48V |
| **Cupra Formentor** | 1.5 eTSI | 48V (kardeş modellerin kaynaklarıyla, bkz. aşağıda) |
| **Skoda Superb (IV, 2024-)** | 1.5 TSI MHEV | 48V, yağ eksiltme |
| **Skoda Karoq** | 1.5 TSI | yağ eksiltme, düşük devirde titreşim (ACT) |
| **Volkswagen Passat (B8)** | 1.5 TSI | yağ eksiltme |
| **Audi A3 (8Y)** | 35 TFSI (1.5) | 48V ve "araç tahrik arızası" |

Kayıtlanmayıp plana `–` olarak yazılanlar (nedenleri [KAPSAM.md](KAPSAM.md) içinde): Golf 7.5 1.5 TSI, Seat Leon 5F 1.5 TSI, Ateca 1.5 TSI, Arteon 1.5 TSI, Kodiaq 1.5 TSI, Kamiq / Scala 1.5 TSI, Superb III 1.5 TSI, Audi Q2 / Q3 35 TFSI ve Passat B9 1.5 eTSI.

| | 7. aşama sonu | 8. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 158 | 164 |
| Kronik sorun | 241 | 249 |
| Ayrıntısı olan sorun | 241 | 249 |
| Yıl kırılımı olan sorun | 59 | 60 |
| Marka | 28 | 29 |
| Sorunlara bağlı kaynak bağlantısı | 1406 | 1443 |
| Farklı kaynak sitesi | 78 | 78 |
| Yalnızca iki siteyle desteklenen sorun | 49 | 53 |
| Plan satırı | 296 | 308 |
| Plan durumu (✓ / – / ○) | 154 / 142 / 0 | 160 / 148 / 0 |

### Eklenen kayıtlar

- **Seat Leon (KL, 2020-), 1.0 eTSI / 1.5 eTSI (1 sorun):** 48V hafif hibrit sistem ve alternatör-marş jeneratörü arızası (SOS ve "Hata: 48V beslemesi" uyarıları, yolda kalma; Şikâyetvar'da 39.000 km'de marş alternatörü ve hibrit akü vakası, iyi niyet desteği verilmemiş).
- **Cupra Formentor (2020-), 1.5 eTSI (1 sorun):** aynı 48V sorunu. Modele özgü kaynak tek bir Ekşi Sözlük yorumu ("kronik alternatör arızası tescilli", 1.5 eTSI'nin 2024 makyajıyla geldiği iddiası; aynı başlıkta bir başka yorumcu aracın kronik arızası olmadığını yazıyor). Diğer kaynaklar eTSI ailesinin DonanımHaber ve Şikâyetvar anlatıları; bu kayıt `detay` metninde de bu şekilde işaretli, risk `Orta`, 2024 sonrası için `Görülebilir` dönem kırılımı var.
- **Skoda Superb (IV, 2024-), 1.5 TSI MHEV (2 sorun):** 48V sistem ve alternatör arızası (Şikâyetvar'da "akü şarj etme arızası" ile ilk haftada yolda kalma, 45.000 km'de de süren sorun, alternatör değişimi gerektiği söylenen vaka); yağ eksiltme (5.000 km'de eksiltme, iki ücretli servis ziyaretine rağmen süren vaka).
- **Skoda Karoq (2017-), 1.5 TSI 150 (2 sorun):** yağ eksiltme (Şikâyetvar'da Mart 2024 tarihli Karoq 1.5 TSI'da ilk günden her 5.000 km'de uyarı, iki yetkili serviste "kitapçıkta yazan normal durum"; Otopark'ta 11 bin km'de 1 litre ve 15 bin km'de 1 litre vakaları); düşük devirde titreşim ve düzensiz rölanti (ACT silindir kapatma, motor takozu, PCV kurumu, LSPI; risk `Düşük`).
- **Volkswagen Passat (B8, 2015-2023), 1.5 TSI 150 (1 sorun):** yağ eksiltme (2021 modeller 12.000-14.200 km'de, ilk bakımdan önce uyarı; servis "normal" diyor ve yağı ücretli tamamlıyor).
- **Audi A3 (8Y, 2020-), 35 TFSI 1.5 (1 sorun):** 48V sistem ve alternatör arızası, "araç tahrik arızası" uyarısı (72.000 km'de çekiciyle servise gitme, 49.000 km'de 77.000 TL katkı payı talebi, alternatör parçası 166.619 TL / bakım karşılığı 76.500 TL beyanı; Ekşi Sözlük'te "35 TFSI olarak geçen yeni nesil VAG araçlarında kronik alternatör arızası" iddiası).
- Yeni 8 sorunun 4'ü `Orta`, 3'ü `Yüksek`, 1'i `Düşük` risk; hepsinde `detay` var (neden 8, teşhis 6, çözüm 8, maliyet 3, önlem 4). 37 bağlantı eklendi, yeni site girmedi.

### Plan değişiklikleri

- **Cupra Formentor** `–` iken kayıtlandı (✓).
- **Passat B8 "2.0 TDI / 1.5 TSI / 1.4 TSI"** satırı bölündü: 1.5 TSI kayıtlandı, 2.0 TDI / 1.4 TSI `–` kaldı.
- **Karoq / Kodiaq "1.5 TSI / 2.0 TDI"** satırı bölündü: Karoq 1.5 TSI kayıtlandı; Kodiaq ve Karoq 2.0 TDI `–` kaldı.
- **Seat Leon 5F / 1P**, **Skoda Superb** ve **Fabia / Superb** satırlarının model eşleşmesi daraltıldı; yeni Leon KL ve Superb IV kayıtları bu satırlara karışmasın diye.
- **Yeni `–` satırları (7):** Golf 7.5 1.5 TSI, Seat Leon 5F 1.5 TSI, Kamiq / Scala 1.5 TSI, Arteon 1.5 TSI, Audi Q2 / Q3 35 TFSI, Passat B9 1.5 eTSI ve Karoq 2.0 TDI (Karoq / Kodiaq satırının bölünmesinden çıkan satır). Ateca ve Superb III satırlarına yeniden arama notu eklendi.
- `KAPSAM.md` ölçütlerine ve README'ye "aynı motoru paylaşan modeller" kuralı yazıldı.

### Bulunup kayıt dışı bırakılan konular

- **2019 düşük devir tork geri çağırması (ÖAMTC, Avusturya):** 1.5 l TSI EVO 110 kW (EU6AG) ve 180 A alternatör kombinasyonunda motor kontrol ünitesi yazılım güncellemesi; VW Arteon, Passat, Tiguan, Tiguan Allspace ve Touran (123 araç), Skoda Karoq, Kodiaq ve Superb (494 araç), Seat Ateca ve Tarraco (634 araç), 2019 model yılı. Kayıt alınmadı: tek site (ÖAMTC), Türkiye'deki araçların kapsamı doğrulanamadı ve "kronik arıza" değil tek seferlik bir yazılım kampanyası.
- **Motor kapağı geri çağırması (KBA 011703, 2020-2022 Arteon, Golf, Tiguan, T-Roc, Passat):** haberler motor tipini belirtmiyor; 1.5 TSI ile bağlantısı kurulamadı.
- **Seat / Skoda / VW enjeksiyon geri çağırması:** haberde "üç silindirli TSI" deniyor, yani 1.0 TSI; 1.5 TSI ile ilgisiz.
- **Triger zinciri:** Autodoc'un bir sayfası 1.5 TSI 150'de 80-120 bin km'de erken zincir aşınması diyor, başka bir sayfası geliştirilmiş zincir ve güvenilirlik diyor; çelişiyor, alınmadı. carwiki.de'deki liste (soğuk devir tutma, kalkışta ruckeln, EGR, turbo) arama özetinde kesik ve Türkçe kaynak yok, alınmadı.
- **Termostat / su pompası gövdesi kaçağı:** tek vwvortex başlığı; 1.4 TSI kayıtlarındaki aynı sorun 1.5'e taşınmadı.
- **Superb IV titreme:** Şikâyetvar'da 2025 model 1.5 TSI Hybrid'de kavrama, volan ve motor takozu değişimine rağmen süren, yaklaşık 14-15 bin TL ücretli titreme vakası var; iki sayfa ama tek site ve tek vaka, kayıt alınmadı.
- **Octavia 2020 rölanti titremesi (Otopark):** P0456 (buharlaşma emisyon) kodu ve MAF sensörü tartışılıyor; 1.5 TSI ile bağlantısı kurulamadı.
- **Golf 1.5 TSI ACT 150 titreme başlığı (DonanımHaber):** sahibi "2020 model" diyor, Golf 7.5 mi Golf 8 mi belli değil; bu yüzden Golf kaydına yazılmadı, Karoq titreşim kaydında "aynı motor" kaynağı olarak anıldı.

### Kanıtı sınırlı ayrıntılar

- **48V kök nedeni:** hiçbir kaynakta doğrulanmış kök neden yok. "Valeo alternatör", "üretici kalıcı çözüm üretmedi" ve "ABD ve Kanada'da 7 yıl ek alternatör garantisi" iddiaları kullanıcı yorumlarında geçiyor, doğrulanmadı ve kayıtlarda iddia olarak anıldı.
- **Seat Leon KL ve Skoda Superb IV 48V:** modele özgü deneyim Şikâyetvar'da; DonanımHaber kaynakları Leon ve Superb'e özgü değil, DSG'li eTSI ve Skoda e-TEC ailesini genel anlatıyor. Bu iki sorun yalnızca iki siteyle destekleniyor.
- **Formentor 48V:** yukarıda yazıldığı gibi tek Ekşi yorumu ve kardeş model kaynakları; `Orta` risk. Bağımsız bir Formentor şikâyeti bulunursa kayıt güçlenir.
- **Audi A3 8Y 48V:** Şikâyetvar başlıkları "35 TFSI Hybrid" ve "tahrik arızası" diyor; sistemin 48V olduğunu Ekşi Sözlük'teki iki yorum (A3 35 TFSI'nın Türkiye'de mild hibrit olduğu, kronik alternatör iddiası) söylüyor; alternatör kaynaklı olduğu servis sözüne dayanıyor.
- **Karoq titreşimi:** iki başlık (Otopark Karoq, DonanımHaber Golf), biri başka modele ait; servis çoğunlukla "motor karakteristiği" diyor, yanıtlayanlar farklı nedenler öne sürüyor. Kilometre kaynaklarda yok, aralık kaba tahmin; `detay` metninde söylendi.
- **Superb IV yağ eksiltmesi:** Şikâyetvar'ın Superb yağ sayfasındaki 5.000 km vakası ile iki ücretli servis ziyareti (yaklaşık 23 bin ve 44 bin TL) olan vakanın aynı araca mı ait olduğu arama özetinden anlaşılmıyor; `detay` metninde ayrı anlatıldı.
- **Yağ eksiltmesi kök nedeni:** segman, supap sapı keçesi, PCV, ince (0W-20) yağ ve düşük kaliteli yağ gibi teoriler forum yorumu; hiçbir resmî bülten bulunamadı. Yağ eksiltmesi modelde "normal" kabul edildiği sürece garanti kapsamı belirsiz.

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **Karoq yağ eksiltmesi:** ilk arama özeti "12.000 km'de yağ uyarısı, 2,6 litre ekleme" vakasını Karoq'a bağlamıştı; ikinci aramada bu sayfanın Kamiq (1.0 TSI) şikâyeti olduğu görüldü ve Karoq kaydından çıkarıldı.
- **Karoq titreşimi:** Ekşi Sözlük "aktif silindir yönetimi" başlığı yalnızca ACT'nin çalışmasını anlatıyor, titreşimin normal olup olmadığını söylemiyor; kayda kaynak olarak alınmadı.
- **Leon 48V:** Şikâyetvar'daki Cupra Leon vakası ışıklı logo ve ekran sorunu, 48V ile ilgisiz; kaynak listesinden çıkarıldı.
- **Superb yağ:** "farlarda buğulanma, viteste boşluk" cümlesi ikinci aramada doğrulanamadı, alınmadı. Passat için "19.500 km'de dört kez yağ uyarısı" cümlesi de ikinci aramada bulunamadı, alınmadı.
- **Ateca:** bir arama özeti Şikâyetvar'daki Ateca yağ uyarısı kaydının aracını 1.4 EcoTSI olarak yazıyordu, ancak kayıt 2024 model; doğrulanamadığı için plan notunda motor ataması yapılmadı.

### Dikkat edilecek sınırlar

- Doğrulama yine arama özetleriyle yapıldı; rakamlar, alıntılar ve model yılı için asıl sayfaya bakmak gerekir. Arama özetleri bazen farklı sayfaların cümlelerini karıştırdı (Karoq / Kamiq örneği); bu yüzden mümkün olan her yerde ayrı sorgularla çapraz kontrol yapıldı ve emin olunamayan yerlerde sayfa adı yerine site adı yazıldı.
- Şikâyet siteleri memnun olmayan kullanıcıların yazdığı örneklerdir; "kronik" ifadesi çoğunlukla sahiplerin ve forum yorumcularının kendi sözüdür, yaygınlık oranı verilemez.
- Kilometre aralıkları kaynakların yazdığı vakalardan çıkarıldı (48V için 1.000-80.000 km); Karoq titreşimi ve yağ eksiltmesi için kaba tahmin.

## 9. aşama: çok kullanılan araçlarda kaçırılanların taraması

Tarih: 2026-10-24

Dokuzuncu aşamanın sorusu şuydu: "Çok kullanılan araçlardan böyle kaçırdığın var mı? Ben hatırlattıkça ekliyorsun, çok kullanılan modeller olmasına rağmen." Dürüst cevap: **evet, vardı.** Her seferinde bir modeli sizin hatırlatmanız gerekmesinin nedeni, planın marka paylarından ve benim kendi model listemden kurulmuş olması, 7. aşamadaki sıralama karşılaştırmasının ise yalnızca model adı düzeyinde yapılmasıydı ("Clio var mı?" sorusuna evet denince hangi motor ve hangi nesil sorusu hiç sorulmadı). Bu aşamada plan, kayıtlar ve sıralama verileriyle nesil ve motor düzeyinde yeniden karşılaştırıldı.

### Kaçırmanın dört nedeni

1. **Birleşik plan satırları kısmi kapsamayı gizliyordu.** "1.4 TSI / 1.6 TDI" gibi bir satır yalnızca bir motor kayıtlıyken de ✓ görünüyordu. Sezgisel tarama 14 böyle satır buldu; hepsi motor bazında bölündü.
2. **Yıl aralığının yalnızca bir kısmı kayıtlıyken ✓ görünen satırlar.** Kayıtların satırın yıllarının yüzde 60'ından azını kapsadığı 6 satır bulundu (eksik nesiller).
3. **Planda hiç olmayan model, nesil ve motorlar:** Jetta (2013-2018), Honda Civic 1.6 i-DTEC, Renault Taliant, Fiat Egea Hybrid, Nissan Qashqai J12 1.3 DIG-T, Opel Mokka B, Kia Ceed CD, Renault Scenic 3 gibi.
4. **`–` satırları görüntüleyicide görünmüyordu.** Aranıp kanıt bulunamayan bir grup, kullanıcıya hiç bakılmamış gibi görünüyordu. Görüntüleyiciye "Arandı ama kayıt açılmayan gruplar" bölümü eklendi (aşağıda).

### Yöntem

- **Sıralama verileri** (arama sonuçlarından, tarihleri ve rakamları kaynaklar arasında farklı): TÜİK verisine dayandığı belirtilen, yaklaşık 2024 tarihli trafikteki araç sayısı listeleri (Tofaş Şahin / Doğan / Kartal 820.962; Corolla 628.137-689.206; Egea 510.676-668.866; Clio 535.718-613.830; Megane 538.121-600.797; Renault R12-Toros 553.164; Astra 448.849-454.378; Focus 398.781-422.838; Symbol 381.708; R9-Broadway 351.183), 2024 ODMD yeni araç satış sıralaması (Egea Sedan, Clio, Megane, Corolla, Togg T10X, Egea Cross, Chery Tiggo 8 Pro, Hyundai i20, Chery Tiggo 7 Pro, Nissan Qashqai) ve ikinci el segment sıralamaları (B: Clio, Polo, i20; C: Egea, Megane, Corolla; D: Passat; SUV: Qashqai, Duster, Tiguan, 3008). Cardata'nın 2017-2021 dönemi ikinci el listelerinde üst sıradaki otomobillerin hemen hepsi dizel (Egea 1.3 Multijet, Megane 1.5 dCi, Passat 1.6 TDI, Symbol 1.5 dCi, Clio 1.5 dCi, Sandero 1.5 dCi, Linea 1.3 Multijet, Accent Blue 1.6 CRDi, Polo 1.4 TDI, Focus 1.6 TDCi).
- **Programatik tarama:** birleşik motor etiketli ✓ satırlar eşleşen kayıtların motorlarıyla; satır yılları kayıt yıllarıyla; bilinen model adları plan ve veritabanıyla; yaklaşık 55 çok kullanılan modelin plan satırları nesil ve motor dökümüyle karşılaştırıldı.
- **Arama:** yaklaşık 45 grup için Şikâyetvar, DonanımHaber, Otopark ve Ekşi Sözlük'te model ve motor adıyla 1-4 sorgu yapıldı. `WebFetch` bu aşamada da kapalıydı, her şey arama özetleriyle yapıldı.

### Sonuç

| | 8. aşama sonu | 9. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 164 | 172 |
| Kronik sorun | 249 | 258 |
| Ayrıntısı olan sorun | 249 | 258 |
| Yıl kırılımı olan sorun | 60 | 61 |
| Marka | 29 | 29 |
| Sorunlara bağlı kaynak bağlantısı | 1443 | 1495 |
| Farklı kaynak sitesi | 78 | 79 |
| Yalnızca iki siteyle desteklenen sorun | 53 | 57 |
| Plan satırı | 308 | 355 |
| Plan durumu (✓ / – / ○) | 160 / 148 / 0 | 168 / 187 / 0 |
| Test | 36 | 37 |

Plana 47 yeni satır girdi: 8'i kayıtlandı (✓), 39'u araştırıldı ama kanıt eşiğini geçmedi (`–`). Aranan her grup ya ✓ ya `–`; bu aşamanın sonunda "sırada" (○) satır kalmadı.

### Eklenen kayıtlar

- **Volkswagen Jetta (2013-2018), 1.2 TSI / 1.4 TSI / 1.6 TDI, DQ200 DSG (1 sorun):** DSG mekatronik arızası (vites göstergesinde anahtar işareti, servis ışığı, vitese geçmeme). Risk `Orta`, 60.000-110.000 km; Şikâyetvar ve DonanımHaber.
- **Honda Civic (FC5, 2016-2021), 1.6 i-DTEC 120 (1 sorun):** DPF arıza lambası ve tıkanması (bazı sahiplerde 6.000 km gibi erken kilometrede; bayinin kullanıcı hatası dediği ve DPF değişimi için yaklaşık 15 bin TL istediği vaka). Risk `Orta`; DonanımHaber, Otopark, Şikâyetvar.
- **Renault Taliant (2021-), 1.0 TCe 90/100 (1 sorun):** turbo wastegate sesi ve arızası. Taliant'a özgü Şikâyetvar kayıtları var; teşhis anlatıları Clio 5 ve Sandero kayıtlarıyla ortak (aynı H4Dt motoru), bu `detay` metninde yazılı.
- **Fiat Egea Hybrid (2022-), 1.5 Hybrid 130 (1 sorun):** hibrit geçişlerinde sarsıntı ve start-stop hissi; risk `Düşük`.
- **Nissan Qashqai (J11 FL / J12, 2019-), 1.3 DIG-T 140/158 (2 sorun):** termostat arızası ve uyarısız soğutma suyu kaybı (`Yüksek`); 2021 sonrası 12V hafif hibrit lityum akü, akü yönetim sistemi ve start-stop arızası (`Orta`, 2021 sonrası için `Görülebilir` dönem kırılımı).
- **Opel Mokka (B, 2021-), 1.2 PureTech 100/130 (1 sorun):** yağ banyolu triger kayışının çatlaması ve dağılması (`Yüksek`). Mokka'ya özgü Şikâyetvar kaydı (2022 model, 47.000 km'de kayış arızası ve sözlü garanti reddi) ile ortak PureTech kaynakları.
- **Kia Ceed (CD, 2018-), T-GDI / 7DCT (1 sorun):** kalkışta silkeleme ve kavrama titremesi (`Orta`); yalnızca iki site.
- **Renault Scenic 3 / Grand Scenic (2009-2016), 1.5 dCi 110 EDC (1 sorun):** EDC şanzıman kontrol ünitesi (beyin) arızası, "vites kutusunu kontrol ettirin" uyarısı. Risk `Orta`, 100.000-170.000 km. Şikâyetvar (2012 model Scenic'te "ilk üretim beyinlerde kronik arıza" sözü, Grand Scenic'te beş aydır gelmeyen parça, iyi niyet garantisi reddi), Planète Renault ve Fiches-Auto'daki Scenic 3 anlatıları; kilometre bilgisi Fiches-Auto'dan (yaklaşık 98.000-167.000 km). Bu kayıtla 79. site (Planète Renault) kullanıma girdi.
- **Symbol adı:** Dacia "Sandero / Logan (2013-2020)" kayıtlarının adı "Sandero / Logan / Symbol (2013-2020)" yapıldı. Symbol III (2013-2020), Dacia Logan II'nin Türkiye'de Renault adıyla satılan ikizi (Motor1 ve Wikipedia'ya göre Bursa'da üretiliyor; lansmanda 0.9 TCe 90, dCi 75 ve dCi 90). Symbol'e özgü ayrı kaynak bulunamadı, bu `detay` metninde yazılı. Symbol 1.2 16V (D4F) `–` kaldı.
- Yeni 9 sorunun 6'sı `Orta`, 2'si `Yüksek`, 1'i `Düşük` risk; hepsinde `detay` var (neden 9, teşhis 3, çözüm 9, maliyet 5, önlem 7). 52 bağlantı eklendi, bir site girdi (Planète Renault).

### Plan değişiklikleri

- **Birleşik satırlar bölündü** (Mokka B, Ceed CD, Scenic 3, Passat, Karoq ve benzerleri); her motor alternatifi kendi durumunu gösteriyor.
- **Eşleşme etiketleri daraltıldı:** Qashqai J11 satırları J12 kaydına karışmasın diye ("Qashqai (J11, 2014"), Jetta eski ve yeni nesil satırları ayrıldı, Civic i-DTEC yalnızca FC5'e bağlandı, Egea Hybrid ayrı etiket aldı.
- **Peugeot 208 / 2008 / 308 / 3008 1.2 PureTech** satırında model parçası olarak yanlışlıkla "PureTech" yazılmıştı; düzeltildi (yeni test bu tür etiket hatalarını yakalıyor).
- **Yeni test:** `test_kayitli_satirda_her_eslesme_parcasi_bir_kayda_denk_gelir`. Bir satırın `eslesme` parçalarından her biri eşleşen kayıtlardan en az birinde bulunmalı; yoksa satır bölünmeli. Bu, kısmi kapsamayı ✓ ile gizleyen satırların tekrar oluşmasını engeller. Test sayısı 36'dan 37'ye çıktı.
- **Görüntüleyici:** sayfanın altına "Arandı ama kayıt açılmayan gruplar" bölümü eklendi. `data/kapsam.json` içindeki `–` satırlarını nedenleriyle gösteriyor; arama kutusu, marka, model yılı ve elektrikli filtreleri bu bölüme de uygulanıyor. Aranan bir araçta kayıt yoksa ama bu bölümde eşleşme varsa boş sonuç kutusu bunu söylüyor ve bölüme götürüyor. Bölüm isteğe bağlı bir eklemedir; istenmezse `viewer/sablon.html` içinden çıkarılabilir.
- README ve `KAPSAM.md` ölçütlerine birleşik satır kuralı ve çok kullanılan araç denetimi yazıldı.

### Araştırılıp eklenmeyen gruplar (39 yeni `–` satırı)

Nedenleri tek tek [KAPSAM.md](KAPSAM.md) içinde yazılıdır. Özet:

- **VW grubu (14):** Polo 6R / 6C 1.4 TDI, Polo AW 1.0 MPI, Polo Sedan, T-Roc 1.0 TSI, Tiguan AD1 1.4 TSI, T-Cross / Taigo 1.0 TSI, Touran, Passat CC, Amarok, Seat Leon 5F 1.4 TSI, Seat Toledo, Skoda Rapid 1.6 MPI, Skoda Octavia A7 (1.2 TSI / 1.6 MPI / 2.0 TDI), Skoda Superb II.
- **Hyundai ve Kia (8):** Tucson NX4 1.6 T-GDI, Tucson TL 1.7 CRDi, Accent Blue 2011-2015 1.6 CRDi, i20 (GB), Kia Sportage 1.7 CRDi, Sportage 1.6 T-GDI, Rio YB, Ceed CD 1.6 CRDi.
- **Diğer markalar (11):** Renault Laguna 3, Koleos, Scenic 3 1.6 16V, Fiat Linea 1.6 Multijet, Opel Meriva B, Zafira Tourer, Mokka B 1.5 BlueHDi, Ford Kuga 2 2.0 TDCi, C-Max / Grand C-Max, Honda Accord, Chery Tiggo 7 Pro / 8 Pro / Omoda 5.
- **Premium (5):** Mercedes A Serisi W177, B Serisi W246, GLC / GLA; BMW X3 / X5, 1 Serisi F40 / X1 F48.
- **Citroën (1):** C-Elysée 1.6 VTi.

Çok kullanılan modellere ait ve dikkat çekenler:

- **Polo 1.4 TDI (Cardata ikinci el listesinde):** DonanımHaber'de enjektör dönüş hortumu kaçağı ve marş sorunu (2016 model), Şikâyetvar'da turbonun dört kez yapıldığı vaka (2014 model) ve 95 bin km'de su eksiltme ile blok çatlağı (2016 model); her biri tek site. Otopark'taki Polo turbo başlığı turbo hortumu çatlağını anlatıyor ve motoru belirtmiyor.
- **Fiat Linea 1.6 Multijet:** Şikâyetvar'da en çok tekrarlanan şikâyet yolcu hava yastığı bölgesinde göğüs paneli çatlağı ve Blue&Me arızası; tek site, motor sorunu değil, kayıt alınmadı.
- **Chery Tiggo 8 Pro:** Şikâyetvar'da yağ soğutucusu arızası ve motor suyuna yağ karışması (iki ayrı vaka) ile Tiggo 8 Pro Max'te şanzıman vuruntusu anlatılıyor; DonanımHaber ve Ekşi Sözlük'te doğrulanmadı (Tiggo 7 Pro 7DCT için olumlu yorumlar var).
- **Hyundai Accent Blue 2011-2015 1.6 CRDi (Cardata listesinde):** tekil vakalar; şikâyetlerin çoğu 2015-2016 DCT'li sürümlere ait.
- **Skoda Rapid, Octavia A7, Tiguan AD1:** şikâyetler DSG ve 1.5 TSI kayıtlarında toplanıyor, listedeki motorlara özgü tekrar eden sorun çıkmadı.
- **Renault Laguna 3, Koleos, Superb II, Mercedes B ve GLC / GLA, BMW X3 / X5:** Türkçe şikâyet ya da forum kaydı çıkmadı; Fransızca ve Almanca sürücü yorumları, Araclo sayfaları ve yabancı rehberler var, deneyim türünde ikinci bir site yok.

### Kanıtı sınırlı ayrıntılar

- **Jetta DSG:** kaynaklar DQ200'ün kök nedenini doğrulamıyor; ABD'ye ait bir NHTSA atfı (kablo çerçevesi korozyonu) DonanımHaber'de geçiyor, Türkiye'deki araçlara uygulanıp uygulanmadığı doğrulanamadı. Yalnızca iki site (Şikâyetvar, DonanımHaber).
- **Taliant turbo:** Taliant'a özgü kayıtlar Şikâyetvar'da; teşhis ve çözüm anlatıları Clio 5 ile ortak (H4Dt). Kayıt bu yüzden doğrudan kanıtı sınırlı sayılır.
- **Qashqai 1.3 DIG-T:** iki sorun yalnızca iki siteyle destekleniyor; termostat vakaları tek tek.
- **Ceed CD 7DCT:** yalnızca iki site; Şikâyetvar'da 2023 model Ceed'de servisin şanzıman sorunu dediği ama arıza kaydı bulunmadığı için değişim yapılmayan vaka, başka bir servisin sorunu başka nedene bağladığı yazılıyor.
- **Egea Hybrid:** sarsıntı ve start-stop hissi kullanıcı yorumu; üretici açıklaması bulunmadı. Risk bu yüzden `Düşük`.
- **Scenic 3 EDC:** kilometre aralığı Fiches-Auto'daki tekil sürücü yorumlarından (yaklaşık 98.000, 120.000, 126.000 ve 167.000 km); aynı derlemede 118.000-130.000 km'de sorun yaşamayan sahipler de var. Fiches-Auto sayfalarının hangisinde hangi kilometrenin yazdığı arama özetinden ayrılamadı, bu yüzden bağlantılar site düzeyinde verildi.
- **Mokka B triger:** bazı kullanıcıların "2022 sonu sonrası triger güçlendirildi" iddiası resmî bir kaynakla doğrulanmadı; kayıtta iddia olarak anıldı.

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **Symbol:** Symbol III'ün Logan II'nin ikizi olduğu önce varsayımdı; arama (Motor1, Wikipedia) ile doğrulanana kadar kayıtlara yazılmadı. Wikipedia ve Motor1'in lansman listesinde Symbol III için 1.2 motoru yok.
- **Polo 1.4 TDI:** ilk bakışta turbo kanıtı gibi görünen anlatılar 1.6 TDI'a ya da motoru belirtilmemiş araçlara aitti; `–` kaldı.
- **`–` notlarının doğrulanması:** notlardaki site ve model atamaları kayıtlı arama özetleriyle tek tek karşılaştırıldı; özetin desteklemediği ayrıntılar notlardan çıkarıldı ya da siteden bağımsız yazıldı. Örnekler: Tiguan'da piston kırılması ve titreme anlatılarının "Şikâyetvar'da iki vaka" olduğu özetten çıkmıyordu (çoğunun 2010-2013 modellerine ait olduğu yazıldı); Touran için DonanımHaber'deki "11 yıldır çözülmeyen" başlığının içeriği görülmediği için anılmadı; Kuga'daki 2011 model aracın Kuga 1 olduğu belirtildi; Leon'daki 2020 model ACT valf hortumu vakasının motoru belli olmadığı için 1.4 TSI'a bağlanmadı; Rapid notundaki "1.2 TSI'a ait" ifadesi özette yoktu, "DSG'li araçlara ait" diye düzeltildi.
- **Scenic 3 EDC:** Ekşi Sözlük'teki "Renault araçlarda kronik EDC sorunu" başlığı modele özgü olmadığı için kaynak olarak alınmadı; yerine modele özgü üç site kullanıldı.
- **8. aşama tablosu:** marka sayısı 28 yazılmıştı; Cupra eklendiği için 29 olmalıydı, düzeltildi.

### Dikkat edilecek sınırlar

- Doğrulama yine arama özetleriyle yapıldı; rakamlar, alıntılar ve model yılı için asıl sayfaya bakmak gerekir.
- Sıralama verileri ilan sayısı değil, TÜİK türevi trafikteki araç sayıları ve satış sıralamaları; kaynaklar arasında rakamlar tutarlı değil. Motor düzeyinde sıralama yalnızca Cardata'nın ikinci el listelerinde var. Sahibinden ve arabam.com'un model-motor ilan sayıları okunamadı.
- **2011 öncesi model yılları planda yok.** Trafikteki en kalabalık otomobiller hâlâ Tofaş Şahin / Doğan / Kartal (820.962), Renault R12-Toros (553.164) ve R9-Broadway (351.183) gibi 2011 öncesi modeller; "10-15 yıl" zaman penceresi kuralıyla dışarıdalar. İstenirse pencere genişletilebilir.
- **Hibritler kapsam dışı** (Toyota Corolla / C-HR hibrit, Honda City hibrit); 48V hafif hibritler kapsamda.
- **Tek sorguyla bakılan gruplar:** Sportage 1.6 T-GDI, Seat Toledo, BMW 1 F40 / X1 F48, Citroën C-Elysée 1.6 VTi, Mokka B 1.5 BlueHDi ve Ceed CD 1.6 CRDi. Bunların `–` olması "kanıt yok" değil "tek sorguda çıkmadı" demektir; nota yazıldı.
- Bu denetim "çok kullanılan hiçbir araç eksik değil" garantisi vermez: bulunmayan bir grup artık ya kayıtta ya da görüntüleyicideki `–` bölümünde görünür; ikisinde de yoksa hiç aranmamıştır.

## 10. aşama: motor ve şanzıman aileleri ve model kataloğu

Tarih: 2026-10-24

Bu aşama iki mesajla başladı. Birincisi: "Biz şu mantıkla mı ilerliyoruz; aslında motor kodlarının kroniklerini bulup o kronikleri kullanan modellere yazsak bundan sonrasında daha az efor olmaz mı? Ya da mesela Jetta'nın diğer modele özgü kroniklerini de yazıyor muyuz?" İkincisi: "Ben listeye her baktığımda çok eksik görüyorum. Mesela Q3, Q5 gibi modeller bile yok, X3, X5." Dürüst cevaplar: (1) evet, aynı motoru ya da şanzımanı paylaşan modeller için sorunu her modelde baştan aramak hem verimsizdi hem de aynı sorunun on yerde on farklı biçimde yazılmasına yol açıyordu (DQ200 DSG sorunu 12 modelde 17 kez, PureTech triger kayışı 6, H4Dt turbo 5, 1.5 TSI 10 modelde); (2) hayır, Jetta'nın motor ve şanzıman dışındaki modele özgü kronikleri (iç mekân, elektronik, gövde) toplanmıyordu: veritabanının yaklaşık yüzde 88'i tahrik organları (258 sorundan yalnızca 8'i bunun dışında). Bu ikinci konu hâlâ açık bir kapsam sorusudur (aşağıda). Q3, Q5, X3 ve X5 ise ya hiç planda yoktu ya da yalnızca `–` ile sınırlıydı.

### Ne yapıldı

1. **Aile katmanı kuruldu.** `data/araclar.json` köküne `aileler` eklendi; bir motor ya da şanzıman sorunu bir kez aileye yazılıyor, aynı motoru kullanan kayıtlar aileye bağlanıyor ([README](README.md#ortak-motor-ve-şanzıman-aileleri-aileler)). Modele özgü bildirimi olan kayıtlar kendi sorununu `aile_sorunu` ile aile sorununa bağlıyor (✓, görüntüleyicide "Aile: ... · bu modelde de bildirilmiş"); modele özgü bildirimi olmayan kayıtlar yalnızca aileli kayıt olarak açılıyor (**◐**, görüntüleyicide kesik çerçeveli "Ortak aile" etiketi ve kayıt başında açıklama). Hiçbir bağ otomatik kurulmadı; her aile bağı tek tek yazıldı.
2. **Doğrulayıcı, şema ve testler:** aile kimliği benzersiz ve biçimli olmalı, her aile kullanılmalı, `aile_sorunu` var olan bir aile sorununa ve kaydın bağlı olduğu aileye işaret etmeli, bir kaydın en az bir sorunu ya da en az bir ailesi olmalı. Test sayısı 37'den 60'a çıktı (aile kuralları, şema ve yeni üretici davranışları).
3. **Üreticiler:** `KAPSAM.md` artık ◐ durumunu, `KAYNAKLAR.md` aile sorunlarının kaynaklarını sayıyor. Görüntüleyici aile etiketlerini, "arandı" ve "sırada" ayrımını ve sayfanın üstünden "kayıt açılmayan gruplar" bölümüne kısayolu gösteriyor. Kısa model kodları ("Q3", "X5") artık kelime başında aranıyor; önceden "Q3" araması "DQ381" içindeki "q3"ü de bulup Kodiaq ve Tiguan kayıtlarını getiriyordu. Harf + tek rakamlı kodların ("X2", "S6") ardından rakam da gelmiyor; "X2" araması Mercedes "X243" / "X253" kodlarını getirmiyor.
4. **Aileler kuruldu ve kardeş modeller eklendi** (aşağıda).
5. **Model kataloğu:** Türkiye ikinci el pazarında yaygın olup planda hiç yer almayan 114 model ve motor grubu "sırada" (○) olarak plana eklendi; bunların bir kısmı aynı aşamada araştırılıp ◐ ya da `–` oldu, 88'i sırada kaldı.
6. **Aile tasarımı kanıt kapsamına göre daraltıldı.** İlk taslakta VAG 1.6 TDI için tek aile vardı (enjektör + EGR / DPF) ve EA288 motorlu modellere de EA189'a özgü enjektör sorunu yazılıyordu; EA189 enjektörü ile 1.6 TDI EGR / DPF ayrıldı. Aynı şekilde VAG 1.2 ve 1.4 TSI (EA111 / EA211) ve EA111 1.2'ye özgü yağ tüketimi ayrı ailelere bölündü. Kural: aile, sorunun kanıtlandığı motor sürümünü aşmıyor.

### Sonuç

| | 9. aşama sonu | 10. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 172 | 328 |
| – bunlardan kayda özgü kaynaklı sorunu olan (✓) | 172 | 172 |
| – bunlardan yalnızca aile kaynaklı (◐) | 0 | 156 |
| Kayda özgü kronik sorun | 258 | 258 |
| Motor / şanzıman ailesi | 0 | 48 |
| Ortak (aile) sorunu | 0 | 82 |
| Aileye bağlı kayıt | 0 | 285 |
| Görüntüleyicide gösterilen sorun (kayda özgü + ortak) | 258 | 712 |
| Marka | 29 | 30 (Alfa Romeo) |
| Farklı kaynak sitesi | 79 | 80 (Sözcü) |
| Kayda özgü sorunlara bağlı kaynak bağlantısı | 1495 | 1495 |
| Aile sorunlarına bağlı kaynak bağlantısı | 0 | 654 |
| Plan satırı | 355 | 575 |
| Plan durumu (✓ / ◐ / – / ○) | 168 / 0 / 187 / 0 | 168 / 142 / 177 / 88 |
| Kademe 1 satırı (işlenen) | 109 (109) | 120 (120) |
| Test | 37 | 60 |

Kayda özgü sorun sayısı değişmedi: bu aşamada yeni bir modele özgü sorun eklenmedi, çünkü yapılan aramalar (aşağıda) iki bağımsız site ve kilometre bilgisi eşiğini geçen yeni bir modele özgü sorun çıkarmadı. Artan şey kapsam: 156 modelin kaydı artık aynı motor ya da şanzımanı kullanan diğer modellerin kaynaklarıyla görünür. Faz 9 sonundaki 187 `–` satırının 22'si doğrudan ◐ oldu, 58'i bölündü ya da yeniden adlandırıldı (parçaları ◐ ya da `–` oldu), 107'si olduğu gibi kaldı.

### Aileler

48 aile (motor 34, şanzıman 10, sistem 4) ve bağlı kayıt sayıları:

| Aile | Tür | Ortak sorun | Bağlı kayıt | Yalnızca aileli (◐) |
| --- | --- | ---: | ---: | ---: |
| Audi Multitronic (0AW) sürekli değişken şanzıman | şanzıman | 1 | 3 | 1 |
| BMW B38 1.5 üç silindir turbo benzin | motor | 1 | 7 | 6 |
| BMW N13 1.6 turbo benzin (116i / 118i / 316i) | motor | 7 | 2 | 1 |
| BMW N20 2.0 turbo benzin | motor | 3 | 5 | 4 |
| BMW N47 2.0 dizel | motor | 2 | 6 | 3 |
| BMW xDrive transfer kutusu (ATC) | sistem | 1 | 8 | 8 |
| Fiat / Jeep / Alfa 1.6 Multijet II - JTDm (common rail dizel) | motor | 2 | 5 | 4 |
| Fiat / Opel 1.3 Multijet - CDTI (common rail dizel, zincirli) | motor | 5 | 11 | 3 |
| Fiat Dualogic tek kavramalı robotize şanzıman | şanzıman | 2 | 3 | 2 |
| Fiat Grubu 6 ileri kuru çift kavramalı DCT (DDCT) | şanzıman | 1 | 3 | 2 |
| Ford / Volvo DPS6 Powershift (6 ileri kuru çift kavramalı) | şanzıman | 2 | 7 | 4 |
| Ford 1.0 EcoBoost (3 silindir turbo benzin) | motor | 2 | 6 | 4 |
| Ford 1.5 EcoBoost (4 silindir turbo benzin) | motor | 1 | 3 | 2 |
| Honda 1.5 VTEC Turbo (L15B7 / L15BE) | motor | 1 | 2 | 1 |
| Honda 1.6 i-DTEC (N16A common rail dizel) | motor | 2 | 4 | 2 |
| Hyundai / Kia 7DCT (7 ileri kuru çift kavramalı) | şanzıman | 1 | 20 | 12 |
| Hyundai / Kia Gamma 1.6 GDI (direkt enjeksiyonlu benzin) | motor | 1 | 5 | 3 |
| Hyundai / Kia U2 1.4 - 1.6 - 1.7 CRDi (common rail dizel) | motor | 2 | 14 | 7 |
| Mercedes 7G-Tronic (722.9) otomatik şanzıman | şanzıman | 1 | 4 | 2 |
| Mercedes OM651 2.1 CDI (2.143 cc dizel, piezo enjektörlü) | motor | 1 | 10 | 8 |
| Opel 1.6 CDTI (B16DTH / B16DTL) | motor | 2 | 6 | 3 |
| Opel 1.6 Ecotec (A16XER) atmosferik benzin | motor | 1 | 3 | 2 |
| Opel A14NET 1.4 Turbo (benzin) | motor | 1 | 5 | 4 |
| PSA / BMW / Mini 1.6 THP - N14 - N18 (EP6 turbo benzin) | motor | 3 | 3 | 1 |
| PSA / Ford 1.6 HDi - e-HDi - BlueHDi - TDCi (DV6) | motor | 3 | 15 | 9 |
| PSA / Opel / Ford 1.5 BlueHDi - EcoBlue (DV5) | motor | 2 | 8 | 4 |
| PSA / Opel PureTech 1.2 (EB2, 3 silindir) | motor | 2 | 8 | 1 |
| PSA BlueHDi AdBlue (SCR) sistemi | sistem | 1 | 10 | 4 |
| PSA MCP / ETG6 / Auto6R tek kavramalı robotize şanzıman | şanzıman | 1 | 2 | 1 |
| Renault / Dacia EDC çift kavramalı şanzıman (6 ve 7 ileri) | şanzıman | 2 | 12 | 4 |
| Renault / Nissan 1.2 TCe - DIG-T (H5Ft / HRA2DDT) | motor | 2 | 4 | 1 |
| Renault / Nissan H4Bt - H4Dt 0.9 / 1.0 TCe (3 silindir turbo benzin) | motor | 1 | 7 | 2 |
| Renault K9K 1.5 dCi (common rail dizel) | motor | 2 | 23 | 11 |
| Subaru FB20 2.0 boxer (atmosferik benzin) | motor | 1 | 3 | 2 |
| Toyota 1ND-TV 1.4 D-4D (common rail dizel) | motor | 2 | 4 | 2 |
| Toyota 1NR-FE 1.33 Dual VVT-i (benzin) | motor | 1 | 3 | 2 |
| Toyota M15A-FKS 1.5 Dynamic Force (benzin) | motor | 1 | 2 | 1 |
| VAG 1.5 TSI evo (EA211 evo, ACT / eTSI) | motor | 2 | 20 | 10 |
| VAG 1.6 TDI EGR valfi ve DPF (EA189 / EA288) | sistem | 1 | 18 | 8 |
| VAG 48V hafif hibrit sistem (eTSI / e-TEC / MHEV) | sistem | 1 | 7 | 1 |
| VAG DQ200 7 ileri kuru kavramalı DSG (S tronic) | şanzıman | 2 | 23 | 9 |
| VAG DQ381 7 ileri ıslak kavramalı DSG | şanzıman | 1 | 2 | 1 |
| VAG EA111 1.2 / 1.4 TSI-TFSI (zincirli, 2008-2015) | motor | 1 | 12 | 7 |
| VAG EA111 1.2 TSI (CBZA / CBZB) | motor | 1 | 4 | 2 |
| VAG EA189 1.6 TDI common rail (CAYC / CAYB / CAYE) | motor | 1 | 15 | 5 |
| VAG EA211 1.2 TSI (CJZA / CJZB) | motor | 1 | 5 | 3 |
| VAG EA211 1.4 TSI-TFSI (125 / 150 PS, ACT) | motor | 1 | 10 | 7 |
| VAG EA888 (Gen1 / Gen2) 1.8 / 2.0 TFSI-TSI | motor | 3 | 6 | 4 |

### Eklenen kardeş model kayıtları (◐, 156)

Bu kayıtlar yalnızca ailelerden beslenir: modele özgü bildirim aranmadı ya da bulunamadı, plan notunda yazılı. Listeler marka bazında:

- **Skoda (15):** Fabia 5J ×2 ve NJ, Octavia A5 FL ×2 ve A7 (1.2 TSI), Superb II ×3 ve III ×3, Kodiaq ×2, Kamiq / Scala 1.5 TSI.
- **Volkswagen (14):** Golf 6 (1.2 TSI), Golf 7.5 (1.5 TSI), Passat B7 / B8 (1.4 TSI) ve B9 (1.5 eTSI), Tiguan AD1 (1.4 TSI), Touran 1T3 ×2 ve 5T ×2, Caddy SA, Arteon, T-Cross / Taigo ve T-Roc (1.0 TSI DSG).
- **Opel (13):** Mokka 1.4 Turbo / 1.6 CDTI / 1.6 benzinli, Insignia A 1.4 Turbo / 1.6 benzinli, Insignia B 1.6 CDTI, Meriva B 1.3 CDTI / 1.4 Turbo, Zafira Tourer 1.4 Turbo / 1.6 CDTI, Combo D, Crossland ve Mokka B 1.5 BlueHDi.
- **BMW (17):** X1 E84 ×2 ve F48, X2 F39 sDrive18i, X3 F25 ×4 (N47, B47, N20, N57), X5 E70 ve F15, 5 Serisi F10 520i / 528i, 3 Serisi F30 316i ve 318i, 4 Serisi F32 / F36 ×3 (420i N20, 420d N47, 418i B38), 2 Serisi F22 / F45 218i (B38).
- **Mercedes-Benz (12):** A Serisi W176 (A200 / A220 CDI) ve W177 (A180 d), B Serisi ×2, GLA ×2, GLC, GLK, C Serisi W205 (C220d), Citan, Vito / V-Class, Sprinter.
- **Audi (11):** Q2 ×3, Q3 8U ×2 ve F3, A1 ×2, A3 8V 1.2 TFSI, A5 8T, A6 C7 2.0 TDI.
- **Ford (11):** C-Max ×3, B-Max ×2, Transit Connect, Courier, EcoSport 1.5 Powershift, Focus 3 ve 4 (1.5 EcoBoost), Puma.
- **Hyundai (9), Kia (6):** i30 GD / PD, Kona ×2, Elantra AD, Tucson TL 1.7, ix35 1.6 GDI, Accent Blue 1.6 GDI; Ceed CD, Sportage QL ×2, Stonic ×2, Rio YB.
- **Renault (7), Nissan (4), Dacia (1):** Kangoo, Laguna 3, Scenic 4, Captur 2 ×2, Arkana, Kadjar 1.2 TCe; Note, Qashqai J10, Juke 1.5 dCi, Micra K14; Lodgy / Dokker.
- **Seat (7):** Leon 5F 1.4 TSI ve FL 1.5 TSI, Ibiza 6F, Arona, Ateca, Toledo ×2.
- **Peugeot (5), Citroën (5):** 207, 308 T7, 508 1.6 THP, Partner, Rifter / Partner; C3, C4, C4 (2020-), Berlingo ×2.
- **Toyota (5), Honda (3), Fiat (4), Jeep (2), Subaru (2), Alfa Romeo (1), Mini (1), Volvo (1):** Yaris XP130 ×2 ve XP210, Corolla E170, Auris E180; Civic FB7, HR-V, CR-V RW; Panda, 500 Dualogic, 500L, 500X; Renegade, Compass; Forester, Impreza; Giulietta; Cooper F56; V60 D2.

Sizin sorduğunuz modeller: **Q3** (8U 2.0 TFSI ve 1.4 TFSI, F3 35 TFSI), **X1 / X3 / X5** (X1 E84 ×2 ve F48, X3 F25 ×4, X5 E70 ve F15) ve **Q2 / A1 / A5 / A6 / Touran / Superb II-III / Kodiaq** artık kayıtlı. **Q5** için yalnızca 8R 2.0 TFSI (yağ tüketimi) kayıtlı; Q5 2.0 TDI (8R) ve Q5 FY araştırıldı, `–` kaldı. BMW **G20 / G30 / X3 G01 / X5 G05** (2017 sonrası nesiller) için dördü de araştırıldı ve `–`; BMW **4 Serisi** ve **2 Serisi (F22 / F45)** ile **X2** benzinli sürümleriyle (420i, 420d, 418i, 218i, sDrive18i) ◐ olarak kayıtlı.

### Araştırılıp eklenmeyen gruplar (bu aşamadaki aramalar)

Bu aşamada Şikâyetvar, DonanımHaber, Otopark ve Ekşi Sözlük'te şu gruplar arandı ve iki bağımsız site ve kilometre bilgisi eşiğini geçen bir sorun çıkmadığı için `–` olarak plana notlarıyla işlendi (ayrıntı [KAPSAM.md](KAPSAM.md) içinde):

- **VAG 2.0 TDI (EA189 / EA288) üçüncü kez arandı:** yağ pompası / balans mili, Q5 2.0 TDI enjektör-turbo-DPF ve CBAB / CFFB / CAGA motor kodlarıyla sorgular yine yalnızca genel anlatılar, PD motorlara (B6) ve eski modellere ait enjektör iddiaları ve tekil Amarok vakası döndürdü. Aile kurulmadı; Passat B7 / B8, Tiguan 5N, Caddy, Transporter, Karoq, Octavia A7 ve Superb II-III 2.0 TDI satırları `–` kaldı.
- **BMW 3 Serisi G20, 5 Serisi G30, X3 G01:** Şikâyetvar'da tekil kayıtlar (G20'de 45.000 km'de su pompası uyarısı, 60 bin km'de park freni, 74.000 km'de diferansiyel uğultusu; G30'da ambiyans aydınlatma, kapı kolu içi erimesi, sunroof perdesi; G01'de acil çağrı pili ve geri görüş kamerası). DonanımHaber ve Ekşi Sözlük'te B48 / B47'nin daha az sorunlu sayıldığı yorumlar var.
- **Audi Q5 (8R) 2.0 TDI, Q5 FY 2.0 TDI, A3 8V 2.0 TDI / 1.8 TFSI:** kronik iddialar kaynaksız ve aynı başlıklardaki kullanıcılarca reddediliyor ya da S tronic şanzımana ve eski modellere ait.
- **Volvo XC60 (2008-2017 ve 2017-), S60 II / V60 (D3 / D4 / D5, T4 / T5):** tekil vakalar (2011 XC60 D5'te şanzıman sektirmesi, 2016 D4'te 300.000 km'de blok çatlağı, 2020 XC60'ta 70.000 km'de turbo); 1.6 T4 EcoBoost için hararet ve su eksilmesi iddiaları Şikâyetvar ve DonanımHaber'de geçiyor ama kilometre bilgisi yok.
- **BMW X5 G05, 5 Serisi F10 520d (B47), 4 Serisi 420d / 420i (B47 / B48), 2 Serisi 216d / 218d:** G05'e özgü kayıt çıkmadı (SOS sistemi, motor kodu belirtilmemiş bir 2018 model X5'te yaklaşık 141.000 km'de motor değişimi anlatısı); B47 için N47 zincir tartışmaları, ZF 8 ileri şanzımanı sorunsuz bulan yorumlar ve B47'yi düzeltilmiş N47 olarak anan tekil bir görüş çıktı; 4 Serisi için ön cam contası, iç kapı kolu ve soğutma sıvısı gibi tekil konular, 216d (B37) için çoğunlukla olumlu yorumlar çıktı.
- **Volvo XC90 (2002-2014 ve 2015-), V40, S90 / V90, XC40:** XC90 2.4 D5 için DonanımHaber'de bir inceleme başlığı var ama kilometre bilgili, ikinci siteyle doğrulanmış enjektör ya da şanzıman sorunu çıkmadı; V40'ta T3 Geartronic için olumlu yorumlar ve tekil turbo / hararet vakaları; S90'da 2017 model D5'te piston deformasyonu nedeniyle motor değişimi (tüketici hakem heyeti ve Yargıtay'ın Mart 2025'te araç değişimi kararını onaması; konuda bir yorumcu sorunu kronik bulmuyor) ve 2021 model B5'te termostat arızasından motor indirmeye varan tekil vaka; XC40'ta 2020 model T3'te 5 yılda 6 aks değişimi, tekrarlayan SRS arızası ve T3 yağ eksilmesi tartışması (tek site ya da tartışmalı).
- **Hafif ticari:** Ford Transit (enjektör, turbo, volan, 2017 model 2.2'de 150 bin km'de piston delinmesi), Peugeot Boxer / Citroën Jumper (enjektör şakırtısı, debriyaj hidroliği), Peugeot Expert / Citroën Jumpy, VW Crafter, Fiat Ducato (AdBlue / NOx, enjektör, debriyaj hidrolik hortumu; debriyaj iki sitede geçiyor ama kilometre bilgisi yok), Opel Vivaro.
- **Diğer:** Toyota Verso (1.6 D-4D krank kasnağı kırılması iki kullanıcıda, kilometre yok), Suzuki Swift, VW Sharan 7N, Ford S-Max / Galaxy, Opel Insignia B 1.5 Turbo.

### Kanıtı sınırlı kayıtlar

- **Tüm ◐ kayıtlar** doğrudan kanıtı sınırlıdır: gösterilen sorunlar başka modellerin kaynaklarına dayanır. Kayıt başındaki açıklama ve plan notu bunu söylüyor.
- **Hangi modelin hangi motor ve şanzımanla (hangi yıllarda, Türkiye'de) satıldığı bilgisi kaynaklarla tek tek doğrulanmadı;** kendi bilgime dayanıyor ve yalnızca ◐ kayıtlarda değil, tüm aile bağlarında geçerli (README ve görüntüleyici bunu yazıyor). Hatalı bir eşleşme görürseniz bildirin ya da `aileler` bağını düzeltin.
- **Aile sorunlarının kaynağı çoğu zaman tek bir ya da iki modelin kayıtlarından geliyor:** ör. Mercedes OM651 piezo enjektörü C W204 ve E W212'den, 7G-Tronic iletken plaka yalnızca C W204'ten, Hyundai-Kia 7DCT yedi kayıttan (üç dizel, dört benzinli).
- **Yalnızca iki siteyle desteklenen aile sorunları** KAYNAKLAR.md içinde sayılıyor; doğrulayıcı toplam 63 yalnızca-iki-siteli sorun bildiriyor (kayda özgü ve ortak).

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **Suzuki SX4 S-Cross / Vitara 1.6 DDiS = PSA DV6:** hafızadan yazılmıştı; arama motoru üreticiyi doğrulayamadı (yalnızca D16AA kodu ve teknik veriler çıktı, üretici adı yok). Kayıt ve aile bağı kaldırıldı, satır `–` olarak geri döndü.
- **Hyundai ix35 1.7 CRDi:** plan notunda Türkiye'de neredeyse hiç satılmadığı yazdığı için kayıt açılmadı.
- **VAG aile taslağı:** yukarıda (EA189 enjektörü ile EA288'e yazılması, 1.2 / 1.4 TSI karışması) düzeltildi.
- **Plan satırları:** Leon 5F 1.4 TSI satırının yılı "2005-2020" idi, "2012-2020" yapıldı. Passat B9 için yinelenen satır birleştirildi; Opel Mokka için çakışan üç `–` satırı düzenlendi; "Fabia / Superb" birleşik `–` satırı silindi; Superb II eşleşme parçası "Superb (II" Superb III'ü de yakalıyordu, "Superb (II," yapıldı; Caddy, Kamiq / Scala, Ibiza, EcoSport, CR-V, Micra, Tucson TL FL, Ceed ✓ satırlarının eşleşme parçaları yeni kardeş kayıtları yakalamasın diye daraltıldı. Sprinter motor etiketi "211-319" iken V6 sürümleri OM651 değildi, "209-316" yapıldı; Peugeot "Partner / Rifter (2008-2018)" etiketi "Partner (2008-2018)" yapıldı.
- **Birleşik `–` satırlarının bölünmesi:** Fabia, Superb III, Passat B7 / B8, A3 8V, Ibiza, Q3, A1, Octavia A7, Superb II, Touran, Mokka, Zafira Tourer, Insignia A, Meriva B, Note, Qashqai J10, Laguna 3, B Serisi, GLA / GLC, C Serisi W205, i30, Elantra, Kona, Rio, Subaru ve benzerleri, böylece ◐ olan parça `–` olan parçayı gizlemiyor.

### Dikkat edilecek sınırlar

- Doğrulama yine arama özetleriyle yapıldı; `WebFetch` kapalıydı. Özetler, sayfaları yorumlayan bir araçtan geliyor; rakam ve alıntılar için asıl sayfaya bakmak gerekir.
- **2017 sonrası araçlar için Türkçe kaynak büyük ölçüde Şikâyetvar'dan ibaret;** ikinci bağımsız site çıkmadığı için G20 / G30 / X3 G01 / X5 G05 / XC60 II / S90 / V90 / XC40 / Q5 FY gibi yeni nesiller `–` kalıyor. Bu "sorun yok" demek değildir.
- **Kapsam soruları açık:** (1) 2011 öncesi model yılı penceresi hâlâ dışarıda (Tofaş Şahin / Doğan / Kartal, Renault R12-Toros, R9-Broadway). (2) Motor ve şanzıman dışı modele özgü kronikler (iç mekân, elektronik, gövde; ör. BMW kapı kolu erimesi, G30 ambiyans aydınlatma, Jetta'nın tahrik dışı sorunları) bu aşamada toplanmıyordu; [11. aşamada](#11-aşama-model-geneli-sorunlar-motordan-bağımsız) model geneli kayıtlarla ele alındı. (3) Hibrit ve plug-in hibritler kapsam dışı.
- **88 satır "sırada":** BMW 2 Serisi F44, X2 (dizel), X4, X6, 7 Serisi; Mercedes GLE, CLA C118, CLS, S Serisi, Viano; Volvo S80 / V70 / XC70; Land Rover, Jeep, Alfa Romeo, Porsche modelleri; Audi A3 8Y, A5 F5, A6 C8, A7, Q7, A1 GB, TT; VW Touareg, Scirocco, Beetle, up!; Seat Altea, Alhambra, Mii; Opel Zafira B, Astra L, Adam / Karl, Antara; Peugeot 5008 I, 107 / 108; Citroën C5, Nemo, DS3 / DS4; Fiat Bravo, Scudo, Fullback; Renault Twingo, Espace, Austral; Nissan Pulsar, X-Trail T31, Murano; Mitsubishi, Suzuki, Subaru, Hyundai, Kia, MG, Ssangyong, Smart modellerinin bir kısmı. Hepsi görüntüleyicinin "Kayıt açılmayan gruplar" bölümünde "Sırada" etiketiyle görünür.

## 11. aşama: model geneli sorunlar (motordan bağımsız)

Tarih: 2026-10-25

Bu aşamanın çıkış noktası şu isteğiniz: "listemizdeki araçların modele bağlı problemlerini de araştırıp yazsak; mesela X modelinde sunroof su alma problemi gibi". Önceki aşamalar yalnızca motor ve şanzıman sorunlarını topluyordu. Cam tavandan su alma, kapı kilidi, boya atması, multimedya donması, direksiyon ve EPB arızası gibi **kasaya (nesle) bağlı** sorunlar motor sürümünden bağımsız olduğu için hiçbir motor kaydına doğru oturmuyordu.

| | 10. aşama sonu | 11. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 328 | 381 (328 motor + 53 model geneli) |
| Kayda özgü kronik sorun | 258 | 320 (62'si model geneli) |
| Farklı kaynak sitesi | 80 | 84 |
| Yalnızca iki siteyle desteklenen sorun | 63 | 114 |
| Ayrıntısı (`detay`) olan sorun | 340 | 402 |
| Plan satırı | 575 | 675 |
| Kanıtı yetersiz `–` satırı | 177 | 214 (37'si model geneli) |
| Sırada `○` satırı | 88 | 98 |

### Ne yapıldı

- **Yeni kayıt türü: model geneli kayıt.** `motor` alanı sabit olarak `Tüm motorlar (model geneli)` yazılır; kayıt bir modelin (neslin) motordan bağımsız sorunlarını toplar. Aynı kaynak kuralı geçerlidir (en az iki farklı site, en az biri deneyim ya da resmî türünde). Kayıt bir aileye bağlanamaz ve en az bir sorunu olmalıdır. **Kilometre aralığı bu kayıtlarda isteğe bağlıdır:** sızdırmazlık, boya, iç mekân ve elektronik sorunlarının kaynakları çoğunlukla kilometre yazmaz; yazmıyorsa aralık uydurulmadı (62 sorunun 62'sinde kilometre bilgisi yok).
- **Şema, doğrulayıcı, testler:** `schema/araclar.schema.json` ve `scripts/dogrula.py` bu kuralları denetler (sabit motor etiketi, aile yok, en az bir sorun, kilometre isteğe bağlı); testlere 14 yeni test eklendi (toplam 75).
- **Görüntüleyici:** model geneli kayıtlar koyu kenarlı, "Model geneli" etiketli ayrı kartlarda görünür; kilometre çubuğu yerine "Kaynaklarda kilometre bilgisi yok" yazar ve kilometre filtresi bu sorunları elemez. Arama düzeltmesi: "X2" gibi harf ve tek rakamlı model kodları artık ardından rakam gelen kodları (X243, X253) yakalamıyor.
- **Kapsam planı:** `KAPSAM.md` model geneli taramasını ayrı sayar (90 model nesli arandı: ✓ 53, – 37) ve motor kayıtlarının kaçının taranmış bir modele ait olduğunu gösterir (328 motor kaydından 62'si taranmış bir modele ait, 266'sı henüz taranmadı).
- **Araştırma yöntemi:** Her model nesli için önce Şikâyetvar, DonanımHaber, Otopark ve Ekşi Sözlük'te modele özgü, motordan bağımsız sorgular çalıştırıldı; ikinci bağımsız site için kayıt defterindeki uluslararası forumlara (Ford Owners Club, Qashqai Forums, AudiWorld, Audizine, Briskoda, Planète Renault, Astra Owners Network, Honest John, CarComplaints, Fiat Forum vb.) ve Parkers rehberlerine bakıldı. Bu aşamada dört yeni site kayıt defterine eklendi: Kia Forums, Tesla Motors Club, SwedeSpeed ve Volvo Owners Club Forum. 2017 sonrası modellerin Türkçe kaynağı çoğunlukla Şikâyetvar'dan ibaret olduğu için bu modeller çoğunlukla `–` kaldı.

### Eklenen kayıtlar (53 model nesli, 62 sorun)

Risk dağılımı: 6 Yüksek (iki EPS direksiyon arızası, iki EPB arızası, bir kolon kilidi arızası, bir arka alt çerçeve korozyonu), 35 Orta, 21 Düşük. Beş sorunda yıl kırılımı var. Marka bazında (sorun konusu):

- **Audi (2):** A3 8V (gündüz LED farı sararması), Q5 8R (cam tavan ve plenum tahliyesi tıkanması: ayak boşluğu ve akü yuvasına su).
- **BMW (4):** 1 Serisi F20 (arka stop LED kısıklığı), 3 Serisi F30 (iç kapı kolu kaplaması erimesi; ön cam fitili ve plastik parça kaynaklı su alma), 5 Serisi F10 ve X1 F48 (iç kapı kolu kaplaması).
- **Dacia (1):** Duster 2010-2017 (direksiyon sertleşmesi, EPS ya da hidrolik pompa).
- **Fiat (5):** 500 (akü boşalması ve elektrik arızaları), Doblo (kapı kilit motoru ve merkezi kilit), Egea (klima kompresörü uğultusu; boya atması), Linea ile Punto Evo / Grande Punto (yolcu airbag kapağı üzerinde torpido çatlaması).
- **Ford (3):** Fiesta Mk7 (direksiyon gıcırtısı), Focus 3 (bagaja ve yedek lastik yuvasına su), Kuga 2 / 3 (panoramik tavan perdesi motoru).
- **Honda (2):** Civic FB7 (boya atması), Civic FC5 (kondenser çatlaması; tavan ve bagaj boyası).
- **Hyundai (2):** i20 PB / GB ve i30 FD (EPS arızası).
- **Jeep (1):** Renegade (cam tavan MySky mekanizması ve panelleri).
- **Kia (2):** Ceed ED / JD (torpido kaplaması), Sportage SL (tavan çevresinden su).
- **Mazda (1):** Mazda 3 BL (torpido yüzeyi erimesi).
- **Mercedes-Benz (3):** A / CLA / GLA W176 ve C W204 (direksiyon açı sensörü), E W212 (arka travers korozyonu).
- **Nissan (3):** Juke F15 ve Qashqai J10 (multimedya ekranının sıcakta silikleşmesi), Qashqai J11 (panoramik tavan ve bagaj çevresinden su).
- **Opel (5):** Astra J (EPB), Astra K (kolon kilidi; tavan ve kaput boyası), Corsa D (direksiyon gıcırtısı), Insignia A (far suyu ve AFL), Mokka B (siyah tavan boyası).
- **Peugeot (3):** 208 / 2008 (arka kapı camı fitili), 3008 (multimedya), 308 T9 (arka travers gıcırtısı; klima gazı kaçırma).
- **Renault (5):** Clio 4 (kapı kilidi ve sensörü), Clio 5 (multimedya), Megane 3 / Fluence (ön cam altı ızgarası ve su), Megane 4 (far buğusu ve C-LED; R-Link ekranı), Scenic 3 (EPB).
- **Seat (1):** Leon 5F (tıkırtı ve zırıltı).
- **Skoda (4):** Kodiaq (bagajdan su), Octavia A7 (panoramik tavandan su), Superb III (cam tavan çerçevesi çatlağı), Yeti (kapı kablo demeti).
- **Tesla (1):** Model Y (cam tavan çatlaması; süspansiyon ve kabin gıcırtısı).
- **Toyota (1):** Corolla E210 (multimedya).
- **Volkswagen (3):** Golf 7 / 7.5 (cam tavan çerçevesi çatlağı; bagaja su), Golf 8 / 8.5 (multimedya; SOS hatası), Tiguan AD1 (cam tavandan su).
- **Volvo (1):** XC60 2008-2017 (ön cam yapışması, tahliye ve tavan sızdırmazlığı kaynaklı su).

Sorduğunuz örnek (cam tavan ya da sunroof su alması) şu kayıtlarda: Golf 7 / 7.5, Tiguan AD1, Octavia A7, Superb III, Qashqai J11, Sportage SL, Q5 8R, XC60 (2008-2017) ve bagaj / ön cam çevresi su alması için Kodiaq, Focus 3, Megane 3, 3 Serisi F30.

### Kanıt durumu

- **51 sorun yalnızca iki siteyle desteklenir** (sınırlı doğrulama; KAYNAKLAR.md içinde sayılıyor); 9 sorun üç, 2 sorun (Fiat 500 akü boşalması ve Mercedes E W212 arka travers korozyonu) dört siteyle desteklenir.
- **Dört sorunun Türkçe kaynağı yok:** Q5 8R (AudiWorld, Audizine), Focus 3 (Ford Owners Club, CarComplaints), Yeti (Briskoda, Parkers) ve XC60 2008-2017 (SwedeSpeed, Volvo Owners Club Forum, Parkers). Bu sorunların Türkiye'deki araçlarda aynı sıklıkla görülüp görülmediği bilinmiyor; Türkçe sitelerde eşleşen başlık çıkmadı (plan notlarında yazılı).
- **Yabancı kaynaklı ayrıntılar:** Honest John, CarComplaints ve forum ayrıntıları İngiltere ve ABD pazarındaki araçlara ait olabilir (ör. Focus 3 şikâyet sayıları, Renegade MySky panel şikâyetleri, Fiat 500 Blue&Me modülü).

### Araştırılıp kaydı açılmayan 37 model nesli (`–`)

İki bağımsız site bulunamadığı için plana notlarıyla `–` olarak işlendi (ayrıntı [KAPSAM.md](KAPSAM.md) içinde):

- **Şikâyetvar'da tekrar eden konular var, ikinci bağımsız site çıkmadı ya da çıkan başlıklar başka nesle ait (28):** BMW X3 F25, Citroën C3, Dacia Sandero / Logan / Symbol, Ford Transit Courier / Connect, Honda HR-V / CR-V, Hyundai Accent Blue / Elantra AD ve Tucson / Kona, Jeep Compass, Kia Rio, Mercedes C W205, Mini Countryman / Cooper, Mitsubishi L200 / ASX, Opel Corsa E / F, Peugeot 301 / Citroën C-Elysée, Renault Kadjar / Captur, Seat Ibiza / Arona / Ateca, Skoda Fabia, Karoq ve Rapid, Suzuki Vitara, Toyota Auris / Yaris ile Corolla E170 / E210 (CarPlay sesi dışındaki konular), VW Caddy, Passat B7 ve B8, Polo, T-Roc, Volvo XC60 (2017-) / S60 / V40. Öne çıkan tekrar eden konular: Passat B7 / B8'de cam tavan çerçevesi çatlağı ve su alma (çok sayıda kayıt), Kadjar'da yan aynaların katlanmaması, 301 / C-Elysée'de boya kabarması ve paslanma, Rapid'de boya verniği atması.
- **Başka siteler var ama nesil ya da model eşleşmedi (9):** Audi A4 B8 / A6 C7; Q3 8U (AudiWorld'ün Q3 su sızıntısı başlıkları 2019-2020 ikinci nesle ait, Audizine'daki 2016-2018 yorumu tek site); Honda Jazz (Parkers 2008-2015 bagaj fitili; DonanımHaber başlıkları genel ya da 2004 Jazz); Land Rover Evoque (CarComplaints örnekleri ve servis aksiyonu N221 ikinci nesle ait); Nissan X-Trail T32 (Parkers cam tavan tahliyesi; Honest John başlığının nedeni belirsiz); Skoda Octavia A5 (Briskoda'da çok sayıda bagaj ve plenum başlığı var, Türkçe site ve A5'e ait Parkers rehberi yok); Toyota C-HR (ön cam çatlaması: Türkçe kayıtlar 2025 / ikinci nesil, yabancı kayıtlar 2017 / birinci nesil); VW Golf 6 ve Tiguan 5N (VWVortex başlıkları ortak platforma ya da eski Golf'lere ait).

### Boşluk taraması: listede hiç olmayan modeller

İsteğiniz üzerine ("başka şeylerde çıkar") kayıtlar ve plan, **kendi bilgime göre** Türkiye'de ikinci elde görülen modellerle karşılaştırıldı (bu kez satış verisiyle değil). Listede ve planda hiç olmayan şu modeller bulundu ve `○ sırada` satırı olarak eklendi; motor etiketleri kendi bilgimdir, araştırılmadı: Kia Picanto TA (2011-2017), Hyundai ix20 (benzinli ve dizel), Toyota Aygo, Citroën C1, Mazda 2 (DJ), CX-3 ve CX-30, Land Rover Defender (L663) ve Range Rover Velar. Planda yalnızca birleşik `–` satırı olanlar: Hyundai i10 (Elantra ile), Mazda 6 ve CX-5 (3 ile), Santa Fe ve Sorento. Hâlâ hiç olmayan, hacmi düşük modeller: Audi A8 ve Q8, BMW 6 Serisi, X7 ve Z4, Mercedes GLB ve G Serisi, Lexus NX ve RX, Toyota Camry, Nissan Almera / Tiida, Opel Cascada ve Movano, Renault Express, Seat Exeo, Volvo C30 / S40 / V50, Ford Fusion ve ağırlıkla 2011 öncesi olan Fiat Albea / Palio.

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **Octavia A7:** önce `–` işlenmişti (yalnızca Şikâyetvar); Briskoda'da panoramik tavan sızıntısı başlıkları çıkınca ✓'ye çevrildi, eski plan satırı silindi.
- **Passat B8:** `–` kaldı. VWVortex'in ve CarComplaints'in (servis bülteni listeleri, cam tavan davası haberleri) cam tavan sızıntısı başlıkları ABD pazarındaki Passat'a ait; Avrupa B8'e bağlanmadı.
- **C-HR ön cam çatlaması:** yabancı kaynaklar 2017 model birinci nesli, Türkçe kayıtlar 2025 model ikinci nesli anlatıyor; aynı sorun sayılmadı.
- **Q3 8U, Golf 6, Tiguan 5N:** su sızıntısı başlıkları başka nesle ya da ortak platforma ait olduğu için kayıt açılmadı.
- **Qashqai J11:** Qashqai Forums'taki bagaj kapağı kablo lastiği (grommet) başlığı J10'a ait olduğundan J11 kaydına alınmadı; yalnızca X-Trail T32 notunda geçiyor.
- **Focus 3:** SYNC / multimedya donması Şikâyetvar'da çoğunlukla Focus 4 model yıllarına ait olduğundan kayda alınmadı. Bagaj sızıntısında "arka tampon arkasındaki havalandırma" anlatımının hangi sayfadan geldiği arama özetinden net ayrılamadığı için site düzeyinde (Ford Owners Club) yazıldı; CarComplaints sayfaları yalnızca şikâyet sayısı olarak kullanıldı.
- **Astra J EPB:** Şikâyetvar'ın "Opel El Freni Uyarı Arızası" sayfası model belirtmediği için kaynak listesine alınmadı. Vauxhall Owners Network başlıklarında model belirtilmediğinden o siteye ait ayrıntılar site düzeyinde yazıldı; kayıt, Astra J'ye açıkça bağlı DonanımHaber ve Astra Owners Network başlıklarıyla da iki siteyi geçiyor.
- **Scenic 3 EPB:** bir Honest John başlığındaki fren hidroliği seviyesi iddiası başka bir araca ait olduğu için çıkarıldı; Laguna 3 aynı modülü paylaşıyor mu belirsiz olduğundan kayda katılmadı.
- **308 T9 arka travers (sizin uyarınız üzerine düzeltildi):** ilk yazımda İngilizce kaynaklardaki "rear axle" ifadesi "arka aks" diye çevrilmişti. 308 önden çekişlidir ve arkada tahrik aksı yoktur; sözü edilen parça torsiyon kirişli arka süspansiyonun traversidir. Sorunun kendisi kaynaklarda duruyor (Honest John'da tıkırtı ve kaynak çatlağı, Türkçe forumlarda ücretsiz parça değişimi); yalnızca adlandırma düzeltildi, kayıtta başka "arka aks" ifadesi kalmadı.
- **Model Y cam tavan:** InsideEVs haberleri 2020-2021 ABD üretimi araçlara ait; yapıştırıcı kök nedeni "doğrulanmış değil" olarak yazıldı.
- **i30 FD:** kaynağın tek bir kilometre noktası verdiği sorunda "75.000 - 75.000 km" aralığı kaldırıldı (kilometre alanı boş bırakıldı).
- **Plan notları:** yeni ✓ satırlarıyla çelişen `–` notları tamamlandı (Volvo XC60 / S60 / V40, Corolla E170 / E210, Passat B7 ve B8); Renegade / Compass birleşik `–` satırı bölündü (Renegade ✓, Compass `–`); "A4 B8 / A6 C7 / Q5" birleşik satırı bölündü (Q5 8R ✓). "Citroën" plan yazımı kayıtlardaki "Citroen" ile eşleşecek şekilde düzeltildi.

### Dikkat edilecek sınırlar

- **Kilometre bilgisi yok (62 sorunun 62'si):** kaynaklar yazmadığı için aralık uydurulmadı; görüntüleyicide bu sorunlar "Kaynaklarda kilometre bilgisi yok" etiketiyle görünür ve kilometre filtresiyle elenmez.
- **Doğrulama yine arama özetleriyle yapıldı; `WebFetch` kapalıydı.** Özetler, sayfaları yorumlayan bir araçtan geliyor. Bir özetin hangi sayfadan geldiği belirsizse iddia site düzeyinde yazıldı (ör. Focus 3 havalandırma anlatımı, Sportage forum başlıkları, Q5). Rakam ve alıntılar için asıl sayfaya bakmak gerekir.
- **Sıklık bilgisi yok.** Her sorun "sahipler bildirdi" düzeyindedir; bir modelde yüzde kaçında görüldüğü bilinmez. Risk seviyesi README'deki ölçeğe göre editoryal bir sınıflandırmadır.
- **Model geneli taraması kısmi:** 328 motor kaydından 266'sı henüz taranmamış bir modele ait; satırı olmayan bir modelde bu sorunlar aranmamıştır, satırı olmaması "sorun yok" demek değildir.
- **Kapsam soruları açık:** (1) 2011 öncesi model yılı penceresi hâlâ dışarıda (Tofaş Şahin / Doğan / Kartal, Renault R12-Toros, R9-Broadway, Fiat Albea / Palio). (2) Hibrit ve plug-in hibritler kapsam dışı.

## 12. aşama: model geneli taramasının sürdürülmesi

Tarih: 2026-10-25

11. aşamada 90 model nesli taranmıştı. Bu aşamada isteğiniz üzerine ("planda kaldığınız yerden devam edin, detaylı ve doğrucu ilerleyin") 11. aşamanın açık kalan işleri bitirildi ve tarama kalan markalara genişletildi. Yöntem ve kural aynıdır: önce Şikâyetvar, DonanımHaber, Otopark ve Ekşi Sözlük'te modele özgü sorgular; ikinci bağımsız site için kayıt defterindeki uluslararası forumlar ve rehberler (Ford Owners Club, French Car Forum, BimmerPost, MBWorld, BenzWorld, MB Club UK, Swedespeed, Volvo Owners Club Forum, Honest John, Parkers, Briskoda vb.); en az iki farklı site, en az biri deneyim ya da resmî türünde; **nesil eşleşmesi doğrulanamazsa kayıt açılmadı.** Kayıt defterine yeni site eklenmedi (84).

| | 11. aşama sonu | 12. aşama sonu |
| --- | ---: | ---: |
| Araç/motor kaydı | 381 (328 motor + 53 model geneli) | 400 (328 motor + 72 model geneli) |
| Kayda özgü kronik sorun | 320 (62'si model geneli) | 344 (86'sı model geneli) |
| Farklı kaynak sitesi | 84 | 84 |
| Yalnızca iki siteyle desteklenen sorun | 114 | 127 |
| Ayrıntısı (`detay`) olan sorun | 402 | 426 |
| Plan satırı | 675 | 734 |
| Kanıtı yetersiz `–` satırı | 214 (37'si model geneli) | 264 (78'i model geneli) |
| Sırada `○` satırı | 98 | 88 |
| Taranan model nesli | 90 (✓ 53, – 37) | 150 (✓ 72, – 78) |
| Taranmış bir modele ait motor kaydı | 62 / 328 | 149 / 328 |

### Ne yapıldı

- **A. 11. aşamada "sırada" eklenen on satır araştırıldı (9 satır):** Kia Picanto TA, Hyundai ix20 (benzinli ve dizel), Toyota Aygo, Citroën C1, Mazda 2, Mazda CX-3, Land Rover Defender ve Range Rover Velar için iki bağımsız site (nesil ve model eşleşmesi doğrulanmış) çıkmadı; hepsi notlarıyla `–` işlendi. Düzeltmeler: CX-3 satırı "2.0 SkyActiv-G 120" etiketiyle yazılmıştı; Otopark'taki lansman haberi Türkiye'ye yalnızca 1.5 SkyActiv-D ile geldiğini yazdığı için etiket düzeltildi. CX-30'un Türkiye'de satıldığı doğrulanamadığından satırı kaldırıldı.
- **B. VAG:** Skoda Octavia A8 ve VW Transporter T5 kayda döndü; Touran, Passat CC, Superb II, Audi A1 8X, Q2, A6 C8 ve Seat Ibiza 6J / 6P `–` kaldı.
- **C. Renault, Dacia, Fiat, Ford, Opel, Peugeot, Citroën:** 8 model nesli kayda döndü (10 sorun); 17 model nesli `–` işlendi.
- **D. Asya (Toyota, Hyundai, Kia, Nissan, Honda, Subaru):** Nissan X-Trail T32 kayda döndü (11. aşamadaki `–` satırı ✓ oldu); 7 yeni satır `–`, Tucson / Kona, HR-V / CR-V ve Auris / Yaris notları genişletildi.
- **E. Premium ve elektrikli (BMW, Mercedes, Audi, Volvo, Mini, Land Rover, Alfa Romeo, Porsche, Togg, BYD, MG, Kia/Hyundai EV):** 8 model nesli kayda döndü (10 sorun; Mercedes C W205 11. aşamadaki `–` satırından ✓ oldu); 12 yeni satır `–`; X3 F25, Mini, Evoque ve Volvo S60 / V60 notları genişletildi.

### Eklenen kayıtlar (19 model nesli, 24 sorun)

Risk dağılımı: 12 Orta, 12 Düşük (Yüksek yok; bu kayıtlarda kilometre bilgisi yok). Marka bazında (sorun konusu):

- **Alfa Romeo (1):** Giulietta (yolcu airbag kapağı şişmesi ve çatlaması; iç kapı kolunun kırılması; klima klapesi arızası).
- **Audi (1):** A3 8Y (MMI ekranının kararması).
- **BMW (3):** 3 Serisi G20 (sunroof perdesi ve gıcırtı), 5 Serisi G30 ve X5 F15 (iç kapı kolu kaplaması erimesi; F30, F10 ve X1 F48 kayıtlarındaki sorunla aynı).
- **Citroën (3):** C4 Cactus (kapı alt kenarı paslanması), C4 Picasso II (cam tavan perdesi tırnağı), C5 Aircross (siyah tavan boyası).
- **Fiat (1):** Bravo (yolcu airbag kapağı; klima klapesi; yolcu güneşliği).
- **Ford (2):** C-Max / Grand C-Max (cam tavan perdesi), Puma (direksiyon sesi).
- **Mercedes-Benz (1):** C Serisi W205 (panoramik tavan ray, kılavuz ve motor arızası).
- **Nissan (1):** X-Trail T32 (ön cam altı ve cam tavan tahliyelerinden ayak boşluğuna ve sigorta kutusuna su).
- **Peugeot (1):** 508 II (sunroof / panoramik tavan).
- **Renault (1):** Captur 2 (Easy Link ekranı donması).
- **Skoda (1):** Octavia A8 (multimedya kendiliğinden açılması ve ses; bagaj kaması sesi).
- **Togg (1):** T10X (kapıların açılmaması ya da kilitlenmemesi).
- **Volkswagen (1):** Transporter T5 (yan cam ve sürgülü kapı fitillerinden su).
- **Volvo (1):** XC90 / S90 / V90 (Sensus orta ekran donması ve yeniden başlaması).

Sorduğunuz türden örnekler: sunroof ve cam tavan kaynaklı sorunlar G20, 508 II, W205 (sunroof / panoramik tavan), C-Max ve C4 Picasso II (cam tavan perdesi); su alma için X-Trail T32 (ön cam altı ve tavan tahliyeleri) ve Transporter T5 (yan cam fitili).

### Kanıt durumu

- **24 sorunun 13'ü yalnızca iki siteyle** (sınırlı doğrulama), 8'i üç, 2'si dört (C4 Cactus kapı paslanması, X-Trail T32) ve 1'i beş siteyle (W205) desteklenir. Her sorunun en az bir Türkçe kaynağı var; **beş sorunun tek Türkçe kaynağı Şikâyetvar'dır** (Puma, G30 ve X5 F15 iç kapı kolu, Transporter T5, Volvo Sensus) ve ikinci kaynak yabancı bir forumdur (Ford Owners Club, BimmerPost, Honest John ve Parkers, Swedespeed ve Volvo Owners Club Forum). Bu sorunların Türkiye'deki araçlarda aynı sıklıkla görülüp görülmediği bilinmiyor.
- **Yabancı kaynaklı ayrıntılar** İngiltere ve ABD pazarındaki araçlara ait olabilir (ör. W205 maliyetleri MBWorld'de dolar cinsinden; BimmerPost ABD'de; French Car Forum ve Ford Owners Club İngiltere'de). Maliyet alanları kullanıcı beyanıdır ve güncel fiyat olarak okunmamalıdır.
- **Site düzeyinde yazılan atıflar:** arama özetlerinin bir iddiayı hangi sayfaya bağladığı belirsiz kaldığında iddia site düzeyinde yazıldı (Bravo ve C5 Aircross DonanımHaber / Ekşi / Otopark sayfaları, C4 Cactus DonanımHaber ve Otopark, Giulietta klima ve kapı kolu, Puma Ford Owners Club, Volvo Swedespeed ve Volvo Forums UK, W205 DonanımHaber / Ekşi yorumu).

### Araştırılıp kaydı açılmayan 43 yeni model nesli (`–`)

İki bağımsız site ya da nesil eşleşmesi bulunamadığı için plana notlarıyla `–` olarak işlendi (ayrıntı [KAPSAM.md](KAPSAM.md) içinde):

- **VAG (7):** Touran, Passat CC, Superb II, Audi A1 8X, Q2, A6 C8, Seat Ibiza 6J / 6P.
- **Renault, Dacia, Fiat, Ford, Opel, PSA (17):** Opel Insignia B, Crossland X / Grandland X, Zafira Tourer, Meriva B, Combo D; Peugeot 207, 3008 I / 5008 I, Partner / Rifter / Citroën Berlingo; Renault Clio 3 / Symbol, Kangoo, Talisman; Fiat Panda, Fiorino / Qubo; Dacia Lodgy / Dokker; Ford Focus 4, EcoSport, Mondeo.
- **Asya (7):** Hyundai i30 GD / PD, ix35, Bayon / i20 BC3; Kia Sportage QL, Ceed CD / Stonic / Picanto JA; Nissan Micra K13 / K14 / Note E12; Subaru Forester / XV / Impreza.
- **Premium ve elektrikli (12):** BMW 2 Serisi / 4 Serisi / X2; Mercedes E W213, A W177 / CLA C118, GLC / GLA / B W246; Audi A4 B9, Q5 FY / Q3 F3; Land Rover Discovery Sport; Alfa Romeo Giulia / Stelvio; Porsche Macan / Cayenne; BYD Atto 3, MG4, Kia EV6 / Hyundai Ioniq 5.

Nedeni çoğunlukla "tek sitede (Şikâyetvar) tekrar eden konular, ikinci bağımsız site yok" (2017 sonrası modellerin Türkçe kaynağı büyük ölçüde Şikâyetvar'dan ibaret). Öne çıkan tekrar eden ama tek siteli konular: i30 GD'de cam tavan kasası çatlağı ve sızıntı, Tucson TL'de cam tavan perdesi ve direksiyon kilidi, Bayon / i20'de cam düğmeleri ve korna, Talisman'da R-Link 2 Bluetooth kopması, Fiorino'da cam krikosu, Ceed CD ve Stonic'te direksiyon kaplaması, Insignia B'de deri direksiyon soyulması, Atto 3'te amortisör sesi ve park sensörü, Stelvio'da far buğusu. **Nesil ya da model eşleşmediği için kayda alınmayan kanıtlar:**

- **Meriva B direksiyon (EPS):** Honest John ve Vauxhall Owners Network'teki EPS başlıkları (tork sensörü, C1500 kodu, BBC Watchdog, geri çağırma talepleri) ağırlıkla ilk kuşak Meriva A (2003-2010) için; Meriva B için 2013 model tek sahip kaydı; DonanımHaber başlığı nesil belirtmiyor.
- **Panda direksiyon (EPS):** Şikâyetvar ve DonanımHaber'deki Panda kayıtları 2005-2011 (169 şasi); fiatforum'da "Panda (Mk3)" etiketli başlıklar da var ama tek site.
- **Micra K13 direksiyon (EPS):** DonanımHaber ve Honest John başlıkları K12 (2003-2010) içindir.
- **Clio 3 / Symbol teyp ekranı:** "Symbol" adı Türkiye'de 2013'ten sonra Logan tabanlı araç için de kullanıldığından Şikâyetvar sayfalarının model yılı doğrulanamadı.
- **Focus 4 SYNC 3:** Ford Owners Club başlıklarının çoğu Mk3 Focus, Fiesta ve EcoSport'a ait.
- **Insignia B deri direksiyon:** Ekşi Sözlük'teki "direksiyon kaplamasının soyulması kronik" yorumunun sayfası Insignia A ve Astra K ile ortak başlıklarda.
- **ix35 4x4 aktarma (freze) sıyırması:** Şikâyetvar'da "kronik" başlıklı ama kilometre bilgisi ve ikinci site yok; motor / şanzıman kaydına da alınamadı.
- **BMW X3 F25 iç kapı kolu:** BimmerPost'ta F25'e özgü başlık çıkmadı (sonuçlar F30, F80, E90, F15).
- **Discovery Sport / Evoque (Ingenium):** CarComplaints kayıtları ABD'de satılan benzinli Ingenium'a ait (ABD'de dizel yok); dizel zincir iddiasına alınmadı, aile açılmadı.

### Yazım sırasında çıkarılan ya da düzeltilen iddialar

- **Octavia A8 bagaj kaması:** ilk arama özeti Ekşi Sözlük'teki "36 bin km'de garantide değişti" yorumunu Şikâyetvar'a bağlamıştı; ayrı bir doğrulama aramasıyla kaynaklar ayrıldı (Şikâyetvar: 2021 model, 68.000 km, 6 servis; Ekşi Sözlük: 36 bin km).
- **Bravo:** Şikâyetvar kaydındaki "bayi 90 bin TL fiyat çıkardı" tutarı doğrulanamadığı için kayda alınmadı; Ekşi Sözlük'te kaplamayı yerinden ayıran şişme anlatımı Fiat 500'e ait olduğundan Bravo'ya katılmadı.
- **Punto Evo / Grande Punto direksiyon (EPS):** bu aşamada yeniden arandı; sorun zaten motor kaydında (1.3 Multijet 75/95 ve 1.4 Fire 77) olduğundan ikinci bir model geneli kayıt açılmadı.
- **Mercedes C W205 ve Nissan X-Trail T32:** 11. aşamada `–` idiler (tek başlıklar / Türkçe kaynak çıkmamıştı); MBWorld'ün W205 bölümünde çok sayıda panoramik tavan başlığı, X-Trail için Ekşi Sözlük ve Şikâyetvar kayıtları bulununca ✓ yapıldı.
- **X-Trail T32 plan satırı:** satırın eşleşme anahtarı kayıt adıyla uyuşmadığından ara kayıt 3 ve 4 commit'lerinde KAPSAM.md'de "sırada" görünüyordu; bu aşamanın son commit'inde düzeltildi.
- **Ara kayıt 4 commit mesajı** dilim E için "11 sorun" yazıyor; doğrusu 10 (aşamanın toplamı 24: dilim B 3, C 10, D 1, E 10).
- **W205 maliyet cümlesi:** "parça ve işçilik için yaklaşık 80.000 TL" ifadesinden kaynakta olmayan "parça ve işçilik" ayrımı çıkarıldı.
- **Plan notları:** yeni ✓ satırlarıyla çelişen ya da güncelliğini yitiren `–` notları (Tucson / Kona, HR-V / CR-V, Auris / Yaris, X3 F25, Mini, Evoque, Volvo S60 / V60) yeni bulgularla tamamlandı.

### Dikkat edilecek sınırlar

- **Kilometre bilgisi yok (86 model geneli sorunun 86'sı):** kaynaklar yazmadığı için aralık uydurulmadı; görüntüleyicide "Kaynaklarda kilometre bilgisi yok" etiketiyle görünür ve kilometre filtresiyle elenmez.
- **Doğrulama yine arama özetleriyle yapıldı; `WebFetch` kapalıydı.** Özetler, sayfaları yorumlayan bir araçtan geliyor; bazen sayfa başlıkları ve alıntılar özetle birebir uyuşmuyor (ör. Giulietta klima ve kapı kolu, Volvo Sensus başlıklarının hangi modele ait olduğu). Rakam ve alıntılar için asıl sayfaya bakmak gerekir.
- **Sıklık bilgisi yok.** Her sorun "sahipler bildirdi" düzeyindedir; Şikâyetvar ve forumlar şikâyet edenleri gösterir. Risk seviyesi README'deki ölçeğe göre editoryal bir sınıflandırmadır.
- **Model geneli taraması kısmi:** 328 motor kaydından 179'u model adı eşleşmesine göre taranmamış bir modele ait görünüyor (eşleşme model adının tam metnine bakar; bazı kayıtlar farklı yazım yüzünden taranmış modellerin altında olsa da sayılmayabilir). Satırı olmayan bir modelde bu sorunlar aranmamıştır; satırı olmaması "sorun yok" demek değildir.
- **Listede olmayan modeller:** tarama sırasında karşılaşılan ve ne veritabanında ne planda olanlar: Ford Transit Custom / Tourneo Custom (Şikâyetvar: akü, yağ eksiltme, DPF), Citroën Jumpy / Jumper, Peugeot Expert / Boxer (motor, şanzıman / kavrama, AdBlue), Tesla Model 3 (şikâyet çıkmadı). Önceki listedeki hacmi düşük modeller (Audi A8 ve Q8, BMW 6 Serisi / X7 / Z4, Mercedes GLB ve G Serisi, Lexus NX / RX, Toyota Camry, Nissan Almera / Tiida, Opel Cascada / Movano, Renault Express, Seat Exeo, Volvo C30 / S40 / V50, Ford Fusion, Fiat Albea / Palio) hâlâ yok.
- **Kapsam soruları açık:** (1) 2011 öncesi model yılı penceresi hâlâ dışarıda (Tofaş Şahin / Doğan / Kartal, Renault R12-Toros, R9-Broadway, Fiat Albea / Palio; Fiat Panda 169 gibi 2011 öncesi nesiller). (2) Hibrit ve plug-in hibritler kapsam dışı.

## Sonraki adımlar

1. Ağ erişimi verilirse `KAYNAKLAR.md` içindeki sayfalar doğrudan okunarak her bağlantının iddiayı gerçekten içerdiği, ayrıntılardaki rakam ve alıntıların doğru olduğu kontrol edilebilir.
2. Yalnızca iki siteyle desteklenen 57 maddeye (3. aşama sonundaki 22, 4. aşamada eklenen 22, 5. aşamada eklenen 2; 6. aşamada üç madde eklendi, Citroën ë-C4 üçüncü kaynak alarak listeden çıktı; 7. aşamada Astra 1.3 CDTI Easytronic eklendi; 8. aşamada Leon KL 48V, Superb IV 48V, Karoq titreşimi ve Audi A3 8Y 48V eklendi; 9. aşamada Jetta DSG mekatroniği, Ceed 7DCT ve Qashqai 1.3 DIG-T'nin iki sorunu eklendi) üçüncü bir kaynak eklenebilir. 11. aşamada eklenen model geneli sorunların 51'i, 12. aşamada eklenenlerin 13'ü yalnızca iki siteyle destekleniyor (doğrulayıcının bildirdiği toplam: 127).
3. Kanıtı yetersiz bulunan 264 grup (186'sı motor ve şanzıman, 78'i model geneli) için [KAPSAM.md](KAPSAM.md) içinde nedenleriyle yazılı; yeni kaynak çıkarsa eklenebilir. Nedeni "ikinci bağımsız kaynak yok" olanlar (ör. Hyundai Kona, Opel Mokka 1.6 CDTI, Honda City, Ford Transit Custom ve Ranger, Nissan Navara, Isuzu D-Max, Toyota Hilux, Fiat Ducato, Renault Megane E-Tech, Fiat 500e, Kia Niro EV, Peugeot e-3008, Alfa Romeo Junior Elettrica, Togg T10F, Kia EV9) için Şikâyetvar dışında bir forum ya da haber kaynağı bulunması yeterli olur.
4. "Kanıtı sınırlı ayrıntılar" listelerindeki maddeler Türkçe servis ya da forum kaynağıyla güçlendirilebilir; maliyet alanı boş kalan 104 soruna güncel Türkiye fiyatı bulunursa eklenebilir.
5. Elektrikli araçlarda geri çağırma kaydı bulunan ama Türkiye kapsamı doğrulanamayan aileler (Volvo EX30, VW ID. serisi, Mini Cooper SE, BMW iX / i4, Audi e-tron GT) için Türkiye distribütörlerinin duyuruları ya da Ticaret Bakanlığı geri çağırma kayıtları bulunursa kayıt açılabilir.
6. Hibrit ve plug-in hibrit araçlar (Toyota hibritleri, BYD Seal U DM-i gibi) bu aşamada kapsam dışı bırakıldı; istenirse aynı kurallarla eklenebilir.
7. Kaynaklar ayırt ettikçe yeni motor versiyonları ayrı kayıt olabilir (ör. N47 177 / 184 bg); eklemek istenen yeni marka, model ve motor için plana satır eklenip aynı döngü uygulanır.
8. **Aile bağlarının doğrulanması:** 285 kaydın hangi motor ve şanzımanla satıldığı üretici ya da distribütör kataloglarından tek tek kontrol edilebilir; özellikle Türkiye'de satılıp satılmadığı belirsiz kombinasyonlar (ör. Stonic 1.6 CRDi, Rio YB 1.0 T-GDI 7DCT, Yaris XP210 benzinli 1.5) için.
9. **Aile sorunlarının güçlendirilmesi:** tek modelin kaynağına dayanan aile sorunları (ör. 7G-Tronic iletken plaka, Multitronic, Subaru FB20, A16XER) başka bir modelin kaynağıyla desteklenebilir; 2.0 TDI (EA189 / EA288), 1.0 TSI (EA211 üç silindir) ve R9M 1.6 dCi gibi büyük ailelerin henüz sorunu yok.
10. **88 "sırada" satırı** aynı döngüyle (önce aile, sonra Türkçe arama) işlenebilir; öncelik Land Rover Evoque ve Discovery Sport (Ingenium), Mercedes GLE W166 ve Vito, BMW X2 / 2 Serisi F44 dizel, Audi A6 C8 / A3 8Y 30 TFSI / Q3 F3, Fiat Bravo (1.4 T-Jet / 1.6 Multijet) ve Panda 1.3, Renault Kangoo 3, Opel Insignia B 1.5 Turbo / 2.0 CDTI, Ford Puma 1.0 EcoBoost. 11. aşamada eklenen on satırın dokuzu 12. aşamada arandı (hepsi `–`; CX-30 satırı kaldırıldı).
11. **Model geneli taramasının sürdürülmesi:** 179 motor kaydı hâlâ taranmamış bir modele ait görünüyor. Model geneli satırı olmayan modeller (kabaca): Audi A5 8T; Chevrolet Cruze; Citroën ë-C4; Cupra Formentor; Dacia Jogger ve Sandero (2021-); Fiat 500L, 500X ve 600e; Ford B-Max ve Transit Connect; Hyundai Ioniq 5 / 6 (EV6 ile birlikte `–`, motor satırları ayrı); Jeep Avenger Electric; Kia EV3; Mercedes Citan, Sprinter, Vito, GLK, EQA / EQB ve EQC; Opel Astra H, Corsa-e / Mokka-e ve Astra Electric; Peugeot 308 T7, e-208 ve e-308; Porsche Taycan; Renault Arkana, Scenic 4, Taliant, Zoe ve Laguna 3; Seat Toledo; Skoda Kamiq / Scala; VW Arteon, Jetta ve T-Cross / Taigo.
12. **`–` kalan model geneli sorunlar:** Şikâyetvar'da tekrar eden konular (Passat B7 / B8 cam tavan çerçevesi, Kadjar yan aynaları, 301 / C-Elysée boyası, Rapid boyası, i30 GD cam tavan kasası, Tucson TL cam tavan perdesi ve direksiyon kilidi, Talisman R-Link 2, Insignia B deri direksiyon, Atto 3 amortisör sesi vb.) için DonanımHaber, Otopark ya da bir yabancı forumda ikinci kaynak bulunursa ✓'ye çevrilebilir. Türkçe kaynağı olmayan dört sorun (Q5 8R, Focus 3, Yeti, XC60) için Türkçe bir site kaydı bulunursa güçlenir.
