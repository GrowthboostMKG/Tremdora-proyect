import json, numpy as np, os
from scipy.io import wavfile
S = os.path.dirname(os.path.abspath(__file__)); SR = 48000
sr, v = wavfile.read(S + "/v48.wav"); v = v.astype(np.float32)
segs = json.load(open(S + "/words3.json"))
# keep: (segment indices to join, pause after in s)
KEEP = [([0], .32), ([1], .55), ([2], .65), ([5, 6], .70), ([8, 9], .80), ([14], .75),
        ([15, 16, 17], .65), ([20, 21], .75), ([23], .42), ([24], .55), ([25], .65), ([26], .40),
        ([27], .55), ([28, 29], .65), ([30], 0)]
env = np.sqrt(np.convolve(v ** 2, np.ones(480) / 480, 'same'))
def quiet_edge(t, direction):           # walk outwards to the nearest quiet point (<-50 dB) within 0.3 s
    i = int(t * SR)
    for k in range(0, int(0.3 * SR), 48):
        j = i + direction * k
        if 0 <= j < len(env) and env[j] < 10 ** (-50 / 20): return j
    return i + direction * int(0.12 * SR)
out = [np.zeros(int(0.30 * SR), np.float32)]; tmap = []; pos = 0.30
for idxs, pause in KEEP:
    a = segs[idxs[0]]["start"]; b = segs[idxs[-1]]["end"]
    i0 = max(0, quiet_edge(max(a - 0.04, 0), -1)); i1 = min(len(v), quiet_edge(b + 0.06, 1))
    clip = v[i0:i1].copy(); f = int(0.015 * SR)
    clip[:f] *= np.linspace(0, 1, f); clip[-f:] *= np.linspace(1, 0, f)
    tmap.append(dict(src0=i0 / SR, dst0=pos, dur=len(clip) / SR, segs=idxs))
    out.append(clip); pos += len(clip) / SR
    out.append(np.zeros(int(pause * SR), np.float32)); pos += pause
voice = np.concatenate(out)
wavfile.write(S + "/v_cut.wav", SR, voice)
# remapped word timings (absolute, already including the 0.30 s lead)
words = []
for m in tmap:
    for si in m["segs"]:
        for w in segs[si]["words"]:
            words.append(dict(w=w["w"], s=w["s"] - m["src0"] + m["dst0"], e=w["e"] - m["src0"] + m["dst0"]))
json.dump(dict(words=words, blocks=[dict(dst0=m["dst0"], dur=m["dur"], text=" ".join(segs[s]["text"].strip() for s in m["segs"])) for m in tmap], voice_end=pos), open(S + "/cut_words.json", "w"), ensure_ascii=False, indent=1)
for m in tmap: print(f'{m["dst0"]:6.2f} +{m["dur"]:.2f}  ' + " ".join(segs[s]["text"].strip() for s in m["segs"]))
print("voice end", round(pos, 2))
