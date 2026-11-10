"""Original instrumental score (piano + pad + bass + strings) synthesised from scratch, plus soft transition SFX."""
import numpy as np, wave, sys

SR = 44100
from tmap import tmap
DUR = tmap(69.3) + 2.2
N = int(SR * DUR)
rng = np.random.default_rng(7)

def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)

def env_adsr(n, a, r, sr=SR):
    e = np.ones(n)
    na, nr = int(a * sr), int(r * sr)
    na = min(na, n); nr = min(nr, n - na)
    if na: e[:na] = np.sin(np.linspace(0, np.pi / 2, na)) ** 2
    if nr: e[n - nr:] *= np.cos(np.linspace(0, np.pi / 2, nr)) ** 2
    return e

L = np.zeros(N); R = np.zeros(N)

def add(sig, t0, pan=0.0, gain=1.0):
    i = int(t0 * SR)
    if i >= N: return
    sig = sig[: N - i]
    gl = np.cos((pan + 1) * np.pi / 4) * gain
    gr = np.sin((pan + 1) * np.pi / 4) * gain
    L[i:i + len(sig)] += sig * gl
    R[i:i + len(sig)] += sig * gr

def piano(m, dur, vel=0.5):
    n = int((dur + 2.5) * SR)
    t = np.arange(n) / SR
    f = hz(m)
    s = np.zeros(n)
    for h in range(1, 8):
        inh = h * np.sqrt(1 + 0.0004 * h * h)
        amp = vel / h ** 1.6
        dec = 0.9 + 0.55 * h + f / 900
        s += amp * np.sin(2 * np.pi * f * inh * t + rng.uniform(0, 6.28)) * np.exp(-t * dec)
    s += 0.25 * vel * np.sin(2 * np.pi * f * t) * np.exp(-t * 0.35)  # sustain body
    att = np.minimum(1, t / 0.004)
    rel = np.ones(n); k = int(dur * SR)
    rel[k:] = np.exp(-(t[k:] - dur) * 6)
    return s * att * rel * 0.5

def pad(ms, dur, gain=0.12, a=1.6, r=1.8, bright=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for m in ms:
        f = hz(m)
        for det in (-0.07, 0.0, 0.06):
            ff = f * 2 ** (det / 12)
            s += np.sin(2 * np.pi * ff * t + rng.uniform(0, 6.28))
            s += 0.30 * bright * np.sin(2 * np.pi * 2 * ff * t + rng.uniform(0, 6.28))
            s += 0.12 * bright * np.sin(2 * np.pi * 3 * ff * t + rng.uniform(0, 6.28))
    s *= (1 + 0.08 * np.sin(2 * np.pi * 0.23 * t))
    return s * env_adsr(n, a, r) * gain / (len(ms) * 3)

def strings(m, dur, gain=0.1):
    n = int(dur * SR)
    t = np.arange(n) / SR
    vib = 1 + 0.004 * np.sin(2 * np.pi * 5.2 * t) * np.minimum(1, t / 1.5)
    f = hz(m)
    ph = 2 * np.pi * f * np.cumsum(vib) / SR
    s = sum((1 / h ** 1.3) * np.sin(h * ph + rng.uniform(0, 6)) for h in range(1, 7))
    return s * env_adsr(n, min(1.8, dur * 0.4), min(1.5, dur * 0.4)) * gain

# A minor-ish emotional progression: Am F C G   (bar = 4 beats @ 72 bpm)
BEAT = 60 / 72
BAR = 4 * BEAT
chords = {
    'Am': [57, 60, 64], 'F': [53, 57, 60], 'C': [48, 52, 55, 60], 'G': [55, 59, 62],
    'Em': [52, 55, 59], 'Fmaj7': [53, 57, 60, 64],
}
prog = ['Am', 'F', 'C', 'G', 'Am', 'F', 'C', 'G', 'F', 'G', 'Am', 'Em', 'F', 'G', 'C', 'Am', 'F', 'G', 'C', 'Fmaj7', 'C', 'C']
nbars = len(prog)

for b, ch in enumerate(prog):
    t0 = b * BAR
    if t0 > DUR: break
    notes = chords[ch]
    root = notes[0]
    sec = t0
    # intensity curve: soft intro, lift at ~28s (Japón), fuller from 46s, peak 57-65s, resolve
    inten = np.interp(sec, [0] + [tmap(v) for v in (12, 28, 46, 57, 64, 68)] + [DUR], [0.75, 0.75, 0.8, 0.88, 1.0, 1.0, 0.75, 0.5])
    # pad
    add(pad([n - 12 for n in notes] + notes, BAR + 1.6, gain=0.10 * inten, a=(0.05 if b == 0 else 1.6), bright=0.6 + 0.4 * inten), t0, 0)
    # piano: broken chord, sparse at first then flowing eighths
    pattern = [0, 2, 1, 3, 2, 1, 3, 2]
    step = BAR / len(pattern)
    arp = [root - 12, notes[1], notes[2], notes[-1] + 12 if len(notes) > 3 else notes[0] + 12]
    for k, idx in enumerate(pattern):
        m = arp[idx]
        jitter = rng.normal(0, 0.008)
        vel = (0.65 if (k == 0 and b == 0) else 0.55 if k == 0 else 0.32) * (0.8 + 0.4 * inten) * rng.uniform(0.9, 1.05)
        add(piano(m, step * 1.6, vel), t0 + k * step + jitter, pan=(-0.25 if m < 60 else 0.25))
    # simple top melody note on beat 1 & 3 from ~28s
    if sec >= tmap(27):
        top = notes[-1] + 12
        add(piano(top, BEAT * 1.8, 0.28 * inten), t0 + 0.004, 0.1)
        add(piano(notes[1] + 12, BEAT * 1.8, 0.2 * inten), t0 + 2 * BEAT, 0.1)
    # bass from 28s
    if sec >= tmap(27):
        n = int((BAR + 0.3) * SR); t = np.arange(n) / SR
        f = hz(root - 24 if root >= 48 else root - 12)
        bs = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)) * env_adsr(n, 0.08, 0.6) * 0.11 * inten
        add(bs, t0, 0)
    # strings from 46s
    if sec >= tmap(45):
        g = 0.05 * inten
        add(strings(notes[-1] + 12, BAR + 1.2, g), t0, -0.3)
        add(strings(notes[1] + 12, BAR + 1.2, g * 0.8), t0, 0.3)

# final sustained resolve chord + fade
end_t = tmap(66.5)
add(pad([48, 55, 60, 64, 67], 5.0, gain=0.12, a=1.2, r=3.0), end_t, 0)
E = tmap(69.3); add(piano(72, 3.0, 0.3), E, 0.1); add(piano(48, 3.0, 0.35), E, -0.2); add(piano(64, 3.0, 0.22), E + 0.02, 0.2)

# reverb: stereo decorrelated exponential noise IR
def reverb(x, seed, rt=2.4):
    r = np.random.default_rng(seed)
    n = int(rt * SR)
    t = np.arange(n) / SR
    ir = r.normal(0, 1, n) * np.exp(-t * 6.9 / rt)
    # darken IR with one-pole lowpass
    y = np.zeros(n); a = 0.75
    acc = 0.0
    for_i = ir.copy()
    ir = np.convolve(for_i, (1 - a) * a ** np.arange(40), mode='same')
    ir[: int(0.02 * SR)] = 0
    ir /= np.sqrt((ir ** 2).sum())
    size = 1 << int(np.ceil(np.log2(len(x) + n)))
    return np.fft.irfft(np.fft.rfft(x, size) * np.fft.rfft(ir, size), size)[: len(x)]

wetL, wetR = reverb(L, 1), reverb(R, 2)
outL = L * 0.75 + wetL * 0.45
outR = R * 0.75 + wetR * 0.45
# fade in/out
fade = np.ones(N)
fi = int(0.03 * SR); fade[:fi] = np.linspace(0, 1, fi) ** 2
fo_start = int((tmap(69.3) + 0.5) * SR); fade[fo_start:] = np.linspace(1, 0, N - fo_start) ** 1.5
outL *= fade; outR *= fade
peak = max(np.abs(outL).max(), np.abs(outR).max())
outL /= peak / 0.89; outR /= peak / 0.89

def write(path, l, r):
    st = np.stack([l, r], 1)
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(st, -1, 1) * 32767).astype('<i2').tobytes())

write('music_short.wav', outL, outR)

# ---- SFX: soft whooshes at whip/zoom transitions, gentle low swell before hook reveal
sl = np.zeros(N); sr_ = np.zeros(N)
def whoosh(tc, dur=0.55, gain=0.35, pan_dir=1):
    n = int(dur * SR); t = np.linspace(0, 1, n)
    noise = rng.normal(0, 1, n)
    # sweeping band: crude via cascaded one-pole lowpass with time-varying coefficient
    y = np.zeros(n); y2 = np.zeros(n); s1 = s2 = 0.0
    cut = 0.03 + 0.25 * np.sin(np.pi * t) ** 2
    for i in range(n):
        s1 += cut[i] * (noise[i] - s1); s2 += cut[i] * (s1 - s2); y[i] = s1 - s2 * 0.6
    e = np.sin(np.pi * t) ** 2.2
    y = y * e; y /= np.abs(y).max() + 1e-9
    i0 = int((tc - dur / 2) * SR)
    pan = np.linspace(-0.6 * pan_dir, 0.6 * pan_dir, n)
    sl[i0:i0 + n] += y * gain * np.cos((pan + 1) * np.pi / 4)
    sr_[i0:i0 + n] += y * gain * np.sin((pan + 1) * np.pi / 4)

for tc, kind in [(tmap(3.0), 'zoom'), (tmap(28.8), 'whip'), (tmap(46.6), 'whip'), (tmap(60.1), 'zoom')]:
    whoosh(tc, 0.6 if kind == 'zoom' else 0.45, 0.28 if kind == 'zoom' else 0.32, 1 if kind == 'whip' else -1)
write('sfx_short.wav', sl, sr_)
print('ok')
