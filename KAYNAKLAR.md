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

Toplam 94 farklı site, 404 sorun için kullanıldı.

## Türkçe kaynaklar

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [DonanımHaber Forum](https://forum.donanimhaber.com/) | TR | orta | 376 | Çok sayıda 'kronik sorun var mı' başlığı. Kullanıcı deneyimi; doğruluk başlığa göre değişiyor. |
| [Şikâyetvar](https://www.sikayetvar.com/) | TR | orta | 353 | Kullanıcıların kendi bildirdiği şikâyetler. Oran göstermez; kilometre ve servis yanıtları işe yarıyor. |
| [Araclo](https://www.araclo.com/) | TR | düşük | 143 | Model ve motor başına 'kronik sorunlar' sayfaları. Ticari bir site; sayfalar birbirine çok benziyor, tek başına yeterli sayılmaz. |
| [OTOPARK.COM Forum](https://otopark.com/forum/) | TR | orta | 139 | Marka ve model bazında 'nasıldır / kronik problemleri var mı' başlıkları. Kullanıcı deneyimi; bazı başlıklar eski veya kapalı. |
| [Ekşi Sözlük](https://eksisozluk.com/) | TR | düşük | 103 | Kısa kullanıcı girdileri. İpucu olarak kullanılır, tek başına kanıt sayılmaz. |
| [And Mehmet Çetin](https://andcetin.com/) | TR | orta | 84 | Motor ve şanzıman sorunlarını model ailesi bazında anlatan yazılar. Tek yazarın görüşü; okur yorumları ek bilgi veriyor. |
| [Autopartia](https://autopartia.com/) | TR | düşük | 10 | Yedek parça satıcısı; motor bazlı blog ve 'uzman' sayfaları. Ticari site, belirli bir OEM parçayı sürekli öneriyor; tek başına yeterli sayılmaz. |
| [Carsece](https://www.carsece.com/) | TR | düşük | 10 | Araç rehberi ve bakım blogu. Maliyet tahminlerinin kaynağını göstermiyor; tek başına yeterli sayılmaz. |
| [Drivisual](https://www.drivisual.tv/) | TR | düşük | 8 | Motor bazlı satın alma ve kronik sorun rehberleri (Türkçe ve İngilizce). Tek bir blog; bağımsız kaynakla karşılaştırılmalı. |
| [arabam.com Blog](https://www.arabam.com/blog/) | TR | düşük | 7 | İlan sitesinin blog yazıları. Genel bilgi verir; bazı yazılar motorun 'büyük bir kronik sorunu yoktur' gibi genellemeler içeriyor. |
| [Technopat Sosyal](https://www.technopat.net/sosyal/) | TR | orta | 3 | Teknoloji ve otomobil başlıkları olan Türk forumu; marka ve model bazlı 'kronik sorun var mı' / 'alınır mı' konuları. Kullanıcı deneyimi; doğruluk başlığa göre değişiyor. |
| [YatırımX](https://www.yatirimx.com.tr/) | TR | düşük | 2 | Türkiye'de otomotiv ve ekonomi haberleri; PSA Grubu 1.5 BlueHDi eksantrik zinciri kampanyası haberi için. |
| [Sözcü](https://www.sozcu.com.tr/) | TR | orta | 1 | Ulusal gazete. Burada yalnızca yabancı toplu dava ve geri çağırma haberlerinin Türkçe aktarımı için kullanıldı. |
| [SıfırAraçAl](https://www.sifiraracal.com/) | TR | düşük | 1 | Türkiye'de yeni araç haberleri ve fiyat listeleri; model yenilemeleri ve motor/batarya verileri için. |

## Yurtdışı kaynaklar

### Resmî belgeler ve dava haberleri

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [NHTSA (ABD)](https://www.nhtsa.gov/) | US | yüksek | 22 | Resmî geri çağırma, servis bülteni (TSB) ve şikâyet kayıtları. |
| [Volkswagen Yeni Zelanda](https://www.volkswagen.co.nz/) | NZ | yüksek | 10 | Üretici kampanya sayfası (DQ200 mekatronik ünitesi, kampanya 35E5). Yeni Zelanda pazarı için yayımlanmış; Türkiye'de geçerliliği ayrıca doğrulanmalı. |
| [ClassAction.org](https://www.classaction.org/) | US | orta | 4 | Toplu dava haberleri. Dava iddiaları kanıtlanmış kusur anlamına gelmez. |
| [OCU (İspanya)](https://www.ocu.org/) | ES | orta | 3 | İspanyol tüketici örgütünün Renault motoru için toplu başvuru sayfası. |
| [Top Class Actions](https://topclassactions.com/) | US | orta | 2 | Toplu dava ve uzlaşma haberleri. |
| [Ammons Law Firm](https://www.ammonslaw.com/) | US | düşük | 1 | Hukuk bürosu sayfası. Honda arka lastik aşınması için servis bülteni özetini içeriyor. |
| [MLIT (Japonya Ulaştırma Bakanlığı)](https://www.mlit.go.jp/en/) | JP | yüksek | 1 | Japonya'da resmî geri çağırma bildirimleri; Türkiye kapsamı ayrıca doğrulanmalıdır. |
| [Que Choisir](https://www.quechoisir.org/) | FR | orta | 1 | Fransız tüketici örgütü (UFC-Que Choisir); sahip bildirimlerine dayanan araştırmalar yayımlar. |
| [ÖAMTC](https://www.oeamtc.at/) | AT | yüksek | 1 | Avusturya otomobil kulübü; geri çağırma duyurularını model ve üretim dönemiyle listeler. |

### Forumlar

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [Honest John](https://www.honestjohn.co.uk/) | UK | orta | 44 | Forum ve editör yanıtları ('Ask HJ'). Forum yazıları çoğunlukla 10 yıldan eski olabiliyor. |
| [French Car Forum](https://www.frenchcarforum.co.uk/) | UK | orta | 22 | Peugeot, Citroën ve Renault forumu. |
| [Fiat Forum](https://www.fiatforum.com/) | UK | orta | 20 | Fiat sahipleri forumu (Dualogic, Multijet, Tipo). |
| [Bimmerpost](https://f30.bimmerpost.com/) | US | orta | 17 | BMW F30 ve diğer kasa forumları. |
| [Ford Owners Club](https://www.fordownersclub.com/) | UK | orta | 17 | Ford sahipleri forumu (Focus, Fiesta, EcoBoost). |
| [BRISKODA](https://www.briskoda.net/forums/) | UK | orta | 15 | Škoda sahipleri forumu. |
| [Planète Renault](https://www.planeterenault.com/forum/) | FR | orta | 14 | Fransızca Renault forumu. K9K yatak sorunu için moderatör yazısı bu sitede. |
| [VWVortex](https://www.vwvortex.com/) | US | orta | 13 | Volkswagen forumu. |
| [Vauxhall Owners Network](https://www.vauxhallownersnetwork.co.uk/) | UK | orta | 13 | Vauxhall/Opel sahipleri forumu. |
| [AudiWorld](https://www.audiworld.com/) | US | orta | 10 | Audi forumu ve rehber yazıları. |
| [MBWorld](https://mbworld.org/) | US | orta | 9 | Mercedes-Benz forumu. |
| [Toyota Owners Club](https://toyotaownersclub.com/) | UK | orta | 9 | Toyota sahipleri forumu (Auris/Corolla D-4D). |
| [MB Club UK](https://forums.mbclub.co.uk/) | UK | orta | 8 | Mercedes-Benz sahipleri forumu. |
| [Astra Owners Network](https://www.astraownersnetwork.co.uk/) | UK | orta | 7 | Opel/Vauxhall Astra forumu. |
| [SwedeSpeed](https://www.swedespeed.com/) | US | orta | 7 | Volvo ve Saab sahipleri forumu (XC60, S60, V60 başlıkları). |
| [BenzWorld](https://www.benzworld.org/) | US | orta | 6 | Mercedes-Benz forumu. |
| [Audizine](https://www.audizine.com/) | US | orta | 5 | Audi forumu. |
| [CivicX](https://www.civicx.com/) | US | orta | 5 | Honda Civic (10. nesil) forumu. |
| [Nissan QashQai Forums](https://www.qashqaiforums.co.uk/) | UK | orta | 5 | Nissan Qashqai sahipleri forumu. |
| [Volvo Owners Club Forum](https://www.volvoforums.org.uk/) | UK | orta | 5 | Volvo Owners Club forumu; XC60 / S60 / V60 teknik başlıkları. |
| [Berlingo Forum](https://www.berlingoforum.com/) | UK | orta | 4 | Citroën Berlingo ve PSA dizel (HDi) forumu. |
| [CruzeTalk](https://www.cruzetalk.com/) | US | orta | 4 | Chevrolet Cruze forumu. Konular çoğunlukla ABD'deki 1.4T ve 1.8 motorlar için. |
| [SpeakEV](https://www.speakev.com/) | UK | orta | 4 | İngiltere merkezli elektrikli araç sahibi forumu; Zoe, Peugeot e-208, BYD gibi modellerde 12V akü, şarj ve tahrik arızası konuları. |
| [German Car Forum](https://www.germancarforum.com/) | Global | orta | 3 | Alman markaları forumu. |
| [E90Post](https://www.e90post.com/) | US | orta | 2 | BMW 3 Serisi E90/E92 forumu. |
| [Forum Peugeot](https://www.forum-peugeot.com/) | FR | orta | 2 | Fransızca Peugeot forumu. |
| [8thCivic](https://www.8thcivic.com/) | US | orta | 1 | Honda Civic (8. nesil, FD) forumu. |
| [Ammirati Forum](https://ammirati.org/forum/) | IT | düşük | 1 | İtalyan oto tamircilerinin 'uzman yanıtlıyor' bölümü; hata kodu ve onarım vakaları. Kullanıcı deneyimi. |
| [AudiSRS](https://audisrs.com/) | UK | orta | 1 | Audi ve VAG forumu. |
| [Car Dealer Magazine Forum](https://forum.cardealermagazine.co.uk/) | UK | düşük | 1 | İngiltere'de bayi ve ikinci el satıcılarının forumu; model bazında alım-satım deneyimleri. Kullanıcı görüşü. |
| [ElectricVehicleForums](https://electricvehicleforums.com/) | US | düşük | 1 | Civic Hybrid forumu; Honda 08-001 bülteni aktarımı içeriyor. |
| [Insignia Drivers Forum](https://insignia-drivers.uk/forum/) | UK | orta | 1 | Vauxhall / Opel Insignia sahiplerinin teknik atölye bölümü; yağ basıncı, motor ve şanzıman konuları. Kullanıcı deneyimi. |
| [Kia Forums](https://www.kia-forums.com/) | US | orta | 1 | Kia sahipleri forumu; Sportage 3. nesil (2011-2016) dahil model bölümleri var. |
| [PicoAuto Forum](https://www.picoauto.com/support/) | UK | düşük | 1 | Tanı cihazı üreticisinin destek forumu. |
| [Tesla Motors Club](https://teslamotorsclub.com/) | US | orta | 1 | Tesla sahipleri ve meraklıları forumu (Model 3 / Model Y bölümleri). |

### Şikâyet platformları, sahip anketleri ve derlemeler

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [CarComplaints.com](https://www.carcomplaints.com/) | US | yüksek | 33 | NHTSA şikâyetlerini ve dava haberlerini model yılı bazında derler. Yalnızca ABD pazarındaki araçları kapsar. |
| [Fiches-Auto.fr](https://www.fiches-auto.fr/) | FR | orta | 15 | Sürücü yorumlarından derlenen arıza ve güvenilirlik sayfaları. |
| [AustralianCar.Reviews](https://australiancar.reviews/) | AU | orta | 6 | Model bazında geri çağırma ve arıza listeleri. |
| [Consumer Reports](https://www.consumerreports.org/) | US | yüksek | 6 | Sahip anketlerine dayalı güvenilirlik verisi ve kampanya haberleri. |
| [CarChecker.pro](https://www.carchecker.pro/) | Global | düşük | 3 | Genel amaçlı model raporları; iddialar zayıf kaynaklıdır. |
| [au7o](https://au7o.io/) | Global | düşük | 3 | Arıza kodu ve bilinen sorun derlemesi. |
| [Autoscore](https://autoscore.pro/) | Global | düşük | 1 | Motor kodu bazında arıza listesi ve kaba kilometre tahmini veren derleme site; kaynağı belirtilmiyor, yalnızca destekleyici olarak kullanıldı. |
| [Car-Recalls.eu](https://car-recalls.eu/) | Global | düşük | 1 | Avrupa geri çağırma ve Safety Gate (Rapex) uyarılarını araç bazında derleyen site; resmî veritabanıyla karşılaştırılmadı. |
| [RepairPal](https://repairpal.com/) | US | orta | 1 | Arıza belirtisi ve onarım maliyeti derlemesi. |

### Editör yazıları ve haberler

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [Parkers](https://www.parkers.co.uk/) | UK | orta | 25 | İkinci el alım rehberleri ve haberler. |
| [L'argus](https://www.largus.fr/) | FR | yüksek | 9 | Fransız otomotiv yayını. Güvenilirlik yazıları, tekrarlayan arıza listeleri ve geri çağırma haberleri. |
| [InsideEVs](https://insideevs.com/) | US | orta | 7 | Elektrikli araç haberleri; geri çağırma ve yaygın arıza özetleri. |
| [electrive.com](https://www.electrive.com/) | DE | orta | 6 | Elektrikli araç ve şarj haberleri; Avrupa geri çağırmaları ve KBA kayıtlarına atıflar. |
| [CompleteCar.ie](https://www.completecar.ie/) | IE | düşük | 4 | İrlanda merkezli araç sitesi; okur sorularına yanıt veriyor. |
| [AUTO BILD](https://www.autobild.de/) | DE | yüksek | 3 | Alman otomotiv yayını. Şikâyet sayıları ve üretici açıklamaları. |
| [Caradisiac](https://www.caradisiac.com/) | FR | orta | 3 | Fransız otomotiv yayını. Güvenilirlik dosyaları ve forum bölümü var. |
| [The Connexion](https://www.connexionfrance.com/) | FR | orta | 3 | Fransa haberleri (İngilizce). UFC-Que Choisir'in 1.2 TCe yağ tüketimi uyarısını aktarıyor. |
| [auto motor und sport](https://www.auto-motor-und-sport.de/) | DE | yüksek | 3 | Alman otomotiv dergisi; geri çağırma haberlerinde KBA (Federal Motorlu Taşıtlar Dairesi) bildirimlerine dayanır. |
| [CarGuide.PH](https://www.carguide.ph/) | PH | orta | 2 | Filipinler otomotiv haberleri. BMW geri çağırma duyurusu. |
| [Malay Mail](https://www.malaymail.com/) | MY | orta | 2 | Malezya haber sitesi; Passat 2.0 TDI yağ pompası geri çağırma haberi. |
| [WardsAuto](https://www.wardsauto.com/) | US | orta | 2 | ABD otomotiv sektörü haber ve analiz yayını; üretici kampanyalarını aktarır. |
| [BMW Group Basın](https://www.press.bmwgroup.com/) | Global | yüksek | 1 | Üretici basın duyuruları (geri çağırma ve teknik kampanyalar); kampanyanın varlığı için güvenilir, arıza yaygınlığı kanıtı değildir. |
| [Gebrauchtwagenberater](https://gebrauchtwagenberater.de/) | DE | düşük | 1 | Almanca ikinci el rehberi (Astra K). Resmî bir Opel belgesi değil. |
| [Recharged](https://recharged.com/) | US | düşük | 1 | Elektrikli araç ikinci el alım rehberleri ve model yazıları. |
| [Stellantis Medya](https://www.media.stellantis.com/) | Global | yüksek | 1 | Üretici basın bültenleri (Türkiye bölümü dahil); batarya, güç ve menzil gibi teknik veriler için güvenilir, arıza kanıtı değildir. |
| [Testcoches](https://testcoches.es/) | ES | orta | 1 | İspanyol otomobil haber sitesi; model bazlı arıza ve geri çağırma haberleri. |
| [WheelStreet](https://www.wheelstreet.lt/) | LT | düşük | 1 | Litvanyaca ikinci el rehberi (Passat B6). |
| [autohaus.de](https://www.autohaus.de/) | DE | orta | 1 | Alman otomotiv ticareti yayını; geri çağırma haberlerinde KBA referans numaralarını aktarır. |
| [Autónavigátor](https://www.autonavigator.hu/) | HU | orta | yalnızca rapor | Macarca yayın. 1.5 dCi için motor yenileyici görüşü içeren yazı (K9K biyel yatağı). |

### Parça ve atölye rehberleri

| Site | Ülke | Güvenilirlik | Kullanıldığı sorun sayısı | Not |
| --- | --- | --- | ---: | --- |
| [FCP Euro](https://www.fcpeuro.com/blog) | US | orta | 7 | Parça satıcısının adım adım onarım rehberleri. Ticari çıkarı olan bir kaynak. |
| [AutoPartsPro](https://www.autopartspro.co.uk/) | UK | düşük | 3 | Parça satıcısının genel arıza yazıları (SEO ağırlıklı); tek başına yeterli sayılmaz. |
| [BimmerWorld](https://www.bimmerworld.com/) | US | düşük | 2 | Parça satıcısı. Ürün sayfalarındaki arıza anlatımları ticari amaçlı. |
| [Foreign Automotive](https://foreignautomotive.ca/) | CA | düşük | 2 | Kanada'da BMW atölyesi; blog yazıları pazarlama dilindedir. |
| [Mercedes Medic](https://www.mercedesmedic.com/) | US | düşük | 2 | Mercedes şanzıman onarım atölyesi blogu. |
| [Service4Service](https://www.service4service.co.uk/) | UK | düşük | 2 | Şanzıman onarım atölyesi; Dualogic arızalarını anlatıyor. |
| [GoParts](https://www.go-parts.com/) | US | düşük | 1 | Parça satıcısı; OBD kodu ve parça rehberleri ticari amaçlıdır. |
| [HELLA TechWorld](https://www.hella.com/techworld/) | Global | orta | 1 | Parça üreticisinin atölye teknik bültenleri. Üretici (Opel/BMW) belgesi değil. |

## Denenmeye değer ek kaynaklar

Bu çalışmada kullanılmadı ve erişilip doğrulanmadı. İleride eklenebilecek kaynak türleri:

- **KBA (Almanya Federal Motorlu Taşıtlar Dairesi) geri çağırma listesi**: Avrupa'daki resmî geri çağırmalar.
- **ADAC arıza istatistikleri**: Marka ve model bazında yolda kalma verisi (Almanya).
- **TÜV Report**: Alman muayene sonuçlarına dayalı arıza oranları.
- **Which? ve What Car? güvenilirlik anketleri**: Birleşik Krallık'ta sahip anketleri.
- **Fabrika servis bültenleri (TSB) ve VIN ile kampanya sorgusu**: Markanın yetkili servisinden veya NHTSA sayfasından alınabilir.
