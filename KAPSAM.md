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

- Plan: **230** model/motor grubu
- Tamamlanan (✓): **130**
- Araştırılıp eklenmeyen (–): **100**
- Sırada (○): **0**
- Kademe 1: **85/85** işlendi (✓ ya da –)
- Veritabanı: **134** kayıt, **203** kronik sorun

| Marka | Plan | ✓ | – | ○ | Kademe 1 işlenen |
| --- | ---: | ---: | ---: | ---: | ---: |
| Renault | 18 | 12 | 6 | 0 | 7/7 |
| Volkswagen | 21 | 15 | 6 | 0 | 9/9 |
| Toyota | 13 | 4 | 9 | 0 | 5/5 |
| Fiat | 12 | 9 | 3 | 0 | 5/5 |
| Hyundai | 17 | 10 | 7 | 0 | 9/9 |
| Peugeot | 9 | 6 | 3 | 0 | 4/4 |
| Opel | 16 | 9 | 7 | 0 | 4/4 |
| Citroen | 7 | 5 | 2 | 0 | 3/3 |
| Skoda | 11 | 7 | 4 | 0 | 5/5 |
| Mercedes-Benz | 14 | 8 | 6 | 0 | 5/5 |
| BMW | 10 | 5 | 5 | 0 | 4/4 |
| Nissan | 11 | 7 | 4 | 0 | 4/4 |
| Ford | 15 | 7 | 8 | 0 | 7/7 |
| Kia | 12 | 6 | 6 | 0 | 4/4 |
| Dacia | 11 | 8 | 3 | 0 | 3/3 |
| Audi | 9 | 5 | 4 | 0 | 4/4 |
| Honda | 7 | 3 | 4 | 0 | 2/2 |
| Seat | 4 | 2 | 2 | 0 | 1/1 |
| Chevrolet | 1 | 0 | 1 | 0 | 0/0 |
| Volvo | 1 | 1 | 0 | 0 | 0/0 |
| Subaru | 1 | 1 | 0 | 0 | 0/0 |
| Mini | 1 | 0 | 1 | 0 | 0/0 |
| Jeep | 1 | 0 | 1 | 0 | 0/0 |
| Alfa Romeo | 1 | 0 | 1 | 0 | 0/0 |
| Mazda | 1 | 0 | 1 | 0 | 0/0 |
| Suzuki | 1 | 0 | 1 | 0 | 0/0 |
| Mitsubishi | 1 | 0 | 1 | 0 | 0/0 |
| Land Rover | 1 | 0 | 1 | 0 | 0/0 |
| Cupra | 1 | 0 | 1 | 0 | 0/0 |
| MG | 1 | 0 | 1 | 0 | 0/0 |
| Lexus | 1 | 0 | 1 | 0 | 0/0 |

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
| 11+ | Chevrolet | — | Ek kademe | Ek kademe: Cruze kaydı ilk aşamadan; Captiva / Aveo Faz 4'te arandı, kanıt tek rehber sitesinde kaldığı için eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Volvo | — | Ek kademe | Ek kademe: Faz 4'te S60 / V40 1.6 D Powershift eklendi. Satış adedi doğrulanamadı. |
| 11+ | Subaru | — | Ek kademe | Ek kademe: Faz 4'te XV 2.0 yağ tüketimi eklendi. Satış adedi doğrulanamadı. |
| 11+ | Mini | — | Ek kademe | Ek kademe: Faz 4'te arandı; ikinci bağımsız kaynak bulunamadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Jeep | — | Ek kademe | Ek kademe: Faz 4'te arandı; ikinci bağımsız kaynak bulunamadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Alfa Romeo | — | Ek kademe | Ek kademe: Faz 4'te arandı; motorlara özgü kaynaklı bulgu çıkmadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Mazda | — | Ek kademe | Ek kademe: Faz 4'te arandı; Türkiye'ye özgü kronik sorun kaynağı çıkmadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Suzuki | — | Ek kademe | Ek kademe: Faz 4'te arandı; bulgular tek rehber sitesi ve elektronik şikâyetlerle sınırlı kaldığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Mitsubishi | — | Ek kademe | Ek kademe: Faz 4'te arandı; ikinci bağımsız kaynak bulunamadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Land Rover | — | Ek kademe | Ek kademe: Faz 4'te arandı; ikinci bağımsız kaynak bulunamadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Cupra | — | Ek kademe | Ek kademe: Faz 4'te arandı; şikâyetler tekil kaldığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | MG | — | Ek kademe | Ek kademe: Faz 4'te arandı; HS şanzıman şikâyetleri yalnızca Şikâyetvar'da, model yılı ve sürüm bilgisi doğrulanamadığı için kayıt eklenmedi. Satış adedi doğrulanamadı. |
| 11+ | Lexus | — | Ek kademe | Ek kademe: Faz 4'te arandı; sonuç çıkmadı. Satış adedi doğrulanamadı. |

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
| 1 | Clio 4 | 2013-2019 | 1.5 dCi 75/90 (K9K) | ✓ 1 sorun |
| 1 | Clio 4 / Captur | 2013-2019 | 1.2 TCe 120 (H5Ft) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Clio 5 | 2019- | 1.0 TCe 90/100 (H4Dt) | ✓ 2 sorun |
| 1 | Megane 3 / Fluence | 2009-2016 | 1.5 dCi (K9K, EDC) | ✓ 3 sorun |
| 1 | Megane 4 | 2016- | 1.3 TCe 140 (H5Ht, EDC) | ✓ 1 sorun |
| 1 | Megane 4 | 2016- | 1.5 Blue dCi 95/115 (K9K) | ✓ 2 sorun |
| 2 | Clio 3 / Symbol | 2008-2013 | 1.5 dCi 70/85/90 (K9K) | ✓ 1 sorun |
| 2 | Clio 4 | 2013-2019 | 1.2 16V 75 (D4F) | – eklenmedi: Şikâyetvar'da tek tek soğukta marş uzaması ve klima şikâyetleri var; D4F motoruna özgü tekrar eden bir sorun için iki bağımsız site bulunamadı. |
| 2 | Kadjar | 2015-2022 | 1.5 dCi 110 (K9K) | ✓ 1 sorun |
| 2 | Kadjar | 2015-2022 | 1.3 TCe 140 (H5H) | ✓ 2 sorun |
| 2 | Megane 3 / Fluence | 2009-2016 | 1.6 16V (K4M, LPG'li dahil) | – eklenmedi: Aramalarda LPG'li K4M supap oturması anılıyor ama iki bağımsız site bulunamadı. |
| 2 | Megane 4 | 2016- | 1.6 SCe 115 (H4M) | – eklenmedi: Aramalarda H4M motoruna özgü arıza çıkmadı; şikâyetler motor tipi belirtmeyen genel Megane 4 konularına (yağ sızıntısı, soğutma, enjeksiyon uyarısı) ve LPG'li araçlara ait. |
| 2 | Symbol | 2008-2020 | 1.2 16V 75 (D4F) | – eklenmedi: Aramalarda D4F motoruna özgü tekrar eden sorun çıkmadı; şikâyetler soğukta marş ve klima gibi tekil konularda. |
| 3 | Captur | 2013-2019 | 1.5 dCi (K9K, EDC) | ✓ 1 sorun |
| 3 | Kangoo | 2008-2021 | 1.5 dCi (K9K) | – eklenmedi: Kangoo'ya özgü ayrı kaynak yok; K9K enjektör ve EGR anlatıları Clio, Megane ve Duster kayıtlarında ele alındı. |
| 3 | Master / Trafic | 2010- | 2.3 dCi (M9T) | – eklenmedi: M9T için kol yatağı, turbo ve enjektör kanıtı yok; EGR / DPF anlatıları tek rehber sitesinden. |
| 3 | Talisman | 2016-2022 | 1.6 dCi / 1.5 dCi (EDC) | ✓ 1 sorun |

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
| 2 | Caddy | 2010-2015 | 1.6 TDI (EA189) | ✓ 1 sorun |
| 2 | Caddy | 2015-2020 | 2.0 TDI | – eklenmedi: 2.0 TDI için Caddy'ye özgü kaynaklar Şikâyetvar (DPF, AdBlue) ile sınırlı; ikinci bağımsız kaynak bulunamadı. |
| 2 | Golf 7 | 2012-2019 | 1.2 TSI 85/105 | ✓ 1 sorun |
| 2 | Golf 8 | 2020- | 1.0 TSI / 1.5 TSI | ✓ 2 sorun, 1 yıl kırılımı |
| 2 | Jetta | 2011-2018 | 1.2 TSI / 1.4 TSI / 1.6 TDI | ✓ 2 sorun, 1 yıl kırılımı |
| 2 | Passat B7 | 2010-2014 | 2.0 TDI / 1.4 TSI | – eklenmedi: Aramalarda 2.0 TDI'ya özgü tekrar eden sorun çıkmadı; forum yorumlarının çoğu eski PD motorlara (B6) ve DSG'ye ait, enjektör iddiaları tekil. |
| 2 | Passat B8 | 2015-2023 | 2.0 TDI / 1.5 TSI / 1.4 TSI | – eklenmedi: Aramalarda B8 2.0 TDI için EGR, DPF ya da AdBlue kaynaklı tekrar eden Türkçe kaynak çıkmadı; en çok DSG şikâyeti var (B8 1.6 TDI kaydında). |
| 2 | Polo 6R / 6C | 2009-2017 | 1.4 TDI / 1.6 TDI | ✓ 1 sorun |
| 2 | Tiguan 5N | 2008-2016 | 2.0 TDI | – eklenmedi: 5N 2.0 TDI'ya özgü turbo, EGR, DPF ya da zincir sorunu için kaynak çıkmadı; sonuçlar 1.4 TSI ve genel Passat 2.0 TDI yorumlarına ait. |
| 2 | Tiguan AD1 | 2016- | 2.0 TDI | ✓ 1 sorun |
| 3 | Passat B7 | 2010-2014 | 2.0 TDI (CFFB / CBAB) | – eklenmedi: B7'ye özgü zincir ya da yüksek basınç pompası kaynağı çıkmadı; enjektör anlatıları PD motorlu B6 kaydında. |
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
| 3 | Corolla E150 | 2007-2013 | 1.4 D-4D (1ND-TV) | ✓ 2 sorun |
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
| 2 | Egea | 2016- | 1.6 E-Torq 110 | – eklenmedi: Aramalarda öne çıkan kronik sorun bulunamadı. |
| 2 | Linea | 2007-2015 | 1.4 Fire / 1.4 T-Jet | – eklenmedi: Dağınık şikâyetler var, tekrar eden bir sorun için iki bağımsız site bulunamadı. |
| 2 | Punto Evo / Grande Punto | 2009-2018 | 1.3 Multijet 75/95 | ✓ 2 sorun |
| 2 | Punto Evo / Grande Punto | 2009-2018 | 1.4 Fire 77 | ✓ 2 sorun |
| 3 | Fiorino / Qubo | 2008-2020 | 1.3 Multijet | ✓ 3 sorun |
| 3 | Linea / Punto | 2007-2015 | 1.4 T-Jet | – eklenmedi: T-Jet'e özgü kaynak çıkmadı; Punto şikâyetleri ağırlıkla direksiyon (EPS) üzerine ve ayrı kayıtta. |

### Hyundai

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Accent Blue | 2011-2019 | 1.6 CRDi (D4FB) | ✓ 1 sorun |
| 1 | Accent Blue | 2011-2019 | 1.4 MPI / 1.6 GDI | – eklenmedi: 1.4 MPI ve 1.6 GDI için tekrar eden sorun bulunamadı (yalnızca tek tek külbütör kapağı yağ kaçağı ve sübap iddiaları). |
| 1 | Bayon | 2021- | 1.0 T-GDI 100/120 (7DCT) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Bayon | 2021- | 1.4 MPI 100 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tucson (TL) | 2015-2020 | 1.6 T-GDI (7DCT) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Tucson (TL) | 2015-2020 | 1.6 CRDi (7DCT) | ✓ 1 sorun |
| 1 | i20 | 2020- | 1.0 T-GDI 100/120 (7DCT) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | i20 | 2020- | 1.4 MPI 100 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | i30 | 2012-2020 | 1.6 CRDi | – eklenmedi: Turbo, DPF ve DCT anıları nesilleri karıştırıyor ve dağınık; model/motor bazında tekrar eden sorun için iki bağımsız site bulunamadı. |
| 2 | Elantra | 2011-2020 | 1.6 MPI / 1.6 CRDi | – eklenmedi: Tek bir 7DCT kalkış titremesi şikâyeti dışında tekrar eden sorun bulunamadı. |
| 2 | Tucson (NX4) | 2021- | 1.6 T-GDI / 1.6 CRDi | ✓ 2 sorun |
| 2 | i20 (PB) | 2009-2014 | 1.4 MPI / 1.4 CRDi | ✓ 1 sorun |
| 2 | i30 | 2012-2020 | 1.4 / 1.6 MPI, 1.0 / 1.4 T-GDI | – eklenmedi: Benzinli motorlar (MPI, T-GDI) için i30'a özgü kronik sorun çıkmadı; aramalar 1.6 CRDi (DPF) ve DCT şikâyetlerine yöneldi ve i30'a özgü olmayan kaynaklardan geldi. |
| 2 | i30 (FD) | 2008-2012 | 1.4 / 1.6 MPI, 1.6 GDI (EPS) | ✓ 1 sorun |
| 2 | ix35 | 2010-2015 | 1.6 GDI / 1.7 CRDi | – eklenmedi: Şikâyetler iç trim, 4x4 şanzıman dişlisi ve LPG'li soğuk çalıştırma gibi tekil konularda; 1.7 CRDi Türkiye'de neredeyse hiç satılmamış. |
| 3 | Kona | 2018- | 1.0 T-GDI / 1.6 T-GDI / 1.6 CRDi | – eklenmedi: 1.6 CRDi DCT kalkış titremesi yalnızca Şikâyetvar kayıtlarında; ikinci bağımsız kaynak bulunamadı. Benzer 7DCT kavrama titremesi Tucson, Bayon, i20 (BC3) ve Sportage kayıtlarında ele alındı. |
| 3 | ix35 / Santa Fe | 2010-2018 | 1.7 / 2.0 / 2.2 CRDi | – eklenmedi: ix35 1.7 / 2.0 CRDi ve Santa Fe 2.2 CRDi için model özelinde kaynak çıkmadı; bulunanlar ix35 1.6 GDI için tek rehber sitesi. |

### Peugeot

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | 208 / 2008 / 308 / 3008 | 2014-2021 | 1.2 PureTech (EB2) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | 208 / 2008 / 308 / 3008 | 2012-2021 | 1.6 BlueHDi / e-HDi (DV6) | – eklenmedi: Enjektör, EGR ve turbo anıları dağınık ve tek tek vaka; 301 kaydındaki DV6 sorunları aynı motor ailesi için geçerlidir. |
| 1 | 208 / 2008 / 308 / 3008 / 5008 | 2019- | 1.5 BlueHDi 100/130 (DV5) | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | 301 | 2012- | 1.6 HDi / BlueHDi (DV6) | ✓ 3 sorun |
| 2 | 308 / 3008 | 2007-2014 | 1.6 THP (EP6) | ✓ 3 sorun, 1 yıl kırılımı |
| 3 | 207 / 206 | 2006-2014 | 1.6 VTi (EP6) | – eklenmedi: EP6 zincir uzaması iddiası tek bir rehber sitesine (Araclo) dayanıyor; forum ve şikâyet kaynaklarında doğrulanmadı. |
| 3 | 301 | 2012- | 1.2 VTi / PureTech | ✓ 2 sorun |
| 3 | 508 | 2011-2018 | 1.6 e-HDi 115 (MCP / Auto6R robotize) | ✓ 1 sorun |
| 3 | 508 | 2011-2018 | 1.6 THP / 2.0 HDi | – eklenmedi: 1.6 THP için tek bir kullanıcı 2011-2012 yüksek basınç pompası sorununu anıyor (308/3008 1.6 THP kaydına bakın); 2.0 HDi için kaynak bulunamadı. |

### Opel

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Astra J | 2010-2015 | 1.4 Turbo (A14NET) | ✓ 1 sorun |
| 1 | Astra K | 2015-2021 | 1.4 Turbo 125/150 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | Corsa D / E | 2006-2019 | 1.3 CDTI 75/95 | ✓ 2 sorun |
| 1 | Mokka | 2012-2019 | 1.4 Turbo (A14NET) | – eklenmedi: Mokka'ya özgü, A14NET'i açıkça belirten tekrar eden bir şikâyet bulunamadı; aynı motor için Astra J ve Astra K kayıtlarına bakın. |
| 2 | Astra J | 2013-2015 | 1.6 CDTI 110/136 | ✓ 1 sorun |
| 2 | Astra K | 2015-2021 | 1.6 CDTI 110/136 | ✓ 1 sorun |
| 2 | Corsa D / E | 2006-2019 | 1.2 / 1.4 benzinli (A12XER, A14XER) | – eklenmedi: Aramalarda A12XER/A14XER için kronik sorun bulunamadı; sonuçlar PureTech'e ait. |
| 2 | Crossland / Corsa F | 2017- | 1.2 PureTech 83/100/110/130 | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Insignia A | 2014-2017 | 1.6 CDTI 136 | ✓ 2 sorun |
| 2 | Insignia A | 2008-2017 | 2.0 CDTI / 1.6 Turbo / 1.4 Turbo | – eklenmedi: Turbo hortumu sorunu 1.6 CDTI kaydında var; 1.6 Turbo'da zincir ve yağ soğutucusu için motor sürümü belirsiz tekil yorumlar, 2.0 CDTI için tekil kayıt çıktı. |
| 2 | Mokka | 2012-2019 | 1.6 CDTI | – eklenmedi: Zincir sesi ve otomatik şanzıman şikâyetleri yalnızca Şikâyetvar'da; ikinci bağımsız site bulunamadı. |
| 3 | Astra J | 2010-2015 | 1.7 / 2.0 CDTI | – eklenmedi: 1.7 ve 2.0 CDTI'ya özgü tekrar eden sorun çıkmadı; sonuçlar 1.6 ve 1.3 CDTI'ya ait. |
| 3 | Corsa D | 2006-2014 | 1.2 / 1.3 CDTI (Easytronic) | ✓ 1 sorun |
| 3 | Crossland | 2017- | 1.5 BlueHDi | – eklenmedi: Crossland şikâyetleri motor beyni ve şanzıman tarafında tekil; 1.5 BlueHDi zincir sorunu Grandland X kaydında ele alındı. |
| 3 | Grandland X / Grandland | 2017- | 1.5 BlueHDi | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Mokka / Mokka X | 2012-2020 | 1.4 Turbo (A14NET) / 1.6 CDTI | – eklenmedi: Mokka 1.6 CDTI zincir sesi ve otomatik şanzıman (P0741) şikâyetleri yalnızca Şikâyetvar'da; A14NET 1.4 Turbo için Mokka'ya özgü kaynak çıkmadı. |

### Citroen

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C-Elysee | 2012-2020 | 1.6 HDi / BlueHDi (DV6) | ✓ 3 sorun |
| 1 | C3 | 2016-2022 | 1.2 PureTech 82/110 | ✓ 1 sorun, 1 yıl kırılımı |
| 1 | C3 / C4 / C5 Aircross | 2019- | 1.5 BlueHDi 100/130 (DV5) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | C-Elysee | 2012-2020 | 1.2 PureTech / 1.6 VTi | ✓ 1 sorun |
| 2 | C3 | 2009-2016 | 1.4 HDi / 1.6 HDi | – eklenmedi: Enjektör ve turbo anıları tekil ve eski forum yazıları; uzun dönem bir kullanıcı turbo arızasını 230.000 km'de, enjektör revizyonunu 310.000 km'de bildiriyor; kronik sorun için yeterli kanıt yok. |
| 2 | C4 / C4 Cactus | 2011-2020 | 1.6 e-HDi / BlueHDi, 1.2 PureTech | ✓ 1 sorun |
| 3 | Berlingo / Partner | 2008-2018 | 1.6 HDi (DV6) | – eklenmedi: Turbo yağ besleme borusu tıkanıklığı tek bir forum yanıtına dayanıyor; Şikâyetvar'daki Berlingo kayıtları ağırlıkla 1.5 BlueHDi zinciri (ayrı kayıtta). |

### Skoda

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Octavia A5 | 2008-2013 | 1.2 TSI 105 (EA111) | ✓ 2 sorun |
| 1 | Octavia A5 / A7 | 2010-2020 | 1.6 TDI 105/110 (DSG DQ200) | ✓ 1 sorun |
| 1 | Octavia A7 | 2013-2020 | 1.4 TSI (EA211, DSG DQ200) | ✓ 3 sorun, 1 yıl kırılımı |
| 1 | Rapid | 2012-2019 | 1.2 TSI 90/105 | ✓ 1 sorun |
| 1 | Rapid | 2012-2019 | 1.6 TDI / 1.6 MPI | ✓ 1 sorun |
| 2 | Fabia | 2014-2021 | 1.0 MPI / 1.2 TSI / 1.4 TDI | – eklenmedi: Fabia için motor bazında tekrar eden sorun çıkmadı (1.4 TDI kavrama/volan, 1.2 krank keçesi ve 1.0 direksiyon uyarısı gibi tekil iddialar). |
| 2 | Kamiq / Scala | 2019- | 1.0 TSI 95/115 | ✓ 1 sorun |
| 2 | Karoq / Kodiaq | 2017- | 1.5 TSI / 2.0 TDI | – eklenmedi: Şikâyetler Şikâyetvar'daki tekil kayıtlarla sınırlı (DSG acil işletim / mekatronik, yağ eksiltme); bağımsız ikinci kaynak yok. Aynı motor ailesi Tiguan 1.5 TSI ve DQ381 kayıtlarında ele alındı. |
| 2 | Octavia A7 / A8 | 2018- | 1.0 TSI / 1.5 TSI | ✓ 2 sorun |
| 2 | Superb | 2015-2023 | 1.4 TSI / 1.6 TDI / 2.0 TDI | – eklenmedi: 1.4 TSI, 1.6 TDI ve 2.0 TDI için tekil şikâyetler çıktı (arıza lambası, start-stop); 1.6 TDI DSG kavrama sorunu Octavia ve Rapid kayıtlarında. |
| 3 | Yeti | 2009-2017 | 1.2 TSI / 1.4 TSI / 1.6 TDI | – eklenmedi: 1.2 TSI zincir iddiaları eski ve tekil (ayrıntısı Octavia A5 1.2 TSI kaydında); DSG görüşleri çelişkili. |

### Mercedes-Benz

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | C Serisi W204 | 2007-2014 | C220 / C250 CDI 2.1 (OM651) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | C Serisi W205 | 2014-2021 | C180 / C200 benzinli (M274) | – eklenmedi: Kaynaklar M274'ü zincir konusunda M271'e göre daha sorunsuz buluyor; belirgin kronik sorun yok (7G-Tronic için dağınık şikâyetler var). |
| 1 | C Serisi W205 | 2014-2021 | C180d / C200d 1.6 (R9M kaynaklı dizel) | ✓ 1 sorun |
| 1 | E Serisi W212 | 2009-2016 | E200 / E250 CGI 1.8 turbo (M271 EVO) | ✓ 1 sorun |
| 1 | E Serisi W212 | 2009-2016 | E250 CDI 2.1 (OM651) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | A Serisi W176 | 2012-2018 | A180 CDI (dizel) | ✓ 1 sorun |
| 2 | A Serisi W176 | 2012-2018 | A200 CDI / A180 1.6 benzinli (enjektör, 7G-DCT) | – eklenmedi: Enjektör ve 7G-DCT iddiaları için güçlü kanıt bulunamadı; tekrarlayan şikâyet Pre-Safe / açı sensörü (CLA ile birlikte ele alındı). |
| 2 | C Serisi W203 / W204 | 2002-2010 | C180 / C200 Kompressor 1.8 (M271) | ✓ 2 sorun |
| 2 | C Serisi W204 | 2009-2014 | C180 / C200 / C250 CGI 1.8 turbo (M271 EVO) | ✓ 1 sorun |
| 2 | C Serisi W205 | 2014-2021 | C220d 2.0 (OM651 / OM654) | – eklenmedi: C220d (OM651 / OM654) için W205'e özgü kaynak bulunamadı; bulunan şikâyetler C200d (R9M) NOx / AdBlue / turbo yağ kaçağı üzerine ve ayrı kayıtta. |
| 2 | E Serisi W213 | 2016- | E180 / E200 / E220d | – eklenmedi: W213 için sistematik veri yok; Şikâyetvar'da tekil SBC fren, ekran ve direksiyon şikâyetleri var ve bir kısmı W212 / W214'e ait. |
| 3 | CLA | 2013-2019 | 180 CDI (dizel) | ✓ 1 sorun |
| 3 | GLA | 2013-2019 | 1.5 d / 1.6 / 2.0 (OM607 / M270 / M274) | – eklenmedi: GLA'ya özgü ayrı kaynak bulunamadı; DonanımHaber'deki Pre-Safe başlığı GLA'yı da anıyor, kapsam A Serisi / CLA kaydında. |
| 3 | Vito / Sprinter | 2010- | 2.2 CDI (OM651) | – eklenmedi: OM651 anlatıları C ve E Serisi kayıtlarında; Vito ve Sprinter'a özgü ayrı kaynak yok. |

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
| 3 | 3 Serisi E90 / 5 Serisi E60 | 2005-2013 | 316i / 318i / 320i (N46 / N52), 520i | – eklenmedi: N46 / N52'ye özgü ayrıntılı kaynak çıkmadı; soğutma sistemi ve yağ kaçağı anlatıları tekil. N47 zincir sorunu ayrı kayıtlarda. |
| 3 | X1 / X3 | 2010-2018 | 1.8d / 2.0d (N47 / B47) | – eklenmedi: X1 / X3 için modele özgü kaynak çıkmadı; N47 zincir sorunu 320d, 116d ve 520d kayıtlarında ele alındı. |

### Nissan

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Juke | 2010-2019 | 1.6 (CVT Xtronic) | ✓ 1 sorun |
| 1 | Juke | 2014-2019 | 1.2 DIG-T 115 (HRA2DDT) | ✓ 1 sorun |
| 1 | Qashqai J11 | 2014-2020 | 1.5 dCi 110 (K9K) / 1.6 dCi 130 (R9M) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Qashqai J11 | 2014-2021 | 1.2 DIG-T (HRA2DDT, Xtronic) | ✓ 3 sorun |
| 2 | Juke | 2010-2019 | 1.5 dCi 110 (K9K) | – eklenmedi: Juke 1.5 dCi için kaynak ağırlıkla tek bir rehber (Araclo); turbo yağ borusu ve DPF anlatıları ikinci bağımsız kaynakla desteklenmedi. K9K turbo hortumu sorunu Qashqai J11 kaydında. |
| 2 | Micra | 2010-2017 | 1.2 (CVT otomatik) | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | Micra | 2013-2019 | 0.9 IG-T | – eklenmedi: 0.9 IG-T motoruna özgü kronik sorun sonuçlarda yer almadı; şikâyetler 1.2 CVT'de toplanıyor. |
| 2 | Qashqai J10 | 2007-2013 | 1.5 dCi / 1.6 | – eklenmedi: J10 dönemine (2007-2013) özgü kaynak bulunamadı; Qashqai 1.5 dCi turbo hortumu şikâyetleri 2012 model ve sonrasında yoğunlaşıyor, J11 kaydında ele alındı. |
| 2 | Qashqai J11 | 2014-2020 | 1.6 dCi 130 (R9M, Xtronic CVT) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Note | 2013- | 1.2 / 1.5 dCi | – eklenmedi: Note 1.2 / 1.5 dCi için ilgili şikâyet bulunamadı (aramada yalnızca X-Trail 1.6 dCi öne çıktı). |
| 3 | X-Trail T32 | 2014-2021 | 1.6 dCi (R9M, Xtronic CVT) | ✓ 1 sorun |

### Ford

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Fiesta | 2008-2017 | 1.4 / 1.6 TDCi | – eklenmedi: Enjektör ve turbo anıları genel TDCi başlıklarıyla karışık; Fiesta'ya özgü tekrar eden sorun bulunamadı. |
| 1 | Fiesta / Focus | 2012-2023 | 1.0 EcoBoost | ✓ 2 sorun, 2 yıl kırılımı |
| 1 | Fiesta Mk7 | 2011-2017 | 1.6 Ti-VCT 105 (Powershift DPS6) | ✓ 1 sorun |
| 1 | Focus 2 / 3 | 2008-2018 | 1.6 TDCi (DV6) | ✓ 3 sorun |
| 1 | Focus 3 | 2011-2018 | 1.6 Ti-VCT (Powershift DPS6) | ✓ 2 sorun, 1 yıl kırılımı |
| 1 | Focus 3 | 2011-2018 | 1.5 TDCi 95/120 | – eklenmedi: Enjektör ve DPF şikâyetleri dağınık, DPF şikâyetleri ağırlıkla 2019 sonrası EcoBlue'ya ait; 2015-2018 1.5 TDCi için ortak sorun yok. |
| 1 | Focus 4 / Kuga 3 | 2019- | 1.5 EcoBlue 120 (DV5) | ✓ 2 sorun |
| 2 | Courier / Tourneo Courier | 2014- | 1.5 TDCi / 1.0 EcoBoost | – eklenmedi: Şikâyetler fren sesi, gıcırtı ve genel motor arıza lambası gibi dağınık konularda; ortak bir arıza için iki bağımsız site bulunamadı. |
| 2 | Fiesta | 2008-2023 | 1.25 / 1.4 Duratec | – eklenmedi: Kullanıcılar 1.25 ve 1.4 benzinlileri sorunsuz olarak anıyor; kronik sorun bulunamadı. |
| 2 | Focus 3 | 2011-2018 | 1.5 EcoBoost 150/182 | – eklenmedi: Focus için sonuçlar ağırlıkla 1.0 EcoBoost; 1.5 EcoBoost silindir kapağı sorunu Kuga 2 / Mondeo kaydında ele alındı, Focus'a özgü kaynak yok. |
| 2 | Kuga 2 | 2013-2019 | 1.5 EcoBoost / 2.0 TDCi | ✓ 1 sorun |
| 2 | Puma | 2019- | 1.0 EcoBoost mHEV | – eklenmedi: Forum görüşleri çelişkili (bazıları en sorunsuz 3 silindirli diyor); tekrar eden bir motor sorunu için kanıt yok. |
| 3 | EcoSport | 2013-2022 | 1.0 EcoBoost | ✓ 1 sorun |
| 3 | Mondeo / Transit Connect / Courier | 2007-2019 | 2.0 / 1.6 TDCi, 1.5 TDCi | – eklenmedi: Mondeo için tekil direksiyon, enjektör ve DPF anlatıları var; Transit Connect ve Courier 1.5 TDCi için sonuç çıkmadı. |
| 3 | Transit Custom | 2012- | 2.0 EcoBlue | – eklenmedi: Yağ tüketimi ve turbo şikâyetleri yalnızca Şikâyetvar'da; ikinci bağımsız kaynak bulunamadı. |

### Kia

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Ceed | 2012-2018 | 1.6 CRDi | ✓ 1 sorun |
| 1 | Rio | 2011-2017 | 1.4 CRDi 90 | ✓ 1 sorun |
| 1 | Sportage SL / QL | 2010-2021 | 1.6 CRDi / 1.7 CRDi | ✓ 1 sorun |
| 1 | Sportage SL / QL | 2010-2021 | 1.6 GDI / 1.6 T-GDI | ✓ 1 sorun |
| 2 | Ceed | 2012-2021 | 1.4 / 1.6 MPI | – eklenmedi: 1.4 ve 1.6 MPI benzinlilerde motora özgü kronik sorun çıkmadı; torpido ve konsol kabarması motor tipinden bağımsız. |
| 2 | Picanto | 2017- | 1.0 / 1.2 MPI | ✓ 1 sorun |
| 2 | Rio | 2011-2017 | 1.4 MPI 100 | – eklenmedi: Forumlarda sorunsuz olarak anılıyor; kronik sorun bulunamadı. |
| 2 | Stonic | 2017- | 1.4 MPI 100 (6 ileri otomatik) | ✓ 1 sorun, 1 yıl kırılımı |
| 3 | Cerato | 2013-2018 | 1.6 (arka stop ve bagajdan su alma) | – eklenmedi: Su alma şikâyetleri Şikâyetvar'da çok, ancak kilometre ve model yılı verisi yok ve ikinci bağımsız kaynak (Ekşi'de tek yorum) sınırlı. |
| 3 | Niro / Cerato / Sorento | 2011- | Hybrid / 1.6 / 2.2 CRDi | – eklenmedi: Cerato ve Niro için sonuç çıkmadı; Sorento 2.2 CRDi için yalnızca tekil şikâyetler var. |
| 3 | Sorento / Venga | 2010-2018 | 2.2 CRDi / 1.4 CRDi | – eklenmedi: Sorento 2.2 CRDi ve Venga 1.4 CRDi için kaynak çıkmadı. |
| 3 | Stonic | 2017- | 1.0 T-GDI / 1.6 CRDi | – eklenmedi: 1.0 T-GDI için tekil titreme ve arıza lambası şikâyetleri; 1.6 CRDi için sonuç çıkmadı. |

### Dacia

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Duster | 2010-2017 | 1.5 dCi (K9K) | ✓ 2 sorun |
| 1 | Duster | 2021-2024 | 1.0 TCe 100 ECO-G (H4Dt) | ✓ 1 sorun |
| 1 | Sandero / Sandero Stepway | 2021- | 1.0 TCe 90/100 (H4Dt) | ✓ 1 sorun |
| 2 | Duster | 2018-2021 | 1.5 dCi 110 (K9K) | ✓ 1 sorun |
| 2 | Duster | 2019-2024 | 1.3 TCe 130/150 (EDC) | ✓ 1 sorun |
| 2 | Sandero / Logan | 2013-2020 | 0.9 TCe 90 (H4Bt) | ✓ 1 sorun |
| 2 | Sandero / Logan | 2013-2020 | 1.5 dCi 75/90 (K9K) | ✓ 1 sorun |
| 3 | Duster | 2018-2021 | 1.6 SCe 115 | – eklenmedi: Kaynaklarda bu motor için öne çıkan bir sorun bulunamadı. |
| 3 | Jogger | 2022- | 1.0 TCe 110 (manuel) | ✓ 1 sorun |
| 3 | Jogger | 2022- | 1.0 TCe 100 ECO-G (LPG) | – eklenmedi: LPG / ECO-G şikâyetleri tekil ve Jogger'a özgü değil (Dacia Eco-G genelinde); ikinci bağımsız kaynak bulunamadı. |
| 3 | Lodgy / Dokker | 2012-2021 | 1.5 dCi (K9K) | – eklenmedi: Lodgy / Dokker 1.5 dCi için turbo ya da enjektör örüntüsü çıkmadı; şikâyetler teyp ekranı ve elektrikte, enjektör anlatıları diğer Renault dizellerinden. |

### Audi (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | A3 8P FL / 8V | 2009-2020 | 1.4 TFSI (S tronic DQ200) | ✓ 1 sorun |
| 1 | A3 8V | 2012-2020 | 1.6 TDI 105/110 | ✓ 2 sorun |
| 1 | A4 B8 | 2008-2015 | 1.8 TFSI / 2.0 TFSI (EA888 Gen2) | ✓ 4 sorun, 2 yıl kırılımı |
| 1 | A4 B8 | 2008-2015 | 2.0 TDI 143/150/177 (Multitronic) | ✓ 1 sorun |
| 2 | A3 8V | 2012-2020 | 1.0 TFSI / 1.2 TFSI | – eklenmedi: 1.2 TFSI için sonuç çıkmadı; 1.0 TFSI için yalnızca tekil anekdotlar (start-stop sonrası kalkış, far). S tronic şikâyetleri 1.4 TFSI ve 1.6 TDI kayıtlarında ele alındı. |
| 2 | A4 B9 | 2016- | 2.0 TFSI / 2.0 TDI | – eklenmedi: B9 için doğrudan kronik sorun listesi çıkmadı; yağ eksiltme şikâyetleri çoğunlukla B8 dönemine ait (kayıtlı), B9'a özgü olanlar tekil (tahrik uyarısı, stop lambası çatlağı). |
| 3 | A6 C7 | 2011-2018 | 2.0 TDI / 3.0 TDI / 2.0 TFSI | – eklenmedi: A6 C7'ye özgü kaynak bulunamadı; bulunan A6 2.0 TDI başlıkları C6 dönemine (2009-2011) ait. |
| 3 | Q3 | 2011-2018 | 2.0 TDI / 2.0 TFSI | – eklenmedi: Q3'e özgü kaynak bulunamadı; 2.0 TFSI yağ tüketimi Q5 ve A4 kayıtlarında ele alındı. |
| 3 | Q5 8R | 2008-2017 | 2.0 TFSI (EA888) | ✓ 1 sorun, 1 yıl kırılımı |

### Honda (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Civic FC5 | 2016-2021 | 1.6 i-VTEC 125 (CVT) | ✓ 1 sorun |
| 1 | Civic FC5 | 2016-2021 | 1.5 VTEC Turbo (L15B7) | ✓ 2 sorun, 1 yıl kırılımı |
| 2 | CR-V | 2012-2018 | 1.6 i-DTEC | ✓ 1 sorun, 1 yıl kırılımı |
| 2 | CR-V | 2012-2018 | 2.0 i-VTEC | – eklenmedi: 2.0 i-VTEC için yağ eksiltme ve SRS şikâyetleri tekil kullanıcı anlatımları; ikinci bağımsız kaynak bulunamadı. |
| 2 | City | 2009- | 1.5 i-VTEC / 1.5 Hybrid | – eklenmedi: City 1.5 için yakıt tüketimi ve vites geçişi şikâyetleri yalnızca Şikâyetvar'da (2021 model); ikinci bağımsız kaynak yok. |
| 2 | Civic FB7 | 2012-2015 | 1.6 i-VTEC / 1.8 i-VTEC | – eklenmedi: FB7 şikâyetleri ağırlıkla boya atması ve kozmetik; motora özgü sorunlar tekil (130 bin km'de motor yanması, 1.8 yağ sızıntısı için eski bir forum yazısı). |
| 3 | Jazz / HR-V | 2011- | 1.3 / 1.5 i-VTEC | – eklenmedi: 1.3 / 1.5 i-VTEC CVT için kanıtlı kronik sorun çıkmadı; bulunanlar eski nesil Jazz CVT, eski kasa HR-V yorumu ve hibrit akü şikâyeti. |

### Seat (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 1 | Leon 5F / 1P | 2005-2020 | 1.2 TSI / 1.4 TSI / 1.6 TDI | ✓ 1 sorun |
| 2 | Ibiza 6J / 6P | 2008-2017 | 1.2 TSI (DSG DQ200) | ✓ 1 sorun |
| 2 | Ibiza 6J / 6P | 2008-2017 | 1.0 TSI / 1.6 TDI | – eklenmedi: Ibiza 1.6 TDI için yalnızca tekil bir direksiyon (EPS) şikâyeti çıktı; 1.0 TSI için kaynak bulunamadı. Zincir iddiası Ibiza'ya özgü değil. |
| 3 | Ateca / Arona | 2016- | 1.0 TSI / 1.5 TSI | – eklenmedi: Arona 1.0 TSI DSG ve Ateca 1.5 TSI için yalnızca Şikâyetvar'daki tekil kayıtlar (DSG vuruntusu, yağ uyarısı, yağ kaçağı); yaygınlığı gösteren bağımsız kaynak yok. |

### Chevrolet (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Captiva / Aveo / Lacetti | 2007-2016 | 2.0 VCDi, 1.4 / 1.2 | – eklenmedi: Captiva 2.0 D ve Aveo 1.4 zincir iddiaları tek rehber sitesine dayanıyor; Lacetti için sonuç çıkmadı. |

### Volvo (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | S60 / V40 | 2011-2018 | 1.6 D DRIVe (Powershift) | ✓ 1 sorun |

### Subaru (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | XV | 2012-2017 | 2.0 benzinli boxer | ✓ 1 sorun, 1 yıl kırılımı |

### Mini (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Cooper (R56 / F56) | 2007-2020 | 1.6 (N14) / 1.5 üç silindir | – eklenmedi: Zincir ve devirdaim / termostat anlatıları tek tek forum yorumları; N14'e özgü ikinci kaynak yok. |

### Jeep (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Renegade / Compass | 2015- | 1.6 MultiJet (DDCT) / 1.4 MultiAir | – eklenmedi: Renegade DDCT'ye özgü kaynak çıkmadı (sonuçlar Egea üzerinden geldi); Compass şanzıman şikâyetlerinde motor ve şanzıman kombinasyonu belirsiz. |

### Alfa Romeo (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | Giulietta | 2010-2020 | 1.4 MultiAir / 1.6 JTDM | – eklenmedi: Şikâyetler gövde ve elektronikte (yolcu airbag kapağı şişmesi, klima); motorlara özgü kaynaklı bulgu yok. |

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
| 3 | Formentor | 2020- | 1.5 eTSI (DSG) | – eklenmedi: Şikâyetler tekil (DSG, alternatör, multimedya); bağımsız ikinci kaynak yok. |

### MG (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | HS | 2021- | 1.5 T (DCT) | – eklenmedi: Şanzıman gecikmesi şikâyetleri yalnızca Şikâyetvar'da; model yılı ve sürüm bilgisi doğrulanamadı. |

### Lexus (ek kademe)

| Kademe | Model | Yıllar | Motor grubu | Durum |
| :---: | --- | --- | --- | --- |
| 3 | IS / CT 200h | 2011- | 2.5 / 1.8 hibrit | – eklenmedi: Aramada sonuç çıkmadı. |

## Plan dışı kayıtlar

İlk aşamada eklenen ve 2011 öncesi üretime ağırlık veren ya da plandaki satırlarla eşleşmeyen kayıtlar. Silinmedi; doğrulanmış veri olarak durur.

| Marka | Model | Motor |
| --- | --- | --- |
| Chevrolet | Cruze (2009-2016) | 1.6 benzin (F16D4) |
| Honda | Civic (FD6, 2006-2011) | 1.6 i-VTEC |
| Opel | Astra H (2004-2010) | 1.6 Twinport (Z16XEP / Z16XER, Easytronic) |
| Volkswagen | Passat (B6, 2005-2010) | 2.0 TDI PD 16V (BKP) |
| Volkswagen | Polo (9N / 6R, 2002-2014) | 1.2 3 silindir (BMD / BME / CGPA) |
