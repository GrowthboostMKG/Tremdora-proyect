# -*- coding: utf-8 -*-
"""Sigue Contigo — Libro 2 de 4 · Diario del Oleaje (generador HTML)."""

CSS = open(__file__.rsplit('/',1)[0] + '/tremdora.css', encoding='utf-8').read()

FOOT = ('<div class="pfoot"><span>Diario del Oleaje · Sigue Contigo · Libro 2 de 4</span>'
        '<span class="n">{}</span></div>')

def page(inner, n=None, cls=''):
    f = FOOT.format(n) if n else ''
    return '<div class="page %s">%s%s</div>' % (cls, inner, f)

# ------------------------------------------------------------------ portada
EMBLEM = '''
<svg viewBox="0 0 150 150">
  <circle cx="75" cy="75" r="62" fill="none" stroke="#748156" stroke-width="1.1"/>
  <path d="M28 88 Q42 62 56 88 T84 88 T112 88" fill="none" stroke="#c1613a"
        stroke-width="2" stroke-linecap="round"/>
  <path d="M28 100 Q42 80 56 100 T84 100 T112 100" fill="none" stroke="#e2cfb4"
        stroke-width="1.6" stroke-linecap="round"/>
  <path d="M75 58 c-6-11-22-9-22 3 0 9 12 16 22 25 10-9 22-16 22-25 0-12-16-14-22-3z"
        fill="#f6e9d6" stroke="#a8502e" stroke-width="1.4" stroke-linejoin="round"/>
</svg>'''

cover = '''
<div class="badge">Libro 2 de 4 · el registro</div>
<div class="kicker">Compañero de escritura diaria</div>
<div class="emblem">%s</div>
<h1>Diario del <i>Oleaje</i></h1>
<div class="sub">Ocho semanas para escribir lo que duele,<br>y descubrir que no todos los días son iguales</div>
<div class="foot">Segundo libro de la serie <b>Sigue Contigo</b><br>
Compañero del eBook y del Plan Práctico de 8 Semanas</div>
''' % EMBLEM

# --------------------------------------------------------------- p2 · sobre
p2 = '''
<p class="eyebrow">Sobre este diario</p>
<h1 class="title">Diario del Oleaje</h1>
<p class="lead">El duelo no baja en línea recta. Baja en olas — y las olas solo
se ven cuando alguien las anota.</p>

<p>Este diario nace de un ejercicio concreto del eBook <em>Sigue Contigo</em>: el
diario del oleaje del Capítulo III. Aquí lo tienes ya preparado, semana a semana,
para que no tengas que construir nada cuando menos fuerzas tienes.</p>

<p>Cada noche vas a escribir dos números y una frase corta. Nada más. Ni un ensayo,
ni una explicación, ni una justificación. Dos números y una frase.</p>

<p>Al cabo de ocho semanas vas a releerlo. Y vas a ver, en tu propia letra, algo que
ahora mismo no puedes creer: que hubo días mejores. Que hubo momentos en que
respiraste. Que el dolor, aunque siga ahí, ha cambiado de forma.</p>

<div class="box left-green">
  <p class="lbl">Por qué funciona</p>
  <p>Poner palabras a una emoción reduce su intensidad en el sistema límbico. El
  neurocientífico Matthew Lieberman lo llamó <em>affect labeling</em>: nombrar el sentir
  literalmente baja la activación de la amígdala. Escribir no es desahogo. Es
  neurología aplicada.</p>
</div>

<div class="stats">
  <div class="stat"><div class="n">8</div><div class="t">semanas<br>de registro</div></div>
  <div class="stat"><div class="n green">2</div><div class="t">números<br>al día</div></div>
  <div class="stat"><div class="n">3</div><div class="t">minutos<br>por noche</div></div>
</div>

<p class="note">Úsalo junto al eBook (capítulos I, III, V y X en especial) y al Plan
Práctico de 8 Semanas, tercer libro de la serie.</p>
'''

# ---------------------------------------------------------------- p3 · cómo
p3 = '''
<p class="eyebrow">Antes de empezar</p>
<h1 class="title">Cómo usar este diario</h1>

<div class="box left-terra">
  <p class="lbl">Tres minutos, por la noche</p>
  <p>Escribe antes de dormir, cuando el día ya no puede pedirte nada más. Si una noche
  no puedes, no pasa nada: deja la casilla en blanco. Un hueco también es información.</p>
</div>

<div class="box left-terra">
  <p class="lbl">No corrijas, no releas, no expliques</p>
  <p>Este cuaderno no es para nadie más. No tiene que estar bien escrito ni tener
  sentido. Si un día solo puedes poner un número y una palabra fea, ponla.</p>
</div>

<div class="box left-terra">
  <p class="lbl">Anota también lo que te sostuvo</p>
  <p>La tercera casilla — <em>lo que me ha sostenido hoy</em> — es la más importante de
  las tres. Puede ser una ducha caliente, una llamada, el sol en la ventana, una serie
  tonta. Escríbelo. Dentro de ocho semanas esa columna será tu mapa de recursos.</p>
</div>

<hr class="rule soft">

<h2 class="sec">Las dos escalas que usarás cada día</h2>
<p><span class="pill"><b>La ola 1-5</b> — 1: hoy casi no me alcanzó · 5: hoy me
tumbó entera, entero</span></p>
<p><span class="pill"><b>El cuerpo 1-5</b> — 1: dormí, comí, funcioné ·
5: no dormí, no comí, me dolía todo</span></p>

<p class="note">No busques que los números bajen. No es un examen y no se aprueba.
Solo se registra. Si después de seis semanas los tuyos siguen todos en 4 y 5, o si
en algún momento aparece la idea de no querer seguir aquí, por favor pide ayuda
profesional. Eso no es fracasar en el duelo: es cuidarte como cuidarías de él o de ella.</p>
'''

# ------------------------------------------------------- p4 · curva del oleaje
WAVE = '''
<svg viewBox="0 0 372 196">
  <defs>
    <linearGradient id="wg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#c1613a" stop-opacity=".28"/>
      <stop offset="100%" stop-color="#c1613a" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="30" y1="160" x2="358" y2="160" stroke="#e2cfb4" stroke-width="1"/>
  <line x1="30" y1="20"  x2="30"  y2="160" stroke="#e2cfb4" stroke-width="1"/>
  <path d="M30 160 L30 46 C48 22 60 30 72 44 C84 60 92 40 104 34
           C120 26 128 62 142 70 C156 78 162 46 176 54
           C192 63 196 96 212 96 C228 96 234 66 248 76
           C262 86 266 116 282 114 C298 112 302 90 318 100
           C332 109 338 126 358 124 L358 160 Z"
        fill="url(#wg)"/>
  <path d="M30 46 C48 22 60 30 72 44 C84 60 92 40 104 34
           C120 26 128 62 142 70 C156 78 162 46 176 54
           C192 63 196 96 212 96 C228 96 234 66 248 76
           C262 86 266 116 282 114 C298 112 302 90 318 100
           C332 109 338 126 358 124"
        fill="none" stroke="#a8502e" stroke-width="1.9" stroke-linecap="round"/>
  <path d="M30 52 L358 132" fill="none" stroke="#748156" stroke-width="1.3"
        stroke-dasharray="4 4"/>
  <text x="34" y="16" font-family="Liberation Sans" font-size="7.5" fill="#9c7c63"
        letter-spacing=".8">INTENSIDAD DEL DOLOR</text>
  <text x="300" y="174" font-family="Liberation Sans" font-size="7.5" fill="#9c7c63"
        letter-spacing=".8">TIEMPO</text>
  <text x="238" y="152" font-family="Liberation Sans" font-size="7.2" fill="#748156"
        letter-spacing=".6">TENDENCIA REAL DE FONDO</text>
</svg>'''

p4 = '''
<p class="eyebrow">Lo que vas a ver</p>
<h1 class="title">La forma real del duelo</h1>
<p class="lead">Esperas una cuesta abajo. Lo que hay es un oleaje que, muy despacio,
va perdiendo altura.</p>

<div class="fig">%s<div class="figcap">El duelo vivido (naranja) frente al duelo real (verde)</div></div>

<p>La línea naranja es tu duelo día a día. La línea verde discontinua es lo que
realmente está pasando por debajo: una tendencia lenta, casi invisible en el
momento, que solo se aprecia cuando miras semanas enteras a la vez.</p>

<p>Por eso este diario existe. Dentro de una ola no se puede ver el oleaje. Vas a
tener días de retroceso — el día 40 puede doler más que el día 12 — y sin un
registro pensarás que has empeorado. No has empeorado. Has tenido una ola.</p>

<div class="box green">
  <p class="lbl">Las cuatro fases, sin calendario</p>
  <p><strong>1 · Shock</strong> — no te lo crees, funcionas en automático.<br>
  <strong>2 · Dolor agudo</strong> — la fase más dura, con la culpa en primer plano.<br>
  <strong>3 · Reorganización</strong> — aparecen días buenos y con ellos la culpa de tenerlos.<br>
  <strong>4 · Integración</strong> — su recuerdo deja de ser herida y empieza a abrigar.</p>
</div>

<p class="note">Nadie las atraviesa en orden. Se salta, se vuelve atrás, se repite.
Las fases no te dicen dónde deberías estar: te dicen que donde estás tiene nombre.</p>
''' % WAVE

# ------------------------------------------------------------- p5 · punto partida
p5 = '''
<p class="eyebrow">Punto de partida</p>
<h1 class="title">Antes de la primera noche</h1>
<p class="lead">Rellena esta página una sola vez. Volverás a ella en la semana ocho.</p>

<table class="ficha">
  <tr><td class="k">Su nombre</td><td class="write"></td></tr>
  <tr><td class="k">Cuánto tiempo estuvimos juntos</td><td class="write"></td></tr>
  <tr><td class="k">El día que se fue</td><td class="write"></td></tr>
  <tr><td class="k">Empiezo este diario el</td><td class="write"></td></tr>
  <tr><td class="k">Lo que más echo de menos</td><td class="write"></td></tr>
  <tr><td class="k">Lo que nadie sabe que echo de menos</td><td class="write"></td></tr>
  <tr><td class="k">Quién me está acompañando</td><td class="write"></td></tr>
  <tr><td class="k">Quién más se quedó en casa<br>
      <span style="font-size:7.4pt;color:#9c7c63">(otras mascotas, si las hay)</span></td>
      <td class="write"></td></tr>
</table>

<p class="ask">Hoy, antes de empezar: del 1 al 5, ¿cómo de alta está la ola?</p>
<div class="write"></div>

<div class="dashed">
  <p class="lbl">Una frase para él, para ella, antes de empezar</p>
  <div class="write dot"></div>
  <div class="write dot"></div>
</div>

<p class="note">No hace falta que la rellenes entera hoy. Puedes dejar líneas en
blanco y volver cuando puedas sostenerlas.</p>
'''

# ------------------------------------------------------------------- semanas
WEEKS = [
 ("Sobrevivir los primeros días",
  "Ninguna exigencia. Comer algo, beber agua, dormir lo que salga. No tomes "
  "decisiones importantes y no muevas sus cosas todavía.",
  "¿Qué es lo único que has conseguido hacer hoy por ti?",
  "¿Qué cosa suya has decidido no mover todavía? Escríbelo, para no dudarlo mañana."),
 ("Ponerle nombre a la ola",
  "Cada noche, una palabra exacta para lo que sientes. No «mal»: rabia, vacío, "
  "miedo, alivio, injusticia. La palabra precisa es la que baja la intensidad.",
  "¿Qué palabra se ha repetido más esta semana?",
  "¿Hubo algún momento en que la ola bajó sola, sin que la forzaras?"),
 ("La culpa, de frente",
  "Sacar la culpa del bucle mental y ponerla por escrito una sola vez. "
  "Lo que se escribe deja de dar vueltas.",
  "Escribe la frase exacta de tu culpa, tal cual suena por dentro.",
  "Si alguien a quien quieres te dijera esa misma frase sobre sí mismo, "
  "¿qué le responderías?"),
 ("Quién sostiene y quién no",
  "Dibujar tu círculo seguro (ejercicio 4 del eBook) y usarlo de verdad: "
  "una conversación real con alguien de ese círculo.",
  "¿Quién te ha sostenido esta semana sin que tuvieras que explicarte?",
  "¿Con quién has decidido no hablar de esto? Escribirlo también es protegerte."),
 ("Su lugar en casa",
  "Crear su rincón o colocar su urna, despacio y con intención. "
  "Un sitio concreto al que ir cuando la ausencia no cabe en ningún sitio.",
  "¿Qué objetos has elegido para su rincón, y por qué esos?",
  "¿Cómo te sentiste al colocarlo? Sé honesta, honesto: también vale «no pude»."),
 ("Lo que me enseñó",
  "Recoger la herencia. Cada noche, una cosa concreta que aprendiste a su lado. "
  "Puede ser diminuta.",
  "Escribe las tres que más te han sorprendido de la semana.",
  "¿Cuál de ellas puedes devolverle a tu propia vida los próximos siete días?"),
 ("Quien se queda",
  "Mirar a la otra mascota de la casa — o a ti, si el superviviente eres tú. "
  "Rutinas estables, presencia tranquila, quince minutos exclusivos al día.",
  "¿Qué has notado esta semana en tu otra mascota, o en el silencio de la casa?",
  "¿Qué rutina habéis conseguido sostener pase lo que pase?"),
 ("Mirar hacia atrás",
  "Releer el diario entero, desde la primera noche. Sin saltarte nada. "
  "Con papel y bolígrafo al lado.",
  "Relee la semana 1 y compárala con hoy. ¿Qué ha cambiado, aunque sea poco?",
  "¿Qué necesitas tú — tú, no él, no ella — para el mes que viene?"),
]

DAYS = ['L','M','X','J','V','S','D']

def week_page(i, title, goal, q1, q2):
    rows = ''.join(
        '<tr><td class="day">%s</td><td class="blank"></td><td></td><td></td></tr>' % d
        for d in DAYS)
    return '''
<div class="wk-head">
  <div class="wk-num">%02d</div>
  <div class="txt"><p class="eyebrow">Semana %d</p><h1 class="title">%s</h1></div>
</div>

<div class="box green">
  <p class="lbl">Lo que esta semana te pide</p>
  <p>%s</p>
</div>

<table>
  <thead><tr><th style="width:22pt">Día</th><th style="width:58pt">Ola 1-5</th>
  <th style="width:70pt">Cuerpo 1-5</th><th>Lo que me ha sostenido hoy</th></tr></thead>
  <tbody>%s</tbody>
</table>

<p class="ask">%s</p>
<div class="write"></div>
<div class="write"></div>

<p class="ask">%s</p>
<div class="write"></div>

<div class="dashed">
  <p class="lbl">Tres gestos de cuidado de esta semana</p>
  <div class="write dot"></div>
  <div class="write dot"></div>
  <div class="write dot"></div>
</div>
''' % (i, i, title, goal, rows, q1, q2)

# ------------------------------------------------------------------ p14 · SOS
p14 = '''
<p class="eyebrow terra">Para los días imposibles</p>
<h1 class="title">Cuando la ola te sobrepasa</h1>
<p class="lead">Tres herramientas de emergencia. No quitan el dolor: evitan que
te ahogues dentro de él.</p>

<div class="box left-terra">
  <p class="lbl">1 · Anclaje 4-6 · dos minutos</p>
  <p>Una mano en el pecho, otra en el vientre. Inspira contando 4, espira contando 6.
  Diez veces. Mientras respiras, repite por dentro: <em>«esto duele, y voy a
  sobrevivirlo»</em>. Al terminar, nombra en voz alta cinco cosas que veas.</p>
  <p class="note" style="margin-top:6pt">La espiración larga activa el nervio vago y
  baja el cortisol en minutos. Nombrar objetos saca al cerebro del bucle.</p>
</div>

<div class="box left-terra">
  <p class="lbl">2 · Poner hora a la pena · quince minutos</p>
  <p>Si el llanto te asalta a media mañana y no puedes sostenerlo, dile a la pena:
  <em>«a las ocho, contigo, quince minutos»</em>. Y cúmplelo. Siéntate, mira sus fotos,
  llora todo lo que necesites. Cuando suene el temporizador, levántate y bebe agua.</p>
  <p class="note" style="margin-top:6pt">No es reprimir: es citar. El duelo aplazado
  con cita se sostiene mejor que el duelo aplazado sin ella.</p>
</div>

<div class="box left-terra">
  <p class="lbl">3 · Háblale en voz alta</p>
  <p>Cuéntale el día. En el coche, en la ducha, delante de su rincón. En voz alta,
  con su nombre. No estás loca, no estás loco: estás manteniendo abierto un canal
  que tu cerebro todavía necesita.</p>
</div>

<hr class="rule">
<p class="ask">Escribe aquí el nombre y el teléfono de la persona a la que puedes
llamar a cualquier hora:</p>
<div class="write"></div>
<p class="note">Si en algún momento aparece la idea de no querer seguir aquí, esa
llamada no es opcional. Hazla. Y busca ayuda profesional cuanto antes.</p>
'''

# ------------------------------------------------------- p15 · quien se queda
p15 = '''
<p class="eyebrow">Registro paralelo</p>
<h1 class="title">Quien se queda también hace duelo</h1>
<p class="lead">Si en casa quedó otro animal, esta media página es suya.
Anota una vez por semana.</p>

<table>
  <thead class="terra"><tr><th style="width:44pt">Semana</th><th style="width:52pt">Come</th>
  <th style="width:52pt">Duerme</th><th style="width:52pt">Juega</th>
  <th>Lo que he observado</th></tr></thead>
  <tbody>
  %s
  </tbody>
</table>

<div class="box green">
  <p class="lbl">Qué ayuda de verdad</p>
  <p>Rutinas idénticas en horario y lugar · tu presencia sin forzar contacto ·
  dejarle oler la manta o el collar del que se fue · paseos algo más largos ·
  hablarle en voz baja con su nombre · no introducir cambios grandes ahora.</p>
</div>

<p class="note">Si a las tres o cuatro semanas sigue sin comer, no juega o se aísla
por completo, consulta al veterinario. En el cuarto libro de la serie —
<em>Ellos También se Despiden</em> — tienes el protocolo completo, día a día.</p>
''' % ''.join(
    '<tr><td class="day green">%d</td><td class="blank"></td><td></td><td></td><td></td></tr>' % w
    for w in range(1, 9))

# ---------------------------------------------------------------- p16 · cierre
p16 = '''
<p class="eyebrow">Para cerrar</p>
<h1 class="title">Ocho semanas después</h1>

<p>Vuelve a la página «Antes de la primera noche» y léela entera. Después lee la
semana 1, noche por noche. Luego la semana 8.</p>

<p>Es muy probable que no notes un cambio enorme. El duelo no funciona así. Pero
si miras la columna de <em>lo que me ha sostenido hoy</em> a lo largo de las ocho
semanas, vas a encontrar algo que no esperabas: una lista de cosas que te
sostuvieron cuando creías que nada lo hacía.</p>

<p>Esa lista es tuya. Guárdala. Es lo que vas a necesitar la próxima vez que
llegue una ola grande — un aniversario, una foto que aparece sola, un perro
igual que él en la calle.</p>

<div class="quote green">No has superado nada.<br>Has aprendido a sostenerte<br>mientras dolía.</div>

<hr class="rule soft">

<h2 class="sec">Si quieres seguir escribiendo</h2>
<p>Puedes fotocopiar las páginas semanales o repetir esta misma estructura en un
cuaderno propio. Muchas personas siguen escribiendo una línea al día durante meses,
y muchas vuelven a este diario en las fechas señaladas: su cumpleaños, el
aniversario, la primera Navidad sin él o sin ella.</p>

<p>No hay un plazo correcto. Solo el tuyo.</p>

<div class="dashed">
  <p class="lbl">Lo que quiero recordar dentro de un año</p>
  <div class="write dot"></div>
  <div class="write dot"></div>
  <div class="write dot"></div>
</div>

<p class="note" style="text-align:center;margin-top:16pt">
Sigue Contigo — Libro 2 de 4 · Diario del Oleaje<br>tremdora</p>
'''

# ------------------------------------------------------------------- ensamble
pages = [page(cover, cls='cover'), page(p2, 2), page(p3, 3), page(p4, 4), page(p5, 5)]
for idx, (t, g, q1, q2) in enumerate(WEEKS, start=1):
    pages.append(page(week_page(idx, t, g, q1, q2), 5 + idx))
pages += [page(p14, 14), page(p15, 15), page(p16, 16)]

html = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<title>Sigue Contigo — Diario del Oleaje</title><style>%s</style></head>'
        '<body>%s</body></html>') % (CSS, ''.join(pages))

out = __file__.rsplit('/', 1)[0] + '/libro2-diario-del-oleaje.html'
open(out, 'w', encoding='utf-8').write(html)
print('escrito', out, len(pages), 'páginas')
