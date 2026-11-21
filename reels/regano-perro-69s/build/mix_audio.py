"""Mezcla voz + música con ducking suave y hueco espectral para la voz.
uso: python3 mix_audio.py <voz.mp3> <musica.wav> <salida.wav>"""
import sys, subprocess, numpy as np, wave
from scipy.signal import butter, sosfiltfilt, sosfilt
VOICE, MUSIC, OUT = sys.argv[1:4]; SR = 44100; LEN = 69.0
def load(p, ch):
    raw = subprocess.run(["ffmpeg","-v","error","-i",p,"-ar",str(SR),"-ac",str(ch),"-f","f32le","-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, ch).astype(np.float64)
v = load(VOICE, 1)[:, 0]; m = load(MUSIC, 2)
n = int(LEN*SR); v = np.pad(v, (0, max(0, n-len(v))))[:n]; m = np.pad(m, ((0, max(0, n-len(m))), (0, 0)))[:n]
# voz: limpieza de graves y compresión suave
v = sosfilt(butter(2, 75, "high", fs=SR, output="sos"), v)
def env(x, att, rel, win=0.02):
    h = int(win*SR); r = np.sqrt(np.convolve(x**2, np.ones(h)/h, "same"))
    a, b = np.exp(-1/(att*SR/h)), np.exp(-1/(rel*SR/h)); e = np.zeros_like(r[::h]); prev = 0
    for i, val in enumerate(r[::h]):
        c = a if val > prev else b; prev = c*prev + (1-c)*val; e[i] = prev
    return np.interp(np.arange(len(x)), np.arange(len(e))*h, e)
ve = env(v, 0.005, 0.15)
db = 20*np.log10(ve+1e-9); thr = np.percentile(db[db > -50], 70)
gain = np.where(db > thr, (thr-db)*(1-1/2.5), 0)      # 2.5:1 por encima del umbral
v = v*10**(gain/20)
v /= np.sqrt(np.mean(v[np.abs(v) > 1e-3]**2))*10**(18/20)   # voz activa ≈ -18 dBFS RMS
# detector de habla (suavizado: entra rápido, sale despacio para no "bombear")
speech = env(v, 0.06, 0.45, 0.02); sp_db = 20*np.log10(speech+1e-9)
duck = np.clip((sp_db + 42)/12, 0, 1)                   # 0 = pausa, 1 = hablando
# música: presente siempre. Bajo la voz −8 dB (suave) + hueco −5 dB en 1,2–4 kHz (zona de inteligibilidad)
band = sosfiltfilt(butter(2, [1200, 4000], "band", fs=SR, output="sos"), m, axis=0)
rest = m - band
g_all = 10**((-8*duck)/20); g_band = 10**((-5*duck)/20)
m2 = (rest + band*g_band[:, None])*g_all[:, None]
m2 = sosfilt(butter(1, 90, "high", fs=SR, output="sos"), m2, axis=0)
MUSIC_LEVEL_DB = -8.6      # en pausas la música sube casi al nivel de la voz; al hablar la voz queda ≈ 8 dB por encima (altavoz de móvil)
m_rms = np.sqrt(np.mean(m2[int(25*SR):int(64*SR)]**2)); m2 *= 10**((-18+MUSIC_LEVEL_DB)/20)/m_rms
mix = m2 + v[:, None]
mix /= max(1.0, np.max(np.abs(mix))/0.95)
with wave.open(OUT, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix, -1, 1)*32767).astype("<i2").tobytes())
# comprobación tipo altavoz de móvil (300 Hz–7 kHz): relación voz/música al hablar y en pausas
ph = butter(4, [300, 7000], "band", fs=SR, output="sos")
vp = sosfilt(ph, v); mp = sosfilt(ph, m2.mean(1))
on = duck > 0.9; off = (duck < 0.1) & (np.arange(n) < 65*SR)
r = lambda x, k: 10*np.log10(np.mean(x[k]**2)+1e-12)
print(f"móvil — voz {r(vp,on):.1f} dB | música bajo voz {r(mp,on):.1f} dB | música en pausas {r(mp,off):.1f} dB | V/M al hablar {r(vp,on)-r(mp,on):.1f} dB")
