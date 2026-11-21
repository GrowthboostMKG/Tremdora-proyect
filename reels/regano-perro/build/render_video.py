"""Renderiza la imagen del Reel (1080x1920, 30 fps) sin texto ni audio.
uso: python3 render_video.py <carpeta_material> <words.json> <salida.mp4>"""
import sys, glob, json, subprocess, numpy as np, cv2
from shots import SHOTS, END
MAT, WORDS, OUT = sys.argv[1:4]
W, H, FPS = 1080, 1920, 30
words = [w for s in json.load(open(WORDS)) for w in s["words"]]
def word_t(token):
    return next(w["s"] for w in words if w["w"].strip().lower().startswith(token)) - 0.08
for s in SHOTS:
    if isinstance(s["t"], str): s["t"] = round(word_t(s["t"]), 2)
for i, s in enumerate(SHOTS):
    s["end"] = SHOTS[i+1]["t"] if i+1 < len(SHOTS) else END
    s["path"] = glob.glob(f"{MAT}/{s['src']}-*")[0]

def window(sw, sh, s, z):
    # mayor ventana 9:16 dentro del área útil, reducida por el zoom, centrada en el foco
    if sw/sh > W/H: bh = sh; bw = sh*W/H
    else: bw = sw; bh = sw*H/W
    ww, wh = bw/z, bh/z
    cx = np.clip(s["cx"]*sw, ww/2, sw-ww/2); cy = np.clip(s["cy"]*sh, wh/2, sh-wh/2)
    return cx-ww/2, cy-wh/2, ww/W

def warp(img, x0, y0, scale):
    M = np.float32([[1/scale, 0, -x0/scale], [0, 1/scale, -y0/scale]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)

def ease(u): return u*u*(3-2*u)

enc = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","bgr24","-s",f"{W}x{H}","-r",str(FPS),
    "-i","-","-c:v","libx264","-preset","medium","-crf","14","-pix_fmt","yuv420p",OUT], stdin=subprocess.PIPE)
total = 0
for s in SHOTS:
    n = int(round(s["end"]*FPS)) - int(round(s["t"]*FPS)); dur = n/FPS
    rect = s.get("rect")
    if s["kind"] == "p":
        img = cv2.imread(s["path"])
        if rect: x,y,w,h = rect; img = img[y:y+h, x:x+w]
        frames = lambda: (img for _ in range(n))
    if s["kind"] == "v":
        cap = cv2.VideoCapture(s["path"]); sfps = cap.get(cv2.CAP_PROP_FPS); cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        inp = s.get("inp", 0.0); avail = cnt/sfps - inp - 0.05
        speed = min(1.0, avail/dur)
        if speed < 1 and avail > dur: speed = 1.0
        s["speed"] = round(speed, 3)
        def frames(cap=cap, sfps=sfps, inp=inp, speed=speed, cnt=cnt, rect=rect):
            buf = {}; pos = -1; last = None
            def get(k):
                nonlocal pos, last
                k = min(k, cnt-1)
                while pos < k:
                    ok, f = cap.read()
                    if not ok: break
                    pos += 1; last = f if not rect else f[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
                    buf[pos] = last
                    for old in [q for q in buf if q < pos-2]: del buf[old]
                return buf.get(k, last)
            for i in range(n):
                st = (inp + i/FPS*speed)*sfps; k = int(st); a = st-k
                f0 = get(k); f1 = get(k+1)
                yield f0 if (a < 0.05 or f1 is None) else cv2.addWeighted(f0, 1-a, f1, a, 0)
    for i, f in enumerate(frames()):
        sh_, sw_ = f.shape[:2]
        z = s["z0"] + (s["z1"]-s["z0"])*ease(i/max(1, n-1))
        x0, y0, sc = window(sw_, sh_, s, z)
        enc.stdin.write(warp(f, x0, y0, sc).tobytes())
    total += n
    print(f'{s["t"]:6.2f}-{s["end"]:6.2f} {s["src"]} {s["kind"]} speed={s.get("speed","-")}', flush=True)
enc.stdin.close(); enc.wait()
json.dump([{k: s[k] for k in ("t","end","src","note")} for s in SHOTS], open(OUT.rsplit(".",1)[0]+"_edl.json","w"), ensure_ascii=False, indent=1)
print("frames", total, total/FPS)
