#!/usr/bin/env python3
"""Genera los cuatro complementos: dos diarios y dos planes de 8 semanas.

Comparten la hoja de estilos y el sistema visual de los libros principales.
"""
import pathlib

HERE = pathlib.Path(__file__).parent

EMBLEMA = '''<div class="emblem"><svg viewBox="0 0 150 150">
      <circle cx="75" cy="75" r="62" fill="none" stroke="#748156" stroke-width="1.1"/>
      <path d="M75 108 C52 90 44 76 44 64 c0-11 9-19 19-19 6 0 10 3 12 7
               2-4 6-7 12-7 10 0 19 8 19 19 0 12-8 26-31 44z"
            fill="#f6e9d6" stroke="#a8502e" stroke-width="1.6" stroke-linejoin="round"/>
      <ellipse cx="75" cy="76" rx="7.5" ry="6" fill="#e2cfb4"/>
      <ellipse cx="67" cy="65" rx="2.8" ry="4" fill="#e2cfb4" transform="rotate(-18 67 65)"/>
      <ellipse cx="75" cy="61" rx="2.8" ry="4.2" fill="#e2cfb4"/>
      <ellipse cx="83" cy="65" rx="2.8" ry="4" fill="#e2cfb4" transform="rotate(18 83 65)"/>
    </svg></div>'''


def pag(contenido, cls=""):
    return f'<section class="page {cls}">\n{contenido}\n</section>'


def cubierta(num, titulo, sub, pie, edi):
    return pag(f'''  <div class="pill">Libro {num} de 3 · {pie}</div>
  <div class="brandmark">TREMDORA</div>
  {EMBLEMA}
  <h1>{titulo}</h1>
  <div class="sub">{sub}</div>
  <div class="cv-foot">
    <div class="lbl">Serie completa</div>
    <div class="names">1 · El método &nbsp;·&nbsp; 2 · El diario &nbsp;·&nbsp; 3 · El plan</div>
    <div class="edi">{edi}</div>
  </div>''', "cover serie")


AUTORA_FOTO = '''  <div class="ph-float">
    <img src="victoria-paris.jpg" alt="Victoria y Paris">
    <span class="cap">Victoria y Paris</span>
  </div>
'''


def autora(cuerpo):
    return pag('''  <div class="kicker">Sobre la autora</div>
  <h1>Diecisiete años<br>con Paris</h1>

''' + AUTORA_FOTO + cuerpo + '''
  <div class="cierre">
    Victoria
    <span>Fundadora de Tremdora · por Paris</span>
  </div>''', "author")


def cierre(titulo, lineas):
    items = "\n".join(f"    <li>{x}</li>" for x in lineas)
    return pag(f'''  <div class="kicker">Para terminar</div>
  <h1 class="ch-title">{titulo}</h1>
  <div class="ch-who">Lo que te llevas de estas ocho semanas</div>

  <ul class="diamond">
{items}
  </ul>

  <div class="cta">
    <span class="big">Tremdora</span>
    Entender · Cuidar · Acompañar · Celebrar
    <span class="web">tremdora.com</span>
    <span class="ig">@tremdora_pets</span>
  </div>''')


def lineas(n, tight=False):
    cls = "lines tight" if tight else "lines"
    return f'<div class="{cls}">' + '<div class="ln"></div>' * n + '</div>'


def semana_diario(n, titulo, foco, cols):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    th = "".join(f"<th>{c}</th>" for c in cols)
    filas = ""
    for d in dias:
        celdas = "".join('<td class="box"></td>' if c.startswith("·") else "<td></td>"
                         for c in cols)
        filas += f'<tr><td class="day">{d}</td>{celdas}</tr>\n'
    return pag(f'''  <div class="wk-head">
    <div class="n">{n:02d}</div>
    <div class="t">{titulo}<span>{foco}</span></div>
  </div>

  <table class="fill">
    <thead><tr><th>Día</th>{th}</tr></thead>
    <tbody>
{filas}    </tbody>
  </table>

  <h3 class="sub"><span class="pre">Al acabar la semana</span>Lo que he visto</h3>
  {lineas(4)}

  <div class="tarea">
    <span class="lbl">Mi victoria de esta semana</span>
    {lineas(2, True)}
  </div>''')


def semana_plan(n, titulo, objetivo, tareas, aviso=None):
    dias = ["L", "M", "X", "J", "V", "S", "D"]
    rej = "".join(f'<div class="d"><span class="lbl">{d}</span><span class="mark"></span></div>'
                  for d in dias)
    ts = "\n".join(f"    <li>{t}</li>" for t in tareas)
    extra = ""
    if aviso:
        extra = f'''
  <div class="box warn">
    <span class="lbl">Ojo con esto</span>
    <p>{aviso}</p>
  </div>'''
    return pag(f'''  <div class="wk-head">
    <div class="n">{n:02d}</div>
    <div class="t">{titulo}<span>{objetivo}</span></div>
  </div>

  <h3 class="sub" style="margin-top:0"><span class="pre">Esta semana</span>Lo que vas a hacer</h3>
  <ul class="check">
{ts}
  </ul>

  <h3 class="sub"><span class="pre">Marca cada día</span>Siete casillas, nada más</h3>
  <div class="rejilla">{rej}</div>
{extra}
  <h3 class="sub">Notas de la semana</h3>
  {lineas(3)}''')


def escribir(nombre, titulo_doc, acento, acento_claro, paginas):
    cab = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{titulo_doc} — Tremdora</title>
<style>/*CSS*/</style>
<style>:root{{--accent:{acento};--accent-soft:{acento_claro};}}</style>
</head>
<body>
'''
    doc = cab + "\n\n".join(paginas) + "\n\n</body>\n</html>\n"
    (HERE / f"{nombre}.html").write_text(doc, encoding="utf-8")
    print(f"{nombre}.html · {len(paginas)} páginas")


# ══════════════════════════════════════════════════════════ HOGAR · DIARIO

AUT_CALMA = '''  <p class="a-lead">Me llamo Victoria, tengo 44 años, y Tremdora existe por una perra que se llamaba Paris.</p>

  <p>Estuve <b>diecisiete años compitiendo con ella</b>, y aun así hubo cosas suyas que no entendí hasta mucho después. Paris era tranquila, muy tranquila, y durante años pensé que eso era su carácter y ya está.</p>

  <p>Este cuaderno existe por una razón muy concreta: <b>yo no anoté nada.</b> Me fiaba de la memoria, y la memoria con los animales es un desastre — se queda con el día malo y borra los quince buenos que vinieron antes. Cuando por fin quise contarle a alguien lo que pasaba, no supe decir ni cuántas veces, ni cuánto duraba, ni qué lo disparaba.</p>

  <p>Anotar dos cosas al día no es burocracia. Es lo que convierte una intuición en un dato, y un dato es lo único que se puede enseñar a un veterinario, comparar con la semana pasada y usar para decidir.</p>'''

CALMA = [
    cubierta(2, "Diario de la <em>Calma</em>",
             "Ocho semanas para ver lo que hoy se te escapa: qué lo dispara, qué funciona y cuánto ha cambiado de verdad.",
             "El diario", "Compañero del método"),

    pag('''  <div class="kicker">Antes de empezar</div>
  <h1 class="ch-title">Cómo usar este diario</h1>
  <div class="ch-who">Dos minutos al día, ni uno más</div>

  <p class="lead">Este cuaderno es el compañero de <i>Hogar en Calma</i>. No hace falta que hayas terminado el libro para empezarlo: puedes abrirlo esta misma noche, con el libro a medias, y te va a servir igual.</p>

  <p><b>Cada día anotas tres cosas.</b> Qué señales has visto, qué pasaba justo antes, y si has hecho el ejercicio del día. Nada más. Ni explicaciones, ni justificaciones, ni un diario de sentimientos — eso no es lo que necesitas aquí.</p>

  <p><b>Y una vez por semana, una frase.</b> Qué has visto al mirar los siete días juntos. Ahí es donde aparece lo que no se ve en el día a día.</p>

  <div class="box">
    <span class="lbl">Lo que vas a conseguir</span>
    <p><b>1 · Tu mapa de disparadores.</b> Casi siempre son dos o tres, siempre los mismos, y se ven a la segunda semana.</p>
    <p><b>2 · Una línea base real.</b> No «creo que está peor»: cuántas veces, cuánto duró, con qué intensidad.</p>
    <p><b>3 · Un informe para el veterinario</b> que vale diez veces más que contarlo de memoria.</p>
  </div>

  <div class="box warn">
    <span class="lbl">Si un día no puedes</span>
    <p>Déjalo en blanco y sigue mañana. Un diario con huecos sirve; un diario abandonado por culpa de un hueco, no. <b>Esto no es un examen.</b></p>
  </div>''') ,

    pag('''  <div class="kicker">Por qué funciona</div>
  <h1 class="ch-title">Anotar no es llevar la cuenta</h1>
  <div class="ch-who">Lo que pasa cuando pones por escrito lo que estás viendo</div>

  <p class="lead">Hay dos motivos, y los dos están estudiados.</p>

  <p><b>El primero es tuyo.</b> Poner palabras a una emoción baja su intensidad. Matthew Lieberman lo demostró en 2007 con resonancia magnética: nombrar lo que uno siente reduce la actividad de la amígdala y activa la corteza prefrontal. Lo llamó <i>affect labeling</i>. Escribir «hoy me ha dado rabia» no es desahogarse: es bajarle el volumen a la rabia.</p>

  <p><b>El segundo es de tu mascota.</b> Los cambios de conducta son graduales, y lo gradual es justo lo que el ojo no detecta. Nadie nota que su perro tarda cuatro segundos más en levantarse. Pero si lo anotas ocho semanas seguidas, lo ves. <b>Los cambios lentos solo se detectan comparando, nunca observando.</b></p>

  <div class="quote">
    <p>«La memoria se queda con el día malo y borra los quince buenos que vinieron antes. El papel, no.»</p>
    <div class="src">Por qué este cuaderno existe</div>
  </div>

  <div class="note">
    <p>Y hay un tercer motivo, menos científico y muy real: <b>en las semanas difíciles, el diario es lo único que te va a demostrar que estás avanzando.</b> Porque la sensación de que nada mejora casi siempre es falsa — y el papel lo desmiente.</p>
  </div>'''),

    pag('''  <div class="kicker">Semana 0</div>
  <h1 class="ch-title">Mi mapa de disparadores</h1>
  <div class="ch-who">El ejercicio del capítulo 5, en una página</div>

  <p>Durante los próximos siete días, cada vez que veas una señal de estrés anota <b>qué pasaba justo antes</b>. Al final de la semana vuelve aquí y escribe los que se repitan.</p>

  <h3 class="sub"><span class="pre">Los que ya sospecho</span>Antes de empezar a mirar</h3>
  ''' + lineas(3) + '''

  <h3 class="sub"><span class="pre">Los que han aparecido</span>Después de siete días mirando</h3>
  ''' + lineas(5) + '''

  <div class="box">
    <span class="lbl">El que voy a trabajar primero</span>
    <p>Elige <b>uno solo</b>. El que más se repita, o el que más le cueste. Con ese se monta la escalera de cinco niveles del Programa A.</p>
    ''' + lineas(2, True) + '''
  </div>'''),

    pag('''  <div class="kicker">Página de consulta</div>
  <h1 class="ch-title">Las ocho señales tempranas</h1>
  <div class="ch-who">Tenla abierta al lado mientras rellenas la semana</div>

  <div class="signals">
    <div class="s"><span class="h">Lamerse el hocico</span><span class="d">sin comida ni agua cerca.</span></div>
    <div class="s"><span class="h">Bostezar fuera de contexto</span><span class="d">no por sueño: para autorregular la tensión.</span></div>
    <div class="s"><span class="h">«Ojo de ballena»</span><span class="d">se ve el blanco del ojo al mirar de reojo.</span></div>
    <div class="s"><span class="h">Orejas hacia atrás o de lado</span><span class="d">postura defensiva o escucha en alerta.</span></div>
    <div class="s"><span class="h">Cuerpo bajo o rígido</span><span class="d">se hace pequeño, o se queda inmóvil y tenso.</span></div>
    <div class="s"><span class="h">Jadeo sin calor ni ejercicio</span><span class="d">respiración rápida y superficial en reposo.</span></div>
    <div class="s"><span class="h">Sacudida corporal «en seco»</span><span class="d">como al salir del agua, sin estar mojado.</span></div>
    <div class="s"><span class="h">Cola baja o entre las patas</span><span class="d">en gatos, pegada al cuerpo o moviéndose rápido de lado a lado.</span></div>
  </div>

  <div class="box warn">
    <span class="lbl">Y lo que no se anota: se atiende</span>
    <p>Si ves <b>autolesión</b> —lamido hasta hacerse herida, uñas rotas contra la puerta—, <b>pánico de verdad</b>, o en gatos <b>esfuerzos para orinar o sangre en la orina</b>: eso no es material de diario. Es consulta veterinaria, y la urinaria es de horas.</p>
  </div>'''),
]

COLS_CALMA = ["Señales que he visto", "Qué pasaba antes", "· Ejercicio", "Nivel 1-5"]
FOCOS_CALMA = [
    ("Observar sin tocar nada", "Solo mirar y anotar. Todavía no se cambia nada."),
    ("El mapa se dibuja", "Empiezan a repetirse dos o tres disparadores."),
    ("El primer nivel", "Arranca la escalera de exposición por el nivel más bajo."),
    ("Subir solo si aburre", "Se sube de nivel cuando el actual ya no genera nada."),
    ("Las señales de salida", "Llaves y zapatos, veinte veces al día, sin salir."),
    ("Las primeras ausencias", "La mitad del tiempo que aguanta, nunca más."),
    ("Consolidar lo que sale bien", "Repetir, no avanzar. Esta semana no se sube."),
    ("Mirar las ocho semanas juntas", "Comparar la semana 1 con esta. Aquí está el premio."),
]
for i, (t, f) in enumerate(FOCOS_CALMA, start=1):
    CALMA.append(semana_diario(i, t, f, COLS_CALMA))

CALMA += [
    pag('''  <div class="kicker">Registro del Programa B</div>
  <h1 class="ch-title">La escalera de ausencias</h1>
  <div class="ch-who">Cada escalón, su fecha y qué pasó</div>

  <p>Apunta aquí cada sesión de ausencia. <b>Sube solo cuando una duración te haya salido bien tres veces</b>, y si aparece angustia vuelve al último escalón que funcionó.</p>

  <table class="fill">
    <thead><tr><th>Fecha</th><th>Minutos</th><th>· Salió bien</th><th>Qué vi en el vídeo</th></tr></thead>
    <tbody>''' + "".join(
        '<tr><td></td><td></td><td class="box"></td><td></td></tr>' for _ in range(13)
    ) + '''</tbody>
  </table>

  <div class="box warn">
    <span class="lbl">La regla de oro</span>
    <p>Si hay angustia, <b>no fue un mal día</b>: el paso fue demasiado grande. No es un fallo, es información — y es la única forma de no retroceder semanas.</p>
  </div>'''),

    pag('''  <div class="kicker">Si tienes gato</div>
  <h1 class="ch-title">El registro felino</h1>
  <div class="ch-who">Programa C · lo que de verdad mueve la aguja</div>

  <h3 class="sub" style="margin-top:0"><span class="pre">Lo primero</span>Qué cambió en casa estos dos meses</h3>
  ''' + lineas(2) + '''

  <h3 class="sub" style="margin-top:5mm"><span class="pre">Los recursos</span>Marca lo que ya tienes</h3>
  <ul class="check">
    <li>Comida y agua <b>separadas entre sí</b></li>
    <li>Sitios altos despejados donde pueda mirar desde arriba</li>
    <li>Escondites a ras de suelo, al menos uno por zona</li>
    <li>Rascadores verticales de un metro, donde ya araña</li>
    <li>Areneros: <b>uno por gato más uno</b>, abiertos, grandes, limpios a diario, con arena fina y sin perfume</li>
  </ul>

  <h3 class="sub" style="margin-top:5mm"><span class="pre">Las cuatro señales</span>Cómo van, semana a semana</h3>
  <table class="fill">
    <thead><tr><th>Sem.</th><th>· Calvas</th><th>· Esconde</th><th>· Arenero</th><th>· Come mal</th></tr></thead>
    <tbody>''' + "".join(
        f'<tr><td class="day">{i}</td><td class="box"></td><td class="box"></td><td class="box"></td><td class="box"></td></tr>'
        for i in range(1, 9)
    ) + '''</tbody>
  </table>'''),

    pag('''  <div class="kicker">Para la consulta</div>
  <h1 class="ch-title">El informe que acelera el diagnóstico</h1>
  <div class="ch-who">Rellénalo la víspera y llévalo impreso</div>

  <p>Un veterinario conductual necesita datos, no impresiones. Esto es exactamente lo que te va a preguntar.</p>

  <h3 class="sub" style="margin-top:5mm"><span class="pre">1</span>Frecuencia, duración e intensidad de las últimas dos semanas</h3>
  ''' + lineas(3, True) + '''

  <h3 class="sub"><span class="pre">2</span>Los disparadores identificados</h3>
  ''' + lineas(2, True) + '''

  <h3 class="sub"><span class="pre">3</span>Qué he probado ya, y qué resultado tuvo</h3>
  ''' + lineas(3, True) + '''

  <div class="box">
    <span class="lbl">Y lo que más vale de todo</span>
    <p><b>Un vídeo de 20 a 30 segundos</b> de un episodio típico, si es seguro grabarlo. El lenguaje corporal en vídeo dice más que tres páginas de descripción.</p>
  </div>'''),

    pag('''  <div class="kicker">Semana 8</div>
  <h1 class="ch-title">Qué ha cambiado en ocho semanas</h1>
  <div class="ch-who">Vuelve a la semana 1 y compárala con hoy</div>

  <p class="lead">Esta es la página por la que existe el cuaderno. Léete la semana 1 entera antes de rellenar nada.</p>

  <h3 class="sub"><span class="pre">Entonces</span>Lo que anotaba la primera semana</h3>
  ''' + lineas(3, True) + '''

  <h3 class="sub"><span class="pre">Ahora</span>Lo que anoto esta semana</h3>
  ''' + lineas(3, True) + '''

  <h3 class="sub"><span class="pre">Lo que funcionó</span>Y lo que no voy a volver a intentar</h3>
  ''' + lineas(3, True) + '''

  <div class="box">
    <span class="lbl">Y ahora</span>
    <p>Si hay mejora, <b>no lo dejes</b>: sigue con lo que funciona y sube un escalón. Si en ocho semanas de trabajo constante no has visto nada, eso también es un dato — y es el momento de sumar a un profesional, no de insistir más fuerte.</p>
  </div>'''),

    autora(AUT_CALMA),

    cierre("Lo que te queda escrito", [
        "<b>Tu mapa de disparadores</b>, que no sabías al empezar y ahora cabe en tres líneas.",
        "<b>Ocho semanas comparables</b>: la prueba en tu propia letra de lo que ha cambiado.",
        "<b>El informe para la consulta</b>, con los datos que de verdad aceleran un diagnóstico.",
        "<b>La escalera de ausencias</b>, con cada escalón fechado — y, si hubo retroceso, el punto exacto al que volver.",
        "Y las <b>ocho victorias semanales</b>, que en los días malos son lo único que demuestra que esto va hacia algún sitio.",
    ]),
]

escribir("c2-diario-calma", "Diario de la Calma", "#748156", "#E6EADA", CALMA)


# ══════════════════════════════════════════════════════════ HOGAR · PLAN

AUT_PLAN_C = '''  <p class="a-lead">Me llamo Victoria, tengo 44 años, y Tremdora existe por una perra que se llamaba Paris.</p>

  <p>Estuve <b>diecisiete años compitiendo con ella</b>. Sé muy bien lo que es un plan: entrenar algo todos los días, en el mismo orden, aunque no apetezca. Y sé también lo que pasa cuando no hay plan — que se hace lo que apetece, que es casi siempre lo mismo, y que lo difícil se va dejando para nunca.</p>

  <p>Por eso esto no es una lista de consejos. <b>Es una tarea al día, decidida de antemano</b>, para que las mañanas malas no tengas que elegir nada. Elegir, cuando estás agotada y preocupada, es justo lo que no se puede hacer.</p>'''

PLAN_C = [
    cubierta(3, "Plan de <em>8 Semanas</em>",
             "Una tarea pequeña cada día, decidida de antemano, para no tener que elegir nada cuando no te quedan fuerzas.",
             "El plan", "Hogar en Calma"),

    pag('''  <div class="kicker">Antes de empezar</div>
  <h1 class="ch-title">Cómo funciona el plan</h1>
  <div class="ch-who">Ocho semanas, una tarea al día, siete casillas por semana</div>

  <p class="lead">Este plan reparte los tres programas de <i>Hogar en Calma</i> en una secuencia diaria. No añade nada nuevo: ordena lo que ya está en el libro para que no tengas que decidir por dónde seguir.</p>

  <div class="box">
    <span class="lbl">Las tres reglas</span>
    <p><b>1 · Una tarea al día, y ya está.</b> Si un día haces tres, no adelantas: la repetición espaciada funciona mejor que los atracones.</p>
    <p><b>2 · El orden importa.</b> Las semanas 1 y 2 parecen que no hacen nada, y son las que sostienen todo lo demás.</p>
    <p><b>3 · Si te saltas un día, sigues donde lo dejaste.</b> No se recupera, no se duplica, no se empieza de cero.</p>
  </div>

  <h3 class="sub"><span class="pre">El mapa</span>Las ocho semanas de un vistazo</h3>
  <div class="tablewrap">
    <table>
      <thead><tr><th>Semanas</th><th>Qué se trabaja</th></tr></thead>
      <tbody>
        <tr><td class="wk">1-2</td><td>Observación y cimientos: diario de señales, rutina de BÚSQUEDA, «sitio», línea base grabada.</td></tr>
        <tr><td class="wk">3-4</td><td>El disparador principal y las señales de salida.</td></tr>
        <tr><td class="wk">5-6</td><td>Escalera avanzada, independencia con presencia y primeras ausencias.</td></tr>
        <tr><td class="wk">7</td><td>Consolidación: repetir lo que sale bien, sin subir nada.</td></tr>
        <tr><td class="wk">8</td><td>Evaluación y decisión.</td></tr>
      </tbody>
    </table>
  </div>

  <div class="box warn">
    <span class="lbl">Si tienes gato</span>
    <p>Los pasos son los mismos, pero <b>más pequeños y más cortos</b>: sesiones de uno a dos minutos en vez de cinco, y el doble de tiempo en cada nivel. Donde el plan diga «sube», tú repites una semana más.</p>
  </div>'''),

    pag('''  <div class="kicker">Semana 0</div>
  <h1 class="ch-title">La línea base</h1>
  <div class="ch-who">Dos tardes antes de empezar · sin esto, el plan es una suposición</div>

  <p class="lead">No se puede medir el progreso sin saber de dónde se parte. Son dos tareas y se hacen antes de la semana 1.</p>

  <div class="tarea">
    <span class="lbl">Tarea 1 · Graba media hora</span>
    <p>Móvil enfocando la puerta, sal con tu rutina normal, quédate fuera entre 15 y 20 minutos. Luego anota <b>el minuto exacto</b> en que aparece la primera señal de angustia: no el destrozo, sino el jadeo, el llanto, el ir y venir.</p>
    <p style="margin-top:3mm"><b>Minuto en que aparece:</b> ''' + lineas(1, True) + '''</p>
  </div>

  <div class="tarea">
    <span class="lbl">Tarea 2 · Monta la zona segura</span>
    <p>Un rincón tranquilo, <b>lejos de la puerta de la calle</b> y de ventanas con mucho ruido. Su cama, agua y una prenda con tu olor. Y la regla familiar: ahí no se le toca, no se le saca, y los niños no entran.</p>
  </div>

  <div class="box">
    <span class="lbl">Lo que acabas de conseguir</span>
    <p>Ese minuto es <b>tu punto de partida real</b>, y casi siempre es mucho más bajo de lo que uno imagina. Las ausencias de la semana 5 empiezan en <b>la mitad</b> de ese número.</p>
  </div>'''),
]

SEM_PLAN_C = [
    ("Mirar sin cambiar nada", "Entrenar tu ojo antes que a tu mascota",
     ["Anota en el diario cada señal temprana que veas y <b>qué pasaba justo antes</b>.",
      "Un paseo con <b>olfateo libre</b> de diez minutos: ella elige la ruta.",
      "Diez minutos de juego de búsqueda en casa (alfombra olfativa, comida escondida).",
      "No corrijas nada todavía. Esta semana solo se mira."], None),
    ("El «sitio» y la rutina", "La habilidad ancla de todo lo demás",
     ["Sigue anotando señales y disparadores.",
      "Diez minutos al día enseñando <b>«sitio»</b>: premia la postura tumbada en la colchoneta, no el llegar.",
      "Mantén el paseo con olfateo y el juego de búsqueda.",
      "Al acabar la semana, mira el diario y <b>elige un solo disparador</b> para trabajar."], None),
    ("El primer escalón", "La escalera de exposición empieza abajo del todo",
     ["Define los <b>cinco niveles</b> de tu disparador, del más suave al real.",
      "Tres o cuatro sesiones cortas: el nivel 1 emparejado con premio de alto valor.",
      "Sigue con «sitio» diez minutos y con la base diaria.",
      "Anota en el diario si ha habido alguna señal durante la sesión."],
     "Si reacciona, <b>has subido demasiado</b>: baja un nivel y quédate ahí. Hecho deprisa, esto empeora el miedo en vez de quitarlo."),
    ("Las llaves no significan nada", "Vaciar de sentido las señales de salida",
     ["Coge las llaves y <b>siéntate</b>. Ponte los zapatos y haz la cena. Veinte veces al día, sin salir.",
      "Sigue la escalera: sube de nivel solo si el actual ya le aburre.",
      "Mantén «sitio» y la base diaria.",
      "Apunta cuándo deja de levantarse al oír las llaves."], None),
    ("Las primeras ausencias", "La mitad del tiempo que aguanta, ni un minuto más",
     ["Una salida real y brevísima al día: <b>la mitad</b> del minuto de la línea base.",
      "Sal sin despedida, vuelve sin fiesta, espera unos segundos de calma antes de saludar.",
      "Repite la misma duración hasta que le aburra, y apúntalo en la escalera del diario.",
      "Deja el kong congelado justo antes de salir."],
     "Nunca dupliques de golpe. Se sube <b>entre un 25 % y un 30 %</b> del tiempo anterior, y solo después de tres sesiones buenas."),
    ("Distancia estando tú en casa", "Muchos no toleran la distancia, no la puerta",
     ["Usa «sitio» para que se quede en la colchoneta mientras tú estás en otra habitación.",
      "Cierra puertas interiores un minuto, como paso intermedio.",
      "Sigue subiendo las ausencias, despacio.",
      "Escalera del disparador: nivel 4 o 5 si va bien."], None),
    ("Consolidar", "Esta semana no se sube nada",
     ["<b>Repite</b> las duraciones y los niveles que ya salen bien. Nada nuevo.",
      "Revisa la zona segura: que siga limpia, disponible y sin invadir.",
      "Comprueba si hay fuentes nuevas de estrés en casa.",
      "Relee tus notas de la semana 1."],
     "La tentación de subir cuando todo va bien es la causa número uno de los retrocesos. <b>Consolidar también es avanzar.</b>"),
    ("Mirar atrás", "Comparar, decidir y seguir",
     ["Rellena la página «Qué ha cambiado en ocho semanas» del diario.",
      "Vuelve a grabar media hora y compárala con la grabación de la semana 0.",
      "Decide: seguir sola con lo que funciona, o sumar a un profesional.",
      "Y escribe tu última victoria."], None),
]
for i, (t, o, ts, av) in enumerate(SEM_PLAN_C, start=1):
    PLAN_C.append(semana_plan(i, t, o, ts, av))

PLAN_C += [
    pag('''  <div class="kicker">Cuando se tuerce</div>
  <h1 class="ch-title">Si aparece un retroceso</h1>
  <div class="ch-who">Pasa en casi todos los procesos, y no significa lo que parece</div>

  <p class="lead">Un día malo después de tres buenos no borra los tres buenos. Los retrocesos son <b>parte esperada</b> del proceso, no una señal de que esto no funciona.</p>

  <h3 class="sub" style="margin-top:6mm"><span class="pre">Qué hacer</span>Tres pasos, en este orden</h3>
  <ul class="check">
    <li><b>Vuelve al último nivel que salió bien</b> y quédate ahí tres o cuatro sesiones más.</li>
    <li><b>Busca qué cambió</b>: una obra, una visita, un horario distinto, un cambio de casa. Casi siempre hay algo.</li>
    <li><b>No subas nada</b> hasta que vuelva a aburrirle. La prisa es lo único que de verdad retrasa esto.</li>
  </ul>

  <div class="box warn">
    <span class="lbl">Y cuándo esto deja de ser cosa de un plan</span>
    <p>Si se autolesiona, se rompe uñas o dientes contra la puerta, hay pánico de verdad, o <b>ocho semanas de trabajo constante no han movido nada</b>: toca un profesional. Tu veterinario, o un veterinario especialista en comportamiento. <b>Pedir ayuda no es haber fracasado.</b></p>
  </div>

  <h3 class="sub">Qué pasó, y qué hice</h3>
  ''' + lineas(4)),

    autora(AUT_PLAN_C),

    cierre("Lo que has construido", [
        "<b>Una habilidad ancla</b> —«sitio»— que vas a usar el resto de su vida.",
        "<b>Un disparador trabajado a fondo</b>, de los dos o tres que tenía.",
        "<b>Las señales de salida vaciadas de significado:</b> las llaves ya no anuncian nada.",
        "<b>Una escalera de ausencias</b> con cada escalón fechado, y el punto exacto al que volver si hace falta.",
        "Y lo más importante: <b>saber que esto se mueve despacio y hacia delante</b>, que es justo lo que no se ve desde dentro.",
    ]),
]

escribir("c3-plan-calma", "Plan de 8 Semanas · Hogar en Calma", "#748156", "#E6EADA", PLAN_C)


# ══════════════════════════════════════════════════════════ EDAD · DIARIO

AUT_DIAS = '''  <p class="a-lead">Me llamo Victoria, tengo 44 años, y Tremdora existe por una perra que se llamaba Paris.</p>

  <p>Estuve <b>diecisiete años compitiendo con ella</b>. Y cuando se hizo mayor descubrí que de ella sabía muchísimo y <b>de la vejez no sabía casi nada</b>.</p>

  <p>Tardé en entender que no estaba cansada: que le dolía. Y lo tardé, entre otras cosas, porque la vejez no avanza de un día para otro — avanza tan despacio que el ojo no lo ve. Yo la miraba cada día y por eso no notaba nada.</p>

  <p>Este cuaderno existe para eso: <b>para comparar.</b> Los cambios lentos solo se detectan comparando el mes de hoy con el de hace tres, y eso es imposible de memoria. Con dos números al mes, se ve.</p>

  <p>Y tiene un segundo propósito, que descubrí tarde: <b>guardar los días buenos.</b> Cuando llega una época difícil, la memoria se queda solo con lo malo. Tener escrito, en tu propia letra, que hubo semanas enteras en que estaba bien, cambia cómo vives lo que viene.</p>'''

DIAS = [
    cubierta(2, "Diario de los <em>Días Buenos</em>",
             "Para ver lo que avanza despacio, llevar datos de verdad a la consulta y guardar los días buenos, que son los que luego se olvidan.",
             "El diario", "Compañero del método"),

    pag('''  <div class="kicker">Antes de empezar</div>
  <h1 class="ch-title">Cómo usar este diario</h1>
  <div class="ch-who">No es un diario de cada día: es un diario de comparar</div>

  <p class="lead">Este cuaderno es el compañero de <i>Edad Dorada</i>, y funciona distinto a lo que esperas. No hay que escribir cada noche. Hay que escribir <b>cada semana una cosa y cada mes otra</b>, y releerlo entero cada tres.</p>

  <div class="box">
    <span class="lbl">El ritmo</span>
    <p><b>Cada semana:</b> el escaneo corporal —cuánto tarda en levantarse, qué notas al palpar— y cómo ha ido el apetito.</p>
    <p><b>Cada mes:</b> el peso, la escala de calidad de vida y la lista DISHA.</p>
    <p><b>Cada tres meses:</b> te lo relees entero. Ahí es donde aparece lo que no se ve mirándolo cada día.</p>
  </div>

  <p>En una mascota mayor, <b>la tendencia dice mucho más que una medición suelta</b>. Un día regular no significa nada. Tres meses de días regulares, sí — y al revés: una mala semana dentro de un trimestre bueno es solo una mala semana.</p>

  <div class="box warn">
    <span class="lbl">Y lo que no espera a la próxima anotación</span>
    <p>Rechazo total de comida más de 24 horas, dificultad para respirar en reposo, colapso, vómitos o diarrea repetidos con sangre, abdomen duro, convulsiones, o un cambio <b>de golpe</b> en cómo se mueve: eso no es material de diario. Es <b>urgencia veterinaria</b>.</p>
  </div>'''),

    pag('''  <div class="kicker">Hoy</div>
  <h1 class="ch-title">La línea base</h1>
  <div class="ch-who">Rellénala una sola vez, antes de empezar</div>

  <p class="lead">Esto es con lo que vas a comparar dentro de tres meses, de seis y de un año. Es la página más importante del cuaderno y se rellena en diez minutos.</p>

  <h3 class="sub" style="margin-top:6mm"><span class="pre">Lo básico</span>Fecha, edad y peso de partida</h3>
  ''' + lineas(2, True) + '''

  <h3 class="sub"><span class="pre">Lo que más cuenta</span>Tres cosas que disfrutaba y ya no hace, o hace mucho menos</h3>
  <p style="font-size:9pt;color:var(--ink-3);margin-bottom:2mm">Subir al sofá, pasear largo, jugar, saludarte en la puerta, subir a la cama…</p>
  ''' + lineas(3, True) + '''

  <h3 class="sub"><span class="pre">Para la consulta</span>Última revisión y último análisis de sangre</h3>
  ''' + lineas(2, True) + '''

  <div class="box">
    <span class="lbl">Esas tres actividades son tu prueba del nueve</span>
    <p>Llévalas a la consulta y pide <b>una valoración del dolor</b>. Si tras tratarlo vuelven, aunque sea en parte, ya tienes la respuesta: <b>era dolor, no era solo la edad.</b> Es la pregunta más rentable de todo el libro.</p>
  </div>'''),

    pag('''  <div class="kicker">Cada semana</div>
  <h1 class="ch-title">El escaneo corporal</h1>
  <div class="ch-who">Dos minutos, el mismo día de la semana</div>

  <p>Obsérvala levantarse desde el reposo y pásale la mano con suavidad por columna, caderas y patas. Anota solo lo que cambie.</p>

  <table class="fill">
    <thead><tr><th>Sem.</th><th>Tarda en levantarse</th><th>· Tensión al palpar</th><th>· Evita superficies</th><th>Apetito 1-5</th></tr></thead>
    <tbody>''' + "".join(
        f'<tr><td class="day">{i}</td><td></td><td class="box"></td><td class="box"></td><td></td></tr>'
        for i in range(1, 13)
    ) + '''</tbody>
  </table>

  <div class="note">
    <p>Doce semanas caben en esta página. Cuando la termines, <b>fotocópiala</b> antes de seguir: lo que vale no es la última fila, es poder poner la primera al lado de la última.</p>
  </div>'''),

    pag('''  <div class="kicker">Cada mes</div>
  <h1 class="ch-title">Escala de calidad de vida</h1>
  <div class="ch-who">El mismo día de cada mes, pensando en la última semana completa</div>

  <p>Puntúa de <b>1 (muy comprometida)</b> a <b>5 (buena)</b>. Repite la escala tres veces en estas páginas y compara.</p>

  <h3 class="sub" style="margin-top:6mm"><span class="pre">Mes 1</span>Fecha</h3>
  <div class="scale-mini"><span class="nm">Apetito e hidratación</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Movilidad</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Dolor y comodidad</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Higiene</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Interacción y alegría</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Más días buenos que malos</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>

  <div class="box">
    <span class="lbl">Cómo leer el total</span>
    <p><b>25 a 30:</b> buena calidad de vida general. <b>15 a 24:</b> merece una conversación con tu veterinario sobre qué áreas reforzar. <b>Por debajo de 15</b>, y sobre todo si «dolor» o «más días buenos que malos» están en 1 o 2: es el momento de una conversación honesta sobre calidad de vida y siguientes pasos.</p>
  </div>'''),

    pag('''  <div class="kicker">Cada mes</div>
  <h1 class="ch-title">Meses 2 y 3</h1>
  <div class="ch-who">Las mismas seis áreas, para poder comparar</div>

  <h3 class="sub" style="margin-top:0"><span class="pre">Mes 2</span>Fecha</h3>
  <div class="scale-mini"><span class="nm">Apetito e hidratación</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Movilidad</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Dolor y comodidad</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Higiene</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Interacción y alegría</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Más días buenos que malos</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>

  <h3 class="sub" style="margin-top:7mm"><span class="pre">Mes 3</span>Fecha</h3>
  <div class="scale-mini"><span class="nm">Apetito e hidratación</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Movilidad</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Dolor y comodidad</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Higiene</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Interacción y alegría</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>
  <div class="scale-mini"><span class="nm">Más días buenos que malos</span><span class="nums"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span></span></div>'''),

    pag('''  <div class="kicker">Cada mes</div>
  <h1 class="ch-title">La lista DISHA</h1>
  <div class="ch-who">Deterioro cognitivo · marca solo los cambios nuevos del último mes</div>

  <table class="fill">
    <thead><tr><th>Mes</th><th>· Desorien&shy;tación</th><th>· Inter&shy;acción</th><th>· Sueño-vigilia</th><th>· Higiene</th><th>· Actividad</th></tr></thead>
    <tbody>''' + "".join(
        f'<tr><td class="day">{i}</td><td class="box"></td><td class="box"></td><td class="box"></td><td class="box"></td><td class="box"></td></tr>'
        for i in range(1, 10)
    ) + '''</tbody>
  </table>

  <div class="box warn">
    <span class="lbl">Dos o más casillas nuevas en el mismo mes</span>
    <p>Pide una <b>valoración cognitiva</b>. Y antes de darlo por deterioro cognitivo, que descarten lo que da cuadros parecidos y <b>sí se trata</b>: dolor, pérdida de vista o de oído, y enfermedad renal o tiroidea.</p>
  </div>

  <h3 class="sub">Qué he observado</h3>
  ''' + lineas(3, True)),

    pag('''  <div class="kicker">Si hay tratamiento</div>
  <h1 class="ch-title">Dolor y medicación</h1>
  <div class="ch-who">Qué toma, desde cuándo, y qué ha cambiado desde entonces</div>

  <table class="fill">
    <thead><tr><th>Desde</th><th>Qué toma y cada cuánto</th><th>Para qué</th></tr></thead>
    <tbody>''' + "".join('<tr><td></td><td></td><td></td></tr>' for _ in range(6)) + '''</tbody>
  </table>

  <h3 class="sub"><span class="pre">La prueba del nueve</span>De las tres actividades de la línea base, ¿ha vuelto alguna?</h3>
  ''' + lineas(3, True) + '''

  <div class="box warn">
    <span class="lbl">Nunca, bajo ningún concepto</span>
    <p><b>Analgésicos humanos, ni los de otra mascota.</b> Muchos son tóxicos para perros y gatos, y el paracetamol y el ibuprofeno matan gatos. Si te parece que le duele, es una llamada al veterinario — nunca el botiquín de casa.</p>
  </div>'''),

    pag('''  <div class="kicker">Cada seis meses</div>
  <h1 class="ch-title">Para la revisión</h1>
  <div class="ch-who">Rellénalo la víspera y llévalo impreso</div>

  <p class="lead">Desde la etapa senior las revisiones pasan de anuales a <b>semestrales</b>, porque el envejecimiento avanza más rápido que en la edad adulta. Esto es lo que conviene llevar escrito.</p>

  <h3 class="sub" style="margin-top:5mm"><span class="pre">1</span>Cambios en apetito, sed, orina, energía y sueño</h3>
  ''' + lineas(2, True) + '''

  <h3 class="sub"><span class="pre">2</span>Peso de hoy, y el de hace seis meses</h3>
  ''' + lineas(1, True) + '''

  <h3 class="sub"><span class="pre">3</span>Lo que quiero preguntar</h3>
  ''' + lineas(3, True) + '''

  <div class="box">
    <span class="lbl">Tres cosas que pedir siempre</span>
    <p><b>1 ·</b> Análisis de sangre y de orina, si no se han hecho en el último año.<br>
    <b>2 ·</b> <b>Valoración dental</b> — el dolor dental es una causa muy frecuente de pérdida de apetito que se pasa por alto.<br>
    <b>3 ·</b> Y si le cuesta moverse: <b>que le valoren el dolor</b>, con tus tres actividades en la mano.</p>
  </div>'''),

    pag('''  <div class="kicker">Lo que de verdad importa</div>
  <h1 class="ch-title">Mis días buenos</h1>
  <div class="ch-who">Esta página no es para el veterinario. Es para ti</div>

  <p class="lead">Todo lo demás de este cuaderno son datos. Esta página es lo otro: los días en que estuvo bien, las cosas que disfrutasteis, los momentos que dentro de un tiempo no vas a recordar si no los escribes.</p>

  <p>Escríbelos cortos. Una línea. La fecha y qué pasó.</p>

  ''' + lineas(11) + '''

  <div class="note">
    <p>Cuando llegue una época difícil, la memoria se va a quedar solo con lo malo — es así, no se puede evitar. <b>Esta página es la prueba de lo demás.</b></p>
  </div>'''),

    autora(AUT_DIAS),

    cierre("Lo que te queda escrito", [
        "<b>Una línea base real</b>, con las tres actividades que son tu prueba del nueve ante el veterinario.",
        "<b>Tres meses de escala de calidad de vida</b>, uno al lado de otro, que es donde se ve la tendencia.",
        "<b>La lista DISHA mes a mes</b>, con el que más vale: detectar el deterioro cuando todavía se puede intervenir.",
        "<b>El informe de la revisión semestral</b>, que acelera el diagnóstico más que cualquier descripción de memoria.",
        "Y <b>la página de los días buenos</b>, que es la única que vas a releer dentro de unos años.",
    ]),
]

escribir("c2-diario-dias", "Diario de los Días Buenos", "#A8502E", "#F6E9D6", DIAS)


# ══════════════════════════════════════════════════════════ EDAD · PLAN

AUT_PLAN_D = '''  <p class="a-lead">Me llamo Victoria, tengo 44 años, y Tremdora existe por una perra que se llamaba Paris.</p>

  <p>Estuve <b>diecisiete años compitiendo con ella</b>. Y cuando se hizo mayor me pasó lo que les pasa a casi todos: <b>sabía lo que había que hacer y no sabía por dónde empezar.</b> Había que mirar el peso, y la casa, y el dolor, y la comida, y pedir hora, y mirar los dientes. Tanto, que muchos días no hacía ninguna.</p>

  <p>Este plan es la respuesta a eso. No añade nada que no esté en el libro: <b>lo reparte.</b> Una cosa al día, en un orden que tiene sentido — primero lo que detecta, después lo que alivia, al final lo que sostiene.</p>

  <p>Si solo pudieras hacer dos semanas de las ocho, haz la 1 y la 4. Ahí está casi todo lo que cambia la vida de un animal mayor.</p>'''

PLAN_D = [
    cubierta(3, "Plan de <em>8 Semanas</em>",
             "Una cosa al día, en el orden que tiene sentido, para no tener que elegir entre las diez que habría que hacer.",
             "El plan", "Edad Dorada"),

    pag('''  <div class="kicker">Antes de empezar</div>
  <h1 class="ch-title">Cómo funciona el plan</h1>
  <div class="ch-who">Ocho semanas, una cosa al día, siete casillas por semana</div>

  <p class="lead">Este plan reparte en una secuencia diaria todo lo que <i>Edad Dorada</i> te pide hacer. No es contenido nuevo: es el mismo, puesto en orden.</p>

  <div class="box">
    <span class="lbl">El orden no es casual</span>
    <p><b>Primero lo que detecta</b> (la revisión y la línea base). <b>Después lo que alivia</b> (el peso, la casa, el dolor), que es lo que más rápido se nota. <b>Al final lo que sostiene</b>: la rutina y el enriquecimiento.</p>
  </div>

  <h3 class="sub"><span class="pre">El mapa</span>Las ocho semanas de un vistazo</h3>
  <div class="tablewrap">
    <table>
      <thead><tr><th>Semana</th><th>Foco</th></tr></thead>
      <tbody>
        <tr><td class="wk">1</td><td>Revisión completa y línea base: peso, análisis, escala de calidad de vida.</td></tr>
        <tr><td class="wk">2</td><td>Nutrición y apetito.</td></tr>
        <tr><td class="wk">3</td><td>La casa: suelos, accesos, descanso, uñas y almohadillas.</td></tr>
        <tr><td class="wk">4</td><td>Dolor y movilidad.</td></tr>
        <tr><td class="wk">5</td><td>Enriquecimiento cognitivo y vínculo diario.</td></tr>
        <tr><td class="wk">6</td><td>Consolidar lo nuevo: medicación, dieta, ejercicio.</td></tr>
        <tr><td class="wk">7</td><td>Seguimiento y ajuste fino con la lista DISHA.</td></tr>
        <tr><td class="wk">8</td><td>Nueva escala de calidad de vida y resultados.</td></tr>
      </tbody>
    </table>
  </div>

  <div class="box warn">
    <span class="lbl">Si solo puedes con dos semanas</span>
    <p>Haz <b>la 1 y la 4</b>: la revisión con análisis y la valoración del dolor. Ahí está casi todo lo que cambia la vida de un animal mayor.</p>
  </div>'''),
]

SEM_PLAN_D = [
    ("La revisión y la línea base", "Sin datos, lo demás son palos de ciego",
     ["<b>Pide cita</b> para una revisión completa: examen físico, análisis de sangre y de orina, y <b>valoración dental</b>.",
      "Pésala y apunta el peso en el diario.",
      "Escribe <b>tres actividades</b> que disfrutaba y ya no hace. Llévalas a la consulta.",
      "Rellena la <b>primera escala de calidad de vida</b>.",
      "Y pide la cita de la siguiente revisión antes de salir: <b>semestral</b>, no anual."], None),
    ("Nutrición y apetito", "Lo más fácil de arreglar, y lo que más preocupa",
     ["Calienta un poco la comida húmeda: potencia el olor y compensa el olfato que ha perdido.",
      "Pasa a <b>raciones más pequeñas y más frecuentes</b>.",
      "Pon agua en varios puntos de la casa, accesibles sin esfuerzo.",
      "Mide en gramos lo que le ofreces y anota lo que deja a los 30 minutos."],
     "En gatos, un rechazo total de comida de más de <b>24 a 48 horas</b> no espera: el riesgo de lipidosis hepática es real. No es un «a ver si se le pasa»."),
    ("La casa", "Una tarde de trabajo y casi nada de dinero",
     ["<b>Agáchate a su altura</b> y recorre la casa: mira qué suelos resbalan y qué escalones le cuestan.",
      "Pon <b>alfombrillas antideslizantes</b> en sus rutas: cama, comedero, puerta. Y comprueba que la alfombra tampoco patine.",
      "Rampa o escalón para sofá y cama, si antes saltaba.",
      "<b>Uñas cortas y el pelo de entre las almohadillas recortado.</b> Con las uñas largas apoya mal y resbala mucho más.",
      "En gatos: arenero de <b>entrada baja</b>, y repartidos por la casa."], None),
    ("Dolor y movilidad", "La semana que más cambia las cosas",
     ["Lleva tus tres actividades al veterinario y pide <b>una prueba de manejo del dolor</b>: un ensayo terapéutico corto con analgésicos apropiados, bajo supervisión.",
      "<b>El peso:</b> si no le palpas las costillas con la mano plana, le sobra. Y cada kilo de más es carga sobre articulaciones que ya duelen.",
      "Pasa de un paseo largo a <b>tres cortos</b>, al ritmo que marque ella.",
      "Anota en el diario si alguna de las tres actividades vuelve."],
     "<b>Nunca le des analgésicos humanos</b> ni los de otra mascota: muchos son tóxicos para perros y gatos."),
    ("La mente y el vínculo", "Enriquecer sin exigir de más",
     ["Tres minutos al día de un juego de bajo impacto: premio escondido bajo un vaso, alfombra olfativa, un truco sencillo que ya conozca.",
      "Termina siempre con <b>un éxito fácil</b>.",
      "Cinco minutos de contacto tranquilo, a la misma hora y en el mismo sitio.",
      "Si le cuesta responder a la voz, prueba con <b>gestos claros</b>: la lectura visual se conserva mucho mejor."], None),
    ("Consolidar", "Que lo nuevo deje de ser nuevo",
     ["Repasa que la medicación, la dieta y los paseos nuevos ya funcionen solos, sin tener que acordarte.",
      "Revisa que los cambios de la semana 3 siguen puestos y en su sitio.",
      "Segundo pesaje del mes. Apúntalo.",
      "Nada nuevo esta semana: solo que lo de antes aguante."], None),
    ("La lista DISHA", "Lo que se detecta a tiempo se puede frenar",
     ["Repasa las <b>cinco categorías</b>: desorientación, interacción, sueño-vigilia, higiene y actividad.",
      "Marca solo <b>los cambios nuevos</b> del último mes.",
      "Si hay dos o más, pide una valoración cognitiva — y que descarten antes dolor, vista, oído, riñón y tiroides.",
      "Mantén rutinas fijas y no reorganices los muebles: la previsibilidad reduce directamente la confusión."], None),
    ("Mirar atrás", "Comparar la semana 1 con hoy",
     ["Rellena la <b>segunda escala de calidad de vida</b> y ponla al lado de la de la semana 1.",
      "Pesa y compara.",
      "Relee las tres actividades de la línea base: ¿ha vuelto alguna?",
      "Y escribe en «Mis días buenos» lo mejor de estas ocho semanas."], None),
]
for i, (t, o, ts, av) in enumerate(SEM_PLAN_D, start=1):
    PLAN_D.append(semana_plan(i, t, o, ts, av))

PLAN_D += [
    pag('''  <div class="kicker">Cuando toca parar</div>
  <h1 class="ch-title">Lo que este plan no puede resolver</h1>
  <div class="ch-who">Y conviene tenerlo escrito antes de necesitarlo</div>

  <p class="lead">Las ocho semanas sirven para que estos años sean cómodos. No sirven para detener el tiempo, y hay un momento en que la pregunta deja de ser qué más hacer.</p>

  <h3 class="sub" style="margin-top:6mm"><span class="pre">Urgencia</span>Esto no espera a la próxima cita</h3>
  <ul class="check">
    <li>Rechazo total de comida y agua más de <b>24 horas</b>.</li>
    <li><b>Dificultad para respirar</b>, o respiración con la boca abierta en reposo.</li>
    <li><b>Colapso</b>, o no poder levantarse de golpe.</li>
    <li>Vómitos o diarrea repetidos, <b>sobre todo con sangre</b>; abdomen duro o distendido.</li>
    <li>Convulsiones, desorientación extrema o pérdida de consciencia.</li>
    <li>En <b>gatos macho</b>: esfuerzos para orinar sin resultado. Eso es cuestión de horas.</li>
  </ul>

  <div class="box">
    <span class="lbl">Y lo otro</span>
    <p>Si la escala de calidad de vida baja de forma sostenida, y sobre todo si «dolor y comodidad» o «más días buenos que malos» se quedan en 1 o 2, <b>es el momento de una conversación honesta con tu veterinario</b>. No de hacer más cosas. Priorizar su bienestar por encima del deseo de tenerla más tiempo es, en sí mismo, un acto de amor.</p>
  </div>'''),

    autora(AUT_PLAN_D),

    cierre("Lo que has puesto en marcha", [
        "<b>Una revisión semestral con análisis</b>, que es lo que detecta las enfermedades comunes de la vejez antes de que den síntomas.",
        "<b>El dolor, valorado</b> — que es el hallazgo que más veces devuelve vitalidad a un animal mayor.",
        "<b>Una casa adaptada</b>: suelos, accesos, descanso, uñas y almohadillas.",
        "<b>Rutinas que ya funcionan solas</b>, sin tener que acordarte cada mañana.",
        "Y <b>dos escalas de calidad de vida</b> que puedes poner una al lado de la otra — que es la única forma de saber si esto va bien.",
    ]),
]

escribir("c3-plan-dorada", "Plan de 8 Semanas · Edad Dorada", "#A8502E", "#F6E9D6", PLAN_D)
