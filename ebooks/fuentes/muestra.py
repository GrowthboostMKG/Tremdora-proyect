#!/usr/bin/env python3
"""Genera las muestras gratuitas a partir de los libros completos.

Las páginas se extraen del HTML del libro completo, no se reescriben, para que
las dos versiones nunca se desincronicen: lo que se corrija en el completo
aparece en la muestra la próxima vez que se genere.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent


def secciones(html: str):
    """Devuelve la lista de secciones .page completas, con su etiqueta."""
    out = []
    for m in re.finditer(r'<section class="page[^"]*">.*?</section>', html, re.S):
        out.append(m.group(0))
    return out


def buscar(secs, marca):
    hits = [s for s in secs if marca in s]
    if len(hits) != 1:
        sys.exit(f"«{marca}»: {len(hits)} coincidencias (debe haber 1)")
    return hits[0]


CABECERA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{titulo} — muestra gratuita · Tremdora</title>
<style>/*CSS*/</style>
<style>:root{{--accent:{acento};--accent-soft:{acento_claro};}}</style>
</head>
<body>
"""


def construir(libro: str, cfg: dict):
    completo = (HERE / f"{libro}.html").read_text(encoding="utf-8")
    secs = secciones(completo)

    paginas = [cfg["cubierta"], cfg["que_es"]]
    for marca in cfg["del_completo"]:
        paginas.append(buscar(secs, marca))
    paginas.insert(cfg["pos_anticipo"], cfg["anticipo"])
    paginas.append(buscar(secs, "Diecisiete años"))
    paginas.append(cfg["cierre"])

    html = CABECERA.format(**cfg["head"]) + "\n\n".join(paginas) + "\n\n</body>\n</html>\n"
    destino = HERE / f"muestra-{libro}.html"
    destino.write_text(html, encoding="utf-8")
    print(f"muestra-{libro}.html · {len(paginas)} páginas")
    return destino


def cubierta(titulo_html, subtitulo):
    emblema = """<div class="emblem"><svg viewBox="0 0 150 150">
      <circle cx="75" cy="75" r="62" fill="none" stroke="#748156" stroke-width="1.1"/>
      <path d="M75 108 C52 90 44 76 44 64 c0-11 9-19 19-19 6 0 10 3 12 7
               2-4 6-7 12-7 10 0 19 8 19 19 0 12-8 26-31 44z"
            fill="#f6e9d6" stroke="#a8502e" stroke-width="1.6" stroke-linejoin="round"/>
      <ellipse cx="75" cy="76" rx="7.5" ry="6" fill="#e2cfb4"/>
      <ellipse cx="67" cy="65" rx="2.8" ry="4" fill="#e2cfb4" transform="rotate(-18 67 65)"/>
      <ellipse cx="75" cy="61" rx="2.8" ry="4.2" fill="#e2cfb4"/>
      <ellipse cx="83" cy="65" rx="2.8" ry="4" fill="#e2cfb4" transform="rotate(18 83 65)"/>
    </svg></div>"""
    return f'''<section class="page cover serie">
  <div class="pill">Libro 1 de 3 · El método</div>
  <div class="brandmark">TREMDORA</div>
  {emblema}
  <h1>{titulo_html}</h1>
  <div class="sub">{subtitulo}</div>
  <div class="muestra">Muestra gratuita</div>
  <div class="cv-foot">
    <div class="lbl">Fundamentado en la obra y los hallazgos de</div>
    <div class="names">
      Ivan Pavlov · B. F. Skinner · Konrad Lorenz · Jaak Panksepp<br>
      Alexandra Horowitz · Brian Hare · Margaret Gruen · Temple Grandin
    </div>
    <div class="edi">Dos capítulos completos</div>
  </div>
</section>'''


def cierre(titulo, frase, que_falta):
    filas = "\n".join(f"    <li>{x}</li>" for x in que_falta)
    return f'''<section class="page">
  <div class="kicker">Hasta aquí la muestra</div>
  <h1 class="ch-title">{titulo} entero</h1>
  <div class="ch-who">{frase}</div>

  <p>Lo que acabas de leer son <b>dos capítulos completos</b>, con sus ejercicios y sus fichas, tal cual están en el libro. No es un resumen ni un adelanto recortado: es el libro, en pequeño.</p>

  <p><b>Lo que no cabía en la muestra:</b></p>
  <ul class="diamond">
{filas}
  </ul>

  <div class="cta">
    <span class="big">{titulo}</span>
    Edición completa · Libro 1 de 3
    <span class="web">tremdora.com</span>
    <span class="ig">@tremdora_pets</span>
  </div>
</section>'''


HOGAR = {
    "head": {"titulo": "Hogar en Calma", "acento": "#748156", "acento_claro": "#E6EADA"},
    "cubierta": cubierta(
        "Hogar en <em>Calma</em>",
        "La guía científica y práctica para liberar a tu mascota de la ansiedad — cuando está contigo y cuando se queda sola."),
    "que_es": '''<section class="page toc">
  <h1>Qué tienes en tus manos</h1>
  <p class="toc-dek">Esta muestra trae <b>dos capítulos completos</b> de los diez del libro, con sus ejercicios y sus fichas rápidas, además de la introducción y los fundamentos científicos. Abajo tienes el libro entero, para que veas dónde encaja lo que vas a leer.</p>

  <div class="toc-part">Antes de empezar</div>
  <div class="toc-row"><span class="n">—</span><span class="t">Introducción: por qué tu mascota siente ansiedad<span class="incluido">EN LA MUESTRA</span></span></div>
  <div class="toc-row"><span class="n">—</span><span class="t">Los ocho pilares científicos de este libro<span class="incluido">EN LA MUESTRA</span></span></div>

  <div class="toc-part">Parte I · La ciencia detrás de la calma</div>
  <div class="toc-row"><span class="n">01</span><span class="t">Etología: el lenguaje instintivo del comportamiento</span><span class="who">Lorenz</span></div>
  <div class="toc-row"><span class="n">02</span><span class="t">Neurociencia afectiva: el mapa emocional del cerebro</span><span class="who">Panksepp</span></div>
  <div class="toc-row"><span class="n">03</span><span class="t">Cognición animal: cómo piensan y sienten</span><span class="who">Hare</span></div>
  <div class="toc-row"><span class="n">04</span><span class="t">Teoría del aprendizaje: construir y deshacer el miedo</span><span class="who">Pavlov · Skinner</span></div>
  <div class="toc-row"><span class="n">05</span><span class="t">Lenguaje corporal: leer antes de que grite<span class="incluido">EN LA MUESTRA</span></span><span class="who">Horowitz</span></div>
  <div class="toc-row"><span class="n">06</span><span class="t">Bienestar animal: diseñar un entorno que calma</span><span class="who">Grandin</span></div>
  <div class="toc-row"><span class="n">07</span><span class="t">Comportamiento clínico: cuándo es un diagnóstico</span><span class="who">Gruen</span></div>
  <div class="toc-row"><span class="n">08</span><span class="t">Dolor y comportamiento: el dolor que se disfraza<span class="incluido">EN LA MUESTRA</span></span><span class="who">Gruen</span></div>
  <div class="toc-row"><span class="n">09</span><span class="t">Envejecimiento y deterioro cognitivo</span><span class="who">Gruen · Panksepp</span></div>
  <div class="toc-row"><span class="n">10</span><span class="t">Refuerzo positivo: construir calma paso a paso</span><span class="who">Skinner</span></div>

  <div class="toc-part">Parte II · El programa práctico</div>
  <div class="toc-row"><span class="n">A</span><span class="t">Calma en tu presencia — cinco frentes de trabajo</span></div>
  <div class="toc-row"><span class="n">B</span><span class="t">Ansiedad por separación — protocolo completo</span></div>
  <div class="toc-row"><span class="n">C</span><span class="t">Ansiedad felina — el programa para gatos</span></div>
  <div class="toc-row"><span class="n">D</span><span class="t">Vista previa del Plan Práctico de 8 Semanas</span></div>

  <div class="note mt7">
    <p><b>Por qué estos dos capítulos y no otros:</b> el 5 te enseña a ver la ansiedad <i>antes</i> de que sea una crisis, y el 8 es el que más veces cambia el diagnóstico entero — porque muchas veces lo que parece ansiedad es dolor. Son los dos que más sirven aunque no leas nada más.</p>
  </div>
</section>''',
    "del_completo": [
        "Por qué tu mascota siente ansiedad",
        "rompecabezas",
        "<h2 class=\"ch-title\">Leer antes de que grite</h2>",
        "Ejercicio · Capítulo 05",
        "Ficha rápida · Capítulo 05",
        "<h2 class=\"ch-title\">El dolor que se disfraza de ansiedad</h2>",
        "Ejercicio · Capítulo 08",
        "Ficha rápida · Capítulo 08",
    ],
    "pos_anticipo": 10,
    "anticipo": '''<section class="page">
  <div class="kicker">Un anticipo del programa práctico</div>
  <h1 class="ch-title">¿Es ansiedad, o es aburrimiento?</h1>
  <div class="ch-who">Las primeras líneas del Programa B, que en el libro ocupa doce páginas</div>

  <p class="lead">No son el mismo problema y no se arreglan igual, así que conviene no confundirlos. Hay una pista muy rápida, aunque no es infalible: <b>fíjate en dónde rompe.</b></p>

  <div class="signals">
    <div class="s"><span class="h">Más probable aburrimiento</span><span class="d">Destrozos repartidos por toda la casa, cosas de morder y de manipular, y te recibe como siempre. Pide estimulación y actividad.</span></div>
    <div class="s"><span class="h">Más probable separación</span><span class="d">Concentrado <b>en las salidas</b>: puerta, marco, ventana, persiana. Y suele venir con llanto continuo, babeo, o necesidades dentro de casa habiendo salido antes.</span></div>
  </div>

  <p>Y si son las dos cosas a la vez, también es normal: muchos animales tienen ambas, y entonces se trabajan las dos.</p>

  <p>La pista de la localización te orienta en un minuto. Pero la que decide de verdad es <b>la grabación</b>: media hora de móvil enfocando la puerta, que es el diagnóstico más barato que existe. Un perro que se tumba y se duerme no tiene un problema de separación, aunque luego rompa algo.</p>

  <div class="box warn">
    <span class="lbl">Y aquí se corta la muestra</span>
    <p>Lo que viene después en el libro es <b>el protocolo entero</b>: cómo medir cuánto aguanta de verdad, cómo vaciar de significado las llaves y los zapatos, y la progresión de ausencias —de dos minutos a tres horas— sin pasarte nunca del umbral, porque cada crisis completa retrasa semanas de trabajo.</p>
    <p>Son los pasos que no se pueden improvisar, y los que más veces se hacen mal.</p>
  </div>
</section>''',
    "cierre": cierre(
        "Hogar en Calma",
        "Diez capítulos, tres programas prácticos y una ficha rápida por capítulo",
        [
            "<b>Los ocho capítulos restantes</b>, cada uno con su ejercicio y su ficha: etología, neurociencia afectiva, cognición, aprendizaje, entorno, comportamiento clínico, vejez y refuerzo positivo.",
            "<b>Programa A · Calma en tu presencia:</b> cinco frentes de trabajo para ruidos, visitas y otros animales, con la escalera de exposición de cinco niveles.",
            "<b>Programa B · Ansiedad por separación:</b> el protocolo completo de cinco pasos, con la progresión de ausencias y la regla de oro del umbral.",
            "<b>Programa C · Ansiedad felina:</b> por qué un gato ansioso no monta ruido, sino que se apaga. Las cuatro señales, los recursos, el arenero y la rutina de caza.",
            "<b>Cuándo pedir ayuda profesional</b>, y la bibliografía completa.",
        ]),
}

EDAD = {
    "head": {"titulo": "Edad Dorada", "acento": "#A8502E", "acento_claro": "#F6E9D6"},
    "cubierta": cubierta(
        "Edad <em>Dorada</em>",
        "Guía científica y práctica para cuidar a tu mascota mayor: entender su vejez, cuidar su cuerpo y acompañar su ritmo con amor."),
    "que_es": '''<section class="page toc">
  <h1>Qué tienes en tus manos</h1>
  <p class="toc-dek">Esta muestra trae <b>dos capítulos completos</b> de los diez del libro, con sus ejercicios y sus fichas rápidas, además de la introducción y los fundamentos científicos. Abajo tienes el libro entero, para que veas dónde encaja lo que vas a leer.</p>

  <div class="toc-part">Antes de empezar</div>
  <div class="toc-row"><span class="n">—</span><span class="t">Introducción: el otoño de la vida de tu mascota<span class="incluido">EN LA MUESTRA</span></span></div>
  <div class="toc-row"><span class="n">—</span><span class="t">Los ocho pilares científicos de este libro<span class="incluido">EN LA MUESTRA</span></span></div>

  <div class="toc-part">Parte I · Entender el envejecimiento</div>
  <div class="toc-row"><span class="n">01</span><span class="t">Etología: los instintos que cambian con la edad</span><span class="who">Lorenz</span></div>
  <div class="toc-row"><span class="n">02</span><span class="t">Neurociencia afectiva: un corazón más sensible</span><span class="who">Panksepp</span></div>
  <div class="toc-row"><span class="n">03</span><span class="t">Cognición animal: qué se mantiene y qué se pierde</span><span class="who">Hare</span></div>
  <div class="toc-row"><span class="n">04</span><span class="t">Teoría del aprendizaje: reentrenar rutinas sin estrés</span><span class="who">Pavlov · Skinner</span></div>
  <div class="toc-row"><span class="n">05</span><span class="t">Lenguaje corporal: leer el malestar silencioso<span class="incluido">EN LA MUESTRA</span></span><span class="who">Horowitz</span></div>
  <div class="toc-row"><span class="n">06</span><span class="t">Bienestar animal: un hogar para su cuerpo de hoy</span><span class="who">Grandin</span></div>
  <div class="toc-row"><span class="n">07</span><span class="t">Comportamiento clínico: cuándo el veterinario es lo primero</span><span class="who">Gruen</span></div>
  <div class="toc-row"><span class="n">08</span><span class="t">Dolor y comportamiento: el enemigo silencioso<span class="incluido">EN LA MUESTRA</span></span><span class="who">Gruen</span></div>
  <div class="toc-row"><span class="n">09</span><span class="t">Envejecimiento y deterioro cognitivo</span><span class="who">Gruen · Panksepp</span></div>
  <div class="toc-row"><span class="n">10</span><span class="t">Refuerzo positivo: enriquecer sin exigir de más</span><span class="who">Skinner</span></div>

  <div class="toc-part">Parte II · Cuidados prácticos del día a día</div>
  <div class="toc-row"><span class="n">A</span><span class="t">Nutrición y apetito: cuando comer se vuelve difícil</span></div>
  <div class="toc-row"><span class="n">B</span><span class="t">Guía rápida de enfermedades comunes en la vejez</span></div>
  <div class="toc-row"><span class="n">C</span><span class="t">Cuando ya no te oye: sordera y señales de mano</span></div>
  <div class="toc-row"><span class="n">D</span><span class="t">Adaptar la rutina y la casa</span></div>
  <div class="toc-row"><span class="n">E</span><span class="t">Señales de alerta: cuándo ir al veterinario ya</span></div>
  <div class="toc-row"><span class="n">F</span><span class="t">Escala de calidad de vida</span></div>

  <div class="note mt7">
    <p><b>Por qué estos dos capítulos y no otros:</b> el 8 es el que más veces cambia la vida de un animal mayor —porque gran parte de lo que llamamos vejez es, en realidad, dolor no tratado— y el 5 te enseña a verlo, que es lo difícil, porque los animales esconden el dolor. Son los dos que más sirven aunque no leas nada más.</p>
  </div>
</section>''',
    "del_completo": [
        "El otoño de la vida de tu mascota",
        "rompecabezas",
        "<h2 class=\"ch-title\">El enemigo silencioso</h2>",
        "Ejercicio · Capítulo 08",
        "Ficha rápida · Capítulo 08",
        "<h2 class=\"ch-title\">Leer el malestar silencioso</h2>",
        "Ejercicio · Capítulo 05",
        "Ficha rápida · Capítulo 05",
    ],
    "pos_anticipo": 10,
    "anticipo": '''<section class="page">
  <div class="kicker">Un anticipo de los cuidados prácticos</div>
  <h1 class="ch-title">Lo que puedes cambiar esta misma tarde</h1>
  <div class="ch-who">Los seis ajustes de la casa, del capítulo 6</div>

  <p class="lead">Un cuerpo con menos fuerza, menos equilibrio y articulaciones más sensibles necesita una casa que reduzca el esfuerzo físico y el riesgo de caídas. Casi todo esto cuesta poco dinero y se hace en una tarde.</p>

  <ul class="check">
    <li><b>Alfombras o alfombrillas antideslizantes</b> en las zonas de suelo liso: cocina, pasillos, baño. Y comprueba que la alfombra tampoco patine.</li>
    <li><b>Rampa o escalones pequeños</b> para subir a la cama o al sofá, si antes saltaba.</li>
    <li><b>Cama ortopédica o acolchada gruesa</b>, firme, lejos de corrientes de aire. Si se hunde, le costará levantarse.</li>
    <li><b>Comederos y bebederos elevados</b> si hay molestia cervical o de espalda.</li>
    <li><b>Temperatura estable</b> en casa: los cuerpos senior regulan peor el frío y el calor.</li>
    <li><b>Buena iluminación nocturna</b> si la vista ha disminuido.</li>
  </ul>

  <div class="note">
    <p><b>Y dos cosas que casi siempre se olvidan:</b> las <b>uñas cortas</b> y <b>el pelo de entre las almohadillas recortado</b>. Con las uñas largas apoya mal y resbala mucho más — y en un animal al que ya le cuesta sostenerse, eso solo puede ser la diferencia entre moverse y dejar de moverse.</p>
  </div>

  <div class="box warn">
    <span class="lbl">Y aquí se corta la muestra</span>
    <p>Empieza por donde pasa <b>él</b>: sus rutas de cama, comedero y puerta. Es lo más barato y lo que antes se nota.</p>
  </div>
</section>''',
    "cierre": cierre(
        "Edad Dorada",
        "Diez capítulos, seis secciones prácticas y una ficha rápida por capítulo",
        [
            "<b>Los ocho capítulos restantes</b>, cada uno con su ejercicio y su ficha: etología, neurociencia afectiva, cognición, aprendizaje, entorno, comportamiento clínico, deterioro cognitivo y refuerzo positivo.",
            "<b>Nutrición y apetito:</b> qué hacer cuando comer se vuelve difícil, y por qué en gatos no se puede esperar a ver si se le pasa.",
            "<b>Guía de las ocho enfermedades más comunes</b> de la vejez, con sus señales, para saber cuándo consultar.",
            "<b>Cuando ya no te oye:</b> la prueba de la sordera que puedes hacer en casa, lo que hay que descartar antes de darlo por perdido, y <b>ocho señales de mano</b> para seguir entendiéndoos.",
            "<b>Señales de alerta urgentes</b> y la <b>escala de calidad de vida</b> para usar en casa, mes a mes.",
        ]),
}


if __name__ == "__main__":
    for libro, cfg in (("hogar", HOGAR), ("edad", EDAD)):
        construir(libro, cfg)
