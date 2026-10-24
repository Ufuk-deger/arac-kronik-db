# Kapsam ve ilerleme

Bu dosya `scripts/kapsam_md_uret.py` ile `data/kapsam.json` (plan) ve `data/araclar.json` (veri) içeriğinden üretilir. Elle düzenlemeyin; planı `data/kapsam.json` içinde değiştirip betiği yeniden çalıştırın.

## Ölçüt

- **Zaman penceresi:** Son 10-15 yılın araçları, yani yaklaşık 2011 model yılı ve sonrası. Daha eski yıllar yalnızca ilk aşamada eklenmiş kayıtlarda kaldı (aşağıda ayrıca listelenir).
- **Marka seçimi:** Türkiye'de en çok satılan 15 marka. Yalnızca elektrikli ya da 2023 sonrası girmiş markalar (BYD, Togg, Tesla, Chery) motor grubu ve ikinci el geçmişi olmadığı için kapsam dışı bırakıldı; yerlerine sıradaki markalar alındı.
- **Sıralama:** Genelden özele gidilir. Önce her markanın en çok satılan ve en çok sorgulanan modelleri ile ana motor grupları (kademe 1), sonra yaygın ama daha az sorgulananlar (kademe 2), en son niş gruplar (kademe 3).
- **Yıl kırılımı:** Kaynaklar üretim yılına göre fark belirtiyorsa sorun `donem_kirilimi` ile yıl aralıklarına ayrılır (ör. revizyon öncesi ve sonrası).
- **Kanıt eşiği:** Her sorun için en az iki farklı site ve en az bir deneyim/resmî türünde kaynak gerekir ([README](README.md#kaynak-kuralı)). Kaynak bulunamayan gruplar plana `–` olarak işlenir; sorun uydurulmaz.

Kademeler:

- **Kademe 1:** Son 10-15 yılda en çok satılan ve ikinci elde en çok sorgulanan model ve ana motor grupları
- **Kademe 2:** Yaygın ama daha az sorgulanan model ve motor grupları
- **Kademe 3:** Niş, yeni ya da kaynağı az olan gruplar

Model ve motor seçimi 2025 satış sıralaması ve ikinci el pazarındaki yaygınlık gözetilerek editoryal olarak yapılmıştır; kademe atamaları kesin bir sıralama değil, çalışma sırasıdır.

## İlerleme

- Plan: **173** model/motor grubu
- Tamamlanan (✓): **76**
- Araştırılıp eklenmeyen (–): **16**
- Sırada (○): **81**
- Kademe 1: **72/84** işlendi (✓ ya da –)
- Veritabanı: **83** kayıt, **140** kronik sorun

| Marka | Plan | ✓ | – | ○ | Kademe 1 işlenen |
| --- | ---: | ---: | ---: | ---: | ---: |
| Renault | 14 | 7 | 1 | 6 | 6/7 |
| Volkswagen | 18 | 10 | 0 | 8 | 9/9 |
| Toyota | 11 | 3 | 4 | 4 | 5/5 |
| Fiat | 11 | 5 | 2 | 4 | 5/5 |
| Hyundai | 15 | 7 | 2 | 6 | 7/9 |
| Peugeot | 7 | 4 | 1 | 2 | 4/4 |
| Opel | 13 | 6 | 2 | 5 | 4/4 |
| Citroen | 6 | 4 | 0 | 2 | 3/3 |
| Skoda | 11 | 5 | 0 | 6 | 5/5 |
| Mercedes-Benz | 9 | 3 | 0 | 6 | 3/5 |
| BMW | 7 | 3 | 0 | 4 | 3/4 |
| Nissan | 8 | 4 | 0 | 4 | 4/4 |
| Ford | 12 | 6 | 3 | 3 | 5/7 |
| Kia | 9 | 3 | 1 | 5 | 3/4 |
| Dacia | 8 | 3 | 0 | 5 | 3/3 |
| Audi | 5 | 1 | 0 | 4 | 1/3 |
| Honda | 6 | 2 | 0 | 4 | 2/2 |
| Seat | 3 | 0 | 0 | 3 | 0/1 |

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
| 9 | BYD | 45.537 | Kapsam dışı | 2023'te Türkiye'ye girdi; elektrikli ve plug-in hibrit. İkinci elde ve kronik sorun kaynaklarında yeterli veri yok. |
| 10 | Skoda | 45.321 | Kapsamda |  |
| 11+ | Mercedes-Benz | 43.224 | Kapsamda | Rakam tek bir haber tablosundan; doğrulanamadı. |
| 11+ | Togg | 39.020 | Kapsam dışı | Yalnızca elektrikli ve 2023'te çıktı; ICE/hibrit motor grubu yok. |
| 11+ | BMW | 33.992 | Kapsamda | Rakam tek bir haber tablosundan; doğrulanamadı. |
| 11+ | Tesla | 31.509 | Kapsam dışı | Yalnızca elektrikli; motor grubu kavramı yok. |
| 11+ | Nissan | 28.705 | Kapsamda | Rakam tek bir haber tablosundan; doğrulanamadı. |
| 11+ | Chery | 28.579 | Kapsam dışı | 2023 sonrası yeni marka; ikinci el ve kronik sorun verisi yok. Rakam doğrulanamadı. |
| 11+ | Ford | — | Kapsamda | Hafif ticari dahil toplamda ilk 5 marka arasında (Ocak-Ağustos 2025'te %7,72 pay). Otomobil adedi doğrulanamadı. |
| 11+ | Kia | 25.420 | Kapsamda | Rakam tek bir haber tablosundan; doğrulanamadı. |
| 11+ | Dacia | 25.405 | Kapsamda | Tek haberde 25.405 olarak geçiyor; Sandero Stepway tek başına 23.699. |
| 11+ | Audi | 24.832 | Ek kademe | Ek kademe: ikinci el pazarındaki yaygınlığı nedeniyle sonra eklenecek. Rakam doğrulanamadı. |
| 11+ | Honda | 16.137 | Ek kademe | Ek kademe: Civic ikinci elde çok sorgulanıyor. Rakam doğrulanamadı. |
| 11+ | Seat | 9.857 | Ek kademe | Ek kademe: Leon ve Ibiza ikinci elde yaygın. Rakam doğrulanamadı. |

\* İlk 10 sıra birden fazla haberde tutarlıdır (Volkswagen ve Toyota için küçük rakam farkları notlandı). 11. sıradan sonrası rakamlar tek bir tablodan alınmış ve ikinci bir kaynakta doğrulanamamıştır; bu yüzden sıra numarası verilmedi ve liste adet sırasındadır. Ford'un otomobil adedi bulunamadı. Kapsamdaki 15 marka bu belirsizliklerden etkilenmez, ancak 11-20. sıradaki markaların kendi aralarındaki sırası kesin değildir. Resmî tablo için ODMD'nin yıllık bülteni esas alınmalıdır.

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
| 1 | Clio 4 | 2013-2019 | 1.5 dCi 75/90 (K9K) | ○ sırada |
| 1 | Clio 4 / Captur | 2013-2019 | 1.2 TCe 120 (H5Ft) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Clio 5 | 2019- | 1.0 TCe 90/100 (H4Dt) | ✓ 2 sorun |
| 1 | Megane 3 / Fluence | 2009-2016 | 1.5 dCi (K9K, EDC) | ✓ 3 sorun |
| 1 | Megane 4 | 2016- | 1.3 TCe 140 (H5Ht, EDC) | ✓ 1 sorun |
| 1 | Megane 4 | 2016- | 1.5 Blue dCi 95/115 (K9K) | ✓ 2 sorun |
| 2 | Clio 3 / Symbol | 2008-2013 | 1.5 dCi 70/85/90 (K9K) | ✓ 1 sorun |
| 2 | Clio 4 | 2013-2019 | 1.2 16V 75 (D4F) | ○ sırada |
| 2 | Kadjar | 2015-2022 | 1.5 dCi 110 (K9K) | ○ sırada |
| 2 | Kadjar | 2015-2022 | 1.3 TCe 140 (H5H) | ○ sırada |
| 2 | Megane 3 / Fluence | 2009-2016 | 1.6 16V (K4M, LPG'li dahil) | – eklenmedi: Aramalarda LPG'li K4M supap oturması anılıyor ama iki bağımsız site bulunamadı. |
| 2 | Megane 4 | 2016- | 1.6 SCe 115 (H4M) | ○ sırada |
| 2 | Symbol | 2008-2020 | 1.2 16V 75 (D4F) | ○ sırada |

### Volkswagen

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Golf 7 | 2012-2019 | 1.4 TSI 122/140 (EA211) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Golf 7 | 2012-2019 | 1.6 TDI 90/105/110 | ✓ 1 sorun |
| 1 | Passat B7 | 2010-2014 | 1.6 TDI (CAYC) | ✓ 1 sorun |
| 1 | Passat B8 | 2015-2023 | 1.6 TDI | ✓ 2 sorun |
| 1 | Polo 6R / 6C | 2009-2017 | 1.2 TSI 90/105/110 | ✓ 2 sorun, 2 yıl kırılımı |
| 1 | Polo AW | 2018- | 1.0 TSI / 1.0 MPI | ✓ 1 sorun |
| 1 | T-Roc | 2018- | 1.0 TSI / 1.5 TSI | ✓ 1 sorun |
| 1 | Tiguan 5N | 2008-2016 | 1.4 TSI 122/150/160 (EA111) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tiguan AD1 | 2016- | 1.4 TSI / 1.5 TSI | ✓ 1 sorun |
| 2 | Caddy | 2010-2020 | 1.6 TDI / 2.0 TDI | ○ sırada |
| 2 | Golf 7 | 2012-2019 | 1.2 TSI 85/105 | ○ sırada |
| 2 | Golf 8 | 2020- | 1.0 TSI / 1.5 TSI | ○ sırada |
| 2 | Jetta | 2011-2018 | 1.2 TSI / 1.4 TSI / 1.6 TDI | ✓ 2 sorun, 1 yıl kırılımı |
| 2 | Passat B7 | 2010-2014 | 2.0 TDI / 1.4 TSI | ○ sırada |
| 2 | Passat B8 | 2015-2023 | 2.0 TDI / 1.5 TSI / 1.4 TSI | ○ sırada |
| 2 | Polo 6R / 6C | 2009-2017 | 1.4 TDI / 1.6 TDI | ○ sırada |
| 2 | Tiguan 5N | 2008-2016 | 2.0 TDI | ○ sırada |
| 2 | Tiguan AD1 | 2016- | 2.0 TDI | ○ sırada |

### Toyota

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C-HR | 2016- | 1.2 Turbo (8NR-FTS) | – eklenmedi: Yağ yakma ve şanzıman anıları motor tipi belirtilmeden, tek tek vaka; iki bağımsız site bulunamadı. |
| 1 | C-HR | 2016- | 1.8 Hybrid (2ZR-FXE) | – eklenmedi: Hibrit sistem uyarısı dışında tekrar eden mekanik sorun bulunamadı. |
| 1 | Corolla E150 FL / E170 | 2009-2018 | 1.33 Dual VVT-i 99 | ✓ 1 sorun |
| 1 | Corolla E210 | 2019- | 1.5 Dynamic Force (M15A-FKS) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Corolla E210 | 2019- | 1.8 Hybrid (2ZR-FXE) | – eklenmedi: Şikâyetler ses yalıtımı, fren diski paslanması ve 12V akü gibi mekanik olmayan konularda; tekrar eden mekanik sorun bulunamadı. |
| 2 | Auris | 2013-2018 | 1.33 / 1.6 / 1.4 D-4D | ○ sırada |
| 2 | Corolla E170 | 2013-2018 | 1.4 D-4D | ○ sırada |
| 2 | Corolla E170 | 2013-2018 | 1.6 Valvematic (Multidrive S) | – eklenmedi: Şikâyet sitelerinde 1.6 Valvematic ve Multidrive S için tekrar eden bir sorun kümesi bulunamadı. |
| 2 | Yaris | 2011-2019 | 1.33 / 1.5 Hybrid | ○ sırada |
| 3 | Corolla E150 | 2007-2013 | 1.4 D-4D (1ND-TV) | ✓ 2 sorun |
| 3 | RAV4 / Hilux | 2013- | 2.0 / 2.5 Hybrid / 2.4 D-4D | ○ sırada |

### Fiat

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Doblo | 2010-2022 | 1.3 / 1.6 Multijet (90/105/120) | ✓ 3 sorun |
| 1 | Egea | 2015- | 1.4 Fire 95 | ✓ 1 sorun |
| 1 | Egea | 2015- | 1.3 Multijet II 95 | ✓ 2 sorun |
| 1 | Egea | 2015- | 1.6 Multijet II 120 | ✓ 3 sorun |
| 1 | Linea | 2007-2015 | 1.3 Multijet (Dualogic) | ✓ 4 sorun |
| 2 | 500 | 2008- | 1.2 Fire / 0.9 TwinAir | ○ sırada |
| 2 | Egea | 2016- | 1.6 E-Torq 110 | – eklenmedi: Aramalarda öne çıkan kronik sorun bulunamadı. |
| 2 | Linea | 2007-2015 | 1.4 Fire / 1.4 T-Jet | – eklenmedi: Dağınık şikâyetler var, tekrar eden bir sorun için iki bağımsız site bulunamadı. |
| 2 | Punto Evo / Grande Punto | 2009-2018 | 1.3 Multijet 75/95 | ○ sırada |
| 2 | Punto Evo / Grande Punto | 2009-2018 | 1.4 Fire 77 | ○ sırada |
| 3 | Fiorino / Qubo | 2008-2020 | 1.3 Multijet | ○ sırada |

### Hyundai

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Accent Blue | 2011-2019 | 1.6 CRDi (D4FB) | ✓ 1 sorun |
| 1 | Accent Blue | 2011-2019 | 1.4 MPI / 1.6 GDI | ○ sırada |
| 1 | Bayon | 2021- | 1.0 T-GDI 100/120 (7DCT) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Bayon | 2021- | 1.4 MPI 100 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tucson (TL) | 2015-2020 | 1.6 T-GDI (7DCT) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tucson (TL) | 2015-2020 | 1.6 CRDi (7DCT) | ○ sırada |
| 1 | i20 | 2020- | 1.0 T-GDI 100/120 (7DCT) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | i20 | 2020- | 1.4 MPI 100 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | i30 | 2012-2020 | 1.6 CRDi | – eklenmedi: Turbo, DPF ve DCT anıları nesilleri karıştırıyor ve dağınık; model/motor bazında tekrar eden sorun için iki bağımsız site bulunamadı. |
| 2 | Elantra | 2011-2020 | 1.6 MPI / 1.6 CRDi | – eklenmedi: Tek bir 7DCT kalkış titremesi şikâyeti dışında tekrar eden sorun bulunamadı. |
| 2 | Tucson (NX4) | 2021- | 1.6 T-GDI / 1.6 CRDi | ✓ 2 sorun |
| 2 | i20 (PB) | 2009-2014 | 1.4 MPI / 1.4 CRDi | ○ sırada |
| 2 | i30 | 2012-2020 | 1.4 / 1.6 MPI, 1.0 / 1.4 T-GDI | ○ sırada |
| 2 | ix35 | 2010-2015 | 1.6 GDI / 1.7 CRDi | ○ sırada |
| 3 | Kona | 2018- | 1.0 T-GDI / 1.6 T-GDI / 1.6 CRDi | ○ sırada |

### Peugeot

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | 208 / 2008 / 308 / 3008 | 2014-2021 | 1.2 PureTech (EB2) | ✓ 2 sorun |
| 1 | 208 / 2008 / 308 / 3008 | 2012-2021 | 1.6 BlueHDi / e-HDi (DV6) | – eklenmedi: Enjektör, EGR ve turbo anıları dağınık ve tek tek vaka; 301 kaydındaki DV6 sorunları aynı motor ailesi için geçerlidir. |
| 1 | 208 / 2008 / 308 / 3008 / 5008 | 2019- | 1.5 BlueHDi 100/130 (DV5) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | 301 | 2012- | 1.6 HDi / BlueHDi (DV6) | ✓ 3 sorun |
| 2 | 308 / 3008 | 2007-2014 | 1.6 THP (EP6) | ✓ 3 sorun, 1 yıl kırılımı |
| 3 | 301 | 2012- | 1.2 VTi / PureTech | ○ sırada |
| 3 | 508 | 2011-2018 | 1.6 THP / 1.6 e-HDi / 2.0 HDi | ○ sırada |

### Opel

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Astra J | 2010-2015 | 1.4 Turbo (A14NET) | ✓ 1 sorun |
| 1 | Astra K | 2015-2021 | 1.4 Turbo 125/150 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Corsa D / E | 2006-2019 | 1.3 CDTI 75/95 | ✓ 1 sorun |
| 1 | Mokka | 2012-2019 | 1.4 Turbo (A14NET) | – eklenmedi: Mokka'ya özgü, A14NET'i açıkça belirten tekrar eden bir şikâyet bulunamadı; aynı motor için Astra J ve Astra K kayıtlarına bakın. |
| 2 | Astra J | 2013-2015 | 1.6 CDTI 110/136 | ✓ 1 sorun |
| 2 | Astra K | 2015-2021 | 1.6 CDTI 110/136 | ○ sırada |
| 2 | Corsa D / E | 2006-2019 | 1.2 / 1.4 benzinli (A12XER, A14XER) | – eklenmedi: Aramalarda A12XER/A14XER için kronik sorun bulunamadı; sonuçlar PureTech'e ait. |
| 2 | Crossland / Corsa F | 2017- | 1.2 PureTech 83/100/110/130 | ✓ 1 sorun |
| 2 | Insignia A | 2014-2017 | 1.6 CDTI 136 | ✓ 2 sorun |
| 2 | Insignia A | 2008-2017 | 2.0 CDTI / 1.6 Turbo / 1.4 Turbo | ○ sırada |
| 2 | Mokka | 2012-2019 | 1.6 CDTI | ○ sırada |
| 3 | Astra J | 2010-2015 | 1.7 / 2.0 CDTI | ○ sırada |
| 3 | Crossland / Grandland | 2017- | 1.5 BlueHDi | ○ sırada |

### Citroen

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C-Elysee | 2012-2020 | 1.6 HDi / BlueHDi (DV6) | ✓ 3 sorun |
| 1 | C3 | 2016-2022 | 1.2 PureTech 82/110 | ✓ 1 sorun |
| 1 | C3 / C4 / C5 Aircross | 2019- | 1.5 BlueHDi 100/130 (DV5) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | C-Elysee | 2012-2020 | 1.2 PureTech / 1.6 VTi | ✓ 1 sorun |
| 2 | C3 | 2009-2016 | 1.4 HDi / 1.6 HDi | ○ sırada |
| 2 | C4 / C4 Cactus | 2011-2020 | 1.6 e-HDi / BlueHDi, 1.2 PureTech | ○ sırada |

### Skoda

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Octavia A5 | 2008-2013 | 1.2 TSI 105 (EA111) | ✓ 2 sorun |
| 1 | Octavia A5 / A7 | 2010-2020 | 1.6 TDI 105/110 (DSG DQ200) | ✓ 1 sorun |
| 1 | Octavia A7 | 2013-2020 | 1.4 TSI (EA211, DSG DQ200) | ✓ 3 sorun, 1 yıl kırılımı |
| 1 | Rapid | 2012-2019 | 1.2 TSI 90/105 | ✓ 1 sorun |
| 1 | Rapid | 2012-2019 | 1.6 TDI / 1.6 MPI | ✓ 1 sorun |
| 2 | Fabia | 2014-2021 | 1.0 MPI / 1.2 TSI / 1.4 TDI | ○ sırada |
| 2 | Kamiq / Scala | 2019- | 1.0 TSI 95/115 | ○ sırada |
| 2 | Karoq / Kodiaq | 2017- | 1.5 TSI / 2.0 TDI | ○ sırada |
| 2 | Octavia A7 / A8 | 2018- | 1.0 TSI / 1.5 TSI | ○ sırada |
| 2 | Superb | 2015-2023 | 1.4 TSI / 1.6 TDI / 2.0 TDI | ○ sırada |
| 3 | Yeti | 2009-2017 | 1.2 TSI / 1.4 TSI / 1.6 TDI | ○ sırada |

### Mercedes-Benz

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C Serisi W204 | 2007-2014 | C220 / C250 CDI 2.1 (OM651) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | C Serisi W205 | 2014-2021 | C180 / C200 benzinli (M274) | ○ sırada |
| 1 | C Serisi W205 | 2014-2021 | C180d / C200d / C220d (OM626 / OM651) | ○ sırada |
| 1 | E Serisi W212 | 2009-2016 | E200 / E250 CGI 1.8 turbo (M271 EVO) | ✓ 1 sorun |
| 1 | E Serisi W212 | 2009-2016 | E250 CDI 2.1 (OM651) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | A Serisi W176 | 2012-2018 | A180 CDI / A200 CDI / A180 1.6 | ○ sırada |
| 2 | C Serisi W204 | 2007-2014 | C180 / C200 CGI 1.8 (M271 EVO) | ○ sırada |
| 2 | E Serisi W213 | 2016- | E180 / E200 / E220d | ○ sırada |
| 3 | CLA / GLA | 2013-2019 | 1.6 / 1.5 d (OM607) | ○ sırada |

### BMW

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | 1 Serisi F20 | 2011-2019 | 116i / 118i (N13 / B38) | ✓ 4 sorun |
| 1 | 3 Serisi F30 | 2012-2015 | 320d 2.0 (N47) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | 3 Serisi F30 | 2012-2015 | 320i / 328i 2.0 (N20) | ✓ 3 sorun |
| 1 | 3 Serisi F30 | 2015-2019 | 320d (B47) / 320i (B48) | ○ sırada |
| 2 | 1 Serisi F20 | 2011-2019 | 116d / 118d (N47 / B47) | ○ sırada |
| 2 | 5 Serisi F10 | 2010-2017 | 520d (N47 / B47) / 520i (N20) | ○ sırada |
| 3 | X1 / X3 | 2010-2018 | 1.8d / 2.0d (N47 / B47) | ○ sırada |

### Nissan

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Juke | 2010-2019 | 1.6 (CVT Xtronic) | ✓ 1 sorun |
| 1 | Juke | 2014-2019 | 1.2 DIG-T 115 (HRA2DDT) | ✓ 1 sorun |
| 1 | Qashqai J11 | 2014-2020 | 1.5 dCi 110 (K9K) / 1.6 dCi 130 (R9M) | ✓ 1 sorun |
| 1 | Qashqai J11 | 2014-2021 | 1.2 DIG-T (HRA2DDT, Xtronic) | ✓ 3 sorun |
| 2 | Juke | 2010-2019 | 1.5 dCi 110 (K9K) | ○ sırada |
| 2 | Micra | 2010-2019 | 1.2 / 0.9 IG-T | ○ sırada |
| 2 | Qashqai J10 | 2007-2013 | 1.5 dCi / 1.6 | ○ sırada |
| 3 | Note / X-Trail | 2013- | 1.2 / 1.5 dCi / 1.6 dCi | ○ sırada |

### Ford

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Fiesta | 2008-2017 | 1.4 / 1.6 TDCi | ○ sırada |
| 1 | Fiesta / Focus | 2012-2023 | 1.0 EcoBoost | ✓ 2 sorun, 2 yıl kırılımı |
| 1 | Fiesta Mk7 | 2011-2017 | 1.6 Ti-VCT 105 (Powershift DPS6) | ✓ 1 sorun |
| 1 | Focus 2 / 3 | 2008-2018 | 1.6 TDCi (DV6) | ✓ 3 sorun |
| 1 | Focus 3 | 2011-2018 | 1.6 Ti-VCT (Powershift DPS6) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Focus 3 | 2011-2018 | 1.5 TDCi 95/120 | ○ sırada |
| 1 | Focus 4 / Kuga 3 | 2019- | 1.5 EcoBlue 120 (DV5) | ✓ 2 sorun |
| 2 | Courier / Tourneo Courier | 2014- | 1.5 TDCi / 1.0 EcoBoost | – eklenmedi: Şikâyetler fren sesi, gıcırtı ve genel motor arıza lambası gibi dağınık konularda; ortak bir arıza için iki bağımsız site bulunamadı. |
| 2 | Fiesta | 2008-2023 | 1.25 / 1.4 Duratec | – eklenmedi: Kullanıcılar 1.25 ve 1.4 benzinlileri sorunsuz olarak anıyor; kronik sorun bulunamadı. |
| 2 | Focus 3 | 2011-2018 | 1.5 EcoBoost 150/182 | ○ sırada |
| 2 | Kuga 2 | 2013-2019 | 1.5 EcoBoost / 2.0 TDCi | ✓ 1 sorun |
| 2 | Puma | 2019- | 1.0 EcoBoost mHEV | – eklenmedi: Forum görüşleri çelişkili (bazıları en sorunsuz 3 silindirli diyor); tekrar eden bir motor sorunu için kanıt yok. |

### Kia

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Ceed | 2012-2018 | 1.6 CRDi | ○ sırada |
| 1 | Rio | 2011-2017 | 1.4 CRDi 90 | ✓ 1 sorun |
| 1 | Sportage SL / QL | 2010-2021 | 1.6 CRDi / 1.7 CRDi | ✓ 1 sorun |
| 1 | Sportage SL / QL | 2010-2021 | 1.6 GDI / 1.6 T-GDI | ✓ 1 sorun |
| 2 | Ceed | 2012-2021 | 1.4 / 1.6 MPI | ○ sırada |
| 2 | Picanto | 2011-2023 | 1.0 / 1.2 MPI | ○ sırada |
| 2 | Rio | 2011-2017 | 1.4 MPI 100 | – eklenmedi: Forumlarda sorunsuz olarak anılıyor; kronik sorun bulunamadı. |
| 2 | Stonic | 2017- | 1.0 T-GDI / 1.4 MPI / 1.6 CRDi | ○ sırada |
| 3 | Niro / Cerato / Sorento | 2011- | Hybrid / 1.6 / 2.2 CRDi | ○ sırada |

### Dacia

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Duster | 2010-2017 | 1.5 dCi (K9K) | ✓ 2 sorun |
| 1 | Duster | 2021-2024 | 1.0 TCe 100 ECO-G (H4Dt) | ✓ 1 sorun |
| 1 | Sandero / Sandero Stepway | 2021- | 1.0 TCe 90/100 (H4Dt) | ✓ 1 sorun |
| 2 | Duster | 2018-2021 | 1.5 dCi / 1.3 TCe / 1.6 SCe | ○ sırada |
| 2 | Sandero / Logan | 2013-2020 | 0.9 TCe 90 (H4Bt) | ○ sırada |
| 2 | Sandero / Logan | 2013-2020 | 1.5 dCi 75/90 (K9K) | ○ sırada |
| 3 | Jogger | 2022- | 1.0 TCe 110 ECO-G | ○ sırada |
| 3 | Lodgy / Dokker | 2012-2021 | 1.5 dCi (K9K) | ○ sırada |

### Audi (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | A3 8V | 2012-2020 | 1.0 / 1.2 / 1.4 TFSI, 1.6 TDI | ○ sırada |
| 1 | A4 B8 | 2008-2015 | 1.8 TFSI / 2.0 TFSI (EA888 Gen2) | ✓ 4 sorun, 2 yıl kırılımı |
| 1 | A4 B8 | 2008-2015 | 2.0 TDI (CAGA / CJCA) | ○ sırada |
| 2 | A4 B9 | 2016- | 2.0 TFSI / 2.0 TDI | ○ sırada |
| 3 | A6 C7 / Q3 / Q5 | 2011- | 2.0 TDI / 3.0 TDI / 2.0 TFSI | ○ sırada |

### Honda (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Civic FC5 | 2016-2021 | 1.6 i-VTEC 125 (CVT) | ✓ 1 sorun |
| 1 | Civic FC5 | 2016-2021 | 1.5 VTEC Turbo (L15B7) | ✓ 2 sorun |
| 2 | CR-V | 2012-2018 | 1.6 i-DTEC / 2.0 i-VTEC | ○ sırada |
| 2 | City | 2009- | 1.5 i-VTEC / 1.5 Hybrid | ○ sırada |
| 2 | Civic FB7 | 2012-2015 | 1.6 i-VTEC / 1.8 i-VTEC | ○ sırada |
| 3 | Jazz / HR-V | 2011- | 1.3 / 1.5 i-VTEC | ○ sırada |

### Seat (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Leon 5F / 1P | 2005-2020 | 1.2 TSI / 1.4 TSI / 1.6 TDI | ○ sırada |
| 2 | Ibiza 6J / 6P | 2008-2021 | 1.2 TSI / 1.0 TSI / 1.6 TDI | ○ sırada |
| 3 | Ateca / Arona | 2016- | 1.0 TSI / 1.5 TSI | ○ sırada |

## Plan dışı kayıtlar

İlk aşamada eklenen ve 2011 öncesi üretime ağırlık veren ya da plandaki satırlarla eşleşmeyen kayıtlar. Silinmedi; doğrulanmış veri olarak durur.

| Marka | Model | Motor |
| --- | --- | --- |
| Chevrolet | Cruze (2009-2016) | 1.6 benzin (F16D4) |
| Honda | Civic (FD6, 2006-2011) | 1.6 i-VTEC |
| Mercedes-Benz | C Serisi (W203 / W204, 2002-2010) | C180 / C200 Kompressor 1.8 (M271) |
| Opel | Astra H (2004-2010) | 1.6 Twinport (Z16XEP / Z16XER, Easytronic) |
| Volkswagen | Passat (B6, 2005-2010) | 2.0 TDI PD 16V (BKP) |
| Volkswagen | Polo (9N / 6R, 2002-2014) | 1.2 3 silindir (BMD / BME / CGPA) |
