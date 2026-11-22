"""Versión 1:09: recorta la narración por frases completas y ajusta las pausas.
uso: python3 edit_voice.py <voz.mp3> <words.json> <voz_editada.wav> <words_editadas.json>"""
import sys, json, subprocess, numpy as np, wave
VOICE, WORDS, OUT, OUTW = sys.argv[1:5]; SR = 44100
REMOVE = {11, 14, 18, 19, 22, 23, 24, 26}   # Viena · «Pero aquí no acaba la cosa» · «No es casualidad» + Suecia · experimento EE. UU. · «No sabe.»
GAP = 0.50                           # pausa estándar entre frases
GAP_AFTER = {2: 0.70, 6: 0.95, 7: 0.45, 8: 0.65, 10: 0.55, 16: 0.45, 17: 0.60, 21: 0.65, 25: 0.55, 27: 0.75, 29: 0.40, 30: 0.65}
raw = subprocess.run(["ffmpeg","-v","error","-i",VOICE,"-ar",str(SR),"-ac","1","-f","f32le","-"], capture_output=True).stdout
x = np.frombuffer(raw, np.float32).astype(np.float64)
W = [w for s in json.load(open(WORDS)) for w in s["words"]]
sents, cur = [], []
for w in W:
    cur.append(w)
    if w["w"].strip().endswith((".", "?", "!")): sents.append(cur); cur = []
# bordes reales de cada frase según la energía (no cortar consonantes)
h = int(0.01*SR); rms = np.sqrt(np.convolve(x**2, np.ones(h)/h, "same")); thr = 10**(-48/20)
def edge(t, d, lim):
    i = int(t*SR); stop = int((t + d*lim)*SR)
    while 0 < i < len(x)-1 and (i - stop)*d < 0 and rms[i] > thr: i += d
    return i/SR
out, words, t = [], [], 0.0
keep = [i for i in range(len(sents)) if i not in REMOVE]
for n, i in enumerate(keep):
    s = sents[i]
    a = max(0.0, edge(s[0]["s"], -1, 0.25) - 0.03); b = edge(s[-1]["e"], +1, 0.35) + 0.05
    if n: t += GAP_AFTER.get(keep[n-1], GAP)
    seg = x[int(a*SR):int(b*SR)].copy(); f = int(0.008*SR)
    seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    out.append((t, seg))
    for w in s: words.append({"w": w["w"], "s": t + w["s"] - a, "e": t + w["e"] - a, "sent": i})
    t += len(seg)/SR
y = np.zeros(int((t+0.1)*SR))
for (st, seg) in out: i0 = int(st*SR); y[i0:i0+len(seg)] += seg
with wave.open(OUT, "wb") as wv:
    wv.setnchannels(1); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((np.clip(y, -1, 1)*32767).astype("<i2").tobytes())
json.dump([{"start": words[0]["s"], "end": words[-1]["e"], "text": "", "words": [{"w": w["w"], "s": w["s"], "e": w["e"]} for w in words]}], open(OUTW, "w"), ensure_ascii=False, indent=0)
print("duración voz", round(t, 2))
