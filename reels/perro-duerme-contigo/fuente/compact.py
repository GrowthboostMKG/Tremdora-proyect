"""Shorten the voiceover: trim long silences, then a gentle pitch-preserving tempo-up. Writes vo_short.wav + timemap.json."""
import json, re, subprocess, wave, numpy as np

SRC = 'vo.mp3'
TARGET_VO = 52.4          # seconds of voice after compaction (+ ~1.9 s logo end card => ~54 s video)
SR = 44100

pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', SRC, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'],
                     capture_output=True).stdout
x = np.frombuffer(pcm, np.float32)
dur = len(x) / SR

log = subprocess.run(['ffmpeg', '-i', SRC, '-af', 'silencedetect=n=-35dB:d=0.3', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
st = [float(v) for v in re.findall(r'silence_start: ([\d.]+)', log)]
en = [float(v) for v in re.findall(r'silence_end: ([\d.]+)', log)]
words = json.load(open('words.json'))

def sentence_end_before(t):
    prev = [w for w in words if w['s'] < t]
    return bool(prev) and prev[-1]['w'].strip().endswith('.')

keep, cur = [], 0.0
for a, b in zip(st, en):
    if a < 0.05: continue
    tgt = 0.45 if sentence_end_before(b) else 0.30
    if b - a > tgt:
        keep.append((cur, a + tgt / 2))
        cur = b - tgt / 2
keep.append((cur, dur))

# concatenate with short crossfades
fade = int(0.012 * SR)
out = np.zeros(0, np.float32)
for a, b in keep:
    seg = x[int(a * SR):int(b * SR)].copy()
    if len(out) and len(seg) > fade:
        ramp = np.linspace(0, 1, fade, dtype=np.float32)
        out[-fade:] = out[-fade:] * (1 - ramp) + seg[:fade] * ramp
        seg = seg[fade:]
    out = np.concatenate([out, seg])
trimmed = len(out) / SR
tempo = trimmed / TARGET_VO
with wave.open('vo_trim.wav', 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(out, -1, 1) * 32767).astype('<i2').tobytes())
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'vo_trim.wav', '-af', f'atempo={tempo:.4f}', 'vo_short.wav'], check=True)

json.dump({'keep': keep, 'tempo': tempo, 'fade': fade / SR}, open('timemap.json', 'w'))
print(f'original {dur:.2f}s  trimmed {trimmed:.2f}s  tempo x{tempo:.3f}  final {trimmed / tempo:.2f}s  cuts {len(keep) - 1}')
