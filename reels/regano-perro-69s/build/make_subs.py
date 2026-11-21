"""Genera subtítulos ASS (1080x1920) desde la transcripción palabra a palabra.
uso: python3 make_subs.py <words.json> <salida.ass> <salida.srt>"""
import sys, json
from PIL import ImageFont
WORDS, OUT, SRT = sys.argv[1:4]
FONT = ImageFont.truetype("/root/.fonts/Lora-600.ttf", 64)   # 64 px de cuerpo (em); en ASS equivale a tamaño 96 (Lora: alto de línea 1,5 em)
MAXW = 880                     # ancho útil de línea (px)
HL = "&H8BD9F4&"               # #F4D98B en BGR
TXT = "&HE8F4FF&"              # blanco cálido #FFF4E8
FIX = {"e-books.": "ebooks.", "ahora": "«ahora", "comenta,": "comenta", "muestra.": "«MUESTRA»."}
HIGHLIGHT = ["Él no.", "Solo sabe volver.", "Él solo tiene una.", "Tú."]
W = []
for s in json.load(open(WORDS)):
    for w in s["words"]:
        W.append([w["w"].strip(), w["s"], w["e"]])
# correcciones de la transcripción automática
for i in range(len(W)-1, 0, -1):
    if W[i][0].startswith("-"): W[i-1][0] += W[i][0]; W[i-1][2] = W[i][2]; del W[i]
for i, w in enumerate(W):
    if w[0] == "dicho," and W[i+1][0] == "ahora": w[0] = "dicho"; W[i+1][0] = "«ahora"; W[i+2][0] = "no»,"
    if w[0] == "comenta,": w[0] = "comenta"; W[i+1][0] = "«MUESTRA»."
    if w[0] == "e-books.": w[0] = "ebooks."
sents, cur = [], []
for w in W:
    cur.append(w)
    if w[0].endswith((".", "?", "!")): sents.append(cur); cur = []
width = lambda t: FONT.getlength(t)
def lines(ws):
    """Mejor reparto en 1-2 líneas; None si no cabe."""
    t = " ".join(w[0] for w in ws)
    if width(t) <= MAXW*0.9: return [t]
    best = None
    for k in range(1, len(ws)):
        a = " ".join(w[0] for w in ws[:k]); b = " ".join(w[0] for w in ws[k:])
        if max(width(a), width(b)) > MAXW: continue
        sc = abs(width(a)-width(b)) - (260 if ws[k-1][0].endswith(",") else 0) \
             + (400 if a.count("«") > a.count("»") else 0) \
             + (220 if ws[k-1][0].lower() in ("te","la","el","que","y","de","con","a","sin","lo","se","una","un","los","las","mil","mis") else 0) \
             - (60 if ws[k][0].lower() in ("y","que","con","de","sin","a","te","la","mucho","detrás") else 0)
        if best is None or sc < best[0]: best = (sc, [a, b])
    return best[1] if best else None
def blocks(ws):
    if lines(ws): return [ws]
    best = None
    for k in range(2, len(ws)-1):
        if not (lines(ws[:k]) and lines(ws[k:])): continue
        sc = abs(len(" ".join(w[0] for w in ws[:k])) - len(" ".join(w[0] for w in ws[k:]))) \
             - (40 if ws[k-1][0].endswith(",") else 0) - (25 if ws[k][0].lower() in ("que","de","con","detrás","mucho","sube") else 0)
        if best is None or sc < best[0]: best = (sc, k)
    k = best[1]; return blocks(ws[:k]) + blocks(ws[k:])
# cortes de frase elegidos a mano donde el automático no queda natural: frase -> bloques (líneas separadas por |)
MANUAL = {
 "Estás en el sofá con el móvil y la cabeza a mil.": ["Estás en el sofá con el móvil|y la cabeza a mil."],
 "Y se tumba lejos con la cabeza entre las patas.": ["Y se tumba lejos|con la cabeza entre las patas."],
 "Y hay un experimento que lo demuestra mejor que nada.": ["Y hay un experimento|que lo demuestra", "mejor que nada."],
 "Y si quieres entenderle aún mejor, comenta «MUESTRA».": ["Y si quieres|entenderle aún mejor,", "comenta «MUESTRA»."],
 "Sus perros corrían a abrirla mucho más rápido que cuando solo tarareaban.": ["Sus perros corrían a abrirla|mucho más rápido", "que cuando solo tarareaban."],
}
LAYOUT = {}
B = []
for s_ in sents:
    t = " ".join(w[0] for w in s_)
    if t in MANUAL:
        i0 = 0
        for blk in MANUAL[t]:
            n = len(blk.replace("|", " ").split()); B.append(s_[i0:i0+n]); i0 += n
            LAYOUT[id(B[-1])] = blk.split("|")
    else: B += blocks(s_)
# unir «Él solo tiene una.» + «Tú.» en un solo bloque para leerlo con calma
for i in range(len(B)-1):
    if " ".join(w[0] for w in B[i]) == "Él solo tiene una." and B[i+1][0][0] == "Tú.":
        B[i] = B[i] + B[i+1]; del B[i+1]; break
def ts(x):
    cs = int(round(x*100)); return f"{cs//360000}:{cs//6000%60:02}:{cs//100%60:02}.{cs%100:02}"
def tsrt(x):
    ms = int(round(x*1000)); return f"{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}"
Q0, Q1 = 65.95, 69.0          # pregunta final
ev, srt = [], []
for i, b in enumerate(B):
    st = max(0, b[0][1]-0.10) if i else 0.0
    nxt = B[i+1][0][1]-0.12 if i+1 < len(B) else min(b[-1][2]+0.5, Q0-0.08)
    en = min(nxt, max(b[-1][2]+0.6, st+1.3))
    ls = LAYOUT.get(id(b)) or lines(b) or [" ".join(w[0] for w in b)]
    if " ".join(w[0] for w in b) == "Él solo tiene una. Tú.": ls = ["Él solo tiene una.", "Tú."]
    def paint(l):
        for h in HIGHLIGHT:
            if l == h or l.endswith(" "+h) and h != "Tú.":
                l = l.replace(h, "{\\c"+HL+"}"+h+"{\\c"+TXT+"}")
            elif l == h: pass
        return l
    txt = "\\N".join(paint(l) for l in ls)
    ev.append(f"Dialogue: 0,{ts(st)},{ts(en)},Sub,,0,0,0,,{{\\fad(160,140)}}{txt}")
    srt.append(f"{i+1}\n{tsrt(st)} --> {tsrt(en)}\n" + "\n".join(ls) + "\n")
# Cierre: pregunta + logo
ev.append(f"Dialogue: 1,{ts(Q0)},{ts(Q1)},Question,,0,0,0,,{{\\fad(450,600)}}¿Cuándo fue la última vez\\Nque le pediste perdón\\Nal tuyo?")
ev.append(f"Dialogue: 1,{ts(63.2)},{ts(Q1)},Logo,,0,0,0,,{{\\fad(900,600)}}TREMDORA")
head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Lora SemiBold,96,&H00E8F4FF,&H00E8F4FF,&H8C000000,&H80000000,0,0,0,0,100,100,0,0,1,2.6,3.5,2,100,100,430,1
Style: Question,Lora SemiBold,99,&H00E8F4FF,&H00E8F4FF,&H8C000000,&H80000000,0,0,0,0,100,100,0,0,1,2.8,3.8,2,90,90,560,1
Style: Logo,Lora SemiBold,42,&H40E8F4FF,&H40E8F4FF,&HB4000000,&HB4000000,0,0,0,0,100,100,10,0,1,1.4,1.8,8,80,80,235,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
# sombra suave: desenfoque sobre contorno y sombra
ev = [e.replace("}", "\\blur5}", 1) if "{\\fad" in e else e for e in ev]
open(OUT, "w").write(head + "\n".join(ev) + "\n")
open(SRT, "w").write("\n".join(srt))
for e in ev: print(e.split(",,",1)[0].split(",")[1], e.split("}",1)[1])
