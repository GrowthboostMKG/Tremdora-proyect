"""Pista original para la versión 1:09: piano de fieltro tipo nana (3/4, Fa mayor) + cuerdas suaves + celesta puntual.
Distinta de la guitarra de nailon del Reel anterior. uso: python3 make_music.py <salida.wav>"""
import sys, numpy as np, wave
from scipy.signal import fftconvolve, butter, sosfilt
SR = 44100; LEN = 69.0; OUT = sys.argv[1]
rng = np.random.default_rng(11)
mf = lambda m: 440*2**((m-69)/12)

def piano(m, vel, dur):
    f0 = mf(m); n = int(dur*SR); t = np.arange(n)/SR; y = np.zeros(n); B = 0.00035
    for k in range(1, 16):
        fk = k*f0*np.sqrt(1 + B*k*k)
        if fk > 7000: break
        amp = (1/k**1.25) * np.exp(-k*(1.15-vel)*0.35)          # fieltro: menos brillo cuanto más suave
        d1 = 0.9 + 0.55*k + f0/400; d2 = 0.25 + 0.08*k           # caída en dos fases
        env = 0.65*np.exp(-d1*t) + 0.35*np.exp(-d2*t*(1+f0/600))
        y += amp*env*np.sin(2*np.pi*fk*t + rng.uniform(0, 6.28))
    att = np.minimum(1, t/0.006); rel = np.minimum(1, (dur - t)/0.25)
    return y*att*np.clip(rel, 0, 1)*vel

def celesta(m, vel, dur):
    f0 = mf(m); t = np.arange(int(dur*SR))/SR
    y = np.sin(2*np.pi*f0*t)*np.exp(-2.2*t) + 0.25*np.sin(2*np.pi*f0*4.0*t)*np.exp(-6*t) + 0.1*np.sin(2*np.pi*f0*2.76*t)*np.exp(-4*t)
    return y*np.minimum(1, t/0.002)*vel

BPM = 72; BEAT = 60/BPM; BAR = 3*BEAT; T0 = 0.25
CH = {"F": (41, [53, 57, 60, 65]), "C/E": (40, [52, 55, 60, 64]), "Dm": (38, [50, 57, 62, 65]), "Bb": (34, [46, 53, 57, 62]),
      "Gm": (43, [50, 55, 58, 62]), "C": (36, [48, 55, 60, 64])}
PROG = ["F", "C/E", "Dm", "Bb"]
MEL = [[(0, 69, 2), (2, 72, 1)], [(0, 67, 3)], [(0, 65, 2), (2, 69, 1)], [(0, 74, 2), (2, 72, 1)],
       [(0, 69, 2), (2, 77, 1)], [(0, 76, 3)], [(0, 74, 2), (2, 72, 1)], [(0, 70, 1.5), (1.5, 69, 1.5)]]
ev = []; strings = []
SIL = (19.7, 22.4)          # aire tras «Y tú la apartas…»
k = 0
while True:
    t = T0 + k*BAR
    if t > 64.4: break
    ch = PROG[k % 4]; bass, tones = CH[ch]
    hum = lambda: rng.normal(0, 0.007)
    if t < 17.0:                                           # inicio: pocas notas
        ev += [(t+hum(), "p", bass+12, .42, 4), (t+BEAT+hum(), "p", tones[2]+12, .28, 3), (t+2*BEAT+hum(), "p", tones[3]+12, .26, 3)]
    elif t < 19.5:
        ev += [(t+hum(), "p", bass+12, .36, 4), (t+BEAT*1.5+hum(), "p", tones[2]+12, .24, 3)]
    elif t < 23.0: pass
    else:                                                  # mece en corcheas
        warm = .40 if t < 34 else .46
        ev.append((t+hum(), "p", bass+12 if t < 34 else bass, warm+.04, 4))
        if t >= 34: ev.append((t+hum(), "p", bass+12, warm*.6, 4))
        for j, i in enumerate([1, 2, 3, 2, 1]):
            ev.append((t + (j+1)*BEAT/2 + hum(), "p", tones[i]+12, warm*(.62 if j % 2 else .7), 3))
        if t >= 33.9:                                      # melodía desde «Diez minutos después, vuelve»
            for (b, m, d) in MEL[k % 8]: ev.append((t + b*BEAT + hum(), "p", m+12 if t > 46 and m < 72 else m, .50 if t < 46 else .56, d*BEAT+1.2))
        if t >= 29.5: strings.append((t, t+BAR, ch, .025 if t < 46 else .04))
    k += 1
ev = [e for e in ev if not (SIL[0] < e[0] < SIL[1])]
ev.append((21.9, "p", 69, .26, 4))                         # una nota en el silencio, sobre «Te mira.»
# celesta en las frases destacadas
for (t, m) in [(5.95, 84), (48.7, 81), (49.25, 84), (54.78, 89)]: ev.append((t, "c", m, .18, 3))
# cierre: Bb – C – F, última nota sobre el plano final
t = T0 + k*BAR
for (dt, chn) in [(0, "Bb"), (BAR*0.8, "C")]:
    bass, tones = CH[chn]
    ev += [(t+dt, "p", bass+12, .42, 4)] + [(t+dt+.12*(i+1), "p", m+12, .30, 3.5) for i, m in enumerate(tones[1:])]
tF = 66.0
ev += [(tF, "p", 41, .40, 3), (tF+.03, "p", 53, .34, 3)] + [(tF+.16*(i+1), "p", m, .30-.03*i, 3) for i, m in enumerate([60, 65, 69, 72])]
ev.append((67.3, "c", 89, .14, 2)); ev.append((67.3, "p", 77, .30, 1.7))
L = np.zeros((int(LEN*SR)+SR*5, 2))
for (t, kind, m, v, d) in ev:
    if t < 0 or t >= LEN: continue
    y = piano(m, v, d) if kind == "p" else celesta(m, v, d)
    pan = np.clip((m-60)/40, -.5, .5); i0 = int(t*SR)
    L[i0:i0+len(y), 0] += y*np.sqrt(.5-pan/2); L[i0:i0+len(y), 1] += y*np.sqrt(.5+pan/2)
# cuerdas cálidas y discretas
tt = np.arange(len(L))/SR; P = np.zeros((len(L), 2))
for (a, b, ch, lvl) in strings:
    i0, i1 = int(a*SR), int(min(b+1.5, LEN)*SR); seg = tt[i0:i1]-a
    env = np.minimum(1, seg/1.2)*np.clip((b+1.5-a-seg)/1.4, 0, 1)
    for c, m in enumerate(CH[ch][1][:3]):
        f = mf(m+12); vib = 1 + .003*np.sin(2*np.pi*5.2*seg + c)
        for side, det in ((0, .999), (1, 1.001)):
            P[i0:i1, side] += lvl*env*sum(np.sin(2*np.pi*f*h*det*vib*seg)/h**1.6 for h in range(1, 6))
P = sosfilt(butter(2, [180, 2200], "band", fs=SR, output="sos"), P, axis=0)
L += P
# sala cálida
n = int(2.6*SR); t2 = np.arange(n)/SR
for c in range(2):
    ir = rng.normal(0, 1, n)*np.exp(-6.9*t2/2.3); ir = sosfilt(butter(2, 5000, "low", fs=SR, output="sos"), ir)
    ir[:int(.025*SR)] = 0; ir /= np.sqrt(np.sum(ir**2))
    L[:, c] = .8*L[:, c] + .32*fftconvolve(L[:, c], ir)[:len(L)]
L = L[:int(LEN*SR)]
fl = int(1.4*SR); L[-fl:] *= (np.linspace(1, 0, fl)**1.5)[:, None]
L /= np.max(np.abs(L))*1.12
with wave.open(OUT, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((L*32767).astype("<i2").tobytes())
print("eventos", len(ev))
