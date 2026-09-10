# -*- coding: utf-8 -*-
"""Sigue Contigo — portada de bienvenida del pack (una página).

El listado de contenidos se genera a partir de lo que hay realmente en
`pdf/` y `assets/`, para que al añadir la frecuencia u otro material
la página se actualice sola en la siguiente ejecución.
"""
import os, sys

D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(D)
CSS = open(os.path.join(D, 'tremdora.css'), encoding='utf-8').read()

AUDIO_EXT = {'.mp3', '.wav', '.m4a', '.flac', '.aac', '.ogg'}

LIBROS = [
    ("1. Sigue Contigo - eBook completo.pdf", "El libro",
     "Diez capítulos y quince ejercicios. Sostiene todo lo demás."),
    ("2. Sigue Contigo - Diario del Oleaje.pdf", "Para escribir cada noche",
     "Ocho semanas de registro. Tres minutos antes de dormir."),
    ("3. Sigue Contigo - Plan Practico 8 Semanas.pdf", "Para saber qué hacer hoy",
     "Cincuenta y seis tareas pequeñas, una por día."),
    ("4. Sigue Contigo - Ellos Tambien se Despiden.pdf", "Si quedó otro animal en casa",
     "Qué vigilar, cuándo llamar al veterinario y un protocolo de 21 días."),
]


def extras():
    """Material adicional presente en assets/ (audio de frecuencia, etc.)."""
    out = []
    adir = os.path.join(ROOT, 'assets')
    for name in sorted(os.listdir(adir)) if os.path.isdir(adir) else []:
        ext = os.path.splitext(name)[1].lower()
        if ext in AUDIO_EXT:
            out.append((name, "Para escuchar",
                        "Ponla baja, de fondo, mientras lees o escribes."))
    return out


def card(fname, kicker, desc):
    return ('<tr><td><b>%s</b></td><td><span style="color:#748156;font-weight:bold">'
            '%s.</span> %s</td></tr>') % (fname, kicker, desc)


def build():
    piezas = [(f, k, d) for f, k, d in LIBROS
              if os.path.exists(os.path.join(ROOT, 'pdf', f))
              or os.path.exists(os.path.join(ROOT, 'assets', f))]
    piezas += extras()
    cards = ('<table><thead><tr><th style="width:150pt">El archivo</th>'
             '<th>Qué es y cuándo abrirlo</th></tr></thead><tbody>%s</tbody></table>'
             % ''.join(card(*p) for p in piezas))

    NUM = {1: 'Una pieza', 2: 'Dos piezas', 3: 'Tres piezas', 4: 'Cuatro piezas',
           5: 'Cinco piezas', 6: 'Seis piezas', 7: 'Siete piezas'}
    cuantas = NUM.get(len(piezas), '%d piezas' % len(piezas))

    page = '''
<p class="eyebrow">Sigue Contigo · pack completo</p>
<h1 class="title">Empieza por aquí</h1>
<p class="lead">%s. No hace falta que las leas todas, ni en orden, ni hoy:
esto no está para leerse de una sentada, sino para acompañarte durante las
próximas semanas. Ábrelo por donde puedas.</p>

%s

<div class="box green">
  <p class="lbl">Un orden que funciona</p>
  <p>Empieza por <strong>el eBook</strong>. Esa misma noche abre el
  <strong>Diario</strong> y escribe tu primera línea, aunque el libro lo lleves a
  medias. Al tercer o cuarto día, el <strong>Plan</strong>. Y si quedó otro animal
  en casa, el <strong>libro cuarto</strong> desde hoy: él no puede esperar.</p>
</div>

<div class="box left-terra">
  <p class="lbl">Si hoy no puedes con nada</p>
  <p>Ve directamente a la página «Cuando la ola te sobrepasa», en el Diario del
  Oleaje: tres herramientas de dos minutos. No necesitas haber leído nada antes.</p>
</div>

<p class="note">El Diario y el Plan están pensados para imprimirse y escribirse a
mano; puedes fotocopiar las páginas semanales las veces que necesites.</p>

<div class="quote green" style="margin:12pt 22pt 0">No estás sola. No estás solo.</div>

''' % (cuantas, cards)

    html = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<title>Sigue Contigo — Empieza por aquí</title><style>%s</style>'
            '</head><body><div class="page">%s</div></body></html>') % (CSS, page)
    out = os.path.join(D, '0-empieza-por-aqui.html')
    open(out, 'w', encoding='utf-8').write(html)
    print('escrito 0-empieza-por-aqui.html · %d piezas listadas' % len(piezas))


if __name__ == '__main__':
    build()
