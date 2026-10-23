# -*- coding: utf-8 -*-
"""Convierte el eBook original en bloques estructurados, sin tocar el texto.

El PDF original se maquetó con ReportLab; el modo de extracción "layout"
conserva sangrías y líneas en blanco, y eso basta para reconocer títulos,
citas centradas, listas y cajas de ejercicio. El texto se copia literal:
aquí solo se decide qué es cada bloque.
"""
import json, re, sys
from pypdf import PdfReader

SRC = sys.argv[1] if len(sys.argv) > 1 else 'assets/1. Sigue Contigo - eBook completo.pdf'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'tools/libro1_bloques.json'

FURNITURE = re.compile(r'^\s*(tremdora|—\s*\d+\s*—)\s*$')
RE_CAP    = re.compile(r'^\s*(CAP[ÍI]TULO\s+[IVX]+|ANTES DE EMPEZAR|CARTA FINAL)\s*$')
RE_EJER   = re.compile(r'^\s*—\s*EJERCICIO\s+\d+\s*—\s*$')
RE_BULLET = re.compile(r'^\s*·\s+')
RE_NUM    = re.compile(r'^\s*\d+\.\s+')
RE_PORQUE = re.compile(r'^\s*Por qué funciona:')

reader = PdfReader(SRC)
bloques = []

def indent(line):
    return len(line) - len(line.lstrip())

for n, page in enumerate(reader.pages, start=1):
    texto = page.extract_text(extraction_mode='layout')
    crudos = re.split(r'\n\s*\n', texto)
    for crudo in crudos:
        lineas = [l.rstrip() for l in crudo.split('\n') if l.strip()]
        lineas = [l for l in lineas if not FURNITURE.match(l)]
        if not lineas:
            continue
        sangria = min(indent(l) for l in lineas)
        limpio = [l.strip() for l in lineas]
        texto_plano = ' '.join(limpio)

        if RE_EJER.match(limpio[0]):
            tipo = 'ejercicio_titulo'
        elif RE_CAP.match(limpio[0]):
            tipo = 'capitulo'
        elif RE_PORQUE.match(limpio[0]):
            tipo = 'porque'
        elif all(RE_BULLET.match(l) or indent(o) > sangria + 2
                 for l, o in zip(limpio, lineas)) and RE_BULLET.match(limpio[0]):
            tipo = 'lista'
        elif RE_NUM.match(limpio[0]):
            tipo = 'numerada'
        elif sangria >= 12:
            tipo = 'cita'
        elif (len(limpio) <= 2 and len(texto_plano) < 62
              and not texto_plano.endswith(('.', ':', '»', '?', '!'))):
            tipo = 'subtitulo'
        else:
            tipo = 'parrafo'

        bloques.append({'pagina': n, 'tipo': tipo, 'sangria': sangria,
                        'lineas': limpio, 'texto': texto_plano})

# Unir párrafos partidos entre páginas: si un bloque empieza en minúscula y el
# anterior no cerró frase, es continuación del anterior.
unidos = []
for b in bloques:
    prev = unidos[-1] if unidos else None
    cont = (prev and b['tipo'] == 'parrafo' == prev['tipo']
            and b['pagina'] != prev['pagina']
            and b['texto'][:1].islower()
            and not prev['texto'].endswith(('.', ':', '»', '?', '!')))
    if cont:
        prev['lineas'] += b['lineas']
        prev['texto'] = prev['texto'] + ' ' + b['texto']
    else:
        unidos.append(b)

json.dump(unidos, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

from collections import Counter
print('bloques:', len(unidos))
print(Counter(b['tipo'] for b in unidos).most_common())
