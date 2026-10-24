# Kapsam ve ilerleme

Bu dosya `scripts/kapsam_md_uret.py` ile `data/kapsam.json` (plan) ve `data/araclar.json` (veri) içeriğinden üretilir. Elle düzenlemeyin; planı `data/kapsam.json` içinde değiştirip betiği yeniden çalıştırın.

## Ölçüt

- **Zaman penceresi:** Son 10-15 yılın araçları, yani yaklaşık 2011 model yılı ve sonrası. Daha eski yıllar yalnızca ilk aşamada eklenmiş kayıtlarda kaldı (aşağıda ayrıca listelenir).
- **Marka seçimi:** Türkiye'de en çok satılan markalar (aşağıdaki tablo). İlk dört aşamada elektrikli ya da 2023 sonrası girmiş markalar (BYD, Togg, Tesla, Chery) "motor grubu ve ikinci el geçmişi yok" gerekçesiyle dışarıda bırakılmıştı; 5. aşamada elektrikli araçlar kapsama alındı ve bu markalar plana girdi. Bu listenin dışındaki markalar (`ek` kapsamı) ikinci el yaygınlığı ve kaynak bulunabilirliği gözetilerek editoryal olarak eklendi; satış adetleri doğrulanamadı.
- **Elektrikli araçlar:** `motor` alanı elektrik motoru ve batarya sürümünü gösterir (ör. `Elektrik (52,4 kWh ve 88,5 kWh)`). Sorunlar batarya, şarj (OBC, ICCU), 12V akü ve yazılım gibi elektrikli araca özgü parçalara aittir. Geri çağırma kaydı olan sorunlarda Türkiye kapsamı doğrulanamıyorsa bu kayıtta ve plan notunda belirtilir. Aynı batarya ve motor değerlerine sahip kardeş modelin kaynağı yalnızca ilgili kayıtta açıkça belirtilerek kullanılabilir (ör. Astra Electric ve Peugeot e-308). Plug-in hibritler (ör. BYD Seal U DM-i) bu aşamada kapsam dışıdır.
- **Sıralama:** Genelden özele gidilir. Önce her markanın en çok satılan ve en çok sorgulanan modelleri ile ana motor grupları (kademe 1), sonra yaygın ama daha az sorgulananlar (kademe 2), en son niş gruplar (kademe 3).
- **Yıl kırılımı:** Kaynaklar üretim yılına göre fark belirtiyorsa sorun `donem_kirilimi` ile yıl aralıklarına ayrılır (ör. revizyon öncesi ve sonrası).
- **Motor versiyonları:** Kaynaklar iki versiyonu motor kodu, güç, şanzıman ya da kasa/nesil ile ayırt ediyorsa ayrı kayıt açılır (ör. M271 Kompressor ve M271 EVO; N47D16 ve N47D20; Qashqai J11 1.5 dCi ve 1.6 dCi Xtronic). Ayırt etmiyorlarsa kayıt bölünmez, fark metinde ya da `donem_kirilimi` içinde belirtilir ([README](README.md#motor-versiyonları)).
- **Aynı motoru ya da şanzımanı paylaşan modeller (10. aşamadan itibaren):** Motor ve şanzıman kaynaklı sorunlar ortak ailelere yazılır ([README](README.md#ortak-motor-ve-şanzıman-aileleri-aileler)); aynı motoru ya da şanzımanı kullandığı bilinen modeller aileye bağlanır. Modele özgü kaynağı olan kayıtlar kendi sorununu aile sorununa bağlar (✓); modele özgü kaynağı olmayanlar yalnızca ortak aile kaynağıyla kayıtlıdır (◐) ve plan notunda modele özgü kaynağın aranmadığı ya da bulunmadığı yazılır. Bu kayıtlar doğrudan kanıtı sınırlı sayılır ve görüntüleyicide "Ortak aile" etiketiyle ayrılır. Aile bağı yalnızca model, yıl ve motor kodunun eşleştiği bilinen kombinasyonlar için kurulur.
- **İlan sayısı kontrolü:** 7. aşamada plan, arabam.com'un aylık ilan sıralamaları ve Cardata listeleriyle karşılaştırıldı (sahibinden.com'un canlı model sayıları okunamadı) ve en çok ilanlı modellerin motor boşlukları kapatıldı. "Çok ilanlı" olmak tek başına kayıt gerekçesi değildir: tekrar eden bir kronik sorun için iki bağımsız kaynak bulunamazsa grup `–` olarak kalır.
- **Çok kullanılan araç denetimi:** 9. aşamada plan, trafikteki araç sayıları (TÜİK verisine dayanan yaklaşık 2024 listeleri) ve ikinci el satış sıralamalarıyla model, nesil ve motor düzeyinde yeniden karşılaştırıldı. Bir satırın `eslesme` parçalarından her biri en az bir kayda denk gelmelidir (test denetler); "1.4 TSI / 1.6 TDI" gibi birleşik bir satırın yalnızca bir parçası kayıtlıysa satır bölünür, böylece ✓ kayıtsız bir motoru gizleyemez. Aranıp eklenmeyen (–) gruplar ile sıraya alınmış (○) gruplar görüntüleyicide "Kayıt açılmayan gruplar" bölümünde gösterilir.
- **Model geneli sorunlar (11. aşamadan itibaren):** Motordan bağımsız, modele (nesle) özgü sorunlar (cam tavan ve bagajdan su alma, far, kapı kilidi, multimedya, boya, ön takım gibi kasa, sızdırmazlık, iç mekân, elektronik ve süspansiyon sorunları) `motor` alanı "Tüm motorlar (model geneli)" olan ayrı bir kayıtta toplanır ([README](README.md#model-geneli-kayıtlar)). Bu sorunlar yaşa ve kullanıma bağlı olduğundan kaynaklarda çoğunlukla kilometre bilgisi yoktur; kilometre aralığı uydurulmaz, boş bırakılır. Model geneli plan satırları yalnızca işlendikçe eklenir (✓ ya da –); satırı olmayan bir modelde bu sorunlar henüz taranmamıştır.
- **Kanıt eşiği:** Her sorun için en az iki farklı site ve en az bir deneyim/resmî türünde kaynak gerekir ([README](README.md#kaynak-kuralı)). Kaynak bulunamayan gruplar plana `–` olarak işlenir; sorun uydurulmaz.

Kademeler:

- **Kademe 1:** Son 10-15 yılda en çok satılan ve ikinci elde en çok sorgulanan model ve ana motor grupları
- **Kademe 2:** Yaygın ama daha az sorgulanan model ve motor grupları
- **Kademe 3:** Niş, yeni ya da kaynağı az olan gruplar

Model ve motor seçimi 2025 satış sıralaması ve ikinci el pazarındaki yaygınlık gözetilerek editoryal olarak yapılmıştır; kademe atamaları kesin bir sıralama değil, çalışma sırasıdır.

## İlerleme

- Plan: **575** model/motor grubu (motor ve şanzıman düzeyi)
- Tamamlanan (✓, modele özgü kaynaklı sorun var): **168**
- Yalnızca ortak aile kaynağıyla kayıtlı (◐): **142**
- Araştırılıp eklenmeyen (–): **177**
- Sırada (○): **88**
- Kademe 1: **120/120** işlendi (✓, ◐ ya da –)
- Model geneli taraması: **54** model nesli arandı (sorun bulunan ✓ **35**, kanıt yetersiz – **19**); 328 motor kaydından **42**'i taranmış bir modele ait, **286**'i henüz taranmadı
- Veritabanı: **363** kayıt (**328** motor, **35** model geneli), **299** kayda özgü kronik sorun, **48** motor/şanzıman ailesi (**82** ortak sorun)

| Marka | Plan | ✓ | ◐ | – | ○ | Kademe 1 işlenen | Model geneli (✓ / –) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Renault | 37 | 15 | 7 | 11 | 4 | 8/8 | 4 / 0 |
| Volkswagen | 50 | 18 | 12 | 15 | 5 | 13/13 | 3 / 5 |
| Toyota | 20 | 4 | 5 | 9 | 2 | 6/6 | 0 / 1 |
| Fiat | 27 | 11 | 4 | 7 | 5 | 5/5 | 4 / 0 |
| Hyundai | 35 | 11 | 9 | 13 | 2 | 13/13 | 2 / 1 |
| Peugeot | 21 | 9 | 5 | 5 | 2 | 5/5 | 2 / 1 |
| Opel | 40 | 14 | 13 | 8 | 5 | 5/5 | 2 / 2 |
| Citroen | 19 | 6 | 5 | 5 | 3 | 3/3 | 0 / 1 |
| BYD | 2 | 1 | 0 | 1 | 0 | 1/1 | — |
| Skoda | 27 | 9 | 8 | 8 | 2 | 6/6 | 3 / 3 |
| Mercedes-Benz | 37 | 10 | 12 | 8 | 7 | 6/6 | 3 / 1 |
| Togg | 2 | 1 | 0 | 1 | 0 | 1/1 | — |
| BMW | 40 | 5 | 17 | 13 | 5 | 13/13 | 2 / 0 |
| Tesla | 2 | 1 | 0 | 1 | 0 | 1/1 | — |
| Nissan | 19 | 8 | 4 | 4 | 3 | 4/4 | 2 / 0 |
| Chery | 2 | 0 | 0 | 2 | 0 | 0/0 | — |
| Ford | 32 | 8 | 11 | 11 | 2 | 8/8 | 2 / 1 |
| Kia | 28 | 9 | 5 | 10 | 4 | 6/6 | 1 / 1 |
| Dacia | 12 | 8 | 1 | 3 | 0 | 3/3 | 1 / 1 |
| Audi | 31 | 6 | 9 | 8 | 8 | 6/6 | 1 / 0 |
| Honda | 12 | 4 | 3 | 5 | 0 | 2/2 | 2 / 0 |
| Seat | 12 | 3 | 5 | 1 | 3 | 2/2 | 1 / 1 |
| Chevrolet | 1 | 0 | 0 | 1 | 0 | 0/0 | — |
| Volvo | 12 | 1 | 1 | 9 | 1 | 2/2 | — |
| Subaru | 6 | 1 | 2 | 0 | 3 | 0/0 | — |
| Mini | 4 | 1 | 1 | 1 | 1 | 0/0 | — |
| Jeep | 7 | 1 | 2 | 1 | 3 | 0/0 | — |
| Alfa Romeo | 6 | 0 | 1 | 2 | 3 | 0/0 | — |
| Mazda | 1 | 0 | 0 | 1 | 0 | 0/0 | — |
| Suzuki | 4 | 0 | 0 | 2 | 2 | 0/0 | — |
| Mitsubishi | 4 | 0 | 0 | 1 | 3 | 0/0 | — |
| Land Rover | 5 | 0 | 0 | 1 | 4 | 0/0 | — |
| Cupra | 2 | 1 | 0 | 1 | 0 | 0/0 | — |
| MG | 4 | 1 | 0 | 2 | 1 | 1/1 | — |
| Lexus | 1 | 0 | 0 | 1 | 0 | 0/0 | — |
| Isuzu | 1 | 0 | 0 | 1 | 0 | 0/0 | — |
| Smart | 2 | 0 | 0 | 1 | 1 | 0/0 | — |
| Porsche | 3 | 1 | 0 | 0 | 2 | 0/0 | — |
| Zeekr | 1 | 0 | 0 | 1 | 0 | 0/0 | — |
| Xpeng | 1 | 0 | 0 | 1 | 0 | 0/0 | — |
| Leapmotor | 1 | 0 | 0 | 1 | 0 | 0/0 | — |
| Ssangyong | 2 | 0 | 0 | 0 | 2 | 0/0 | — |

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
| 11+ | Ssangyong | — | Ek kademe | Ek kademe: Faz 10'da sıraya alındı, henüz aranmadı. Satış adedi doğrulanamadı. |

\* İlk 10 sıra birden fazla haberde tutarlıdır (Volkswagen ve Toyota için küçük rakam farkları notlandı). 11. sıradan sonrası rakamlar tek bir tablodan alınmış ve ikinci bir kaynakta doğrulanamamıştır; bu yüzden sıra numarası verilmedi ve liste adet sırasındadır. Ford'un otomobil adedi bulunamadı. Kapsamdaki 18 marka bu belirsizliklerden etkilenmez, ancak 11-20. sıradaki markaların kendi aralarındaki sırası kesin değildir. Resmî tablo için ODMD'nin yıllık bülteni esas alınmalıdır.

Pazar verisi kaynakları:

- <https://www.donanimhaber.com/2025-te-turkiye-de-en-cok-satan-otomobiller-belli-oldu--200556>
- <https://www.cnbce.com/otomotiv/2025te-en-cok-satilan-otomobil-modelleri-belli-oldu-turkiyede-en-cok-satin-alinan-otomobil-hangisi-2025te-ne-kadar-clio-satildi-g22597>
- <https://www.ekonomist.com.tr/otomotiv/2025-te-turkiye-de-en-cok-hangi-otomobiller-satildi-satis-listesi-aciklandi-69679>
- <https://www.habergazetesi.com.tr/togg-2025te-elektrikli-arac-satislarinda-birinci-tesla-ve-byd-satis-rakamlari-aciklandi/amp>
- <https://www.odmd.org.tr> (Otomotiv Distribütörleri ve Mobilite Derneği, aylık basın bültenleri)

## Plan ve durum

Durum: **✓** veritabanında kayıtlı ve modele özgü kaynaklı sorunu var, **◐** kayıtlı ama yalnızca motor/şanzıman ailesinin ortak kaynaklarına dayanıyor (bu modele özgü bildirim ayrıca doğrulanmadı), **○** sırada, **–** araştırıldı ama iki bağımsız site bulunamadığı için eklenmedi. Motor grubu "Tüm motorlar (model geneli)" olan satırlar modelin motordan bağımsız sorunlarını gösterir (✓ sorun bulundu, – kanıt yetersiz). Yıllar yaklaşık üretim ya da Türkiye satış yıllarıdır.

### Renault

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Clio 4 | 2013-2019 | 0.9 TCe 90 (H4Bt) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Clio 4 | 2013-2019 | 1.5 dCi 75/90 (K9K) | ✓ 1 sorun (+1 ortak aile) |
| 1 | Clio 4 | 2013-2019 | Tüm motorlar (model geneli) | ✓ 1 sorun — Kapı kilidi ve sensörü arızası Şikâyetvar ve DonanımHaber'de doğrulandı. Orijinal multimedya ekranının donması yalnızca Şikâyetvar'da var (DonanımHaber'deki donma anlatıları sonradan takılan Android ünitelere ait); ön takım sesi tek bir yorum. |
| 1 | Clio 4 / Captur | 2013-2019 | 1.2 TCe 120 (H5Ft) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Clio 5 | 2019- | 1.0 TCe 90/100 (H4Dt) | ✓ 2 sorun |
| 1 | Clio 5 | 2019- | Tüm motorlar (model geneli) | ✓ 1 sorun — Multimedya ekranı şikâyeti iki sitede doğrulandı. Tavan döşemesinde lekelenme (2020 model, garanti kapsamında değişti) tek şikâyet. |
| 1 | Megane 3 / Fluence | 2009-2016 | 1.5 dCi (K9K, EDC) | ✓ 3 sorun (+2 ortak aile) |
| 1 | Megane 3 / Fluence | 2009-2016 | Tüm motorlar (model geneli) | ✓ 1 sorun — Ön cam altı ızgarası ve tahliye kanalı kaynaklı su alma iki sitede doğrulandı. Ekşi Sözlük'te cam krikosu arızası ve DonanımHaber'de klima kondansatörü arızası iddiası (kaynaksız) ile Şikâyetvar'da arka cam düğmeleri şikâyeti tek kaynakta kaldı; forumlarda bazı kullanıcılar Megane 3'te bilinen kronik arıza olmadığını savunuyor. |
| 1 | Megane 4 | 2016- | 1.3 TCe 140 (H5Ht, EDC) | ✓ 1 sorun (+1 ortak aile) |
| 1 | Megane 4 | 2016- | 1.5 Blue dCi 95/115 (K9K) | ✓ 2 sorun (+2 ortak aile) |
| 1 | Megane 4 / Sedan | 2016- | Tüm motorlar (model geneli) | ✓ 2 sorun — Far içi buğulanma / C-LED sararması ve fabrika multimedya şikâyetleri Şikâyetvar ve DonanımHaber'de doğrulandı (multimedya şikâyetlerinin çoğu sonradan takılan Android ekranlara ait, ayrıldı). Şikâyetvar'da kapı kolu soyulması (2024 model) tek şikâyet. |
| 1 | Zoe | 2019- | Elektrik (Z.E. 40 / Z.E. 50) | ✓ 1 sorun |
| 2 | Arkana | 2022- | 1.3 TCe 140 (EDC) | ◐ 2 ortak aile sorunu — Arkana'ya özgü kaynak aranmadı; gösterilen EDC sorunları Kadjar, Megane 4 ve Duster kayıtlarına dayanır. |
| 2 | Captur 2 | 2020- | 1.3 TCe 130/155 (EDC) | ◐ 2 ortak aile sorunu — Captur 2'ye özgü kaynak aranmadı; gösterilen EDC sorunları Kadjar, Megane 4 ve Duster kayıtlarına dayanır. |
| 2 | Captur 2 | 2020- | 1.0 TCe 100 (H4Dt) | ◐ 1 ortak aile sorunu — Captur 2'ye özgü kaynak aranmadı; gösterilen turbo wastegate sorunu aynı H4Dt motorunu kullanan Clio 5, Sandero ve Duster kayıtlarına dayanır. |
| 2 | Clio 3 / Clio 4 / Symbol | 2005-2019 | 1.2 16V 75 (D4F) | – eklenmedi: Şikâyetvar'da tek tek soğukta marş uzaması ve klima şikâyetleri var; D4F motoruna özgü tekrar eden bir sorun için iki bağımsız site bulunamadı. |
| 2 | Clio 3 / Symbol | 2008-2013 | 1.5 dCi 70/85/90 (K9K) | ✓ 1 sorun (+1 ortak aile) |
| 2 | Kadjar | 2015-2022 | 1.5 dCi 110 (K9K) | ✓ 1 sorun (+3 ortak aile) |
| 2 | Kadjar | 2015-2022 | 1.3 TCe 140 (H5H) | ✓ 2 sorun (+1 ortak aile) |
| 2 | Kadjar | 2015-2018 | 1.2 TCe 130 (H5Ft, manuel ve EDC) | ◐ 4 ortak aile sorunu, 1 yıl kırılımı — Kadjar 1.2 TCe'ye özgü kaynak aranmadı; gösterilen yağ tüketimi ve zincir sorunları aynı H5Ft motorunu kullanan Clio 4, Captur, Juke ve Qashqai kayıtlarına, EDC sorunları Kadjar 1.3 TCe ve 1.5 dCi kayıtlarına dayanır. |
| 2 | Kangoo 3 | 2021- | 1.5 Blue dCi / 1.3 TCe | ○ sırada |
| 2 | Megane 3 / Fluence | 2009-2016 | 1.6 16V (K4M, LPG'li dahil) | – eklenmedi: Aramalarda LPG'li K4M supap oturması anılıyor ama iki bağımsız site bulunamadı. |
| 2 | Megane 4 | 2016- | 1.6 SCe 115 (H4M) | – eklenmedi: Aramalarda H4M motoruna özgü arıza çıkmadı; şikâyetler motor tipi belirtmeyen genel Megane 4 konularına (yağ sızıntısı, soğutma, enjeksiyon uyarısı) ve LPG'li araçlara ait. |
| 2 | Megane E-Tech Electric | 2022- | Elektrik (60 kWh) | – eklenmedi: Şikâyetvar'da DC şarjda 'elektrik sistemini kontrol ettirin' uyarısı, şarj ünitesi arızası ve gerçek menzil şikâyetleri var; Ekşi Sözlük ve DonanımHaber'de aynı arızaları doğrulayan bir kaynak çıkmadı (12V akü başlığı Megane II'ye ait). |
| 2 | Scenic 3 / Grand Scenic | 2009-2016 | 1.5 dCi 110 (K9K, EDC) | ✓ 1 sorun (+3 ortak aile) |
| 2 | Scenic 4 | 2016-2022 | 1.5 dCi 110 (K9K, EDC) | ◐ 4 ortak aile sorunu — Scenic 4'e özgü kaynak aranmadı; gösterilen sorunlar aynı K9K motoru ve EDC şanzımanı kullanan Megane, Kadjar ve Captur kayıtlarına dayanır. |
| 2 | Symbol | 2008-2020 | 1.2 16V 75 (D4F) | – eklenmedi: Aramalarda D4F motoruna özgü tekrar eden sorun çıkmadı; şikâyetler soğukta marş ve klima gibi tekil konularda. Symbol III (2013-2020), Dacia Logan II'nin Türkiye'de Renault adıyla satılan ikizi (Motor1, Wikipedia); 0.9 TCe ve 1.5 dCi sürümleri 'Sandero / Logan / Symbol' kayıtlarında. |
| 2 | Taliant | 2021- | 1.0 TCe 90/100 (H4Dt) | ✓ 1 sorun |
| 3 | Austral | 2022- | 1.2 hafif hibrit / 1.3 TCe | ○ sırada |
| 3 | Captur | 2013-2019 | 1.5 dCi (K9K, EDC) | ✓ 1 sorun (+3 ortak aile) |
| 3 | Espace V | 2015- | 1.6 dCi 130/160 (R9M) / 1.6 TCe | ○ sırada |
| 3 | Kangoo | 2008-2021 | 1.5 dCi (K9K) | ◐ 2 ortak aile sorunu — Kangoo'ya özgü ayrı kaynak yok; gösterilen enjektör ve EGR sorunları aynı K9K motorunu kullanan Clio, Megane, Duster ve Sandero kaynaklarına dayanır. |
| 3 | Koleos | 2008- | 2.0 dCi (4x4) | – eklenmedi: Faz 9'da iki sorguyla arandı: Türkçe kaynak çıkmadı; yabancı derlemelerde X-Tronic CVT kayması, dizel 4x4'te arka diferansiyel ve kardan kırılması ile DPF tıkanması anlatılıyor (Koleos II ağırlıklı); anlatılar iki bağımsız kaynağa bağlanamadı. |
| 3 | Laguna 3 | 2007-2015 | 2.0 dCi | – eklenmedi: Faz 9'da iki sorguyla arandı: Türkçe şikâyet ya da forum kaydı çıkmadı; sonuçlar Fransızca sürücü yorumlarına dayanıyor (Fiches-Auto'da 1.5 dCi 110'da biyel kolu kırılganlığı ve enjektör sorunları, 2.0 dCi otomatikte şanzıman-kardan bağlantısı aşınması; Planète Renault'ta tekil enjeksiyon arızası). Kilometre ve tekrar bilgisi yetersiz. |
| 3 | Laguna 3 | 2007-2015 | 1.5 dCi 110 (K9K) | ◐ 2 ortak aile sorunu — Laguna 3'e özgü Türkçe kaynak çıkmadı; Fransızca sürücü yorumlarında 1.5 dCi 110'da biyel kolu kırılganlığı ve enjektör sorunları geçiyor (tekil). Gösterilen enjektör ve EGR sorunları aynı K9K motorunu kullanan Clio, Megane, Duster ve Sandero kaynaklarına dayanır. |
| 3 | Master / Trafic | 2010- | 2.3 dCi (M9T) | – eklenmedi: M9T için kol yatağı, turbo ve enjektör kanıtı yok; EGR / DPF anlatıları tek rehber sitesinden. |
| 3 | Megane 3 / Fluence | 2009-2016 | 1.6 16V (K4M) | – eklenmedi: K4M için en somut tema bobin arızası ve tek bir forum başlığında; yağ tüketimi ve termostat kaynakları motoru belirtmiyor. |
| 3 | Scenic 3 / Grand Scenic | 2009-2016 | 1.6 16V | – eklenmedi: Faz 9'da arandı: tek bir forum yorumu (2013 tarihli) 1.6 16V'de açı kaydırıcı (VVT) arızasını ve Sagem ateşleme bobinlerini anıyor; ikinci kaynak çıkmadı. 1.5 dCi EDC (şanzıman beyni arızası) ayrı satırda kayıtlandı. |
| 3 | Scenic E-Tech / 5 E-Tech | 2024- | Elektrik | – eklenmedi: Scenic E-Tech ve Renault 5 E-Tech'e özgü arıza kaydı çıkmadı; Şikâyetvar'daki R5 kayıtları kaza sonrası ekspertiz ve kampanya şikâyetleri, E-Tech arızaları ise Megane E-Tech'e ait. |
| 3 | Talisman | 2016-2022 | 1.6 dCi / 1.5 dCi (EDC) | ✓ 1 sorun (+1 ortak aile) |
| 3 | Twingo III | 2014-2019 | 0.9 TCe 90 (H4Bt) / 1.0 SCe 70 | ○ sırada |

### Volkswagen

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Golf 6 / Jetta | 2008-2013 | 1.6 TDI 90/105 (CAYC) | ✓ 2 sorun |
| 1 | Golf 7 | 2012-2019 | 1.4 TSI 122/140 (EA211) | ✓ 2 sorun (+1 ortak aile), 1 yıl kırılımı |
| 1 | Golf 7 | 2012-2019 | 1.6 TDI 90/105/110 | ✓ 1 sorun (+1 ortak aile) |
| 1 | Golf 7 / 7.5 | 2012-2020 | Tüm motorlar (model geneli) | ✓ 2 sorun, 1 yıl kırılımı — Cam tavan çerçevesi çatlağı ve bagaja su alma iki sitede doğrulandı. DonanımHaber'deki 27 maddelik Golf 7 listesinde kabine su alma (2012-2013), far ve sis buğulanması, 6.5" ekran kararması (2015), tavan kaplaması sarkması, arka silecek su sızdırması gibi maddeler var; bu maddeler yalnızca bu listede geçtiği için (ikinci bağımsız site bulunamadı) kayıt açılmadı; başlıktaki birçok kullanıcı listenin bir kısmına itiraz ediyor. |
| 1 | Golf 8 / 8.5 | 2020- | Tüm motorlar (model geneli) | ✓ 2 sorun — Multimedya ve SOS hatası iki sitede doğrulandı. Şikâyetvar'da sürüş asistanlarının (Travel Assist, ACC, Front Assist) birlikte devre dışı kalması ve DonanımHaber'de trafik işareti tanımanın yanlış hız sınırı uygulaması, start-stop hatası, park sensörü / arka kamera hatası ve 'bileşen koruma' uyarısı tek kaynakta ya da tek başlıkta kaldı. Far ve kapı için kaynak çıkmadı. |
| 1 | Passat B7 | 2010-2014 | 1.6 TDI (CAYC) | ✓ 1 sorun (+1 ortak aile) |
| 1 | Passat B7 | 2010-2014 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da tavan ile ön ve arka cam birleşiminde boya atması (2011-2012 modeller), sunroof çerçevesinde çatlak ve su alma (yaklaşık 55 bin TL teklif) çok sayıda kayıtta geçiyor; DonanımHaber'de B7 için yalnızca 2012 tarihli bir başlıkta konsol gıcırtısı ve start-stop memnuniyetsizliği var. Uluslararası forumlarda (VWVortex) panoramik cam tavan su sızıntısı konuşuluyor ama bunlar B7 / B8 Avrupa kasasına bağlanamadı; ikinci bağımsız site yok. |
| 1 | Passat B8 | 2015-2023 | 1.6 TDI | ✓ 2 sorun (+1 ortak aile) |
| 1 | Passat B8 | 2015-2023 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da cam tavan çerçevesinin kendiliğinden çatlaması ve su sızması (üç yıl sonra aynı sorunun yeniden çıkması, yaklaşık 35 bin TL parça bedeli), tavan kenar çıtası çatlağı, tavan ile ön cam birleşiminde boya atması ve 2015 modelde multimedya Bluetooth ses sorunu çok sayıda şikâyette geçiyor. DonanımHaber'de B8'e özgü ikinci kaynak çıkmadı (2021 Passat'ta 25 bin km'de cam tavan tıkırtısı tek başlık); bu yüzden kayıt açılmadı. VWVortex'te panoramik cam tavan su sızıntısı başlıkları var ama çoğu ABD'deki Passat'a ait ve B8 Avrupa kasasına bağlanamadı; tahliye hortumu tıkanması en sık neden olarak anılıyor. |
| 1 | Polo 6R / 6C | 2009-2017 | 1.2 TSI 90/105/110 | ✓ 2 sorun, 2 yıl kırılımı |
| 1 | Polo 6R / 6C | 2009-2017 | 1.4 TDI 75/90 (BMT, 3 silindir) | – eklenmedi: Faz 9'da arandı: DonanımHaber'de 2016 model 1.4 TDI 90 PS için enjektör dönüş hortumu kaçağı ve marş sorunu başlığı var; Şikâyetvar'da 2014 model 1.4 TDI'da turbonun dört kez yapıldığı (47.000 TL ödenmiş) ve 2016 modelde 95 bin km'de su eksiltme ile blok çatlağı gibi tekil vakalar çıktı. Otopark'taki Polo turbo başlığı turbo hortumu çatlağı anlatıyor ve motor tipi net değil; her sorun tek siteyle sınırlı kaldı. |
| 1 | Polo 6R / 6C / AW | 2009- | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da tavan döşemesi sarkması (2011-2012 modeller), tavan-ön cam birleşiminde boya atması, marşpiyel boya akması (bayi fabrikasyon hata dedi), klimanın kendiliğinden açılması ve multimedya ekranının kapanması geçiyor; DonanımHaber sonuçları 1998-2000 Polo'ya ait olduğundan ikinci site bulunamadı. |
| 1 | Polo AW | 2018- | 1.0 TSI 95/110 | ✓ 1 sorun (+1 ortak aile) |
| 1 | Polo AW | 2018- | 1.0 MPI 65/75 | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da turbosuz 1.0 Polo'da 12.000 km'de yağ uyarısı ve yaklaşık 2 litre takviye anlatılıyor (tek vaka, servis normal bulmuş); DonanımHaber'deki rölanti titremesi başlıkları ve DSG şikâyetleri 1.0 TSI'ya ait. MPI 65/75 için tekrar eden sorun çıkmadı. |
| 1 | T-Roc | 2018- | 1.5 TSI 150 (EA211 evo) | ✓ 1 sorun (+1 ortak aile) |
| 1 | T-Roc | 2018- | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da silecek sesi ve silme performansı (kronik diyenler var), motor ısındıktan sonra şıkırtı, multimedya arızası, ayna altı LED aydınlatma (garanti dışı 3-4 bin TL) ve cam açma mekanizması şikâyetleri tekrar ediyor; DonanımHaber ve Ekşi Sözlük'te T-Roc'a özgü ikinci site çıkmadı. |
| 1 | Tiguan (AD1) | 2016-2024 | Tüm motorlar (model geneli) | ✓ 1 sorun — Cam tavan su sızması iki sitede geçiyor. Şikâyetvar'da ayrıca ön ve arka farlarda su alması (2025 R-Line), sürüş asistanı (front assist) hataları ve multimedya ekranın kapanması var; bunlar tek sitede kaldı. |
| 1 | Tiguan 5N | 2008-2016 | 1.4 TSI 122/150/160 (EA111) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tiguan AD1 | 2016- | 1.5 TSI 150 (EA211 evo) | ✓ 1 sorun (+1 ortak aile) |
| 1 | Tiguan AD1 | 2016-2020 | 1.4 TSI 125/150 (ACT) | ◐ 1 ortak aile sorunu — Faz 9'da arandı: Tiguan 1.4 TSI için piston kırılması, titreme ve yağ eksiltme anlatılarının çoğu 2010-2013 (5N) modellere ait; AD1 dönemi için Şikâyetvar'da 2024 model bir Tiguan'da 7-8 bin km'de yağ eksiltme uyarısı (motor tipi belirtilmiyor) ve 2021 model bir Tiguan'da mekatronik kartı arızası gibi tekil kayıtlar var. Gösterilen devirdaim sorunu aynı motoru kullanan Octavia A7 ve Golf 7 kayıtlarına dayanır. |
| 2 | Caddy | 2010-2015 | 1.6 TDI (EA189) | ✓ 1 sorun |
| 2 | Caddy | 2015-2020 | 2.0 TDI | – eklenmedi: 2.0 TDI için Caddy'ye özgü kaynaklar Şikâyetvar (DPF, AdBlue) ile sınırlı; ikinci bağımsız kaynak bulunamadı. |
| 2 | Caddy (2K / SA) | 2010-2020 | Tüm motorlar (model geneli) | – eklenmedi: DonanımHaber'deki kayar kapı kilidi ve merkezi kilit anlatıları 2006-2007 model Caddy'lere ait (aranan nesil dışında); Şikâyetvar'da kayar kapı sesi, tavan sesi ve tavan klimasından uğultu ile 2025 model bir araçta su alma tekil şikâyetler. Caddy 2K / SA'ya özgü ikinci site yok. |
| 2 | Caddy SA | 2015-2020 | 1.6 TDI 102 (EA288) | ◐ 1 ortak aile sorunu — Caddy SA 1.6 TDI'ya özgü kaynak aranmadı; gösterilen EGR / DPF sorunu 1.6 TDI kayıtlarının ortak kaynaklarına dayanır. |
| 2 | Crafter | 2006- | 2.0 TDI | – eklenmedi: Bu oturumdaki aramada Şikâyetvar'da enjektör (2015 Crafter'da enjektörün yerinden fırlaması), turbo (2020 modelde turbo hortumu ve turbo değişimine rağmen süren arıza), yağ basıncı uyarısı (2016 model) ve rot-balans gibi tekil şikâyetler çıktı; Otopark'ta Crafter için olumlu yorumlar var (makyajlı 2.0 BiTDI'da kronik sorunların daha az olduğu yazılıyor). İkinci bağımsız kaynakla doğrulanan tekrar eden sorun çıkmadı. |
| 2 | Golf 6 | 2008-2013 | 1.2 TSI 105 (EA111, manuel ve DSG) | ◐ 4 ortak aile sorunu, 2 yıl kırılımı — Golf 6 1.2 TSI'ya özgü kaynak aranmadı; gösterilen sorunlar aynı motorları kullanan Polo 6R ve Octavia A5 (1.2 TSI), Golf 6 1.4 TSI (zincir) ve DQ200 DSG kayıtlarına dayanır. |
| 2 | Golf 7 | 2012-2019 | 1.2 TSI 85/105 | ✓ 1 sorun |
| 2 | Golf 7.5 | 2017-2020 | 1.5 TSI 130/150 (ACT) | ◐ 2 ortak aile sorunu — Golf 7.5'a özgü kaynak sınırlı: DonanımHaber'de tek başlık var (Golf 1.5 TSI ACT 150, iki silindir modunda titreme); sahibi 2020 model diyor ve Golf 7.5 / Golf 8 ayrımı yapılamıyor. 'Golf 7 yağ eksiltme sorunu' başlığındaki anlatılar ağırlıkla 1.2 / 1.4 TSI'ya ait. Gösterilen sorunlar aynı motoru kullanan Karoq, Passat ve Tiguan kayıtlarına dayanır. |
| 2 | Golf 8 | 2020- | 1.0 eTSI / 1.5 eTSI (48V hafif hibrit) | ✓ 2 sorun (+2 ortak aile), 1 yıl kırılımı |
| 2 | ID.4 / ID.3 / ID.7 | 2022- | Elektrik | – eklenmedi: Ekim 2026'da Avrupa'da ID.3, ID.4, ID.7, ID. Buzz ve Cupra Born'un belirli partilerini kapsayan batarya geri çağırması (%80 şarj sınırı) duyuruldu; ABD'deki ID.4 geri çağırmalarının Zwickau ve Emden üretimi Avrupa araçlarını kapsamadığı yazılıyor, Türkiye'deki araçların kapsamı doğrulanamadı. Türkiye şikâyetleri (navigasyon, bağlantılı hizmetler, tabela okuma uyarısı) farklı konularda ve yalnızca Şikâyetvar ile Ekşi Sözlük'te. |
| 2 | Jetta | 2011-2013 | 1.4 TSI / 1.6 TDI | ✓ 4 sorun (+1 ortak aile), 1 yıl kırılımı |
| 2 | Jetta | 2013-2018 | 1.2 TSI / 1.4 TSI / 1.6 TDI (DQ200 DSG) | ✓ 1 sorun (+3 ortak aile) |
| 2 | Passat B7 | 2010-2014 | 2.0 TDI | – eklenmedi: Aramalarda 2.0 TDI'ya özgü tekrar eden sorun çıkmadı; forum yorumlarının çoğu eski PD motorlara (B6) ve DSG'ye ait, enjektör iddiaları tekil. Faz 7'de yeniden arandı: DonanımHaber'de 2.0 TDI için enjektör, EGR, zincir gergisi, turbo ve DPF sıralanıyor ancak kaynaklar PD motorlu B6 ve DSG'ye ait; B7 / B8 2.0 TDI'ya özgü tekrar eden bir sorun için ikinci bağımsız site yok. |
| 2 | Passat B7 | 2010-2014 | 1.4 TSI 122 (EA111) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — Passat B7 1.4 TSI'ya özgü kaynak çıkmadı; gösterilen zincir sorunu aynı EA111 motorunu kullanan Golf 6, Polo ve Tiguan kaynaklarına dayanır. |
| 2 | Passat B8 | 2015-2023 | 2.0 TDI | – eklenmedi: Aramalarda B8 2.0 TDI için EGR, DPF ya da AdBlue kaynaklı tekrar eden Türkçe kaynak çıkmadı; en çok DSG şikâyeti var (B8 1.6 TDI kaydında). Faz 7'de yeniden arandı: DonanımHaber'de 2.0 TDI için enjektör, EGR, zincir gergisi, turbo ve DPF sıralanıyor ancak kaynaklar PD motorlu B6 ve DSG'ye ait; B7 / B8 2.0 TDI'ya özgü tekrar eden bir sorun için ikinci bağımsız site yok. Faz 8: 1.5 TSI bu satırdan ayrıldı ve kayıtlandı (Passat B8 1.5 TSI 150, yağ eksiltme). |
| 2 | Passat B8 | 2015-2023 | 1.5 TSI 150 (ACT) | ✓ 1 sorun (+1 ortak aile) |
| 2 | Passat B8 | 2015-2023 | 1.4 TSI 125/150 (EA211, ACT) | ◐ 1 ortak aile sorunu — Passat B8 1.4 TSI'ya özgü kaynak çıkmadı; gösterilen devirdaim sorunu aynı motoru kullanan Octavia A7 ve Golf 7 kaynaklarına dayanır. |
| 2 | Passat CC | 2008-2017 | 2.0 TDI / 1.4 TSI (DSG) | – eklenmedi: Faz 9'da arandı: Passat CC'ye özgü kaynak çıkmadı; DSG kavrama / mekatronik, 2.0 TDI yağ tüketimi (2015 model, yaklaşık 500 km'de 1 litre) ve yağ pompası değişimi anlatıları B7 ve sonrası Passat'lara ait (DSG sorunları Passat B8 ve B6 kayıtlarında). |
| 2 | Polo 6R / 6C | 2009-2017 | 1.6 TDI | ✓ 1 sorun (+1 ortak aile) |
| 2 | Polo Sedan | 2010-2017 | 1.4 / 1.6 MPI, 1.6 TDI | – eklenmedi: Faz 9'da arandı: Polo Sedan / Vento'ya özgü kaynak çıkmadı; sonuçlar genel Polo şikâyetleri ve DSG ('Hata: Şanzıman', mikro şalter, mekatronik) üzerine; 1.6 benzinli Polo'da zamanlama zinciri ve yağ yakma eğilimi genel bir forum derlemesinde geçiyor. |
| 2 | Sharan 7N | 2010-2020 | 2.0 TDI / 1.4 TSI | – eklenmedi: Sharan'a özgü sonuç çıkmadı; sonuçlar VW DSG geneline ait (Şikâyetvar'da Passat, Tiguan ve Caddy vakaları). Bir forum kullanıcısı 2.0 TDI'larda 6 ileri DQ250 kullanıldığını ve nadiren sorun çıkardığını yazıyor; Sharan 7N'nin şanzıman kodu doğrulanamadı. |
| 2 | T-Cross / Taigo | 2019- | 1.0 TSI 95/110 (DSG) | ◐ 2 ortak aile sorunu — Faz 9'da arandı: Şikâyetvar'da sıfır bir T-Cross 1.0 DSG'de acil işletim ve geri vites uyarıları ile 2025 model 1.0 TSI 116 PS DSG'de servisin şanzıman arızasını kullanıcı hatası saydığı bir şikâyet var (tekil vakalar); 1.0 TSI zincir ve yağ tüketimi DonanımHaber'de motor genelinde anılıyor. T-Cross'a özgü ikinci kaynak çıkmadı; gösterilen DSG sorunları DQ200 kayıtlarına dayanır. |
| 2 | T-Roc | 2018- | 1.0 TSI 115 | ◐ 2 ortak aile sorunu — Faz 9'da arandı: T-Roc yağ eksiltme şikâyetleri 1.5 TSI'ya ve 2022 modellere ait, DSG şikâyetleri genel T-Roc DSG'sine ait; DonanımHaber'de 1.0 TSI zincir ve yağ tüketimi motor genelinde anılıyor. 1.0 TSI 115'e özgü kaynak çıkmadı (yağ eksiltme T-Roc 1.5 TSI kaydında). Gösterilen DSG sorunları DQ200 kayıtlarına dayanır. |
| 2 | Tiguan 5N | 2008-2016 | 2.0 TDI | – eklenmedi: 5N 2.0 TDI'ya özgü turbo, EGR, DPF ya da zincir sorunu için kaynak çıkmadı; sonuçlar 1.4 TSI ve genel Passat 2.0 TDI yorumlarına ait. |
| 2 | Tiguan AD1 | 2016- | 2.0 TDI | ✓ 1 sorun |
| 2 | Touran | 2010-2022 | 2.0 TDI (DSG) | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da Touran için yalnızca 2 şikâyet var (parça temini, antifriz kaçağı); Touran'a özgü ikinci kaynak çıkmadı. |
| 2 | Touran 1T3 | 2010-2015 | 1.4 TSI 140 / 1.6 TDI 105 | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — Şikâyetvar'da Touran için yalnızca 2 şikâyet var (parça temini, antifriz kaçağı); Touran'a özgü ikinci kaynak çıkmadı. Gösterilen sorunlar aynı motorları kullanan diğer VAG kayıtlarına dayanır. |
| 2 | Touran 5T | 2015-2022 | 1.4 TSI 125/150 / 1.6 TDI 115 | ◐ 2 ortak aile sorunu — Şikâyetvar'da Touran için yalnızca 2 şikâyet var (parça temini, antifriz kaçağı); Touran'a özgü ikinci kaynak çıkmadı. Gösterilen sorunlar aynı motorları kullanan diğer VAG kayıtlarına dayanır. |
| 3 | Amarok | 2010- | 2.0 TDI / BiTDI | – eklenmedi: Faz 9'da arandı: DonanımHaber'de 2011 model 2.0 TDI 4x2 bir Amarok'ta yağ basıncı lambası ve yağ pompası değişimi (tek vaka), Şikâyetvar'da 2011 ve 2024 model turbo arızaları var; şanzıman kayıtları V6'ya ait; DPF için kayıt çıkmadı. Aynı sorun iki siteyle doğrulanmadı. |
| 3 | Arteon | 2017-2023 | 1.5 TSI 150 (ACT, DSG) | ◐ 2 ortak aile sorunu — DonanımHaber ve Otopark'ta Arteon 1.5 TSI test ve ilk sürüş başlıkları var, arıza anlatısı yok; Şikâyetvar'daki tek Arteon DSG şikâyeti (2018 model, mekatronik değişiminden sonra şanzıman yağı eksik) 1.5 TSI'ya bağlanamıyor. Gösterilen sorunlar aynı motoru kullanan Karoq, Passat ve Tiguan kayıtlarına dayanır. |
| 3 | Beetle | 2011-2019 | 1.2 TSI / 1.4 TSI | ○ sırada |
| 3 | Golf Sportsvan | 2014-2020 | 1.2 / 1.4 TSI, 1.6 TDI | ○ sırada |
| 3 | Passat B7 | 2010-2014 | 2.0 TDI (CFFB / CBAB) | – eklenmedi: B7'ye özgü zincir ya da yüksek basınç pompası kaynağı çıkmadı; enjektör anlatıları PD motorlu B6 kaydında. |
| 3 | Passat B9 | 2024- | 1.5 eTSI (48V hafif hibrit, DSG) | ◐ 3 ortak aile sorunu — B9 için bulunan başlıklar plug-in hibrit (E-Hybrid) sürümüne ait; 1.5 eTSI (48V hafif hibrit) için B9'a özgü Şikâyetvar ya da forum kaydı çıkmadı. Gösterilen sorunlar aynı motor ve 48V sistemini kullanan Superb IV, Octavia A8, Golf 8 kayıtlarına dayanır. |
| 3 | Scirocco | 2008-2017 | 1.4 TSI / 2.0 TSI / 2.0 TDI | ○ sırada |
| 3 | Touareg | 2010- | 3.0 TDI | ○ sırada |
| 3 | Transporter T5 / T6 | 2003- | 2.0 TDI | – eklenmedi: T5 / T6 2.0 TDI için kronik arıza listesi çıkmadı; yalnızca tekil enjektör ve turbo anlatıları. |
| 3 | up! | 2011-2023 | 1.0 MPI | ○ sırada |

### Toyota

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C-HR | 2016- | 1.2 Turbo (8NR-FTS) | – eklenmedi: Yağ yakma ve şanzıman anıları motor tipi belirtilmeden, tek tek vaka; iki bağımsız site bulunamadı. |
| 1 | C-HR | 2016- | 1.8 Hybrid (2ZR-FXE) | – eklenmedi: Hibrit sistem uyarısı dışında tekrar eden mekanik sorun bulunamadı. |
| 1 | Corolla E150 FL / E170 | 2009-2018 | 1.33 Dual VVT-i 99 | ✓ 1 sorun |
| 1 | Corolla E170 / E210 | 2013- | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da multimedya ekranında nikelaj kabarması (2021), USB için FAT32 / 32 GB sınırı, yazılım güncellenmemesi (2020), klima kompresörü (2021, tek vaka), 2021 modelde akü sorunu ve stop lambası içi çatlak tekil; DonanımHaber'de ise genel multimedya başlığı var. Şikâyetvar'daki kronik boya sorunu 2010-2013 (E140 / E150) modellere ait. E170 / E210'a özgü iki bağımsız site çıkmadı. |
| 1 | Corolla E210 | 2019- | 1.5 Dynamic Force (M15A-FKS) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Corolla E210 | 2019- | 1.8 Hybrid (2ZR-FXE) | – eklenmedi: Şikâyetler ses yalıtımı, fren diski paslanması ve 12V akü gibi mekanik olmayan konularda; tekrar eden mekanik sorun bulunamadı. |
| 1 | Yaris XP130 | 2011-2020 | 1.33 Dual VVT-i 99 (1NR-FE) | ◐ 1 ortak aile sorunu — Şikâyetler yeni nesil Yaris Hybrid ve Yaris Cross akü ve garanti konularında; 2011-2019 Yaris için tekrar eden mekanik sorun bulunamadı. Gösterilen yağ tüketimi Corolla E150 FL / E170 (1.33) kaydına dayanır. |
| 2 | Auris | 2013-2018 | 1.6 (benzinli) | – eklenmedi: Auris 1.6 benzinli için kaynak yok. |
| 2 | Auris E180 | 2013-2018 | 1.33 Dual VVT-i 99 (1NR-FE) | ◐ 1 ortak aile sorunu — 1.33'te yağ tüketimi ve oksijen sensörü tekil şikâyetler; gösterilen yağ tüketimi Corolla 1.33 kaydına dayanır. 1.4 D-4D, Faz 4'te ayrı satır ve kayıt olarak eklendi. |
| 2 | Corolla E170 | 2013-2018 | 1.4 D-4D 90 (1ND-TV) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — Aramalar E150 ve E170 ayrımı yapmıyor; turbo ve DPF anıları dağınık. Gösterilen yağ tüketimi ve enjektör sorunları aynı 1ND-TV motorunu kullanan Corolla E150 ve Auris kayıtlarına dayanır. |
| 2 | Corolla E170 | 2013-2018 | 1.6 Valvematic (Multidrive S) | – eklenmedi: Şikâyet sitelerinde 1.6 Valvematic ve Multidrive S için tekrar eden bir sorun kümesi bulunamadı. |
| 2 | Verso | 2009-2018 | 1.6 D-4D / 1.8 Valvematic | – eklenmedi: Şikâyetvar'da 1.6 D-4D için krank kasnağının kırılması (yolda kalma, yaklaşık 4.500 TL onarım ve garanti reddi) iki ayrı kullanıcıda geçiyor; bir forumda Toyota Türkiye'nin 1.6 dizel iddialarını doğrulamadığı yazılıyor. 1.8 Valvematic / Multidrive için çıkan şikâyetler 2004-2007 MMT'li Verso'lara ait. Kilometre bilgisi ve ikinci bağımsız doğrulama yetersiz olduğundan kayıt açılmadı. |
| 2 | Yaris | 2011-2019 | 1.5 Hybrid | – eklenmedi: Şikâyetler yeni nesil Yaris Hybrid ve Yaris Cross akü ve garanti konularında; 2011-2019 Yaris için tekrar eden mekanik sorun bulunamadı. |
| 2 | Yaris XP130 | 2011-2020 | 1.4 D-4D 90 (1ND-TV) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — Yaris 1.4 D-4D'ye özgü kaynak aranmadı; gösterilen yağ tüketimi ve enjektör sorunları Corolla E150 ve Auris (1ND-TV) kayıtlarına dayanır. |
| 2 | Yaris XP210 | 2020- | 1.5 Dynamic Force 125 (M15A-FKS) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — Yaris XP210 benzinli 1.5'e özgü kaynak aranmadı; şikâyetler çoğunlukla hibrit akü ve garanti konularında. Gösterilen krank ve biyel yatağı sarması aynı M15A-FKS motorunu kullanan Corolla E210 kaydına dayanır. |
| 3 | Auris | 2007-2018 | 1.4 D-4D (1ND-TV) | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 3 | Avensis | 2011-2018 | 2.0 D-4D | – eklenmedi: Avensis 2.0 D-4D için güvenilir bir kronik sorun listesi çıkmadı; yalnızca tekil şikâyetler. |
| 3 | Corolla E150 | 2007-2013 | 1.4 D-4D (1ND-TV) | ✓ 2 sorun, 1 yıl kırılımı |
| 3 | Land Cruiser Prado | 2009- | 3.0 D-4D / 2.7 | ○ sırada |
| 3 | Proace / Proace City | 2013- | 1.6 / 2.0 D-4D | ○ sırada |
| 3 | RAV4 / Hilux | 2013- | 2.0 / 2.5 Hybrid / 2.4 D-4D | – eklenmedi: RAV4 için sistematik sorun çıkmadı; Hilux 2.4 DPF / PCS arıza şikâyetleri yalnızca Şikâyetvar'da (ikinci bağımsız kaynak yok). |

### Fiat

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Doblo | 2010-2022 | 1.3 / 1.6 Multijet (90/105/120) | ✓ 3 sorun (+2 ortak aile) |
| 1 | Doblo | 2010-2022 | Tüm motorlar (model geneli) | ✓ 1 sorun — Kapı kilidi arızası Şikâyetvar ve DonanımHaber'de doğrulandı. Şikâyetvar'da kapı üstünden su alma (yeni araçta), sürgülü kapı sesi ve sarkması, 2025 model fren ve direksiyon arızaları tek şikâyet; ön takım su alma, elektrik ve klima için kaynak çıkmadı. |
| 1 | Egea | 2015- | 1.4 Fire 95 | ✓ 1 sorun |
| 1 | Egea | 2015- | 1.3 Multijet II 95 | ✓ 2 sorun (+3 ortak aile) |
| 1 | Egea | 2015- | 1.6 Multijet II 120 | ✓ 3 sorun |
| 1 | Egea / Egea Cross | 2015- | Tüm motorlar (model geneli) | ✓ 2 sorun — Klima kompresörü uğultusu ve boya atması iki sitede doğrulandı. Şikâyetvar'da ayrıca ön takım ve debriyaj sesleri ile Cross'ta tavan çıtalarının solması geçiyor; ikinci site yok. |
| 1 | Linea | 2007-2015 | 1.3 Multijet (Dualogic) | ✓ 4 sorun (+3 ortak aile) |
| 1 | Linea | 2007-2015 | Tüm motorlar (model geneli) | ✓ 1 sorun — Airbag üstü torpido çatlağı Şikâyetvar'da çok sayıda şikâyetle, fiatforum'da Punto Evo / Grande Punto başlıklarıyla doğrulandı. Şikâyetvar'da boya atması (ön direk, tavan), ESP kaynaklı direksiyon kilitlenmesi (Panda, Punto ve Linea için kronik denmiş) ve direksiyon sesi tek sitede kaldı. |
| 1 | Punto Evo / Grande Punto | 2009-2018 | Tüm motorlar (model geneli) | ✓ 1 sorun — Airbag üstü torpido çatlağı Şikâyetvar ve fiatforum'da doğrulandı. |
| 2 | 500 | 2008- | 1.2 Fire / 0.9 TwinAir | ✓ 1 sorun |
| 2 | 500 Dualogic | 2008- | 0.9 TwinAir / 1.2 Fire (Dualogic) | ◐ 2 ortak aile sorunu — 500 Dualogic'e özgü kaynak aranmadı; gösterilen hidrolik ünite, aktüatör ve kavrama sorunları aynı Dualogic şanzımanı kullanan Linea kaydına dayanır. |
| 2 | 500X | 2015- | 1.4 MultiAir / 1.3 FireFly Turbo | ○ sırada |
| 2 | 500X | 2015- | 1.6 MultiJet 120 | ◐ 2 ortak aile sorunu — 500X'e özgü kaynak aranmadı; gösterilen çift kütleli volan ve EGR / DPF sorunları aynı Multijet II motorunu kullanan Egea 1.6 kaydına dayanır. |
| 2 | 500e | 2021- | Elektrik (42 kWh) | – eklenmedi: Şikâyetvar'da şarj sorunları ve batarya arızası (menzil göstergesinin 320 km'den 260 km'ye düşmesi) tekil; DonanımHaber yorumu olumlu, Ekşi Sözlük yorumları ABD'deki eski modellere ait. |
| 2 | 600e | 2024- | Elektrik (54 kWh, 156 PS) | ✓ 1 sorun |
| 2 | Bravo | 2007-2014 | 1.4 T-Jet / 1.6 Multijet | ○ sırada |
| 2 | Egea | 2016- | 1.6 E-Torq 110 | – eklenmedi: Aramalarda öne çıkan kronik sorun bulunamadı. |
| 2 | Egea Hybrid | 2022- | 1.5 Hybrid 130 (48V hafif hibrit, çift kavramalı) | ✓ 1 sorun |
| 2 | Linea | 2007-2015 | 1.4 Fire / 1.4 T-Jet | – eklenmedi: Dağınık şikâyetler var, tekrar eden bir sorun için iki bağımsız site bulunamadı. |
| 2 | Linea | 2011-2015 | 1.6 Multijet 105 | – eklenmedi: Faz 9'da arandı: Şikâyetvar'ın Linea 1.6 Multijet şikâyetlerinde en çok tekrarlanan konu yolcu hava yastığı bölgesinde göğüs paneli çatlağı ve Blue&Me arızası; sıcak motorda zor çalışma ayrı bir şikâyet. EGR, enjektör ve turbo iddiaları genel motor ailesine ait tek bir DonanımHaber başlığında. 1.4 T-Jet (turbo, yağ eksiltme) için sonuç çıkmadı; Dualogic sorunları Linea 1.3 Multijet kaydında. |
| 2 | Panda | 2012-2020 | 1.3 Multijet | ○ sırada |
| 2 | Panda | 2012-2020 | 0.9 TwinAir / 1.2 Fire (Dualogic) | ◐ 2 ortak aile sorunu — Panda 0.9 TwinAir için yağ tüketimi sonucu çıkmadı, motor yorumları genelde olumlu (şehir içinde yaklaşık 6 litre); Dualogic için DonanımHaber ve Ekşi Sözlük'te yağın azalıp katranlaşması, aktüatör pistonunda talaş birikimi (bir Lancia sahibinin anlatısı), vites yükseltmeme ve direksiyon sertleşmesi anlatıları var. Gösterilen hidrolik ünite, aktüatör ve kavrama sorunları aynı Dualogic şanzımanı kullanan Linea kaydına dayanır. |
| 2 | Punto Evo / Grande Punto | 2009-2018 | 1.3 Multijet 75/95 | ✓ 2 sorun (+5 ortak aile) |
| 2 | Punto Evo / Grande Punto | 2009-2018 | 1.4 Fire 77 | ✓ 2 sorun (+5 ortak aile) |
| 3 | 500L | 2013-2022 | 1.3 Multijet 95 | ◐ 5 ortak aile sorunu — 500L'e özgü kaynak aranmadı; gösterilen sorunlar aynı Multijet motorunu kullanan Doblo, Egea ve Linea kaynaklarına dayanır. |
| 3 | Ducato | 2010- | 2.2 / 2.3 MultiJet | – eklenmedi: AdBlue, DPF ve NOx sensörü şikâyetleri yalnızca Şikâyetvar'da; Boxer ve Jumper için ayrı veri çıkmadı. Bu oturumdaki aramada Şikâyetvar'da 2023 model 2.3'te tekrarlayan AdBlue / partikül / NOx sensörü arızaları, enjektör değişimine rağmen süren hata, turbo parçalarının motora kaçması ve debriyaj hidrolik hortumu kaçağı anlatıları var; DonanımHaber'de de Ducato debriyaj arızası başlığı çıktı. Debriyaj hidroliği iki sitede geçse de kilometre bilgisi ve tekrar örüntüsü yetersiz olduğu için kayıt açılmadı. |
| 3 | Fiorino / Qubo | 2008-2020 | 1.3 Multijet | ✓ 3 sorun (+3 ortak aile) |
| 3 | Fullback | 2016-2019 | 2.4 Dizel | ○ sırada |
| 3 | Grande Panda Electric | 2025- | Elektrik | – eklenmedi: Şikâyetvar'da şarj ve kilit sorunu sonrası 8 saat yol yardımı beklemek, şarj soketinin erimesi ve teslimde arıza ışığı tekil; tek taramada ikinci bağımsız site çıkmadı. |
| 3 | Linea / Punto | 2007-2015 | 1.4 T-Jet | – eklenmedi: T-Jet'e özgü kaynak çıkmadı; Punto şikâyetleri ağırlıkla direksiyon (EPS) üzerine ve ayrı kayıtta. |
| 3 | Scudo / Talento | 2007-2021 | 2.0 Multijet | ○ sırada |

### Hyundai

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Accent Blue | 2015-2019 | 1.6 CRDi 136 (7DCT) | ✓ 1 sorun (+3 ortak aile) |
| 1 | Accent Blue | 2011-2019 | 1.4 MPI | – eklenmedi: 1.4 MPI için tekrar eden sorun bulunamadı (yalnızca tek tek külbütör kapağı yağ kaçağı ve sübap iddiaları). Faz 7'de yeniden arandı: Şikâyetvar'da 1.4 CVT otomatiklerde kalkışta ve rampada çıtırdama ile yetkili serviste çözülemeyen şanzıman arızası şikâyetleri var; forumlarda aynı motorun taksilerde 400-500 bin km sorunsuz gittiği ve şanzıman yağ değişiminin sorunu azalttığı yazılıyor, bağımsız ikinci kaynak çıkmadı. |
| 1 | Accent Blue | 2011-2015 | 1.6 CRDi 128 (manuel / 6 ileri otomatik) | – eklenmedi: Faz 9'da arandı: tekil vakalar (2013 model 1.6 CRDi'da yağ seviyesinin yükselmesi ve enjektör temizliği; LPG sonrası enjektör arızası); DPF ve turbo için yıla özgü güvenilir kaynak yok, DPF konusunda forumlarda görüş ayrılığı var. Şikâyetlerin çoğu otomatik ve 2015-2016 DCT'li sürümlere ait (DCT sorunu Accent Blue 2015-2019 kaydında). |
| 1 | Accent Blue / Elantra AD | 2011-2020 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da Accent Blue'da kaput boya atması (2015 ve 2017), EPS uyarısı ve Elantra'da 2016 modelde ön kapı kollarının kilitlenince dışarıdan açılmaması (kilit tamircisi 2016 Elantra, i30, ix35 ve Tucson'da kronik demiş; Hyundai kronik kaydı olmadığını söylüyor), boya atması (2011-2016 ve 2021-2023) tekrar ediyor; DonanımHaber'de yalnızca 2013 tarihli sert arka süspansiyon konusu ve eski Accent Era boya başlığı var; ikinci bağımsız site yok. |
| 1 | Bayon | 2021- | 1.0 T-GDI 100/120 (7DCT) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Bayon | 2021- | 1.4 MPI 100 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Ioniq 5 / Ioniq 6 | 2022- | Elektrik (E-GMP) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tucson (TL FL) | 2018-2020 | 1.6 CRDi (7DCT) | ✓ 1 sorun (+2 ortak aile) |
| 1 | Tucson (TL) | 2015-2020 | 1.6 T-GDI (7DCT) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | i20 | 2020- | 1.0 T-GDI 100/120 (7DCT) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | i20 | 2020- | 1.4 MPI 100 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | i20 (GB) | 2014-2020 | 1.25 / 1.4 MPI, 1.4 CRDi | – eklenmedi: Faz 9'da arandı: i20 şikâyetleri otomatik şanzımanda toplanıyor (tork konvertörlü şanzıman çoğu yorumda sorunsuz, DCT'li BC3 kaydında); 1.4 MPI için forum yorumları sorunsuz diyor, 1.4 CRDi için enjektör, turbo ve silindir kapağı sıralaması genel bir forum listesinden geliyor. Kayıt açılacak kanıt çıkmadı. |
| 1 | i20 (PB / GB) | 2009-2020 | Tüm motorlar (model geneli) | ✓ 1 sorun — EPS arızası Şikâyetvar ve DonanımHaber'de geçiyor; hangi nesle ait olduğu şikâyetlerin çoğunda belirsiz (2011 PB ve 2015 GB örnekleri). Şikâyetvar'da yakıt pompası, akü boşalması, arka cam patlaması ve cam modülü / cam tuşu arızası tek sitede kaldı. |
| 1 | i30 GD | 2012-2017 | 1.6 CRDi | – eklenmedi: Turbo, DPF ve DCT anıları nesilleri karıştırıyor ve dağınık; model/motor bazında tekrar eden sorun için iki bağımsız site bulunamadı. Faz 7'de yeniden arandı: İngiltere forumlarında EGR tereddüdü ve çift kütleli volan, Türkçe kaynaklarda ise 'kronik sorun yok' yorumları ile tekil titreme, DPF ve DCT anıları var; Tucson 1.6 CRDi şikâyetleri i30'a taşınamaz, iki bağımsız site aynı sorunu doğrulamadı. |
| 1 | i30 PD | 2017-2023 | 1.6 CRDi 110/136 (6MT ve 7DCT) | ◐ 3 ortak aile sorunu — Turbo, DPF ve DCT anıları nesilleri karıştırıyor ve dağınık; i30'a özgü iki bağımsız site bulunamadı (Türkçe kaynaklarda 'kronik sorun yok' yorumları ile tekil titreme, DPF ve DCT anıları). Tucson 1.6 CRDi şikâyetleri i30'a taşınamaz; gösterilen DPF / yağa mazot karışması ve enjektör kodlama sorunları Tucson NX4, Rio UB ve Ceed kayıtlarına dayanır. Gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. |
| 2 | Accent Blue | 2011-2017 | 1.6 GDI 132/140 | ◐ 1 ortak aile sorunu — 1.6 GDI için tekrar eden sorun bulunamadı; gösterilen yağ tüketimi aynı Gamma GDI motorunu kullanan Sportage SL kaynaklarına dayanır. |
| 2 | Elantra | 2011-2020 | 1.6 MPI | – eklenmedi: 1.6 MPI için tekrar eden sorun bulunamadı. |
| 2 | Elantra AD | 2016-2020 | 1.6 CRDi 136 (7DCT) | ◐ 3 ortak aile sorunu — Elantra'da tek bir 7DCT kalkış titremesi şikâyeti dışında tekrar eden sorun bulunamadı; gösterilen DPF / yağa mazot karışması ve enjektör kodlama sorunları Tucson NX4, Rio UB ve Ceed kayıtlarına dayanır. Gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. |
| 2 | Kona Electric / Inster | 2021- | Elektrik (39,2 / 64 kWh) | – eklenmedi: Batarya yangını geri çağırması 2017-2020 arası üretimi kapsıyor; Türkiye'de elektrikli Kona'nın resmî satışı Eylül 2021'de başladı ve kapsam doğrulanamadı. Türkiye'deki batarya modülü arızası ve parça bekleme şikâyetleri yalnızca Şikâyetvar'da. Faz 6'da yeniden arandı (2. nesil Kona ve Inster dahil): Inster'de şarj sırasında duman ve teslim günü şarj olmama tekil, Kona'da batarya modülü arızası, parça bekleme ve %81'de şarjın sonlanması yalnızca Şikâyetvar'da; ikinci bağımsız site çıkmadı. |
| 2 | Tucson (NX4) | 2021- | 1.6 CRDi 136 (7DCT) | ✓ 2 sorun (+1 ortak aile) |
| 2 | Tucson (NX4) | 2021- | 1.6 T-GDI (7DCT) | – eklenmedi: Faz 9'da arandı: DonanımHaber'de 2025 model 1.6 DCT'li bir Tucson'da 35 bin km'de dişli kırılması anlatılıyor (tek vaka, motor tipi belirtilmiyor); Şikâyetvar'daki Tucson şanzıman şikâyetlerinin çoğu dizel araçlara ait; yağ yakma iddiaları 1.6 GDi ve 6 ileri otomatik konusunda. T-GDI'ya özgü tekrar eden sorun çıkmadı. 7DCT titremesi Tucson NX4 1.6 CRDi kaydında ele alındı. |
| 2 | Tucson (TL) | 2015-2018 | 1.7 CRDi 115/141 (6MT ve 7DCT) | ◐ 3 ortak aile sorunu — Faz 9'da arandı: 1.7 CRDi'ya özgü kaynak çıkmadı; Şikâyetvar'daki Tucson dizel DPF, enjektör ve turbo şikâyetleri 2021 ve sonrası modellere ait. Gösterilen DPF / yağa mazot karışması ve enjektör kodlama sorunları Tucson NX4, Rio UB ve Ceed kayıtlarına dayanır. Gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. |
| 2 | i20 (PB) | 2009-2014 | 1.4 MPI / 1.4 CRDi | ✓ 1 sorun (+2 ortak aile) |
| 2 | i30 | 2012-2020 | 1.4 / 1.6 MPI | – eklenmedi: Benzinli MPI motorlar için i30'a özgü kronik sorun çıkmadı; aramalar 1.6 CRDi (DPF) ve DCT şikâyetlerine yöneldi ve i30'a özgü olmayan kaynaklardan geldi. |
| 2 | i30 (FD) | 2008-2012 | 1.4 / 1.6 MPI, 1.6 GDI (EPS) | ✓ 1 sorun (+1 ortak aile) |
| 2 | i30 FD | 2008-2012 | Tüm motorlar (model geneli) | ✓ 1 sorun — EPS arızası Şikâyetvar ve DonanımHaber'de geçiyor; şikâyetlerin çoğu GD'den (2012-2017) eski modellere ait, GD için nesle özgü kanıt çıkmadı. Şikâyetvar'da i30 için sunroof kasasında çatlak ve boya atması tek sitede. |
| 2 | i30 GD | 2012-2017 | 1.6 GDI 135 | ◐ 1 ortak aile sorunu — i30 GD 1.6 GDI'ya özgü kaynak aranmadı; gösterilen yağ tüketimi aynı Gamma GDI motorunu kullanan Sportage SL kaynaklarına dayanır. |
| 2 | i30 PD | 2017-2023 | 1.0 T-GDI 120 / 1.4 T-GDI 140 (7DCT) | ◐ 1 ortak aile sorunu — T-GDI için i30'a özgü kronik sorun çıkmadı; aramalar 1.6 CRDi (DPF) ve DCT şikâyetlerine yöneldi ve i30'a özgü olmayan kaynaklardan geldi. Gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. |
| 2 | ix35 | 2010-2015 | 1.7 CRDi | – eklenmedi: 1.7 CRDi Türkiye'de neredeyse hiç satılmamış; şikâyetler iç trim, 4x4 şanzıman dişlisi ve LPG'li soğuk çalıştırma gibi tekil konularda. |
| 2 | ix35 | 2010-2015 | 1.6 GDI 135 | ◐ 1 ortak aile sorunu — Şikâyetler iç trim, 4x4 şanzıman dişlisi ve LPG'li soğuk çalıştırma gibi tekil konularda; gösterilen yağ tüketimi aynı Gamma GDI motorunu kullanan Sportage SL kaynaklarına dayanır. |
| 3 | Creta / Venue | 2019- | 1.5 / 1.6 MPI, 1.0 T-GDI | ○ sırada |
| 3 | Elantra / i10 | 2011- | 1.6 MPI otomatik, 1.0 / 1.25 | – eklenmedi: Elantra AD 1.6 MPI ve i10 için kronik motor sorunu çıkmadı; şikâyetler otomatik şanzıman (dizel), direksiyon ve ESP üzerine ve motor hacmi belirsiz. |
| 3 | H-1 / Starex | 2008- | 2.5 CRDi | – eklenmedi: H-1 / Starex 2.5 CRDi için enjektör, turbo ve EGR kanıtı çıkmadı; bulunanlar eski forum yorumları ve diğer modellere ait. |
| 3 | Kona | 2018- | 1.0 T-GDI | – eklenmedi: Kona 1.0 T-GDI için ilgili sonuç çıkmadı. |
| 3 | Kona | 2017-2023 | 1.6 CRDi 115/136 (7DCT) | ◐ 3 ortak aile sorunu — 1.6 CRDi DCT kalkış titremesi yalnızca Şikâyetvar kayıtlarında; ikinci bağımsız kaynak bulunamadı. Gösterilen DPF / yağa mazot karışması ve enjektör kodlama sorunları Tucson NX4, Rio UB ve Ceed kayıtlarına dayanır. Gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. |
| 3 | Kona | 2017-2023 | 1.6 T-GDI 177 (7DCT) | ◐ 1 ortak aile sorunu — Kona 1.6 T-GDI'ya özgü kaynak bulunamadı; gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. |
| 3 | i40 | 2011-2019 | 1.7 CRDi / 1.6 GDI | ○ sırada |
| 3 | ix35 / Santa Fe | 2010-2018 | 1.7 / 2.0 / 2.2 CRDi | – eklenmedi: ix35 1.7 / 2.0 CRDi ve Santa Fe 2.2 CRDi için model özelinde kaynak çıkmadı; bulunanlar ix35 1.6 GDI için tek rehber sitesi. 1.7 CRDi Türkiye'de neredeyse hiç satılmamış. |

### Peugeot

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | 208 / 2008 | 2012-2019 | Tüm motorlar (model geneli) | ✓ 1 sorun, 1 yıl kırılımı — Arka cam fitili iki sitede doğrulandı. Şikâyetvar'da dokunmatik ekran arızası (2020), teyp hoparlörü, otomatik far yükseklik ayarı (GT) ve kapı kilitlerinin çalışmaması tek şikâyet; fren, ön takım ve tavan su alma için kaynak çıkmadı. |
| 1 | 208 / 2008 / 308 / 3008 | 2014-2021 | 1.2 PureTech (EB2) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | 208 / 2008 / 308 / 3008 | 2012-2021 | 1.6 BlueHDi / e-HDi (DV6) | ✓ 4 sorun |
| 1 | 208 / 2008 / 308 / 3008 / 5008 | 2019- | 1.5 BlueHDi 100/130 (DV5) | ✓ 2 sorun (+1 ortak aile), 1 yıl kırılımı |
| 1 | 3008 | 2016- | Tüm motorlar (model geneli) | ✓ 1 sorun — Multimedya donması Şikâyetvar, DonanımHaber ve Ekşi Sözlük'te doğrulandı. Şikâyetvar'da elektrik ve akü boşalması (ekranların açık kalması, kapıların kilitlenmemesi), alternatör seti ve akü / PGA kutusu iddiası ve 2024 3008 Hybrid şikâyetleri tek sitede kaldı; cam tavan için kaynak çıkmadı. |
| 1 | 301 | 2012- | 1.6 HDi / BlueHDi (DV6) | ✓ 3 sorun (+1 ortak aile) |
| 1 | 301 / Citroën C-Elysée | 2012- | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da en çok tekrarlanan konu kapı içi, bagaj kapağı ve tavanda boya kabarması ve paslanma (301 ve C-Elysée'de, orijinal boyada; bir kullanıcıya yetkili servis her C-Elysée'nin %10'unda görüldüğünü söylemiş), ön / alt takım sesi (amortisör değişimine rağmen), cam sıyırıcı fitil erimesi ve C-Elysée'de arka stop farlarına su kaçağı tekrar ediyor; DonanımHaber'de yalnızca 2013 tarihli genel başlıklar var, ikinci bağımsız site çıkmadı. |
| 1 | e-208 / e-2008 | 2022- | Elektrik (50 kWh; 2024 sonrası 54 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | 207 | 2006-2014 | 1.6 HDi 90/110 (DV6) | ◐ 3 ortak aile sorunu — Peugeot 207 1.6 HDi'ya özgü kaynak aranmadı; gösterilen enjektör, turbo yağ süzgeci ve EGR / DPF sorunları aynı DV6 motorunu kullanan Peugeot 301, Citroën C-Elysée, Ford Focus ve Fiesta kaynaklarına dayanır. |
| 2 | 308 / 3008 | 2007-2014 | 1.6 THP (EP6) | ✓ 3 sorun, 1 yıl kırılımı |
| 2 | 308 T7 | 2007-2013 | 1.6 HDi / e-HDi 90/112 (DV6) | ◐ 3 ortak aile sorunu — 308 T7 1.6 HDi'ya özgü kaynak aranmadı; gösterilen enjektör, turbo yağ süzgeci ve EGR / DPF sorunları aynı DV6 motorunu kullanan Peugeot 301, Citroën C-Elysée, Ford Focus ve Fiesta kaynaklarına dayanır. |
| 2 | 508 | 2011-2018 | 1.6 THP 156/165 (EP6) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — 1.6 THP için tek bir kullanıcı 2011-2012 yüksek basınç pompası sorununu anıyor (308 / 3008 1.6 THP kaydına bakın). Gösterilen sorunlar aynı EP6 motorunu kullanan 308 / 3008 ve Mini Cooper S kaynaklarına dayanır. |
| 2 | Boxer | 2006- | 2.2 HDi / 2.0 BlueHDi | – eklenmedi: Şikâyetvar'da Boxer / Jumper için tekrar eden konular enjektör şakırtısı (enjektör değişiminden sonra da süren), debriyaj alt merkezi / hidrolik boru sızıntısı ve pedalın takılı kalması (bazı kullanıcılarda ilk 25.000 km'de), tek vaka turbo arızası ve AdBlue uyarıları; şikâyetlerin çoğu 2023 sonrası 2.2 BlueHDi 140 / 180 araçlara ait. Anlatılar tek siteye (Şikâyetvar) dayanıyor ve kilometre bilgisi kullanıcı beyanı; ikinci bağımsız kaynak çıkmadı. |
| 2 | Expert / Traveller | 2007- | 2.0 HDi / BlueHDi | – eklenmedi: Bu oturumdaki aramada 2.0 HDi / BlueHDi için kronik enjektör ya da DPF kaynağı çıkmadı; Şikâyetvar'da Expert 2.0 BlueHDi için geç marş ve şanzıman sesi, Jumpy için 2022 model bir araçta garanti kapsamında motor değişimi gibi tekil şikâyetler var; DonanımHaber'deki bir başlıkta eski 2.0 HDi'ların ilk sürümlerinin önerilmediği yazılıyor (yaklaşık 15 yıllık yorum). |
| 2 | Partner | 2008-2018 | 1.6 HDi 75/92/100/115 (DV6) | ◐ 3 ortak aile sorunu — Partner 1.6 HDi'ya özgü kaynak aranmadı (Berlingo ile aynı motor ve kasa); gösterilen enjektör, turbo yağ süzgeci ve EGR / DPF sorunları aynı DV6 motorunu kullanan Peugeot 301, Citroën C-Elysée, Ford Focus ve Fiesta kaynaklarına dayanır. |
| 2 | Rifter / Partner | 2018- | 1.5 BlueHDi 100/130 (DV5) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — Rifter / Partner 1.5 BlueHDi'ya özgü kaynak aranmadı; gösterilen eksantrik zinciri sorunu aynı DV5 motorunu kullanan Peugeot, Citroën, Opel Grandland ve Ford kaynaklarına, AdBlue sorunu Peugeot kaynaklarına dayanır. |
| 2 | e-3008 / e-5008 | 2024- | Elektrik | – eklenmedi: Şikâyetvar'da 2024 model e-3008 için seyir halinde 'elektrikli çekiş sistemi arızası' uyarısıyla durma ve şarj almama (çekici) şikâyetleri var. İkinci bağımsız site bulunamadı: Ekşi Sözlük ve DonanımHaber yorumları yalnızca gerçek menzil ve şarj eğrisi hakkında; SpeakEV'de batarya boyutu yazmayan tek bir erken e-3008 şikâyeti var; e-3008 / e-5008 için geri çağırma kaydı çıkmadı (ÖAMTC'nin 3008 / 508 kaydı plug-in hibritlere ait). |
| 2 | e-308 | 2023-2025 | Elektrik (54 kWh, 156 PS) | ✓ 1 sorun |
| 3 | 107 / 108 | 2005-2021 | 1.0 VTi | ○ sırada |
| 3 | 207 / 206 | 2006-2014 | 1.6 VTi (EP6) | – eklenmedi: EP6 zincir uzaması iddiası tek bir rehber sitesine (Araclo) dayanıyor; forum ve şikâyet kaynaklarında doğrulanmadı. |
| 3 | 301 | 2012- | 1.2 VTi / PureTech | ✓ 2 sorun (+1 ortak aile), 1 yıl kırılımı |
| 3 | 5008 I | 2009-2016 | 1.6 THP / 1.6 e-HDi / 2.0 HDi | ○ sırada |
| 3 | 508 | 2011-2018 | 1.6 e-HDi 115 (MCP / Auto6R robotize) | ✓ 1 sorun |
| 3 | 508 | 2011-2018 | 2.0 HDi | – eklenmedi: 2.0 HDi için kaynak bulunamadı. |

### Opel

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Astra H / J | 2005-2015 | 1.3 CDTI 90/95 (manuel ve Easytronic) | ✓ 4 sorun (+2 ortak aile) |
| 1 | Astra J | 2010-2015 | 1.4 Turbo (A14NET) | ✓ 1 sorun |
| 1 | Astra J | 2009-2015 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da tavanda kabarma ve boya atması (2015 ve 2017 model) ile kaputta boya atması, bcm beynine kaloriferden su sızması tekil; forumda Astra J'ye özgü kronik boya iddiası doğrulanamadı (sonuçlar Astra K ve eski modellere ait). |
| 1 | Astra K | 2015-2021 | 1.4 Turbo 125/150 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Astra K | 2015-2021 | Tüm motorlar (model geneli) | ✓ 2 sorun, 1 yıl kırılımı — Kolon kilidi arızası ve tavan boyası iki sitede doğrulandı. Şikâyetvar'da multimedya ekranının açılmaması (2022 model) ve direksiyon kutusu arızası (iki kez, 2016 model) tek şikâyet; far, ön cam ve kapı için kaynak çıkmadı. |
| 1 | Corsa D / E | 2006-2019 | 1.3 CDTI 75/95 | ✓ 2 sorun (+9 ortak aile) |
| 1 | Mokka / Mokka X | 2012-2020 | 1.4 Turbo (A14NET) | ◐ 1 ortak aile sorunu — Mokka'ya özgü, A14NET'i açıkça belirten tekrar eden bir şikâyet bulunamadı. Faz 7'de yeniden arandı: Mokka şikâyetleri (47.000 km'de triger kayışı, yağ-su karışması, yağ kaçağı) motor tipini belirtmiyor ya da 1.2 PureTech'e ait. Gösterilen PCV diyaframı ve emme manifoldu valfi sorunu aynı A14NET motorunu kullanan Astra J kaydına dayanır. |
| 2 | Astra Electric | 2023-2025 | Elektrik (54 kWh, 156 PS) | ✓ 2 sorun, 2 yıl kırılımı |
| 2 | Astra J | 2013-2015 | 1.6 CDTI 110/136 | ✓ 1 sorun (+1 ortak aile) |
| 2 | Astra J | 2010-2015 | 1.6 benzinli atmosferik (Ecotec) | ✓ 1 sorun |
| 2 | Astra K | 2015-2021 | 1.6 CDTI 110/136 | ✓ 1 sorun (+1 ortak aile) |
| 2 | Combo D | 2011-2018 | 1.3 CDTI 90 (Multijet) | ◐ 5 ortak aile sorunu — Combo D'ye özgü kaynak aranmadı (Fiat Doblo ile aynı platform ve motor); gösterilen sorunlar Doblo, Fiorino ve Egea kaynaklarına dayanır. |
| 2 | Corsa D | 2006-2014 | Tüm motorlar (model geneli) | ✓ 1 sorun — Direksiyon sesi DonanımHaber ve Ekşi Sözlük'te geçiyor (nedeni belirsiz). Corsa D için kapı elektriği ve ön takım için kaynak çıkmadı; Şikâyetvar'daki 'yakıt göstergesi' şikâyeti 2021 model araca ait. |
| 2 | Corsa D / E | 2006-2019 | 1.2 / 1.4 benzinli (A12XER, A14XER) | – eklenmedi: Aramalarda A12XER/A14XER için kronik sorun bulunamadı; sonuçlar PureTech'e ait. |
| 2 | Corsa E / F | 2014- | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da (çoğu Corsa F) multimedya ekranı kararması / CarPlay kesintisi ve siyah tavanda boya atması tekrar ediyor; DonanımHaber ve Ekşi Sözlük'te Corsa E / F'ye özgü ikinci site çıkmadı. |
| 2 | Corsa-e / Mokka-e | 2020- | Elektrik (50 kWh; 2024 sonrası Mokka'da 54 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Crossland / Corsa F | 2017- | 1.2 PureTech 83/100/110/130 | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 2 | Insignia A | 2014-2017 | 1.6 CDTI 136 | ✓ 2 sorun |
| 2 | Insignia A | 2008-2017 | 2.0 CDTI / 1.6 Turbo | – eklenmedi: Turbo hortumu sorunu 1.6 CDTI kaydında var; 1.6 Turbo'da zincir ve yağ soğutucusu için motor sürümü belirsiz tekil yorumlar, 2.0 CDTI için tekil kayıt çıktı. |
| 2 | Insignia A | 2008-2017 | 1.6 115 (A16XER) | ◐ 1 ortak aile sorunu — Insignia 1.6 benzinliye özgü kaynak aranmadı; gösterilen termostat gövdesi, soğutma suyu eksilmesi ve yağ soğutucu sorunu aynı A16XER motorunu kullanan Astra J kaydına dayanır. |
| 2 | Insignia B | 2017-2022 | 1.5 Turbo / 2.0 CDTI | ○ sırada |
| 2 | Insignia B | 2017-2022 | 1.6 CDTI 136 | ◐ 2 ortak aile sorunu — Bu oturumdaki aramada Insignia B (GrandSport) 1.6 CDTI için DonanımHaber, Şikâyetvar ve Ekşi Sözlük'te turbo hortumunun bağlantı yerinden yırtılması (50 bin ve 72 bin km vakaları), enjektör şakırtısı ve zincir sesi anlatıları, otomatik şanzımanda titreme ve selenoid arızası (Şikâyetvar'da 187 bin km'de 202 bin TL'lik revizyon) çıktı; modele özgü kilometre bilgisi ve ikinci kaynakla doğrulanmış ayrı kayıt oluşmadı. Gösterilen triger zinciri ve turbo hortumu sorunları Astra J / K ve Insignia A kaynaklarına dayanır. |
| 2 | Meriva B | 2010-2017 | 1.4 atmosferik | – eklenmedi: Meriva 1.4 atmosferik için tekrar eden sorun çıkmadı; şikâyetler hava yastığı geri çağırması ve kapı kaplamasında. |
| 2 | Mokka / Mokka X | 2012-2020 | 1.6 CDTI | ◐ 2 ortak aile sorunu — Mokka 1.6 CDTI zincir sesi ve otomatik şanzıman (P0741) şikâyetleri yalnızca Şikâyetvar'da; Mokka'ya özgü ikinci bağımsız site bulunamadı. Gösterilen triger zinciri ve turbo hortumu sorunları aynı motoru kullanan Astra J / K ve Insignia kaynaklarına dayanır. |
| 2 | Mokka / Mokka X | 2012-2016 | 1.6 115 (A16XER) | ◐ 1 ortak aile sorunu — Mokka 1.6 benzinliye özgü kaynak aranmadı; gösterilen termostat gövdesi, soğutma suyu eksilmesi ve yağ soğutucu sorunu aynı A16XER motorunu kullanan Astra J kaydına dayanır. |
| 2 | Mokka B | 2021- | 1.2 PureTech 100/130 (EB2) | ✓ 1 sorun (+1 ortak aile) |
| 2 | Vivaro | 2014- | 1.6 CDTI (Biturbo) | – eklenmedi: Vivaro 1.6 CDTI biturbo'ya özgü kaynak çıkmadı; sonuçlar Insignia 1.6 CDTI'ya (turbo hortumu, enjektör şakırtısı, DPF) ait. |
| 2 | Zafira Tourer | 2012-2019 | 2.0 CDTI | – eklenmedi: Faz 9'da arandı: Şikâyetvar'daki Zafira şikâyetleri elektronik ve uyarı lambaları üzerine; Zafira 2.0 CDTI için tek bir inceleme (sert vites düşürme) var; 1.6 CDTI ve 1.4 Turbo için sonuç çıkmadı. Motora özgü tekrar eden sorun çıkmadı. |
| 2 | Zafira Tourer | 2012-2019 | 1.6 CDTI 120/136 | ◐ 2 ortak aile sorunu — Zafira Tourer 1.6 CDTI için modele özgü sonuç çıkmadı (şikâyetler elektronik ve uyarı lambalarında). Gösterilen triger zinciri ve turbo hortumu sorunları aynı motoru kullanan Astra J / K ve Insignia kaynaklarına dayanır. |
| 2 | Zafira Tourer | 2012-2019 | 1.4 Turbo 140 (A14NET) | ◐ 1 ortak aile sorunu — Zafira Tourer 1.4 Turbo için sonuç çıkmadı (şikâyetler elektronik ve uyarı lambalarında); gösterilen PCV diyaframı ve emme manifoldu valfi sorunu aynı A14NET motorunu kullanan Astra J kaydına dayanır. |
| 3 | Adam / Karl | 2013-2019 | 1.2 / 1.4 | ○ sırada |
| 3 | Antara | 2007-2015 | 2.2 CDTI | ○ sırada |
| 3 | Astra J | 2010-2015 | 1.7 / 2.0 CDTI | – eklenmedi: 1.7 ve 2.0 CDTI'ya özgü tekrar eden sorun çıkmadı; sonuçlar 1.6 ve 1.3 CDTI'ya ait. |
| 3 | Astra L | 2022- | 1.2 Turbo / 1.5 Dizel | ○ sırada |
| 3 | Corsa D | 2006-2014 | 1.2 / 1.3 CDTI (Easytronic) | ✓ 1 sorun (+5 ortak aile) |
| 3 | Crossland | 2017- | 1.5 BlueHDi | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — Crossland şikâyetleri motor beyni ve şanzıman tarafında tekil; gösterilen eksantrik zinciri sorunu aynı DV5 motorunu kullanan Peugeot, Citroën, Opel Grandland ve Ford kaynaklarına, AdBlue sorunu Peugeot kaynaklarına dayanır. |
| 3 | Frontera Electric | 2025- | Elektrik | – eklenmedi: Şikâyetvar'da 112 şikâyet listeleniyor (batarya arızası, uzun servis bekleme, kalkışta geri kayma, fren diski korozyonu); tek taramada ikinci bağımsız site çıkmadı. |
| 3 | Grandland X / Grandland | 2017- | 1.5 BlueHDi | ✓ 1 sorun (+2 ortak aile), 1 yıl kırılımı |
| 3 | Insignia A | 2008-2017 | 2.0 CDTI (A20DTH) | – eklenmedi: A20DTH'ye özgü kronik sorun listesi çıkmadı; turbo hortumu şikâyetleri çoğunlukla 1.6 CDTI'a ait ve o kayıtta. |
| 3 | Insignia A | 2008-2017 | 1.4 Turbo 140 (A14NET) | ◐ 1 ortak aile sorunu — Insignia 1.4 Turbo'ya özgü kaynak çıkmadı; gösterilen PCV diyaframı ve emme manifoldu valfi sorunu aynı A14NET motorunu kullanan Astra J kaydına dayanır. |
| 3 | Meriva B | 2010-2017 | 1.3 CDTI 95 (Multijet) | ◐ 5 ortak aile sorunu — Meriva 1.3 CDTI için forum yorumları eski ve genel (çoğunlukla olumlu); modele özgü sorun çıkmadı. Gösterilen enjektör, turbo, EGR ve zincir sorunları aynı Multijet motorunu kullanan Fiat ve Opel kaynaklarına dayanır. |
| 3 | Meriva B | 2010-2017 | 1.4 Turbo 120 (A14NET) | ◐ 1 ortak aile sorunu — Meriva 1.4 Turbo için sonuç çıkmadı (şikâyetler hava yastığı geri çağırması ve kapı kaplamasında); gösterilen PCV diyaframı ve emme manifoldu valfi sorunu aynı A14NET motorunu kullanan Astra J kaydına dayanır. |
| 3 | Mokka B | 2021- | 1.5 BlueHDi 110 (DV5) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — Faz 9'da arandı (tek sorgu, PureTech ile birlikte): Mokka B 1.5 BlueHDi'ya özgü kaynak çıkmadı; forumlarda AdBlue ve DPF sorunları PSA 1.5 BlueHDi'nın geneli için anılıyor. Gösterilen eksantrik zinciri sorunu aynı DV5 motorunu kullanan Peugeot, Citroën, Opel Grandland ve Ford kaynaklarına, AdBlue sorunu Peugeot kaynaklarına dayanır. |
| 3 | Zafira B | 2005-2014 | 1.6 / 1.9 CDTI | ○ sırada |

### Citroen

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C-Elysee | 2012-2020 | 1.6 HDi / BlueHDi (DV6) | ✓ 3 sorun (+1 ortak aile) |
| 1 | C3 | 2016-2022 | 1.2 PureTech 82/110 | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 1 | C3 / C4 / C5 Aircross | 2019- | 1.5 BlueHDi 100/130 (DV5) | ✓ 1 sorun (+2 ortak aile), 1 yıl kırılımı |
| 2 | Berlingo K9 | 2018- | 1.5 BlueHDi 100/130 (DV5) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — Berlingo 1.5 BlueHDi için Şikâyetvar'da eksantrik zinciri kayıtları var (Faz 4-9); gösterilen eksantrik zinciri sorunu aynı DV5 motorunu kullanan Peugeot, Citroën, Opel Grandland ve Ford kaynaklarına, AdBlue sorunu Peugeot kaynaklarına dayanır. |
| 2 | C-Elysee | 2017-2020 | 1.2 PureTech 82 | ✓ 1 sorun (+1 ortak aile) |
| 2 | C-Elysee | 2012-2016 | 1.6 VTi 115 (EP6) | – eklenmedi: Faz 9'da arandı (tek sorgu): şikâyet ya da forum kaydı çıkmadı; sonuçlar teknik özellik ve katalog sayfalarından oluştu. C-Elysée 1.6 HDi ve 1.2 PureTech 82 ayrı kayıtlarda. |
| 2 | C3 | 2009-2016 | 1.4 HDi | – eklenmedi: Enjektör ve turbo anıları tekil ve eski forum yazıları; uzun dönem bir kullanıcı turbo arızasını 230.000 km'de, enjektör revizyonunu 310.000 km'de bildiriyor; kronik sorun için yeterli kanıt yok. |
| 2 | C3 | 2009-2016 | 1.6 HDi 92 (DV6) | ◐ 3 ortak aile sorunu — Enjektör ve turbo anıları tekil ve eski forum yazıları; uzun dönem bir kullanıcı turbo arızasını 230.000 km'de, enjektör revizyonunu 310.000 km'de bildiriyor; kronik sorun için yeterli kanıt yok. Gösterilen enjektör, turbo yağ süzgeci ve EGR / DPF sorunları aynı DV6 motorunu kullanan Peugeot 301, Citroën C-Elysée, Ford Focus ve Fiesta kaynaklarına dayanır. |
| 2 | C3 | 2009- | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da 2023 model C3'te ana ekranın donması ve havalandırma peteklerinde nikelaj kaplamanın soyulması tek şikâyet; DonanımHaber ve Ekşi Sözlük'te modele özgü ikinci site çıkmadı (1.2 PureTech triger kayışı motor konusu). |
| 2 | C4 | 2020- | 1.2 PureTech 130 (EB2) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — C4'e (2020-) özgü kaynak aranmadı; gösterilen yağ banyolu triger kayışı ve yağ tüketimi sorunları aynı PureTech motorunu kullanan C3, 208 ve 308 kaynaklarına dayanır. |
| 2 | C4 Cactus | 2014-2020 | 1.2 PureTech 82/110 | ✓ 1 sorun (+1 ortak aile) |
| 2 | Jumper | 2006- | 2.2 HDi / 2.0 BlueHDi | – eklenmedi: Şikâyetvar'da Boxer / Jumper için tekrar eden konular enjektör şakırtısı (enjektör değişiminden sonra da süren), debriyaj alt merkezi / hidrolik boru sızıntısı ve pedalın takılı kalması (bazı kullanıcılarda ilk 25.000 km'de), tek vaka turbo arızası ve AdBlue uyarıları; şikâyetlerin çoğu 2023 sonrası 2.2 BlueHDi 140 / 180 araçlara ait. Anlatılar tek siteye (Şikâyetvar) dayanıyor ve kilometre bilgisi kullanıcı beyanı; ikinci bağımsız kaynak çıkmadı. |
| 2 | Jumpy | 2007- | 2.0 HDi / BlueHDi | – eklenmedi: Bu oturumdaki aramada 2.0 HDi / BlueHDi için kronik enjektör ya da DPF kaynağı çıkmadı; Şikâyetvar'da Expert 2.0 BlueHDi için geç marş ve şanzıman sesi, Jumpy için 2022 model bir araçta garanti kapsamında motor değişimi gibi tekil şikâyetler var; DonanımHaber'deki bir başlıkta eski 2.0 HDi'ların ilk sürümlerinin önerilmediği yazılıyor (yaklaşık 15 yıllık yorum). |
| 2 | ë-C4 / ë-C4 X | 2021- | Elektrik (50 kWh; 2024 sonrası 54 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Berlingo | 2008-2018 | 1.6 HDi 75/92/100/115 (DV6) | ◐ 3 ortak aile sorunu — Turbo yağ besleme borusu tıkanıklığı tek bir forum yanıtına dayanıyor; Şikâyetvar'daki Berlingo kayıtları ağırlıkla 1.5 BlueHDi zinciri. Gösterilen enjektör, turbo yağ süzgeci ve EGR / DPF sorunları aynı DV6 motorunu kullanan Peugeot 301, Citroën C-Elysée, Ford Focus ve Fiesta kaynaklarına dayanır. |
| 3 | C4 / C4 Picasso | 2010-2018 | 1.6 e-HDi 115 (MCP robotize şanzıman) | ◐ 4 ortak aile sorunu — MCP şanzıman için forum görüşleri karışık ('anlatıldığı kadar kötü değil'), kilometre ve maliyet verisi yok; aynı şanzıman Peugeot 508 kaydında ele alındı. Motor sorunları (enjektör, EGR / DPF) DV6 ailesinden gösterilir. |
| 3 | C5 | 2008-2017 | 1.6 e-HDi / 2.0 HDi | ○ sırada |
| 3 | DS3 / DS4 | 2010-2018 | 1.6 THP / 1.6 e-HDi | ○ sırada |
| 3 | Nemo / Peugeot Bipper | 2008-2018 | 1.3 HDi | ○ sırada |
| 3 | ë-C3 | 2025- | Elektrik | – eklenmedi: Şikâyetvar'da sıfır km araçlarda çekiş sistemi uyarısı, şarj soketinin kilitlenmesi ve şarj sırasında bataryadan ses gelmesi tekil; tek taramada ikinci bağımsız site çıkmadı. |

### BYD

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Atto 3 | 2023- | Elektrik (60,4 kWh) | ✓ 1 sorun |
| 2 | Dolphin / Seal / Seal U / Sealion 7 | 2024- | Elektrik | – eklenmedi: Şikâyetvar'da şarj kapağının açılmaması, ani şarj düşüşü, uygulama ve dijital anahtar sorunları tekil; ikinci site yok. Faz 6'da Seal U (elektrikli), Sealion 7 ve Atto 2 de arandı: şarj yüzde 25'teyken uyarısız durma, güç kaybı uyarısı, gerçek menzil ve batarya soğutma radyatörü garanti reddi tekil; Atto 2 için kayıt çıkmadı. 12V akü sorunu Atto 3 kaydında. |

### Skoda

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Fabia (5J / NJ) | 2010-2021 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da kapıdan su alma (2006 model Classic), 2023 modelde multimedya hataları, ön podya rulmanı ve direksiyon simidi aşınması / boya kabarması garanti reddi şikâyetleri tekil; DonanımHaber'de bir yorum kapıdan su almanın Fabia ve Polo'nun ortak sorunu olduğunu söylüyor (eski, kaynaksız). Fabia 5J / NJ'ye özgü iki bağımsız site çıkmadı (sonuçlar 1.0 DSG, start-stop ve eski 1.4 TDI konularına ait). |
| 1 | Kodiaq | 2017- | Tüm motorlar (model geneli) | ✓ 1 sorun — Bagajdan su alma Şikâyetvar ve Briskoda'da doğrulandı. Şikâyetvar'da Kodiaq'ta far mercek camlarında renk solması, şoför kapısı kilidi uyumsuzluğu, multimedyanın kendiliğinden açılıp kapanması ve CarPlay kopması tek sitede; Briskoda'daki panoramik cam tavan sızıntısı başlığı için Şikâyetvar karşılığı çıkmadı. |
| 1 | Octavia A5 | 2008-2013 | 1.2 TSI 105 (EA111) | ✓ 2 sorun |
| 1 | Octavia A5 / A7 | 2010-2020 | 1.6 TDI 105/110 (DSG DQ200) | ✓ 1 sorun (+3 ortak aile), 1 yıl kırılımı |
| 1 | Octavia A7 | 2013-2020 | 1.4 TSI (EA211, DSG DQ200) | ✓ 3 sorun, 1 yıl kırılımı |
| 1 | Octavia A7 | 2013-2020 | Tüm motorlar (model geneli) | ✓ 1 sorun — Cam tavan su sızması Şikâyetvar ve Briskoda'da doğrulandı. Şikâyetvar'da ayrıca multimedyanın kendiliğinden ses değiştirmesi / kapanması (Hybrid), far ayar düğmesinin olmaması ve ön konsol krom çıtasında kabarma tek sitede kaldı; bagaj kaması sesi ve yakıt kapağı kilit motoru yalnızca bir forum başlığında geçiyor. |
| 1 | Rapid | 2012-2019 | 1.2 TSI 90/105 | ✓ 1 sorun (+1 ortak aile) |
| 1 | Rapid | 2012-2019 | 1.6 TDI 90/105 | ✓ 1 sorun (+3 ortak aile) |
| 1 | Rapid | 2012-2019 | 1.6 MPI 105 | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da DSG vites geçişi şikâyeti (garanti dışı 30.000 TL teklif) ve DonanımHaber'de 2014 model dizel Rapid'de vites boşa düşmesi var, ikisi de otomatik şanzımanlı araçlara ait; yağ eksiltme şikâyetinde model ve motor belirtilmiyor; Ekşi Sözlük'te manuel 1.6 105 bg için olumlu bir yorum çıktı. Manuel 1.6 MPI'ya özgü sorun çıkmadı. DSG sorunları Rapid 1.2 TSI ve 1.6 TDI kayıtlarında. |
| 1 | Superb III | 2015-2023 | Tüm motorlar (model geneli) | ✓ 1 sorun — Cam tavan çatlağı ve su sızması Şikâyetvar ve Briskoda'da geçiyor (nedeni ayırt edilemiyor). Şikâyetvar'da multimedya Android Auto kopması (2024), kapı camı fitili çıkması, arka camda rüzgar sesi, iç ambiyans ışığının erken sönmesi, yolcu koltuğu gürültüsü ve anahtar pilinin sık bitmesi tek sitede kaldı. |
| 2 | Fabia | 2014-2021 | 1.0 MPI / 1.4 TDI | – eklenmedi: Fabia için motor bazında tekrar eden sorun çıkmadı (1.4 TDI kavrama / volan ve 1.0 direksiyon uyarısı gibi tekil iddialar). |
| 2 | Fabia 5J | 2010-2014 | 1.2 TSI 86/105 / 1.6 TDI 90/105 | ◐ 4 ortak aile sorunu, 2 yıl kırılımı — Fabia'ya özgü tekrar eden motor sorunu çıkmadı (1.2 krank keçesi gibi tekil iddialar); gösterilen sorunlar aynı motorları kullanan Polo, Golf ve Octavia kaynaklarına dayanır. |
| 2 | Fabia NJ | 2015-2021 | 1.2 TSI 90/110 (EA211) | ◐ 1 ortak aile sorunu — Fabia'ya özgü tekrar eden motor sorunu çıkmadı; gösterilen yağ tüketimi anlatısı aynı motoru kullanan Golf 7 kaynaklarına dayanır. |
| 2 | Kamiq / Scala | 2019- | 1.0 TSI 95/115 | ✓ 1 sorun (+1 ortak aile) |
| 2 | Karoq | 2017- | 1.5 TSI 150 (ACT) | ✓ 2 sorun |
| 2 | Karoq | 2017- | 2.0 TDI | – eklenmedi: Şikâyetler Şikâyetvar'daki tekil kayıtlarla sınırlı (DSG acil işletim / mekatronik, yağ eksiltme); bağımsız ikinci kaynak yok. Aynı motor ailesi Tiguan 1.5 TSI ve DQ381 kayıtlarında ele alındı. Karoq 1.5 TSI ayrı satırda kayıtlandı (Faz 8). |
| 2 | Karoq | 2017- | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da Karoq'ta farın içine su alması (8.000 km'de, garanti kapsamında) ve yağ tüketimi tek şikâyet; Briskoda'da yeni Karoq'ta far içi yoğuşma başlığı var ama sahipler hafif buğulanmanın normal olabileceğini, damla birikiminin sızıntıya işaret edebileceğini yazıyor; kronik sayılacak ikinci kaynak yok. |
| 2 | Kodiaq | 2017- | 1.5 TSI / 2.0 TDI | ◐ 3 ortak aile sorunu — Kodiaq'a özgü tekrar eden motor sorunu çıkmadı: Şikâyetvar'da su alma, AKF valf hortumu çatlağı, start-stop uyarısı, mekatronik / şanzıman acil işletim ve yazılım şikâyetleri var ve çoğunda motor tipi belirtilmemiş. Gösterilen sorunlar 1.5 TSI için Karoq, Passat ve Tiguan; 2.0 TDI DSG için Tiguan kaynaklarına dayanır. |
| 2 | Octavia A5 FL | 2009-2013 | 1.4 TSI 122 / 1.8 TSI 160 | ◐ 4 ortak aile sorunu, 3 yıl kırılımı — Octavia A5 FL'ye özgü kaynak aranmadı; gösterilen sorunlar aynı motorları kullanan Golf 6, Polo, Tiguan (EA111) ile A4, Q5 (EA888) kaynaklarına dayanır. |
| 2 | Octavia A7 | 2013-2020 | 1.6 MPI / 2.0 TDI | – eklenmedi: Faz 9'da arandı: Şikâyetvar'da DSG 'aracı P konumunda terk edin' uyarısı, mekatronik değişimi ve mikro şalter anlatılıyor; DonanımHaber'de 1.6 TDI için şakırdama, Ekşi Sözlük'te VAG DSG ve TDI geneli için kronik listesi var. 1.6 MPI ve 2.0 TDI için motor bazında liste çıkmadı. |
| 2 | Octavia A7 | 2013-2020 | 1.2 TSI 86/105 (manuel ve DSG) | ◐ 3 ortak aile sorunu — 1.2 TSI için motor bazında liste çıkmadı; gösterilen sorunlar aynı motor ve DQ200 DSG için Golf 7 ve Octavia 1.4 TSI kaynaklarına dayanır. |
| 2 | Octavia A7 / A8 | 2018- | 1.0 TSI / 1.5 TSI | ✓ 2 sorun (+2 ortak aile) |
| 2 | Rapid | 2012-2019 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da garanti bitiminden kısa süre sonra kaput ve kapılarda boya verniği atması, klima servomotoru ve park sensörü mikro şalteri (servisin kronik olduğunu kabul ettiği ama ücret aldığı bir şikâyet) tekil; DonanımHaber'de Rapid için yalnızca DSG başlıkları var (motor/şanzıman konusu ayrı kayıtta). |
| 2 | Superb III | 2015-2023 | 1.4 TSI / 1.5 TSI / 1.6 TDI | ◐ 4 ortak aile sorunu — Superb III'e özgü motor kaynağı çıkmadı (1.4 TSI ve 1.6 TDI için tekil arıza lambası / start-stop şikâyetleri). 1.5 TSI ACT için Superb şikâyetleri (48V, yağ eksiltme, titreme) 2024 sonrası Superb IV'e ait; gösterilen sorunlar aynı motorları kullanan Octavia, Golf, Karoq ve Passat kayıtlarına dayanır. |
| 2 | Superb III | 2015-2023 | 2.0 TDI | – eklenmedi: 2.0 TDI için yalnızca tekil şikâyetler çıktı (arıza lambası, start-stop); tekrar eden sorun yok. |
| 2 | Superb IV | 2024- | 1.5 TSI MHEV (48V hafif hibrit, DSG) | ✓ 2 sorun (+1 ortak aile) |
| 3 | Citigo | 2012-2019 | 1.0 MPI | ○ sırada |
| 3 | Enyaq / Elroq | 2021- | Elektrik | – eklenmedi: Elroq için Şikâyetvar'da tabela okuma uyarısı, Türkiye'de kapalı uygulama ve menzil şikâyetleri var; Enyaq için doğrudan kayıt çıkmadı. İkinci bağımsız kaynak yok. |
| 3 | Kamiq / Scala | 2019- | 1.5 TSI 150 (ACT) | ◐ 2 ortak aile sorunu — Kamiq ve Scala şikâyetleri (4 ayda 4 kez şanzıman uyarısı, 12.000 km'de yağ seviyesi uyarısı, titreşim) 1.0 TSI araçlara ait görünüyor; 1.5 TSI 150 için modele özgü kaynak çıkmadı. Gösterilen sorunlar 1.5 TSI evo ailesinin Karoq, Passat ve Tiguan kayıtlarına dayanır. |
| 3 | Roomster | 2006-2015 | 1.2 TSI / 1.6 TDI | ○ sırada |
| 3 | Superb II | 2008-2015 | 2.0 TDI | – eklenmedi: Faz 9'da iki sorguyla arandı: Şikâyetvar ya da DonanımHaber kaydı çıkmadı; Araclo'nun Superb II sayfalarında 2.0 TDI için DSG mekatronik valf burcu ve yüksek basınç pompası var; deneyim türünde (şikâyet / forum) kaynak yok, Araclo tek başına yeterli sayılmıyor. |
| 3 | Superb II | 2009-2015 | 1.4 TSI 125 / 1.6 TDI 105 / 1.8 TSI 160 | ◐ 6 ortak aile sorunu, 3 yıl kırılımı — Superb II'ye özgü deneyim kaynağı çıkmadı (yalnızca Araclo sayfaları ve yabancı rehberler: 1.6 TDI'da enjektör, 1.8 TSI'da zincir ve DSG); gösterilen sorunlar aynı motorları kullanan diğer VAG kayıtlarına dayanır. |
| 3 | Yeti | 2009-2017 | 1.2 TSI / 1.4 TSI / 1.6 TDI | – eklenmedi: 1.2 TSI zincir iddiaları eski ve tekil (ayrıntısı Octavia A5 1.2 TSI kaydında); DSG görüşleri çelişkili. |

### Mercedes-Benz

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | A Serisi / CLA / GLA W176 | 2012-2019 | Tüm motorlar (model geneli) | ✓ 1 sorun — Direksiyon açı sensörü iki sitede doğrulandı. Airbag / emniyet kemeri soketi arızası (Ekşi Sözlük ve Şikâyetvar'da kronik denmiş; kemer soketi için bağımsız ikinci site çıkmadı), GLA'da multimedya piksel kaybı ve arka klima, CLA 200 turbo wastegate (motor konusu) tekil kaldı. |
| 1 | C Serisi W204 | 2007-2014 | C220 / C250 CDI 2.1 (OM651) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | C Serisi W204 | 2007-2014 | Tüm motorlar (model geneli) | ✓ 1 sorun — Direksiyon açı sensörü iki sitede doğrulandı. Sunroof tahliye tıkanması ve kabine su sızması, iç kapı açma kolu telinin kopması, kapı kilit pompası, ön park lambalarının ısıdan patlaması ve far yuvası erimesi, kırmızıda vernik atması Türkçe kaynaklarda anılıyor ama modele özgü ikinci site çıkmadı. |
| 1 | C Serisi W205 | 2014-2021 | C180 / C200 benzinli (M274) | – eklenmedi: Kaynaklar M274'ü zincir konusunda M271'e göre daha sorunsuz buluyor; belirgin kronik sorun yok (7G-Tronic için dağınık şikâyetler var). |
| 1 | C Serisi W205 | 2014-2021 | C180d / C200d 1.6 (R9M kaynaklı dizel) | ✓ 1 sorun |
| 1 | C Serisi W205 | 2014-2021 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar ve DonanımHaber'de sunroof arızası, direksiyon kutusu sesi, klima klape motoru (göğüs sökümü gerekiyor), havalandırma çıkışlarından çıtırtı ve COMAND ekran konuları geçiyor; hepsi tek başlıkta ya da tek kullanıcıda, ortak bir sorun oluşmadı. Far ve kapı için kaynak çıkmadı. |
| 1 | E Serisi W212 | 2009-2016 | E200 / E250 CGI 1.8 turbo (M271 EVO) | ✓ 1 sorun |
| 1 | E Serisi W212 | 2009-2016 | E250 CDI 2.1 (OM651) | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 1 | E Serisi W212 | 2009-2016 | Tüm motorlar (model geneli) | ✓ 1 sorun — Arka travers korozyonu Şikâyetvar ve yabancı forumlarda (MBWorld, MBClub, BenzWorld) doğrulandı; Türkiye'deki kapsam doğrulanamadı. Şikâyetvar'da direksiyon simidi aşınması (hepsinde aynı diyen yorum), tavan döşemesi sarkması (2014 model), navigasyonun hafıza kartını okumaması ve vitesin kendiliğinden P'ye geçmesi tek sitede kaldı. |
| 1 | EQA / EQB | 2021- | Elektrik (70,5 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | A Serisi W176 | 2012-2018 | A180 CDI (dizel) | ✓ 1 sorun (+2 ortak aile) |
| 2 | A Serisi W176 | 2012-2018 | A180 1.6 benzinli (M270, 7G-DCT) | – eklenmedi: Enjektör ve 7G-DCT iddiaları için güçlü kanıt bulunamadı; tekrarlayan şikâyet Pre-Safe / açı sensörü (CLA ile birlikte ele alındı). |
| 2 | A Serisi W176 | 2012-2018 | A200 CDI / A220 CDI 2.1 (OM651) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — Enjektör ve 7G-DCT iddiaları için güçlü kanıt bulunamadı; tekrarlayan şikâyet Pre-Safe / açı sensörü (CLA ile birlikte ele alındı). Gösterilen piezo enjektör sorunu C Serisi W204 ve E Serisi W212 (OM651) kayıtlarına dayanır. |
| 2 | A Serisi W177 | 2018- | A180 d 1.5 (OM608, K9K) | ◐ 2 ortak aile sorunu — Faz 9'da arandı: W177'ye özgü kaynak çok az; 7G-DCT vuruntu ve geri vites uyarısı ile PRE-SAFE / ESP uyarıları çoğunlukla W176 dönemine ait (A Serisi / CLA W176 kaydı), MBUX ekranına özgü kronik sorun bulunamadı. Gösterilen enjektör ve EGR sorunları 1.5 dizelin Renault K9K ile ortak olması nedeniyle Renault ve Dacia kaynaklarına dayanır. |
| 2 | A Serisi W177 | 2018- | A180 1.3 / A200 | – eklenmedi: 1.3 benzinli (M282) ve A200 için kaynak çıkmadı. |
| 2 | B Serisi W246 | 2011-2018 | B180 CDI 1.5 (OM607, 7G-DCT) | ◐ 2 ortak aile sorunu — B Serisi'ne özgü Türkçe şikâyet ya da forum kaydı çıkmadı; gösterilen enjektör ve EGR sorunları 1.5 dizelin Renault K9K ile ortak olması nedeniyle Renault ve Dacia kaynaklarına dayanır. 7G-DCT bu kayıtta yer almıyor. |
| 2 | C Serisi W203 / W204 | 2002-2010 | C180 / C200 Kompressor 1.8 (M271) | ✓ 2 sorun |
| 2 | C Serisi W204 | 2009-2014 | C180 / C200 / C250 CGI 1.8 turbo (M271 EVO) | ✓ 1 sorun |
| 2 | C Serisi W205 | 2018-2021 | C220d 2.0 (OM654) | – eklenmedi: C220d (OM654) için W205'e özgü kaynak bulunamadı; bulunan şikâyetler C200d (R9M) NOx / AdBlue / turbo yağ kaçağı üzerine ve ayrı kayıtta. |
| 2 | C Serisi W205 | 2014-2018 | C220d / C250d 2.1 (OM651) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — C220d (OM651) için W205'e özgü kaynak bulunamadı; bulunan şikâyetler C200d (R9M) NOx / AdBlue / turbo yağ kaçağı üzerine ve ayrı kayıtta. Gösterilen piezo enjektör sorunu C Serisi W204 ve E Serisi W212 (OM651) kayıtlarına dayanır. |
| 2 | Citan | 2012-2021 | 108 / 109 / 111 CDI 1.5 (OM607, K9K) | ◐ 2 ortak aile sorunu — Citan'a özgü kaynak aranmadı; gösterilen enjektör ve EGR sorunları aynı K9K motorunu kullanan Renault Kangoo, Clio ve Dacia kayıtlarına dayanır. |
| 2 | E Serisi W213 | 2016- | E180 / E200 / E220d | – eklenmedi: W213 için sistematik veri yok; Şikâyetvar'da tekil SBC fren, ekran ve direksiyon şikâyetleri var ve bir kısmı W212 / W214'e ait. |
| 2 | EQC | 2019-2023 | Elektrik (80 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | GLA | 2013-2019 | GLA 180 d 1.5 (OM607) | ◐ 2 ortak aile sorunu — GLA'ya özgü ayrı kaynak bulunamadı; DonanımHaber'deki Pre-Safe başlığı GLA'yı da anıyor. Gösterilen enjektör ve EGR sorunları 1.5 dizelin Renault K9K ile ortak olması nedeniyle Renault ve Dacia kaynaklarına dayanır. |
| 2 | GLA | 2013-2019 | GLA 200 CDI / 220 CDI 2.1 (OM651, 7G-DCT) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — GLA'ya özgü ayrı kaynak bulunamadı; DonanımHaber'deki Pre-Safe başlığı GLA'yı da anıyor. Gösterilen piezo enjektör sorunu C Serisi W204 ve E Serisi W212 (OM651) kayıtlarına dayanır. |
| 2 | GLC | 2015-2019 | GLC 220 d / 250 d 2.1 (OM651, 9G-Tronic) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — GLC 220 d için Türkçe deneyim kaynağı tek vakada kaldı (2020 model araç, OM654 olabilir); yabancı rehberler OM651'de EGR kurumu ve NOx / AdBlue arızalarını sayıyor. Gösterilen piezo enjektör sorunu C Serisi W204 ve E Serisi W212 (OM651) kayıtlarına dayanır. |
| 2 | GLE W166 (ML) | 2011-2018 | 250 d (OM651) / 350 d (OM642) | ○ sırada |
| 2 | Vito W447 (1.6) | 2014- | 109 / 111 CDI 1.6 (OM622, R9M) | ○ sırada |
| 3 | B Serisi W246 | 2011-2018 | B200 CDI / B220 CDI 2.1 (OM651) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — Faz 9'da iki sorguyla arandı: Türkçe şikâyet ya da forum kaydı çıkmadı; Carchecker ve Au7o'daki rehber ve ABD sahip raporları OM651 dizelde DPF-EGR tıkanması ve 7G-DCT'de kalkış titreşimi gösteriyor (A Serisi / W176 kaydındaki bulgularla örtüşüyor); DonanımHaber'de bir kullanıcı B200'ün 7G-DCT'sinin sorunsuz olduğunu yazıyor. Gösterilen piezo enjektör sorunu C Serisi W204 ve E Serisi W212 (OM651) kayıtlarına dayanır. |
| 3 | CLA | 2013-2019 | 180 CDI (dizel) | ✓ 1 sorun (+2 ortak aile) |
| 3 | CLA C118 | 2019- | CLA 180 (M282) / 200 d (OM654) | ○ sırada |
| 3 | CLS C218 | 2011-2017 | CLS 250 CDI (OM651) / 350 CDI (OM642) | ○ sırada |
| 3 | EQE / EQS | 2022- | Elektrik | – eklenmedi: Şikâyetvar'da EQS için şarj almama ve yolda kalma, EQE için menzil kaybı şikâyetleri tekil. NHTSA 24V372 (EQE / EQS batarya yönetimi yazılımı, sürüş gücü kaybı) ABD'deki araçlara ait ve Türkiye şikâyetleriyle aynı belirtiyi göstermiyor. DonanımHaber'de 'Mercedes EQE ve EQS Kullanıcı Deneyimleri' başlığı var ancak eşleşen bir arıza çıkmadı. |
| 3 | GLA | 2013-2019 | 1.6 / 2.0 benzinli (M270 / M274) | – eklenmedi: GLA'ya özgü ayrı kaynak bulunamadı; DonanımHaber'deki Pre-Safe başlığı GLA'yı da anıyor, kapsam A Serisi / CLA kaydında. |
| 3 | GLC / GLA benzinli | 2013- | 200 / 250 (M274 / M270) | – eklenmedi: Faz 9'da iki sorguyla arandı: Şikâyetvar'da 2020 model bir GLC 220d'nin yolda kalması ve şanzıman arızası şikâyeti var (tek vaka; 2019 sonrası araçlar OM654 motorludur); Araclo'nun GLC 200 ve GLA 200 sayfaları 9G-Tronic sarsıntısı ve GLA'da çift kavramalı şanzıman başlığını gösteriyor; yabancı rehberler OM651'de EGR kurumu ve NOx / AdBlue arızalarını sayıyor. Türkçe deneyim kaynağı tek vakada kaldı. |
| 3 | GLK | 2008-2015 | GLK 220 CDI 4MATIC 2.1 (OM651, 7G-Tronic) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — GLK'ya özgü kaynak aranmadı; gösterilen piezo enjektör ve 7G-Tronic iletken plaka sorunları C Serisi W204 ve E Serisi W212 kayıtlarına dayanır. |
| 3 | S Serisi W222 | 2013-2020 | S 350 d (OM642) / S 400 | ○ sırada |
| 3 | Sprinter | 2006-2018 | 209-316 CDI (OM651) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — Sprinter'a özgü ayrı kaynak yok; gösterilen piezo enjektör sorunu C ve E Serisi (OM651) kayıtlarına dayanır. |
| 3 | Sprinter W907 | 2018- | 316 CDI (OM654) | ○ sırada |
| 3 | Viano W639 | 2003-2014 | 2.2 CDI (OM646) | ○ sırada |
| 3 | Vito / V-Class | 2014- | 114 / 116 / 119 CDI (OM651) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — Vito ve Sprinter'a özgü ayrı kaynak yok; gösterilen piezo enjektör ve 7G-Tronic iletken plaka sorunları C ve E Serisi (OM651) kayıtlarına dayanır. |

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
| 1 | 3 Serisi F30 | 2012-2019 | Tüm motorlar (model geneli) | ✓ 1 sorun — İç kapı kolu erimesi Şikâyetvar ve BimmerPost'ta doğrulandı. Şikâyetvar'da kapı iç keçelerinin deformasyonu ve yağışta su alma, sunroof fitili yıpranması, direksiyon kutusu sesi (DonanımHaber'de kronik denmiş), akü deşarjı ve ekran sorunları tekil kaldı; N13 turbo manifoldundan su kaçırma motor konusu. |
| 1 | 3 Serisi G20 | 2019- | 320i (B48) / 320d (B47) | – eklenmedi: Şikâyetvar'da G20 için tekil kayıtlar var (45.000 km'de su pompası uyarısı, 60 bin km'de park freni arızası, 74.000 km'de diferansiyel uğultusu, 139.000 km'de soğutma sistemi uyarısı); Ekşi Sözlük'te N20 / B47 / B48'in daha az sorunlu sayıldığı, DonanımHaber'de bir G20 sahibinin B48'de kronik sorun yaşamadığı yazılıyor. Motora özgü tekrar eden sorun için iki bağımsız site çıkmadı. |
| 1 | 5 Serisi G30 | 2017-2023 | 520i (B48) / 520d (B47) | – eklenmedi: Şikâyetvar'da G30 520i için tekrar eden konular ambiyans aydınlatma kesilmesi, kapı kolu içlerinin erimesi, sunroof perdesi, acil çağrı pili ve multimedya; motor ya da şanzıman için sistematik kayıt yok ve konular tek siteye (Şikâyetvar) ait. DonanımHaber'deki eski bir yazı egzoz ve şanzıman sorunlarını sayıyor ama zayıf bir kaynak. |
| 1 | X1 E84 | 2009-2015 | sDrive18d / xDrive18d / xDrive20d (N47) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — Modele özgü şikâyet çıkmadı; Şikâyetvar'daki X1 şikâyetleri şanzıman, direksiyon, fren ve kapı gıcırtısında toplanıyor. Gösterilen N47 zincir sorunu 1, 3 ve 5 Serisi kaynaklarına dayanır; bir yabancı rehber (Carpedia) zincir sorununun Mart 2011 sonrası üretimde belirgin azaldığını yazıyor. |
| 1 | X1 F48 | 2015-2022 | sDrive18i 1.5 turbo (B38) | ◐ 1 ortak aile sorunu — Faz 9'da (tek sorgu) X1 F48 için Türkçe şikâyet ya da forum kaydı çıkmadı; bir Türkçe alım rehberi F48 18i'nin 1.5 üç silindirli turbo olduğunu yazıyor. Gösterilen turbo manifoldu çatlaması aynı B38 motorunu kullanan 1 Serisi (F20 LCI) kaydına dayanır. |
| 1 | X3 F25 | 2010-2014 | sDrive18d / xDrive20d (N47) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı |
| 1 | X3 F25 LCI | 2014-2017 | sDrive18d / xDrive20d (B47) | ◐ 1 ortak aile sorunu — B47 motoruna özgü kronik sorun aranmadı; yalnızca xDrive transfer kutusu ailesi gösteriliyor. |
| 1 | X3 G01 | 2017- | xDrive20d (B47) / xDrive20i (B48) / xDrive30i | – eklenmedi: G01 için kronik arıza bulan kaynak çıkmadı: Şikâyetvar'da 2018 model acil çağrı pili ve 2020 model geri görüş kamerası gibi tekil kayıtlar var; xDrive servo motor (VTG) anlatısı 2006 model X3'e ait. |
| 1 | X5 E70 | 2007-2013 | xDrive30d / xDrive40d (M57 / N57) | ◐ 1 ortak aile sorunu — N57 motoruna özgü sorun için Türkçe kanıt çıkmadı: Şikâyetvar'da X5 için tekil turbo / interkol hortumu vakaları, forumlarda N57S'nin genelde sorunsuz olduğu yorumları var; yabancı rehberlerde zincir iddiası çelişkili (bazıları sorunu asıl N47'ye bağlıyor). Gösterilen sorun xDrive transfer kutusuna aittir. |
| 1 | X5 F15 | 2013-2018 | xDrive25d / 30d / 40d (N57) | ◐ 1 ortak aile sorunu — N57 motoruna özgü sorun için Türkçe kanıt çıkmadı: Şikâyetvar'da X5 için tekil turbo / interkol hortumu vakaları, forumlarda N57S'nin genelde sorunsuz olduğu yorumları var; yabancı rehberlerde zincir iddiası çelişkili (bazıları sorunu asıl N47'ye bağlıyor). Gösterilen sorun xDrive transfer kutusuna aittir. |
| 2 | 1 Serisi F20 | 2011-2015 | 116d 1.6 (N47D16) | ✓ 1 sorun (+1 ortak aile) |
| 2 | 1 Serisi F20 | 2011-2019 | 118d 2.0 (N47D20 / B47) | – eklenmedi: 118d / B47 için F20'ye özgü ayrı kaynak bulunamadı; N47D20 zincir sorunu 320d ve 520d kayıtlarında ele alındı. |
| 2 | 2 Serisi F22 / F45 | 2014-2021 | 216d / 218d (B37 / B47) | – eklenmedi: Bu oturumdaki aramada 216d (B37) için çoğunlukla olumlu yorumlar çıktı; F22 ve 216d'ye özgü veri yok. F45 için akü boşalması, elektronik el freni ve şanzıman gibi genel şikâyetler DonanımHaber'de dağınık geçiyor; ortak bir arıza oluşmadı. |
| 2 | 2 Serisi F22 / F45 | 2014-2021 | 218i 1.5 turbo (B38) | ◐ 1 ortak aile sorunu — Bu oturumdaki 2 Serisi aramasında B38 turbo manifoldu çatlaması anlatıları Şikâyetvar, Ekşi Sözlük ve DonanımHaber'de yinelendi (aile sorununda kayıtlı); 218i'ye özgü kilometre bilgili ayrı kayıt oluşmadı. Gösterilen turbo manifoldu çatlaması aynı B38 motorunu kullanan 1 Serisi (F20 LCI) kaydına dayanır. |
| 2 | 2 Serisi F44 Gran Coupé | 2020- | 216d / 218i / 220i | ○ sırada |
| 2 | 3 Serisi F30 | 2012-2015 | 316i 1.6 turbo (N13) | ◐ 7 ortak aile sorunu — 316i'ye özgü kaynak aranmadı; gösterilen sorunlar aynı N13 motorunu kullanan 116i / 118i (F20) kaydının kaynaklarına dayanır. |
| 2 | 4 Serisi F32 / F36 | 2016-2020 | 420i (B48) / 420d (B47) | – eklenmedi: Bu oturumdaki aramada 4 Serisi 420d / 420i için triger zinciri ya da motora özgü kayıt çıkmadı; çıkanlar ön cam contası, iç kapı kolu ve soğutma sıvısı gibi tekil ya da model geneli konular. B47 / B48 için ayrı kaynak bulunamadı. |
| 2 | 4 Serisi F32 / F36 | 2013-2016 | 420i 2.0 turbo benzin (N20) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — 420i'ye özgü kaynak çıkmadı (bu oturumdaki aramada zincir anlatısı yok); gösterilen triger zinciri, devirdaim pompası ve yağ filtresi yuvası sorunları aynı N20 motorunu kullanan 320i / 328i (F30) kaydının kaynaklarına dayanır. |
| 2 | 4 Serisi F32 / F36 | 2013-2015 | 420d 2.0 dizel (N47) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — 420d'ye özgü kaynak çıkmadı (bu oturumdaki aramada zincir anlatısı yok); gösterilen triger zinciri ve EGR soğutucusu sorunları aynı N47 motorunu kullanan 320d (F30) ve 520d (F10) kayıtlarının kaynaklarına dayanır. |
| 2 | 5 Serisi F10 | 2010-2015 | 520d 2.0 (N47D20) | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 2 | 5 Serisi F10 | 2011-2016 | 520i / 528i (N20) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı |
| 2 | 5 Serisi F10 | 2015-2017 | 520d (B47) | – eklenmedi: Bu oturumdaki aramada B47'ye özgü kayıt çıkmadı: sonuçlar N47 zincir tartışmalarına ve ZF 8 ileri şanzımanı sorunsuz bulan yorumlara ait; bir yorum B47'yi düzeltilmiş N47 olarak anıyor (tekil görüş). |
| 2 | 5 Serisi F10 | 2010-2016 | Tüm motorlar (model geneli) | ✓ 1 sorun — İç kapı kolu erimesi Şikâyetvar ve BimmerPost'ta doğrulandı. |
| 2 | X1 E84 | 2011-2015 | sDrive20i / xDrive28i (N20) | ◐ 4 ortak aile sorunu, 1 yıl kırılımı |
| 2 | X3 F25 | 2012-2017 | xDrive28i (N20) | ◐ 4 ortak aile sorunu, 1 yıl kırılımı |
| 2 | X3 F25 | 2011-2017 | xDrive30d (N57) | ◐ 1 ortak aile sorunu — N57 motoruna özgü sorun için Türkçe kanıt çıkmadı: Şikâyetvar'da X5 için tekil turbo / interkol hortumu vakaları, forumlarda N57S'nin genelde sorunsuz olduğu yorumları var; yabancı rehberlerde zincir iddiası çelişkili (bazıları sorunu asıl N47'ye bağlıyor). Gösterilen sorun xDrive transfer kutusuna aittir. |
| 2 | X5 G05 | 2018- | xDrive30d / xDrive40d (B57) | – eklenmedi: Bu oturumdaki aramada G05'e özgü kayıt çıkmadı: sonuçlar SOS (acil çağrı) sistemi gibi tekil konular, motor kodu belirtilmemiş bir 2018 model X5'te yaklaşık 141.000 km'de motor değişimi anlatısı (G05 mi F15 mi belli değil) ve eski kuşak listelerinden oluşuyor. |
| 2 | iX / iX1 / iX3 / i4 | 2021- | Elektrik | – eklenmedi: Şikâyetvar'da hızlı şarjta düşük güç, şarj kapağı kilidi ve şarj soketi arızaları tekil; DonanımHaber'de yalnızca i4 menzil göstergesi tartışması var, ortak bir örüntü doğrulanamadı. NHTSA kayıtlarında iX / i4 için batarya (22V-541), birleşik şarj ünitesi (23V-449) ve 2024 i4 modül kaynak dikişi (24V-135) geri çağırmaları var; Türkiye kapsamı doğrulanamadı. |
| 3 | 1 Serisi F40 / X1 F48 | 2015- | 116d / 118i / sDrive16d / sDrive18d | – eklenmedi: Faz 9'da arandı (tek sorgu): Türkçe şikâyet ya da forum kaydı çıkmadı; bir Türkçe alım rehberi zincir / Valvetronic sorunlarının E84'ün 2.0 motoruna ait olduğunu, F48 18i'nin 1.5 üç silindirli turbo olduğunu yazıyor; AUTO BILD TÜV testi geri çağırmaları sıralıyor (EGR sızıntısı, airbag ateşleme, DKG bağlantıları). |
| 3 | 3 Serisi E90 / 5 Serisi E60 | 2005-2013 | 316i / 318i / 320i (N46 / N52), 520i | – eklenmedi: N46 / N52'ye özgü ayrıntılı kaynak çıkmadı; soğutma sistemi ve yağ kaçağı anlatıları tekil. N47 zincir sorunu ayrı kayıtlarda. |
| 3 | 3 Serisi F30 LCI | 2015-2019 | 318i 1.5 turbo (B38) | ◐ 1 ortak aile sorunu — 318i'ye özgü kaynak aranmadı; gösterilen turbo manifoldu çatlaması aynı B38 motorunu kullanan 1 Serisi (F20 LCI) kaydına dayanır. |
| 3 | 4 Serisi F32 / F36 | 2016-2020 | 418i 1.5 turbo (B38) | ◐ 1 ortak aile sorunu — 418i'ye özgü sorun kaydı oluşmadı; bu oturumdaki aramada bir 418i'de turbo manifoldu anlatısı geçti (B38 ailesindeki sorunla aynı). Gösterilen turbo manifoldu çatlaması aynı B38 motorunu kullanan 1 Serisi (F20 LCI) kaydına dayanır. |
| 3 | 7 Serisi F01 / G11 | 2009- | 730d / 740d (N57 / B57) | ○ sırada |
| 3 | X2 F39 | 2018-2023 | sDrive18d / xDrive20d (B47) | ○ sırada |
| 3 | X2 F39 | 2018-2023 | sDrive18i 1.5 turbo (B38) | ◐ 1 ortak aile sorunu — X2'ye özgü kaynak aranmadı; gösterilen turbo manifoldu çatlaması aynı B38 motorunu kullanan 1 Serisi (F20 LCI) kaydına dayanır. |
| 3 | X4 F26 / G02 | 2014- | xDrive20d / xDrive30d (B47 / N57) | ○ sırada |
| 3 | X6 E71 / F16 | 2008-2019 | xDrive30d / xDrive40d (N57) | ○ sırada |
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
| 1 | Juke | 2014-2019 | 1.2 DIG-T 115 (HRA2DDT) | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 1 | Juke | 2010-2019 | Tüm motorlar (model geneli) | ✓ 1 sorun, 1 yıl kırılımı — Ekran silikleşmesi Şikâyetvar ve DonanımHaber'de geçiyor. Şikâyetvar'da yeni Juke'ta far içine su alma (metin bozuk), start-stop arızası ve şanzıman konuları ayrı ya da tekil. |
| 1 | Qashqai J11 | 2014-2020 | 1.5 dCi 110 (K9K) / 1.6 dCi 130 (R9M) | ✓ 2 sorun (+2 ortak aile), 1 yıl kırılımı |
| 1 | Qashqai J11 | 2014-2021 | 1.2 DIG-T (HRA2DDT, Xtronic) | ✓ 3 sorun, 2 yıl kırılımı |
| 2 | Juke | 2010-2019 | 1.5 dCi 110 (K9K) | ◐ 2 ortak aile sorunu — Juke 1.5 dCi için kaynak ağırlıkla tek bir rehber (Araclo); turbo yağ borusu ve DPF anlatıları ikinci bağımsız kaynakla desteklenmedi. Gösterilen enjektör ve EGR sorunları aynı K9K motorunu kullanan Renault ve Dacia kayıtlarına, K9K turbo hortumu sorunu ise Qashqai J11 kaydına dayanır. |
| 2 | Micra | 2010-2017 | 1.2 (CVT otomatik) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Micra K14 | 2017-2023 | 0.9 IG-T 90 (H4Bt) | ◐ 1 ortak aile sorunu — 0.9 IG-T motoruna özgü kronik sorun sonuçlarda yer almadı; şikâyetler 1.2 CVT'de toplanıyor. Gösterilen turbo wastegate sorunu aynı H4Bt motorunu kullanan Sandero ve Clio 4 kayıtlarına dayanır. |
| 2 | Note E12 | 2013-2017 | 1.5 dCi 90 (K9K) | ◐ 2 ortak aile sorunu — Note 1.5 dCi için ilgili şikâyet bulunamadı (aramada yalnızca X-Trail 1.6 dCi öne çıktı); gösterilen enjektör ve EGR sorunları aynı K9K motorunu kullanan Clio, Megane, Duster ve Sandero kaynaklarına dayanır. |
| 2 | Qashqai J10 | 2007-2013 | 1.6 (benzinli) | – eklenmedi: J10 dönemine (2007-2013) özgü kaynak bulunamadı; 1.6 benzinli için ayrıca sonuç çıkmadı. |
| 2 | Qashqai J10 | 2007-2013 | 1.5 dCi 106 (K9K) | ◐ 2 ortak aile sorunu — J10 dönemine (2007-2013) özgü kaynak bulunamadı; Qashqai 1.5 dCi turbo hortumu şikâyetleri 2012 model ve sonrasında yoğunlaşıyor, J11 kaydında ele alındı. Gösterilen enjektör ve EGR sorunları aynı K9K motorunu kullanan Clio, Megane, Duster ve Sandero kaynaklarına dayanır. |
| 2 | Qashqai J10 | 2007-2013 | Tüm motorlar (model geneli) | ✓ 1 sorun — Ekran silikleşmesi Şikâyetvar (2012-2013 Tekna) ve DonanımHaber (bir yorum) kaynaklı. J11 için bu aramada ön takım, panoramik cam tavan ve far çıkmadı; sağ ön kapı kilidinin kilitlenmemesi (kronik denmiş) ve kapı kartı kaplamasının soyulması (2022 model) tek şikâyet. |
| 2 | Qashqai J11 | 2014-2020 | 1.6 dCi 130 (R9M, Xtronic CVT) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Qashqai J11 FL / J12 | 2019- | 1.3 DIG-T 140/158 (2021 sonrası 12V hafif hibrit, Xtronic CVT) | ✓ 2 sorun, 1 yıl kırılımı |
| 3 | Leaf | 2019- | Elektrik | – eklenmedi: Türkiye'ye özgü kaynak çıkmadı (yalnızca bir Ekşi Sözlük yorumu: aktif batarya soğutması yok, CHAdeMO). Hava soğutmalı bataryanın kapasite kaybı InsideEVs, MyNissanLeaf ve Electrek'te belgeli, ancak bunlar ağırlıkla ABD'nin sıcak iklimine ve ilk nesil Leaf'e ait. NHTSA 24V-700 geri çağırması ABD'de Smyrna'da üretilen 2019-2020 Leaf'leri kapsıyor (CHAdeMO hızlı şarjda yangın riski); Türkiye kapsamı doğrulanamadı. |
| 3 | Murano Z51 | 2008-2014 | 3.5 V6 (CVT) | ○ sırada |
| 3 | Navara | 2010- | 2.5 dCi | – eklenmedi: Enjektör ve turbo şikâyetleri yalnızca Şikâyetvar'da; ikinci bağımsız kaynak çıkmadı. |
| 3 | Note | 2013- | 1.2 (benzinli) | – eklenmedi: Note 1.2 için ilgili şikâyet bulunamadı (aramada yalnızca X-Trail 1.6 dCi öne çıktı). |
| 3 | Pulsar C13 | 2014-2018 | 1.2 DIG-T / 1.5 dCi | ○ sırada |
| 3 | X-Trail T31 | 2007-2014 | 2.0 dCi | ○ sırada |
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
| 1 | Fiesta Mk7 | 2011-2017 | 1.6 Ti-VCT 105 (Powershift DPS6) | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 1 | Fiesta Mk7 | 2008-2017 | Tüm motorlar (model geneli) | ✓ 1 sorun — Direksiyon sesi iki sitede doğrulandı. Şikâyetvar'da teyp donması ve direksiyon kumanda tuşları, bagaja far kısmından su alma (tek vaka), 2013 tarihli bir forum başlığında kapı içi sesleri ve cam düşmesi tekil kaldı. |
| 1 | Focus 2 / 3 | 2008-2018 | 1.6 TDCi (DV6) | ✓ 3 sorun |
| 1 | Focus 3 | 2011-2018 | 1.6 Ti-VCT (Powershift DPS6) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Focus 3 | 2011-2018 | 1.5 TDCi 95/120 | – eklenmedi: Enjektör ve DPF şikâyetleri dağınık, DPF şikâyetleri ağırlıkla 2019 sonrası EcoBlue'ya ait; 2015-2018 1.5 TDCi için ortak sorun yok. Faz 7'de yeniden arandı: Türkçe kaynaklar 1.6 TDCi ve 2019 sonrası EcoBlue'ya ait; Mk3 1.5 TDCi için yalnızca Ford Owners Club'da (İngiltere) DPF, EGR ve çalışma sorunu konuları var, ikinci bağımsız Türkçe kaynak çıkmadı. |
| 1 | Focus 3 | 2011-2018 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da SYNC / multimedya ekranının donması, kontak kapandıktan sonra ekranın açık kalması ve CarPlay kopması (2016-2025 model yılları, çoğu Focus 4) tekrar ediyor; DonanımHaber ve Otopark'taki kapı kilidi başlıkları eski Focus'lara ya da çocuk kilidi / hıza bağlı otomatik kilit konusuna ait. Focus 3'e özgü ikinci site yok. |
| 1 | Focus 4 / Kuga 3 | 2019- | 1.5 EcoBlue 120 (DV5) | ✓ 2 sorun |
| 1 | Transit | 2006- | 2.2 TDCi / 2.0 EcoBlue | – eklenmedi: Şikâyetvar'da Transit için enjektör (37.500 km'de enjektör arızası, yaklaşık 50 bin TL teklif), turbo ve volan / debriyaj şikâyetleri ile 2017 model Transit 2.2 155 PS'te 150 bin km'de piston delinmesi var; DonanımHaber'de 2012 Transit 350 için volan değişimi önerisi geçiyor. Anlatılar tekil, motor hacmi ayrımı yapılmıyor; iki bağımsız siteyle doğrulanan tekrar eden bir sorun çıkmadı. |
| 2 | C-Max / Grand C-Max | 2010-2019 | 1.5 TDCi | – eklenmedi: C-Max 1.5 TDCi için sonuç çıkmadı. |
| 2 | C-Max / Grand C-Max | 2010-2019 | 1.6 TDCi 95/115 (DV6) | ◐ 3 ortak aile sorunu — Faz 9'da arandı: DonanımHaber'de 2011 model C-Max 1.6 TDCi'da enjektör arızası (tek başlık, bir enjektör için yaklaşık 1.230 TL teklif), Şikâyetvar'da 2012 model 1.6 TDCi'da enjektör pulu değişiminden sonra motor arızası (tek vaka); turbo boru / hortum ve DPF yorumları genel 1.6 TDCi'ya ait (Focus 1.6 TDCi kaydı). İkinci bağımsız doğrulama yok. Gösterilen enjektör, turbo yağ süzgeci ve EGR / DPF sorunları aynı DV6 motorunu kullanan Peugeot 301, Citroën C-Elysée, Ford Focus ve Fiesta kaynaklarına dayanır. |
| 2 | C-Max / Grand C-Max | 2010-2019 | 1.6 Ti-VCT 105 (Powershift DPS6) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — C-Max'e özgü Powershift kaynağı aranmadı; gösterilen kavrama ve TCM sorunları Focus 3, Fiesta ve Volvo V40 / S60 kaynaklarına dayanır. |
| 2 | C-Max / Grand C-Max | 2010-2019 | 1.0 EcoBoost 100/125 | ◐ 2 ortak aile sorunu, 2 yıl kırılımı — C-Max 1.0 EcoBoost'a özgü kaynak aranmadı; gösterilen sorunlar aynı EcoBoost motorunu kullanan Fiesta, Focus ve EcoSport kaynaklarına dayanır. |
| 2 | Courier / Tourneo Courier | 2014- | 1.5 TDCi | – eklenmedi: Şikâyetler fren sesi, gıcırtı ve genel motor arıza lambası gibi dağınık konularda; ortak bir arıza için iki bağımsız site bulunamadı. |
| 2 | Courier / Tourneo Courier | 2014- | 1.0 EcoBoost 100 | ◐ 2 ortak aile sorunu, 2 yıl kırılımı — Şikâyetler fren sesi, gıcırtı ve genel motor arıza lambası gibi dağınık konularda; ortak bir arıza için iki bağımsız site bulunamadı. Gösterilen sorunlar aynı EcoBoost motorunu kullanan Fiesta, Focus ve EcoSport kaynaklarına dayanır. |
| 2 | EcoSport | 2013-2017 | 1.5 Ti-VCT 112 (Powershift DPS6) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — EcoSport 1.5 Ti-VCT Powershift'e özgü kaynak aranmadı; gösterilen kavrama ve TCM sorunları Focus 3, Fiesta ve Volvo V40 / S60 kaynaklarına dayanır. |
| 2 | Fiesta | 2008-2023 | 1.25 / 1.4 Duratec | – eklenmedi: Kullanıcılar 1.25 ve 1.4 benzinlileri sorunsuz olarak anıyor; kronik sorun bulunamadı. |
| 2 | Focus 3 | 2015-2018 | 1.5 EcoBoost 150/182 | ◐ 1 ortak aile sorunu — Focus için sonuçlar ağırlıkla 1.0 EcoBoost; Focus'a özgü 1.5 EcoBoost kaynağı yok. Gösterilen silindir kapağı sorunu aynı motoru kullanan Kuga 2 / Mondeo kaydına dayanır. |
| 2 | Focus 4 | 2018- | 1.5 EcoBoost 150/182 | ◐ 1 ortak aile sorunu — Focus 4 1.5 EcoBoost'a özgü kaynak aranmadı; gösterilen silindir kapağı sorunu aynı motoru kullanan Kuga 2 / Mondeo kaydına dayanır. |
| 2 | Kuga 2 | 2013-2019 | 1.5 EcoBoost 150/182 | ✓ 1 sorun |
| 2 | Kuga 2 | 2013-2019 | 2.0 TDCi 140/150/180 | – eklenmedi: Faz 9'da arandı: 2011 model bir Kuga'da (Kuga 1) enjektör tutucu bacaklarının kırılması (tek vaka) ve Powershift'te düşük devirde vites düşürme gecikmesi, geri vitesten D'ye geçişte sarsıntı yorumları var; Şikâyetvar'daki turbo arızası şikâyetinde motor tipi belirtilmiyor. 2.0 TDCi için tekrar eden, iki siteyle doğrulanan sorun çıkmadı. |
| 2 | Kuga 2 / 3 | 2013- | Tüm motorlar (model geneli) | ✓ 1 sorun — Cam tavan perdesi arızası DonanımHaber ve Şikâyetvar'da geçiyor (iki nesli ve tekil vakaları kapsıyor). Soğutma sistemi / su eksilmesi ve piston arızaları motor konusu; panoramik tavan çatlaması (2022 model), silecek motoru ve korna arızası tek şikâyet; kapı su kaçağı ve multimedya için kaynak çıkmadı. |
| 2 | Puma | 2019- | 1.0 EcoBoost mHEV | ◐ 2 ortak aile sorunu, 2 yıl kırılımı — Forum görüşleri çelişkili (bazıları en sorunsuz 3 silindirli diyor); tekrar eden bir motor sorunu için kanıt yok. Gösterilen soğutma kaçağı ve yağ banyolu kayış sorunları aynı EcoBoost motorunu kullanan Fiesta, Focus ve EcoSport kaynaklarına dayanır. |
| 2 | S-Max / Galaxy | 2006-2023 | 2.0 TDCi / 2.0 EcoBlue | – eklenmedi: S-Max / Galaxy 2.0 TDCi'ya özgü kronik sorun kaynağı çıkmadı: bir forum yorumu 2.0 TDCi'da yakıt kalitesine bağlı enjektör ve volan sorunlarını anıyor, bir S-Max sahibi 3,5 yılda sorun yaşamadığını yazıyor; Powershift titremesi anlatıları modelsiz. |
| 2 | Transit Connect | 2013-2022 | 1.6 TDCi 75/95/115 (DV6) | ◐ 3 ortak aile sorunu — Transit Connect 1.5 TDCi için sonuç çıkmadı; 1.6 TDCi için modele özgü kaynak aranmadı. Gösterilen enjektör, turbo yağ süzgeci ve EGR / DPF sorunları aynı DV6 motorunu kullanan Peugeot 301, Citroën C-Elysée, Ford Focus ve Fiesta kaynaklarına dayanır. |
| 3 | B-Max | 2012-2017 | 1.6 Ti-VCT 105 (Powershift DPS6) | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — B-Max'e özgü kaynak aranmadı; gösterilen kavrama ve TCM sorunları Focus 3, Fiesta ve Volvo V40 / S60 kaynaklarına dayanır. |
| 3 | B-Max | 2012-2017 | 1.0 EcoBoost 100/125 | ◐ 2 ortak aile sorunu, 2 yıl kırılımı — B-Max'e özgü kaynak aranmadı; gösterilen sorunlar aynı EcoBoost motorunu kullanan Fiesta, Focus ve EcoSport kaynaklarına dayanır. |
| 3 | EcoSport | 2013-2022 | 1.0 EcoBoost | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 3 | Ka | 2008-2016 | 1.2 benzinli | ○ sırada |
| 3 | Kuga 1 | 2008-2012 | 2.0 TDCi (Powershift) | ○ sırada |
| 3 | Mondeo | 2007-2019 | 2.0 / 1.6 TDCi | – eklenmedi: Mondeo için tekil direksiyon, enjektör ve DPF anlatıları var. |
| 3 | Puma Gen-E / Mustang Mach-E / Explorer Electric | 2022- | Elektrik | – eklenmedi: Şikâyetvar'da Puma Gen-E için sürüş sırasında şarj hatası (iki kez yol yardımı) ve batarya su sızıntısı tekil; Mustang Mach-E ve Explorer Electric için kayıt çıkmadı. |
| 3 | Ranger | 2012- | 2.2 / 3.2 TDCi | – eklenmedi: Şikâyetvar'da turbo ve hortum şikâyetleri var; 2.2 ve 3.2 TDCi'ye özgü ikinci bağımsız kaynak çıkmadı. |
| 3 | Transit Custom | 2012- | 2.0 EcoBlue | – eklenmedi: Yağ tüketimi ve turbo şikâyetleri yalnızca Şikâyetvar'da; ikinci bağımsız kaynak bulunamadı. |

### Kia

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Ceed | 2012-2018 | 1.6 CRDi | ✓ 1 sorun (+1 ortak aile) |
| 1 | Ceed (ED / JD) | 2009-2016 | Tüm motorlar (model geneli) | ✓ 1 sorun, 1 yıl kırılımı — Ön göğüs kabarması Şikâyetvar ve DonanımHaber'de (üç başlık) doğrulandı. Şikâyetvar'da EPS arızası (2010 model, kronik denmiş), 2017 modelde volan sesi ve forumda boya kalınlığı tartışması tekil kaldı. |
| 1 | EV6 | 2022- | Elektrik (E-GMP, 77,4 kWh) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Rio | 2011-2017 | 1.4 CRDi 90 | ✓ 1 sorun (+1 ortak aile) |
| 1 | Sportage QL FL / NQ5 | 2018- | 1.6 CRDi 136 (7DCT) | ✓ 1 sorun (+2 ortak aile) |
| 1 | Sportage SL / QL | 2010-2021 | 1.6 GDI 135 | ✓ 1 sorun |
| 1 | Sportage SL / QL | 2010-2018 | 1.7 CRDi 115/141 | – eklenmedi: Faz 9'da arandı: 1.7 CRDi'ya özgü kronik arıza çıkmadı; turbo mili, enjektör ve DPF vakaları 1.6 CRDi ve 2020 sonrası araçlara ait (7DCT titremesi Sportage 1.6 CRDi kaydında). |
| 2 | Ceed | 2012-2021 | 1.4 / 1.6 MPI | – eklenmedi: 1.4 ve 1.6 MPI benzinlilerde motora özgü kronik sorun çıkmadı; torpido ve konsol kabarması motor tipinden bağımsız. |
| 2 | Ceed CD | 2018- | T-GDI benzinli (7DCT) | ✓ 1 sorun |
| 2 | EV3 | 2024- | Elektrik (58,3 / 81,4 kWh) | ✓ 1 sorun |
| 2 | Niro EV | 2019- | Elektrik | – eklenmedi: Şikâyetvar'da menzil, DC şarj süresi ve batarya bağlantı ünitesi (parçanın Türkiye'de bulunmaması) şikâyetleri tekil; ikinci bağımsız kaynak yok. EV3 ICCU arızası Faz 6'da ayrı kayıt oldu; ICCU geri çağırması Kia EV6 kaydında. |
| 2 | Picanto | 2017- | 1.0 / 1.2 MPI | ✓ 1 sorun |
| 2 | Rio | 2011-2017 | 1.4 MPI 100 | – eklenmedi: Forumlarda sorunsuz olarak anılıyor; kronik sorun bulunamadı. |
| 2 | Rio | 2011-2023 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da kapı fitillerinin erimesi (2012-2016 modeller; servisler 11 yaşındaki araçta normal bulmuş), 2020 modelde CarPlay kopması tekrar ediyor; DonanımHaber ve Ekşi Sözlük'te Rio'ya özgü ikinci site çıkmadı. |
| 2 | Rio YB | 2017-2023 | 1.4 MPI 100 | – eklenmedi: Faz 9'da arandı: DonanımHaber'de Rio 1.4 MPI ve 6 ileri tork konvertörlü otomatik için sorunsuz yorumları var (bir sahip yaklaşık 27.500 km'de sorun yaşamadığını yazıyor). Rio UB 1.4 CRDi DPF sorunu ayrı kayıtta. |
| 2 | Rio YB | 2017-2023 | 1.0 T-GDI 100 (7DCT) | ◐ 1 ortak aile sorunu — Rio 1.0 T-GDI için kaynak çıkmadı; gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. |
| 2 | Stonic | 2017- | 1.4 MPI 100 (6 ileri otomatik) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Carens | 2013-2019 | 1.7 CRDi / 1.6 GDI | ○ sırada |
| 3 | Ceed / Rio | 2010-2021 | 1.4 MPI, 1.25 | – eklenmedi: Ceed 1.4 MPI ve Rio 1.25 için motor kaynaklı kronik sorun çıkmadı; Ceed şikâyetleri torpido / konsol çatlaması ve start-stop üzerine. |
| 3 | Ceed CD | 2018- | 1.6 CRDi 115/136 | ◐ 3 ortak aile sorunu — Faz 9'da arandı (tek sorgu, T-GDI ile birlikte): Ceed CD'ye özgü sonuçlar 7DCT silkelemesinde toplandı (T-GDI satırında kayıtlı); 1.6 CRDi motoru ve yağ eksiltme için bilgi çıkmadı. Gösterilen DPF / yağa mazot karışması ve enjektör kodlama sorunları Tucson NX4, Rio UB ve Ceed kayıtlarına dayanır. |
| 3 | Cerato | 2013-2018 | 1.6 (arka stop ve bagajdan su alma) | – eklenmedi: Su alma şikâyetleri Şikâyetvar'da çok, ancak kilometre ve model yılı verisi yok ve ikinci bağımsız kaynak (Ekşi'de tek yorum) sınırlı. |
| 3 | EV9 | 2024- | Elektrik | – eklenmedi: Şikâyetvar'da hızlı şarjın araç tarafından durdurulması (yaklaşık 20.000 km) ve batarya elektrik arızası (üç hafta serviste) tekil. CarComplaints'te ABD'deki 2024 EV9'lara ait elektrik sistemi şikâyetleri var ancak Türkiye şikâyetleriyle aynı arıza değil; NHTSA'nın ICCU geri çağırmasının EV9'u kapsadığı doğrulanamadı (EV6 kaydı). |
| 3 | Niro / Cerato / Sorento | 2011- | Hybrid / 1.6 / 2.2 CRDi | – eklenmedi: Cerato ve Niro için sonuç çıkmadı; Sorento 2.2 CRDi için yalnızca tekil şikâyetler var. |
| 3 | Optima | 2012-2020 | 1.7 CRDi / 2.0 | ○ sırada |
| 3 | Seltos / XCeed | 2019- | 1.6 MPI / 1.0 / 1.4 T-GDI | ○ sırada |
| 3 | Sorento / Venga | 2010-2018 | 2.2 CRDi / 1.4 CRDi | – eklenmedi: Sorento 2.2 CRDi ve Venga 1.4 CRDi için kaynak çıkmadı. |
| 3 | Soul | 2009-2019 | 1.6 CRDi / 1.6 GDI | ○ sırada |
| 3 | Sportage QL | 2015-2018 | 1.6 T-GDI 177 (7DCT) | ◐ 1 ortak aile sorunu — Faz 9'da arandı (tek sorgu): Şikâyetvar ya da DonanımHaber kaydı çıkmadı; sonuçlar genel inceleme ve teknik özellik sayfalarından oluştu. 7DCT kavrama titremesi Sportage 1.6 CRDi kaydında; gösterilen sorun 7DCT ailesinden. |
| 3 | Sportage QL | 2015-2018 | 1.7 CRDi 115/141 (6MT ve 7DCT) | ◐ 3 ortak aile sorunu — Sportage 1.7 CRDi için motor kaynaklı kronik sorun çıkmadı. Gösterilen DPF / yağa mazot karışması ve enjektör kodlama sorunları Tucson NX4, Rio UB ve Ceed kayıtlarına dayanır. Gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. |
| 3 | Stonic | 2017- | 1.0 T-GDI / 1.6 CRDi | ◐ 4 ortak aile sorunu — 1.0 T-GDI için tekil titreme ve arıza lambası şikâyetleri; 1.6 CRDi için sonuç çıkmadı. Gösterilen 7DCT kavrama titremesi Tucson, Sportage, Bayon, i20 (BC3) ve Ceed kayıtlarına dayanır. Gösterilen DPF / yağa mazot karışması ve enjektör kodlama sorunları Tucson NX4, Rio UB ve Ceed kayıtlarına dayanır. |

### Dacia

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Duster | 2010-2017 | 1.5 dCi (K9K) | ✓ 2 sorun |
| 1 | Duster | 2021-2024 | 1.0 TCe 100 ECO-G (H4Dt) | ✓ 1 sorun |
| 1 | Duster (2010-2017) | 2010-2017 | Tüm motorlar (model geneli) | ✓ 1 sorun — Direksiyon sertleşmesi ve EPS arızası Şikâyetvar ve DonanımHaber'de geçiyor; sorun hidrolik pompa ile EPS arasında dağınık ve model yılına göre yaygınlığı belirsiz. 2010-2017 Duster'da kapı su alması için kaynak çıkmadı; ESP ısıtma bujisi (2015 model) tek şikâyet. |
| 1 | Sandero / Logan / Symbol | 2013-2020 | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da Easy-R otomatik şanzımanda titreme (ayrı bir motor/şanzıman konusu), otomatik kilit algılama ve sağ kapının kilitlenmemesi, Logan MCV'de kapı ikaz lambası, ön göğüs sesi ve far buğulanması tekil şikâyetler olarak geçiyor; ikinci bağımsız site yok (DonanımHaber sonucu yaklaşık 16 yıllık Logan yorumu). Fren hortumu, ön takım ve boya için kaynak çıkmadı. |
| 1 | Sandero / Sandero Stepway | 2021- | 1.0 TCe 90/100 (H4Dt) | ✓ 1 sorun |
| 2 | Duster | 2018-2021 | 1.5 dCi 110 (K9K) | ✓ 1 sorun (+1 ortak aile) |
| 2 | Duster | 2019-2024 | 1.3 TCe 130/150 (EDC) | ✓ 1 sorun (+1 ortak aile) |
| 2 | Sandero / Logan / Symbol | 2013-2020 | 0.9 TCe 90 (H4Bt) | ✓ 1 sorun |
| 2 | Sandero / Logan / Symbol | 2013-2020 | 1.5 dCi 75/90 (K9K) | ✓ 1 sorun (+1 ortak aile) |
| 3 | Duster | 2018-2021 | 1.6 SCe 115 | – eklenmedi: Kaynaklarda bu motor için öne çıkan bir sorun bulunamadı. |
| 3 | Jogger | 2022- | 1.0 TCe 110 (manuel) | ✓ 1 sorun |
| 3 | Jogger | 2022- | 1.0 TCe 100 ECO-G (LPG) | – eklenmedi: LPG / ECO-G şikâyetleri tekil ve Jogger'a özgü değil (Dacia Eco-G genelinde); ikinci bağımsız kaynak bulunamadı. |
| 3 | Lodgy / Dokker | 2012-2021 | 1.5 dCi (K9K) | ◐ 2 ortak aile sorunu — Lodgy / Dokker 1.5 dCi için turbo ya da enjektör örüntüsü çıkmadı; şikâyetler teyp ekranı ve elektrikte. Gösterilen enjektör ve EGR sorunları aynı K9K motorunu kullanan Duster, Sandero ve Renault kayıtlarına dayanır. |
| 3 | Spring | 2022- | Elektrik | – eklenmedi: Şikâyetvar'da 'akü şarj almıyor' uyarısı ve Ekşi Sözlük'te menzil kaybı tekil; sistematik bir şarj ya da batarya sorunu bulunamadı. |

### Audi (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | A3 8P FL / 8V | 2009-2020 | 1.4 TFSI (S tronic DQ200) | ✓ 1 sorun (+3 ortak aile), 2 yıl kırılımı |
| 1 | A3 8V | 2012-2020 | 1.6 TDI 105/110 | ✓ 2 sorun (+2 ortak aile) |
| 1 | A3 8V | 2012-2020 | Tüm motorlar (model geneli) | ✓ 1 sorun — Gündüz LED sararması iki sitede doğrulandı. MMI ekranın donması / kapanması / açılmaması Şikâyetvar'da çoğunlukla 2021 sonrası (8Y) araçlara ait (2015 model bir 8V sahibi de ekranın açılmadığını bildiriyor); cam tavan çevresi plastik çatlakları ve ön takım (2025 model) tekil. |
| 1 | A4 B8 | 2008-2015 | 1.8 TFSI / 2.0 TFSI (EA888 Gen2) | ✓ 4 sorun, 2 yıl kırılımı |
| 1 | A4 B8 | 2008-2015 | 2.0 TDI 143/150/177 (Multitronic) | ✓ 1 sorun |
| 1 | Q5 8R | 2008-2017 | 2.0 TDI | – eklenmedi: Q5 2.0 TDI için modele özgü kaynak çıkmadı: DonanımHaber'de Q5 başlıkları 2.0 TFSI yağ yakma (ayrı kayıtta), S tronic ve akü / alternatör üzerine; 2.0 TDI enjektör ve DPF anlatıları A5 / A6 başlıklarında ve eski 143-170 hp motorlara ait, 2.0 TDI için doğrulanmış bir sorun listesi çıkmadı. |
| 1 | Q5 FY | 2017- | 40 TDI 2.0 (quattro S tronic) / 45 TFSI | – eklenmedi: 2017 Q5 2.0 TDI quattro için DonanımHaber'de kronik sorun iddiası kaynaksız, aynı başlıktaki kullanıcılar 2.0 TDI 177 hp ve S tronic'in sağlam olduğunu yazıyor; yağ tüketimi anlatıları TFSI'ya ait. Doğrulanmış bir sorun çıkmadı. |
| 2 | A3 8V | 2012-2020 | 1.0 TFSI | – eklenmedi: 1.0 TFSI için yalnızca tekil anekdotlar (start-stop sonrası kalkış, far). |
| 2 | A3 8V | 2012-2020 | 1.2 TFSI 105 (EA211) | ◐ 1 ortak aile sorunu — 1.2 TFSI için A3'e özgü sonuç çıkmadı; gösterilen yağ tüketimi anlatısı aynı EA211 1.2 TSI motorunu kullanan Golf 7 kaynaklarına dayanır. S tronic şikâyetleri 1.4 TFSI ve 1.6 TDI kayıtlarında. |
| 2 | A3 8V (2.0 TDI / 1.8 TFSI) | 2012-2020 | 2.0 TDI 150 / 1.8 TFSI 180 | – eklenmedi: Bu oturumdaki aramada 8V 2.0 TDI 150 için model ya da motora özgü şikâyet çıkmadı; forumlarda en çok konuşulan konu S tronic şanzıman (titreme ve vuruntuyla başlayıp mekatronik arızasıyla biten anlatılar; kullanım alışkanlığına bağlayan yorumlar), enjektör ve DPF anlatıları ise genel ya da eski (2006 model) araçlara ait. Bir forum kullanıcısı 2.0 TDI'larda 6 ileri DQ250 kullanıldığını ve nadiren sorun çıkardığını yazıyor; kuru kavramalı DQ200 kaydı 1.4 TFSI ve 1.6 TDI için ayrı. |
| 2 | A3 8Y | 2020- | 35 TFSI 1.5 (48V hafif hibrit, S tronic) | ✓ 1 sorun (+2 ortak aile) |
| 2 | A4 B9 | 2016- | 2.0 TFSI / 2.0 TDI | – eklenmedi: B9 için doğrudan kronik sorun listesi çıkmadı; yağ eksiltme şikâyetleri çoğunlukla B8 dönemine ait (kayıtlı), B9'a özgü olanlar tekil (tahrik uyarısı, stop lambası çatlağı). |
| 2 | A5 8T | 2008-2016 | 1.8 TFSI / 2.0 TFSI (EA888) | ◐ 3 ortak aile sorunu, 2 yıl kırılımı — A5'e özgü kaynak aranmadı; gösterilen sorunlar aynı EA888 motorunu kullanan A4 B8 ve Q5 kaynaklarına dayanır. |
| 2 | Q2 | 2016- | 1.0 TFSI 116 / 1.4 TFSI 150 | ◐ 3 ortak aile sorunu — Q2'ye özgü kaynak aranmadı; gösterilen sorunlar aynı motor ve S tronic şanzımanı kullanan Polo, Golf 7 ve Octavia kayıtlarına dayanır. |
| 2 | Q3 8U | 2011-2014 | 2.0 TFSI 170/211 (EA888 Gen2) | ◐ 3 ortak aile sorunu, 2 yıl kırılımı — Q3'e özgü kaynak bulunamadı; gösterilen sorunlar aynı motorları kullanan A4 / Q5 (2.0 TFSI) ve Golf / Octavia (1.4 TSI) kayıtlarına dayanır. |
| 2 | Q3 8U | 2014-2018 | 1.4 TFSI 150 (ACT) | ◐ 1 ortak aile sorunu — Q3'e özgü kaynak bulunamadı; gösterilen sorunlar aynı motorları kullanan A4 / Q5 (2.0 TFSI) ve Golf / Octavia (1.4 TSI) kayıtlarına dayanır. |
| 3 | A1 (8X) | 2010-2014 | 1.4 TFSI 122 (S tronic) | ◐ 3 ortak aile sorunu, 1 yıl kırılımı — A1'e özgü kaynak çıkmadı; gösterilen sorunlar aynı motor ve şanzımanı kullanan Golf 6, Polo ve A3 kayıtlarına dayanır. A1 1.2 TFSI için kayıt açılmadı. |
| 3 | A1 (8X) | 2010-2018 | 1.6 TDI 90/116 | ◐ 2 ortak aile sorunu — A1 1.6 TDI'ya özgü kaynak aranmadı; gösterilen sorunlar 1.6 TDI kayıtlarının ortak kaynaklarına dayanır. |
| 3 | A1 GB | 2018- | 25 TFSI 1.0 / 30 TFSI | ○ sırada |
| 3 | A3 8Y (30 TFSI / 2.0 TDI) | 2020- | 30 TFSI 1.0 / 35 TDI 2.0 | ○ sırada |
| 3 | A5 F5 | 2017- | 40 TDI / 40 TFSI 2.0 | ○ sırada |
| 3 | A6 C7 | 2011-2018 | 3.0 TDI / 2.0 TFSI | – eklenmedi: A6 C7'ye özgü kaynak bulunamadı; bulunan A6 2.0 TDI başlıkları C6 dönemine (2009-2011) ait. |
| 3 | A6 C7 | 2011-2014 | 2.0 TDI 177 (Multitronic) | ◐ 1 ortak aile sorunu — A6 C7'ye özgü kaynak bulunamadı; bulunan A6 2.0 TDI başlıkları C6 dönemine (2009-2011) ait. Gösterilen Multitronic sorunu A4 B8 (aynı 0AW şanzıman) kayıtlarına dayanır. |
| 3 | A6 C8 | 2018- | 40 TDI 2.0 / 45 TFSI | ○ sırada |
| 3 | A7 4G | 2010-2018 | 3.0 TDI / 2.0 TFSI | ○ sırada |
| 3 | Q2 / Q3 | 2016- | 35 TFSI (1.5) | ◐ 4 ortak aile sorunu — Şikâyetvar'da Q2 35 TFSI için 2024 model bir araçta sürekli tahrik hatası, Q3 için alternatör şüphesiyle yolda kalma gibi tekil kayıtlar var; Q2 / Q3'e özgü ikinci bağımsız kaynak çıkmadı. Gösterilen yağ eksiltme ve titreşim sorunları aynı motoru kullanan Karoq, Passat ve Tiguan kayıtlarına dayanır. |
| 3 | Q3 8U | 2011-2018 | 2.0 TDI | – eklenmedi: Q3 2.0 TDI için modele özgü kaynak bulunamadı. |
| 3 | Q3 F3 (dizel) | 2018- | 35 TDI 2.0 | ○ sırada |
| 3 | Q4 e-tron / e-tron | 2021- | Elektrik | – eklenmedi: Şikâyetvar'da uzaktan erişim hizmetinin Türkiye'de kapalı olması, yeni araçta akü arızası ve menzil şikâyetleri tekil; ikinci site yok. e-tron GT için Mart 2024 batarya modülü geri çağırmaları (93VM, 93VN; Taycan ile aynı modüller, şarjın %80 ile sınırlanması) var; Türkiye kapsamı doğrulanamadı. |
| 3 | Q5 8R | 2008-2017 | 2.0 TFSI (EA888) | ✓ 1 sorun (+2 ortak aile), 2 yıl kırılımı |
| 3 | Q7 4L / 4M | 2006- | 3.0 TDI | ○ sırada |
| 3 | TT 8S | 2014-2023 | 2.0 TFSI | ○ sırada |

### Honda (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Civic FC5 | 2016-2021 | 1.6 i-VTEC 125 (CVT) | ✓ 1 sorun |
| 1 | Civic FC5 | 2016-2021 | 1.5 VTEC Turbo (L15B7) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Civic FC5 | 2016-2021 | Tüm motorlar (model geneli) | ✓ 2 sorun — Klima radyatörü çatlaması ve boya atması Şikâyetvar ve CivicX'te (ABD) doğrulandı. Şikâyetvar'da yakıt pompası arızası (2018 model) ve ön cam tedarik gecikmesi tekil; CVT şanzıman şikâyetleri motor/şanzıman konusu (ayrı kayıt). |
| 2 | Accord | 2008-2015 | 2.0 i-VTEC / 2.2 i-DTEC | – eklenmedi: Faz 9'da arandı: Accord 2.0 i-VTEC / 2.2 i-DTEC için bu aramada veri çıkmadı (aynı sorgudaki Civic 1.6 i-DTEC DPF sorunu ayrı kayıtta). |
| 2 | CR-V | 2012-2018 | 1.6 i-DTEC | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 2 | CR-V | 2012-2018 | 2.0 i-VTEC | – eklenmedi: 2.0 i-VTEC için yağ eksiltme ve SRS şikâyetleri tekil kullanıcı anlatımları; ikinci bağımsız kaynak bulunamadı. |
| 2 | CR-V RW | 2017-2022 | 1.5 VTEC Turbo 173 (CVT) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — CR-V 1.5 VTEC Turbo'ya özgü kaynak aranmadı; gösterilen yağa yakıt karışması aynı motor ailesini kullanan Civic FC5 kaydına dayanır. |
| 2 | City | 2009- | 1.5 i-VTEC / 1.5 Hybrid | – eklenmedi: City 1.5 için yakıt tüketimi ve vites geçişi şikâyetleri yalnızca Şikâyetvar'da (2021 model); ikinci bağımsız kaynak yok. |
| 2 | Civic FB7 | 2012-2015 | 1.6 i-VTEC / 1.8 i-VTEC | – eklenmedi: FB7 şikâyetleri ağırlıkla boya atması ve kozmetik; motora özgü sorunlar tekil (130 bin km'de motor yanması, 1.8 yağ sızıntısı için eski bir forum yazısı). |
| 2 | Civic FB7 | 2012-2016 | Tüm motorlar (model geneli) | ✓ 1 sorun — Beyaz renkte boya atması Şikâyetvar ve DonanımHaber'de geçiyor. İç kapı kolu soyulması (2012 model, bazılarına ücretsiz değişim), ön cam parça bekleme süresi ve direksiyon kutusu tıkırtısı tekil. |
| 2 | Civic FC5 (dizel) | 2016-2021 | 1.6 i-DTEC 120 (9 ileri otomatik) | ✓ 1 sorun (+1 ortak aile), 1 yıl kırılımı |
| 3 | Civic FB7 | 2013-2016 | 1.6 i-DTEC 120 | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — Civic FB7 1.6 i-DTEC'e özgü kaynak aranmadı; gösterilen DPF ve turbo hortumu sorunları aynı N16A motorunu kullanan Civic FC5 ve CR-V kayıtlarına dayanır. |
| 3 | HR-V RU | 2015-2021 | 1.6 i-DTEC 120 | ◐ 2 ortak aile sorunu, 1 yıl kırılımı — HR-V 1.6 i-DTEC'e özgü kaynak aranmadı; gösterilen DPF ve turbo hortumu sorunları aynı N16A motorunu kullanan Civic FC5 ve CR-V kayıtlarına dayanır. |
| 3 | Jazz / HR-V | 2011- | 1.3 / 1.5 i-VTEC | – eklenmedi: 1.3 / 1.5 i-VTEC CVT için kanıtlı kronik sorun çıkmadı; bulunanlar eski nesil Jazz CVT, eski kasa HR-V yorumu ve hibrit akü şikâyeti. |

### Seat (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Leon 5F | 2012-2020 | 1.2 TSI / 1.6 TDI (DSG DQ200) | ✓ 1 sorun (+4 ortak aile) |
| 1 | Leon 5F | 2012-2020 | 1.4 TSI 122/125/140/150 (EA211, ACT) | ◐ 1 ortak aile sorunu — Faz 9'da arandı: 1.4 TSI ACT için zincir ve yağ eksiltme anlatıları çoğunlukla 1.2 TSI'ya ait; Şikâyetvar'da 1.4 TSI Leon sahibinin zincir şüphesi (ustanın doğrulanmamış teşhisi) ve 2020 model bir Leon'da ACT valf hortumu yırtığı tekil vakaları var. Gösterilen devirdaim sorunu Octavia A7 ve Golf 7 kayıtlarına dayanır; DSG kavrama ve mekatronik sorunları Leon 5F 1.2 TSI / 1.6 TDI (DSG DQ200) kaydında. |
| 1 | Leon 5F | 2013-2020 | Tüm motorlar (model geneli) | ✓ 1 sorun — Trim sesleri DonanımHaber ve Şikâyetvar'da doğrulandı. Şikâyetvar'da cam tavan mikasının kendiliğinden çatlaması (2015 model), tavan boyasının kabarması ve sis farı buğulanması (2020 model) tek sitede kaldı; multimedya için kaynak çıkmadı. |
| 2 | Ibiza / Arona / Ateca | 2017- | Tüm motorlar (model geneli) | – eklenmedi: Şikâyetvar'da Ibiza'da CarPlay'in tam ekran olmaması, far içi lekelenme ve arka kamera görüşü; Ateca'da klima menfez düğmeleri, stop lambası çatlakları, menfez düşmesi, far buğulanması ve sağ ön amortisör sesi (servis kronik dedi); Arona'da bagaj sesi ve amortisör takozu gıcırtısı tekrar ediyor. DonanımHaber'de yalnızca genel 'Seat kronik sorunları' başlığı var; modele özgü ikinci site çıkmadı. |
| 2 | Ibiza 6F | 2017- | 1.0 TSI 95/115 (DSG DQ200) | ◐ 2 ortak aile sorunu — Ibiza 1.0 TSI için kaynak bulunamadı; gösterilen DSG sorunları DQ200 kayıtlarına dayanır. |
| 2 | Ibiza 6J / 6P | 2008-2017 | 1.2 TSI (DSG DQ200) | ✓ 1 sorun (+1 ortak aile) |
| 2 | Ibiza 6J / 6P | 2008-2017 | 1.6 TDI | – eklenmedi: Ibiza 1.6 TDI için yalnızca tekil bir direksiyon (EPS) şikâyeti çıktı. Zincir iddiası Ibiza'ya özgü değil. |
| 2 | Leon 5F FL | 2018-2020 | 1.5 TSI 130/150 (ACT) | ◐ 2 ortak aile sorunu — Şikâyetvar'da 2018 model 1.5 TSI Leon sahibi yetkili servisin bir litreye yakın yağ eksiltmeyi normal saydığını ve litre başına ücret istediğini yazıyor; DonanımHaber'deki 2019 Leon FR 1.5 TSI 150 başlığında cam tavan titremesi ve DSG mekatronik değişimi anılıyor. Tekil kayıtlar; gösterilen yağ eksiltmesi aynı motoru kullanan Karoq ve Passat kayıtlarına dayanır. |
| 2 | Leon KL | 2020- | 1.0 eTSI / 1.5 eTSI (48V hafif hibrit, DSG) | ✓ 1 sorun (+2 ortak aile) |
| 3 | Alhambra | 2010-2020 | 2.0 TDI / 1.4 TSI | ○ sırada |
| 3 | Altea / Altea XL | 2004-2015 | 1.2 TSI / 1.6 TDI / 2.0 TDI | ○ sırada |
| 3 | Ateca / Arona | 2016- | 1.0 TSI / 1.5 TSI | ◐ 4 ortak aile sorunu — Ateca'ya özgü ikinci bağımsız kaynak çıkmadı: Şikâyetvar'da tek kayıt var (24.000 km'de dört kez yağ eksik uyarısı). Arona 1.0 TSI DSG için yalnızca tekil kayıtlar (DSG vuruntusu, yağ kaçağı). Gösterilen sorunlar aynı motor ve şanzımanı kullanan diğer VAG kayıtlarına dayanır. |
| 3 | Mii | 2012-2021 | 1.0 MPI | ○ sırada |
| 3 | Toledo | 2012-2019 | 1.2 TSI / 1.6 TDI (DSG) | ◐ 4 ortak aile sorunu — Faz 9'da arandı (tek sorgu): Türkçe kaynak çıkmadı; sonuçlar tanıtım ve ilan sayfaları ile İspanyolca bir sorun sayfasından oluştu (DQ200'de kalkışta kayma ve sarsıntı, 1.6 TDI'da DPF tıkanma eğilimi). Gösterilen sorunlar aynı motor ve şanzımanı kullanan Leon 5F, Rapid ve Polo kayıtlarına dayanır. |

### Chevrolet (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Captiva / Aveo / Lacetti | 2007-2016 | 2.0 VCDi, 1.4 / 1.2 | – eklenmedi: Captiva 2.0 D ve Aveo 1.4 zincir iddiaları tek rehber sitesine dayanıyor; Lacetti için sonuç çıkmadı. |

### Volvo (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | S60 II / V60 | 2010-2018 | D3 / D4 / D5, T4 / T5 | – eklenmedi: Bu oturumdaki aramada Türkçe kaynakların çoğu S60'a ait ve en çok tekrarlanan konu D2 Powershift (ayrı kayıtta); V60 ve D3 / D4 / D5 Drive-E için özel veri az. 1.6 T4 EcoBoost için hararet, soğutma suyu eksilmesi ve silindir kapağı contası iddiaları var (Şikâyetvar ve DonanımHaber; 65-70 bin TL'lik blok değişimi teklifi gibi eski tarihli tekil vakalar), ancak kilometre bilgisi ve tekrar örüntüsü doğrulanamadı. |
| 1 | XC60 (2008-2017) | 2008-2017 | 2.4 D5 / D4 2.0 (Drive-E) / T5 | – eklenmedi: Bu oturumdaki aramada DonanımHaber'de 2011 model XC60 D5'te otomatik şanzımanda D'ye alırken sektirme (yağ değişiminin biraz iyileştirdiği) ve 2016 model D4'te yaklaşık 300.000 km'de blok çatlağı gibi tekil anlatılar çıktı; enjektör için kayıt yok. Tekrar eden bir sorun için iki bağımsız site çıkmadı. |
| 2 | EX30 / XC40 Recharge | 2021- | Elektrik | – eklenmedi: EX30 için hücre kusuru geri çağırması var (Sunwoda hücreleri, %70 şarj sınırı, modül değişimi); Avrupa'da yalnızca sağ direksiyonlu 69 kWh modelleri kapsadığı yazılıyor ve Türkiye kapsamı doğrulanamadı. Şikâyetvar'daki hızlı şarj, 'Electric Drive Fault' ve XC40 Recharge motor / batarya şikâyetleri tekil. |
| 2 | S90 / V90 | 2016- | D4 / D5 / T5 / T6 | – eklenmedi: Bu oturumdaki aramada S90 / V90 için motora özgü tekrar eden sorun çıkmadı; belirgin vakalar tekil: DonanımHaber'de 2017 model S90 D5'te piston deformasyonu ve yağın turbolara kaçması nedeniyle motor değişimi (tüketici hakem heyeti süreci ve Yargıtay'ın Mart 2025'te araç değişimi kararını onaması; konuda bir yorumcu sorunun kronik görünmediğini yazıyor), Şikâyetvar'da dizel hibrit bir S90'da 102.500 km'de tekrarlayan soğutma suyu arızası ve 2021 model S90 B5'te termostat arızası → conta yanması → 126.000 km'de motor indirme. Diğer şikâyetler bilgi-eğlence donmaları, sunroof tahliye kanalı, titreşim ve garanti / servis uyuşmazlıkları; kayıt açılmadı. |
| 2 | V40 (2012-2019) | 2012-2019 | D4 2.0 (Drive-E) / T3 / T4 / T5 | – eklenmedi: Bu oturumdaki aramada V40 D4 / T3 / T4 için tekrar eden tek bir sorun çıkmadı: T3 ile gelen Aisin Geartronic için forum yorumları olumlu, dizeldeki Powershift şikâyetleri D2 kaydında ayrı ele alınıyor. Şikâyetvar'da T3 için 4 yılda 4. kez turbo arızası ve 2017 modelde su haznesi kaynaklı ısınma uyarısı tekil vakalar; Ekşi Sözlük'te tekrarlayan düşük motor performansı uyarısı ve dizelde partikül filtresi anlatıları tekil. Kilometre bilgisi ve ikinci bağımsız doğrulama yetersiz olduğundan kayıt açılmadı. |
| 2 | V60 | 2013-2018 | D2 1.6 D DRIVe (Powershift) | ◐ 5 ortak aile sorunu, 1 yıl kırılımı — V60 D2'ye özgü kaynak aranmadı (S60 / V40 D2 ile aynı motor ve şanzıman); gösterilen sorunlar S60 / V40 D2 Powershift ve DV6 kayıtlarına dayanır. |
| 2 | XC40 (2018-) | 2018- | T3 / T4 / D3 / B4 (hafif hibrit) | – eklenmedi: Bu oturumdaki aramada motor tipine göre ayrılabilen tekrar eden sorun çıkmadı. Şikâyetvar'da 2020 model XC40 T3 için 5 yılda 6 aks değişimi ve garanti reddi (tek vaka), 2021 modelde 8 kez SRS (hava yastığı) arızası, 2023 modelde (motor tipi belirtilmemiş) tahrik sistemi arızasıyla 6 ayda 4 kez yolda kalma anlatıları var; DonanımHaber'de T3 üç silindirli motorda yağ eksilmesi kronik mi diye tartışmalı (bir kullanıcı sorun yaşamadığını yazıyor). Ön takım tıkırtısı yeni araçlarda (XC40 / EX40) dünya genelinde bilinen sorun olarak anılıyor (tek kaynak). Kilometre bilgisi ve ikinci bağımsız doğrulama yetersiz olduğundan kayıt açılmadı. |
| 2 | XC60 (2017-) | 2017- | D4 / D5 / T5 / B4 | – eklenmedi: Bu oturumdaki aramada Şikâyetvar'da 2020 model XC60'larda turbo arızası (70.000 km) ve B4 dizelde partikül sensörü şikâyeti gibi tekil kayıtlar çıktı; ikinci bağımsız kaynak yok. |
| 2 | XC90 (2002-2014) | 2002-2014 | 2.4 D5 / 3.2 | – eklenmedi: Bu oturumdaki aramada DonanımHaber'de XC90 2.4 D5 için kronik sorunları da kapsayan bir inceleme başlığı ve 2007 model 2.4 D5 sorunları başlığı çıktı; bir kullanıcı T (benzinli) motorların arızalı olduğunu duyduğunu, 2.4 D motorlardan şikâyet duymadığını yazıyor (tekil yorum). Şanzımanda sorunun sık yaşandığı ama tamirden sonra yeniden çıkmadığı yazılıyor; Şikâyetvar'da bir şanzıman arızası, yüksek masraf ve uzun parça bekleme süresi şikâyeti var (tek vaka). 2.4 D5 enjektörü için doğrudan kayıt çıkmadı; kilometre bilgili, ikinci siteyle doğrulanmış sorun oluşmadı. |
| 2 | XC90 (2015-) | 2015- | D5 / T5 / T6 | – eklenmedi: Bu oturumdaki aramada 2015 sonrası D5 / T5 / T6'yı kuşak olarak ayırabilen kayıt çıkmadı (sonuçlar çoğunlukla eski kuşağa ait). Bir forum yorumu benzinli T6 için erken vites kaydırma ve güç kaybı şanzıman sorunlarını anıyor (kuşak belirtilmemiş); Şikâyetvar'da far içine su alması ve garanti uygulamaları üzerine bir şikâyet var (tek vaka). |
| 3 | S60 / V40 | 2011-2018 | 1.6 D DRIVe (Powershift) | ✓ 1 sorun (+4 ortak aile) |
| 3 | S80 / V70 / XC70 | 2007-2016 | D5 2.4 / D4 | ○ sırada |

### Subaru (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Forester | 2013-2018 | 2.0D | ○ sırada |
| 3 | Forester SJ | 2013-2018 | 2.0 boxer 150 (FB20) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — Forester'a özgü kaynak aranmadı; gösterilen aşırı yağ tüketimi aynı FB20 motorunu kullanan XV kaydına dayanır. |
| 3 | Impreza GJ / GK | 2012-2022 | 2.0 boxer 150 (FB20) | ◐ 1 ortak aile sorunu, 1 yıl kırılımı — Impreza'ya özgü kaynak aranmadı; gösterilen aşırı yağ tüketimi aynı FB20 motorunu kullanan XV kaydına dayanır. |
| 3 | Impreza GJ / GK | 2012-2022 | 1.6 (FB16) | ○ sırada |
| 3 | Outback | 2010-2020 | 2.5 / 2.0D | ○ sırada |
| 3 | XV | 2012-2017 | 2.0 benzinli boxer | ✓ 1 sorun, 1 yıl kırılımı |

### Mini (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Cooper / One (F56) | 2014- | 1.5 üç silindir turbo (B38) | ◐ 1 ortak aile sorunu — F56 1.5 üç silindir için kaynak çıkmadı; bir Ekşi yorumu yağ kaçırdığını söylüyor ama motor belirsiz. Gösterilen turbo manifoldu çatlaması aynı B38 motorunu kullanan 1 Serisi (F20 LCI) kaydına dayanır. |
| 3 | Cooper S / Countryman S (R56 / R60) | 2007-2016 | 1.6 turbo benzinli (N14 / N18) | ✓ 1 sorun (+2 ortak aile) |
| 3 | Cooper SE | 2020- | Elektrik | – eklenmedi: Şikâyetvar'da dört kayıt (sürüş kontrolü kaybı iddiası, 37 gün parça beklemesi); DonanımHaber yorumları olumlu. Tekrar eden bir arıza örüntüsü yok. NHTSA 24V-612 geri çağırması 2020-2024 Cooper SE'yi kapsıyor (12.535 araç; yazılımla bataryanın %30'un altına boşaltılması, yangın riski); Türkiye kapsamı ve Türkiye'den bir şikâyet bulunamadı. |
| 3 | Countryman F60 | 2017- | Cooper / Cooper S 1.5 - 2.0 (B38 / B48) | ○ sırada |

### Jeep (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 2 | Avenger Electric | 2023- | Elektrik (54 kWh, 156 PS) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Cherokee KL | 2014- | 2.0 MultiJet / 2.4 MultiAir | ○ sırada |
| 3 | Compass | 2017- | 1.6 MultiJet 120 (6MT ve DDCT) | ◐ 3 ortak aile sorunu — Compass şanzıman şikâyetlerinde motor ve şanzıman kombinasyonu belirsiz. Gösterilen çift kütleli volan ve EGR / DPF sorunları aynı Multijet II motorunu kullanan Egea 1.6 kaydına dayanır. |
| 3 | Grand Cherokee WK2 | 2011-2021 | 3.0 CRD / 3.6 V6 | ○ sırada |
| 3 | Renegade | 2015- | 1.6 MultiJet 120 (6MT ve DDCT) | ◐ 3 ortak aile sorunu — Renegade DDCT'ye özgü kaynak çıkmadı (sonuçlar Egea üzerinden geldi). Gösterilen çift kütleli volan ve EGR / DPF sorunları aynı Multijet II motorunu kullanan Egea 1.6 kaydına dayanır. DDCT kavrama sorunu Egea 1.6 kaydına dayanır. |
| 3 | Renegade / Compass | 2015- | 1.4 MultiAir | – eklenmedi: Renegade ve Compass 1.4 MultiAir için kaynak çıkmadı. |
| 3 | Wrangler JK / JL | 2007- | 2.8 CRD / 3.6 V6 / 2.0 turbo | ○ sırada |

### Alfa Romeo (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Giulia | 2016- | 2.0 Turbo / 2.2 JTDm | ○ sırada |
| 3 | Giulietta | 2010-2020 | 1.4 MultiAir | – eklenmedi: Giulietta 1.4 MultiAir için kaynak çıkmadı; şikâyetler gövde ve elektronikte (yolcu airbag kapağı şişmesi, klima). |
| 3 | Giulietta | 2014-2020 | 1.6 JTDm 120 (Multijet II) | ◐ 2 ortak aile sorunu — Şikâyetler gövde ve elektronikte (yolcu airbag kapağı şişmesi, klima); motora özgü kaynaklı bulgu yok. Gösterilen çift kütleli volan ve EGR / DPF sorunları aynı Multijet II motorunu kullanan Egea 1.6 kaydına dayanır. |
| 3 | Junior Elettrica | 2024- | Elektrik (54 kWh, 156 PS) | – eklenmedi: Şikâyetvar'da 2025-2026 tarihli tekrarlayan 'elektrikli çekiş sistemi arızası' uyarısı (bir araç yaklaşık 90 gün serviste), 900 km'de yolda kalıp şarj almama ve batarya sızıntısı şikâyetleri var; ikinci bağımsız site bulunamadı. Aynı 54 kWh / 156 PS değerlerine sahip Avenger Electric ve Fiat 600e ayrı kayıtlarda. |
| 3 | MiTo | 2008-2018 | 1.4 MultiAir / 1.3 JTDm | ○ sırada |
| 3 | Stelvio | 2017- | 2.0 Turbo / 2.2 JTDm | ○ sırada |

### Mazda (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | 3 / 6 / CX-5 | 2013- | Skyactiv-G / Skyactiv-D | – eklenmedi: Skyactiv motorlar için Türkiye'ye özgü kronik sorun kaynağı çıkmadı; 2.2 dizelin Türkiye'de satılmadığı yazılıyor. |

### Suzuki (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 2 | Swift | 2011-2017 | 1.2 (K12B) / 1.3 DDiS | – eklenmedi: Şikâyetvar'da en tekrarlanan konu multimedya / navigasyon donması ve geri görüş kamerası; Ekşi Sözlük ve Otopark'ta 4x4 şanzıman arızası, DonanımHaber'de direksiyon kutusu iddiaları tekil. 1.2 K12B için motor sorunu çıkmadı (DonanımHaber'de 1.2 GL otomatik sahibi bilinen kronik sorun olmadığını yazıyor). |
| 3 | Baleno / Ignis | 2016- | 1.2 Dualjet | ○ sırada |
| 3 | Jimny | 2018- | 1.5 | ○ sırada |
| 3 | SX4 S-Cross / Vitara / Swift | 2014- | 1.4 BoosterJet / 1.6 DDiS | – eklenmedi: Bulgular tek rehber sitesi (Araclo) ve Şikâyetvar'ın elektronik / multimedya şikâyetleriyle sınırlı. |

### Mitsubishi (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Eclipse Cross | 2018- | 1.5 T | ○ sırada |
| 3 | L200 / ASX / Lancer | 2010- | 2.5 DI-D / 1.6 MIVEC | – eklenmedi: L200 DPF ve turbo anlatıları rehber siteleri ve tekil Şikâyetvar kayıtları; ASX 1.6 MIVEC sıcak marş sorunu yalnızca Ekşi'de. |
| 3 | Outlander | 2012- | 2.0 MIVEC / 2.2 DI-D | ○ sırada |
| 3 | Pajero | 2006-2021 | 3.2 DI-D | ○ sırada |

### Land Rover (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 2 | Discovery Sport | 2015- | 2.0 TD4 / SD4 (Ingenium) | ○ sırada |
| 2 | Range Rover Evoque | 2011-2019 | 2.2 SD4 / 2.0 TD4 (Ingenium) / 2.0 Si4 | ○ sırada |
| 3 | Discovery 4 | 2009-2016 | 2.7 TDV6 / 3.0 SDV6 | ○ sırada |
| 3 | Freelander 2 | 2007-2014 | 2.2 TD4 | – eklenmedi: Turbo hortumu ve Haldex anlatıları tekil; Discovery Sport ve Evoque için güvenilir kaynak yok. |
| 3 | Range Rover Sport | 2005- | 3.0 TDV6 / SDV6 | ○ sırada |

### Cupra (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Born | 2022- | Elektrik | – eklenmedi: Arama sonuç vermedi. Cupra Born, Ekim 2026 VW grubu batarya geri çağırmasının kapsadığı modeller arasında (belirli üretim partileri); Türkiye kapsamı doğrulanamadı. |
| 3 | Formentor | 2020- | 1.5 eTSI (48V hafif hibrit, DSG) | ✓ 1 sorun (+2 ortak aile), 1 yıl kırılımı |

### MG (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | MG4 Electric | 2023- | Elektrik (51 / 64 kWh) | ✓ 1 sorun |
| 3 | HS | 2021- | 1.5 T (DCT) | – eklenmedi: Şanzıman gecikmesi şikâyetleri yalnızca Şikâyetvar'da; model yılı ve sürüm bilgisi doğrulanamadı. |
| 3 | ZS | 2017- | 1.5 VTi | ○ sırada |
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
| 3 | fortwo / forfour 453 | 2015-2023 | 0.9 TCe 90 (H4Bt) / 1.0 | ○ sırada |

### Porsche (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 2 | Taycan | 2020- | Elektrik (4S / Turbo) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Cayenne (958) | 2010-2017 | 3.0 diesel / 3.6 V6 | ○ sırada |
| 3 | Macan | 2014- | 2.0 turbo / 3.0 S Diesel | ○ sırada |

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

### Ssangyong (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Korando / Tivoli | 2011- | 2.0 e-XDi / 1.6 | ○ sırada |
| 3 | Rexton | 2012- | 2.0 / 2.2 e-XDi | ○ sırada |

## Plan dışı kayıtlar

İlk aşamada eklenen ve 2011 öncesi üretime ağırlık veren ya da plandaki satırlarla eşleşmeyen kayıtlar. Silinmedi; doğrulanmış veri olarak durur.

| Marka | Model | Motor |
| --- | --- | --- |
| Chevrolet | Cruze (2009-2016) | 1.6 benzin (F16D4) |
| Honda | Civic (FD6, 2006-2011) | 1.6 i-VTEC |
| Opel | Astra H (2004-2010) | 1.6 Twinport (Z16XEP / Z16XER, Easytronic) |
| Volkswagen | Passat (B6, 2005-2010) | 2.0 TDI PD 16V (BKP) |
| Volkswagen | Polo (9N / 6R, 2002-2014) | 1.2 3 silindir (BMD / BME / CGPA) |
