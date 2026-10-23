# -*- coding: utf-8 -*-
"""Extrae el eBook original con posición, fuente y tamaño de cada línea.

El PDF original se generó con ReportLab, así que la estructura (títulos,
cursivas, cajas de ejercicio) solo se puede recuperar mirando qué fuente y
qué tamaño usa cada fragmento. Esto vuelca esos datos en JSON.
"""
import json, sys
from collections import defaultdict
from pypdf import PdfReader

SRC = sys.argv[1] if len(sys.argv) > 1 else 'assets/1. Sigue Contigo - eBook completo.pdf'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'tools/libro1_raw.json'

reader = PdfReader(SRC)
paginas = []

for n, page in enumerate(reader.pages, start=1):
    trozos = []

    def visit(text, cm, tm, font_dict, font_size, _t=trozos):
        if not text or not text.strip():
            return
        base = ''
        if isinstance(font_dict, dict):
            base = str(font_dict.get('/BaseFont', ''))
        _t.append({'x': round(tm[4], 1), 'y': round(tm[5], 1),
                   'size': round(font_size, 1), 'font': base.split('+')[-1],
                   'text': text})

    page.extract_text(visitor_text=visit)

    # Agrupar trozos en líneas por coordenada Y
    lineas = defaultdict(list)
    for t in trozos:
        lineas[t['y']].append(t)
    salida = []
    for y in sorted(lineas, reverse=True):
        parts = sorted(lineas[y], key=lambda t: t['x'])
        texto = ''.join(p['text'] for p in parts).strip()
        if not texto:
            continue
        salida.append({
            'y': y,
            'x': min(p['x'] for p in parts),
            'x_fin': round(max(p['x'] + len(p['text']) * p['size'] * 0.5
                               for p in parts), 1),
            'size': max(p['size'] for p in parts),
            'fonts': sorted({p['font'] for p in parts}),
            'text': texto,
        })
    paginas.append({'pagina': n, 'lineas': salida})

json.dump(paginas, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

hist = defaultdict(int)
for p in paginas:
    for l in p['lineas']:
        hist[(l['size'], tuple(l['fonts']))] += 1
print('páginas:', len(paginas), '| líneas:', sum(len(p['lineas']) for p in paginas))
print('\nestilos encontrados (tamaño, fuentes) -> nº de líneas:')
for k, v in sorted(hist.items(), key=lambda x: -x[1]):
    print('   %-5s %-40s %4d' % (k[0], ', '.join(k[1]), v))
