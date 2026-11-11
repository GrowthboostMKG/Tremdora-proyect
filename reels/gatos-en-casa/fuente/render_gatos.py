"""Tremdora cat reel: real footage only, gentle camera moves, organic transitions, elegant ivory subtitles (no music)."""
import json, subprocess, sys, math, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

UP = '/root/.claude/uploads/89643bfb-0721-519a-968f-c88117646256/'
W, H, FPS = 1080, 1920, 30
PREVIEW = len(sys.argv) > 1 and sys.argv[1] == 'preview'
TOTAL = 52.54

# file, crop (w,h,x,y)
CLIPS = {
    'P': (UP + '01f3376b-ScreenRecording_11-11-2026_19-05-22_1.mov', (1194, 1734, 6, 2)),
    'Q': (UP + '2997c0d4-ScreenRecording_11-11-2026_19-03-03_1.mov', (1178, 1756, 14, 2)),
    'R': (UP + '3fa87aa7-ScreenRecording_11-11-2026_19-10-18_1.mov', (1194, 2400, 6, 2)),
    'S': (UP + '80801a15-ScreenRecording_11-11-2026_19-09-07_1.mov', (1194, 2072, 6, 2)),
    'T': (UP + '97a676fd-ScreenRecording_11-11-2026_19-07-21_1.mov', (1194, 2022, 6, 2)),
    'U': (UP + 'ac26523e-ScreenRecording_11-11-2026_19-02-38_1.mov', (1194, 2312, 6, 2)),
    'V': (UP + 'ba47764f-ScreenRecording_11-11-2026_19-04-55_1.mp4', (1194, 2280, 6, 4)),     # player bar below cut
    'W': (UP + 'e5093884-ScreenRecording_11-11-2026_19-05-47_1.mov', (1194, 1880, 6, 2)),
    'X': (UP + 'e7ebd55c-ScreenRecording_11-11-2026_19-04-28_1.mov', (1194, 1506, 6, 6)),
    'Y': (UP + 'f561cb1d-ScreenRecording_11-11-2026_19-11-18_1.mov', (1194, 2290, 6, 4)),     # player bar below cut
}

# start, end, clip, src0, src1, zoom0, zoom1, (cx0,cy0), (cx1,cy1)
SEGS = [
    (0.00, 2.95, 'U', 0.0, 2.10, 1.00, 1.09, (0.50, 0.44), (0.50, 0.40)),   # hook: kitten looking at camera, push-in
    (2.95, 7.05, 'Q', 0.0, 3.05, 1.06, 1.00, (0.50, 0.44), (0.48, 0.44)),   # bendición silenciosa: pull-out
    (7.05, 12.75, 'S', 0.0, 4.70, 1.00, 1.08, (0.52, 0.42), (0.58, 0.40)),  # dormir cerca de ti
    (12.75, 16.95, 'W', 0.0, 4.00, 1.04, 1.10, (0.40, 0.42), (0.36, 0.40)), # mal día / no es casualidad
    (16.95, 20.25, 'V', 0.0, 1.80, 1.10, 1.02, (0.50, 0.36), (0.52, 0.38)), # es ciencia
    (20.25, 23.58, 'P', 0.0, 2.20, 1.04, 1.14, (0.52, 0.46), (0.56, 0.44)), # ronroneo close-up
    (23.58, 28.70, 'X', 0.0, 2.24, 1.10, 1.00, (0.58, 0.40), (0.52, 0.44)), # 26,3 Hz / calma
    (28.70, 32.60, 'T', 0.0, 3.00, 1.00, 1.05, (0.50, 0.42), (0.48, 0.42)), # reduce la ansiedad
    (32.60, 36.20, 'T', 3.00, 5.70, 1.22, 1.30, (0.48, 0.30), (0.46, 0.30)),# lealtad (punch-in)
    (36.20, 41.75, 'R', 3.00, 8.50, 1.00, 1.06, (0.50, 0.36), (0.50, 0.34)),# ¿quién dice que son fríos?
    (41.75, 46.85, 'Y', 0.0, 1.70, 1.02, 1.12, (0.52, 0.40), (0.56, 0.34)), # privilegio / afortunado
]
TRANS = [('zoom', .40), ('dissolve', .50), ('slide', .45), ('dissolve', .40), ('focus', .45), ('dissolve', .35),
         ('slide', .40), ('cut', 0), ('zoom', .35), ('dissolve', .55), ('endcard', .60)]
FADE_OUT = 0.3
END_START = 46.85   # Tremdora logo card carries the CTA

def ease(x):
    x = min(max(x, 0.0), 1.0); return x * x * (3 - 2 * x)
def ease_io(x):
    x = min(max(x, 0.0), 1.0); return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2

class Source:
    def __init__(self, i):
        s0, s1, clip = SEGS[i][0], SEGS[i][1], SEGS[i][2]
        tin = TRANS[i - 1][1] / 2 if i > 0 else 0
        tout = TRANS[i][1] / 2
        self.rs, self.re = s0 - tin, s1 + tout
        self.i = i
        f, (cw, ch, cx, cy) = CLIPS[clip]
        src0, src1 = SEGS[i][3], SEGS[i][4]
        dur = self.re - self.rs
        if (src1 - src0) / dur > 1.0: src1 = src0 + dur
        self.speed = (src1 - src0) / dur
        self.w, self.h = cw, ch
        rate = (f"framerate=fps={FPS}:interp_start=0:interp_end=255:scene=100" if self.speed < 0.6 else f"fps={FPS}")
        vf = (f"crop={cw}:{ch}:{cx}:{cy},"
              f"eq=contrast=1.03:saturation=1.04:gamma=1.0,"
              f"colorbalance=rs=0.012:bs=-0.012:rh=0.008:bh=-0.006,"
              f"unsharp=5:5:0.35,setpts=(PTS-STARTPTS)/{self.speed:.5f},{rate}")
        self.cmd = ['ffmpeg', '-v', 'error', '-ss', f'{src0}', '-t', f'{src1 - src0 + 0.05}', '-i', f, '-an',
                    '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
        self.p = None; self.idx = -1; self.frame = None
        self.cover = max(W / cw, H / ch)

    def get(self, t):
        if self.p is None:
            self.p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=10 ** 8)
        want = int((t - self.rs) * FPS + 1e-6)
        while self.idx < want:
            buf = self.p.stdout.read(self.w * self.h * 3)
            if len(buf) < self.w * self.h * 3: break
            self.frame = Image.frombuffer('RGB', (self.w, self.h), buf, 'raw', 'RGB', 0, 1); self.idx += 1
        return self.frame

    def close(self):
        if self.p: self.p.kill(); self.p = None

    def render(self, t, zoom_mul=1.0):
        s = SEGS[self.i]
        u = ease_io((t - self.rs) / (self.re - self.rs))
        z = (s[5] + (s[6] - s[5]) * u) * zoom_mul
        cx = (s[7][0] + (s[8][0] - s[7][0]) * u) * self.w
        cy = (s[7][1] + (s[8][1] - s[7][1]) * u) * self.h
        sc = self.cover * z
        hw, hh = W / 2 / sc, H / 2 / sc
        cx = min(max(cx, hw), self.w - hw); cy = min(max(cy, hh), self.h - hh)
        return self.get(t).transform((W, H), Image.AFFINE, (1 / sc, 0, cx - hw, 0, 1 / sc, cy - hh), resample=Image.BICUBIC)

yy, xx = np.mgrid[0:H, 0:W]
r = np.sqrt(((xx - W / 2) / (W * .62)) ** 2 + ((yy - H / 2) / (H * .62)) ** 2)
VIGNETTE = (1 - 0.18 * np.clip(r - 0.5, 0, 1) ** 1.6)[..., None].astype(np.float32)

# ---------- subtitles ----------
FONT = ImageFont.truetype('Montserrat.ttf', 64)
try: FONT.set_variation_by_axes([600])
except Exception: FONT.set_variation_by_name('SemiBold')
IVORY = (247, 243, 234)
words = json.load(open('words_cut.json'))
for w in words: w['w'] = w['w'].strip()
# merge "26" + ",3"
m = []
for w in words:
    if m and w['w'].startswith(',') and m[-1]['w'].isdigit():
        m[-1]['w'] += w['w']; m[-1]['e'] = w['e']
    else: m.append(dict(w))
words = m

BLOCK_TEXT = [
    "¿Por qué es importante", "tener gatos en casa?",
    "Tener un gato en casa", "es una bendición silenciosa.",
    "¿Te has dado cuenta", "de que siempre eligen", "dormir cerca de ti",
    "cuando estás enfermo, tenso", "o después de un mal día?", "No es casualidad.",
    "Y esto no es misticismo, es ciencia.",
    "El ronroneo vibra", "en una frecuencia media", "de 26,3 hercios",
    "que literalmente calma", "tu sistema nervioso,", "reduce la ansiedad", "y baja la presión arterial.",
    "No necesitan hacer ruido", "para demostrarte su lealtad.",
    "¿Quién dice que los gatos son fríos?", "Es porque simplemente", "nunca has sido elegido por uno.",
    "Si tienes el privilegio", "de compartir tu vida", "con un felino, eres afortunado.",
    "Comparte esto con una persona", "que tenga un gato", "y no olvides seguir este perfil.",
]
blocks, k = [], 0
for txt in BLOCK_TEXT:
    n = len(txt.split()); blocks.append(words[k:k + n]); k += n
assert k == len(words), (k, len(words))
for txt, b in zip(BLOCK_TEXT, blocks):
    got = ' '.join(x['w'] for x in b).lower().replace('¿', '').replace('?', '')
    assert got.replace(',', '').replace('.', '') == txt.lower().replace('¿', '').replace('?', '').replace(',', '').replace('.', ''), (txt, got)
for k, b in enumerate(blocks):
    nxt = blocks[k + 1][0]['s'] if k + 1 < len(blocks) else 99
    b_start = b[0]['s'] - 0.08
    b_end = min(nxt - 0.12, b[-1]['e'] + 0.6, TOTAL - FADE_OUT)
    blocks[k] = dict(words=b, s=b_start, e=b_end, text=BLOCK_TEXT[k])

def wrap(text, maxw=840):
    ws = text.split(); lines = ['']
    for w_ in ws:
        t = (lines[-1] + ' ' + w_).strip()
        if FONT.getlength(t) > maxw and lines[-1]: lines.append(w_)
        else: lines[-1] = t
    if len(lines) == 2 and len(lines[1].split()) == 1 and len(lines[0].split()) > 2:   # balance lines
        a = lines[0].split(); lines = [' '.join(a[:-1]), a[-1] + ' ' + lines[1]]
    return lines

sub_cache = {}
BROWN = (92, 56, 38)
def sub_img(text, brand=False):
    if (text, brand) in sub_cache: return sub_cache[(text, brand)]
    lines = wrap(text); lh = 80; pad = 40
    widths = [FONT.getlength(l) for l in lines]
    im = Image.new('RGBA', (int(max(widths)) + 2 * pad, lh * len(lines) + 2 * pad), (0, 0, 0, 0))
    mask = Image.new('L', im.size, 0); d = ImageDraw.Draw(mask)
    for i, l in enumerate(lines):
        d.text((im.width / 2, pad + i * lh + lh / 2 + 3), l, font=FONT, fill=255, anchor='mm')
    soft = mask.filter(ImageFilter.GaussianBlur(11)).point(lambda v: min(255, int(v * 0.75)))
    near = mask.filter(ImageFilter.GaussianBlur(2.2)).point(lambda v: min(255, int(v * 0.62)))
    sh = Image.new('RGBA', im.size, (10, 8, 6, 0)); sh.putalpha(Image.fromarray(np.maximum(np.asarray(soft), np.asarray(near))))
    if not brand: im = Image.alpha_composite(im, sh)
    d2 = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        d2.text((im.width / 2, pad + i * lh + lh / 2), l, font=FONT, fill=(BROWN if brand else IVORY) + (255,), anchor='mm',
                stroke_width=0 if brand else 1, stroke_fill=(30, 24, 18, 110))
    sub_cache[(text, brand)] = im
    return im

SUB_Y = {}
DEFAULT_Y = 1360      # lower third, above Instagram caption/buttons
def seg_index(t):
    for i, s in enumerate(SEGS):
        if s[0] <= t < s[1]: return i
    return len(SEGS) - 1

def draw_subs(frame, t):
    for b in blocks:
        if b['s'] <= t < b['e']:
            a = min(1, (t - b['s']) / 0.18, (b['e'] - t) / 0.15)
            im = sub_img(b['text'], brand=b['words'][0]['s'] >= END_START)
            if a < 1:
                im = im.copy(); im.putalpha(im.getchannel('A').point(lambda v: int(v * a)))
            y = SUB_Y.get(seg_index(b['words'][0]['s']), DEFAULT_Y)
            frame.alpha_composite(im, (int(W / 2 - im.width / 2), int(y - im.height / 2)))
    return frame

sources = [Source(i) for i in range(len(SEGS))]
for s in sources: print(f"seg {s.i} {SEGS[s.i][2]} speed {s.speed:.2f}", file=sys.stderr)

def grade(img): return np.asarray(img).astype(np.float32) * VIGNETTE

LOGO = Image.open(UP + 'd63984a0-image.jpg').convert('RGB')
PAPER = (241, 232, 224)
def _endcard():
    bw, bh = int(W * 1.06), int(H * 1.06)
    bg = Image.new('RGB', (bw, bh), PAPER)
    lw = int(900 * 1.06); lh = int(LOGO.height * lw / LOGO.width)
    lg = LOGO.resize((lw, lh), Image.LANCZOS)
    m = Image.new('L', (lw, lh), 0)
    ImageDraw.Draw(m).rounded_rectangle((50, 50, lw - 50, lh - 50), 70, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(40))
    bg.paste(lg, ((bw - lw) // 2, int(760 * 1.06) - lh // 2), m)
    a = np.asarray(bg).astype(np.float32)
    a += np.random.default_rng(3).normal(0, 2.0, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
ENDCARD = _endcard()
def endcard(t):
    u = ease_io((t - END_START) / (TOTAL - END_START))
    z = 1.0 + 0.05 * u                       # very slow push-in
    sc = z / 1.06; hw, hh = W / 2 / sc, H / 2 / sc
    cx, cy = ENDCARD.width / 2, ENDCARD.height / 2
    return np.asarray(ENDCARD.transform((W, H), Image.AFFINE, (1 / sc, 0, cx - hw, 0, 1 / sc, cy - hh),
                                        resample=Image.BICUBIC)).astype(np.float32)

def frame_at(t):
    d = TRANS[-1][1]
    if t >= END_START - d / 2:
        if t < END_START + d / 2:
            e = ease((t - (END_START - d / 2)) / d)
            return grade(sources[-1].render(t)) * (1 - e) + endcard(t) * e
        return endcard(t)
    for k in range(len(SEGS) - 1):
        typ, d = TRANS[k]; b = SEGS[k][1]
        if d and b - d / 2 <= t < b + d / 2:
            p = (t - (b - d / 2)) / d; A, B = sources[k], sources[k + 1]; e = ease(p)
            if typ == 'dissolve':
                return grade(A.render(t)) * (1 - e) + grade(B.render(t)) * e
            if typ == 'zoom':
                return grade(A.render(t, 1 + 0.12 * p ** 2)) * (1 - e) + grade(B.render(t, 1 + 0.08 * (1 - p) ** 2)) * e
            if typ == 'focus':
                rad = 10 * math.sin(math.pi * p); ia, ib = A.render(t), B.render(t)
                if rad > 0.5: ia = ia.filter(ImageFilter.GaussianBlur(rad)); ib = ib.filter(ImageFilter.GaussianBlur(rad))
                e2 = ease((p - 0.25) / 0.5)
                return grade(ia) * (1 - e2) + grade(ib) * e2
            if typ == 'slide':   # gentle lateral move with soft motion blur + crossfade
                off = int(ease_io(p) * 220)
                a = np.asarray(A.render(t)); bb = np.asarray(B.render(t))
                a = np.roll(a, -off, axis=1); bb = np.roll(bb, 220 - off, axis=1)
                mix = a.astype(np.float32) * (1 - e) + bb.astype(np.float32) * e
                k_ = int(40 * math.sin(math.pi * p))
                if k_ > 2:
                    acc = np.zeros_like(mix)
                    for j in range(5): acc += np.roll(mix, int((j - 2) * k_ / 5), axis=1)
                    mix = acc / 5
                return mix * VIGNETTE
    i = next((j for j, s in enumerate(sources) if s.rs <= t < s.re), len(sources) - 1)
    out = grade(sources[i].render(t))
    return out

def compose(t):
    img = Image.fromarray(np.clip(frame_at(t), 0, 255).astype(np.uint8)).convert('RGBA')
    return draw_subs(img, t).convert('RGB')

if PREVIEW:
    for t in [float(x) for x in sys.argv[2].split(',')]:
        for s in sources: s.close(); s.idx = -1; s.frame = None
        compose(t).resize((360, 640)).save(f'prev_{t:05.2f}.png')
    sys.exit()

nframes = int(TOTAL * FPS)
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                        '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p',
                        '-profile:v', 'high', '-movflags', '+faststart', 'video_noaudio.mp4'], stdin=subprocess.PIPE)
for n in range(nframes):
    t = n / FPS
    enc.stdin.write(compose(t).tobytes())
    for s in sources:
        if s.re < t - 0.5: s.close()
    if n % 150 == 0: print(f'{n}/{nframes}', file=sys.stderr, flush=True)
enc.stdin.close(); enc.wait()

def ts_(x):
    return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{int(x % 60):02d},{int(round((x % 1) * 1000)) % 1000:03d}"
with open('subtitulos_gatos.srt', 'w') as f:
    for n, b in enumerate(blocks, 1):
        f.write(f"{n}\n{ts_(max(0, b['s']))} --> {ts_(b['e'])}\n{b['text']}\n\n")
print('done', file=sys.stderr)
