import numpy as np, subprocess, json, os
from scipy.signal import butter, sosfilt, fftconvolve

S = os.path.dirname(os.path.abspath(__file__))
SR = 48000; TOTAL = 54.8; OFF = 0.30
N = int(TOTAL * SR)
rng = np.random.default_rng(23)
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


# ------------------------------------------------------------ score #2: F major lullaby-waltz, 3/4, 70 bpm
def felt(n, vel, dur):          # felt/muted piano: softer, darker, shorter sustain
    x = piano(n, vel, dur)
    return lp(x, 1400 + 1600 * vel) * 1.25
BEAT = 60 / 70; BAR = 3 * BEAT
F_, C_E, Dm, Bb, Am, Gm, C_, F_A = (41, [65, 69, 72]), (40, [64, 67, 72]), (38, [65, 69, 74]), (34, [65, 70, 74]), \
                                   (45, [64, 69, 72]), (43, [65, 70, 74]), (36, [64, 67, 72]), (45, [65, 69, 72])
PROG = [F_, C_E, Dm, Bb, F_, C_E, Gm, Am, Bb, C_, Dm, Bb, F_A, C_, Bb, C_, Dm, Bb, Gm, C_, F_, F_]
NB = len(PROG)
piano_bus = np.zeros(N); cello_bus = np.zeros(N); pad_bus = np.zeros(N)
def tb(bar, beat=0): return 0.9 + bar * BAR + beat * BEAT
def sec_of(bar): return tb(bar)
# cello melody (bar: [(beat, midi, beats)]) — sings from ~13 s
MEL = {3: [(0, 57, 2), (2, 55, 1)], 4: [(0, 53, 3)], 5: [(0, 52, 2), (2, 55, 1)], 6: [(0, 55, 3)], 7: [(0, 57, 3)],
       8: [(0, 58, 6)], 10: [(0, 57, 2), (2, 60, 1)], 11: [(0, 58, 2), (2, 57, 1)], 12: [(0, 57, 2), (2, 60, 1)],
       13: [(0, 64, 3)], 14: [(0, 65, 2), (2, 62, 1)], 15: [(0, 64, 3)], 16: [(0, 62, 3)], 17: [(0, 58, 3)],
       18: [(0, 58, 2), (2, 60, 1)], 19: [(0, 64, 3)], 20: [(0, 65, 6)]}
ANS = {3: [(1, 81, 1), (2, 77, 1)], 5: [(1, 79, 1), (2, 76, 1)], 11: [(1, 81, 1), (2, 77, 1)], 13: [(1, 79, 1), (2, 76, 1)],
       15: [(0, 84, 1), (1, 81, 1), (2, 77, 1)], 19: [(1, 79, 1), (2, 76, 1)], 20: [(0, 81, 3)]}
def dens(sec):
    k = [(0, 0), (4, .1), (8, .35), (16, .5), (19.5, .45), (20.3, .2), (23.8, .25), (25, .55), (33, .75), (41.5, .85), (42.2, .3), (46.3, .35), (47.2, .9), (51, 1.0), (53.5, .6), (56, .3)]
    for (a, x), (b, y) in zip(k, k[1:]):
        if a <= sec <= b: return x + (y - x) * (sec - a) / (b - a)
    return .3
for bar in range(NB):
    bass, tones = PROG[bar]; t0 = tb(bar)
    if t0 > TOTAL - 0.5: break
    I = dens(t0 + 1); pause = 19.9 < t0 + 1.2 < 24.0; dip = 42.1 < t0 + 1.2 < 46.4
    add(pad_bus, pad([bass + 12] + tones, BAR + 1.6, 0.35 + 0.6 * I), t0 - 0.3)
    if t0 < 5.5: continue
    hum = lambda: rng.normal(0, 0.009)
    if not pause:
        # waltz rocking: bass on 1, chord on 2 and 3 (left hand), very soft
        add(piano_bus, felt(bass + 12, 0.26 + 0.24 * I, BAR), t0 + hum())
        if not dip:
            for bt in (1, 2):
                for k, n in enumerate(tones[:2] if bt == 1 else tones[1:]):
                    add(piano_bus, felt(n - 12 if I < .5 else n, (0.13 + 0.16 * I) * rng.uniform(.9, 1.05), BEAT * 1.1),
                        t0 + bt * BEAT + k * 0.012 + hum())
            if I > .6:   # flowing eighths in the climax
                for e, n in [(0.5, tones[2]), (1.5, tones[0] + 12), (2.5, tones[2])]:
                    add(piano_bus, felt(n, 0.11 + 0.1 * I, BEAT * .8), t0 + e * BEAT + hum())
    else:
        add(piano_bus, felt(tones[2] + 12, 0.18, BAR * 1.5), t0 + 0.4)      # a single, suspended note
    if bar in ANS and not dip and not pause:
        for bt, n, ln in ANS[bar]:
            add(piano_bus, felt(n, (0.20 + 0.18 * I) * rng.uniform(.9, 1.05), ln * BEAT + .4), tb(bar, bt) + hum())
    if bar in MEL:
        for bt, n, ln in MEL[bar]:
            v = 0.5 + 0.5 * I
            if dip: v *= 0.55
            add(cello_bus, cello(n - 12, ln * BEAT + 0.5, v), tb(bar, bt) - 0.12)
add(piano_bus, felt(77, .24, 4), tb(20, 1)); add(piano_bus, felt(72, .2, 4), tb(20, 1.05)); add(piano_bus, felt(65, .2, 4), tb(20, 1.1))
music = reverb(piano_bus * 1.1 + cello_bus * 1.0 + pad_bus * 0.9, 3.8, 0.40)
music = hp(music, 45)
fade = np.ones(N); fi = int(6 * SR); fade[:fi] = np.linspace(0, 1, fi) ** 2
fo = int(2.2 * SR); fade[-fo:] *= np.linspace(1, 0, fo) ** 1.5
music *= fade

# ------------------------------------------------------------ sound design #2
sfx = np.zeros(N)
def noise(d): return rng.normal(0, 1, int(d * SR))
def env_box(a, b, fi=1.0, fo=1.5):
    e = np.zeros(N); i0, i1 = int(a * SR), int(min(b, TOTAL) * SR); L = i1 - i0
    e[i0:i1] = np.minimum(1, np.minimum(np.arange(L) / (fi * SR), (L - np.arange(L)) / (fo * SR))); return e
room = lp(noise(TOTAL), 260, 2) * 0.011
sfx += room * (env_box(0, 9.4) + env_box(19.9, 24.3, 1.0, 1.0))
# soft distant birdsong outside the window (door shot and empty-bed shot)
def chirp(f0, f1, d, amp):
    t = t_(d); f = np.linspace(f0, f1, len(t)); ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.sin(np.pi * t / d) ** 2 * amp
for a, b in [(9.8, 14.3), (20.4, 23.8)]:
    tt = a
    while tt < b:
        f0 = rng.uniform(3200, 4200)
        for k in range(rng.integers(2, 5)):
            add(sfx, lp(chirp(f0, f0 * rng.uniform(1.1, 1.35), rng.uniform(.05, .09), .006), 6000), tt + k * 0.11)
        tt += rng.uniform(0.8, 1.6)
# air on the two blinks and the zoom-throughs
def air(d, peak, lo=300, hi=2500, amp=0.05):
    x = bp(noise(d), lo, hi); t = t_(d)
    return x * np.exp(-((t - peak) / (d / 4)) ** 2) * amp
for T, a in [(4.82, .035), (9.40, .045), (14.55, .03), (23.92, .03)]:
    add(sfx, air(1.3, .65, 250, 2200, a), T - 0.65)
def rustle(d, amp=0.03):
    x = bp(noise(d), 1800, 7000); t = t_(d); e = np.zeros_like(t)
    for _ in range(int(d * 2.5)):
        c = rng.uniform(0, d); w = rng.uniform(0.06, 0.22); e += rng.uniform(.4, 1) * np.exp(-((t - c) / w) ** 2)
    return x * np.clip(e, 0, 1) * amp
add(sfx, rustle(2.2, .02), 16.4); 
def swish(d=0.9, amp=0.03):
    t = t_(d); x = bp(noise(d), 400, 3000); return x * np.sin(np.pi * t / d) ** 2 * amp
add(sfx, swish(1.0, .028), 33.9 - 0.5); add(sfx, swish(0.9, .025), 36.3 - 0.1)
wd = TOTAL - 47.5; w = lp(noise(wd), 650, 2); t = t_(wd)
gust = 0.6 + 0.4 * np.sin(2 * np.pi * 0.11 * t + .5) * np.sin(2 * np.pi * 0.06 * t)
add(sfx, w * gust * np.clip(t / 3, 0, 1) * np.clip((wd - t) / 2, 0, 1) * 0.045, 47.5)
sfx = reverb(sfx, 1.5, 0.2)
np.save(S + "/music5.npy", music.astype(np.float32)); np.save(S + "/sfx5.npy", sfx.astype(np.float32))
print("ok", np.abs(music).max())
