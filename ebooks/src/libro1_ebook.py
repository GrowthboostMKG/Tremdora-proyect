# -*- coding: utf-8 -*-
"""Sigue Contigo — Libro 1 de 4 · eBook completo, remaquetado.

Toma los bloques extraídos del PDF original (tools/libro1_bloques.json), los
viste con el sistema editorial de la serie y los reparte en páginas midiendo
la altura real de cada bloque en Chromium. El texto NO se toca: cada bloque se
copia literal desde el original.
"""
import html as H
import json, os, re, subprocess, sys, tempfile

D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(D)
CSS = open(os.path.join(D, 'tremdora.css'), encoding='utf-8').read()
CHROME = os.environ.get('CHROME', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome')

ALTO_PAGINA = 679.92
PAD_SUP, PAD_INF = 44.0, 34.0
ALTO_UTIL = ALTO_PAGINA - PAD_SUP - PAD_INF          # 601.92 pt
ANCHO_UTIL = 468 - 96                                # 372 pt

BLOQUES = json.load(open(os.path.join(ROOT, 'tools', 'libro1_bloques.json'),
                         encoding='utf-8'))

EXTRA = '''
.b{ margin:0 0 9pt; }
.b:last-child{ margin-bottom:0; }
.b.h2{ margin:15pt 0 6pt; }
.b.cap{ margin:0 0 16pt; }
.b.quote{ margin:16pt 22pt; }
.b.ejer{ margin:14pt 0; }
.ded{ font-family:'Liberation Serif',Georgia,serif; font-size:12.5pt;
      line-height:1.85; text-align:center; color:var(--ink-soft); }
.idx{ font-size:9.6pt; line-height:1.5; padding:5.5pt 0;
      border-bottom:.7pt solid var(--line); }
.idx b{ font-family:'Liberation Serif',Georgia,serif; font-weight:bold;
        font-size:10.2pt; color:var(--ink); }
.ejer-box{ border:.9pt solid var(--line); border-radius:6pt; background:var(--paper);
           padding:13pt 15pt; }
.ejer-box .mk{ font-size:7.8pt; letter-spacing:1.9pt; text-transform:uppercase;
               font-weight:bold; color:var(--terra); margin:0 0 4pt; }
.ejer-box .ti{ font-family:'Liberation Serif',Georgia,serif; font-size:12pt;
               font-weight:bold; margin:0 0 9pt; line-height:1.3; }
.ejer-box p{ font-size:9pt; margin:0 0 7pt; }
.ejer-box ol, .ejer-box ul{ margin:0 0 7pt; padding-left:14pt; }
.ejer-box li{ font-size:9pt; line-height:1.6; margin-bottom:4pt; }
.ejer-box .pq{ font-size:8.4pt; line-height:1.6; font-style:italic;
               color:var(--muted); margin:9pt 0 0; padding-top:8pt;
               border-top:.7pt solid var(--line); }
.ejer-box .pq b{ font-style:normal; color:var(--terra-soft); }
.lst{ list-style:none; margin:0 0 9pt; padding:0; }
.lst li{ font-size:9.5pt; line-height:1.72; margin-bottom:5pt;
         padding-left:13pt; text-indent:-13pt; }
.ejer-box .lst li{ font-size:9pt; line-height:1.6; margin-bottom:4pt; }
.firma{ font-family:'Liberation Serif',Georgia,serif; font-style:italic;
        font-size:10.5pt; line-height:1.7; color:var(--ink-soft); }
'''
CSS += EXTRA


def esc(t):
    return H.escape(t, quote=False)


def br(lineas):
    return '<br>'.join(esc(l) for l in lineas)


# --------------------------------------------------------------- localizar hitos
def indice_de(pred, desde=0):
    for i in range(desde, len(BLOQUES)):
        if pred(BLOQUES[i]):
            return i
    raise SystemExit('no se encontró un bloque esperado en el original')


I_INDICE = indice_de(lambda b: b['texto'].strip() == 'Índice')
I_ENTRADAS = I_INDICE + 1
I_CUERPO = indice_de(lambda b: b['tipo'] == 'capitulo')
I_RECURSOS = indice_de(lambda b: b['texto'].startswith('Recursos que pueden ayudarte'))

assert I_INDICE == 6 and I_CUERPO == 19, (I_INDICE, I_CUERPO)
ENTRADAS = BLOQUES[I_ENTRADAS:I_CUERPO]
assert len(ENTRADAS) == 12, len(ENTRADAS)


# ------------------------------------------------------------------ renderizado
RE_EJ = re.compile(r'^—\s*(EJERCICIO\s+\d+)\s*—\s*(.*)$')
RE_CAP = re.compile(r'^(CAPÍTULO\s+[IVX]+|ANTES DE EMPEZAR|CARTA FINAL)\s+(.*)$')


RE_MARCA = re.compile(r'^(?:·|\d+\.)\s')


def lista_html(lineas):
    """Lista con el marcador tal cual venía en el original, sin renumerar.

    En el PDF de origen cada punto puede ocupar varias líneas; las que no
    empiezan por marcador son continuación del punto anterior, no un punto nuevo.
    """
    items = []
    for l in lineas:
        if RE_MARCA.match(l) or not items:
            items.append(l)
        else:
            items[-1] += ' ' + l
    return '<ul class="lst">%s</ul>' % ''.join('<li>%s</li>' % esc(i) for i in items)


def render_ejercicio(bloques):
    """Un ejercicio completo: marcador, título, cuerpo y el «por qué funciona»."""
    cab = bloques[0]
    m = RE_EJ.match(cab['texto'])
    cuerpo, i = [], 1
    while i < len(bloques):
        b = bloques[i]
        if b['tipo'] == 'porque':
            t = esc(b['texto'])
            t = t.replace('Por qué funciona:', '<b>Por qué funciona:</b>', 1)
            cuerpo.append('<p class="pq">%s</p>' % t)
        elif b['tipo'] in ('numerada', 'lista'):
            # Los puntos de una misma lista llegan como bloques sueltos: se unen.
            lineas = []
            while i < len(bloques) and bloques[i]['tipo'] == b['tipo']:
                lineas += bloques[i]['lineas']
                i += 1
            cuerpo.append(lista_html(lineas))
            continue
        else:
            cuerpo.append('<p>%s</p>' % esc(b['texto']))
        i += 1
    marca = '— %s —' % m.group(1)          # los guiones son del original
    return ('<div class="ejer-box"><p class="mk">%s</p><p class="ti">%s</p>%s</div>'
            % (esc(marca), esc(m.group(2)), ''.join(cuerpo)))


def render(b, extra=None):
    t = b['tipo']
    if t == 'capitulo':
        m = RE_CAP.match(b['texto'])
        lead = ('<p class="lead" style="margin:0">%s</p>' % esc(extra['texto'])) if extra else ''
        return ('<p class="eyebrow">%s</p><h1 class="title" style="margin-bottom:%s">%s</h1>%s'
                % (esc(m.group(1)), '8pt' if lead else '0', esc(m.group(2)), lead))
    if t == 'cita':
        return '<div class="quote">%s</div>' % br(b['lineas'])
    if t == 'subtitulo':
        if b['texto'].startswith('Con todo el cariño'):
            return '<div class="firma">%s</div>' % br(b['lineas'])
        return '<h2 class="sec" style="margin:0">%s</h2>' % br(b['lineas'])
    if t in ('lista', 'numerada'):
        return lista_html(b['lineas'])
    return '<p>%s</p>' % esc(b['texto'])


CLASE = {'capitulo': 'cap', 'cita': 'quote', 'subtitulo': 'h2'}


def construir_unidades():
    """Une los bloques en unidades atómicas de maquetación."""
    uds, i = [], I_CUERPO
    while i < I_RECURSOS:
        b = BLOQUES[i]
        if b['tipo'] == 'ejercicio_titulo':
            j = i + 1
            while j < len(BLOQUES) and BLOQUES[j]['tipo'] != 'porque':
                j += 1
            uds.append({'clase': 'ejer', 'salto': False,
                        'html': render_ejercicio(BLOQUES[i:j + 1]),
                        'ids': list(range(i, j + 1))})
            i = j + 1
            continue
        if b['tipo'] == 'capitulo':
            sig = BLOQUES[i + 1]
            lead = (len(sig['texto']) < 80 and len(sig['lineas']) == 1
                    and sig['tipo'] in ('parrafo', 'cita', 'subtitulo'))
            uds.append({'clase': 'cap', 'salto': True,
                        'html': render(b, sig if lead else None),
                        'ids': [i] + ([i + 1] if lead else [])})
            i += 2 if lead else 1
            continue
        if b['tipo'] in ('numerada', 'lista'):
            lineas, ids, j = [], [], i
            while j < I_RECURSOS and BLOQUES[j]['tipo'] == b['tipo']:
                lineas += BLOQUES[j]['lineas']
                ids.append(j)
                j += 1
            uds.append({'clase': '', 'salto': False,
                        'html': lista_html(lineas), 'ids': ids})
            i = j
            continue
        uds.append({'clase': CLASE.get(b['tipo'], ''), 'salto': False,
                    'html': render(b), 'ids': [i]})
        i += 1
    return uds


# --------------------------------------------------- medición real en Chromium
def medir(uds):
    piezas = ''.join('<div class="b %s" data-i="%d">%s</div>' % (u['clase'], k, u['html'])
                     for k, u in enumerate(uds))
    probe = '''<script>
    var o=[];document.querySelectorAll('.b').forEach(function(e){
      var s=getComputedStyle(e);
      o.push(e.dataset.i+':'+(e.getBoundingClientRect().height
             +parseFloat(s.marginBottom)).toFixed(2));});
    var d=document.createElement('div');d.id='m';d.textContent='M['+o.join(' ')+']';
    document.body.appendChild(d);</script>'''
    doc = ('<!doctype html><meta charset="utf-8"><style>%s\n'
           '.col{width:%spt;}</style><div class="col">%s</div>%s'
           % (CSS, ANCHO_UTIL, piezas, probe))
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False,
                                     encoding='utf-8') as fh:
        fh.write(doc); tmp = fh.name
    try:
        dom = subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu',
                              '--virtual-time-budget=5000', '--dump-dom', tmp],
                             capture_output=True, text=True, timeout=180).stdout
    finally:
        os.unlink(tmp)
    m = re.search(r'id="m"[^>]*>M\[(.*?)\]</div>', dom)
    if not m:
        raise SystemExit('no se pudo medir la altura de los bloques')
    alturas = {}
    for par in m.group(1).split():
        k, v = par.split(':')
        alturas[int(k)] = float(v)
    if len(alturas) != len(uds):
        raise SystemExit('medidas incompletas: %d de %d' % (len(alturas), len(uds)))
    return alturas


def paginar(uds, alturas):
    paginas, actual, usado = [], [], 0.0
    for k, u in enumerate(uds):
        h = alturas[k]
        if (u['salto'] and actual) or (usado + h > ALTO_UTIL and actual):
            paginas.append(actual)
            actual, usado = [], 0.0
        actual.append(u)
        usado += h
    if actual:
        paginas.append(actual)
    return paginas


# ------------------------------------------------------------ páginas fijas
FOOT = ('<div class="pfoot"><span>Sigue Contigo · Libro 1 de 4</span>'
        '<span class="n">{}</span></div>')

EMBLEM = '''
<svg viewBox="0 0 150 150">
  <circle cx="75" cy="75" r="62" fill="none" stroke="#748156" stroke-width="1.1"/>
  <path d="M75 108 C52 90 44 76 44 64 c0-11 9-19 19-19 6 0 10 3 12 7
           2-4 6-7 12-7 10 0 19 8 19 19 0 12-8 26-31 44z"
        fill="#f6e9d6" stroke="#a8502e" stroke-width="1.6" stroke-linejoin="round"/>
  <ellipse cx="75" cy="76" rx="7.5" ry="6" fill="#e2cfb4"/>
  <ellipse cx="67" cy="65" rx="2.8" ry="4" fill="#e2cfb4" transform="rotate(-18 67 65)"/>
  <ellipse cx="75" cy="61" rx="2.8" ry="4.2" fill="#e2cfb4"/>
  <ellipse cx="83" cy="65" rx="2.8" ry="4" fill="#e2cfb4" transform="rotate(18 83 65)"/>
</svg>'''


def pagina(inner, n=None, cls=''):
    return '<div class="page %s">%s%s</div>' % (cls, inner, FOOT.format(n) if n else '')


def portada():
    return '''
<div class="badge">Libro 1 de 4 · el libro</div>
<div class="kicker">%s</div>
<div class="emblem">%s</div>
<h1>Sigue <i>contigo</i></h1>
<div class="sub">%s</div>
<div class="foot">Primer libro de la serie <b>Sigue Contigo</b><br>%s</div>
''' % (esc(BLOQUES[0]['texto']), EMBLEM, esc(BLOQUES[2]['texto']),
       esc(BLOQUES[3]['texto']))


def dedicatoria():
    return ('<div style="height:150pt"></div><div class="ded">%s</div>'
            '<div style="height:26pt"></div><div class="ded">%s</div>'
            % (br(BLOQUES[4]['lineas']), br(BLOQUES[5]['lineas'])))


def indice(mapa):
    filas = []
    for b in ENTRADAS:
        partes = b['texto'].split('·', 1)
        izq = partes[0].strip()
        der = partes[1].strip() if len(partes) > 1 else ''
        pg = mapa.get(b['texto'], '')
        filas.append('<div class="idx"><span style="float:right;color:#9c7c63">%s</span>'
                     '<b>%s</b>%s</div>'
                     % (pg, esc(izq), ('  ·  ' + esc(der)) if der else ''))
    return ('<p class="eyebrow">Sigue Contigo</p><h1 class="title">%s</h1>%s'
            % (esc(BLOQUES[I_INDICE]['texto']), ''.join(filas)))


def cierre():
    partes = ['<p class="eyebrow">Para terminar</p>']
    for b in BLOQUES[I_RECURSOS:]:
        if b['tipo'] == 'subtitulo' and b['texto'].startswith('Recursos'):
            partes.append('<h1 class="title">%s</h1>' % esc(b['texto']))
        elif b['tipo'] == 'subtitulo':
            partes.append('<h3 class="sub">%s</h3>' % esc(b['texto']))
        elif b['texto'].startswith('Con todo el cariño'):
            partes.append('<hr class="rule soft"><div class="firma" '
                          'style="text-align:center">%s</div>' % br(b['lineas']))
        else:
            partes.append('<p>%s</p>' % esc(b['texto']))
    return ''.join(partes)


def numero_de_capitulos(paginas, primera):
    """Página real en la que arranca cada entrada del índice."""
    mapa, titulos = {}, []
    for b in ENTRADAS:
        izq = b['texto'].split('·', 1)[0].strip()
        titulos.append((b['texto'], izq.upper().replace('CAPÍTULO', 'CAPÍTULO')))
    for i, pg in enumerate(paginas):
        for u in pg:
            if u['clase'] != 'cap':
                continue
            marca = BLOQUES[u['ids'][0]]['texto']
            for clave, izq in titulos:
                if marca.upper().startswith(izq):
                    mapa.setdefault(clave, primera + i)
    return mapa


def main():
    uds = construir_unidades()
    alturas = medir(uds)
    paginas = paginar(uds, alturas)

    PRE = 3                      # portada, dedicatoria, índice
    mapa = numero_de_capitulos(paginas, PRE + 1)

    cuerpo = []
    for i, pg in enumerate(paginas):
        inner = ''.join('<div class="b %s">%s</div>' % (u['clase'], u['html']) for u in pg)
        cuerpo.append(pagina(inner, PRE + 1 + i))

    total = PRE + len(paginas)
    html_pags = [pagina(portada(), cls='cover'),
                 pagina(dedicatoria(), 2),
                 pagina(indice(mapa), 3)]
    html_pags += cuerpo
    html_pags.append(pagina(cierre(), total + 1))

    doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
           '<title>Sigue Contigo — eBook completo</title><style>%s</style>'
           '</head><body>%s</body></html>') % (CSS, ''.join(html_pags))
    salida = os.path.join(D, 'libro1-ebook-completo.html')
    open(salida, 'w', encoding='utf-8').write(doc)
    print('escrito libro1 · %d páginas (original: 57)' % len(html_pags))
    faltan = [b['texto'][:40] for b in ENTRADAS if b['texto'] not in mapa]
    if faltan:
        print('  aviso: sin número de página en el índice:', faltan)


if __name__ == '__main__':
    main()
