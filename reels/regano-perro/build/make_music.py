"""Pista original de guitarra de nailon (síntesis Karplus-Strong) con arpegios espaciados.
uso: python3 make_music.py <salida.wav>"""
import sys, numpy as np, numba
from scipy.signal import fftconvolve, butter, sosfilt
SR = 44100; LEN = 99.6; OUT = sys.argv[1]
rng = np.random.default_rng(7)

@numba.njit(cache=True)
def ks(f, dur, t60, bright, exc):
    n = int(dur*SR); y = np.zeros(n); N = SR/f
    Ni = int(N - 0.5); frac = N - 0.5 - Ni           # retardo entero + fracción (all-pass)
    a = (1-frac)/(1+frac); g = 10**(-3/(f*t60))
    buf = np.zeros(Ni+2); ap_x = 0.0; ap_y = 0.0; lp = 0.0; idx = 0
    for i in range(n):
        x = exc[i] if i < exc.shape[0] else 0.0
        d = buf[idx]
        lp = bright*d + (1-bright)*lp                # pérdida: pasa-bajos en el lazo (nailon cálido)
        ap = a*lp + ap_x - a*ap_y; ap_x = lp; ap_y = ap   # afinación fina
        out = x + g*ap
        buf[idx] = out; idx += 1
        if idx >= Ni: idx = 0
        y[i] = out
    return y

def note(midi, vel, dur):
    f = 440*2**((midi-69)/12)
    N = int(SR/f); L = N
    e = rng.uniform(-1, 1, L)
    # dedo (no púa): ruido suavizado y posición de pulsación
    for _ in range(3): e = np.convolve(e, [0.25, 0.5, 0.25], "same")
    p = max(1, int(0.17*L)); e[p:] -= e[:-p]*0.9
    e *= vel/np.max(np.abs(e))
    t60 = np.interp(midi, [40, 80], [3.4, 2.0])
    bright = np.interp(vel, [0.2, 1.0], [0.42, 0.62])
    y = ks(f, dur, t60, bright, e)
    att = np.minimum(1, np.arange(len(y))/(0.004*SR)); y *= att
    y *= vel*0.12/np.sqrt(np.mean(y[:int(0.3*SR)]**2)+1e-12)   # mismo volumen percibido en todas las cuerdas
    if midi < 48: y *= 0.8
    return y

# acordes (voicings de guitarra, MIDI)
CH = {
 "D":  [50, 57, 64, 66, 69, 73],   # Dmaj9
 "Bm": [47, 54, 62, 64, 66, 69],   # Bm11
 "G":  [43, 50, 57, 59, 66, 69],   # Gmaj9
 "A":  [45, 52, 57, 62, 64, 69],   # Asus4
 "A2": [45, 52, 57, 61, 64, 69],   # A
 "Em": [40, 52, 55, 59, 64, 67],   # Em7
}
BEAT = 60/66; BAR = 4*BEAT; T0 = 0.35
ev = []   # (t, midi, vel, dur, pan)
def bar(t, ch, pattern, vel=0.55):
    c = CH[ch]
    for (b, i, v) in pattern:
        ev.append((t + b*BEAT + rng.normal(0, 0.008), c[i], vel*v*rng.uniform(.9, 1.05), 5.0, (i-2.5)/6))
# patrones: (pulso, cuerda, intensidad)
SPARSE = [(0, 0, 1.0), (1.5, 2, .7), (2.5, 4, .6)]
SPARSE2 = [(0, 0, 1.0), (1, 2, .65), (2, 4, .6), (3, 3, .5)]
WARM = [(0, 0, 1.0), (.5, 2, .55), (1, 3, .6), (1.5, 4, .55), (2, 5, .6), (2.5, 4, .5), (3, 3, .55), (3.5, 2, .45)]
SILENCE = (18.9, 23.0)       # aire tras «Y tú la apartas…»
prog1 = ["D", "Bm", "G", "A"]
prog2 = ["Bm", "G", "D", "A"]
pad = []                     # (t0, t1, acorde, nivel)
k = 0
while True:
    t = T0 + k*BAR
    if t > 91.5: break
    if t < 18.0:   bar(t, prog1[k % 4], SPARSE, 0.50)                 # inicio: pocas notas
    elif t < 22.0: pass
    elif t < 39.0: bar(t, prog2[k % 4], SPARSE2, 0.52)                # tensión contenida
    else:                                                             # desde «Pero aquí no acaba la cosa»: gana calidez
        ch = prog1[k % 4]; warm = 0.56 if t < 75 else 0.62
        bar(t, ch, WARM, warm)
        if k % 2 == 0: ev.append((t + 2*BEAT, CH[ch][5]+12 if ch != "D" else 78, warm*0.55, 5.0, 0.2))  # melodía aguda
        pad.append((t, t+BAR, ch, 0.05 if t < 75 else 0.075))
    k += 1
ev = [e for e in ev if not (SILENCE[0] < e[0] < SILENCE[1])]
# una sola nota que respira en el silencio (sobre «Te mira.»)
ev.append((22.0, 66, 0.30, 5.0, 0.1))
# cierre: G -> Asus -> A -> D, la última nota sobre el paseo final
t = T0 + k*BAR
for i, (ch, pat) in enumerate([("G", SPARSE), ("A", [(0, 0, 1.), (1.5, 3, .6)]), ("A2", [(0, 4, .5)])]):
    bar(t + i*BAR*0.75, ch, pat, 0.48)
tD = 96.1
for j, m in enumerate([50, 57, 62, 66, 69]):          # acorde final arpegiado lento
    ev.append((tD + j*0.11, m, 0.5 - j*0.04, 4.0, (j-2)/5))
ev.append((97.6, 74, 0.38, 2.5, 0.25))                  # última nota (D5)

L = np.zeros((int(LEN*SR)+SR, 2))
cache = {}
for (t, m, v, d, pan) in ev:
    if t < 0 or t >= LEN: continue
    y = note(m, v, min(d, LEN-t+0.5))
    i0 = int(t*SR); y = y[:len(L)-i0]
    L[i0:i0+len(y), 0] += y*np.sqrt(0.5-pan*0.5); L[i0:i0+len(y), 1] += y*np.sqrt(0.5+pan*0.5)
# cuerpo de la guitarra: resonancias suaves
tt = np.arange(int(0.25*SR))/SR
body = np.zeros_like(tt); body[0] = 1
for f, a, dcy in [(117, .006, 40), (228, .008, 45), (405, .005, 50)]: body += a*np.sin(2*np.pi*f*tt)*np.exp(-dcy*tt)
for c in range(2): L[:, c] = fftconvolve(L[:, c], body)[:len(L)]
# pad cálido y discreto
P = np.zeros(len(L)); tt = np.arange(len(L))/SR
for (a, b, ch, lvl) in pad:
    i0, i1 = int(a*SR), int(min(b+1.2, LEN)*SR); seg = tt[i0:i1]-a
    env = np.minimum(1, seg/1.4)*np.minimum(1, np.maximum(0, (b+1.2-a-seg))/1.2)
    for m in CH[ch][:4]:
        f = 440*2**((m+12-69)/12) if m < 48 else 440*2**((m-69)/12)
        P[i0:i1] += lvl*env*(np.sin(2*np.pi*f*seg) + .3*np.sin(2*np.pi*f*1.003*seg) + .15*np.sin(4*np.pi*f*seg))/4
P = sosfilt(butter(2, 1400, "low", fs=SR, output="sos"), P)
L[:, 0] += P; L[:, 1] += P
# reverb de sala (IR sintética estéreo)
n = int(2.4*SR); tt = np.arange(n)/SR
for c in range(2):
    ir = rng.normal(0, 1, n)*np.exp(-6.9*tt/2.1); ir = sosfilt(butter(2, 4500, "low", fs=SR, output="sos"), ir)
    ir[:int(0.022*SR)] = 0; ir /= np.sqrt(np.sum(ir**2))
    L[:, c] = 0.78*L[:, c] + 0.30*fftconvolve(L[:, c], ir)[:len(L)]
L = L[:int(LEN*SR)]
fade = np.ones(len(L)); fl = int(1.6*SR); fade[-fl:] = np.linspace(1, 0, fl)**1.5
L *= fade[:, None]
L /= np.max(np.abs(L))*1.12
import wave
with wave.open(OUT, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((L*32767).astype("<i2").tobytes())
print("notas", len(ev), "dur", len(L)/SR)
