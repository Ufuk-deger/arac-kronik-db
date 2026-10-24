# Kapsam ve ilerleme

Bu dosya `scripts/kapsam_md_uret.py` ile `data/kapsam.json` (plan) ve `data/araclar.json` (veri) içeriğinden üretilir. Elle düzenlemeyin; planı `data/kapsam.json` içinde değiştirip betiği yeniden çalıştırın.

## Ölçüt

- **Zaman penceresi:** Son 10-15 yılın araçları, yani yaklaşık 2011 model yılı ve sonrası. Daha eski yıllar yalnızca ilk aşamada eklenmiş kayıtlarda kaldı (aşağıda ayrıca listelenir).
- **Marka seçimi:** Türkiye'de en çok satılan markalar (aşağıdaki tablo). İlk dört aşamada elektrikli ya da 2023 sonrası girmiş markalar (BYD, Togg, Tesla, Chery) "motor grubu ve ikinci el geçmişi yok" gerekçesiyle dışarıda bırakılmıştı; 5. aşamada elektrikli araçlar kapsama alındı ve bu markalar plana girdi. Bu listenin dışındaki markalar (`ek` kapsamı) ikinci el yaygınlığı ve kaynak bulunabilirliği gözetilerek editoryal olarak eklendi; satış adetleri doğrulanamadı.
- **Elektrikli araçlar:** `motor` alanı elektrik motoru ve batarya sürümünü gösterir (ör. `Elektrik (52,4 kWh ve 88,5 kWh)`). Sorunlar batarya, şarj (OBC, ICCU), 12V akü ve yazılım gibi elektrikli araca özgü parçalara aittir. Geri çağırma kaydı olan sorunlarda Türkiye kapsamı doğrulanamıyorsa bu kayıtta ve plan notunda belirtilir. Aynı batarya ve motor değerlerine sahip kardeş modelin kaynağı yalnızca ilgili kayıtta açıkça belirtilerek kullanılabilir (ör. Astra Electric ve Peugeot e-308). Plug-in hibritler (ör. BYD Seal U DM-i) bu aşamada kapsam dışıdır.
- **Sıralama:** Genelden özele gidilir. Önce her markanın en çok satılan ve en çok sorgulanan modelleri ile ana motor grupları (kademe 1), sonra yaygın ama daha az sorgulananlar (kademe 2), en son niş gruplar (kademe 3).
- **Yıl kırılımı:** Kaynaklar üretim yılına göre fark belirtiyorsa sorun `donem_kirilimi` ile yıl aralıklarına ayrılır (ör. revizyon öncesi ve sonrası).
- **Motor versiyonları:** Kaynaklar iki versiyonu motor kodu, güç, şanzıman ya da kasa/nesil ile ayırt ediyorsa ayrı kayıt açılır (ör. M271 Kompressor ve M271 EVO; N47D16 ve N47D20; Qashqai J11 1.5 dCi ve 1.6 dCi Xtronic). Ayırt etmiyorlarsa kayıt bölünmez, fark metinde ya da `donem_kirilimi` içinde belirtilir ([README](README.md#motor-versiyonları)).
- **Aynı motoru paylaşan modeller:** Motor kaynaklı sorunlar (ör. 1.5 TSI yağ eksiltmesi, 48V hafif hibrit sistem) her modelde ayrı kayıt olarak durur ve yalnızca o modele ait şikâyeti olan modellere yazılır. Modele özgü ikinci site bulunamazsa aynı motoru taşıyan başka modelin kaynağı kullanılabilir; bu durum kaydın `detay` metninde açıkça yazılır ve kayıt doğrudan kanıtı sınırlı sayılır (ör. Karoq ACT titreşimi, Formentor 48V).
- **İlan sayısı kontrolü:** 7. aşamada plan, arabam.com'un aylık ilan sıralamaları ve Cardata listeleriyle karşılaştırıldı (sahibinden.com'un canlı model sayıları okunamadı) ve en çok ilanlı modellerin motor boşlukları kapatıldı. "Çok ilanlı" olmak tek başına kayıt gerekçesi değildir: tekrar eden bir kronik sorun için iki bağımsız kaynak bulunamazsa grup `–` olarak kalır.
- **Çok kullanılan araç denetimi:** 9. aşamada plan, trafikteki araç sayıları (TÜİK verisine dayanan yaklaşık 2024 listeleri) ve ikinci el satış sıralamalarıyla model, nesil ve motor düzeyinde yeniden karşılaştırıldı. Bir satırın `eslesme` parçalarından her biri en az bir kayda denk gelmelidir (test denetler); "1.4 TSI / 1.6 TDI" gibi birleşik bir satırın yalnızca bir parçası kayıtlıysa satır bölünür, böylece ✓ kayıtsız bir motoru gizleyemez. Aranıp eklenmeyen (–) gruplar görüntüleyicide "Arandı ama kayıt açılmayan gruplar" bölümünde nedenleriyle gösterilir.
- **Kanıt eşiği:** Her sorun için en az iki farklı site ve en az bir deneyim/resmî türünde kaynak gerekir ([README](README.md#kaynak-kuralı)). Kaynak bulunamayan gruplar plana `–` olarak işlenir; sorun uydurulmaz.

Kademeler:

- **Kademe 1:** Son 10-15 yılda en çok satılan ve ikinci elde en çok sorgulanan model ve ana motor grupları
- **Kademe 2:** Yaygın ama daha az sorgulanan model ve motor grupları
- **Kademe 3:** Niş, yeni ya da kaynağı az olan gruplar

Model ve motor seçimi 2025 satış sıralaması ve ikinci el pazarındaki yaygınlık gözetilerek editoryal olarak yapılmıştır; kademe atamaları kesin bir sıralama değil, çalışma sırasıdır.

## İlerleme

- Plan: **355** model/motor grubu
- Tamamlanan (✓): **168**
- Araştırılıp eklenmeyen (–): **187**
- Sırada (○): **0**
- Kademe 1: **104/104** işlendi (✓ ya da –)
- Veritabanı: **172** kayıt, **258** kronik sorun

| Marka | Plan | ✓ | – | ○ | Kademe 1 işlenen |
| --- | ---: | ---: | ---: | ---: | ---: |
| Renault | 27 | 15 | 12 | 0 | 8/8 |
| Volkswagen | 37 | 18 | 19 | 0 | 13/13 |
| Toyota | 13 | 4 | 9 | 0 | 5/5 |
| Fiat | 18 | 11 | 7 | 0 | 5/5 |
| Hyundai | 25 | 11 | 14 | 0 | 12/12 |
| Peugeot | 12 | 9 | 3 | 0 | 5/5 |
| Opel | 26 | 14 | 12 | 0 | 5/5 |
| Citroen | 11 | 6 | 5 | 0 | 3/3 |
| BYD | 2 | 1 | 1 | 0 | 1/1 |
| Skoda | 20 | 9 | 11 | 0 | 6/6 |
| Mercedes-Benz | 20 | 10 | 10 | 0 | 6/6 |
| Togg | 2 | 1 | 1 | 0 | 1/1 |
| BMW | 14 | 5 | 9 | 0 | 4/4 |
| Tesla | 2 | 1 | 1 | 0 | 1/1 |
| Nissan | 14 | 8 | 6 | 0 | 4/4 |
| Chery | 2 | 0 | 2 | 0 | 0/0 |
| Ford | 19 | 8 | 11 | 0 | 7/7 |
| Kia | 22 | 9 | 13 | 0 | 6/6 |
| Dacia | 12 | 8 | 4 | 0 | 3/3 |
| Audi | 13 | 6 | 7 | 0 | 4/4 |
| Honda | 9 | 4 | 5 | 0 | 2/2 |
| Seat | 8 | 3 | 5 | 0 | 2/2 |
| Chevrolet | 1 | 0 | 1 | 0 | 0/0 |
| Volvo | 2 | 1 | 1 | 0 | 0/0 |
| Subaru | 1 | 1 | 0 | 0 | 0/0 |
| Mini | 3 | 1 | 2 | 0 | 0/0 |
| Jeep | 2 | 1 | 1 | 0 | 0/0 |
| Alfa Romeo | 2 | 0 | 2 | 0 | 0/0 |
| Mazda | 1 | 0 | 1 | 0 | 0/0 |
| Suzuki | 1 | 0 | 1 | 0 | 0/0 |
| Mitsubishi | 1 | 0 | 1 | 0 | 0/0 |
| Land Rover | 1 | 0 | 1 | 0 | 0/0 |
| Cupra | 2 | 1 | 1 | 0 | 0/0 |
| MG | 3 | 1 | 2 | 0 | 1/1 |
| Lexus | 1 | 0 | 1 | 0 | 0/0 |
| Isuzu | 1 | 0 | 1 | 0 | 0/0 |
| Smart | 1 | 0 | 1 | 0 | 0/0 |
| Porsche | 1 | 1 | 0 | 0 | 0/0 |
| Zeekr | 1 | 0 | 1 | 0 | 0/0 |
| Xpeng | 1 | 0 | 1 | 0 | 0/0 |
| Leapmotor | 1 | 0 | 1 | 0 | 0/0 |

## Markalar

2025 yılında Türkiye'de satılan sıfır otomobil sayısı **1.084.496**. Aşağıdaki sıralama hafif ticari araçlar hariç sıfır otomobil satışlarına göre, ODMD verisini aktaran haberlerden alınmıştır.

| Sıra* | Marka | 2025 otomobil satışı | Kapsam | Not |
| :---: | --- | ---: | --- | --- |
| 1 | Renault | 131.764 | Kapsamda | İki haberde tutarlı. |
| 2 | Volkswagen | 88.682 | Kapsamda | Bir haber 93.682 veriyor. |
| 3 | Toyota | 76.620 | Kapsamda | Bir haber 73.632 veriyor. |
| 4 | Fiat | 71.787 | Kapsamda | İki haberde tutarlı. |
| 5 | Hyundai | 66.261 | Kapsamda |  |
| 6 | Peugeot | 59.798 | Kapsamda |  |
| 7 | Opel | 48.016 | Kapsamda |  |
| 8 | Citroen | 47.818 | Kapsamda |  |
| 9 | BYD | 45.537 | Kapsamda | 2023'te Türkiye'ye girdi. İlk dört aşamada elektrikli ve 2023 sonrası marka olduğu için kapsam dışıydı; 5. aşamada elektrikli modeller kapsama alındı (Atto 3 kayıtlı; Dolphin / Seal araştırıldı, eklenmedi). Plug-in hibrit modeller (Seal U DM-i) kapsam dışı. |
| 10 | Skoda | 45.321 | Kapsamda |  |
| 11+ | Mercedes-Benz | 43.224 | Kapsamda | Rakam tek bir haber tablosundan; doğrulanamadı. |
| 11+ | Togg | 39.020 | Kapsamda | Yalnızca elektrikli ve 2023'te çıktı. İlk dört aşamada kapsam dışıydı; 5. aşamada elektrikli araçlar kapsama alındı ve T10X kaydedildi. |
| 11+ | BMW | 33.992 | Kapsamda | Rakam tek bir haber tablosundan; doğrulanamadı. |
| 11+ | Tesla | 31.509 | Kapsamda | Yalnızca elektrikli. İlk dört aşamada kapsam dışıydı; 5. aşamada elektrikli araçlar kapsama alındı. Model Y kayıtlı, Model 3 araştırıldı ama eklenmedi. |
| 11+ | Nissan | 28.705 | Kapsamda | Rakam tek bir haber tablosundan; doğrulanamadı. |
| 11+ | Chery | 28.579 | Ek kademe | 2023 sonrası yeni marka. 5. aşamada elektrikli Omoda E5 arandı, kaynak bulunamadı; benzinli Omoda 5 elektrikli kapsamının dışında. Rakam doğrulanamadı. |
| 11+ | Ford | — | Kapsamda | Hafif ticari dahil toplamda ilk 5 marka arasında (Ocak-Ağustos 2025'te %7,72 pay). Otomobil adedi doğrulanamadı. |
| 11+ | Kia | 25.420 | Kapsamda | Rakam tek bir haber tablosundan; doğrulanamadı. |
| 11+ | Dacia | 25.405 | Kapsamda | Tek haberde 25.405 olarak geçiyor; Sandero Stepway tek başına 23.699. |
| 11+ | Audi | 24.832 | Ek kademe | Ek kademe: ikinci el pazarındaki yaygınlığı nedeniyle sonra eklenecek. Rakam doğrulanamadı. |
| 11+ | Honda | 16.137 | Ek kademe | Ek kademe: Civic ikinci elde çok sorgulanıyor. Rakam doğrulanamadı. |
| 11+ | Seat | 9.857 | Ek kademe | Ek kademe: Leon ve Ibiza ikinci elde yaygın. Rakam doğrulanamadı. |
| 11+ | Chevrolet | — | Ek kademe | Ek kademe: Cruze kaydı ilk aşamadan; Captiva / Aveo Faz 4'te arandı, kanıt tek rehber sitesinde kaldığı için eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Volvo | — | Ek kademe | Ek kademe: Faz 4'te S60 / V40 1.6 D Powershift eklendi. Satış adedi doğrulanamadı. |
| 11+ | Subaru | — | Ek kademe | Ek kademe: Faz 4'te XV 2.0 yağ tüketimi eklendi. Satış adedi doğrulanamadı. |
| 11+ | Mini | — | Ek kademe | Ek kademe: Faz 4'te Cooper S / Countryman S 1.6 turbo yüksek basınç yakıt pompası eklendi. Satış adedi doğrulanamadı. |
| 11+ | Jeep | — | Ek kademe | Ek kademe: Faz 4'te benzinli / dizel Renegade-Compass arandı, ikinci bağımsız kaynak bulunamadı. Faz 6'da elektrikli Avenger kaydedildi (KBA geri çağırması ve Şikâyetvar). Satış adedi doğrulanamadı. |
| 11+ | Alfa Romeo | — | Ek kademe | Ek kademe: Faz 4'te arandı; motorlara özgü kaynaklı bulgu çıkmadığı için kayıt eklenmedi. Faz 6'da elektrikli Junior arandı; ikinci bağımsız kaynak bulunamadı. Satış adedi doğrulanamadı. |
| 11+ | Mazda | — | Ek kademe | Ek kademe: Faz 4'te arandı; Türkiye'ye özgü kronik sorun kaynağı çıkmadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Suzuki | — | Ek kademe | Ek kademe: Faz 4'te arandı; bulgular tek rehber sitesi ve elektronik şikâyetlerle sınırlı kaldığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Mitsubishi | — | Ek kademe | Ek kademe: Faz 4'te arandı; ikinci bağımsız kaynak bulunamadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Land Rover | — | Ek kademe | Ek kademe: Faz 4'te arandı; ikinci bağımsız kaynak bulunamadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Cupra | — | Ek kademe | Ek kademe: Faz 4'te arandı; şikâyetler tekil kaldığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | MG | — | Ek kademe | Ek kademe: Faz 4'te arandı; HS şanzıman şikâyetleri yalnızca Şikâyetvar'da, model yılı ve sürüm bilgisi doğrulanamadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Lexus | — | Ek kademe | Ek kademe: Faz 4'te arandı; sonuç çıkmadı. Satış adedi doğrulanamadı. |
| 11+ | Isuzu | — | Ek kademe | Ek kademe: Faz 4'te arandı; D-Max anlatıları forum yorumu ve tek rehber sitesiyle sınırlı kaldığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Smart | — | Ek kademe | Ek kademe: 5. aşamada #1 arandı; Türkiye'ye ait sonuç çıkmadı. Satış adedi doğrulanamadı. |
| 11+ | Porsche | — | Ek kademe | Ek kademe: 5. aşamada Taycan yüksek gerilim batarya modülü geri çağırmasıyla eklendi. Satış adedi doğrulanamadı. |
| 11+ | Zeekr | — | Ek kademe | Ek kademe: Faz 6'da arandı; Şikâyetvar'da kayıt çıkmadı, Ekşi Sözlük'te yalnızca tekil yorumlar var. Satış adedi doğrulanamadı. |
| 11+ | Xpeng | — | Ek kademe | Ek kademe: Faz 6'da arandı; Türkiye'ye ait şikâyet kaydı çıkmadı. Satış adedi doğrulanamadı. |
| 11+ | Leapmotor | — | Ek kademe | Ek kademe: Faz 6'da arandı; T03 için tekil şikâyetler var, ikinci bağımsız kaynak çıkmadı. Satış adedi doğrulanamadı. |

\* İlk 10 sıra birden fazla haberde tutarlıdır (Volkswagen ve Toyota için küçük rakam farkları notlandı). 11. sıradan sonrası rakamlar tek bir tablodan alınmış ve ikinci bir kaynakta doğrulanamamıştır; bu yüzden sıra numarası verilmedi ve liste adet sırasındadır. Ford'un otomobil adedi bulunamadı. Kapsamdaki 18 marka bu belirsizliklerden etkilenmez, ancak 11-20. sıradaki markaların kendi aralarındaki sırası kesin değildir. Resmî tablo için ODMD'nin yıllık bülteni esas alınmalıdır.

Pazar verisi kaynakları:

- <https://www.donanimhaber.com/2025-te-turkiye-de-en-cok-satan-otomobiller-belli-oldu--200556>
- <https://www.cnbce.com/otomotiv/2025te-en-cok-satilan-otomobil-modelleri-belli-oldu-turkiyede-en-cok-satin-alinan-otomobil-hangisi-2025te-ne-kadar-clio-satildi-g22597>
- <https://www.ekonomist.com.tr/otomotiv/2025-te-turkiye-de-en-cok-hangi-otomobiller-satildi-satis-listesi-aciklandi-69679>
- <https://www.habergazetesi.com.tr/togg-2025te-elektrikli-arac-satislarinda-birinci-tesla-ve-byd-satis-rakamlari-aciklandi/amp>
- <https://www.odmd.org.tr> (Otomotiv Distribütörleri ve Mobilite Derneği, aylık basın bültenleri)

## Plan ve durum

Durum: **✓** veritabanında kayıtlı, **○** sırada, **–** araştırıldı ama iki bağımsız site bulunamadığı için eklenmedi. Yıllar yaklaşık üretim ya da Türkiye satış yıllarıdır.

### Renault

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Clio 4 | 2013-2019 | 0.9 TCe 90 (H4Bt) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Clio 4 | 2013-2019 | 1.5 dCi 75/90 (K9K) | ✓ 1 sorun |
| 1 | Clio 4 / Captur | 2013-2019 | 1.2 TCe 120 (H5Ft) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Clio 5 | 2019- | 1.0 TCe 90/100 (H4Dt) | ✓ 2 sorun |
| 1 | Megane 3 / Fluence | 2009-2016 | 1.5 dCi (K9K, EDC) | ✓ 3 sorun |
| 1 | Megane 4 | 2016- | 1.3 TCe 140 (H5Ht, EDC) | ✓ 1 sorun |
| 1 | Megane 4 | 2016- | 1.5 Blue dCi 95/115 (K9K) | ✓ 2 sorun |
| 1 | Zoe | 2019- | Elektrik (Z.E. 40 / Z.E. 50) | ✓ 1 sorun |
| 2 | Clio 3 / Clio 4 / Symbol | 2005-2019 | 1.2 16V 75 (D4F) | – eklenmedi: Şikâyetvar'da tek tek soğukta marş uzaması ve klima şikâyetleri var; D4F motoruna özgü tekrar eden bir sorun için iki bağımsız site bulunamadı. |
| 2 | Clio 3 / Symbol | 2008-2013 | 1.5 dCi 70/85/90 (K9K) | ✓ 1 sorun |
| 2 | Kadjar | 2015-2022 | 1.5 dCi 110 (K9K) | ✓ 1 sorun |
| 2 | Kadjar | 2015-2022 | 1.3 TCe 140 (H5H) | ✓ 2 sorun |
| 2 | Megane 3 / Fluence | 2009-2016 | 1.6 16V (K4M, LPG'li dahil) | – eklenmedi: Aramalarda LPG'li K4M supap oturması anılıyor ama iki bağımsız site bulunamadı. |
| 2 | Megane 4 | 2016- | 1.6 SCe 115 (H4M) | – eklenmedi: Aramalarda H4M motoruna özgü arıza çıkmadı; şikâyetler motor tipi belirtmeyen genel Megane 4 konularına (yağ sızıntısı, soğutma, enjeksiyon uyarısı) ve LPG'li araçlara ait. |
| 2 | Megane E-Tech Electric | 2022- | Elektrik (60 kWh) | – eklenmedi: Şikâyetvar'da DC şarjda 'elektrik sistemini kontrol ettirin' uyarısı, şarj ünitesi arızası ve gerçek menzil şikâyetleri var; Ekşi Sözlük ve DonanımHaber'de aynı arızaları doğrulayan bir kaynak çıkmadı (12V akü başlığı Megane II'ye ait). |
| 2 | Scenic 3 / Grand Scenic | 2009-2016 | 1.5 dCi 110 (K9K, EDC) | ✓ 1 sorun |
| 2 | Symbol | 2008-2020 | 1.2 16V 75 (D4F) | – eklenmedi: Aramalarda D4F motoruna özgü tekrar eden sorun çıkmadı; şikâyetler soğukta marş ve klima gibi tekil konularda. Symbol III (2013-2020), Dacia Logan II'nin Türkiye'de Renault adıyla satılan ikizi (Motor1, Wikipedia); 0.9 TCe ve 1.5 dCi sürümleri 'Sandero / Logan / Symbol' kayıtlarında. |
| 2 | Taliant | 2021- | 1.0 TCe 90/100 (H4Dt) | ✓ 1 sorun |
| 3 | Captur | 2013-2019 | 1.5 dCi (K9K, EDC) | ✓ 1 sorun |
| 3 | Kangoo | 2008-2021 | 1.5 dCi (K9K) | – eklenmedi: Kangoo'ya özgü ayrı kaynak yok; K9K enjektör ve EGR anlatıları Clio, Megane ve Duster kayıtlarında ele alındı. |
| 3 | Koleos | 2008- | 2.0 dCi (4x4) | – eklenmedi: Faz 9'da iki sorguyla arandı: Türkçe kaynak çıkmadı; yabancı derlemelerde X-Tronic CVT kayması, dizel 4x4'te arka diferansiyel ve kardan kırılması ile DPF tıkanması anlatılıyor (Koleos II ağırlıklı); anlatılar iki bağımsız kaynağa bağlanamadı. |
| 3 | Laguna 3 | 2007-2015 | 1.5 dCi / 2.0 dCi | – eklenmedi: Faz 9'da iki sorguyla arandı: Türkçe şikâyet ya da forum kaydı çıkmadı; sonuçlar Fransızca sürücü yorumlarına dayanıyor (Fiches-Auto'da 1.5 dCi 110'da biyel kolu kırılganlığı ve enjektör sorunları, 2.0 dCi otomatikte şanzıman-kardan bağlantısı aşınması; Planète Renault'ta tekil enjeksiyon arızası). Kilometre ve tekrar bilgisi yetersiz. |
| 3 | Master / Trafic | 2010- | 2.3 dCi (M9T) | – eklenmedi: M9T için kol yatağı, turbo ve enjektör kanıtı yok; EGR / DPF anlatıları tek rehber sitesinden. |
| 3 | Megane 3 / Fluence | 2009-2016 | 1.6 16V (K4M) | – eklenmedi: K4M için en somut tema bobin arızası ve tek bir forum başlığında; yağ tüketimi ve termostat kaynakları motoru belirtmiyor. |
| 3 | Scenic 3 / Grand Scenic | 2009-2016 | 1.6 16V | – eklenmedi: Faz 9'da arandı: tek bir forum yorumu (2013 tarihli) 1.6 16V'de açı kaydırıcı (VVT) arızasını ve Sagem ateşleme bobinlerini anıyor; ikinci kaynak çıkmadı. 1.5 dCi EDC (şanzıman beyni arızası) ayrı satırda kayıtlandı. |
| 3 | Scenic E-Tech / 5 E-Tech | 2024- | Elektrik | – eklenmedi: Scenic E-Tech ve Renault 5 E-Tech'e özgü arıza kaydı çıkmadı; Şikâyetvar'daki R5 kayıtları kaza sonrası ekspertiz ve kampanya şikâyetleri, E-Tech arızaları ise Megane E-Tech'e ait. |
| 3 | Talisman | 2016-2022 | 1.6 dCi / 1.5 dCi (EDC) | ✓ 1 sorun |

### Volkswagen

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Golf 6 / Jetta | 2008-2013 | 1.6 TDI 90/105 (CAYC) | ✓ 2 sorun |
| 1 | Golf 7 | 2012-2019 | 1.4 TSI 122/140 (EA211) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Golf 7 | 2012-2019 | 1.6 TDI 90/105/110 | ✓ 1 sorun |
| 1 | Passat B7 | 2010-2014 | 1.6 TDI (CAYC) | ✓ 1 sorun |
| 1 | Passat B8 | 2015-2023 | 1.6 TDI | ✓ 2 sorun |
| 1 | Polo 6R / 6C | 2009-2017 | 1.2 TSI 90/105/110 | ✓ 2 sorun, 2 yıl kırılımı |
| 1 | Polo 6R / 6C | 2009-2017 | 1.4 TDI 75/90 (BMT, 3 silindir) | – eklenmedi: Faz 9'da arandı: DonanımHaber'de 2016 model 1.4 TDI 90 PS için enjektör dönüş hortumu kaçağı ve marş sorunu başlığı var; Şikâyetvar'da 2014 model 1.4 TDI'da turbonun dört kez yapıldığı (47.000 TL ödenmiş) ve 2016 modelde 95 bin km'de su eksiltme ile blok çatlağı gibi tekil vakalar çıktı. Otopark'taki Polo turbo başlığı turbo hortumu çatlağı anlatıyor ve motor tipi net değil; her sorun tek siteyle sınırlı kaldı. |
| 1 | Polo AW | 2018- | 1.0 TSI 95/110 | ✓ 1 sorun |
| 1 | Polo AW | 2018- | 1.0 MPI 65/75 | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da turbosuz 1.0 Polo'da 12.000 km'de yağ uyarısı ve yaklaşık 2 litre takviye anlatılıyor (tek vaka, servis normal bulmuş); DonanımHaber'deki rölanti titremesi başlıkları ve DSG şikâyetleri 1.0 TSI'ya ait. MPI 65/75 için tekrar eden sorun çıkmadı. |
| 1 | T-Roc | 2018- | 1.5 TSI 150 (EA211 evo) | ✓ 1 sorun |
| 1 | Tiguan 5N | 2008-2016 | 1.4 TSI 122/150/160 (EA111) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tiguan AD1 | 2016- | 1.5 TSI 150 (EA211 evo) | ✓ 1 sorun |
| 1 | Tiguan AD1 | 2016- | 1.4 TSI 125/150 (ACT) | – eklenmedi: Faz 9'da arandı: Tiguan 1.4 TSI için piston kırılması, titreme ve yağ eksiltme anlatılarının çoğu 2010-2013 (5N) modellere ait; AD1 dönemi için Şikâyetvar'da 2024 model bir Tiguan'da 7-8 bin km'de yağ eksiltme uyarısı (motor tipi belirtilmiyor) ve 2021 model bir Tiguan'da mekatronik kartı arızası gibi tekil kayıtlar var. 5N 1.4 TSI zincir gergisi arızası ve AD1 1.5 TSI yağ eksiltmesi ayrı kayıtlarda. |
| 2 | Caddy | 2010-2015 | 1.6 TDI (EA189) | ✓ 1 sorun |
| 2 | Caddy | 2015-2020 | 2.0 TDI | – eklenmedi: 2.0 TDI için Caddy'ye özgü kaynaklar Şikâyetvar (DPF, AdBlue) ile sınırlı; ikinci bağımsız kaynak bulunamadı. |
| 2 | Golf 7 | 2012-2019 | 1.2 TSI 85/105 | ✓ 1 sorun |
| 2 | Golf 7.5 | 2017-2020 | 1.5 TSI 130/150 (ACT) | – eklenmedi: DonanımHaber'de tek başlık var (Golf 1.5 TSI ACT 150, iki silindir modunda titreme); sahibi 2020 model diyor ve Golf 7.5 / Golf 8 ayrımı yapılamıyor. 'Golf 7 yağ eksiltme sorunu' başlığındaki anlatılar ağırlıkla 1.2 / 1.4 TSI'ya ait; bir başka başlıkta 1.5 TSI 150 Golf sahibi 112 bin km'de DSG kavramasını değiştirdiğini yazıyor (tekil). Aynı motorun ACT titreşimi ve yağ eksiltmesi Karoq ve Passat kayıtlarında ele alındı. |
| 2 | Golf 8 | 2020- | 1.0 eTSI / 1.5 eTSI (48V hafif hibrit) | ✓ 2 sorun, 1 yıl kırılımı |
| 2 | ID.4 / ID.3 / ID.7 | 2022- | Elektrik | – eklenmedi: Ekim 2026'da Avrupa'da ID.3, ID.4, ID.7, ID. Buzz ve Cupra Born'un belirli partilerini kapsayan batarya geri çağırması (%80 şarj sınırı) duyuruldu; ABD'deki ID.4 geri çağırmalarının Zwickau ve Emden üretimi Avrupa araçlarını kapsamadığı yazılıyor, Türkiye'deki araçların kapsamı doğrulanamadı. Türkiye şikâyetleri (navigasyon, bağlantılı hizmetler, tabela okuma uyarısı) farklı konularda ve yalnızca Şikâyetvar ile Ekşi Sözlük'te. |
| 2 | Jetta | 2011-2013 | 1.4 TSI / 1.6 TDI | ✓ 4 sorun, 1 yıl kırılımı |
| 2 | Jetta | 2013-2018 | 1.2 TSI / 1.4 TSI / 1.6 TDI (DQ200 DSG) | ✓ 1 sorun |
| 2 | Passat B7 | 2010-2014 | 2.0 TDI / 1.4 TSI | – eklenmedi: Aramalarda 2.0 TDI'ya özgü tekrar eden sorun çıkmadı; forum yorumlarının çoğu eski PD motorlara (B6) ve DSG'ye ait, enjektör iddiaları tekil. Faz 7'de yeniden arandı: DonanımHaber'de 2.0 TDI için enjektör, EGR, zincir gergisi, turbo ve DPF sıralanıyor ancak kaynaklar PD motorlu B6 ve DSG'ye ait; B7 / B8 2.0 TDI'ya özgü tekrar eden bir sorun için ikinci bağımsız site yok. |
| 2 | Passat B8 | 2015-2023 | 2.0 TDI / 1.4 TSI | – eklenmedi: Aramalarda B8 2.0 TDI için EGR, DPF ya da AdBlue kaynaklı tekrar eden Türkçe kaynak çıkmadı; en çok DSG şikâyeti var (B8 1.6 TDI kaydında). Faz 7'de yeniden arandı: DonanımHaber'de 2.0 TDI için enjektör, EGR, zincir gergisi, turbo ve DPF sıralanıyor ancak kaynaklar PD motorlu B6 ve DSG'ye ait; B7 / B8 2.0 TDI'ya özgü tekrar eden bir sorun için ikinci bağımsız site yok. Faz 8: 1.5 TSI bu satırdan ayrıldı ve kayıtlandı (Passat B8 1.5 TSI 150, yağ eksiltme). |
| 2 | Passat B8 | 2015-2023 | 1.5 TSI 150 (ACT) | ✓ 1 sorun |
| 2 | Passat CC | 2008-2017 | 2.0 TDI / 1.4 TSI (DSG) | – eklenmedi: Faz 9'da arandı: Passat CC'ye özgü kaynak çıkmadı; DSG kavrama / mekatronik, 2.0 TDI yağ tüketimi (2015 model, yaklaşık 500 km'de 1 litre) ve yağ pompası değişimi anlatıları B7 ve sonrası Passat'lara ait (DSG sorunları Passat B8 ve B6 kayıtlarında). |
| 2 | Polo 6R / 6C | 2009-2017 | 1.6 TDI | ✓ 1 sorun |
| 2 | Polo Sedan | 2010-2017 | 1.4 / 1.6 MPI, 1.6 TDI | – eklenmedi: Faz 9'da arandı: Polo Sedan / Vento'ya özgü kaynak çıkmadı; sonuçlar genel Polo şikâyetleri ve DSG ('Hata: Şanzıman', mikro şalter, mekatronik) üzerine; 1.6 benzinli Polo'da zamanlama zinciri ve yağ yakma eğilimi genel bir forum derlemesinde geçiyor. |
| 2 | T-Cross / Taigo | 2019- | 1.0 TSI 95/110 (DSG) | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da sıfır bir T-Cross 1.0 DSG'de acil işletim ve geri vites uyarıları ile 2025 model 1.0 TSI 116 PS DSG'de servisin şanzıman arızasını kullanıcı hatası saydığı bir şikâyet var (tekil vakalar); 1.0 TSI zincir ve yağ tüketimi DonanımHaber'de motor genelinde anılıyor. T-Cross'a özgü ikinci kaynak çıkmadı. |
| 2 | T-Roc | 2018- | 1.0 TSI 115 | – eklenmedi: Faz 9'da arandı: T-Roc yağ eksiltme şikâyetleri 1.5 TSI'ya ve 2022 modellere ait, DSG şikâyetleri genel T-Roc DSG'sine ait; DonanımHaber'de 1.0 TSI zincir ve yağ tüketimi motor genelinde anılıyor. 1.0 TSI 115'e özgü kaynak çıkmadı (yağ eksiltme T-Roc 1.5 TSI kaydında). |
| 2 | Tiguan 5N | 2008-2016 | 2.0 TDI | – eklenmedi: 5N 2.0 TDI'ya özgü turbo, EGR, DPF ya da zincir sorunu için kaynak çıkmadı; sonuçlar 1.4 TSI ve genel Passat 2.0 TDI yorumlarına ait. |
| 2 | Tiguan AD1 | 2016- | 2.0 TDI | ✓ 1 sorun |
| 2 | Touran | 2010-2022 | 1.6 TDI / 2.0 TDI / 1.4 TSI (DSG) | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da Touran için yalnızca 2 şikâyet var (parça temini, antifriz kaçağı); Touran'a özgü ikinci kaynak çıkmadı. DSG ve TDI yağ tüketimi anlatıları VW grubunun geneline ait. |
| 3 | Amarok | 2010- | 2.0 TDI / BiTDI | – eklenmedi: Faz 9'da arandı: DonanımHaber'de 2011 model 2.0 TDI 4x2 bir Amarok'ta yağ basıncı lambası ve yağ pompası değişimi (tek vaka), Şikâyetvar'da 2011 ve 2024 model turbo arızaları var; şanzıman kayıtları V6'ya ait; DPF için kayıt çıkmadı. Aynı sorun iki siteyle doğrulanmadı. |
| 3 | Arteon | 2017- | 1.5 TSI 150 (ACT, DSG) | – eklenmedi: DonanımHaber ve Otopark'ta Arteon 1.5 TSI test ve ilk sürüş başlıkları var, arıza anlatısı yok; Şikâyetvar'daki tek Arteon DSG şikâyeti (2018 model, mekatronik değişiminden sonra şanzıman yağı eksik) 1.5 TSI'ya bağlanamıyor. 1.5 TSI yağ eksiltmesi Karoq ve Passat kayıtlarında ele alındı. |
| 3 | Passat B7 | 2010-2014 | 2.0 TDI (CFFB / CBAB) | – eklenmedi: B7'ye özgü zincir ya da yüksek basınç pompası kaynağı çıkmadı; enjektör anlatıları PD motorlu B6 kaydında. |
| 3 | Passat B9 | 2024- | 1.5 eTSI (48V hafif hibrit, DSG) | – eklenmedi: B9 için bulunan başlıklar plug-in hibrit (E-Hybrid) sürümüne ait; 1.5 eTSI (48V hafif hibrit) için B9'a özgü Şikâyetvar ya da forum kaydı çıkmadı. Aynı 48 V sistem Golf 8, Octavia, Leon, Superb, Formentor ve A3 (8Y) kayıtlarında ele alındı. |
| 3 | Transporter T5 / T6 | 2003- | 2.0 TDI | – eklenmedi: T5 / T6 2.0 TDI için kronik arıza listesi çıkmadı; yalnızca tekil enjektör ve turbo anlatıları. |

### Toyota

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C-HR | 2016- | 1.2 Turbo (8NR-FTS) | – eklenmedi: Yağ yakma ve şanzıman anıları motor tipi belirtilmeden, tek tek vaka; iki bağımsız site bulunamadı. |
| 1 | C-HR | 2016- | 1.8 Hybrid (2ZR-FXE) | – eklenmedi: Hibrit sistem uyarısı dışında tekrar eden mekanik sorun bulunamadı. |
| 1 | Corolla E150 FL / E170 | 2009-2018 | 1.33 Dual VVT-i 99 | ✓ 1 sorun |
| 1 | Corolla E210 | 2019- | 1.5 Dynamic Force (M15A-FKS) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Corolla E210 | 2019- | 1.8 Hybrid (2ZR-FXE) | – eklenmedi: Şikâyetler ses yalıtımı, fren diski paslanması ve 12V akü gibi mekanik olmayan konularda; tekrar eden mekanik sorun bulunamadı. |
| 2 | Auris | 2013-2018 | 1.33 / 1.6 (benzinli) | – eklenmedi: 1.33'te yağ tüketimi ve oksijen sensörü tekil şikâyetler (yağ tüketimi Corolla 1.33 kaydında); 1.6 için kaynak yok. 1.4 D-4D, Faz 4'te ayrı satır ve kayıt olarak eklendi. |
| 2 | Corolla E170 | 2013-2018 | 1.4 D-4D | – eklenmedi: Aramalar E150 ve E170 ayrımı yapmıyor; turbo ve DPF anıları dağınık; enjektör ve yağ tüketimi E150 1.4 D-4D kaydında. |
| 2 | Corolla E170 | 2013-2018 | 1.6 Valvematic (Multidrive S) | – eklenmedi: Şikâyet sitelerinde 1.6 Valvematic ve Multidrive S için tekrar eden bir sorun kümesi bulunamadı. |
| 2 | Yaris | 2011-2019 | 1.33 / 1.5 Hybrid | – eklenmedi: Şikâyetler yeni nesil Yaris Hybrid ve Yaris Cross akü ve garanti konularında; 2011-2019 Yaris için tekrar eden mekanik sorun bulunamadı. |
| 3 | Auris | 2007-2018 | 1.4 D-4D (1ND-TV) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Corolla E150 | 2007-2013 | 1.4 D-4D (1ND-TV) | ✓ 2 sorun, 1 yıl kırılımı |
| 3 | RAV4 / Hilux | 2013- | 2.0 / 2.5 Hybrid / 2.4 D-4D | – eklenmedi: RAV4 için sistematik sorun çıkmadı; Hilux 2.4 DPF / PCS arıza şikâyetleri yalnızca Şikâyetvar'da (ikinci bağımsız kaynak yok). |
| 3 | Yaris / Avensis | 2011- | 1.33 / hibrit / 2.0 D-4D | – eklenmedi: Yaris (1.33, hibrit) ve Avensis 2.0 D-4D için güvenilir bir kronik sorun listesi çıkmadı; yalnızca tekil şikâyetler. |

### Fiat

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Doblo | 2010-2022 | 1.3 / 1.6 Multijet (90/105/120) | ✓ 3 sorun |
| 1 | Egea | 2015- | 1.4 Fire 95 | ✓ 1 sorun |
| 1 | Egea | 2015- | 1.3 Multijet II 95 | ✓ 2 sorun |
| 1 | Egea | 2015- | 1.6 Multijet II 120 | ✓ 3 sorun |
| 1 | Linea | 2007-2015 | 1.3 Multijet (Dualogic) | ✓ 4 sorun |
| 2 | 500 | 2008- | 1.2 Fire / 0.9 TwinAir | ✓ 1 sorun |
| 2 | 500e | 2021- | Elektrik (42 kWh) | – eklenmedi: Şikâyetvar'da şarj sorunları ve batarya arızası (menzil göstergesinin 320 km'den 260 km'ye düşmesi) tekil; DonanımHaber yorumu olumlu, Ekşi Sözlük yorumları ABD'deki eski modellere ait. |
| 2 | 600e | 2024- | Elektrik (54 kWh, 156 PS) | ✓ 1 sorun |
| 2 | Egea | 2016- | 1.6 E-Torq 110 | – eklenmedi: Aramalarda öne çıkan kronik sorun bulunamadı. |
| 2 | Egea Hybrid | 2022- | 1.5 Hybrid 130 (48V hafif hibrit, çift kavramalı) | ✓ 1 sorun |
| 2 | Linea | 2007-2015 | 1.4 Fire / 1.4 T-Jet | – eklenmedi: Dağınık şikâyetler var, tekrar eden bir sorun için iki bağımsız site bulunamadı. |
| 2 | Linea | 2011-2015 | 1.6 Multijet 105 | – eklenmedi: Faz 9'da arandı: Şikâyetvar'ın Linea 1.6 Multijet şikâyetlerinde en çok tekrarlanan konu yolcu hava yastığı bölgesinde göğüs paneli çatlağı ve Blue&Me arızası; sıcak motorda zor çalışma ayrı bir şikâyet. EGR, enjektör ve turbo iddiaları genel motor ailesine ait tek bir DonanımHaber başlığında. 1.4 T-Jet (turbo, yağ eksiltme) için sonuç çıkmadı; Dualogic sorunları Linea 1.3 Multijet kaydında. |
| 2 | Punto Evo / Grande Punto | 2009-2018 | 1.3 Multijet 75/95 | ✓ 2 sorun |
| 2 | Punto Evo / Grande Punto | 2009-2018 | 1.4 Fire 77 | ✓ 2 sorun |
| 3 | Ducato | 2010- | 2.2 / 2.3 MultiJet | – eklenmedi: AdBlue, DPF ve NOx sensörü şikâyetleri yalnızca Şikâyetvar'da; Boxer ve Jumper için ayrı veri çıkmadı. |
| 3 | Fiorino / Qubo | 2008-2020 | 1.3 Multijet | ✓ 3 sorun |
| 3 | Grande Panda Electric | 2025- | Elektrik | – eklenmedi: Şikâyetvar'da şarj ve kilit sorunu sonrası 8 saat yol yardımı beklemek, şarj soketinin erimesi ve teslimde arıza ışığı tekil; tek taramada ikinci bağımsız site çıkmadı. |
| 3 | Linea / Punto | 2007-2015 | 1.4 T-Jet | – eklenmedi: T-Jet'e özgü kaynak çıkmadı; Punto şikâyetleri ağırlıkla direksiyon (EPS) üzerine ve ayrı kayıtta. |

### Hyundai

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Accent Blue | 2015-2019 | 1.6 CRDi 136 (7DCT) | ✓ 1 sorun |
| 1 | Accent Blue | 2011-2019 | 1.4 MPI / 1.6 GDI | – eklenmedi: 1.4 MPI ve 1.6 GDI için tekrar eden sorun bulunamadı (yalnızca tek tek külbütör kapağı yağ kaçağı ve sübap iddiaları). Faz 7'de yeniden arandı: Şikâyetvar'da 1.4 CVT otomatiklerde kalkışta ve rampada çıtırdama ile yetkili serviste çözülemeyen şanzıman arızası şikâyetleri var; forumlarda aynı motorun taksilerde 400-500 bin km sorunsuz gittiği ve şanzıman yağ değişiminin sorunu azalttığı yazılıyor, bağımsız ikinci kaynak çıkmadı; 1.6 GDI için tekrar eden sorun yok. |
| 1 | Accent Blue | 2011-2015 | 1.6 CRDi 128 (manuel / 6 ileri otomatik) | – eklenmedi: Faz 9'da arandı: tekil vakalar (2013 model 1.6 CRDi'da yağ seviyesinin yükselmesi ve enjektör temizliği; LPG sonrası enjektör arızası); DPF ve turbo için yıla özgü güvenilir kaynak yok, DPF konusunda forumlarda görüş ayrılığı var. Şikâyetlerin çoğu otomatik ve 2015-2016 DCT'li sürümlere ait (DCT sorunu Accent Blue 2015-2019 kaydında). |
| 1 | Bayon | 2021- | 1.0 T-GDI 100/120 (7DCT) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Bayon | 2021- | 1.4 MPI 100 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Ioniq 5 / Ioniq 6 | 2022- | Elektrik (E-GMP) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tucson (TL FL) | 2018-2020 | 1.6 CRDi (7DCT) | ✓ 1 sorun |
| 1 | Tucson (TL) | 2015-2020 | 1.6 T-GDI (7DCT) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | i20 | 2020- | 1.0 T-GDI 100/120 (7DCT) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | i20 | 2020- | 1.4 MPI 100 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | i20 (GB) | 2014-2020 | 1.25 / 1.4 MPI, 1.4 CRDi | – eklenmedi: Faz 9'da arandı: i20 şikâyetleri otomatik şanzımanda toplanıyor (tork konvertörlü şanzıman çoğu yorumda sorunsuz, DCT'li BC3 kaydında); 1.4 MPI için forum yorumları sorunsuz diyor, 1.4 CRDi için enjektör, turbo ve silindir kapağı sıralaması genel bir forum listesinden geliyor. Kayıt açılacak kanıt çıkmadı. |
| 1 | i30 | 2012-2020 | 1.6 CRDi | – eklenmedi: Turbo, DPF ve DCT anıları nesilleri karıştırıyor ve dağınık; model/motor bazında tekrar eden sorun için iki bağımsız site bulunamadı. Faz 7'de yeniden arandı: İngiltere forumlarında EGR tereddüdü ve çift kütleli volan, Türkçe kaynaklarda ise 'kronik sorun yok' yorumları ile tekil titreme, DPF ve DCT anıları var; Tucson 1.6 CRDi şikâyetleri i30'a taşınamaz, iki bağımsız site aynı sorunu doğrulamadı. |
| 2 | Elantra | 2011-2020 | 1.6 MPI / 1.6 CRDi | – eklenmedi: Tek bir 7DCT kalkış titremesi şikâyeti dışında tekrar eden sorun bulunamadı. |
| 2 | Kona Electric / Inster | 2021- | Elektrik (39,2 / 64 kWh) | – eklenmedi: Batarya yangını geri çağırması 2017-2020 arası üretimi kapsıyor; Türkiye'de elektrikli Kona'nın resmî satışı Eylül 2021'de başladı ve kapsam doğrulanamadı. Türkiye'deki batarya modülü arızası ve parça bekleme şikâyetleri yalnızca Şikâyetvar'da. Faz 6'da yeniden arandı (2. nesil Kona ve Inster dahil): Inster'de şarj sırasında duman ve teslim günü şarj olmama tekil, Kona'da batarya modülü arızası, parça bekleme ve %81'de şarjın sonlanması yalnızca Şikâyetvar'da; ikinci bağımsız site çıkmadı. |
| 2 | Tucson (NX4) | 2021- | 1.6 CRDi 136 (7DCT) | ✓ 2 sorun |
| 2 | Tucson (NX4) | 2021- | 1.6 T-GDI (7DCT) | – eklenmedi: Faz 9'da arandı: DonanımHaber'de 2025 model 1.6 DCT'li bir Tucson'da 35 bin km'de dişli kırılması anlatılıyor (tek vaka, motor tipi belirtilmiyor); Şikâyetvar'daki Tucson şanzıman şikâyetlerinin çoğu dizel araçlara ait; yağ yakma iddiaları 1.6 GDi ve 6 ileri otomatik konusunda. T-GDI'ya özgü tekrar eden sorun çıkmadı. 7DCT titremesi Tucson NX4 1.6 CRDi kaydında ele alındı. |
| 2 | Tucson (TL) | 2015-2018 | 1.7 CRDi 115/141 | – eklenmedi: Faz 9'da arandı: 1.7 CRDi'ya özgü kaynak çıkmadı; Şikâyetvar'daki Tucson dizel DPF, enjektör ve turbo şikâyetleri 2021 ve sonrası modellere ait. |
| 2 | i20 (PB) | 2009-2014 | 1.4 MPI / 1.4 CRDi | ✓ 1 sorun |
| 2 | i30 | 2012-2020 | 1.4 / 1.6 MPI, 1.0 / 1.4 T-GDI | – eklenmedi: Benzinli motorlar (MPI, T-GDI) için i30'a özgü kronik sorun çıkmadı; aramalar 1.6 CRDi (DPF) ve DCT şikâyetlerine yöneldi ve i30'a özgü olmayan kaynaklardan geldi. |
| 2 | i30 (FD) | 2008-2012 | 1.4 / 1.6 MPI, 1.6 GDI (EPS) | ✓ 1 sorun |
| 2 | ix35 | 2010-2015 | 1.6 GDI / 1.7 CRDi | – eklenmedi: Şikâyetler iç trim, 4x4 şanzıman dişlisi ve LPG'li soğuk çalıştırma gibi tekil konularda; 1.7 CRDi Türkiye'de neredeyse hiç satılmamış. |
| 3 | Elantra / i10 | 2011- | 1.6 MPI otomatik, 1.0 / 1.25 | – eklenmedi: Elantra AD 1.6 MPI ve i10 için kronik motor sorunu çıkmadı; şikâyetler otomatik şanzıman (dizel), direksiyon ve ESP üzerine ve motor hacmi belirsiz. |
| 3 | H-1 / Starex | 2008- | 2.5 CRDi | – eklenmedi: H-1 / Starex 2.5 CRDi için enjektör, turbo ve EGR kanıtı çıkmadı; bulunanlar eski forum yorumları ve diğer modellere ait. |
| 3 | Kona | 2018- | 1.0 T-GDI / 1.6 T-GDI / 1.6 CRDi | – eklenmedi: 1.6 CRDi DCT kalkış titremesi yalnızca Şikâyetvar kayıtlarında; ikinci bağımsız kaynak bulunamadı. Benzer 7DCT kavrama titremesi Tucson, Bayon, i20 (BC3) ve Sportage kayıtlarında ele alındı. |
| 3 | ix35 / Santa Fe | 2010-2018 | 1.7 / 2.0 / 2.2 CRDi | – eklenmedi: ix35 1.7 / 2.0 CRDi ve Santa Fe 2.2 CRDi için model özelinde kaynak çıkmadı; bulunanlar ix35 1.6 GDI için tek rehber sitesi. |

### Peugeot

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | 208 / 2008 / 308 / 3008 | 2014-2021 | 1.2 PureTech (EB2) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | 208 / 2008 / 308 / 3008 | 2012-2021 | 1.6 BlueHDi / e-HDi (DV6) | ✓ 4 sorun |
| 1 | 208 / 2008 / 308 / 3008 / 5008 | 2019- | 1.5 BlueHDi 100/130 (DV5) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | 301 | 2012- | 1.6 HDi / BlueHDi (DV6) | ✓ 3 sorun |
| 1 | e-208 / e-2008 | 2022- | Elektrik (50 kWh; 2024 sonrası 54 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | 308 / 3008 | 2007-2014 | 1.6 THP (EP6) | ✓ 3 sorun, 1 yıl kırılımı |
| 2 | e-3008 / e-5008 | 2024- | Elektrik | – eklenmedi: Şikâyetvar'da 2024 model e-3008 için seyir halinde 'elektrikli çekiş sistemi arızası' uyarısıyla durma ve şarj almama (çekici) şikâyetleri var. İkinci bağımsız site bulunamadı: Ekşi Sözlük ve DonanımHaber yorumları yalnızca gerçek menzil ve şarj eğrisi hakkında; SpeakEV'de batarya boyutu yazmayan tek bir erken e-3008 şikâyeti var; e-3008 / e-5008 için geri çağırma kaydı çıkmadı (ÖAMTC'nin 3008 / 508 kaydı plug-in hibritlere ait). |
| 2 | e-308 | 2023-2025 | Elektrik (54 kWh, 156 PS) | ✓ 1 sorun |
| 3 | 207 / 206 | 2006-2014 | 1.6 VTi (EP6) | – eklenmedi: EP6 zincir uzaması iddiası tek bir rehber sitesine (Araclo) dayanıyor; forum ve şikâyet kaynaklarında doğrulanmadı. |
| 3 | 301 | 2012- | 1.2 VTi / PureTech | ✓ 2 sorun |
| 3 | 508 | 2011-2018 | 1.6 e-HDi 115 (MCP / Auto6R robotize) | ✓ 1 sorun |
| 3 | 508 | 2011-2018 | 1.6 THP / 2.0 HDi | – eklenmedi: 1.6 THP için tek bir kullanıcı 2011-2012 yüksek basınç pompası sorununu anıyor (308/3008 1.6 THP kaydına bakın); 2.0 HDi için kaynak bulunamadı. |

### Opel

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Astra H / J | 2005-2015 | 1.3 CDTI 90/95 (manuel ve Easytronic) | ✓ 4 sorun |
| 1 | Astra J | 2010-2015 | 1.4 Turbo (A14NET) | ✓ 1 sorun |
| 1 | Astra K | 2015-2021 | 1.4 Turbo 125/150 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Corsa D / E | 2006-2019 | 1.3 CDTI 75/95 | ✓ 2 sorun |
| 1 | Mokka | 2012-2019 | 1.4 Turbo (A14NET) | – eklenmedi: Mokka'ya özgü, A14NET'i açıkça belirten tekrar eden bir şikâyet bulunamadı; aynı motor için Astra J ve Astra K kayıtlarına bakın. Faz 7'de yeniden arandı: Mokka şikâyetleri (47.000 km'de triger kayışı, yağ-su karışması, yağ kaçağı) motor tipini belirtmiyor ya da 1.2 PureTech'e ait; A14NET için Mokka'ya özgü kaynak yok. |
| 2 | Astra Electric | 2023-2025 | Elektrik (54 kWh, 156 PS) | ✓ 2 sorun, 2 yıl kırılımı |
| 2 | Astra J | 2013-2015 | 1.6 CDTI 110/136 | ✓ 1 sorun |
| 2 | Astra J | 2010-2015 | 1.6 benzinli atmosferik (Ecotec) | ✓ 1 sorun |
| 2 | Astra K | 2015-2021 | 1.6 CDTI 110/136 | ✓ 1 sorun |
| 2 | Corsa D / E | 2006-2019 | 1.2 / 1.4 benzinli (A12XER, A14XER) | – eklenmedi: Aramalarda A12XER/A14XER için kronik sorun bulunamadı; sonuçlar PureTech'e ait. |
| 2 | Corsa-e / Mokka-e | 2020- | Elektrik (50 kWh; 2024 sonrası Mokka'da 54 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Crossland / Corsa F | 2017- | 1.2 PureTech 83/100/110/130 | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Insignia A | 2014-2017 | 1.6 CDTI 136 | ✓ 2 sorun |
| 2 | Insignia A | 2008-2017 | 2.0 CDTI / 1.6 Turbo / 1.4 Turbo | – eklenmedi: Turbo hortumu sorunu 1.6 CDTI kaydında var; 1.6 Turbo'da zincir ve yağ soğutucusu için motor sürümü belirsiz tekil yorumlar, 2.0 CDTI için tekil kayıt çıktı. |
| 2 | Meriva B | 2010-2017 | 1.3 CDTI / 1.4 benzinli / 1.4 Turbo | – eklenmedi: Faz 9'da arandı: Şikâyetvar'daki Meriva kayıtları 2011 model Meriva B'de hava yastığı geri çağırması ve kapı kaplama parçası üzerine; forum yorumları eski ve genel (1.3 CDTI için çoğunlukla olumlu); 1.4 Turbo için sonuç çıkmadı. Motora özgü tekrar eden sorun çıkmadı. |
| 2 | Mokka | 2012-2019 | 1.6 CDTI | – eklenmedi: Zincir sesi ve otomatik şanzıman şikâyetleri yalnızca Şikâyetvar'da; ikinci bağımsız site bulunamadı. |
| 2 | Mokka B | 2021- | 1.2 PureTech 100/130 (EB2) | ✓ 1 sorun |
| 2 | Zafira Tourer | 2012-2019 | 1.6 CDTI / 2.0 CDTI / 1.4 Turbo | – eklenmedi: Faz 9'da arandı: Şikâyetvar'daki Zafira şikâyetleri elektronik ve uyarı lambaları üzerine; Zafira 2.0 CDTI için tek bir inceleme (sert vites düşürme) var; 1.6 CDTI ve 1.4 Turbo için sonuç çıkmadı. Motora özgü tekrar eden sorun çıkmadı. |
| 3 | Astra J | 2010-2015 | 1.7 / 2.0 CDTI | – eklenmedi: 1.7 ve 2.0 CDTI'ya özgü tekrar eden sorun çıkmadı; sonuçlar 1.6 ve 1.3 CDTI'ya ait. |
| 3 | Corsa D | 2006-2014 | 1.2 / 1.3 CDTI (Easytronic) | ✓ 1 sorun |
| 3 | Crossland | 2017- | 1.5 BlueHDi | – eklenmedi: Crossland şikâyetleri motor beyni ve şanzıman tarafında tekil; 1.5 BlueHDi zincir sorunu Grandland X kaydında ele alındı. |
| 3 | Frontera Electric | 2025- | Elektrik | – eklenmedi: Şikâyetvar'da 112 şikâyet listeleniyor (batarya arızası, uzun servis bekleme, kalkışta geri kayma, fren diski korozyonu); tek taramada ikinci bağımsız site çıkmadı. |
| 3 | Grandland X / Grandland | 2017- | 1.5 BlueHDi | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Insignia A | 2008-2017 | 2.0 CDTI (A20DTH) | – eklenmedi: A20DTH'ye özgü kronik sorun listesi çıkmadı; turbo hortumu şikâyetleri çoğunlukla 1.6 CDTI'a ait ve o kayıtta. |
| 3 | Mokka / Mokka X | 2012-2020 | 1.4 Turbo (A14NET) / 1.6 CDTI | – eklenmedi: Mokka 1.6 CDTI zincir sesi ve otomatik şanzıman (P0741) şikâyetleri yalnızca Şikâyetvar'da; A14NET 1.4 Turbo için Mokka'ya özgü kaynak çıkmadı. |
| 3 | Mokka B | 2021- | 1.5 BlueHDi 110 (DV5) | – eklenmedi: Faz 9'da arandı (tek sorgu, PureTech ile birlikte): Mokka B 1.5 BlueHDi'ya özgü kaynak çıkmadı; forumlarda AdBlue ve DPF sorunları PSA 1.5 BlueHDi'nın geneli için anılıyor. Aynı DV5 motorunun AdBlue ve eksantrik zinciri sorunları Peugeot, Citroën ve Opel Grandland kayıtlarında. |

### Citroen

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C-Elysee | 2012-2020 | 1.6 HDi / BlueHDi (DV6) | ✓ 3 sorun |
| 1 | C3 | 2016-2022 | 1.2 PureTech 82/110 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | C3 / C4 / C5 Aircross | 2019- | 1.5 BlueHDi 100/130 (DV5) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | C-Elysee | 2017-2020 | 1.2 PureTech 82 | ✓ 1 sorun |
| 2 | C-Elysee | 2012-2016 | 1.6 VTi 115 (EP6) | – eklenmedi: Faz 9'da arandı (tek sorgu): şikâyet ya da forum kaydı çıkmadı; sonuçlar teknik özellik ve katalog sayfalarından oluştu. C-Elysée 1.6 HDi ve 1.2 PureTech 82 ayrı kayıtlarda. |
| 2 | C3 | 2009-2016 | 1.4 HDi / 1.6 HDi | – eklenmedi: Enjektör ve turbo anıları tekil ve eski forum yazıları; uzun dönem bir kullanıcı turbo arızasını 230.000 km'de, enjektör revizyonunu 310.000 km'de bildiriyor; kronik sorun için yeterli kanıt yok. |
| 2 | C4 Cactus | 2014-2020 | 1.2 PureTech 82/110 | ✓ 1 sorun |
| 2 | ë-C4 / ë-C4 X | 2021- | Elektrik (50 kWh; 2024 sonrası 54 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Berlingo / Partner | 2008-2018 | 1.6 HDi (DV6) | – eklenmedi: Turbo yağ besleme borusu tıkanıklığı tek bir forum yanıtına dayanıyor; Şikâyetvar'daki Berlingo kayıtları ağırlıkla 1.5 BlueHDi zinciri (ayrı kayıtta). |
| 3 | C4 / C4 Picasso | 2010-2018 | 1.6 e-HDi (MCP robotize şanzıman) | – eklenmedi: MCP şanzıman için forum görüşleri karışık ('anlatıldığı kadar kötü değil'), kilometre ve maliyet verisi yok; aynı şanzıman 508 kaydında ele alındı. |
| 3 | ë-C3 | 2025- | Elektrik | – eklenmedi: Şikâyetvar'da sıfır km araçlarda çekiş sistemi uyarısı, şarj soketinin kilitlenmesi ve şarj sırasında bataryadan ses gelmesi tekil; tek taramada ikinci bağımsız site çıkmadı. |

### BYD

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Atto 3 | 2023- | Elektrik (60,4 kWh) | ✓ 1 sorun |
| 2 | Dolphin / Seal / Seal U / Sealion 7 | 2024- | Elektrik | – eklenmedi: Şikâyetvar'da şarj kapağının açılmaması, ani şarj düşüşü, uygulama ve dijital anahtar sorunları tekil; ikinci site yok. Faz 6'da Seal U (elektrikli), Sealion 7 ve Atto 2 de arandı: şarj yüzde 25'teyken uyarısız durma, güç kaybı uyarısı, gerçek menzil ve batarya soğutma radyatörü garanti reddi tekil; Atto 2 için kayıt çıkmadı. 12V akü sorunu Atto 3 kaydında. |

### Skoda

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Octavia A5 | 2008-2013 | 1.2 TSI 105 (EA111) | ✓ 2 sorun |
| 1 | Octavia A5 / A7 | 2010-2020 | 1.6 TDI 105/110 (DSG DQ200) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Octavia A7 | 2013-2020 | 1.4 TSI (EA211, DSG DQ200) | ✓ 3 sorun, 1 yıl kırılımı |
| 1 | Rapid | 2012-2019 | 1.2 TSI 90/105 | ✓ 1 sorun |
| 1 | Rapid | 2012-2019 | 1.6 TDI 90/105 | ✓ 1 sorun |
| 1 | Rapid | 2012-2019 | 1.6 MPI 105 | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da DSG vites geçişi şikâyeti (garanti dışı 30.000 TL teklif) ve DonanımHaber'de 2014 model dizel Rapid'de vites boşa düşmesi var, ikisi de otomatik şanzımanlı araçlara ait; yağ eksiltme şikâyetinde model ve motor belirtilmiyor; Ekşi Sözlük'te manuel 1.6 105 bg için olumlu bir yorum çıktı. Manuel 1.6 MPI'ya özgü sorun çıkmadı. DSG sorunları Rapid 1.2 TSI ve 1.6 TDI kayıtlarında. |
| 2 | Fabia | 2014-2021 | 1.0 MPI / 1.2 TSI / 1.4 TDI | – eklenmedi: Fabia için motor bazında tekrar eden sorun çıkmadı (1.4 TDI kavrama/volan, 1.2 krank keçesi ve 1.0 direksiyon uyarısı gibi tekil iddialar). |
| 2 | Kamiq / Scala | 2019- | 1.0 TSI 95/115 | ✓ 1 sorun |
| 2 | Karoq | 2017- | 1.5 TSI 150 (ACT) | ✓ 2 sorun |
| 2 | Karoq | 2017- | 2.0 TDI | – eklenmedi: Şikâyetler Şikâyetvar'daki tekil kayıtlarla sınırlı (DSG acil işletim / mekatronik, yağ eksiltme); bağımsız ikinci kaynak yok. Aynı motor ailesi Tiguan 1.5 TSI ve DQ381 kayıtlarında ele alındı. Karoq 1.5 TSI ayrı satırda kayıtlandı (Faz 8). |
| 2 | Kodiaq | 2017- | 1.5 TSI / 2.0 TDI | – eklenmedi: Kodiaq için motor bazında tekrar eden sorun çıkmadı: Şikâyetvar'da su alma, AKF valf hortumu çatlağı, start-stop uyarısı, mekatronik / şanzıman acil işletim ve yazılım şikâyetleri var ve çoğunda motor tipi belirtilmemiş; 2020 model bir 1.5 Elite sahibi bagajdan su aldığını yazıyor. Aynı motorun yağ eksiltmesi ve ACT titreşimi Karoq 1.5 TSI kaydında ele alındı (Faz 8). |
| 2 | Octavia A7 | 2013-2020 | 1.2 TSI / 1.6 MPI / 2.0 TDI | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da DSG 'aracı P konumunda terk edin' uyarısı, mekatronik değişimi ve mikro şalter anlatılıyor; DonanımHaber'de 1.6 TDI için şakırdama, Ekşi Sözlük'te VAG DSG ve TDI geneli için kronik listesi var. 1.2 TSI, 1.6 MPI ve 2.0 TDI için motor bazında liste çıkmadı (DSG sorunları Octavia 1.6 TDI ve 1.4 TSI kayıtlarında). |
| 2 | Octavia A7 / A8 | 2018- | 1.0 TSI / 1.5 TSI | ✓ 2 sorun |
| 2 | Superb III | 2015-2023 | 1.4 TSI / 1.5 TSI / 1.6 TDI / 2.0 TDI | – eklenmedi: 1.4 TSI, 1.6 TDI ve 2.0 TDI için tekil şikâyetler çıktı (arıza lambası, start-stop); 1.6 TDI DSG kavrama sorunu Octavia ve Rapid kayıtlarında. Faz 8'de 1.5 TSI ACT (2019-2023) de arandı: Superb 1.5 TSI şikâyetleri (48V, yağ eksiltme, titreme) 2024 sonrası Superb IV'e ait; III kuşak 1.5 TSI için ayrı kaynak çıkmadı. Superb IV ayrı satırda kayıtlandı. |
| 2 | Superb IV | 2024- | 1.5 TSI MHEV (48V hafif hibrit, DSG) | ✓ 2 sorun |
| 3 | Enyaq / Elroq | 2021- | Elektrik | – eklenmedi: Elroq için Şikâyetvar'da tabela okuma uyarısı, Türkiye'de kapalı uygulama ve menzil şikâyetleri var; Enyaq için doğrudan kayıt çıkmadı. İkinci bağımsız kaynak yok. |
| 3 | Fabia / Superb | 2015- | 1.2 TSI DSG, 2.0 TDI | – eklenmedi: Fabia 1.2 TSI DSG ve Superb 2.0 TDI için yalnızca tekil Şikâyetvar kayıtları ve genel DSG anlatıları; Fabia 1.4 TDI için sonuç çıkmadı. |
| 3 | Kamiq / Scala | 2019- | 1.5 TSI 150 (ACT) | – eklenmedi: Kamiq ve Scala şikâyetleri (4 ayda 4 kez şanzıman uyarısı, 12.000 km'de yağ seviyesi uyarısı, titreşim) 1.0 TSI araçlara ait görünüyor; 1.5 TSI 150 için modele özgü kaynak çıkmadı. 1.0 TSI DSG sorunları Kamiq / Scala 1.0 TSI kaydında. |
| 3 | Superb II | 2008-2015 | 1.6 TDI / 2.0 TDI / 1.8 TSI | – eklenmedi: Faz 9'da iki sorguyla arandı: Şikâyetvar ya da DonanımHaber kaydı çıkmadı; Araclo'nun Superb II sayfaları (1.6 TDI'da enjektör, 2.0 TDI'da DSG mekatronik valf burcu ve yüksek basınç pompası, 1.8 TSI'da zincir ve DSG) ve yabancı rehberler var; deneyim türünde (şikâyet / forum) kaynak yok, Araclo tek başına yeterli sayılmıyor. |
| 3 | Yeti | 2009-2017 | 1.2 TSI / 1.4 TSI / 1.6 TDI | – eklenmedi: 1.2 TSI zincir iddiaları eski ve tekil (ayrıntısı Octavia A5 1.2 TSI kaydında); DSG görüşleri çelişkili. |

### Mercedes-Benz

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C Serisi W204 | 2007-2014 | C220 / C250 CDI 2.1 (OM651) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | C Serisi W205 | 2014-2021 | C180 / C200 benzinli (M274) | – eklenmedi: Kaynaklar M274'ü zincir konusunda M271'e göre daha sorunsuz buluyor; belirgin kronik sorun yok (7G-Tronic için dağınık şikâyetler var). |
| 1 | C Serisi W205 | 2014-2021 | C180d / C200d 1.6 (R9M kaynaklı dizel) | ✓ 1 sorun |
| 1 | E Serisi W212 | 2009-2016 | E200 / E250 CGI 1.8 turbo (M271 EVO) | ✓ 1 sorun |
| 1 | E Serisi W212 | 2009-2016 | E250 CDI 2.1 (OM651) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | EQA / EQB | 2021- | Elektrik (70,5 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | A Serisi W176 | 2012-2018 | A180 CDI (dizel) | ✓ 1 sorun |
| 2 | A Serisi W176 | 2012-2018 | A200 CDI / A180 1.6 benzinli (enjektör, 7G-DCT) | – eklenmedi: Enjektör ve 7G-DCT iddiaları için güçlü kanıt bulunamadı; tekrarlayan şikâyet Pre-Safe / açı sensörü (CLA ile birlikte ele alındı). |
| 2 | A Serisi W177 | 2018- | A180 1.3 / A180d 1.5 / A200 | – eklenmedi: Faz 9'da arandı: W177'ye özgü kaynak çok az; 7G-DCT vuruntu ve geri vites uyarısı ile PRE-SAFE / ESP uyarıları çoğunlukla W176 dönemine ait (A Serisi / CLA W176 kaydı), MBUX ekranına özgü kronik sorun bulunamadı; 1.3 benzinli ve 1.5 dizel için kaynak çıkmadı. |
| 2 | C Serisi W203 / W204 | 2002-2010 | C180 / C200 Kompressor 1.8 (M271) | ✓ 2 sorun |
| 2 | C Serisi W204 | 2009-2014 | C180 / C200 / C250 CGI 1.8 turbo (M271 EVO) | ✓ 1 sorun |
| 2 | C Serisi W205 | 2014-2021 | C220d 2.0 (OM651 / OM654) | – eklenmedi: C220d (OM651 / OM654) için W205'e özgü kaynak bulunamadı; bulunan şikâyetler C200d (R9M) NOx / AdBlue / turbo yağ kaçağı üzerine ve ayrı kayıtta. |
| 2 | E Serisi W213 | 2016- | E180 / E200 / E220d | – eklenmedi: W213 için sistematik veri yok; Şikâyetvar'da tekil SBC fren, ekran ve direksiyon şikâyetleri var ve bir kısmı W212 / W214'e ait. |
| 2 | EQC | 2019-2023 | Elektrik (80 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | B Serisi W246 | 2011-2018 | B180 / B200 CDI / 1.5 d | – eklenmedi: Faz 9'da iki sorguyla arandı: Türkçe şikâyet ya da forum kaydı çıkmadı; Carchecker ve Au7o'daki rehber ve ABD sahip raporları OM651 dizelde DPF-EGR tıkanması ve 7G-DCT'de kalkış titreşimi gösteriyor (A Serisi / W176 kaydındaki bulgularla örtüşüyor); DonanımHaber'de bir kullanıcı B200'ün 7G-DCT'sinin sorunsuz olduğunu yazıyor. |
| 3 | CLA | 2013-2019 | 180 CDI (dizel) | ✓ 1 sorun |
| 3 | EQE / EQS | 2022- | Elektrik | – eklenmedi: Şikâyetvar'da EQS için şarj almama ve yolda kalma, EQE için menzil kaybı şikâyetleri tekil. NHTSA 24V372 (EQE / EQS batarya yönetimi yazılımı, sürüş gücü kaybı) ABD'deki araçlara ait ve Türkiye şikâyetleriyle aynı belirtiyi göstermiyor. DonanımHaber'de 'Mercedes EQE ve EQS Kullanıcı Deneyimleri' başlığı var ancak eşleşen bir arıza çıkmadı. |
| 3 | GLA | 2013-2019 | 1.5 d / 1.6 / 2.0 (OM607 / M270 / M274) | – eklenmedi: GLA'ya özgü ayrı kaynak bulunamadı; DonanımHaber'deki Pre-Safe başlığı GLA'yı da anıyor, kapsam A Serisi / CLA kaydında. |
| 3 | GLC / GLA | 2013- | 220d / 200 / 250 | – eklenmedi: Faz 9'da iki sorguyla arandı: Şikâyetvar'da 2020 model bir GLC 220d'nin yolda kalması ve şanzıman arızası şikâyeti var (tek vaka); Araclo'nun GLC 200 ve GLA 200 sayfaları 9G-Tronic sarsıntısı ve GLA'da çift kavramalı şanzıman başlığını gösteriyor; yabancı rehberler OM651'de EGR kurumu ve NOx / AdBlue arızalarını sayıyor. Türkçe deneyim kaynağı tek vakada kaldı. |
| 3 | Vito / Sprinter | 2010- | 2.2 CDI (OM651) | – eklenmedi: OM651 anlatıları C ve E Serisi kayıtlarında; Vito ve Sprinter'a özgü ayrı kaynak yok. |

### Togg

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | T10X | 2023- | Elektrik (52,4 / 88,5 kWh) | ✓ 3 sorun |
| 2 | T10F | 2025- | Elektrik | – eklenmedi: Şikâyetvar'da T10F için yüzlerce şikâyet listeleniyor (AC şarj almama / OBC, 12V akü, yazılım donması, Trugo soketinin takılması). DonanımHaber ve Ekşi Sözlük'te T10F'ye özgü eşleşen kayıt çıkmadı: 12V akü ve enerji sistemi başlıkları T10X'e ait (T10X kaydında), T10F için yalnızca test sürüşüne dayanan bir yazılım yorumu var. T10F'nin T10X ile aynı sürücü paketi ve yazılımı paylaştığı kaynakla doğrulanamadı. |

### BMW

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | 1 Serisi F20 | 2011-2019 | 116i / 118i (N13 / B38) | ✓ 8 sorun |
| 1 | 3 Serisi F30 | 2012-2015 | 320d 2.0 (N47) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | 3 Serisi F30 | 2012-2015 | 320i / 328i 2.0 (N20) | ✓ 3 sorun, 1 yıl kırılımı |
| 1 | 3 Serisi F30 | 2015-2019 | 320d (B47) / 320i (B48) | – eklenmedi: Kaynaklar B47'nin N47 sorunlarını büyük ölçüde çözdüğünü yazıyor ama çelişkili; B48 zincir/turbo yağ terlemesi tek kaynakta kaldı. |
| 2 | 1 Serisi F20 | 2011-2015 | 116d 1.6 (N47D16) | ✓ 1 sorun |
| 2 | 1 Serisi F20 | 2011-2019 | 118d 2.0 (N47D20 / B47) | – eklenmedi: 118d / B47 için F20'ye özgü ayrı kaynak bulunamadı; N47D20 zincir sorunu 320d ve 520d kayıtlarında ele alındı. |
| 2 | 5 Serisi F10 | 2010-2015 | 520d 2.0 (N47D20) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | 5 Serisi F10 | 2010-2017 | 520i (N20) / 520d (B47) | – eklenmedi: N20 520i için zincir sorununa dair kaynak çıkmadı; B47 için yalnızca N47'den daha sorunsuz olduğunu yazan tekil forum görüşleri var. |
| 2 | iX / iX1 / iX3 / i4 | 2021- | Elektrik | – eklenmedi: Şikâyetvar'da hızlı şarjta düşük güç, şarj kapağı kilidi ve şarj soketi arızaları tekil; DonanımHaber'de yalnızca i4 menzil göstergesi tartışması var, ortak bir örüntü doğrulanamadı. NHTSA kayıtlarında iX / i4 için batarya (22V-541), birleşik şarj ünitesi (23V-449) ve 2024 i4 modül kaynak dikişi (24V-135) geri çağırmaları var; Türkiye kapsamı doğrulanamadı. |
| 3 | 1 Serisi F40 / X1 F48 | 2015- | 116d / 118i / sDrive16d / 18i | – eklenmedi: Faz 9'da arandı (tek sorgu): Türkçe şikâyet ya da forum kaydı çıkmadı; bir Türkçe alım rehberi zincir / Valvetronic sorunlarının E84'ün 2.0 motoruna ait olduğunu, F48 18i'nin 1.5 üç silindirli turbo olduğunu yazıyor; AUTO BILD TÜV testi geri çağırmaları sıralıyor (EGR sızıntısı, airbag ateşleme, DKG bağlantıları). |
| 3 | 3 Serisi E90 / 5 Serisi E60 | 2005-2013 | 316i / 318i / 320i (N46 / N52), 520i | – eklenmedi: N46 / N52'ye özgü ayrıntılı kaynak çıkmadı; soğutma sistemi ve yağ kaçağı anlatıları tekil. N47 zincir sorunu ayrı kayıtlarda. |
| 3 | X1 / X3 | 2010-2018 | 1.8d / 2.0d (N47 / B47) | – eklenmedi: X1 / X3 için modele özgü kaynak çıkmadı; N47 zincir sorunu 320d, 116d ve 520d kayıtlarında ele alındı. |
| 3 | X3 / X5 | 2010- | xDrive 25d / 30d / 3.0d | – eklenmedi: Faz 9'da iki sorguyla arandı: Türkçe şikâyet ya da forum kaydı çıkmadı; Araclo sayfaları ve yabancı rehberler N57 zincir gergisi aşınması, EGR soğutucusu ve DPF'yi anıyor (bazı rehberler zincir sorununu asıl N47'ye bağlıyor); deneyim türünde kaynak yok. |
| 3 | i3 | 2014-2022 | Elektrik | – eklenmedi: Türkiye'deki i3'lerde range extender bulunmadığı yazılıyor; batarya kapasite kaybı (5 yılda %30'dan fazla) ve batarya testi ücreti tek bir Şikâyetvar kaydında, menzil yorumları Ekşi Sözlük'te; tekrar eden arıza örüntüsü çıkmadı. |

### Tesla

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Model Y | 2023- | Elektrik (Standart / Uzun Menzil / Performans) | ✓ 2 sorun |
| 2 | Model 3 | 2019- | Elektrik | – eklenmedi: Model 3'e özgü kaynak çıkmadı: Şikâyetvar'daki sonuçlar Model Y ve Wall Connector şarj cihazına ait; forum yorumları lastik basınç sensörü, stop lambasında su buharı ve bagaj kapağı gibi tekil konularda. |

### Nissan

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Juke | 2010-2019 | 1.6 (CVT Xtronic) | ✓ 1 sorun |
| 1 | Juke | 2014-2019 | 1.2 DIG-T 115 (HRA2DDT) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Qashqai J11 | 2014-2020 | 1.5 dCi 110 (K9K) / 1.6 dCi 130 (R9M) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Qashqai J11 | 2014-2021 | 1.2 DIG-T (HRA2DDT, Xtronic) | ✓ 3 sorun, 2 yıl kırılımı |
| 2 | Juke | 2010-2019 | 1.5 dCi 110 (K9K) | – eklenmedi: Juke 1.5 dCi için kaynak ağırlıkla tek bir rehber (Araclo); turbo yağ borusu ve DPF anlatıları ikinci bağımsız kaynakla desteklenmedi. K9K turbo hortumu sorunu Qashqai J11 kaydında. |
| 2 | Micra | 2010-2017 | 1.2 (CVT otomatik) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Micra | 2013-2019 | 0.9 IG-T | – eklenmedi: 0.9 IG-T motoruna özgü kronik sorun sonuçlarda yer almadı; şikâyetler 1.2 CVT'de toplanıyor. |
| 2 | Qashqai J10 | 2007-2013 | 1.5 dCi / 1.6 | – eklenmedi: J10 dönemine (2007-2013) özgü kaynak bulunamadı; Qashqai 1.5 dCi turbo hortumu şikâyetleri 2012 model ve sonrasında yoğunlaşıyor, J11 kaydında ele alındı. |
| 2 | Qashqai J11 | 2014-2020 | 1.6 dCi 130 (R9M, Xtronic CVT) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Qashqai J11 FL / J12 | 2019- | 1.3 DIG-T 140/158 (2021 sonrası 12V hafif hibrit, Xtronic CVT) | ✓ 2 sorun, 1 yıl kırılımı |
| 3 | Leaf | 2019- | Elektrik | – eklenmedi: Türkiye'ye özgü kaynak çıkmadı (yalnızca bir Ekşi Sözlük yorumu: aktif batarya soğutması yok, CHAdeMO). Hava soğutmalı bataryanın kapasite kaybı InsideEVs, MyNissanLeaf ve Electrek'te belgeli, ancak bunlar ağırlıkla ABD'nin sıcak iklimine ve ilk nesil Leaf'e ait. NHTSA 24V-700 geri çağırması ABD'de Smyrna'da üretilen 2019-2020 Leaf'leri kapsıyor (CHAdeMO hızlı şarjda yangın riski); Türkiye kapsamı doğrulanamadı. |
| 3 | Navara | 2010- | 2.5 dCi | – eklenmedi: Enjektör ve turbo şikâyetleri yalnızca Şikâyetvar'da; ikinci bağımsız kaynak çıkmadı. |
| 3 | Note | 2013- | 1.2 / 1.5 dCi | – eklenmedi: Note 1.2 / 1.5 dCi için ilgili şikâyet bulunamadı (aramada yalnızca X-Trail 1.6 dCi öne çıktı). |
| 3 | X-Trail T32 | 2014-2021 | 1.6 dCi (R9M, Xtronic CVT) | ✓ 1 sorun |

### Chery (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 2 | Tiggo 7 Pro / Tiggo 8 Pro / Omoda 5 | 2023- | 1.6 TGDI (7DCT) / 1.5 T | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da Tiggo 8 Pro için yağ soğutucusu arızası ve motor suyuna yağ karışması (30.116 km ve 1.500 km gibi tek tek vakalar) ile Tiggo 8 Pro Max'te 30.000 km sonrası şanzıman vuruntusu anlatılıyor; DonanımHaber ve Ekşi Sözlük'te bu iddialar doğrulanmadı (Tiggo 7 Pro 7DCT için olumlu yorumlar, 1.6 TGDI için yakıt tüketimi tartışması; motor suyuna yağ karışmasını anlatan bir DonanımHaber başlığı model belirtmiyor). |
| 3 | Omoda E5 | 2024- | Elektrik | – eklenmedi: Omoda E5 için şikâyet bulunamadı; çıkan sonuçlar benzinli Omoda 5'e (akü bitmesi, ekran ve yazılım) ait ve elektrikli kapsamının dışında. |

### Ford

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Fiesta | 2008-2017 | 1.4 / 1.6 TDCi | ✓ 3 sorun |
| 1 | Fiesta / Focus | 2012-2023 | 1.0 EcoBoost | ✓ 2 sorun, 2 yıl kırılımı |
| 1 | Fiesta Mk7 | 2011-2017 | 1.6 Ti-VCT 105 (Powershift DPS6) | ✓ 1 sorun |
| 1 | Focus 2 / 3 | 2008-2018 | 1.6 TDCi (DV6) | ✓ 3 sorun |
| 1 | Focus 3 | 2011-2018 | 1.6 Ti-VCT (Powershift DPS6) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Focus 3 | 2011-2018 | 1.5 TDCi 95/120 | – eklenmedi: Enjektör ve DPF şikâyetleri dağınık, DPF şikâyetleri ağırlıkla 2019 sonrası EcoBlue'ya ait; 2015-2018 1.5 TDCi için ortak sorun yok. Faz 7'de yeniden arandı: Türkçe kaynaklar 1.6 TDCi ve 2019 sonrası EcoBlue'ya ait; Mk3 1.5 TDCi için yalnızca Ford Owners Club'da (İngiltere) DPF, EGR ve çalışma sorunu konuları var, ikinci bağımsız Türkçe kaynak çıkmadı. |
| 1 | Focus 4 / Kuga 3 | 2019- | 1.5 EcoBlue 120 (DV5) | ✓ 2 sorun |
| 2 | C-Max / Grand C-Max | 2010-2019 | 1.6 TDCi / 1.5 TDCi / 1.0 EcoBoost | – eklenmedi: Faz 9'da arandı: DonanımHaber'de 2011 model C-Max 1.6 TDCi'da enjektör arızası (tek başlık, bir enjektör için yaklaşık 1.230 TL teklif), Şikâyetvar'da 2012 model 1.6 TDCi'da enjektör pulu değişiminden sonra motor arızası (tek vaka); turbo boru / hortum ve DPF yorumları genel 1.6 TDCi'ya ait (Focus 1.6 TDCi kaydı). İkinci bağımsız doğrulama yok. |
| 2 | Courier / Tourneo Courier | 2014- | 1.5 TDCi / 1.0 EcoBoost | – eklenmedi: Şikâyetler fren sesi, gıcırtı ve genel motor arıza lambası gibi dağınık konularda; ortak bir arıza için iki bağımsız site bulunamadı. |
| 2 | Fiesta | 2008-2023 | 1.25 / 1.4 Duratec | – eklenmedi: Kullanıcılar 1.25 ve 1.4 benzinlileri sorunsuz olarak anıyor; kronik sorun bulunamadı. |
| 2 | Focus 3 | 2011-2018 | 1.5 EcoBoost 150/182 | – eklenmedi: Focus için sonuçlar ağırlıkla 1.0 EcoBoost; 1.5 EcoBoost silindir kapağı sorunu Kuga 2 / Mondeo kaydında ele alındı, Focus'a özgü kaynak yok. |
| 2 | Kuga 2 | 2013-2019 | 1.5 EcoBoost 150/182 | ✓ 1 sorun |
| 2 | Kuga 2 | 2013-2019 | 2.0 TDCi 140/150/180 | – eklenmedi: Faz 9'da arandı: 2011 model bir Kuga'da (Kuga 1) enjektör tutucu bacaklarının kırılması (tek vaka) ve Powershift'te düşük devirde vites düşürme gecikmesi, geri vitesten D'ye geçişte sarsıntı yorumları var; Şikâyetvar'daki turbo arızası şikâyetinde motor tipi belirtilmiyor. 2.0 TDCi için tekrar eden, iki siteyle doğrulanan sorun çıkmadı. |
| 2 | Puma | 2019- | 1.0 EcoBoost mHEV | – eklenmedi: Forum görüşleri çelişkili (bazıları en sorunsuz 3 silindirli diyor); tekrar eden bir motor sorunu için kanıt yok. |
| 3 | EcoSport | 2013-2022 | 1.0 EcoBoost | ✓ 1 sorun |
| 3 | Mondeo / Transit Connect / Courier | 2007-2019 | 2.0 / 1.6 TDCi, 1.5 TDCi | – eklenmedi: Mondeo için tekil direksiyon, enjektör ve DPF anlatıları var; Transit Connect ve Courier 1.5 TDCi için sonuç çıkmadı. |
| 3 | Puma Gen-E / Mustang Mach-E / Explorer Electric | 2022- | Elektrik | – eklenmedi: Şikâyetvar'da Puma Gen-E için sürüş sırasında şarj hatası (iki kez yol yardımı) ve batarya su sızıntısı tekil; Mustang Mach-E ve Explorer Electric için kayıt çıkmadı. |
| 3 | Ranger | 2012- | 2.2 / 3.2 TDCi | – eklenmedi: Şikâyetvar'da turbo ve hortum şikâyetleri var; 2.2 ve 3.2 TDCi'ye özgü ikinci bağımsız kaynak çıkmadı. |
| 3 | Transit Custom | 2012- | 2.0 EcoBlue | – eklenmedi: Yağ tüketimi ve turbo şikâyetleri yalnızca Şikâyetvar'da; ikinci bağımsız kaynak bulunamadı. |

### Kia

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Ceed | 2012-2018 | 1.6 CRDi | ✓ 1 sorun |
| 1 | EV6 | 2022- | Elektrik (E-GMP, 77,4 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Rio | 2011-2017 | 1.4 CRDi 90 | ✓ 1 sorun |
| 1 | Sportage QL FL / NQ5 | 2018- | 1.6 CRDi 136 (7DCT) | ✓ 1 sorun |
| 1 | Sportage SL / QL | 2010-2021 | 1.6 GDI 135 | ✓ 1 sorun |
| 1 | Sportage SL / QL | 2010-2018 | 1.7 CRDi 115/141 | – eklenmedi: Faz 9'da arandı: 1.7 CRDi'ya özgü kronik arıza çıkmadı; turbo mili, enjektör ve DPF vakaları 1.6 CRDi ve 2020 sonrası araçlara ait (7DCT titremesi Sportage 1.6 CRDi kaydında). |
| 2 | Ceed | 2012-2021 | 1.4 / 1.6 MPI | – eklenmedi: 1.4 ve 1.6 MPI benzinlilerde motora özgü kronik sorun çıkmadı; torpido ve konsol kabarması motor tipinden bağımsız. |
| 2 | Ceed CD | 2018- | T-GDI benzinli (7DCT) | ✓ 1 sorun |
| 2 | EV3 | 2024- | Elektrik (58,3 / 81,4 kWh) | ✓ 1 sorun |
| 2 | Niro EV | 2019- | Elektrik | – eklenmedi: Şikâyetvar'da menzil, DC şarj süresi ve batarya bağlantı ünitesi (parçanın Türkiye'de bulunmaması) şikâyetleri tekil; ikinci bağımsız kaynak yok. EV3 ICCU arızası Faz 6'da ayrı kayıt oldu; ICCU geri çağırması Kia EV6 kaydında. |
| 2 | Picanto | 2017- | 1.0 / 1.2 MPI | ✓ 1 sorun |
| 2 | Rio | 2011-2017 | 1.4 MPI 100 | – eklenmedi: Forumlarda sorunsuz olarak anılıyor; kronik sorun bulunamadı. |
| 2 | Rio YB | 2017-2023 | 1.4 MPI 100 / 1.0 T-GDI | – eklenmedi: Faz 9'da arandı: DonanımHaber'de Rio 1.4 MPI ve 6 ileri tork konvertörlü otomatik için sorunsuz yorumları var (bir sahip yaklaşık 27.500 km'de sorun yaşamadığını yazıyor); 1.0 T-GDI için kaynak çıkmadı. Rio UB 1.4 CRDi DPF sorunu ayrı kayıtta. |
| 2 | Stonic | 2017- | 1.4 MPI 100 (6 ileri otomatik) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Ceed CD | 2018- | 1.6 CRDi 115/136 | – eklenmedi: Faz 9'da arandı (tek sorgu, T-GDI ile birlikte): Ceed CD'ye özgü sonuçlar 7DCT silkelemesinde toplandı (T-GDI satırında kayıtlı); 1.6 CRDi motoru ve yağ eksiltme için bilgi çıkmadı. |
| 3 | Cerato | 2013-2018 | 1.6 (arka stop ve bagajdan su alma) | – eklenmedi: Su alma şikâyetleri Şikâyetvar'da çok, ancak kilometre ve model yılı verisi yok ve ikinci bağımsız kaynak (Ekşi'de tek yorum) sınırlı. |
| 3 | EV9 | 2024- | Elektrik | – eklenmedi: Şikâyetvar'da hızlı şarjın araç tarafından durdurulması (yaklaşık 20.000 km) ve batarya elektrik arızası (üç hafta serviste) tekil. CarComplaints'te ABD'deki 2024 EV9'lara ait elektrik sistemi şikâyetleri var ancak Türkiye şikâyetleriyle aynı arıza değil; NHTSA'nın ICCU geri çağırmasının EV9'u kapsadığı doğrulanamadı (EV6 kaydı). |
| 3 | Niro / Cerato / Sorento | 2011- | Hybrid / 1.6 / 2.2 CRDi | – eklenmedi: Cerato ve Niro için sonuç çıkmadı; Sorento 2.2 CRDi için yalnızca tekil şikâyetler var. |
| 3 | Sorento / Venga | 2010-2018 | 2.2 CRDi / 1.4 CRDi | – eklenmedi: Sorento 2.2 CRDi ve Venga 1.4 CRDi için kaynak çıkmadı. |
| 3 | Sportage / Ceed / Rio | 2010-2021 | 1.7 CRDi, 1.4 MPI, 1.25 | – eklenmedi: Sportage 1.7 CRDi, Ceed 1.4 MPI ve Rio 1.25 için motor kaynaklı kronik sorun çıkmadı; Ceed şikâyetleri torpido / konsol çatlaması ve start-stop üzerine. |
| 3 | Sportage SL / QL | 2010-2021 | 1.6 T-GDI 177 (7DCT) | – eklenmedi: Faz 9'da arandı (tek sorgu): Şikâyetvar ya da DonanımHaber kaydı çıkmadı; sonuçlar genel inceleme ve teknik özellik sayfalarından oluştu. 7DCT kavrama titremesi Sportage 1.6 CRDi kaydında. |
| 3 | Stonic | 2017- | 1.0 T-GDI / 1.6 CRDi | – eklenmedi: 1.0 T-GDI için tekil titreme ve arıza lambası şikâyetleri; 1.6 CRDi için sonuç çıkmadı. |

### Dacia

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Duster | 2010-2017 | 1.5 dCi (K9K) | ✓ 2 sorun |
| 1 | Duster | 2021-2024 | 1.0 TCe 100 ECO-G (H4Dt) | ✓ 1 sorun |
| 1 | Sandero / Sandero Stepway | 2021- | 1.0 TCe 90/100 (H4Dt) | ✓ 1 sorun |
| 2 | Duster | 2018-2021 | 1.5 dCi 110 (K9K) | ✓ 1 sorun |
| 2 | Duster | 2019-2024 | 1.3 TCe 130/150 (EDC) | ✓ 1 sorun |
| 2 | Sandero / Logan / Symbol | 2013-2020 | 0.9 TCe 90 (H4Bt) | ✓ 1 sorun |
| 2 | Sandero / Logan / Symbol | 2013-2020 | 1.5 dCi 75/90 (K9K) | ✓ 1 sorun |
| 3 | Duster | 2018-2021 | 1.6 SCe 115 | – eklenmedi: Kaynaklarda bu motor için öne çıkan bir sorun bulunamadı. |
| 3 | Jogger | 2022- | 1.0 TCe 110 (manuel) | ✓ 1 sorun |
| 3 | Jogger | 2022- | 1.0 TCe 100 ECO-G (LPG) | – eklenmedi: LPG / ECO-G şikâyetleri tekil ve Jogger'a özgü değil (Dacia Eco-G genelinde); ikinci bağımsız kaynak bulunamadı. |
| 3 | Lodgy / Dokker | 2012-2021 | 1.5 dCi (K9K) | – eklenmedi: Lodgy / Dokker 1.5 dCi için turbo ya da enjektör örüntüsü çıkmadı; şikâyetler teyp ekranı ve elektrikte, enjektör anlatıları diğer Renault dizellerinden. |
| 3 | Spring | 2022- | Elektrik | – eklenmedi: Şikâyetvar'da 'akü şarj almıyor' uyarısı ve Ekşi Sözlük'te menzil kaybı tekil; sistematik bir şarj ya da batarya sorunu bulunamadı. |

### Audi (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | A3 8P FL / 8V | 2009-2020 | 1.4 TFSI (S tronic DQ200) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | A3 8V | 2012-2020 | 1.6 TDI 105/110 | ✓ 2 sorun |
| 1 | A4 B8 | 2008-2015 | 1.8 TFSI / 2.0 TFSI (EA888 Gen2) | ✓ 4 sorun, 2 yıl kırılımı |
| 1 | A4 B8 | 2008-2015 | 2.0 TDI 143/150/177 (Multitronic) | ✓ 1 sorun |
| 2 | A3 8V | 2012-2020 | 1.0 TFSI / 1.2 TFSI | – eklenmedi: 1.2 TFSI için sonuç çıkmadı; 1.0 TFSI için yalnızca tekil anekdotlar (start-stop sonrası kalkış, far). S tronic şikâyetleri 1.4 TFSI ve 1.6 TDI kayıtlarında ele alındı. |
| 2 | A3 8Y | 2020- | 35 TFSI 1.5 (48V hafif hibrit, S tronic) | ✓ 1 sorun |
| 2 | A4 B9 | 2016- | 2.0 TFSI / 2.0 TDI | – eklenmedi: B9 için doğrudan kronik sorun listesi çıkmadı; yağ eksiltme şikâyetleri çoğunlukla B8 dönemine ait (kayıtlı), B9'a özgü olanlar tekil (tahrik uyarısı, stop lambası çatlağı). |
| 3 | A1 (8X) | 2010-2018 | 1.2 / 1.4 TFSI (S tronic) | – eklenmedi: A1'e özgü veri sınırlı; yağ tüketimi ve S tronic anlatıları A3 ve A4 kayıtlarında ele alındı. |
| 3 | A6 C7 | 2011-2018 | 2.0 TDI / 3.0 TDI / 2.0 TFSI | – eklenmedi: A6 C7'ye özgü kaynak bulunamadı; bulunan A6 2.0 TDI başlıkları C6 dönemine (2009-2011) ait. |
| 3 | Q2 / Q3 | 2016- | 35 TFSI (1.5) | – eklenmedi: Şikâyetvar'da Q2 35 TFSI için 2024 model bir araçta sürekli tahrik hatası, Q3 için alternatör şüphesiyle yolda kalma gibi tekil kayıtlar var; Q2 / Q3'e özgü ikinci bağımsız kaynak çıkmadı. Aynı 1.5 TFSI motorlu A3 (8Y) 35 TFSI kaydında 48 V / alternatör arızası ele alındı. |
| 3 | Q3 | 2011-2018 | 2.0 TDI / 2.0 TFSI | – eklenmedi: Q3'e özgü kaynak bulunamadı; 2.0 TFSI yağ tüketimi Q5 ve A4 kayıtlarında ele alındı. |
| 3 | Q4 e-tron / e-tron | 2021- | Elektrik | – eklenmedi: Şikâyetvar'da uzaktan erişim hizmetinin Türkiye'de kapalı olması, yeni araçta akü arızası ve menzil şikâyetleri tekil; ikinci site yok. e-tron GT için Mart 2024 batarya modülü geri çağırmaları (93VM, 93VN; Taycan ile aynı modüller, şarjın %80 ile sınırlanması) var; Türkiye kapsamı doğrulanamadı. |
| 3 | Q5 8R | 2008-2017 | 2.0 TFSI (EA888) | ✓ 1 sorun, 1 yıl kırılımı |

### Honda (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Civic FC5 | 2016-2021 | 1.6 i-VTEC 125 (CVT) | ✓ 1 sorun |
| 1 | Civic FC5 | 2016-2021 | 1.5 VTEC Turbo (L15B7) | ✓ 2 sorun, 1 yıl kırılımı |
| 2 | Accord | 2008-2015 | 2.0 i-VTEC / 2.2 i-DTEC | – eklenmedi: Faz 9'da arandı: Accord 2.0 i-VTEC / 2.2 i-DTEC için bu aramada veri çıkmadı (aynı sorgudaki Civic 1.6 i-DTEC DPF sorunu ayrı kayıtta). |
| 2 | CR-V | 2012-2018 | 1.6 i-DTEC | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | CR-V | 2012-2018 | 2.0 i-VTEC | – eklenmedi: 2.0 i-VTEC için yağ eksiltme ve SRS şikâyetleri tekil kullanıcı anlatımları; ikinci bağımsız kaynak bulunamadı. |
| 2 | City | 2009- | 1.5 i-VTEC / 1.5 Hybrid | – eklenmedi: City 1.5 için yakıt tüketimi ve vites geçişi şikâyetleri yalnızca Şikâyetvar'da (2021 model); ikinci bağımsız kaynak yok. |
| 2 | Civic FB7 | 2012-2015 | 1.6 i-VTEC / 1.8 i-VTEC | – eklenmedi: FB7 şikâyetleri ağırlıkla boya atması ve kozmetik; motora özgü sorunlar tekil (130 bin km'de motor yanması, 1.8 yağ sızıntısı için eski bir forum yazısı). |
| 2 | Civic FC5 (dizel) | 2016-2021 | 1.6 i-DTEC 120 (9 ileri otomatik) | ✓ 1 sorun |
| 3 | Jazz / HR-V | 2011- | 1.3 / 1.5 i-VTEC | – eklenmedi: 1.3 / 1.5 i-VTEC CVT için kanıtlı kronik sorun çıkmadı; bulunanlar eski nesil Jazz CVT, eski kasa HR-V yorumu ve hibrit akü şikâyeti. |

### Seat (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Leon 5F | 2012-2020 | 1.2 TSI / 1.6 TDI (DSG DQ200) | ✓ 1 sorun |
| 1 | Leon 5F | 2005-2020 | 1.4 TSI 122/125/140/150 (EA211, ACT) | – eklenmedi: Faz 9'da arandı: 1.4 TSI ACT için zincir ve yağ eksiltme anlatıları çoğunlukla 1.2 TSI'ya ait; Şikâyetvar'da 1.4 TSI Leon sahibinin zincir şüphesi (ustanın doğrulanmamış teşhisi) ve 2020 model bir Leon'da ACT valf hortumu yırtığı tekil vakaları var. DSG kavrama ve mekatronik sorunları Leon 5F 1.2 TSI / 1.6 TDI (DSG DQ200) kaydında. |
| 2 | Ibiza 6J / 6P | 2008-2017 | 1.2 TSI (DSG DQ200) | ✓ 1 sorun |
| 2 | Ibiza 6J / 6P | 2008-2017 | 1.0 TSI / 1.6 TDI | – eklenmedi: Ibiza 1.6 TDI için yalnızca tekil bir direksiyon (EPS) şikâyeti çıktı; 1.0 TSI için kaynak bulunamadı. Zincir iddiası Ibiza'ya özgü değil. |
| 2 | Leon 5F FL | 2018-2020 | 1.5 TSI 130/150 (ACT) | – eklenmedi: Şikâyetvar'da 2018 model 1.5 TSI Leon sahibi yetkili servisin bir litreye yakın yağ eksiltmeyi normal saydığını ve litre başına ücret istediğini yazıyor; DonanımHaber'deki 2019 Leon FR 1.5 TSI 150 başlığında cam tavan titremesi ve DSG mekatronik değişimi anılıyor. Tekil kayıtlar; aynı motorun yağ eksiltmesi Karoq ve Passat kayıtlarında ele alındı. |
| 2 | Leon KL | 2020- | 1.0 eTSI / 1.5 eTSI (48V hafif hibrit, DSG) | ✓ 1 sorun |
| 3 | Ateca / Arona | 2016- | 1.0 TSI / 1.5 TSI | – eklenmedi: Arona 1.0 TSI DSG ve Ateca 1.5 TSI için yalnızca Şikâyetvar'daki tekil kayıtlar (DSG vuruntusu, yağ uyarısı, yağ kaçağı); yaygınlığı gösteren bağımsız kaynak yok. Faz 8'de 1.5 TSI için yeniden arandı: Şikâyetvar'daki Ateca kaydı (24.000 km'de dört kez yağ eksik uyarısı) tek başına; DonanımHaber'de Ateca için yağ eksiltme anlatıları genel TSI başlıklarında geçiyor, Ateca 1.5 TSI'ya özgü ikinci bağımsız kaynak çıkmadı. |
| 3 | Toledo | 2012-2019 | 1.2 TSI / 1.6 TDI (DSG) | – eklenmedi: Faz 9'da arandı (tek sorgu): Türkçe kaynak çıkmadı; sonuçlar tanıtım ve ilan sayfaları ile İspanyolca bir sorun sayfasından oluştu (DQ200'de kalkışta kayma ve sarsıntı, 1.6 TDI'da DPF tıkanma eğilimi). DQ200 sorunları Leon 5F, Rapid ve Polo kayıtlarında. |

### Chevrolet (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Captiva / Aveo / Lacetti | 2007-2016 | 2.0 VCDi, 1.4 / 1.2 | – eklenmedi: Captiva 2.0 D ve Aveo 1.4 zincir iddiaları tek rehber sitesine dayanıyor; Lacetti için sonuç çıkmadı. |

### Volvo (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 2 | EX30 / XC40 Recharge | 2021- | Elektrik | – eklenmedi: EX30 için hücre kusuru geri çağırması var (Sunwoda hücreleri, %70 şarj sınırı, modül değişimi); Avrupa'da yalnızca sağ direksiyonlu 69 kWh modelleri kapsadığı yazılıyor ve Türkiye kapsamı doğrulanamadı. Şikâyetvar'daki hızlı şarj, 'Electric Drive Fault' ve XC40 Recharge motor / batarya şikâyetleri tekil. |
| 3 | S60 / V40 | 2011-2018 | 1.6 D DRIVe (Powershift) | ✓ 1 sorun |

### Subaru (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | XV | 2012-2017 | 2.0 benzinli boxer | ✓ 1 sorun, 1 yıl kırılımı |

### Mini (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Cooper / One (F56) | 2014- | 1.5 üç silindir (B38) | – eklenmedi: F56 1.5 üç silindir için kaynak çıkmadı; bir Ekşi yorumu yağ kaçırdığını söylüyor ama motor belirsiz. |
| 3 | Cooper S / Countryman S (R56 / R60) | 2007-2016 | 1.6 turbo benzinli (N14 / N18) | ✓ 1 sorun |
| 3 | Cooper SE | 2020- | Elektrik | – eklenmedi: Şikâyetvar'da dört kayıt (sürüş kontrolü kaybı iddiası, 37 gün parça beklemesi); DonanımHaber yorumları olumlu. Tekrar eden bir arıza örüntüsü yok. NHTSA 24V-612 geri çağırması 2020-2024 Cooper SE'yi kapsıyor (12.535 araç; yazılımla bataryanın %30'un altına boşaltılması, yangın riski); Türkiye kapsamı ve Türkiye'den bir şikâyet bulunamadı. |

### Jeep (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 2 | Avenger Electric | 2023- | Elektrik (54 kWh, 156 PS) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Renegade / Compass | 2015- | 1.6 MultiJet (DDCT) / 1.4 MultiAir | – eklenmedi: Renegade DDCT'ye özgü kaynak çıkmadı (sonuçlar Egea üzerinden geldi); Compass şanzıman şikâyetlerinde motor ve şanzıman kombinasyonu belirsiz. |

### Alfa Romeo (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Giulietta | 2010-2020 | 1.4 MultiAir / 1.6 JTDM | – eklenmedi: Şikâyetler gövde ve elektronikte (yolcu airbag kapağı şişmesi, klima); motorlara özgü kaynaklı bulgu yok. |
| 3 | Junior Elettrica | 2024- | Elektrik (54 kWh, 156 PS) | – eklenmedi: Şikâyetvar'da 2025-2026 tarihli tekrarlayan 'elektrikli çekiş sistemi arızası' uyarısı (bir araç yaklaşık 90 gün serviste), 900 km'de yolda kalıp şarj almama ve batarya sızıntısı şikâyetleri var; ikinci bağımsız site bulunamadı. Aynı 54 kWh / 156 PS değerlerine sahip Avenger Electric ve Fiat 600e ayrı kayıtlarda. |

### Mazda (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | 3 / 6 / CX-5 | 2013- | Skyactiv-G / Skyactiv-D | – eklenmedi: Skyactiv motorlar için Türkiye'ye özgü kronik sorun kaynağı çıkmadı; 2.2 dizelin Türkiye'de satılmadığı yazılıyor. |

### Suzuki (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | SX4 S-Cross / Vitara / Swift | 2014- | 1.4 BoosterJet / 1.6 DDiS | – eklenmedi: Bulgular tek rehber sitesi (Araclo) ve Şikâyetvar'ın elektronik / multimedya şikâyetleriyle sınırlı. |

### Mitsubishi (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | L200 / ASX / Lancer | 2010- | 2.5 DI-D / 1.6 MIVEC | – eklenmedi: L200 DPF ve turbo anlatıları rehber siteleri ve tekil Şikâyetvar kayıtları; ASX 1.6 MIVEC sıcak marş sorunu yalnızca Ekşi'de. |

### Land Rover (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Freelander 2 | 2007-2014 | 2.2 TD4 | – eklenmedi: Turbo hortumu ve Haldex anlatıları tekil; Discovery Sport ve Evoque için güvenilir kaynak yok. |

### Cupra (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Born | 2022- | Elektrik | – eklenmedi: Arama sonuç vermedi. Cupra Born, Ekim 2026 VW grubu batarya geri çağırmasının kapsadığı modeller arasında (belirli üretim partileri); Türkiye kapsamı doğrulanamadı. |
| 3 | Formentor | 2020- | 1.5 eTSI (48V hafif hibrit, DSG) | ✓ 1 sorun, 1 yıl kırılımı |

### MG (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | MG4 Electric | 2023- | Elektrik (51 / 64 kWh) | ✓ 1 sorun |
| 3 | HS | 2021- | 1.5 T (DCT) | – eklenmedi: Şanzıman gecikmesi şikâyetleri yalnızca Şikâyetvar'da; model yılı ve sürüm bilgisi doğrulanamadı. |
| 3 | ZS EV | 2020- | Elektrik | – eklenmedi: Şikâyetvar'da batarya bölümünden gelen ses ve şarj olmama (2023) tekil; ikinci bağımsız kaynak yok. DC şarj sorunu MG4 kaydında. |

### Lexus (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | IS / CT 200h | 2011- | 2.5 / 1.8 hibrit | – eklenmedi: Aramada sonuç çıkmadı. |

### Isuzu (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | D-Max | 2012- | 1.9 / 3.0 D | – eklenmedi: EGR, turbo ve enjektör anlatıları bir forum yorumu ve tek rehber sitesinde; ikinci bağımsız kaynak çıkmadı. |

### Smart (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | #1 / #3 | 2023- | Elektrik | – eklenmedi: Aramada Smart #1 için Türkiye'ye ait sonuç çıkmadı. Faz 6'da #3 de arandı: Smart adını taşıyan telefon ve TV servisi şikâyetleri dışında Türkiye'ye ait araç kaydı çıkmadı. |

### Porsche (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 2 | Taycan | 2020- | Elektrik (4S / Turbo) | ✓ 1 sorun, 1 yıl kırılımı |

### Zeekr (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | 001 / X | 2023- | Elektrik | – eklenmedi: Şikâyetvar'da Zeekr'e ait kayıt çıkmadı; Ekşi Sözlük'te yalnızca sürücü ayık tutma modu, kafa tarama modu ve fiyat tartışması gibi tekil yorumlar var. |

### Xpeng (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | G6 / G9 / P7 | 2024- | Elektrik | – eklenmedi: Şikâyetvar'da Xpeng'e ait kayıt çıkmadı; Ekşi Sözlük'te yalnızca bir P7+ test sürüşü izlenimi var. |

### Leapmotor (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | T03 / C10 | 2022- | Elektrik | – eklenmedi: Şikâyetvar'da T03 için şarj edilememe, gerçek menzilin 200-250 km'ye gerilemesi, aracın iki kez kendini kilitlemesi ve Çince menü şikâyetleri tekil; Ekşi Sözlük'te yalnızca menzil yorumları var; C10 için kayıt çıkmadı. |

## Plan dışı kayıtlar

İlk aşamada eklenen ve 2011 öncesi üretime ağırlık veren ya da plandaki satırlarla eşleşmeyen kayıtlar. Silinmedi; doğrulanmış veri olarak durur.

| Marka | Model | Motor |
| --- | --- | --- |
| Chevrolet | Cruze (2009-2016) | 1.6 benzin (F16D4) |
| Honda | Civic (FD6, 2006-2011) | 1.6 i-VTEC |
| Opel | Astra H (2004-2010) | 1.6 Twinport (Z16XEP / Z16XER, Easytronic) |
| Volkswagen | Passat (B6, 2005-2010) | 2.0 TDI PD 16V (BKP) |
| Volkswagen | Polo (9N / 6R, 2002-2014) | 1.2 3 silindir (BMD / BME / CGPA) |
