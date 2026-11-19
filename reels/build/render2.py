"""TREMDORA reel #2 — 'El color vuelve'. Same narration, new visual language."""
import json, math, subprocess, sys, os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont

U = "/root/.claude/uploads/9fabe8a0-8107-516d-9495-8cf23d88ccf5/"
S = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
OFF = 0.30
TOTAL = 88.8
FONT = S + "/npmf/package/files/montserrat-latin-600-normal.woff"

def img(n): return U + n + "-image.jpg"
def mov(n):
    for f in os.listdir(U):
        if f.startswith(n) and f.endswith(".mov"): return U + f

def V(name, ss, speed, cam0, cam1, crop=(0, 0, 0, 0)):
    return dict(src=mov(name), ss=ss, speed=speed, cam0=cam0, cam1=cam1, crop=crop)
def I(name, cam0, cam1):
    return dict(src=img(name), cam0=cam0, cam1=cam1)

# narration-time boundaries
B = [-OFF, 4.15, 6.50, 9.50, 12.10, 15.00, 20.65, 25.25, 31.10, 34.25, 37.50,
     44.10, 49.48, 54.85, 59.25, 62.15, 67.00, 70.25, 79.00, TOTAL - OFF]
SHOTS = [
 dict(V("953e0d36", 0.0, .88, (.55, .5, 1.05), (.6, .47, 1.22)), tr=None),                         # hook: the eye
 dict(I("9eacdc71", (.38, .34, 1.45), (.38, .335, 1.62)), tr=("blink", .7)),                       # Jack Russell held
 dict(I("50130dc3", (.53, .48, 1.0), (.55, .47, 1.07)), tr=("cut", 0)),                            # presence
 dict(I("9062e00e", (.55, .42, 1.22), (.57, .40, 1.34)), tr=("wipe", .8, (1, 0))),                 # eye contact
 dict(V("0a12c4bb", 0.4, 1.0, (.5, .45, 1.0), (.5, .43, 1.06)), tr=("cut", 0)),                    # the vet
 dict(I("90085c87", (.48, .55, 1.0), (.40, .44, 1.17)), tr=("blink", .8)),                         # waiting at the door
 dict(V("b63db83f", 0.1, .74, (.5, .45, 1.0), (.47, .42, 1.08)), tr=("zoom", .7)),                 # hearing / smell
 dict(I("53d6fb3d", (.58, .60, 1.04), (.65, .66, 1.26)), tr=("sweep", 1.0, (1, -1))),              # your hand
 dict(V("91404d20", 0.0, 1.0, (.42, .5, 1.04), (.44, .48, 1.09)), tr=("cut", 0)),                  # talk to him softly
 dict(V("5c111bb6", 1.3, 1.0, (.55, .5, 1.0), (.57, .5, 1.05)), tr=("wipe", .8, (0, -1))),         # blanket / scent
 dict(V("437098cd", 0.0, .14, (.5, .55, 1.0), (.5, .58, 1.10)), tr=("dip", .9)),                    # the empty bed
 dict(I("b5e97078", (.55, .55, 1.0), (.56, .56, 1.10)), tr=("zoom", .7)),                          # not abandoned
 dict(I("e2e26db4", (.45, .55, 1.08), (.44, .55, 1.24)), tr=("cut", 0)),                           # you carried the pain
 dict(I("810b155e", (.52, .40, 1.10), (.53, .38, 1.20)), tr=("dissolve", .7)),                     # last act of care
 dict(V("a0d33277", 0.5, 1.0, (.56, .5, 1.02), (.58, .48, 1.08)), tr=("sweep", 1.0, (-1, -1))),
 dict(kind="diptych", A=V("ba01271f", 0.3, 1.0, (.5, .5, 1.0), (.5, .5, 1.04), crop=(0, 0, 0, 14)),
      Bv=V("da7097f4", 0.0, .28, (.55, .45, 1.0), (.57, .42, 1.06), crop=(14, 4, 14, 20)),
      split_end=64.45 + OFF - 0.1, tr=("cut", 0)),
 dict(I("886b9d96", (.52, .50, 1.0), (.55, .52, 1.16)), tr=("dissolve", .6)),                      # his home
 dict(V("ee798865", 0.0, .48, (.5, .5, 1.0), (.5, .46, 1.10)), tr=("dip", .8)),                    # in your arms
 dict(I("0c9f3887", (.5, .58, 1.0), (.55, .40, 1.22)), tr=("sweep", 1.2, (0, -1))),                # closing
]
for i, sh in enumerate(SHOTS):
    sh["a"] = B[i] + OFF; sh["b"] = B[i + 1] + OFF

def curve(t, keys):
    n = t - OFF
    for (x0, y0), (x1, y1) in zip(keys, keys[1:]):
        if x0 <= n <= x1:
            u = (n - x0) / (x1 - x0); u = u * u * (3 - 2 * u)
            return y0 + (y1 - y0) * u
    return keys[-1][1] if n > keys[-1][0] else keys[0][1]
# 'El color vuelve': near-monochrome at the start, colour returns with the story
def sat_at(t): return curve(t, [(-1, .30), (8, .32), (15, .45), (36, .62), (38, .48), (47, .55), (58, .85), (63, 1.0), (90, 1.02)])
def warm_at(t): return curve(t, [(-1, -.18), (15, -.15), (36, 0), (44, -.08), (58, .25), (66, .45), (90, .5)])
def letterbox_at(t):
    a, b = SHOTS[10]["a"], SHOTS[12]["a"]
    if t < a or t > b + 0.9: return 0.0
    u = min((t - a) / 0.9, 1.0) if t < a + 0.9 else (1.0 if t < b - 0.2 else max(0.0, 1 - (t - (b - 0.2)) / 1.1))
    return u * u * (3 - 2 * u)

# ------------------------------------------------------------------ sources
_img_cache = {}
def load_image(p):
    if p not in _img_cache:
        im = Image.open(p).convert("RGB")
        _img_cache[p] = im.filter(ImageFilter.UnsharpMask(radius=1.4, percent=35, threshold=2))
    return _img_cache[p]

def ease(u):
    u = min(max(u, 0.0), 1.0)
    return 0.55 * u + 0.45 * (0.5 - 0.5 * math.cos(math.pi * u))

def frame_from(im, cam, size=(W, H)):
    w, h = im.size; tw, th = size
    cx, cy, z = cam
    s = max(tw / w, th / h) * z
    ww, hh = tw / s, th / s
    x0 = min(max(cx * w - ww / 2, 0), w - ww)
    y0 = min(max(cy * h - hh / 2, 0), h - hh)
    return im.transform((tw, th), Image.AFFINE, (1 / s, 0, x0, 0, 1 / s, y0), resample=Image.BICUBIC)

class VideoReader:
    def __init__(self, path, crop, t_start):
        j = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height,r_frame_rate:format=duration", "-of", "json", path]))
        st = j["streams"][0]; n, d = st["r_frame_rate"].split("/"); self.fps = float(n) / float(d)
        self.dur = float(j["format"]["duration"])
        l, t, r, b = crop
        self.w, self.h = st["width"] - l - r, st["height"] - t - b
        self.t0 = max(0.0, min(t_start, self.dur - 0.12) - 0.05)
        self.p = subprocess.Popen(["ffmpeg", "-v", "quiet", "-ss", f"{self.t0:.4f}", "-i", path, "-vf",
                                   f"crop={self.w}:{self.h}:{l}:{t},format=rgb24", "-vsync", "0", "-f", "rawvideo", "-"],
                                  stdout=subprocess.PIPE)
        self.k = -1; self.prev = self.cur = None; self.eof = False; self.size = self.w * self.h * 3
    def _read(self):
        buf = self.p.stdout.read(self.size)
        if len(buf) < self.size: self.eof = True; return False
        self.prev = self.cur; self.cur = np.frombuffer(buf, np.uint8).reshape(self.h, self.w, 3); self.k += 1
        return True
    def get(self, ts, blend):
        f = max((ts - self.t0) * self.fps, 0.0)
        while not self.eof and self.k < math.floor(f) + (1 if blend else 0):
            if not self._read(): break
        if self.cur is None: self._read()
        if blend and self.prev is not None and not self.eof:
            fr = min(max(f - (self.k - 1), 0.0), 1.0)
            return Image.fromarray((self.prev * (1 - fr) + self.cur * fr).astype(np.uint8))
        return Image.fromarray(self.cur)

_readers = {}
def clip_frame(key, c, a, b, t, size=(W, H), zmul=1.0):
    u = ease((t - a) / (b - a))
    cx, cy, z = (c0 + (c1 - c0) * u for c0, c1 in zip(c["cam0"], c["cam1"]))
    if c["src"].endswith(".jpg"):
        im = load_image(c["src"])
    else:
        ts = c["ss"] + (t - a) * c["speed"]
        if key not in _readers: _readers[key] = VideoReader(c["src"], c.get("crop", (0, 0, 0, 0)), max(ts, 0))
        rd = _readers[key]
        im = rd.get(min(max(ts, 0), rd.dur - 0.03), c["speed"] < 0.95)
    return frame_from(im, (cx, cy, z * zmul), size)

# ------------------------------------------------------------------ grade
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
rr = np.sqrt(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H * 0.47) / (H * 0.62)) ** 2)
VIG = (1 - 0.30 * np.clip(rr - 0.35, 0, 1) ** 1.6)[..., None].astype(np.float32)
YN = (yy / H)[..., None]; XN = (xx / W)[..., None]
rng = np.random.default_rng(7)
GRAIN = [np.repeat(np.repeat(rng.normal(0, 0.012, (H // 2, W // 2)).astype(np.float32), 2, 0), 2, 1)[..., None] for _ in range(6)]
LUMA = np.array([0.2126, 0.7152, 0.0722], np.float32)

def grade(im, t, sat_mul=1.0, warm_add=0.0):
    x = np.asarray(im, np.float32) / 255.0
    sat = sat_at(t) * sat_mul; warm = warm_at(t) + warm_add
    lum = (x @ LUMA)[..., None]
    # monochrome part keeps a faint warm-silver tint (never cold blue)
    mono = lum * np.array([1.015, 1.0, 0.975], np.float32)
    x = mono + (x - lum) * sat
    x = np.clip(x, 0, 1)
    x = x - 0.10 * x * (1 - x) * (2 * x - 1)
    x = 0.024 + x * 0.962
    x = x * np.array([1 + 0.055 * warm, 1 + 0.018 * warm, 1 - 0.075 * warm], np.float32)
    lum = (x @ LUMA)[..., None]
    x = x + np.array([0.012, 0.006, -0.010], np.float32) * np.clip(lum - 0.6, 0, 1) * 2.5
    x = x + np.array([0.010, 0.004, -0.004], np.float32) * np.clip(0.35 - lum, 0, 1) * 2.0
    return x

# per-source corrections (tame strong oranges / saturated skies so all feel like one film)
FIX = {"5c111bb6": (.82, -.5), "91404d20": (.82, -.4), "ba01271f": (.72, .15), "da7097f4": (.85, -.1),
       "a0d33277": (.85, .15), "ee798865": (1.0, -.25), "886b9d96": (.88, -.3), "0c9f3887": (.9, -.25),
       "b63db83f": (1.0, -.15), "437098cd": (1.0, .05), "953e0d36": (1.0, -.1)}
def fix_of(c):
    for k, v in FIX.items():
        if k in c["src"]: return v
    return (1.0, 0.0)

def render_shot(i, t, zmul=1.0):
    sh = SHOTS[i]
    if sh.get("kind") == "diptych":
        return render_diptych(i, t)
    sm, wa = fix_of(sh)
    return grade(clip_frame(i, sh, sh["a"], sh["b"], t, zmul=zmul), t, sm, wa)

GAP = 8
def render_diptych(i, t):
    sh = SHOTS[i]; a, b = sh["a"], sh["b"]; se = sh["split_end"]
    # top panel (her life) shrinks away; bottom panel (him) expands to the whole frame
    u = min(max((t - se) / 0.9, 0), 1); u = u * u * (3 - 2 * u)
    half = (H - GAP) // 2
    top_h = int(round(half * (1 - u)))
    canvas = np.empty((H, W, 3), np.float32); canvas[:] = np.array([0.93, 0.89, 0.82], np.float32)  # cream divider
    if top_h > 4:
        A = sh["A"]; sm, wa = fix_of(A)
        ta = grade(clip_frame((i, "A"), A, a, b, t, (W, top_h)), t, sm, wa) * (1 - 0.45 * u)
        canvas[:top_h] = ta
    y0 = top_h + int(round(GAP * (1 - u)))
    Bc = sh["Bv"]; sm, wa = fix_of(Bc)
    canvas[y0:] = grade(clip_frame((i, "B"), Bc, a, b, t, (W, H - y0)), t, sm, wa)
    return canvas

# ------------------------------------------------------------------ transitions
def smooth(u): u = min(max(u, 0), 1); return u * u * (3 - 2 * u)
DARK = np.array([0.02, 0.016, 0.012], np.float32)

def transition(i, t, typ, d, extra):
    T = SHOTS[i]["a"]; u = (t - (T - d / 2)) / d; s = smooth(u)
    if typ == "blink":                       # an eyelid closing and opening
        c = smooth(u / 0.45) if u < 0.45 else (1.0 if u < 0.55 else 1 - smooth((u - 0.55) / 0.45))
        base = render_shot(i - 1, t) if u < 0.5 else render_shot(i, t)
        e = c * (0.5 + 0.06)
        dist = np.minimum(YN, 1 - YN)              # distance to nearest edge (0..0.5)
        curve_ = 0.035 * (1 - ((XN - 0.5) * 2) ** 2)  # lid is slightly curved
        m = np.clip((e - dist + curve_ * c) / 0.05, 0, 1)
        return base * (1 - m) + DARK * m
    if typ == "zoom":
        A = render_shot(i - 1, t, zmul=1 + 0.10 * s); Bf = render_shot(i, t, zmul=1 + 0.07 * (1 - s))
        return A * (1 - s) + Bf * s
    if typ == "dip":
        A = render_shot(i - 1, t) if u < 0.45 else None
        Bf = render_shot(i, t) if u > 0.35 else None
        ka = 1 - smooth(u / 0.45); kb = smooth((u - 0.35) / 0.65)
        out = DARK.copy() * np.ones((H, W, 3), np.float32)
        if A is not None: out = out * (1 - ka) + A * ka
        if Bf is not None: out = out * (1 - kb) + Bf * kb
        return out
    A = render_shot(i - 1, t); Bf = render_shot(i, t)
    if typ == "dissolve":
        return A * (1 - s) + Bf * s
    dx, dy = extra
    L = abs(dx) + abs(dy)
    proj = ((XN if dx >= 0 else 1 - XN) * abs(dx) + (YN if dy >= 0 else 1 - YN) * abs(dy)) / L
    f = 0.22 if typ == "wipe" else 0.30
    p = -f + (1 + 2 * f) * smooth(u)
    m = np.clip((p - proj) / f + 0.5, 0, 1); m = m * m * (3 - 2 * m)
    out = A * (1 - m) + Bf * m
    if typ == "sweep":   # a soft band of warm light travels with the reveal
        glow = np.exp(-((proj - p) / 0.12) ** 2) * math.sin(math.pi * u) * 0.22
        out = out + glow * np.array([1.0, 0.86, 0.62], np.float32)
    return out

# ------------------------------------------------------------------ captions (word-by-word reveal)
WORDS = [w for s in json.load(open(S + "/words.json")) for w in s["words"]]
CAPS = [
 (0, 9, "Si el veterinario te dice que llegó la hora", "llegó la hora"),
 (9, 14, "de despedirte de tu mascota,", None),
 (14, 19, "no salgas de esa sala.", "no salgas de esa sala."),
 (19, 24, "Tu presencia lo cambia todo.", "lo cambia todo."),
 (24, 28, "Te explico por qué.", None),
 (28, 33, "Muchos veterinarios cuentan lo mismo.", None),
 (33, 38, "Cuando el dueño se va,", None),
 (38, 48, "el animal lo busca con la mirada hasta el final.", "lo busca con la mirada"),
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
 (171, 174, "No le fallaste.", "HERO"),
 (174, 183, "Se fue en los brazos de quien más amaba.", "quien más amaba."),
 (183, 191, "Si alguien que conoces está pasando por esto,", None),
 (191, 194, "mándale este video.", None),
 (194, 200, "Nadie debería pasar un duelo solo.", "un duelo solo."),
 (200, 202, "Comenta MUESTRA", "MUESTRA"),
 (202, 212, "y te envío gratis un adelanto de mis e-books.", None),
]
IVORY = (255, 249, 240); GOLD = (242, 212, 122)
CAP_BOTTOM = H - 270

def build_caption(text, hl, word_times):
    hero = hl == "HERO"
    toks = text.split(" ")
    hl_set = set(range(len(toks))) if hero else set()
    if hl and not hero:
        ht = hl.split(" ")
        for i in range(len(toks) - len(ht) + 1):
            if toks[i:i + len(ht)] == ht: hl_set.update(range(i, i + len(ht)))
    sizes = (96,) if hero else (58, 54, 50, 48)
    for size in sizes:
        f = ImageFont.truetype(FONT, size); sp = f.getlength(" ")
        widths = [f.getlength(t) for t in toks]
        lw = lambda a, b: sum(widths[a:b]) + sp * (b - a - 1)
        if lw(0, len(toks)) <= 900: lines = [(0, len(toks))]
        else:
            k = min(range(1, len(toks)), key=lambda k: max(lw(0, k), lw(k, len(toks))))
            lines = [(0, k), (k, len(toks))]
        if max(lw(a, b) for a, b in lines) <= 960: break
    lh = int(size * 1.28); pad = 44; ch = lh * len(lines) + 2 * pad
    txt = Image.new("RGBA", (W, ch), (0, 0, 0, 0)); d = ImageDraw.Draw(txt)
    mask = Image.new("L", (W, ch), 0); dm = ImageDraw.Draw(mask)
    boxes = []
    for li, (a, b) in enumerate(lines):
        x = (W - lw(a, b)) / 2; y = pad + li * lh
        for k in range(a, b):
            d.text((x, y), toks[k], font=f, fill=(GOLD if k in hl_set else IVORY) + (255,))
            dm.text((x, y), toks[k], font=f, fill=255)
            boxes.append((int(x) - 18, int(x + widths[k]) + 18, li))
            x += widths[k] + sp
    sh1 = mask.filter(ImageFilter.GaussianBlur(3)); sh2 = mask.filter(ImageFilter.GaussianBlur(16 if hero else 14))
    sa = np.clip(np.asarray(sh1, np.float32) / 255 * 0.55 + np.asarray(sh2, np.float32) / 255 * (0.5 if hero else 0.35), 0, 1)
    sa = np.roll(sa, 2, axis=0)
    tt = np.asarray(txt, np.float32) / 255; ta = tt[..., 3:4]
    alpha = ta + sa[..., None] * (1 - ta)
    rgb = tt[..., :3] * ta + np.array([0.08, 0.06, 0.05], np.float32) * sa[..., None] * (1 - ta)
    top = (H // 2 - ch // 2 - 40) if hero else CAP_BOTTOM - ch + pad
    return dict(rgb=rgb, alpha=alpha, top=top, boxes=boxes, lines=len(lines), lh=lh, pad=pad, hero=hero, times=word_times)

CAPTIONS = []
for ci, (a, b, text, hl) in enumerate(CAPS):
    st = WORDS[a]["s"] - 0.06 + OFF
    nxt = WORDS[CAPS[ci + 1][0]]["s"] - 0.06 + OFF if ci + 1 < len(CAPS) else TOTAL
    en = min(nxt - 0.02, WORDS[b - 1]["e"] + OFF + 0.7)
    times = [WORDS[k]["s"] + OFF - 0.05 for k in range(a, b)]
    if text == "Comenta MUESTRA": times = times[:2]
    CAPTIONS.append(dict(st=st, en=en, text=text, hl=hl, times=times))
_cap = {}

def overlay_captions(x, t):
    for ci, c in enumerate(CAPTIONS):
        if not (c["st"] <= t < c["en"]): continue
        if ci not in _cap: _cap[ci] = build_caption(c["text"], c["hl"], c["times"])
        cp = _cap[ci]; rgb, al = cp["rgb"], cp["alpha"]
        fo = smooth((c["en"] - t) / 0.15)
        if cp["hero"]:
            k = smooth((t - c["st"]) / 0.35) * fo
            amap = np.full(al.shape, k, np.float32)
        else:
            amap = np.zeros(al.shape, np.float32)
            for (x0, x1, li), wt in zip(cp["boxes"], c["times"] + [c["times"][-1]] * 20):
                k = smooth((t - wt) / 0.16) * fo
                y0 = 0 if li == 0 else cp["pad"] + li * cp["lh"] + int(cp["lh"] * 0.12)
                y1 = al.shape[0] if li == cp["lines"] - 1 else cp["pad"] + (li + 1) * cp["lh"] + int(cp["lh"] * 0.12)
                amap[y0:y1, max(0, x0):x1] = np.maximum(amap[y0:y1, max(0, x0):x1], k)
        y = cp["top"]; h = rgb.shape[0]
        reg = x[y:y + h]; a2 = al * amap
        x[y:y + h] = reg * (1 - a2) + rgb * amap
    return x

# ------------------------------------------------------------------ compose
def compose(t):
    i = max([k for k in range(len(SHOTS)) if SHOTS[k]["a"] <= t] + [0])
    if i + 1 < len(SHOTS):
        tr = SHOTS[i + 1]["tr"]
        if tr[1] and t >= SHOTS[i + 1]["a"] - tr[1] / 2: i += 1
    tr = SHOTS[i]["tr"] or ("cut", 0)
    typ, d = tr[0], tr[1]
    if d and abs(t - SHOTS[i]["a"]) < d / 2:
        out = transition(i, t, typ, d, tr[2] if len(tr) > 2 else None)
    else:
        out = render_shot(i, t)
    out = out * VIG
    lb = letterbox_at(t)
    if lb > 0:
        bh = int(round(205 * lb))
        out[:bh] = DARK; out[H - bh:] = DARK
    if t < 0.4: out = out * smooth(t / 0.4)
    if t > TOTAL - 1.0: out = out * smooth((TOTAL - t) / 1.0)
    out = out + GRAIN[int(t * FPS) % len(GRAIN)] * (1.0 - 0.35 * sat_at(t))
    out = overlay_captions(np.clip(out, 0, 1), t)
    return (np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8)

if __name__ == "__main__":
    if sys.argv[1] == "still":
        for tt in sys.argv[2:]:
            t = float(tt); _readers.clear()
            Image.fromarray(compose(t)).save(f"{S}/s2_{t:06.2f}.jpg", quality=90)
    else:
        f0, f1, outp = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                                "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "slow", "-profile:v", "high",
                                "-pix_fmt", "yuv420p", "-b:v", "20M", "-maxrate", "25M", "-bufsize", "40M", "-g", "60",
                                "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", outp],
                               stdin=subprocess.PIPE)
        for fi in range(f0, f1):
            enc.stdin.write(compose(fi / FPS).tobytes())
            if fi % 150 == 0: print(outp, fi, flush=True)
        enc.stdin.close(); enc.wait()
