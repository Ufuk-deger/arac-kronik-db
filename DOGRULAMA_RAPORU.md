# Doğrulama raporu

Tarih: 2026-10-24

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
- Opel Astra K 1.4 Turbo LSPI ve piston kırılması (Astra K veritabanında yok)
- Mercedes OM651 zincir gergisi conta geri çağırması, 2015 (tek kaynak, AustralianCar.Reviews)
- Peugeot 3008 (2020) kam zinciri geri çağırması (Şikâyetvar alıntısı; 1.6 THP'yi kapsayıp kapsamadığı belirsiz)
- Ford 1.0 EcoBoost yağ pompası kayışı gergi kolu geri çağırması (ABD pazarındaki Focus ve EcoSport)

## Sonraki adımlar

1. Ağ erişimi verilirse `KAYNAKLAR.md` içindeki sayfalar doğrudan okunarak her bağlantının iddiayı gerçekten içerdiği kontrol edilebilir.
2. Yalnızca iki siteyle desteklenen maddelere üçüncü bir kaynak eklenebilir.
3. Eksik modeller (Hyundai i20, Kia, Skoda Superb vb.) aynı kuralla eklenebilir.
