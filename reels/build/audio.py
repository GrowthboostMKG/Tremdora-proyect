import numpy as np, subprocess, json, os
from scipy.signal import butter, sosfilt, fftconvolve

S = os.path.dirname(os.path.abspath(__file__))
SR = 48000; TOTAL = 88.8; OFF = 0.30
N = int(TOTAL * SR)
rng = np.random.default_rng(11)
def t_(d): return np.arange(int(d * SR)) / SR
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, a, b, o=2): return sosfilt(butter(o, [a, b], 'band', fs=SR, output='sos'), x)
def midi(n): return 440 * 2 ** ((n - 69) / 12)
def add(buf, x, t0):
    i = int(t0 * SR)
    if i >= len(buf): return
    x = x[:len(buf) - i]; buf[i:i + len(x)] += x

# ------------------------------------------------------------ instruments
def piano(n, vel, dur=4.0):
    f = midi(n); t = t_(dur + 1.5); x = np.zeros_like(t)
    B = 0.00015
    for k in range(1, 12):
        fk = f * k * np.sqrt(1 + B * k * k)
        if fk > 9000: break
        amp = (1 / k ** 1.3) * (0.6 + 0.4 * vel)
        dec = 1.6 + 2.2 * (60 / n) ** 2 / k ** 0.6
        x += amp * np.sin(2 * np.pi * fk * t + rng.uniform(0, 6)) * np.exp(-t / dec * (1 + 0.15 * k))
    att = 1 - np.exp(-t / 0.004)
    rel = np.clip((dur + 1.5 - t) / 1.5, 0, 1)   # damper
    x *= att * rel
    x = lp(x, 1800 + 3500 * vel)
    return x * vel * 0.32

def cello(n, dur, vel=0.6):
    f0 = midi(n); t = t_(dur)
    vib = 1 + 0.0045 * np.sin(2 * np.pi * 5.1 * t) * np.clip((t - 0.5) / 0.8, 0, 1)
    ph = 2 * np.pi * np.cumsum(f0 * vib) / SR
    x = sum((1 / k) * np.sin(k * ph) * (0.85 ** k if k > 6 else 1) for k in range(1, 16))
    x = bp(x, 90, 2600)
    x = x + 0.6 * bp(x, 250, 600) + 0.4 * bp(x, 900, 1300)   # body formants
    bow = bp(rng.normal(0, 1, len(t)), 1500, 4000) * 0.015
    env = np.clip(t / 0.55, 0, 1) ** 1.5 * np.clip((dur - t) / 0.9, 0, 1)
    swell = 0.85 + 0.15 * np.sin(np.pi * np.clip(t / dur, 0, 1))
    return (x * 0.11 + bow) * env * swell * vel

def pad(notes, dur, vel=0.5):
    t = t_(dur); x = np.zeros_like(t)
    for n in notes:
        for det in (-0.07, 0, 0.06):
            x += np.sin(2 * np.pi * midi(n + det) * t + rng.uniform(0, 6))
            x += 0.25 * np.sin(4 * np.pi * midi(n + det) * t)
    x = lp(x, 900)
    env = np.clip(t / 1.8, 0, 1) * np.clip((dur - t) / 1.8, 0, 1)
    return x * env * vel * 0.018

def reverb(x, secs=3.2, mix=0.32):
    t = t_(secs)
    ir = rng.normal(0, 1, len(t)) * np.exp(-t / (secs / 6.9) * 2.2)
    ir = lp(ir, 5000); ir[:int(0.012 * SR)] = 0; ir /= np.sqrt(np.sum(ir ** 2))
    wet = fftconvolve(x, ir)[:len(x)]
    return x * (1 - mix) + wet * mix * 1.3

# ------------------------------------------------------------ score (D major, 64 bpm)
BEAT = 60 / 64; BAR = 4 * BEAT
# chord per bar: (bass midi, chord tones)
D, A_Cs, Bm, G, Em, D_Fs, A, Fsm = (38, [62, 66, 69]), (37, [61, 64, 69]), (35, [62, 66, 71]), (31, [62, 67, 71]), \
                                  (40, [64, 67, 71]), (42, [62, 66, 69]), (33, [61, 64, 69]), (42, [61, 66, 69])
PROG = [D, A_Cs, Bm, G,  D, A_Cs, Bm, G,  Em, G, D_Fs, A,  G, D_Fs, Em, A,  Bm, G, D, A,  G, A, D, D]
NB = len(PROG)
piano_bus = np.zeros(N); cello_bus = np.zeros(N); pad_bus = np.zeros(N)

def tb(bar, beat=0): return 0.6 + bar * BAR + beat * BEAT   # music bar grid (starts 0.6 s)
def intensity(sec):
    # arrangement density 0..1 following the story
    k = [(0, .0), (7, .15), (14, .35), (25, .5), (37, .55), (45, .62), (62, .78), (69, .85), (70.6, .35), (74.6, .4),
         (76, .95), (82, 1.0), (86, .6), (89, .3)]
    for (a, x), (b, y) in zip(k, k[1:]):
        if a <= sec <= b: return x + (y - x) * (sec - a) / (b - a)
    return .3

# melody (bar, beat, midi, beats) — gentle, hopeful line entering later
MEL = {4: [(0, 78, 2), (2, 76, 1), (3, 74, 1)], 5: [(0, 76, 3), (3, 73, 1)], 6: [(0, 74, 2), (2, 73, 1), (3, 71, 1)],
       7: [(0, 71, 3)],
       8: [(0, 71, 1.5), (1.5, 74, .5), (2, 76, 2)], 9: [(0, 74, 1), (1, 71, 1), (2, 74, 2)], 10: [(0, 78, 3)],
       11: [(0, 76, 2), (2, 73, 2)],
       12: [(0, 74, 1), (1, 79, 2), (3, 78, 1)], 13: [(0, 78, 2), (2, 76, 1), (3, 74, 1)], 14: [(0, 76, 3)],
       15: [(0, 76, 1.5), (1.5, 73, .5), (2, 81, 2)],
       16: [(0, 78, 2), (2, 74, 1), (3, 78, 1)], 17: [(0, 79, 3), (3, 78, 1)], 18: [(0, 78, 2)],
       19: [(0, 76, 4)],
       20: [(0, 83, 2), (2, 81, 1), (3, 79, 1)], 21: [(0, 81, 2), (2, 76, 2)], 22: [(0, 78, 4)], 23: [(0, 74, 4)]}
CEL = {6: [(0, 50, 4)], 7: [(0, 55, 4)], 8: [(0, 52, 4)], 9: [(0, 50, 4)], 10: [(0, 54, 4)], 11: [(0, 52, 4)],
       12: [(0, 55, 2), (2, 57, 2)], 13: [(0, 54, 4)], 14: [(0, 55, 2), (2, 52, 2)], 15: [(0, 57, 4)],
       16: [(0, 54, 2), (2, 50, 2)], 17: [(0, 55, 3), (3, 54, 1)], 18: [(0, 50, 4)], 19: [(0, 52, 4)],
       20: [(0, 55, 2), (2, 54, 2)], 21: [(0, 52, 2), (2, 57, 2)], 22: [(0, 54, 4)], 23: [(0, 50, 4)]}

for bar in range(NB):
    bass, tones = PROG[bar]
    t0 = tb(bar)
    if t0 > TOTAL: break
    I = intensity(t0 + 1)
    add(pad_bus, pad([bass + 12] + tones, BAR + 1.8, 0.4 + 0.6 * I), t0 - 0.4)
    if t0 < 7.5: continue
    # left hand: bass + broken chord in eighths, density by intensity
    hum = lambda: rng.normal(0, 0.008)
    add(piano_bus, piano(bass + 12, 0.30 + 0.25 * I, BAR), t0 + hum())
    pattern = [bass + 19, tones[0], tones[1], tones[2], tones[1], tones[0], bass + 19, tones[1]]
    climax_dip = 70.4 < t0 + 2 < 74.8
    step = 1 if I > 0.55 and not climax_dip else 2
    for e in range(0, 8, step):
        v = (0.16 + 0.22 * I) * (1.0 if e % 4 == 0 else 0.8) * rng.uniform(.88, 1.05)
        add(piano_bus, piano(pattern[e] - 12 if e == 0 else pattern[e], v, 1.2 * step), t0 + e * BEAT / 2 + hum())
    if bar in MEL and not climax_dip:
        for beat, n, ln in MEL[bar]:
            add(piano_bus, piano(n, (0.38 + 0.3 * I) * rng.uniform(.9, 1.05), ln * BEAT + 0.3), tb(bar, beat) + hum())
    elif bar in MEL and climax_dip:
        beat, n, ln = MEL[bar][0]
        add(piano_bus, piano(n, 0.33, BAR), tb(bar, beat))
    if bar in CEL:
        for beat, n, ln in CEL[bar]:
            add(cello_bus, cello(n - 12 if bar < 12 else n - 12, ln * BEAT + 0.6, 0.45 + 0.5 * I * (0.5 if climax_dip else 1)),
                tb(bar, beat) - 0.15)
# final resolving chord
add(piano_bus, piano(62, .32, 5), tb(23, 0)); add(piano_bus, piano(69, .28, 5), tb(23, 0.05)); add(piano_bus, piano(78, .3, 5), tb(23, .1))

music = reverb(piano_bus * 1.0 + cello_bus * 0.9 + pad_bus, 3.4, 0.36)
music = hp(music, 45)
fade = np.ones(N); fi = int(7 * SR); fade[:fi] = np.linspace(0, 1, fi) ** 2
fo = int(3.0 * SR); fade[-fo:] *= np.linspace(1, 0, fo) ** 1.5
music *= fade

# ------------------------------------------------------------ sound design
sfx = np.zeros(N)
def noise(d): return rng.normal(0, 1, int(d * SR))
# domestic ambience (room tone + very soft distant clock) at the start and at the door shot
room = lp(noise(TOTAL), 220, 2) * 0.012
amb_env = np.zeros(N)
for a, b in [(0, 10), (15, 21)]:
    i0, i1 = int(a * SR), int(b * SR); L = i1 - i0
    amb_env[i0:i1] = np.minimum(1, np.minimum(np.arange(L) / (0.8 * SR), (L - np.arange(L)) / (1.2 * SR)))
sfx += room * amb_env * 1.0
for k in range(0, 10):
    c = bp(noise(0.03), 2500, 6000) * np.exp(-t_(0.03) / 0.004) * 0.010
    add(sfx, c, 0.45 + k * 1.0)
# soft air at focus transitions
def air(d, peak, lo=300, hi=2500, amp=0.05):
    x = bp(noise(d), lo, hi); t = t_(d)
    env = np.exp(-((t - peak) / (d / 4)) ** 2)
    return x * env * amp
add(sfx, air(1.6, .8), OFF + 15.0 - 0.8)
add(sfx, air(1.4, .7, 200, 1800, .04), OFF + 40.4 - 0.7)
# textile rustle during caresses
def rustle(d, amp=0.03):
    x = bp(noise(d), 1800, 7000); t = t_(d)
    env = np.zeros_like(t)
    for _ in range(int(d * 2.5)):
        c = rng.uniform(0, d); w = rng.uniform(0.06, 0.22)
        env += rng.uniform(.4, 1) * np.exp(-((t - c) / w) ** 2)
    return x * np.clip(env, 0, 1) * amp
add(sfx, rustle(2.4, .022), OFF + 31.2)
add(sfx, rustle(1.6, .016), OFF + 25.6)
# small movement between two shots (light dissolve into the climax close)
def swish(d=0.9, amp=0.035):
    t = t_(d); f = 600 + 1800 * (t / d)
    x = bp(noise(d), 400, 3000)
    return x * np.sin(np.pi * t / d) ** 2 * amp
add(sfx, swish(), OFF + 74.55 - 0.45)
add(sfx, swish(0.7, .025), OFF + 20.65 - 0.35)
# closing wind
wd = TOTAL - (OFF + 75.5)
w = lp(noise(wd), 700, 2); t = t_(wd)
gust = 0.6 + 0.4 * np.sin(2 * np.pi * 0.13 * t + 1) * np.sin(2 * np.pi * 0.07 * t)
wenv = np.clip(t / 3, 0, 1) * np.clip((wd - t) / 2, 0, 1)
add(sfx, w * gust * wenv * 0.05, OFF + 75.5)
sfx = reverb(sfx, 1.5, 0.2)

np.save(S + "/music.npy", music.astype(np.float32)); np.save(S + "/sfx.npy", sfx.astype(np.float32))
print("ok", np.abs(music).max(), np.abs(sfx).max())
