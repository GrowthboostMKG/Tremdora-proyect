import json, math, subprocess, sys, os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont

U = "/root/.claude/uploads/9fabe8a0-8107-516d-9495-8cf23d88ccf5/"
S = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
OFF = 0.30            # narration starts at 0.30 s
TOTAL = 88.8
FONT = S + "/npmf/package/files/montserrat-latin-600-normal.woff"

def img(n): return U + n + "-image.jpg"
def mov(n):
    for f in os.listdir(U):
        if f.startswith(n) and f.endswith(".mov"): return U + f

# ---------------------------------------------------------------- shots
# boundaries in narration time; shot i spans B[i]..B[i+1]
B = [-OFF, 4.15, 6.50, 9.50, 12.10, 15.00, 20.65, 25.25, 31.10, 34.25, 37.50, 40.40,
     44.10, 49.48, 54.85, 59.25, 62.15, 64.45, 67.00, 70.25, 74.55, TOTAL - OFF]
# transition INTO shot i (type, duration)
# kind: image -> cam0, cam1 = (cx, cy, zoom); video -> src_start, speed, crop(l,t,r,b), cam0, cam1
SHOTS = [
 dict(src=img("e2e26db4"), cam0=(.43,.55,1.95), cam1=(.425,.54,2.35), tr=None, w=0.0, sat=.9),          # hook eyes
 dict(src=img("9062e00e"), cam0=(.58,.37,1.75), cam1=(.585,.365,1.9), tr=("cut",0), w=0.0),               # match cut eye
 dict(src=img("50130dc3"), cam0=(.52,.48,1.0), cam1=(.54,.47,1.08), tr=("cut",0), w=-.1),                 # maltese + owner
 dict(src=mov("a0d33277"), ss=0.0, speed=.5, cam0=(.56,.5,1.0), cam1=(.57,.48,1.06), tr=("dissolve",.4), w=.15, sat=.85),
 dict(src=img("810b155e"), cam0=(.5,.42,1.12), cam1=(.52,.40,1.22), tr=("cut",0), w=0.0),
 dict(src=img("90085c87"), cam0=(.48,.55,1.0), cam1=(.40,.45,1.18), tr=("focus",1.0), w=0.0),            # pause: waiting at the door
 dict(src=mov("b63db83f"), ss=0.1, speed=.74, cam0=(.5,.45,1.0), cam1=(.47,.42,1.08), tr=("light",.8), w=-.15),
 dict(src=img("53d6fb3d"), cam0=(.60,.62,1.05), cam1=(.66,.66,1.28), tr=("dissolve",.6), w=0.0),
 dict(src=mov("5c111bb6"), ss=1.3, speed=1.0, cam0=(.5,.5,1.0), cam1=(.52,.5,1.05), tr=("cut",0), w=-.55, sat=.82),
 dict(src=mov("91404d20"), ss=0.0, speed=1.0, cam0=(.5,.5,1.0), cam1=(.5,.48,1.05), tr=("dissolve",.5), w=-.45, sat=.82),
 dict(src=img("e2e26db4"), cam0=(.5,.56,1.12), cam1=(.5,.56,1.0), tr=("cut",0), w=-.1, sat=.8),           # callback: pull-out
 dict(src=img("50130dc3"), cam0=(.64,.40,1.75), cam1=(.65,.41,1.85), tr=("focus",.8), w=0.0),             # her face: guilt
 dict(src=img("b5e97078"), cam0=(.5,.55,1.0), cam1=(.52,.56,1.07), tr=("light",.8), w=0.0),
 dict(src=img("b5e97078"), cam0=(.60,.57,1.75), cam1=(.60,.575,1.9), tr=("cut",0), w=0.0),                # cut-in puppy
 dict(src=img("9062e00e"), cam0=(.62,.50,1.05), cam1=(.64,.48,1.16), tr=("dissolve",.7), w=0.0),          # hands cradling: care
 dict(src=mov("a0d33277"), ss=1.4, speed=.86, cam0=(.57,.48,1.06), cam1=(.58,.47,1.12), tr=("light",.8), w=.1, sat=.85),
 dict(src=mov("ba01271f"), ss=0.4, speed=1.0, crop=(0,0,0,14), cam0=(.5,.55,1.0), cam1=(.5,.55,1.05), tr=("cut",0), w=.15, sat=.72),
 dict(src=mov("5c111bb6"), ss=0.0, speed=.49, cam0=(.58,.5,1.06), cam1=(.6,.5,1.12), tr=("cut",0), w=-.55, sat=.82),
 dict(src=mov("da7097f4"), ss=0.0, speed=.41, crop=(14,4,14,20), cam0=(.55,.45,1.0), cam1=(.57,.42,1.08), tr=("dissolve",.5), w=-.1, sat=.85),
 dict(src=img("886b9d96"), cam0=(.52,.50,1.0), cam1=(.55,.53,1.22), tr=("dissolve",.6), w=-.3, sat=.88),
 dict(src=mov("ee798865"), ss=0.0, speed=.36, cam0=(.5,.5,1.0), cam1=(.5,.45,1.12), tr=("light",1.0), w=-.25),
]
for i, sh in enumerate(SHOTS):
    sh["a"] = B[i] + OFF; sh["b"] = B[i + 1] + OFF

def global_warmth(t):
    n = t - OFF
    k = [(-1, -.32), (38, -.32), (44, -.15), (52, .15), (62, .42), (90, .48)]
    for (x0, y0), (x1, y1) in zip(k, k[1:]):
        if x0 <= n <= x1:
            u = (n - x0) / (x1 - x0); u = u * u * (3 - 2 * u)
            return y0 + (y1 - y0) * u
    return k[-1][1]

# ---------------------------------------------------------------- sources
_img_cache = {}
def load_image(p):
    if p not in _img_cache:
        im = Image.open(p).convert("RGB")
        im = im.filter(ImageFilter.UnsharpMask(radius=1.4, percent=35, threshold=2))
        _img_cache[p] = im
    return _img_cache[p]

def ease(u):
    u = min(max(u, 0.0), 1.0)
    return 0.55 * u + 0.45 * (0.5 - 0.5 * math.cos(math.pi * u))

def frame_from(im, cam):
    w, h = im.size
    cx, cy, z = cam
    s = max(W / w, H / h) * z
    ww, hh = W / s, H / s
    x0 = min(max(cx * w - ww / 2, 0), w - ww)
    y0 = min(max(cy * h - hh / 2, 0), h - hh)
    return im.transform((W, H), Image.AFFINE, (1 / s, 0, x0, 0, 1 / s, y0), resample=Image.BICUBIC)

class VideoReader:
    def __init__(self, path, crop, t_start):
        info = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                        "stream=width,height,r_frame_rate:format=duration", "-of", "json", path])
        j = json.loads(info); st = j["streams"][0]
        n, d = st["r_frame_rate"].split("/"); self.fps = float(n) / float(d)
        self.dur = float(j["format"]["duration"])
        l, t, r, b = crop
        self.w, self.h = st["width"] - l - r, st["height"] - t - b
        self.t0 = max(0.0, t_start)
        vf = f"crop={self.w}:{self.h}:{l}:{t},format=rgb24"
        self.p = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", f"{self.t0:.4f}", "-i", path, "-vf", vf,
                                   "-vsync", "0", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
        self.k = -1; self.prev = None; self.cur = None; self.eof = False
        self.size = self.w * self.h * 3
    def _read(self):
        buf = self.p.stdout.read(self.size)
        if len(buf) < self.size:
            self.eof = True; return False
        self.prev = self.cur
        self.cur = np.frombuffer(buf, np.uint8).reshape(self.h, self.w, 3)
        self.k += 1; return True
    def get(self, ts, blend):
        # frame index relative to t0 (fractional)
        f = (ts - self.t0) * self.fps
        f = max(f, 0.0)
        while not self.eof and self.k < math.floor(f) + (1 if blend else 0):
            if not self._read(): break
        if self.cur is None: self._read()
        if blend and self.prev is not None and not self.eof:
            fr = f - (self.k - 1)
            fr = min(max(fr, 0.0), 1.0)
            a = self.prev.astype(np.float32) * (1 - fr) + self.cur.astype(np.float32) * fr
            return Image.fromarray(a.astype(np.uint8))
        return Image.fromarray(self.cur)

_readers = {}
def shot_frame(i, t):
    sh = SHOTS[i]
    u = ease((t - sh["a"]) / (sh["b"] - sh["a"]))
    cam = tuple(c0 + (c1 - c0) * u for c0, c1 in zip(sh["cam0"], sh["cam1"]))
    if sh["src"].endswith(".jpg"):
        im = load_image(sh["src"])
    else:
        ts = sh["ss"] + (t - sh["a"]) * sh["speed"]
        if i not in _readers:
            _readers[i] = VideoReader(sh["src"], sh.get("crop", (0, 0, 0, 0)), ts)
        rd = _readers[i]
        ts = min(max(ts, 0), rd.dur - 0.03)
        im = rd.get(ts, sh["speed"] < 0.95)
    return frame_from(im, cam)

# ---------------------------------------------------------------- grade
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
rr = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H * 0.47) / (H * 0.62)) ** 2)
VIG = (1 - 0.30 * np.clip(rr - 0.35, 0, 1) ** 1.6)[..., None].astype(np.float32)
rng = np.random.default_rng(7)
GRAIN = [rng.normal(0, 0.011, (H // 2, W // 2)).astype(np.float32) for _ in range(6)]
GRAIN = [np.repeat(np.repeat(g, 2, 0), 2, 1)[..., None] for g in GRAIN]
LUMA = np.array([0.2126, 0.7152, 0.0722], np.float32)

def grade(im, warm, sat):
    x = np.asarray(im, np.float32) / 255.0
    lum = x @ LUMA
    x = lum[..., None] + (x - lum[..., None]) * sat
    # gentle filmic contrast + lifted, warm blacks
    x = np.clip(x, 0, 1)
    x = x + 0.10 * x * (1 - x) * (2 * x - 1) * -1.0  # soften extremes slightly
    x = 0.022 + x * 0.965
    gain = np.array([1 + 0.055 * warm, 1 + 0.018 * warm, 1 - 0.075 * warm], np.float32)
    x = x * gain
    # cream highlights, chocolate shadows (the Tremdora palette)
    lum = (x @ LUMA)[..., None]
    x = x + (np.array([0.012, 0.006, -0.010], np.float32) * np.clip(lum - 0.6, 0, 1) * 2.5)
    x = x + (np.array([0.010, 0.004, -0.004], np.float32) * np.clip(0.35 - lum, 0, 1) * 2.0)
    return x

# ---------------------------------------------------------------- captions
WORDS = [w for s in json.load(open(S + "/words.json")) for w in s["words"]]
CAPS = [
 (0, 9, "Si el veterinario te dice que llegó la hora", "llegó la hora"),
 (9, 14, "de despedirte de tu mascota,", None),
 (14, 19, "no salgas de esa sala.", "no salgas de esa sala."),
 (19, 24, "Tu presencia lo cambia todo.", "lo cambia todo."),
 (24, 28, "Te explico por qué.", None),
 (28, 33, "Muchos veterinarios cuentan lo mismo.", None),
 (33, 38, "Cuando el dueño se va,", None),
 (38, 48, "el animal lo busca con la mirada hasta el final.", "hasta el final."),
 (48, 53, "El oído y el olfato", None),
 (53, 61, "son de los últimos sentidos que se apagan.", None),
 (61, 66, "Aunque ya casi no vea,", None),
 (66, 77, "tu voz y tu mano le dicen que está a salvo.", "está a salvo."),
 (77, 79, "Háblale bajito,", None),
 (79, 84, "acarícialo donde siempre le gustó", None),
 (84, 92, "y deja cerca una prenda con tu olor.", None),
 (92, 99, "Pero eso no es lo más difícil.", None),
 (99, 108, "Lo más difícil es la culpa que viene después.", "la culpa"),
 (108, 113, "Si ya tomaste esa decisión,", None),
 (113, 117, "escúchame, no lo abandonaste.", "no lo abandonaste."),
 (117, 122, "Cargaste tú con el dolor", None),
 (122, 129, "para que él no tuviera que cargar", None),
 (129, 134, "con el sufrimiento de mañana.", None),
 (134, 138, "Eso no es rendirse.", None),
 (138, 144, "Es el último acto de cuidado.", "último acto de cuidado."),
 (144, 152, "Y hay algo que quizá nadie te dijo.", None),
 (152, 159, "Tú tuviste muchas cosas en tu vida.", None),
 (159, 165, "Él solo te tuvo a ti.", "Él solo te tuvo a ti."),
 (165, 171, "Fuiste su casa, su mundo entero.", None),
 (171, 174, "No le fallaste.", "No le fallaste."),
 (174, 183, "Se fue en los brazos de quien más amaba.", "quien más amaba."),
 (183, 191, "Si alguien que conoces está pasando por esto,", None),
 (191, 194, "mándale este video.", None),
 (194, 200, "Nadie debería pasar un duelo solo.", "un duelo solo."),
 (200, 202, "Comenta MUESTRA", "MUESTRA"),
 (202, 212, "y te envío gratis un adelanto de mis e-books.", None),
]
IVORY = (255, 249, 240); GOLD = (242, 212, 122)
CAP_BOTTOM = H - 270          # bottom of text block (inside IG safe zone)

def render_caption(text, hl):
    toks = text.split(" ")
    hl_set = set()
    if hl:
        ht = hl.split(" ")
        for i in range(len(toks) - len(ht) + 1):
            if toks[i:i + len(ht)] == ht: hl_set.update(range(i, i + len(ht)))
    for size in (58, 54, 50, 48):
        f = ImageFont.truetype(FONT, size)
        sp = f.getlength(" ")
        widths = [f.getlength(t) for t in toks]
        def lw(a, b): return sum(widths[a:b]) + sp * (b - a - 1)
        if lw(0, len(toks)) <= 900:
            lines = [(0, len(toks))]
        else:
            best = min(range(1, len(toks)), key=lambda k: max(lw(0, k), lw(k, len(toks))))
            lines = [(0, best), (best, len(toks))]
        if max(lw(a, b) for a, b in lines) <= 960: break
    lh = int(size * 1.28)
    pad = 40
    ch = lh * len(lines) + 2 * pad
    txt = Image.new("RGBA", (W, ch), (0, 0, 0, 0)); d = ImageDraw.Draw(txt)
    mask = Image.new("L", (W, ch), 0); dm = ImageDraw.Draw(mask)
    for li, (a, b) in enumerate(lines):
        x = (W - lw(a, b)) / 2; y = pad + li * lh
        for k in range(a, b):
            col = GOLD if k in hl_set else IVORY
            d.text((x, y), toks[k], font=f, fill=col + (255,))
            dm.text((x, y), toks[k], font=f, fill=255)
            x += widths[k] + sp
    # subtle shadow: tight + soft
    sh1 = mask.filter(ImageFilter.GaussianBlur(3)); sh2 = mask.filter(ImageFilter.GaussianBlur(14))
    sa = np.clip(np.asarray(sh1, np.float32) / 255 * 0.55 + np.asarray(sh2, np.float32) / 255 * 0.35, 0, 1)
    sa = np.roll(sa, 2, axis=0)
    t = np.asarray(txt, np.float32) / 255
    ta = t[..., 3:4]
    # composite text over shadow (shadow color warm near-black)
    alpha = ta + sa[..., None] * (1 - ta)
    rgb = t[..., :3] * ta + np.array([0.08, 0.06, 0.05], np.float32) * sa[..., None] * (1 - ta)
    return rgb, alpha, CAP_BOTTOM - ch + pad   # premultiplied rgb, alpha, top y

CAPTIONS = []
for ci, (a, b, text, hl) in enumerate(CAPS):
    st = WORDS[a]["s"] - 0.06 + OFF
    end_word = WORDS[b - 1]["e"] + OFF
    nxt = WORDS[CAPS[ci + 1][0]]["s"] - 0.06 + OFF if ci + 1 < len(CAPS) else TOTAL
    en = min(nxt - 0.02, end_word + 0.65)
    CAPTIONS.append(dict(st=st, en=en, text=text, hl=hl))
_cap_cache = {}

def overlay_captions(x, t):
    for ci, c in enumerate(CAPTIONS):
        if c["st"] <= t < c["en"]:
            if ci not in _cap_cache: _cap_cache[ci] = render_caption(c["text"], c["hl"])
            rgb, al, y0 = _cap_cache[ci]
            fi = min(1.0, (t - c["st"]) / 0.15)
            fo = min(1.0, (c["en"] - t) / 0.12)
            k = min(fi, fo); k = k * k * (3 - 2 * k)
            rise = int(round((1 - fi) * 6))
            y = y0 + rise
            reg = x[y:y + rgb.shape[0]]
            x[y:y + rgb.shape[0]] = reg * (1 - al * k) + rgb * k
    return x

# ---------------------------------------------------------------- compose
def shot_graded(i, t):
    sh = SHOTS[i]
    return grade(shot_frame(i, t), global_warmth(t) + sh.get("w", 0), 0.9 * sh.get("sat", 1.0))

def compose(t):
    i = max(k for k in range(len(SHOTS)) if SHOTS[k]["a"] <= t or k == 0)
    # incoming transition into shot i+1 starting before its boundary?
    out = None
    if i + 1 < len(SHOTS):
        typ, d = SHOTS[i + 1]["tr"]
        if d and t >= SHOTS[i + 1]["a"] - d / 2: i, inc = i + 1, True
    typ, d = SHOTS[i]["tr"] or ("cut", 0)
    T = SHOTS[i]["a"]
    if d and abs(t - T) < d / 2:
        u = (t - (T - d / 2)) / d
        s = u * u * (3 - 2 * u)
        if typ == "focus":
            r_out = 16 * min(1, u * 2); r_in = 16 * max(0, 1 - (u - 0.5) * 2) if u > 0.5 else 16
            A = shot_frame(i - 1, t).filter(ImageFilter.GaussianBlur(r_out)) if u < 0.75 else None
            Bf = shot_frame(i, t).filter(ImageFilter.GaussianBlur(r_in)) if u > 0.25 else None
            sh0, sh1 = SHOTS[i - 1], SHOTS[i]
            if A is not None: A = grade(A, global_warmth(t) + sh0.get("w", 0), .9 * sh0.get("sat", 1))
            if Bf is not None: Bf = grade(Bf, global_warmth(t) + sh1.get("w", 0), .9 * sh1.get("sat", 1))
            m = min(max((u - 0.25) / 0.5, 0), 1); m = m * m * (3 - 2 * m)
            out = Bf if A is None else (A if Bf is None else A * (1 - m) + Bf * m)
        else:
            A = shot_graded(i - 1, t); Bf = shot_graded(i, t)
            out = A * (1 - s) + Bf * s
            if typ == "light":
                lift = math.sin(math.pi * u)
                out = out * (1 + 0.10 * lift) + np.array([0.035, 0.028, 0.018], np.float32) * lift
    else:
        out = shot_graded(i, t)
    out = out * VIG
    # gentle fade in from black (first 0.35 s) and to warm dark at the very end
    if t < 0.35: out = out * (t / 0.35)
    if t > TOTAL - 0.9: out = out * max(0.0, (TOTAL - t) / 0.9) ** 1.2
    out = out + GRAIN[int(t * FPS) % len(GRAIN)] * 0.8
    out = overlay_captions(np.clip(out, 0, 1), t)
    return (np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8)

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "still":
        for tt in sys.argv[2:]:
            t = float(tt); _readers.clear()
            Image.fromarray(compose(t)).save(f"{S}/still_{t:06.2f}.jpg", quality=90)
    else:
        f0, f1, outp = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                                "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "slow", "-profile:v", "high",
                                "-pix_fmt", "yuv420p", "-b:v", "20M", "-maxrate", "25M", "-bufsize", "40M",
                                "-g", "60", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
                                outp], stdin=subprocess.PIPE)
        for fi in range(f0, f1):
            enc.stdin.write(compose(fi / FPS).tobytes())
            if fi % 150 == 0: print(outp, fi, flush=True)
        enc.stdin.close(); enc.wait()
