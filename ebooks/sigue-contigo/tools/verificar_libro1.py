#!/usr/bin/env python3
"""Comprueba que el remaquetado del eBook no ha perdido ni una letra.

Compara los dos PDF como flujos de caracteres sin espacios. Así dan igual los
saltos de línea, la partición de párrafos y el letter-spacing de los rótulos
(que el extractor devuelve como "C A P Í T U L O"): lo único que queda es el
contenido. Sale con código 1 si algo del original no está en el nuevo.
"""
import re, sys, unicodedata
from pypdf import PdfReader

ORIG = 'tools/original_libro1.pdf'
NUEVO = 'pdf/1. Sigue Contigo - eBook completo.pdf'

# Paginería propia de cada edición: no es contenido del libro.
LINEAS_FUERA = {
    'orig': [re.compile(r'^\s*tremdora\s*$'),
             re.compile(r'^\s*—\s*\d+\s*—\s*$')],
    'nuevo': [],
}
QUITAR_EN_LINEA = {
    'orig': [],
    'nuevo': [re.compile(r'Sigue Contigo · Libro 1 de 4\s*\d*')],
}
# Rótulos con letter-spacing, que el extractor devuelve letra a letra.
CHROME_CHAR = {
    'orig': [],
    'nuevo': [r'libro1de4·ellibro', r'primerlibrodelaserie', r'paraterminar'],
}


def flujo(ruta, cual):
    crudo = '\n'.join((p.extract_text() or '') for p in PdfReader(ruta).pages)
    lineas = []
    for linea in crudo.split('\n'):
        for pat in QUITAR_EN_LINEA[cual]:
            linea = pat.sub(' ', linea)
        if not linea.strip():
            continue
        if any(pat.match(linea) for pat in LINEAS_FUERA[cual]):
            continue
        lineas.append(linea)
    texto = '\n'.join(lineas)
    chrome = CHROME_CHAR[cual]
    t = unicodedata.normalize('NFC', texto).lower()
    t = (t.replace('’', "'").replace('‘', "'")
          .replace('“', '"').replace('”', '"')
          .replace('—', '-').replace('–', '-').replace('‑', '-')
          .replace(' ', ''))
    t = re.sub(r'\s+', '', t)
    for patron in chrome:
        t = re.sub(patron, '', t)
    return t


def contexto(fuente, ini, fin, margen=45):
    return fuente[max(0, ini - margen):fin + margen]


a = flujo(ORIG, 'orig')
b = flujo(NUEVO, 'nuevo')

import difflib
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
perdido, anadido = [], 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag in ('delete', 'replace'):
        perdido.append((i1, i2, a[i1:i2], contexto(a, i1, i2)))
    elif tag == 'insert':
        anadido += j2 - j1

iguales = sum(bl.size for bl in sm.get_matching_blocks())
print('original : %6d caracteres' % len(a))
print('nuevo    : %6d caracteres (%d añadidos por la nueva edición)' % (len(b), anadido))
print('conserva : %6d  ->  %.3f%% del original' % (iguales, 100.0 * iguales / len(a)))
print()

if perdido:
    total = sum(len(p[2]) for p in perdido)
    print('!! FALTAN %d caracteres del original en %d tramos:' % (total, len(perdido)))
    for _, _, trozo, ctx in perdido[:30]:
        print('   falta: %r' % trozo[:120])
        print('   en   : ...%s...' % ctx[:150])
    sys.exit(1)

print('OK · el nuevo PDF contiene el 100% del texto del original')
