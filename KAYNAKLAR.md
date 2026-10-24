# Kaynaklar

Bu dosya `scripts/kaynaklar_md_uret.py` ile `data/kaynaklar.json` ve `data/araclar.json` içeriğinden üretilir. Elle düzenlemeyin; siteyi `data/kaynaklar.json` içinde değiştirip betiği yeniden çalıştırın.

## Kural

`data/araclar.json` içindeki her kronik sorun (araç kayıtlarındakiler ve motor/şanzıman ailelerinin ortak sorunları), `kaynaklar` alanında **en az iki farklı sitenin** sayfasıyla desteklenir. Kaynaklardan en az biri deneyime ya da resmî belgeye dayanmalıdır (forum, şikâyet, anket, dava haberi, haber veya resmî belge). Yalnızca blog, parça satıcısı ya da derleme sitesi olan sorunlar veritabanına alınmaz. `python3 scripts/dogrula.py` bu kuralı denetler.

## Nasıl okunmalı

Her sayfa yalnızca bir ipucudur. Bir forum yazısı tek bir aracı, bir şikâyet tek bir sürücüyü anlatır ve oran göstermez. Birden fazla bağımsız sitede aynı sorunun görülmesi güven verir; yine de kilometre aralıkları tahmindir ve satın alma ya da onarım kararından önce aracın yetkili serviste kontrol edilmesi gerekir.

| Tür | Anlamı |
| --- | --- |
| `resmi` | Resmî kurum belgesi (geri çağırma, servis bülteni, şikâyet kaydı) |
| `forum` | Kullanıcı forumu |
| `sikayet` | Şikâyet platformu veya sürücü yorumu derlemesi |
| `anket` | Sahip anketi |
| `dava-haberi` | Dava, toplu başvuru veya tüketici örgütü duyurusu |
| `haber` | Haber sitesi |
| `editoryal` | Editör veya blog yazısı |
| `parca-atolye` | Parça üreticisi, parça satıcısı veya atölye rehberi |
| `toplayici` | Başka kaynaklardan derleme yapan site |

Güvenilirlik sütunu sitenin türüne ve düzenine göre verilmiş bir değerlendirmedir: `yüksek` resmî belge veya köklü yayın, `orta` kullanıcı deneyimi içeren kalabalık kaynak, `düşük` ticari ya da zayıf kaynaklı site demektir. `düşük` kaynaklar tek başına yeterli sayılmaz.

## Doğrulama yöntemi ve sınırları

Bu çalışmayı yürüten ortamda dış sitelere doğrudan erişim kapalıydı. Aşağıdaki adreslere sayfa açma denemesi başarısız oldu (`WebFetch` alan adını çözemedi, `curl` proxy tarafından `403` ile reddedildi):

- `otopark.com`
- `andcetin.com`
- `carcomplaints.com`
- `honestjohn.co.uk`
- `araclo.com`
- `forum.donanimhaber.com`
- `static.nhtsa.gov`
- `planeterenault.com`
- `en.wikipedia.org`

Bu yüzden kaynaklar web araması sonuçlarından toplandı. Her bağlantı, arama sonucunda göründüğü sayfa başlığı ve özetine göre ilgili soruna eşlendi; sayfaların tamamı tek tek okunmadı. Bir bağlantıda iddia bulamazsanız `DOGRULAMA_RAPORU.md` içindeki bilgiyi ve ilgili sorunun diğer kaynaklarını kontrol edin, bulamadığınız maddeyi bildirin. Ortama ağ erişimi verilirse sayfalar doğrudan okunarak doğrulama derinleştirilebilir.

İlk istekte "Mehmet Çetin'in sitesi" diye anılan kaynak için `andcetin.com` ("And Mehmet Çetin") kullanıldı. Kastedilen site farklıysa `data/kaynaklar.json` güncellenmelidir.

Toplam 80 farklı site, 258 sorun için kullanıldı.

## Türkçe kaynaklar

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [DonanımHaber Forum](https://forum.donanimhaber.com/) | TR | orta | 245 | Çok sayıda 'kronik sorun var mı' başlığı. Kullanıcı deneyimi; doğruluk başlığa göre değişiyor. |
| [Şikâyetvar](https://www.sikayetvar.com/) | TR | orta | 218 | Kullanıcıların kendi bildirdiği şikâyetler. Oran göstermez; kilometre ve servis yanıtları işe yarıyor. |
| [Araclo](https://www.araclo.com/) | TR | düşük | 130 | Model ve motor başına 'kronik sorunlar' sayfaları. Ticari bir site; sayfalar birbirine çok benziyor, tek başına yeterli sayılmaz. |
| [OTOPARK.COM Forum](https://otopark.com/forum/) | TR | orta | 115 | Marka ve model bazında 'nasıldır / kronik problemleri var mı' başlıkları. Kullanıcı deneyimi; bazı başlıklar eski veya kapalı. |
| [And Mehmet Çetin](https://andcetin.com/) | TR | orta | 79 | Motor ve şanzıman sorunlarını model ailesi bazında anlatan yazılar. Tek yazarın görüşü; okur yorumları ek bilgi veriyor. |
| [Ekşi Sözlük](https://eksisozluk.com/) | TR | düşük | 73 | Kısa kullanıcı girdileri. İpucu olarak kullanılır, tek başına kanıt sayılmaz. |
| [arabam.com Blog](https://www.arabam.com/blog/) | TR | düşük | 6 | İlan sitesinin blog yazıları. Genel bilgi verir; bazı yazılar motorun 'büyük bir kronik sorunu yoktur' gibi genellemeler içeriyor. |
| [Autopartia](https://autopartia.com/) | TR | düşük | 5 | Yedek parça satıcısı; motor bazlı blog ve 'uzman' sayfaları. Ticari site, belirli bir OEM parçayı sürekli öneriyor; tek başına yeterli sayılmaz. |
| [Carsece](https://www.carsece.com/) | TR | düşük | 5 | Araç rehberi ve bakım blogu. Maliyet tahminlerinin kaynağını göstermiyor; tek başına yeterli sayılmaz. |
| [Drivisual](https://www.drivisual.tv/) | TR | düşük | 4 | Motor bazlı satın alma ve kronik sorun rehberleri (Türkçe ve İngilizce). Tek bir blog; bağımsız kaynakla karşılaştırılmalı. |
| [Sözcü](https://www.sozcu.com.tr/) | TR | orta | 1 | Ulusal gazete. Burada yalnızca yabancı toplu dava ve geri çağırma haberlerinin Türkçe aktarımı için kullanıldı. |
| [SıfırAraçAl](https://www.sifiraracal.com/) | TR | düşük | 1 | Türkiye'de yeni araç haberleri ve fiyat listeleri; model yenilemeleri ve motor/batarya verileri için. |

## Yurtdışı kaynaklar

### Resmî belgeler ve dava haberleri

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [NHTSA (ABD)](https://www.nhtsa.gov/) | US | yüksek | 10 | Resmî geri çağırma, servis bülteni (TSB) ve şikâyet kayıtları. |
| [Volkswagen Yeni Zelanda](https://www.volkswagen.co.nz/) | NZ | yüksek | 10 | Üretici kampanya sayfası (DQ200 mekatronik ünitesi, kampanya 35E5). Yeni Zelanda pazarı için yayımlanmış; Türkiye'de geçerliliği ayrıca doğrulanmalı. |
| [ClassAction.org](https://www.classaction.org/) | US | orta | 3 | Toplu dava haberleri. Dava iddiaları kanıtlanmış kusur anlamına gelmez. |
| [OCU (İspanya)](https://www.ocu.org/) | ES | orta | 3 | İspanyol tüketici örgütünün Renault motoru için toplu başvuru sayfası. |
| [Ammons Law Firm](https://www.ammonslaw.com/) | US | düşük | 1 | Hukuk bürosu sayfası. Honda arka lastik aşınması için servis bülteni özetini içeriyor. |
| [Que Choisir](https://www.quechoisir.org/) | FR | orta | 1 | Fransız tüketici örgütü (UFC-Que Choisir); sahip bildirimlerine dayanan araştırmalar yayımlar. |
| [Top Class Actions](https://topclassactions.com/) | US | orta | 1 | Toplu dava ve uzlaşma haberleri. |
| [ÖAMTC](https://www.oeamtc.at/) | AT | yüksek | 1 | Avusturya otomobil kulübü; geri çağırma duyurularını model ve üretim dönemiyle listeler. |

### Forumlar

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [Honest John](https://www.honestjohn.co.uk/) | UK | orta | 19 | Forum ve editör yanıtları ('Ask HJ'). Forum yazıları çoğunlukla 10 yıldan eski olabiliyor. |
| [French Car Forum](https://www.frenchcarforum.co.uk/) | UK | orta | 15 | Peugeot, Citroën ve Renault forumu. |
| [Ford Owners Club](https://www.fordownersclub.com/) | UK | orta | 13 | Ford sahipleri forumu (Focus, Fiesta, EcoBoost). |
| [Fiat Forum](https://www.fiatforum.com/) | UK | orta | 11 | Fiat sahipleri forumu (Dualogic, Multijet, Tipo). |
| [VWVortex](https://www.vwvortex.com/) | US | orta | 10 | Volkswagen forumu. |
| [BRISKODA](https://www.briskoda.net/forums/) | UK | orta | 9 | Škoda sahipleri forumu. |
| [Vauxhall Owners Network](https://www.vauxhallownersnetwork.co.uk/) | UK | orta | 9 | Vauxhall/Opel sahipleri forumu. |
| [Bimmerpost](https://f30.bimmerpost.com/) | US | orta | 7 | BMW F30 ve diğer kasa forumları. |
| [AudiWorld](https://www.audiworld.com/) | US | orta | 6 | Audi forumu ve rehber yazıları. |
| [Berlingo Forum](https://www.berlingoforum.com/) | UK | orta | 4 | Citroën Berlingo ve PSA dizel (HDi) forumu. |
| [MBWorld](https://mbworld.org/) | US | orta | 4 | Mercedes-Benz forumu. |
| [Nissan QashQai Forums](https://www.qashqaiforums.co.uk/) | UK | orta | 4 | Nissan Qashqai sahipleri forumu. |
| [SpeakEV](https://www.speakev.com/) | UK | orta | 4 | İngiltere merkezli elektrikli araç sahibi forumu; Zoe, Peugeot e-208, BYD gibi modellerde 12V akü, şarj ve tahrik arızası konuları. |
| [Astra Owners Network](https://www.astraownersnetwork.co.uk/) | UK | orta | 3 | Opel/Vauxhall Astra forumu. |
| [CruzeTalk](https://www.cruzetalk.com/) | US | orta | 3 | Chevrolet Cruze forumu. Konular çoğunlukla ABD'deki 1.4T ve 1.8 motorlar için. |
| [Audizine](https://www.audizine.com/) | US | orta | 2 | Audi forumu. |
| [BenzWorld](https://www.benzworld.org/) | US | orta | 2 | Mercedes-Benz forumu. |
| [CivicX](https://www.civicx.com/) | US | orta | 2 | Honda Civic (10. nesil) forumu. |
| [E90Post](https://www.e90post.com/) | US | orta | 2 | BMW 3 Serisi E90/E92 forumu. |
| [Forum Peugeot](https://www.forum-peugeot.com/) | FR | orta | 2 | Fransızca Peugeot forumu. |
| [German Car Forum](https://www.germancarforum.com/) | Global | orta | 2 | Alman markaları forumu. |
| [MB Club UK](https://forums.mbclub.co.uk/) | UK | orta | 2 | Mercedes-Benz sahipleri forumu. |
| [Planète Renault](https://www.planeterenault.com/forum/) | FR | orta | 2 | Fransızca Renault forumu. K9K yatak sorunu için moderatör yazısı bu sitede. |
| [8thCivic](https://www.8thcivic.com/) | US | orta | 1 | Honda Civic (8. nesil, FD) forumu. |
| [AudiSRS](https://audisrs.com/) | UK | orta | 1 | Audi ve VAG forumu. |
| [ElectricVehicleForums](https://electricvehicleforums.com/) | US | düşük | 1 | Civic Hybrid forumu; Honda 08-001 bülteni aktarımı içeriyor. |
| [PicoAuto Forum](https://www.picoauto.com/support/) | UK | düşük | 1 | Tanı cihazı üreticisinin destek forumu. |
| [Toyota Owners Club](https://toyotaownersclub.com/) | UK | orta | 1 | Toyota sahipleri forumu (Auris/Corolla D-4D). |

### Şikâyet platformları, sahip anketleri ve derlemeler

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [CarComplaints.com](https://www.carcomplaints.com/) | US | yüksek | 23 | NHTSA şikâyetlerini ve dava haberlerini model yılı bazında derler. Yalnızca ABD pazarındaki araçları kapsar. |
| [Fiches-Auto.fr](https://www.fiches-auto.fr/) | FR | orta | 13 | Sürücü yorumlarından derlenen arıza ve güvenilirlik sayfaları. |
| [AustralianCar.Reviews](https://australiancar.reviews/) | AU | orta | 3 | Model bazında geri çağırma ve arıza listeleri. |
| [CarChecker.pro](https://www.carchecker.pro/) | Global | düşük | 2 | Genel amaçlı model raporları; iddialar zayıf kaynaklıdır. |
| [Consumer Reports](https://www.consumerreports.org/) | US | yüksek | 2 | Sahip anketlerine dayalı güvenilirlik verisi ve kampanya haberleri. |
| [RepairPal](https://repairpal.com/) | US | orta | 1 | Arıza belirtisi ve onarım maliyeti derlemesi. |
| [au7o](https://au7o.io/) | Global | düşük | 1 | Arıza kodu ve bilinen sorun derlemesi. |

### Editör yazıları ve haberler

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [Parkers](https://www.parkers.co.uk/) | UK | orta | 13 | İkinci el alım rehberleri ve haberler. |
| [L'argus](https://www.largus.fr/) | FR | yüksek | 7 | Fransız otomotiv yayını. Güvenilirlik yazıları, tekrarlayan arıza listeleri ve geri çağırma haberleri. |
| [InsideEVs](https://insideevs.com/) | US | orta | 5 | Elektrikli araç haberleri; geri çağırma ve yaygın arıza özetleri. |
| [CompleteCar.ie](https://www.completecar.ie/) | IE | düşük | 4 | İrlanda merkezli araç sitesi; okur sorularına yanıt veriyor. |
| [electrive.com](https://www.electrive.com/) | DE | orta | 4 | Elektrikli araç ve şarj haberleri; Avrupa geri çağırmaları ve KBA kayıtlarına atıflar. |
| [The Connexion](https://www.connexionfrance.com/) | FR | orta | 3 | Fransa haberleri (İngilizce). UFC-Que Choisir'in 1.2 TCe yağ tüketimi uyarısını aktarıyor. |
| [auto motor und sport](https://www.auto-motor-und-sport.de/) | DE | yüksek | 3 | Alman otomotiv dergisi; geri çağırma haberlerinde KBA (Federal Motorlu Taşıtlar Dairesi) bildirimlerine dayanır. |
| [AUTO BILD](https://www.autobild.de/) | DE | yüksek | 2 | Alman otomotiv yayını. Şikâyet sayıları ve üretici açıklamaları. |
| [CarGuide.PH](https://www.carguide.ph/) | PH | orta | 2 | Filipinler otomotiv haberleri. BMW geri çağırma duyurusu. |
| [Caradisiac](https://www.caradisiac.com/) | FR | orta | 2 | Fransız otomotiv yayını. Güvenilirlik dosyaları ve forum bölümü var. |
| [Malay Mail](https://www.malaymail.com/) | MY | orta | 2 | Malezya haber sitesi; Passat 2.0 TDI yağ pompası geri çağırma haberi. |
| [Gebrauchtwagenberater](https://gebrauchtwagenberater.de/) | DE | düşük | 1 | Almanca ikinci el rehberi (Astra K). Resmî bir Opel belgesi değil. |
| [Stellantis Medya](https://www.media.stellantis.com/) | Global | yüksek | 1 | Üretici basın bültenleri (Türkiye bölümü dahil); batarya, güç ve menzil gibi teknik veriler için güvenilir, arıza kanıtı değildir. |
| [Testcoches](https://testcoches.es/) | ES | orta | 1 | İspanyol otomobil haber sitesi; model bazlı arıza ve geri çağırma haberleri. |
| [WardsAuto](https://www.wardsauto.com/) | US | orta | 1 | ABD otomotiv sektörü haber ve analiz yayını; üretici kampanyalarını aktarır. |
| [WheelStreet](https://www.wheelstreet.lt/) | LT | düşük | 1 | Litvanyaca ikinci el rehberi (Passat B6). |
| [autohaus.de](https://www.autohaus.de/) | DE | orta | 1 | Alman otomotiv ticareti yayını; geri çağırma haberlerinde KBA referans numaralarını aktarır. |
| [Autónavigátor](https://www.autonavigator.hu/) | HU | orta | yalnızca rapor | Macarca yayın. 1.5 dCi için motor yenileyici görüşü içeren yazı (K9K biyel yatağı). |

### Parça ve atölye rehberleri

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [FCP Euro](https://www.fcpeuro.com/blog) | US | orta | 6 | Parça satıcısının adım adım onarım rehberleri. Ticari çıkarı olan bir kaynak. |
| [AutoPartsPro](https://www.autopartspro.co.uk/) | UK | düşük | 3 | Parça satıcısının genel arıza yazıları (SEO ağırlıklı); tek başına yeterli sayılmaz. |
| [BimmerWorld](https://www.bimmerworld.com/) | US | düşük | 2 | Parça satıcısı. Ürün sayfalarındaki arıza anlatımları ticari amaçlı. |
| [Foreign Automotive](https://foreignautomotive.ca/) | CA | düşük | 2 | Kanada'da BMW atölyesi; blog yazıları pazarlama dilindedir. |
| [GoParts](https://www.go-parts.com/) | US | düşük | 1 | Parça satıcısı; OBD kodu ve parça rehberleri ticari amaçlıdır. |
| [HELLA TechWorld](https://www.hella.com/techworld/) | Global | orta | 1 | Parça üreticisinin atölye teknik bültenleri. Üretici (Opel/BMW) belgesi değil. |
| [Mercedes Medic](https://www.mercedesmedic.com/) | US | düşük | 1 | Mercedes şanzıman onarım atölyesi blogu. |
| [Service4Service](https://www.service4service.co.uk/) | UK | düşük | 1 | Şanzıman onarım atölyesi; Dualogic arızalarını anlatıyor. |

## Denenmeye değer ek kaynaklar

Bu çalışmada kullanılmadı ve erişilip doğrulanmadı. İleride eklenebilecek kaynak türleri:

- **KBA (Almanya Federal Motorlu Taşıtlar Dairesi) geri çağırma listesi**: Avrupa'daki resmî geri çağırmalar.
- **ADAC arıza istatistikleri**: Marka ve model bazında yolda kalma verisi (Almanya).
- **TÜV Report**: Alman muayene sonuçlarına dayalı arıza oranları.
- **Which? ve What Car? güvenilirlik anketleri**: Birleşik Krallık'ta sahip anketleri.
- **Fabrika servis bültenleri (TSB) ve VIN ile kampanya sorgusu**: Markanın yetkili servisinden veya NHTSA sayfasından alınabilir.
