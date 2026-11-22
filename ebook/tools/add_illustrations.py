# Inserta ilustraciones de línea (SVG) bajo el título de cada capítulo.
import re, sys
p = sys.argv[1]; s = open(p).read()
HEART = "M0,4 C-6,-2 -10,-6 -6,-10 C-3,-13 0,-11 0,-8 C0,-11 3,-13 6,-10 C10,-6 6,-2 0,4 Z"
SPARK = "M0,-5 Q0,0 5,0 Q0,0 0,5 Q0,0 -5,0 Q0,0 0,-5Z"
def heart(x, y, k=1, fill=False):
    f = 'fill="var(--accent)" fill-opacity=".18"' if fill else ''
    return f'<path d="{HEART}" transform="translate({x},{y}) scale({k})" {f}/>'
def paw(x, y, k=1, r=0, op=1):
    return f'<use href="#paw" transform="translate({x},{y}) rotate({r}) scale({k})" opacity="{op}"/>'
def spark(x, y, k=1):
    return f'<path d="{SPARK}" transform="translate({x},{y}) scale({k})" fill="var(--accent)" fill-opacity=".35"/>'
side = '<path d="M8,{y} L{a},{y}" opacity=".45"/><path d="M{b},{y} L152,{y}" opacity=".45"/>'
def lines(y, a, b): return side.format(y=y, a=a, b=b)

ILL = {
 'p-carta':  # sobre con un corazón que sale
   lines(44,36,124) + '<rect x="42" y="24" width="76" height="40" rx="3"/><path d="M42,26 L80,48 L118,26"/>'
   + heart(80, 14, 1.0, True) + spark(104, 10, .7) + spark(58, 8, .55),
 'p-1':  # latido: línea de pulso y corazón
   '<path d="M8,42 L58,42 L64,42 L69,30 L75,56 L81,24 L87,48 L91,42 L152,42"/>' + heart(118, 24, 1.1, True),
 'p-2':  # huella dentro de un corazón: el vínculo
   lines(36,40,120) + heart(80, 50, 3.0) + paw(80, 34, .85),
 'p-3':  # el oleaje
   '<path d="M8,32 Q28,20 48,32 T88,32 T128,32 T168,32"/>'
   '<path d="M8,44 Q28,32 48,44 T88,44 T128,44 T168,44" opacity=".65"/>'
   '<path d="M8,56 Q28,44 48,56 T88,56 T128,56 T168,56" opacity=".35"/>'
   '<circle cx="124" cy="13" r="6" fill="var(--accent)" fill-opacity=".18"/>',
 'p-4':  # conversaciones
   '<path d="M46,38 L42,50 L58,38" fill="var(--paper)"/><rect x="28" y="12" width="56" height="27" rx="13" fill="var(--paper)"/>'
   '<circle cx="46" cy="25.5" r="1.6" fill="var(--accent)"/><circle cx="56" cy="25.5" r="1.6" fill="var(--accent)"/><circle cx="66" cy="25.5" r="1.6" fill="var(--accent)"/>'
   '<path d="M118,52 L124,62 L106,52" fill="var(--paper)"/><rect x="78" y="27" width="56" height="26" rx="13" fill="var(--paper)"/>'
   + heart(106, 42, .85, True),
 'p-5':  # luna y estrellas: dejar ir en paz
   lines(36,50,112) + '<path d="M86,19.2 A16,16 0 1,0 86,48.8 A17,17 0 0,1 86,19.2 Z" fill="var(--accent)" fill-opacity=".14"/>'
   + spark(104, 18, 1) + spark(114, 36, .7) + spark(58, 14, .6) + spark(98, 52, .5),
 'p-6':  # brote: herramientas para crecer
   lines(62,48,112) + '<path d="M80,62 C80,52 80,42 80,28"/>'
   '<path d="M80,46 C70,44 61,36 63,27 C72,29 79,36 80,46Z" fill="var(--accent)" fill-opacity=".14"/>'
   '<path d="M80,36 C89,32 97,24 95,15 C86,17 80,25 80,36Z" fill="var(--accent)" fill-opacity=".14"/>',
 'p-7':  # urna y vela
   lines(62,40,124) + '<path d="M54,62 L76,62 C81,52 81,41 75,33 L55,33 C49,41 49,52 54,62Z"/>'
   '<path d="M56,33 L74,33 M59,33 C59,27 71,27 71,33"/><circle cx="65" cy="25" r="1.8"/>' + heart(65, 48, .7, True)
   + '<rect x="94" y="38" width="12" height="24" rx="1.5"/><path d="M100,38 L100,33"/>'
   '<path d="M100,32 C96,27 97.5,21 100,16 C102.5,21 104,27 100,32Z" fill="var(--accent)" fill-opacity=".25"/>',
 'p-8':  # una casa con amor de nuevo
   lines(62,46,114) + '<path d="M54,62 L54,36 L80,15 L106,36 L106,62"/><path d="M48,40 L80,12 L112,40" opacity=".45"/>'
   + heart(80, 48, 1.3, True) + spark(118, 18, .6),
 'p-9':  # cometa: la infancia
   '<path d="M80,6 L95,25 L80,46 L65,25 Z" fill="var(--accent)" fill-opacity=".12"/><path d="M80,6 L80,46 M65,25 L95,25" opacity=".6"/>'
   '<path d="M80,46 C74,52 88,56 80,62 C74,66 84,70 82,72"/>'
   '<path d="M77,53 L83,51 M79,61 L85,59" />' + heart(116, 20, .7, True) + spark(48, 16, .7) + spark(124, 46, .5),
 'p-10':  # dos rastros de huellas que caminan juntos
   paw(56, 52, .75, -12) + paw(74, 28, .75, -12) + paw(96, 56, .5, 12) + paw(108, 36, .5, 12) + paw(120, 17, .5, 12),
 'p-final':  # huellas que llevan a un corazón
   paw(26, 52, .5, 35, .4) + paw(46, 42, .5, 35, .55) + paw(64, 52, .5, 35, .7) + paw(84, 42, .5, 35, .85)
   + heart(118, 44, 1.7, True),
 'p-rec':  # libro abierto
   '<path d="M80,26 C70,20 52,20 40,24 L40,60 C52,56 70,56 80,62 C90,56 108,56 120,60 L120,24 C108,20 90,20 80,26 Z M80,26 L80,62"/>'
   '<path d="M48,32 L72,31 M48,40 L72,39 M88,31 L112,32 M88,39 L112,40" opacity=".4"/>' + heart(80, 14, .9, True),
}
DEFS = ('<svg width="0" height="0" style="position:absolute"><defs><g id="paw">'
        '<path d="M-9,6 C-9,-1 -4,-4 0,-4 C4,-4 9,-1 9,6 C9,10 5,11 0,9 C-5,11 -9,10 -9,6 Z" fill="var(--accent)" fill-opacity=".18"/>'
        '<ellipse cx="-11" cy="-6" rx="3" ry="4" transform="rotate(-20 -11 -6)"/><ellipse cx="-4" cy="-12" rx="3" ry="4.3"/>'
        '<ellipse cx="4" cy="-12" rx="3" ry="4.3"/><ellipse cx="11" cy="-6" rx="3" ry="4" transform="rotate(20 11 -6)"/>'
        '</g></defs></svg>')
def svg(inner, w='46mm'):
    return (f'<div class="ill"><svg viewBox="0 0 160 72" style="width:{w}" fill="none" stroke="var(--accent)" '
            f'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg></div>')
for key, inner in ILL.items():
    pat = re.compile(r'(data-mark="%s">.*?)<div class="orn">——— · ———</div>' % re.escape(key), re.S)
    s, n = pat.subn(lambda m: m.group(1) + svg(inner), s, count=1); assert n == 1, key
# Portada: huella en corazón; página de cierre: rastro de huellas
s = s.replace('<h1>Sigue<br>contigo</h1>\n    <div class="orn">——— · ———</div>',
              '<h1>Sigue<br>contigo</h1>\n    ' + svg(lines(36,40,120) + heart(80, 50, 3.0) + paw(80, 34, .85), '40mm'), 1)
s = s.replace('<div class="closing">',
              '<div class="closing">' + svg(paw(40, 56, .5, 30, .3) + paw(62, 44, .5, 30, .5) + paw(82, 54, .5, 30, .7)
                                              + paw(104, 42, .5, 30, .85) + paw(124, 52, .5, 30, 1), '44mm'), 1)
s = s.replace('<body>\n', '<body>\n' + DEFS + '\n', 1)
s = s.replace('  .note {', '  .ill { text-align:center; margin: .3em 0 .6em; line-height:0; }\n  .ill svg { height:auto; }\n  .ill svg *, #paw * { vector-effect: non-scaling-stroke; }\n  .note {', 1)
s = s.replace('text-transform:uppercase; margin-top: 20mm; }', 'text-transform:uppercase; margin-top: 4mm; }')
open(p, 'w').write(s)
