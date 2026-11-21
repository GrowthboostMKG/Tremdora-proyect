"""Imagen del Reel 1:09 (1080x1920, 30 fps) con fundidos encadenados y destellos cálidos de luz.
uso: python3 render_video.py <carpeta_material> <salida.mp4>"""
import sys, glob, json, subprocess, numpy as np, cv2
from shots import SHOTS, END
MAT, OUT = sys.argv[1:3]
W, H, FPS = 1080, 1920, 30
for i, s in enumerate(SHOTS):
    s["end"] = SHOTS[i+1]["t"] if i+1 < len(SHOTS) else END
    s["path"] = glob.glob(f"{MAT}/{s['src']}-*")[0]
    s["a"] = s["t"] - s.get("x", 0)/2                                            # inicio real (con fundido)
    s["b"] = s["end"] + (SHOTS[i+1].get("x", 0)/2 if i+1 < len(SHOTS) else 0)    # final real
ease = lambda u: u*u*(3-2*u)

class Source:
    def __init__(s, sh):
        s.sh = sh; s.rect = sh.get("rect"); dur = sh["b"] - sh["a"]
        if sh["kind"] == "p":
            img = cv2.imread(sh["path"]); s.img = img if not s.rect else img[s.rect[1]:s.rect[1]+s.rect[3], s.rect[0]:s.rect[0]+s.rect[2]]
        else:
            s.cap = cv2.VideoCapture(sh["path"]); s.sfps = s.cap.get(cv2.CAP_PROP_FPS); s.cnt = int(s.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            s.inp = sh.get("inp", 0.0); avail = s.cnt/s.sfps - s.inp - 0.05
            if avail < dur: s.inp = max(0, s.inp - (dur - avail)); avail = s.cnt/s.sfps - s.inp - 0.05
            s.speed = min(1.0, avail/dur); s.pos = -1; s.buf = {}; s.last = None
            sh["speed"] = round(s.speed, 3)
    def _get(s, k):
        k = min(k, s.cnt-1)
        while s.pos < k:
            ok, f = s.cap.read()
            if not ok: break
            s.pos += 1; r = s.rect; s.last = f if not r else f[r[1]:r[1]+r[3], r[0]:r[0]+r[2]]; s.buf[s.pos] = s.last
            for q in [q for q in s.buf if q < s.pos-2]: del s.buf[q]
        return s.buf.get(k, s.last)
    def frame(s, t):
        sh = s.sh; u = (t - sh["a"])/(sh["b"] - sh["a"])
        if sh["kind"] == "p": f = s.img
        else:
            st = (s.inp + (t - sh["a"])*s.speed)*s.sfps; k = int(st); a = st - k
            f0 = s._get(k); f1 = s._get(k+1)
            f = f0 if (a < .05 or f1 is None) else cv2.addWeighted(f0, 1-a, f1, a, 0)
        z = sh["z0"] + (sh["z1"]-sh["z0"])*ease(np.clip(u, 0, 1))
        h_, w_ = f.shape[:2]
        if w_/h_ > W/H: bh = h_; bw = h_*W/H
        else: bw = w_; bh = w_*H/W
        ww, wh = bw/z, bh/z
        cx = np.clip(sh["cx"]*w_, ww/2, w_-ww/2); cy = np.clip(sh["cy"]*h_, wh/2, h_-wh/2)
        sc = ww/W; M = np.float32([[1/sc, 0, -(cx-ww/2)/sc], [0, 1/sc, -(cy-wh/2)/sc]])
        return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT).astype(np.float32)

# destello cálido: halo suave que cruza el encuadre en diagonal
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
WARM = np.array([120, 185, 255], np.float32)      # BGR ámbar suave
def leak(p):
    cx = -150 + p*(W+300); cy = H*0.12 + p*H*0.22
    g = np.exp(-(((xx-cx)/430)**2 + ((yy-cy)/600)**2))
    return g[..., None]*WARM

enc = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","bgr24","-s",f"{W}x{H}","-r",str(FPS),
    "-i","-","-c:v","libx264","-preset","medium","-crf","14","-pix_fmt","yuv420p",OUT], stdin=subprocess.PIPE)
srcs = {}
N = int(round(END*FPS))
for i in range(N):
    t = i/FPS
    act = [j for j, s in enumerate(SHOTS) if s["a"] <= t < s["b"]]
    for j in act:
        if j not in srcs: srcs[j] = Source(SHOTS[j])
    for j in [j for j in srcs if j not in act and SHOTS[j]["b"] <= t]: del srcs[j]
    if len(act) == 1: img = srcs[act[0]].frame(t)
    else:
        j0, j1 = act[0], act[-1]; s1 = SHOTS[j1]
        p = ease((t - s1["a"])/(s1["b"] - s1["a"]) if False else (t - s1["a"])/max(1e-3, s1.get("x", .4)))
        p = float(np.clip(p, 0, 1))
        img = srcs[j0].frame(t)*(1-p) + srcs[j1].frame(t)*p
        if s1.get("leak"):
            k = np.sin(np.pi*p)**1.5
            img = 255 - (255-img)*(1 - k*0.24*leak(p)/255)          # mezcla "screen"
    enc.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
for s in SHOTS: print(f'{s["t"]:6.2f}-{s["end"]:6.2f} {s["src"]} speed={s.get("speed","-")}')
json.dump([{k: s[k] for k in ("t","end","src","note")} for s in SHOTS], open(OUT.rsplit(".",1)[0]+"_edl.json","w"), ensure_ascii=False, indent=1)
