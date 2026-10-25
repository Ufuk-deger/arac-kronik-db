# Sahibinden listesi karşılaştırması: bizde olmayan modeller

Kaynak liste: "Sahibinden.com son 15 yılın en çok ilan adedine sahip otomobil modelleri (2011-2026)", 150 model (130 içten yanmalı/hibrit, 20 elektrikli).

Karşılaştırma `claude/fervent-goldberg-0vaev1` dalındaki `data/araclar.json` (467 kayıt) ve `data/kapsam.json` (765 plan satırı) ile model düzeyinde yapıldı. Bu dosya yalnızca bir devam listesidir; veri dosyalarına dokunulmadı.

Bu dosyayı kullanan oturum için notlar:

- Plan ve veri dosyaları `claude/fervent-goldberg-0vaev1` dalında. Bu dosya `ccr-f3fa2c90-lyi6zu` dalında.
- Bölüm 1'deki modeller `data/kapsam.json` içinde zaten `sonuc: yetersiz-kanit` ile duruyor. Yeniden aramadan önce o satırın `not` alanına bakın (hangi sorgularla arandığı yazıyor).
- Bölüm 2'deki modeller planda yok. Önce `data/kapsam.json` planına satır eklenmeli (marka, model, yillar, motor, kademe, eslesme).
- Kanıt eşiği değişmedi: her sorun için en az iki farklı site ve en az bir deneyim/resmî kaynak. Kaynak bulunamazsa sorun uydurulmaz.

## 1. Yeterli kanıt olmayanlar (planda var, kayıt açılmamış)

| Marka | Model | Gerekçe |
| --- | --- | --- |
| Audi | A4 B9 | Yağ eksiltme şikâyetleri B8'e ait, B9 için doğrudan liste çıkmadı |
| Audi | A6 C8 | Yalnızca tekil Şikâyetvar kayıtları var |
| Mercedes-Benz | E Serisi W213 | Sistematik veri yok, tekil fren, ekran ve direksiyon şikâyetleri var |
| Volvo | XC40 (T3/T4/D3/B4) | Motora göre ayrılabilen tekrar eden sorun çıkmadı |
| Volvo | XC40 Recharge / EX40 | EX30 hücre geri çağırması var, Türkiye kapsamı doğrulanamadı |
| Hyundai | i10 | Elantra ile birlikte arandı, kronik sorun çıkmadı |
| Hyundai | Kona Electric | Batarya geri çağırması var, Türkiye'de resmî satışı doğrulanamadı |
| Kia | Cerato | Su alma şikâyeti var ama km ve yıl verisi ile ikinci bağımsız kaynak yok |
| Suzuki | Swift | Çoğunlukla multimedya ve kamera şikâyeti, ikinci kaynak yok |
| Suzuki | Vitara | Kamera su alması ve multimedya donması var, tek kaynak |
| Mini | Countryman F60 | Tekil kayıtlar |
| Mini | Cooper SE | Tekil kayıtlar |
| MG | ZS (1.5 VTi) | Akü ve yazılım şikâyeti var, ikinci kaynak yok |
| MG | HS (1.5T DCT) | Şanzıman gecikmesi yalnızca Şikâyetvar'da |
| MG | ZS EV | Tekil, ikinci kaynak yok |
| Renault | Koleos | Türkçe kaynak çıkmadı |
| Renault | Megane E-Tech Electric | Şarj uyarısı şikâyetleri tekil |
| Volkswagen | Passat CC | CC'ye özgü kaynak çıkmadı |
| Volkswagen | Touareg (3.0 TDI) | Kayıtlar ağırlıkla ABD kaynaklı (NHTSA servis kayıtları) |
| Toyota | C-HR (1.2T ve 1.8 Hybrid) | Tek tek vakalar, iki bağımsız site yok |
| Toyota | RAV4 | Sistematik sorun çıkmadı |
| Mazda | CX-5 | Skyactiv için Türkiye'ye özgü kaynak çıkmadı |
| Alfa Romeo | Stelvio | Tekil elektronik ve parça bekleme şikâyetleri |
| Chery | Omoda 5 | Kaynak yetersiz (Omoda E5 için şikâyet bulunamadı) |
| Chery | Tiggo 7 Pro | Kaynak yetersiz |
| Chery | Tiggo 8 Pro | Yağ soğutucusu arızası şikâyeti var, bağımsız ikinci kaynak yok |
| BMW | iX1, iX3, i4 | Şarj sorunları tekil |

## 2. Hiç olmayanlar (ne planda ne veritabanında)

Model olarak:

- DS Automobiles DS 7 Crossback
- DS Automobiles DS 4 (2021 sonrası; veritabanındaki "DS3 / DS4" eski Citroën DS4'tür)
- Cupra Leon
- Mercedes-Benz E Coupe / Cabriolet (C207, C238)
- Alfa Romeo Tonale
- KG Mobility Torres EVX

Model var ama Sahibinden'de geçen nesil yok:

- Honda Civic FE1
- Nissan X-Trail T33
- Hyundai Elantra CN7
- Mazda 3 BM/BN
- BMW X1 U11
- BMW 4 Serisi G22/G26

Bu nesil listesi örnektir, tam değildir. Devam eden oturum Sahibinden listesindeki nesil parantezlerini (ör. "Astra J, K, L", "Golf Mk6-Mk8") veritabanındaki `model` alanlarıyla satır satır karşılaştırarak tamamlayabilir.

## Karşılaştırma notları

- Ortak aile satırlarındaki birleşik modeller (ör. "Kuga 2 / Mondeo", "Cooper S / Countryman S (R56 / R60)") bu karşılaştırmada "var" sayıldı.
- Sahibinden listesi kendi içinde karışık: Mokka-e elektrikli bölümünde, Citroën C4 ve C4 Cactus tek satırda.
