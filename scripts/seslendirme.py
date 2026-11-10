"""Google Cloud Text-to-Speech ile Türkçe seslendirme (cümle cümle, önbellekli).

API anahtarı ortamın ağ vekili tarafından istek başlığına eklenir; kodda anahtar tutulmaz. Üretilen her cümle
.seslendirme/ klasöründe metnin özetiyle saklanır (git dışı), aynı metin ikinci kez faturalanmaz.
"""
import base64
import hashlib
import io
import json
import re
import urllib.request
import wave
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
ONBELLEK = KOK / ".seslendirme"
ADRES = "https://texttospeech.googleapis.com/v1/text:synthesize"
ORNEKLEME = 24000
SES = {"dil": "tr-TR", "ad": "tr-TR-Chirp3-HD-Charon", "hiz": 0.95}   # sakin erkek sesi; seçim seslendirme denemesiyle kesinleşir

BIRLER = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]


def okunur(metin):
    """Seslendirme için yazımı konuşma diline çevirir: 1.5 -> bir nokta beş, km -> kilometre, parantez ve eğik çizgi ayıklanır."""
    m = metin
    m = re.sub(r"\(([^)]*)\)", "", m)
    m = re.sub(r"(\d)\.(\d)(?!\d)", lambda x: f"{BIRLER[int(x.group(1))] or 'sıfır'} nokta {BIRLER[int(x.group(2))] or 'sıfır'}", m)
    m = re.sub(r"(\d+)\.000", r"\1 bin", m)
    m = re.sub(r"(\d+)\s*[-–]\s*(\d+)\s*km/s", r"saatte \1 ile \2 kilometre", m)
    m = re.sub(r"(\d+)\s*km/s", r"saatte \1 kilometre", m)
    m = re.sub(r"(\d[\d ]*bin|\d+)\s*[-–]\s*(\d)", r"\1 ile \2", m)
    m = re.sub(r"\bkm\b", "kilometre", m)
    m = re.sub(r"\s*/\s*", " ya da ", m)
    m = m.replace("'", "")
    return re.sub(r"\s+", " ", m).strip()


def sentezle(metin, ses=SES):
    """Metni WAV (16 bit, mono, 24 kHz) olarak döndürür; önbellekte varsa oradan okur."""
    ONBELLEK.mkdir(exist_ok=True)
    anahtar = hashlib.sha1(json.dumps([metin, ses], ensure_ascii=False).encode()).hexdigest()
    dosya = ONBELLEK / f"{anahtar}.wav"
    if not dosya.exists():
        govde = json.dumps({"input": {"text": metin}, "voice": {"languageCode": ses["dil"], "name": ses["ad"]},
                            "audioConfig": {"audioEncoding": "LINEAR16", "sampleRateHertz": ORNEKLEME, "speakingRate": ses["hiz"]}}).encode()
        istek = urllib.request.Request(ADRES, data=govde, method="POST",
                                       headers={"Content-Type": "application/json", "X-Goog-Api-Key": "vekil-tarafindan-eklenir"})
        with urllib.request.urlopen(istek, timeout=60) as y:
            dosya.write_bytes(base64.b64decode(json.loads(y.read())["audioContent"]))
    return dosya.read_bytes()


def pcm(wav_bayt):
    with wave.open(io.BytesIO(wav_bayt)) as w:
        assert w.getnchannels() == 1 and w.getsampwidth() == 2, "beklenmeyen ses biçimi"
        return w.readframes(w.getnframes()), w.getframerate()


def birlestir(parcalar, cikti, toplam_sn):
    """parcalar: [(başlangıç_sn, wav_bayt)]. Hepsini zaman çizelgesine yerleştirip tek WAV yazar."""
    tampon = bytearray(int(toplam_sn * ORNEKLEME) * 2)
    for bas, w in parcalar:
        veri, hz = pcm(w)
        assert hz == ORNEKLEME
        i = int(bas * ORNEKLEME) * 2
        tampon[i:i + len(veri)] = veri[: max(0, len(tampon) - i)]
    with wave.open(str(cikti), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(ORNEKLEME)
        w.writeframes(bytes(tampon))


def sure(wav_bayt):
    veri, hz = pcm(wav_bayt)
    return len(veri) / 2 / hz
