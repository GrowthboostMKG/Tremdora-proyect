"""Tremdora reel renderer: Ken Burns camera moves, varied cinematic transitions, word-synced animated subtitles."""
import json, subprocess, sys, math, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

UP = '/root/.claude/uploads/89643bfb-0721-519a-968f-c88117646256/'
W, H, FPS = 1080, 1920, 30
PREVIEW = len(sys.argv) > 1 and sys.argv[1] == 'preview'   # renders stills only
TOTAL = 71.2

CLIPS = {  # file, crop (w,h,x,y) to remove bars/edges, extra filters
    'A': (UP + '363bf58c-ScreenRecording_11-10-2026_17-52-55_1.mov', (1194, 1490, 6, 0), 'hqdn3d=2:2:3:3,'),
    'B': (UP + 'ff049614-ScreenRecording_11-10-2026_17-53-47_1.mov', (1194, 1800, 6, 2), ''),
    'C': (UP + '7e8ea63a-ScreenRecording_11-10-2026_16-45-46_1.mov', (1194, 1336, 6, 2), 'hqdn3d=1.5:1.5:2:2,'),
    'D': (UP + '6d8298b9-ScreenRecording_11-10-2026_16-43-58_1.mov', (1190, 1590, 8, 2), ''),
    'E': (UP + 'a27915f0-ScreenRecording_11-10-2026_16-47-10_1.mov', (1190, 1802, 6, 2), ''),
    'F': (UP + '3bfaf5ef-ScreenRecording_11-10-2026_16-44-35_1.mov', (1194, 950, 6, 220), 'hqdn3d=2.5:2.5:3:3,'),
    'G': (UP + '7d72a573-ScreenRecording_11-10-2026_16-45-46_1.mov', (1194, 1336, 6, 2), ''),
}

# start, end, clip, src0, src1, zoom0, zoom1, (cx0,cy0), (cx1,cy1)   centres normalised in the cropped source
SEGS = [
    (0.00, 3.00, 'G', 0.0, 2.0, 1.00, 1.10, (0.50, 0.42), (0.53, 0.43)),
    (3.00, 6.85, 'D', 0.0, 2.9, 1.04, 1.32, (0.45, 0.50), (0.30, 0.47)),
    (6.85, 12.70, 'C', 0.0, 3.6, 1.14, 1.00, (0.40, 0.50), (0.47, 0.50)),
    (12.70, 17.30, 'D', 2.9, 5.9, 1.40, 1.50, (0.28, 0.47), (0.25, 0.46)),
    (17.30, 23.30, 'G', 2.0, 5.3, 1.12, 1.30, (0.58, 0.47), (0.62, 0.52)),
    (23.30, 26.70, 'A', 0.0, 2.5, 1.04, 1.12, (0.50, 0.45), (0.50, 0.42)),
    (26.70, 28.80, 'C', 3.6, 5.0, 1.00, 1.06, (0.44, 0.50), (0.46, 0.50)),
    (28.80, 36.80, 'B', 0.0, 5.0, 1.00, 1.13, (0.50, 0.44), (0.44, 0.40)),
    (36.80, 41.60, 'B', 5.0, 9.5, 1.14, 1.04, (0.55, 0.45), (0.52, 0.47)),
    (41.60, 46.60, 'F', 0.0, 4.16, 1.00, 1.08, (0.42, 0.60), (0.40, 0.58)),
    (46.60, 50.45, 'C', 5.0, 7.2, 1.10, 1.00, (0.52, 0.50), (0.48, 0.50)),
    (50.45, 57.00, 'E', 0.0, 6.1, 1.00, 1.12, (0.50, 0.55), (0.50, 0.60)),
    (57.00, 60.10, 'C', 7.2, 9.4, 1.22, 1.30, (0.40, 0.46), (0.38, 0.47)),
    (60.10, 65.50, 'G', 0.0, 3.2, 1.28, 1.14, (0.45, 0.38), (0.48, 0.40)),
    (65.50, 69.30, 'A', 0.0, 2.5, 1.16, 1.04, (0.55, 0.40), (0.50, 0.42)),
]
# transition at end of SEGS[i]  (type, duration)
TRANS = [('zoom', .35), ('dissolve', .45), ('cut', 0), ('focus', .4), ('dissolve', .4), ('cut', 0), ('whip', .3),
         ('dissolve', .5), ('focus', .4), ('whip', .3), ('cut', 0), ('zoom', .35), ('cut', 0), ('dissolve', .5),
         ('endcard', .7)]
END_START = SEGS[-1][1]

def ease(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * (3 - 2 * x)

def ease_io(x):  # softer cubic in-out for camera
    x = min(max(x, 0.0), 1.0)
    return 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2

# ---------- frame sources ----------
class Source:
    def __init__(self, i):
        s0, s1, clip = SEGS[i][0], SEGS[i][1], SEGS[i][2]
        tin = TRANS[i - 1][1] / 2 if i > 0 else 0
        tout = TRANS[i][1] / 2
        self.rs, self.re = s0 - tin, s1 + tout
        self.i = i
        f, (cw, ch, cx, cy), extra = CLIPS[clip]
        src0, src1 = SEGS[i][3], SEGS[i][4]
        dur = self.re - self.rs
        self.speed = (src1 - src0) / dur
        self.w, self.h = cw, ch
        vf = (f"crop={cw}:{ch}:{cx}:{cy},{extra}"
              f"eq=contrast=1.06:saturation=1.07:gamma=0.98,"
              f"colorbalance=rs=0.02:gs=0.005:bs=-0.02:rh=0.015:bh=-0.015,"
              f"unsharp=5:5:0.45,setpts=(PTS-STARTPTS)/{self.speed:.5f},fps={FPS}")
        self.cmd = ['ffmpeg', '-v', 'error', '-ss', f'{src0}', '-t', f'{src1 - src0 + 0.1}', '-i', f,
                    '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
        self.p = None; self.idx = -1; self.frame = None
        self.cover = max(W / cw, H / ch)

    def get(self, t):
        if self.p is None:
            self.p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, bufsize=10 ** 8)
        want = int((t - self.rs) * FPS + 1e-6)
        while self.idx < want:
            buf = self.p.stdout.read(self.w * self.h * 3)
            if len(buf) < self.w * self.h * 3:
                break  # hold last frame
            self.frame = Image.frombuffer('RGB', (self.w, self.h), buf, 'raw', 'RGB', 0, 1)
            self.idx += 1
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
        img = self.get(t)
        return img.transform((W, H), Image.AFFINE, (1 / sc, 0, cx - hw, 0, 1 / sc, cy - hh), resample=Image.BICUBIC)

# ---------- static layers ----------
yy, xx = np.mgrid[0:H, 0:W]
r = np.sqrt(((xx - W / 2) / (W * .62)) ** 2 + ((yy - H / 2) / (H * .62)) ** 2)
VIGNETTE = (1 - 0.32 * np.clip(r - 0.45, 0, 1) ** 1.6)[..., None].astype(np.float32)
# soft gradient at bottom & top for text legibility (very subtle)
GRAD = np.ones((H, 1, 1), np.float32)
g = np.clip((yy[:, :1] - 1050) / 600, 0, 1) * 0.22
GRAD = (1 - g)[..., None].astype(np.float32)

logo = Image.open(UP + 'e9e2ee7f-image.jpg').convert('RGB')
PAPER = (236, 227, 218)
def make_endcard():
    bg = Image.new('RGB', (W, H), PAPER)
    lw = 1000; lh = int(logo.height * lw / logo.width)
    lg = logo.resize((lw, lh), Image.LANCZOS)
    m = Image.new('L', (lw, lh), 0)
    ImageDraw.Draw(m).rounded_rectangle((60, 60, lw - 60, lh - 60), 80, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(45))
    bg.paste(lg, ((W - lw) // 2, 820 - lh // 2), m)
    # subtle grain to tie the extended paper together
    a = np.asarray(bg).astype(np.float32)
    a += np.random.default_rng(3).normal(0, 2.2, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
ENDCARD = make_endcard()

# ---------- subtitles ----------
FB = '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
FSB = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
LIME = (205, 240, 120)
WHITE = (255, 255, 255)
HL = {'calor', 'cerebro', 'igual', 'Emory', 'escáner', 'dueño', 'recompensa', 'premio', 'loco', 'Japón', 'oxitocina',
      'apego', 'bebé', 'profundo', 'ancestros', 'manada', 'vulnerable', 'comodidad', 'hogar', 'comentarios', 'espalda', 'olor'}

words = json.load(open('words.json'))
fixed = []
k = 0
while k < len(words):
    w = dict(words[k]); w['w'] = w['w'].strip()
    if w['w'] == 'universidad' and words[k + 1]['w'].strip() == 'de' and words[k + 2]['w'].strip().startswith('Mori'):
        fixed.append(dict(w='Universidad', s=w['s'], e=w['e']))
        fixed.append(dict(w='Emory,', s=words[k + 1]['s'], e=words[k + 2]['e'])); k += 3; continue
    if w['w'] == 'le' and words[k + 1]['w'].strip() == 'sube':
        w['w'] = 'les'
    fixed.append(w); k += 1
words = fixed

def clean(t):
    return t.rstrip('.,')

# group into chunks: break at sentence end, comma+pause, long pause, or >= 4 words / 22 chars
chunks, cur = [], []
for j, w in enumerate(words):
    cur.append(w)
    nxt = words[j + 1] if j + 1 < len(words) else None
    gap = (nxt['s'] - w['e']) if nxt else 9
    txt = ' '.join(clean(x['w']) for x in cur)
    end_sentence = w['w'].endswith('.')
    if (nxt is None or end_sentence or gap > 0.33 or (w['w'].endswith(',') and len(cur) >= 2)
            or len(cur) >= 4 or len(txt) + len(clean(nxt['w'])) + 1 > 21):
        chunks.append(cur); cur = []
for c_i, c in enumerate(chunks):
    nxt = chunks[c_i + 1][0]['s'] if c_i + 1 < len(chunks) else 99
    c_end = min(nxt - 0.02, c[-1]['e'] + 0.9)
    for w in c: w['chunk_end'] = c_end

word_cache = {}
def word_img(text, color, size):
    key = (text, color, size)
    if key in word_cache: return word_cache[key]
    f = ImageFont.truetype(FB, size)
    bb = f.getbbox(text)
    pad = 30
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    im = Image.new('RGBA', (tw + 2 * pad, th + 2 * pad), (0, 0, 0, 0))
    sh = Image.new('L', im.size, 0)
    ImageDraw.Draw(sh).text((pad - bb[0], pad - bb[1] + 4), text, font=f, fill=255)
    soft = sh.filter(ImageFilter.GaussianBlur(11)).point(lambda v: int(v * 0.75))
    tight = sh.filter(ImageFilter.GaussianBlur(2.5)).point(lambda v: int(v * 0.55))
    shadow = Image.new('RGBA', im.size, (0, 0, 0, 0))
    a = np.maximum(np.asarray(soft), np.asarray(tight))
    shadow.putalpha(Image.fromarray(a))
    im = Image.alpha_composite(im, shadow)
    ImageDraw.Draw(im).text((pad - bb[0], pad - bb[1]), text, font=f, fill=color + (255,))
    word_cache[key] = (im, pad, tw, th, f.getlength(' '))
    return word_cache[key]

def layout_chunk(c, size):
    items = [(clean(w['w']), w) for w in c]
    sp = ImageFont.truetype(FB, size).getlength(' ')
    lines, line, lw = [], [], 0
    for txt, w in items:
        col = LIME if clean(w['w']).lower() in {h.lower() for h in HL} else WHITE
        im, pad, tw, th, _ = word_img(txt, col, size)
        add = tw + (sp if line else 0)
        if line and lw + add > 900:
            lines.append((line, lw)); line, lw = [], 0; add = tw
        line.append((txt, w, col, tw)); lw += add
    if line: lines.append((line, lw))
    return lines, sp

SUB_Y = {13: 1440}
DEFAULT_Y = 1270
def sub_y(t):
    for i, s in enumerate(SEGS):
        if s[0] <= t < s[1]: return SUB_Y.get(i, DEFAULT_Y)
    return DEFAULT_Y

def draw_subs(frame, t):
    active = None
    for c in chunks:
        if c[0]['s'] - 0.06 <= t < c[0]['chunk_end']:
            active = c
    if not active: return frame
    size = 96 if active is chunks[0] or active is chunks[1] else 84
    lines, sp = layout_chunk(active, size)
    lh = size * 1.18
    y0 = sub_y(active[0]['s']) - lh * len(lines) / 2
    fade_out = min(1, max(0, (active[0]['chunk_end'] - t) / 0.08))
    for li, (line, lw) in enumerate(lines):
        x = W / 2 - lw / 2
        y = y0 + li * lh
        for txt, w, col, tw in line:
            im, pad, _, th, _ = word_img(txt, col, size)
            dt = t - (w['s'] - 0.06)
            if dt >= 0:
                a = min(1, dt / 0.10) * fade_out
                p = min(1, dt / 0.20)
                sc = 0.82 + 0.18 * (1 + 2.2 * (p - 1) ** 3 + 1.2 * (p - 1) ** 2) if p < 1 else 1.0
                dy = (1 - ease(p)) * 14
                wi = im
                if abs(sc - 1) > 0.005:
                    wi = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.BICUBIC)
                if a < 1:
                    wi = wi.copy(); wi.putalpha(wi.getchannel('A').point(lambda v: int(v * a)))
                cxw = x + tw / 2; cyw = y + th / 2 + dy
                frame.alpha_composite(wi, (int(cxw - wi.width / 2), int(cyw - wi.height / 2)))
            x += tw + sp
    return frame

# study chips (brand colours)
CHIPS = [(12.95, 17.15, 'ESTUDIO', 'Universidad Emory · EE. UU.'),
         (29.05, 36.6, 'ESTUDIO', 'Japón · revista Science, 2015')]
def chip_img(tag, text):
    f1 = ImageFont.truetype(FB, 30); f2 = ImageFont.truetype(FSB, 34)
    w1 = f1.getlength(tag); w2 = f2.getlength(text)
    wdt = int(w1 + w2 + 34 + 34 + 26); hgt = 74
    im = Image.new('RGBA', (wdt + 40, hgt + 40), (0, 0, 0, 0))
    sh = Image.new('L', im.size, 0)
    ImageDraw.Draw(sh).rounded_rectangle((20, 26, 20 + wdt, 26 + hgt), 37, fill=110)
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    shadow = Image.new('RGBA', im.size, (40, 20, 10, 0)); shadow.putalpha(sh)
    im = Image.alpha_composite(im, shadow)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((20, 20, 20 + wdt, 20 + hgt), 37, fill=(243, 235, 225, 240))
    d.rounded_rectangle((26, 26, 26 + w1 + 34, 14 + hgt), 31, fill=(122, 74, 52, 255))
    d.text((26 + 17, 20 + hgt / 2), tag, font=f1, fill=(243, 235, 225), anchor='lm')
    d.text((26 + w1 + 34 + 18, 20 + hgt / 2 + 1), text, font=f2, fill=(92, 56, 38), anchor='lm')
    return im
CHIP_IMGS = [chip_img(c[2], c[3]) for c in CHIPS]

def draw_chips(frame, t):
    for (a, b, *_), im in zip(CHIPS, CHIP_IMGS):
        if a <= t < b:
            p_in = ease((t - a) / 0.35); p_out = ease((b - t) / 0.3)
            al = min(p_in, p_out)
            dy = (1 - p_in) * -24
            wi = im.copy(); wi.putalpha(wi.getchannel('A').point(lambda v: int(v * al)))
            frame.alpha_composite(wi, (int(W / 2 - im.width / 2), int(300 + dy)))
    return frame

# ---------- compositing ----------
sources = [Source(i) for i in range(len(SEGS))]
for s in sources:
    print(f"seg {s.i} {SEGS[s.i][2]} speed {s.speed:.2f}", file=sys.stderr)

def grade(img):
    a = np.asarray(img).astype(np.float32)
    a *= VIGNETTE; a *= GRAD
    return a

def hshift_blur(a, k):
    if k < 2: return a
    acc = np.zeros_like(a); n = 7
    for j in range(n):
        acc += np.roll(a, int((j - n // 2) * k / n), axis=1)
    return acc / n

def frame_at(t):
    # endcard
    i = next((j for j, s in enumerate(sources) if s.rs <= t < s.re), None)
    if t >= END_START + TRANS[-1][1] / 2 or i is None:
        if t >= END_START - TRANS[-1][1] / 2:
            return np.asarray(ENDCARD).astype(np.float32)
    # transition?
    for k in range(len(SEGS)):
        typ, d = TRANS[k]
        b = SEGS[k][1]
        if d and b - d / 2 <= t < b + d / 2:
            p = (t - (b - d / 2)) / d
            A = sources[k]
            if typ == 'endcard':
                out = grade(A.render(t, 1 + 0.04 * p))
                return out * (1 - ease(p)) + np.asarray(ENDCARD).astype(np.float32) * ease(p)
            Bs = sources[k + 1]
            if typ == 'dissolve':
                return grade(A.render(t)) * (1 - ease(p)) + grade(Bs.render(t)) * ease(p)
            if typ == 'zoom':
                e = ease(p)
                a = grade(A.render(t, 1 + 0.35 * p ** 2)); bb = grade(Bs.render(t, 1 + 0.25 * (1 - p) ** 2))
                out = a * (1 - e) + bb * e
                return out
            if typ == 'focus':
                rad = 16 * math.sin(math.pi * p)
                ia, ib = A.render(t), Bs.render(t)
                if rad > 0.5:
                    ia = ia.filter(ImageFilter.GaussianBlur(rad)); ib = ib.filter(ImageFilter.GaussianBlur(rad))
                e = ease((p - 0.25) / 0.5)
                return grade(ia) * (1 - e) + grade(ib) * e
            if typ == 'whip':
                e = ease_io(p)
                off = int(e * W)
                a = grade(A.render(t)); bb = grade(Bs.render(t))
                canvas = np.concatenate([a, bb], 1)[:, off:off + W]
                return hshift_blur(canvas, int(140 * math.sin(math.pi * p)))
    return grade(sources[i].render(t))

def compose(t):
    a = frame_at(t)
    img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert('RGBA')
    if t < END_START:
        img = draw_chips(img, t)
        img = draw_subs(img, t)
    return img.convert('RGB')

if PREVIEW:
    ts = [float(x) for x in sys.argv[2].split(',')]
    for t in ts:
        # fresh sources for random access
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

# SRT export
def ts_(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
with open('subtitulos.srt', 'w') as f:
    for n, c in enumerate(chunks, 1):
        f.write(f"{n}\n{ts_(c[0]['s'])} --> {ts_(c[0]['chunk_end'])}\n{' '.join(clean(w['w']) for w in c)}\n\n")
print('done', file=sys.stderr)
