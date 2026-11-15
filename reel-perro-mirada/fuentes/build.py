#!/usr/bin/env python3
"""Montaje del Reel TREMDORA: ¿Por qué tu perro te mira mientras comes?"""
import json, os, subprocess, sys

S = os.path.dirname(os.path.abspath(__file__))
U = '/root/.claude/uploads/f678b386-cc3d-5da2-acb9-83b9c830adb1'
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(S, 'reel.mp4')
FPS = 30
W, H = 1080, 1920
END = 54.84
os.makedirs(f'{S}/shots', exist_ok=True)

def src(i):
    return next(f'{U}/{f}' for f in os.listdir(U) if f.startswith(i))

GRADE = "eq=contrast=1.04:saturation=1.06:gamma=1.01,colorbalance=rs=0.025:gs=0.008:bs=-0.025:rm=0.015:bm=-0.015,unsharp=5:5:0.35"

# Cortes (s) sincronizados con la voz editada
# (id, tipo, cut_in, opciones)
shots = [
    # 1 GANCHO — mirada fija mientras su humano come
    dict(id='0036e5cf', t0=0.00, ss=4.0, z=(1.00, 1.08), cy=0.45),
    # 2 INTRIGA — mirada tierna
    dict(id='8790d5c2', t0=4.90, ss=0.0, z=(1.02, 1.08), cy=0.45, xf=0.25),
    # 3 VÍNCULO SOCIAL — familia comiendo con su perro
    dict(id='e0eb5caa', t0=9.42, ss=0.0, z=(1.00, 1.06), cy=0.70, cx=0.47, crop='1182:1784:12:0'),
    # 4 CONTACTO VISUAL
    dict(id='7af4583f', t0=16.08, ss=0.0, z=(1.00, 1.05), cy=0.45, xf=0.2),
    # 5 OXITOCINA — caricia / beso
    dict(id='b6af6316', t0=21.36, ss=0.0, z=(1.00, 1.04), cy=0.5),
    # 6 GIRO «Pero ¡ojo!» — mirando el plato
    dict(id='ba4ad2dd', t0=24.88, ss=0.6, z=(1.12, 1.02), ease=0.5, cy=0.45),
    # 7 CONDUCTA APRENDIDA — pidiendo junto a la mesa
    dict(id='db70d6b1', t0=28.08, ss=0.3, z=(1.00, 1.05), cy=0.35, cx=0.4, crop='1182:1644:12:0'),
    dict(id='e8093ab0', t0=30.80, ss=0.0, z=(1.00, 1.04), cy=0.4),
    # 8 PROBLEMA COTIDIANO — cena con visitas
    dict(id='b71e58c3', t0=32.80, ss=0.0, z=(1.00, 1.05), cy=0.55, cx=0.5),
    # 9 CONSEJO — a su camita
    dict(id='ff2a6824', t0=36.48, ss=0.1, z=(1.00, 1.04), cy=0.55),
    # 10 REFUERZO POSITIVO — premio en su cama
    dict(img='f7858ae0-image.jpg', t0=38.52, z=(1.00, 1.06), box=(300, 0, 1125, 817), fy=0.5),
    # 11 RESULTADO — tranquilo mientras cenan
    dict(img='fb2b5fc3-image.jpg', t0=42.52, z=(1.00, 1.06), box=None, fy=0.5, xf=0.25),
    dict(id='cbccdfbe', t0=45.14, ss=0.4, z=(1.00, 1.04), cy=0.55),
    # 12 CIERRE EMOCIONAL
    dict(id='dd70bdd1', t0=47.48, ss=0.0, z=(1.00, 1.05), cy=0.4, crop='1206:2130:0:2', xf=0.25),
    dict(img='3d0ae87f-image.png', t0=50.88, z=(1.00, 1.035), box=None, fy=0.168, fw=820, ad=True, xf=0.3),
]
for i, s in enumerate(shots):
    s['t1'] = shots[i + 1]['t0'] if i + 1 < len(shots) else END
    s['xin'] = s.get('xf', 0)
    s['xout'] = shots[i + 1].get('xf', 0) if i + 1 < len(shots) else 0


def fr(t):
    return round(t * FPS) / FPS


def zoom_expr(z0, z1, D, ease=None):
    if ease:  # punch-in that settles quickly (cut marcado)
        return f"({z1}+({z0}-{z1})*exp(-t/{ease*0.4}))"
    return f"({z0}+({z1}-{z0})*t/{D:.3f})"


def render(i, s):
    # timeline: shot visible from t0 - xin/2 to t1 + xout/2
    D = fr((s['t1'] + s['xout'] / 2) - (s['t0'] - s['xin'] / 2))
    s['D'] = D
    out = f"{S}/shots/{i:02d}.mp4"
    s['file'] = out
    z = zoom_expr(*s['z'], D, s.get('ease'))
    if 'id' in s:
        f = src(s['id'])
        dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
        avail = dur - s['ss'] - 0.05
        speed = min(1.0, avail / D)  # slow-motion only if the clip is too short
        s['speed'] = round(speed, 3)
        crop = f"crop={s['crop']}," if s.get('crop') else ''
        cx, cy = s.get('cx', 0.5), s.get('cy', 0.5)
        vf = (f"{crop}setpts=(PTS-STARTPTS)/{speed},fps={FPS},"
              f"scale='if(gt(a,{W}/{H}),-2,{W})':'if(gt(a,{W}/{H}),{H},-2)',"  # cover
              f"scale=w='trunc(iw*{z}/2)*2':h='trunc(ih*{z}/2)*2':eval=frame:flags=bicubic,"
              f"crop={W}:{H}:'(iw-{W})*{cx}':'(ih-{H})*{cy}',"
              f"{GRADE},setsar=1,format=yuv420p")
        cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', str(s['ss']), '-i', f, '-t', f'{D:.3f}', '-an', '-vf', vf]
    else:
        f = f"{U}/{s['img']}"
        box = s.get('box')
        pre = f"crop={box[2]-box[0]}:{box[3]-box[1]}:{box[0]}:{box[1]}," if box else ''
        fw = s.get('fw', W)
        fy = s['fy']
        bg = (f"[0]{pre}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"boxblur=40:3,eq=brightness=-0.10:saturation=0.85[bg];")
        fg = (f"[0]{pre}scale={fw}:-2,fps={FPS},"
              f"scale=w='trunc(iw*{z}/2)*2':h='trunc(ih*{z}/2)*2':eval=frame:flags=bicubic[fg];")
        grade = '' if s.get('ad') else f",{GRADE}"
        fc = bg + fg + f"[bg]fps={FPS}[bgf];[bgf][fg]overlay=x='(W-w)/2':y='(H-h)*{fy}':eval=frame:shortest=1{grade},setsar=1,format=yuv420p[v]"
        cmd = ['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-framerate', str(FPS), '-t', f'{D:.3f}', '-i', f,
               '-filter_complex', fc, '-map', '[v]', '-t', f'{D:.3f}']
    cmd += ['-r', str(FPS), '-c:v', 'libx264', '-preset', 'medium', '-crf', '14', out]
    subprocess.run(cmd, check=True)


for i, s in enumerate(shots):
    if os.environ.get('SKIP') and os.path.exists(f"{S}/shots/{i:02d}.mp4"):
        s['D'] = fr((s['t1'] + s['xout'] / 2) - (s['t0'] - s['xin'] / 2)); s['file'] = f"{S}/shots/{i:02d}.mp4"
    else:
        render(i, s)
    print(f"{i+1:2d} {s.get('id', s.get('img'))[:8]} {s['t0']:6.2f}-{s['t1']:6.2f} D={s['D']:.2f} speed={s.get('speed', '-')}")

# ---------- Ensamblado con cortes limpios + disolvencias puntuales ----------
inputs, fc, cur, curlen = [], '', '[n0]', shots[0]['D']
for i, s in enumerate(shots):
    inputs += ['-i', s['file']]
    fc += f"[{i}:v]setpts=PTS-STARTPTS,fps={FPS},settb=1/{FPS}[n{i}];"
for i in range(1, len(shots)):
    s = shots[i]
    lab = f'[c{i}]'
    if s['xin'] > 0:
        off = curlen - s['xin']
        fc += f"{cur}[n{i}]xfade=transition=fade:duration={s['xin']}:offset={off:.3f}{lab};"
        curlen = curlen + s['D'] - s['xin']
    else:
        fc += f"{cur}[n{i}]concat=n=2:v=1:a=0,settb=1/{FPS}{lab};"
        curlen += s['D']
    cur = lab
print('video length', round(curlen, 3))

# ---------- Subtítulos ASS ----------
words = [w for seg in json.load(open(f'{S}/trans_new.json')) for w in seg['words']]
groups = [
    ("¿Sabías que cuando", 3), ("tu perro te {mira}", 4), ("mientras comes,", 2),
    ("no siempre te está", 4), ("pidiendo {comida}?", 2),
    ("A veces,", 2), ("detrás de esa {mirada},", 4),
    ("hay algo mucho", 3), ("más {bonito}.", 2),
    ("Los perros son", 3), ("animales sociales", 2),
    ("y comer cerca", 3), ("de quienes consideran", 3), ("su {familia}", 2),
    ("puede ser parte", 3), ("de su {vínculo}.", 3),
    ("Además,", 1), ("estudios han relacionado", 3), ("el {contacto visual}", 3), ("afectuoso", 1),
    ("entre perros y humanos", 4), ("con la {oxitocina},", 3),
    ("conocida como", 2), ("la hormona del vínculo.", 4),
    ("Pero {¡ojo!}", 2),
    ("también puede estar", 3), ("pidiendo {comida}.", 2),
    ("Si alguna vez", 3), ("le diste un {trocito}", 4), ("desde la mesa,", 3),
    ("pudo aprender", 2), ("que mirarte {funciona}.", 3),
    ("¿Y cómo evitarlo?", 3),
    ("Especialmente", 1), ("cuando tienes {visitas}.", 3),
    ("Enséñale a quedarse", 3), ("en su {camita}.", 3),
    ("{Premia} cuando", 2), ("esté {tranquilo}", 2),
    ("y evita darle comida", 4), ("desde la mesa.", 3),
    ("Practícalo antes", 2), ("de recibir {invitados},", 3),
    ("porque comprender", 2), ("su {mirada}", 2), ("es importante.", 2),
    ("Pero enseñarle", 2), ("con {cariño}", 2),
    ("también es una forma", 4), ("de {amarlo}.", 2),
    ("¿El tuyo también", 3), ("te {mira así}?", 3),
    ("{¡Te leo!}", 2),
]
assert sum(n for _, n in groups) == len(words), (sum(n for _, n in groups), len(words))
ev, k = [], 0
for txt, n in groups:
    ws = words[k:k + n]; k += n
    ev.append([ws[0]['s'] - 0.06, ws[-1]['e'], txt, [w['s'] for w in ws]])
for j, e in enumerate(ev):
    nxt = ev[j + 1][0] if j + 1 < len(ev) else END - 0.05
    e[1] = min(nxt, e[1] + 0.45) if nxt - e[1] > 0.45 else nxt


def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); sec = t % 60
    return f"{h}:{m:02d}:{sec:05.2f}"

IVORY, GOLD = '&H00EFF5F8', '&H0096BED8'
ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Montserrat SemiBold,72,{IVORY},{IVORY},&H8C1A120C,&H78000000,0,0,0,0,100,100,1.2,0,1,2.6,3,2,80,80,430,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for a, b, txt, wst in ev:
    # palabra a palabra: cada palabra aparece cuando se pronuncia
    toks, tb, inhl = [], '', False
    for ch in txt:
        if ch == '{': inhl = True; continue
        if ch == '}': inhl = False; continue
        if ch == ' ':
            toks.append((tb, hlw)); tb = ''; continue
        if tb == '': hlw = inhl
        tb += ch
        if inhl: hlw = True
    toks.append((tb, hlw))
    assert len(toks) == len(wst), (txt, toks)
    out = ''
    for j, ((w, h), t) in enumerate(zip(toks, wst)):
        d = max(0, int((t - a) * 1000))
        col = GOLD if h else IVORY
        out += ('' if j == 0 else ' ') + '{\\1c' + col + '&\\alpha&HFF&\\t(' + f'{d},{d+120}' + ',\\alpha&H00&)}' + w
    anim = '{\\blur0.8\\fad(0,80)\\fscx96\\fscy96\\t(0,160,\\fscx100\\fscy100)}'
    if a >= shots[-1]['t0'] - 0.1:
        anim = anim.replace('{', '{\\an2\\pos(540,1268)', 1)
    ass += f"Dialogue: 0,{ts(a)},{ts(b)},Sub,,0,0,0,,{anim}{out}\n"
open(f'{S}/subs.ass', 'w').write(ass)

# ---------- Logo al cierre ----------
LOGO_T0 = shots[-1]['t0'] + 0.35
fc += (f"{cur}settb=AVTB[cur2];[{len(shots)}:v]scale=315:-1,format=rgba,colorchannelmixer=aa=0.95,"
       f"fade=t=in:st={LOGO_T0}:d=0.6:alpha=1[lg];"
       f"[cur2][lg]overlay=x=(W-w)/2:y=1305:enable='gte(t,{LOGO_T0})'[vl];"
       f"[vl]ass={S}/subs.ass:fontsdir={S}/fonts/mont/package,format=yuv420p[vout];")
inputs += ['-loop', '1', '-framerate', str(FPS), '-t', f'{END}', '-i', f'{S}/logo_tremdora_marfil_sombra.png']

# ---------- Audio: voz protagonista + música con ducking ----------
vi, mi = len(shots) + 1, len(shots) + 2
inputs += ['-i', f'{S}/audio/voz_edit.wav', '-i', f'{S}/audio/music1.mp3']
fc += (f"[{vi}:a]aresample=48000,apad=whole_dur={END},asplit=2[voz][sc];"
       f"[{mi}:a]aresample=48000,atrim=0:{END},asetpts=PTS-STARTPTS,volume=-7dB,"
       f"afade=t=in:d=0.4,afade=t=out:st={END-1.1}:d=1.1[mus];"
       f"[mus][sc]sidechaincompress=threshold=0.05:ratio=2.5:attack=80:release=500:makeup=1[mduck];"
       f"[voz][mduck]amix=inputs=2:duration=first:normalize=0,"
       f"loudnorm=I=-14:TP=-1.0:LRA=11,aresample=48000[aout]")

cmd = ['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', fc, '-map', '[vout]', '-map', '[aout]',
       '-t', f'{END}', '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
       '-r', str(FPS), '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', OUT]
subprocess.run(cmd, check=True)
print('OK', OUT)
