# -*- coding: utf-8 -*-
"""Sigue Contigo — Libro 4 de 4 · Ellos También se Despiden (generador HTML)."""
import math

D = __file__.rsplit('/', 1)[0]
CSS = open(D + '/tremdora.css', encoding='utf-8').read()

EXTRA_CSS = '''
.chain{ margin:10pt 0 12pt; }
.chain .lk{
  display:inline-block; background:var(--paper); border:.7pt solid var(--line);
  border-radius:20pt; padding:3.5pt 9pt; font-size:7.6pt; letter-spacing:.4pt;
  color:var(--ink-soft); margin:0 2pt 5pt 0;
}
.chain .ar{ color:var(--green); font-size:8pt; margin:0 1pt 5pt 0; display:inline-block; }
.sem{ border-left:3pt solid #748156; background:var(--green-soft);
      border-radius:0 5pt 5pt 0; padding:10pt 13pt; margin-bottom:9pt; }
.sem.amber{ border-left-color:#c08a2e; background:#f7ecd6; }
.sem.red{ border-left-color:#a8502e; background:#f4e0d6; }
.sem .lbl{ font-size:7.8pt; letter-spacing:1.5pt; text-transform:uppercase;
           font-weight:bold; color:#748156; margin:0 0 5pt; }
.sem.amber .lbl{ color:#9a6c1e; }
.sem.red .lbl{ color:#a8502e; }
.sem p{ font-size:8.6pt; line-height:1.55; margin:0; }
.ref{ font-size:8pt; line-height:1.5; color:var(--ink-soft); margin:0 0 5pt;
      padding-left:11pt; text-indent:-11pt; }
.ref b{ color:var(--ink); }
'''
CSS += EXTRA_CSS

FOOT = ('<div class="pfoot"><span>Ellos También se Despiden · Sigue Contigo · Libro 4 de 4</span>'
        '<span class="n">{}</span></div>')

def page(inner, n=None, cls=''):
    return '<div class="page %s">%s%s</div>' % (cls, inner, FOOT.format(n) if n else '')

# ---------------------------------------------------------------- portada
EMBLEM = '''
<svg viewBox="0 0 150 150">
  <circle cx="75" cy="75" r="62" fill="none" stroke="#748156" stroke-width="1.1"/>
  <g stroke="#e2cfb4" stroke-width="1.5" fill="none" opacity=".95">
    <ellipse cx="52" cy="88" rx="12" ry="9.5"/>
    <ellipse cx="41" cy="72" rx="4.3" ry="6" transform="rotate(-18 41 72)"/>
    <ellipse cx="52" cy="67" rx="4.3" ry="6.4"/>
    <ellipse cx="63" cy="71" rx="4.3" ry="6" transform="rotate(16 63 71)"/>
  </g>
  <g stroke="#a8502e" stroke-width="1.6" fill="#f6e9d6">
    <ellipse cx="97" cy="88" rx="12" ry="9.5"/>
    <ellipse cx="86" cy="72" rx="4.3" ry="6" transform="rotate(-18 86 72)"/>
    <ellipse cx="97" cy="67" rx="4.3" ry="6.4"/>
    <ellipse cx="108" cy="71" rx="4.3" ry="6" transform="rotate(16 108 71)"/>
  </g>
</svg>'''

cover = '''
<div class="badge">Libro 4 de 4 · la ciencia aplicada</div>
<div class="kicker">Guía de acompañamiento animal</div>
<div class="emblem">%s</div>
<h1>Ellos También<br><i>se Despiden</i></h1>
<div class="sub">Cómo acompañar a la mascota que se queda,<br>
según la etología y la neurociencia afectiva</div>
<div class="foot">Cuarto libro de la serie <b>Sigue Contigo</b><br>
Con un protocolo de 21 días y su registro</div>
''' % EMBLEM

# ------------------------------------------------------------ p2 · sobre
CHAIN = ['Etología', 'Neurociencia afectiva', 'Cognición animal',
         'Teoría del aprendizaje', 'Lenguaje corporal', 'Bienestar animal',
         'Comportamiento clínico', 'Dolor y comportamiento',
         'Envejecimiento cognitivo', 'Refuerzo positivo']
chain_html = '<div class="chain">' + '<span class="ar">&rsaquo;</span>'.join(
    '<span class="lk">%s</span>' % c for c in CHAIN) + '</div>'

p2 = '''
<p class="eyebrow">Sobre este libro</p>
<h1 class="title">Ellos También se Despiden</h1>
<p class="lead">Lo que estás viendo en el animal que se quedó no es imaginación
tuya. Tiene nombre, tiene circuito cerebral y tiene manejo.</p>

<p>Cuando muere una mascota, casi todo el acompañamiento se dirige — con razón — a
la persona. Pero si en casa quedó otro animal, hay un segundo duelo ocurriendo a la
vez, silencioso, y muchas veces más intenso que el nuestro en los primeros días.</p>

<p>Este libro reúne lo que sabemos de ese proceso. No desde la intuición ni desde
frases bonitas, sino desde el trabajo de ocho investigadores que dedicaron su vida
a entender cómo sienten, aprenden y sufren los animales. Y lo traduce en algo que
puedas hacer mañana por la mañana.</p>

%s

<div class="box left-green">
  <p class="lbl">La ruta de este libro</p>
  <p>Primero <strong>entender</strong> — qué se ha roto y por qué duele. Después
  <strong>observar</strong> — qué es normal, qué vigilar y cuándo llamar al
  veterinario. Y por último <strong>actuar</strong> — un protocolo de veintiún días
  con su registro, para reconstruir la rutina sin forzar nada.</p>
</div>

<p class="note">Nada de lo que leas aquí sustituye a una consulta veterinaria. Al
contrario: parte de este libro existe precisamente para ayudarte a saber cuándo
pedirla y qué contar cuando llegues.</p>
''' % chain_html

# --------------------------------------------------- p3 y p4 · referentes
SCI = [
 ("Konrad Lorenz", "Etología · Nobel de Medicina 1973",
  "Fundador de la etología moderna. Describió el vínculo social animal como un "
  "sistema biológico, no como un adorno afectivo. Al observar gansos que perdían "
  "a su pareja anotó exactamente lo mismo que la psicología describía en niños "
  "separados de su madre: la mirada se apaga, el cuello se hunde, el animal pierde "
  "rango social y busca llamando. Lo escribió hace más de cincuenta años."),
 ("Jaak Panksepp", "Neurociencia afectiva",
  "Demostró que los mamíferos compartimos siete sistemas emocionales básicos, "
  "situados en zonas antiguas del cerebro. Uno de ellos, el sistema de PÁNICO / "
  "DUELO, es el que se dispara ante la separación de una figura de apego. No es "
  "una metáfora: es un circuito concreto, regulado por los mismos opioides "
  "internos y la misma oxitocina que en nosotros."),
 ("Alexandra Horowitz", "Cognición animal · el mundo del olfato",
  "Popularizó la idea de <em>umwelt</em>: cada especie habita un mundo perceptivo "
  "propio. El del perro está hecho de olor. Entre doscientos y trescientos millones "
  "de receptores olfativos, frente a nuestros cinco o seis. Eso cambia por completo "
  "qué significa para él la manta del compañero que ya no está — y qué haces tú "
  "con ella."),
 ("Brian Hare", "Cognición social canina",
  "Su trabajo mostró que los perros leen los gestos comunicativos humanos mejor "
  "que ningún otro animal, incluidos los grandes simios, y que la domesticación "
  "seleccionó amabilidad y cooperación. Consecuencia directa para ti: tu estado "
  "emocional no es el telón de fondo del duelo de tu perro. Es parte de él."),
]
SCI2 = [
 ("Iván Pávlov", "Teoría del aprendizaje · condicionamiento clásico",
  "Describió cómo un estímulo neutro se carga de significado por asociación. Tu "
  "casa está llena de esos estímulos: el ruido de dos cuencos, la hora del paseo, "
  "la llave en la puerta. Cada uno sigue anunciando a alguien que ya no llega. "
  "También describió la <em>recuperación espontánea</em>: por qué, semanas después, "
  "vuelve a esperar en la puerta sin motivo aparente."),
 ("B. F. Skinner", "Teoría del aprendizaje · refuerzo positivo",
  "Mostró que la conducta se sostiene por sus consecuencias. Cuando desaparece "
  "aquello que reforzaba una conducta — buscar al compañero, esperarlo —, esa "
  "conducta entra en extinción, y la extinción empieza casi siempre con un "
  "aumento: el <em>estallido de extinción</em>. Sobre esa misma ley se construye "
  "la salida: reforzar la calma en lugar de atender solo el llanto."),
 ("Margaret Gruen", "Comportamiento clínico · dolor y conducta",
  "Especialista en medicina del comportamiento y dolor animal. Su línea de trabajo "
  "insiste en algo que salva vidas: un cambio de conducta es, muy a menudo, el "
  "primer signo de dolor o de enfermedad. Antes de llamar duelo a lo que ves, hay "
  "que descartar que sea otra cosa."),
 ("Temple Grandin", "Bienestar animal · el entorno sensorial",
  "Cambió la forma de diseñar entornos para animales al describir que piensan en "
  "detalles sensoriales concretos, no en conceptos: un objeto movido, una sombra "
  "nueva, un olor distinto pueden importar más que cualquier explicación. Su "
  "propuesta de bienestar es directa — reducir el miedo y el pánico, y mantener "
  "activo el sistema de búsqueda."),
]

def sci_page(items, kicker, title, lead, tail=''):
    cards = ''.join(
        '<div class="sci"><p class="nm">%s</p><p class="fl">%s</p><p>%s</p></div>'
        % (n, f, t) for n, f, t in items)
    return ('<p class="eyebrow">%s</p><h1 class="title">%s</h1>'
            '<p class="lead">%s</p>%s%s') % (kicker, title, lead, cards, tail)

p3 = sci_page(SCI, 'Quién sostiene este libro', 'Los ocho referentes · I',
  'Ocho investigadores, ocho disciplinas. Nada de lo que sigue es opinión nuestra.')
p4 = sci_page(SCI2, 'Quién sostiene este libro', 'Los ocho referentes · II',
  'De cómo aprende un animal a cómo se le nota que le duele algo.',
  '<p class="note">A lo largo del libro verás sus nombres junto a cada '
  'recomendación, para que sepas de dónde viene lo que te estamos pidiendo que hagas.</p>')

# ------------------------------------------------- p5 · Panksepp (donut)
SYS = [('BÚSQUEDA', '#c9d1ae'), ('RABIA', '#e2cfb4'), ('MIEDO', '#dcc9ad'),
       ('DESEO', '#e6dcc4'), ('CUIDADO', '#c9d1ae'), ('PÁNICO / DUELO', '#a8502e'),
       ('JUEGO', '#e2cfb4')]

def donut(cx, cy, r, rin, segs):
    out, a0 = [], -90.0
    step = 360.0 / len(segs)
    for name, col in segs:
        a1 = a0 + step
        x0, y0 = cx + r * math.cos(math.radians(a0)),  cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)),  cy + r * math.sin(math.radians(a1))
        xi1, yi1 = cx + rin * math.cos(math.radians(a1)), cy + rin * math.sin(math.radians(a1))
        xi0, yi0 = cx + rin * math.cos(math.radians(a0)), cy + rin * math.sin(math.radians(a0))
        out.append('<path d="M%.1f %.1f A%.0f %.0f 0 0 1 %.1f %.1f L%.1f %.1f '
                   'A%.0f %.0f 0 0 0 %.1f %.1f Z" fill="%s" stroke="#fbf3e6" '
                   'stroke-width="1.4"/>' % (x0, y0, r, r, x1, y1, xi1, yi1,
                                             rin, rin, xi0, yi0, col))
        a0 = a1
    return ''.join(out)

legend = ''.join(
    '<rect x="196" y="%d" width="9" height="9" rx="2" fill="%s"/>'
    '<text x="211" y="%d" font-family="Liberation Sans" font-size="8" fill="%s">%s</text>'
    % (18 + i * 22, c, 26 + i * 22, '#a8502e' if n.startswith('P') else '#6b4a38', n)
    for i, (n, c) in enumerate(SYS))

RING = ('<svg viewBox="0 0 372 176">%s'
        '<text x="88" y="86" text-anchor="middle" font-family="Liberation Serif" '
        'font-size="11" font-style="italic" fill="#6b4a38">7 sistemas</text>'
        '<text x="88" y="100" text-anchor="middle" font-family="Liberation Serif" '
        'font-size="11" font-style="italic" fill="#6b4a38">emocionales</text>%s</svg>'
        ) % (donut(88, 88, 72, 44, SYS), legend)

p5 = '''
<p class="eyebrow">Entender · Jaak Panksepp</p>
<h1 class="title">Por qué la separación duele</h1>
<p class="lead">El duelo no es un sentimiento sofisticado que solo tenemos los
humanos. Es un circuito antiguo que compartimos con ellos.</p>

<div class="fig">%s<div class="figcap">Los sistemas emocionales primarios descritos por Panksepp</div></div>

<p>Panksepp identificó siete sistemas emocionales básicos, alojados en zonas
profundas y evolutivamente antiguas del cerebro de todos los mamíferos. Uno de
ellos, el sistema de <strong>pánico y duelo</strong>, es el que se activa cuando
desaparece una figura de apego.</p>

<p>Ese circuito está regulado por los mismos opioides internos y la misma oxitocina
que en nosotros. Cuando el vínculo está presente, mantiene la calma. Cuando se
rompe, aparece la angustia de separación: llamadas, búsqueda, inquietud, pérdida
de apetito, sueño alterado.</p>

<div class="box green">
  <p class="lbl">Lo que esto significa en tu casa</p>
  <p>Tu perro o tu gato no «está raro». Tiene activado, ahora mismo, el mismo
  sistema cerebral que tienes activado tú. Con la diferencia de que él no puede
  contárselo a nadie, ni entender qué ha pasado, ni saber que esto va a pasar.</p>
</div>

<p class="note">Es también la razón por la que la presencia tranquila funciona
mejor que cualquier distracción: el sistema de pánico se calma con contacto y
previsibilidad, no con estímulos nuevos.</p>
''' % RING

# ------------------------------------------------------------ p6 · Pavlov
p6 = '''
<p class="eyebrow">Entender · Iván Pávlov</p>
<h1 class="title">Una casa llena de señales</h1>
<p class="lead">Para él, tu casa no es un espacio: es un sistema de anuncios.
Y todos siguen anunciando a alguien que ya no llega.</p>

<p>Durante años, cada detalle cotidiano quedó asociado a la presencia del
compañero. El ruido de dos cuencos al apoyarse en el suelo. La hora exacta del
paseo. El sonido de la correa. Tu forma de coger las llaves los sábados. El chirrido
de una puerta concreta.</p>

<p>Ninguno de esos estímulos era importante por sí mismo. Se volvieron importantes
por asociación — eso es, exactamente, lo que Pávlov describió. Y hoy siguen
disparando la misma expectativa: mirar a la puerta, ir a buscar, esperar.</p>

<div class="box left-terra">
  <p class="lbl">Por qué no se apaga de un día para otro</p>
  <p>Una asociación construida durante años no se borra en una semana. Se
  desactiva por exposición repetida: la señal aparece, y no pasa nada. Otra vez.
  Y otra. Ese proceso lleva semanas, y es normal que lleve semanas.</p>
</div>

<div class="box left-terra">
  <p class="lbl">La recuperación espontánea</p>
  <p>Un día, al mes largo, cuando ya parecía todo estabilizado, tu perro vuelve a
  esperar en la puerta durante horas. No ha recaído ni ha empeorado: Pávlov
  describió este fenómeno hace un siglo. Las respuestas ya extinguidas reaparecen
  solas tras un periodo de pausa, y vuelven a apagarse antes que la primera vez.</p>
</div>

<h2 class="sec">Qué hacer con esto</h2>
<ul class="clean terra">
  <li>No elimines de golpe todas las señales — el vacío total desorienta más que la ausencia.</li>
  <li>Mantén rígidos los horarios de comida, paseo y sueño: son las señales que sí siguen cumpliéndose.</li>
  <li>Cambia gradualmente lo que tenga que cambiar: un cuenco, un sitio, una ruta, de uno en uno.</li>
  <li>Cuando aparezca la espera en la puerta, no la castigues ni la premies. Llámale a hacer algo agradable dos minutos después.</li>
</ul>
'''

# ------------------------------------------------- p7 · Skinner (curva)
CURVE = '''
<svg viewBox="0 0 372 184">
  <defs><linearGradient id="sg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#748156" stop-opacity=".22"/>
    <stop offset="100%" stop-color="#748156" stop-opacity="0"/></linearGradient></defs>
  <line x1="34" y1="150" x2="356" y2="150" stroke="#e2cfb4" stroke-width="1"/>
  <line x1="34" y1="18"  x2="34"  y2="150" stroke="#e2cfb4" stroke-width="1"/>
  <path d="M34 150 L34 92 C46 80 56 34 74 30 C92 26 100 52 116 68
           C140 92 160 112 196 122 C232 132 250 128 266 122
           C276 118 282 100 292 100 C302 100 306 118 318 126
           C332 135 342 138 356 138 L356 150 Z" fill="url(#sg)"/>
  <path d="M34 92 C46 80 56 34 74 30 C92 26 100 52 116 68
           C140 92 160 112 196 122 C232 132 250 128 266 122
           C276 118 282 100 292 100 C302 100 306 118 318 126
           C332 135 342 138 356 138"
        fill="none" stroke="#748156" stroke-width="1.9" stroke-linecap="round"/>
  <line x1="74" y1="30" x2="74" y2="150" stroke="#a8502e" stroke-width=".8" stroke-dasharray="3 3"/>
  <line x1="292" y1="100" x2="292" y2="150" stroke="#a8502e" stroke-width=".8" stroke-dasharray="3 3"/>
  <circle cx="74" cy="30" r="3.4" fill="#a8502e"/>
  <circle cx="292" cy="100" r="3.4" fill="#a8502e"/>
  <text x="80" y="24" font-family="Liberation Sans" font-size="7.6" font-weight="bold"
        fill="#a8502e">ESTALLIDO DE EXTINCIÓN</text>
  <text x="215" y="92" font-family="Liberation Sans" font-size="7.6" font-weight="bold"
        fill="#a8502e">RECUPERACIÓN ESPONTÁNEA</text>
  <text x="38" y="14" font-family="Liberation Sans" font-size="7.4" fill="#9c7c63"
        letter-spacing=".7">CUÁNTO BUSCA</text>
  <text x="34" y="166" font-family="Liberation Sans" font-size="7.4" fill="#9c7c63">Día 1</text>
  <text x="186" y="166" font-family="Liberation Sans" font-size="7.4" fill="#9c7c63"
        text-anchor="middle">Día 10</text>
  <text x="356" y="166" font-family="Liberation Sans" font-size="7.4" fill="#9c7c63"
        text-anchor="end">Día 30</text>
</svg>'''

p7 = '''
<p class="eyebrow">Entender · B. F. Skinner</p>
<h1 class="title">Por qué busca más al principio</h1>
<p class="lead">Si estos días te parece que está peor que el primero, no te lo
estás imaginando. Y no significa que vaya a peor.</p>

<div class="fig">%s<div class="figcap">Curva típica de la conducta de búsqueda tras la pérdida del compañero</div></div>

<p>Buscar al compañero era, durante años, una conducta que funcionaba: buscabas y
lo encontrabas. Ahora ya no funciona nunca. Cuando una conducta deja de obtener su
resultado, entra en <strong>extinción</strong> — pero la extinción casi nunca
empieza bajando.</p>

<p>Empieza subiendo. El animal insiste más, busca más, llama más fuerte, recorre
más veces la casa. Es el <em>estallido de extinción</em> que describió Skinner, y
suele aparecer entre el tercer y el décimo día. Después, si el entorno se mantiene
estable, empieza a bajar de verdad.</p>

<div class="box green">
  <p class="lbl">Lo que esto te ahorra</p>
  <p>Saber esto evita el error más común de estos días: pensar que lo que estás
  haciendo no funciona, y cambiarlo todo justo cuando el proceso estaba
  avanzando. La subida de la primera semana es parte del camino, no su fracaso.</p>
</div>

<p class="note">Si pasadas tres o cuatro semanas la búsqueda no ha empezado a
bajar en absoluto, entonces sí: consulta. Puede haber otra cosa por debajo.</p>
''' % CURVE

# ------------------------------------------------------ p8 · Horowitz
BARS = '''
<svg viewBox="0 0 372 118">
  <text x="0" y="20" font-family="Liberation Sans" font-size="8" fill="#6b4a38">Perro</text>
  <rect x="52" y="10" width="300" height="15" rx="3" fill="#a8502e"/>
  <text x="358" y="21" font-family="Liberation Sans" font-size="7.6" fill="#a8502e"
        text-anchor="end" transform="translate(-6,0)"></text>
  <text x="344" y="21" font-family="Liberation Sans" font-size="8" fill="#fdf8f0"
        text-anchor="end" font-weight="bold">200-300 millones</text>
  <text x="0" y="58" font-family="Liberation Sans" font-size="8" fill="#6b4a38">Gato</text>
  <rect x="52" y="48" width="82" height="15" rx="3" fill="#748156"/>
  <text x="140" y="59" font-family="Liberation Sans" font-size="8" fill="#748156">60-80 millones</text>
  <text x="0" y="96" font-family="Liberation Sans" font-size="8" fill="#6b4a38">Tú</text>
  <rect x="52" y="86" width="7" height="15" rx="2" fill="#c9a98a"/>
  <text x="65" y="97" font-family="Liberation Sans" font-size="8" fill="#9c7c63">5-6 millones</text>
  <text x="52" y="120" font-family="Liberation Sans" font-size="7.4" fill="#9c7c63"
        font-style="italic">Receptores olfativos · a escala real</text>
</svg>'''

p8 = '''
<p class="eyebrow">Entender · Alexandra Horowitz</p>
<h1 class="title">Su mundo está hecho de olor</h1>
<p class="lead">Lo primero que la mayoría de la gente hace es lavarlo todo. Es,
casi siempre, lo peor que se puede hacer.</p>

<div class="fig">%s</div>

<p>Horowitz recuperó una idea clave: cada especie vive en su propio mundo
perceptivo. El nuestro es visual. El del perro es olfativo, en una proporción que
cuesta imaginar — su bulbo olfatorio es, en relación a su cerebro, unas cuarenta
veces mayor que el nuestro.</p>

<p>Para él, el olor no es un recuerdo: es información presente. Fuerte significa
«hace poco»; débil, «hace tiempo». Es su forma de leer el paso del tiempo.</p>

<div class="box left-green">
  <p class="lbl">La regla del olor</p>
  <p>No laves ni retires de golpe la manta, la cama o el collar del que se fue.
  Ese rastro que se va desvaneciendo, día tras día, es exactamente el mecanismo por
  el que su cerebro entiende que ya no vuelve. Quitarlo de golpe no le ahorra
  dolor: le borra la explicación.</p>
</div>

<h2 class="sec">Cómo aplicarla</h2>
<ul class="clean">
  <li>Deja sus cosas al menos las dos primeras semanas, en el mismo sitio.</li>
  <li>Permítele olerlas todo el tiempo que quiera. No le interrumpas ni le llames.</li>
  <li>Retira después un objeto por semana, empezando por el que menos use.</li>
  <li>Guarda una prenda suya sin lavar, en una bolsa cerrada, por si hace falta más adelante.</li>
  <li>Suma paseos de olfato: veinte minutos eligiendo él dónde huele calman más que una hora de correr.</li>
</ul>
''' % BARS

# ------------------------------------------------- p9 · Lorenz y Hare
p9 = '''
<p class="eyebrow">Entender · Konrad Lorenz y Brian Hare</p>
<h1 class="title">Qué se ha roto exactamente</h1>
<p class="lead">No ha perdido «compañía». Ha perdido una pieza de su propio
sistema de regulación.</p>

<h2 class="sec">Lorenz: el duelo existía antes que nosotros</h2>
<p>Observando gansos salvajes que perdían a su pareja, Lorenz anotó una lista de
signos que le resultaba inquietantemente familiar: la mirada se apaga, la cabeza
se hunde entre los hombros, el animal pierde rango dentro del grupo, se vuelve
temeroso — y emprende vuelos de búsqueda llamando sin parar.</p>
<p>Él mismo señaló que era, punto por punto, lo que la psicología describía en
niños separados de su madre. El duelo no es una construcción cultural humana: es
lo que ocurre cuando se rompe un vínculo social en un animal social.</p>

<div class="quote green">Lo que ves en tu perro o en tu gato<br>
tiene más de cincuenta años<br>de literatura científica detrás.</div>

<h2 class="sec">Hare: y además te está leyendo a ti</h2>
<p>El trabajo de Hare mostró que los perros interpretan nuestras señales
comunicativas mejor que ningún otro animal — mejor incluso que los chimpancés — y
que su historia evolutiva seleccionó justamente eso: cooperación, atención al
humano, sensibilidad social.</p>

<div class="box left-terra">
  <p class="lbl">La consecuencia incómoda</p>
  <p>Tu perro no está atravesando su duelo en un entorno neutro. Está atravesándolo
  contigo dentro. Tu tono de voz, tus horarios rotos, tus silencios largos y tu
  cuerpo tenso forman parte de lo que él tiene que gestionar.</p>
  <p>Esto no es para que te sientas culpable: es imposible no estar triste, y
  esconderlo tampoco funciona. Es para que sepas que las dos cosas que más le
  ayudan — rutina estable y tono tranquilo — son también las dos que más te
  ayudan a ti. Podéis hacerlas juntos.</p>
</div>
'''

# --------------------------------------------------------- p10 · Grandin
p10 = '''
<p class="eyebrow">Actuar · Temple Grandin</p>
<h1 class="title">El entorno que calma</h1>
<p class="lead">Los animales no piensan en conceptos: piensan en detalles
concretos. Un objeto movido puede pesar más que toda tu buena intención.</p>

<p>Grandin cambió el diseño de instalaciones ganaderas al demostrar algo que hasta
entonces se ignoraba: lo que asusta a un animal no suele ser lo grande, sino lo
pequeño y nuevo. Una sombra distinta, un reflejo, un objeto fuera de sitio, un
sonido que antes no estaba.</p>

<p>En una casa en duelo, todo eso cambia a la vez. Se mueven muebles, se guardan
cosas, entran visitas, se rompen los horarios, hay llanto, hay silencios raros. Para
el animal que se quedó, la pérdida no viene sola: viene con un entorno que dejó de
ser predecible justo cuando más lo necesitaba.</p>

<div class="box green">
  <p class="lbl">Las cuatro reglas del entorno</p>
  <p><strong>1 · Previsible.</strong> Horarios de comida, paseo y sueño clavados,
  aunque tú estés fatal. Es lo que más baja el cortisol.<br>
  <strong>2 · Reconocible.</strong> Nada de mudanzas, obras, reformas ni viajes
  este mes, si puedes evitarlo.<br>
  <strong>3 · Sensorialmente amable.</strong> Menos ruido, luz suave por la noche,
  un lugar de descanso caliente y sin corrientes.<br>
  <strong>4 · Con algo que hacer.</strong> El sistema de búsqueda necesita
  activarse: olfatear, resolver, explorar.</p>
</div>

<p>Esa última regla es la que la gente olvida. Grandin lo formula casi como una
consigna de bienestar: no basta con quitar el miedo, hay que dar algo que buscar.
Un animal que no puede activar el sistema de búsqueda se apaga.</p>

<p class="note">Y una advertencia suya que aquí importa mucho: lo nuevo puede ser
enriquecimiento o puede ser amenaza, y la diferencia está en si el animal puede
elegir acercarse. Ofrece siempre; nunca impongas.</p>
'''

# ----------------------------------------------------------- p11 · Gruen
p11 = '''
<p class="eyebrow">Observar · Margaret Gruen</p>
<h1 class="title">¿Es duelo, o es dolor?</h1>
<p class="lead">Este capítulo es el más importante del libro. Confundir una cosa
con la otra retrasa diagnósticos y cuesta vidas.</p>

<p>Desde la medicina del comportamiento, Gruen insiste en algo que a menudo se pasa
por alto: <strong>un cambio de conducta es, muchas veces, el primer signo de
dolor o de enfermedad</strong>, mucho antes de que aparezca una cojera o un
síntoma evidente.</p>

<p>El problema es el momento. Si tu gato deja de comer la semana en que murió su
compañero, lo lógico es pensar «está de duelo». Y puede serlo. Pero también puede
ser una enfermedad que empezó justo entonces — y la etiqueta de duelo hace que
esperes dos semanas de más.</p>

<table>
  <thead><tr><th style="width:92pt">Lo que ves</th><th>Puede ser duelo</th>
  <th>Descarta dolor o enfermedad</th></tr></thead>
  <tbody>
    <tr><td>Come menos</td><td>Baja parcial unos días, luego se recupera</td>
        <td>Rechazo total, o baja que dura más de 3-4 días</td></tr>
    <tr><td>Se mueve menos</td><td>Duerme más, menos iniciativa, responde si le llamas</td>
        <td>Rigidez, cojera, evita saltar o subir, se queja al tocarlo</td></tr>
    <tr><td>Se esconde</td><td>Busca sitios altos o cerrados, sale a comer</td>
        <td>No sale nunca, postura encogida, no se asea</td></tr>
    <tr><td>Vocaliza</td><td>Llamadas al compañero, sobre todo al principio</td>
        <td>Quejido al moverse, maullido nocturno nuevo en animal mayor</td></tr>
    <tr><td>Se lame o acicala</td><td>Algo más de acicalado, sin lesión</td>
        <td>Zona concreta, calva, herida, o deja de asearse del todo</td></tr>
  </tbody>
</table>

<div class="box left-terra">
  <p class="lbl">Qué llevar a la consulta</p>
  <p>Lleva datos, no impresiones: cuántos días lleva comiendo menos, cuánto pesa
  hoy comparado con antes, a qué hora ocurre lo que ves, y un vídeo corto con el
  móvil. Un vídeo de treinta segundos vale más que diez minutos de explicación.</p>
</div>
'''

# -------------------------------------------------------- p12 · semáforo
p12 = '''
<p class="eyebrow">Observar</p>
<h1 class="title">El semáforo de señales</h1>
<p class="lead">Qué es esperable, qué hay que vigilar y qué no admite espera.
Ten esta página a mano las próximas semanas.</p>

<div class="sem">
  <p class="lbl">Verde · esperable, acompaña y observa</p>
  <p>Busca por la casa y huele sus sitios · espera en la puerta o en su cama ·
  duerme más de lo habitual · come algo menos durante unos días · se pega a ti y
  te sigue de habitación en habitación · vocaliza más los primeros días ·
  juega menos · duerme en el sitio del que se fue.</p>
</div>

<div class="sem amber">
  <p class="lbl">Ámbar · ajusta y consulta si dura más de dos semanas</p>
  <p>Come claramente menos durante más de tres o cuatro días · no juega nada en
  absoluto · se esconde la mayor parte del día · vocalización nocturna nueva ·
  se lame o se acicala en exceso · orina o defeca en casa habiéndolo dejado de
  hacer hace años · destroza cosas cuando te vas · no puede quedarse solo ni un
  minuto.</p>
</div>

<div class="sem red">
  <p class="lbl">Rojo · llama al veterinario hoy</p>
  <p>Un gato que no come nada en 24 horas — es una urgencia real, por riesgo de
  lipidosis hepática · un perro que no come nada en 48 horas · vómitos o diarrea
  · pérdida de peso rápida · no bebe · letargo extremo, no responde a estímulos ·
  jadeo, temblor o inquietud constantes · agresividad que antes no existía ·
  autolesión · cualquier signo de dolor.</p>
</div>

<p class="note">Ante la duda, llama. Ningún veterinario te va a reprochar una
consulta de más en el mes en que se te acaba de morir un animal — y la mitad de
los casos ámbar se resuelven con una llamada de diez minutos.</p>
'''

# --------------------------------------------------- p13 · lenguaje corporal
p13 = '''
<p class="eyebrow">Observar</p>
<h1 class="title">Leer lo que no te puede decir</h1>
<p class="lead">Todo lo que necesitas saber sobre cómo está te lo está diciendo
con el cuerpo, ahora mismo.</p>

<table>
  <thead><tr><th style="width:128pt">Lo que hace</th><th style="width:104pt">Qué suele significar</th>
  <th>Qué hacer tú</th></tr></thead>
  <tbody>
    <tr><td>Bosteza o se lame el hocico sin motivo</td><td>Tensión leve, señal de calma</td>
        <td>Baja el ritmo, aparta la mirada, dale espacio</td></tr>
    <tr><td>Aparta la mirada cuando le hablas</td><td>Evita el conflicto, está saturado</td>
        <td>No insistas en el contacto ahora</td></tr>
    <tr><td>Se ve el blanco del ojo, pupila muy dilatada</td><td>Tensión alta</td>
        <td>Retírate y reduce estímulos de golpe</td></tr>
    <tr><td>Orejas atrás, cuerpo bajo, cola recogida</td><td>Miedo o inseguridad</td>
        <td>Voz baja, rutina, nada nuevo hoy</td></tr>
    <tr><td>Te sigue a todas partes, no te pierde de vista</td><td>Búsqueda de seguridad</td>
        <td>Atención programada tú, no cuando la pide</td></tr>
    <tr><td>Olfatea largo un rincón, inmóvil</td><td>Está leyendo información</td>
        <td>No le interrumpas nunca. Espera</td></tr>
    <tr><td>Aullido o maullido largo y repetido</td><td>Llamada de separación</td>
        <td>Rutina, presencia, veterinario si persiste</td></tr>
    <tr><td>Duerme en el sitio del compañero</td><td>Procesa el vínculo</td>
        <td>Permíteselo. No es morboso, es adaptativo</td></tr>
  </tbody>
</table>

<p class="note">En gatos, añade tres señales propias: dejar de usar sitios altos,
cambios en la caja de arena y dejar de acicalarse. Las tres son motivo de consulta
si duran más de unos días.</p>
'''

# ------------------------------------------------- p14 · mapa protocolo
MAPA = '''
<svg viewBox="0 0 372 108">
  <rect x="0"   y="28" width="118" height="34" rx="6" fill="#e6eada"/>
  <rect x="127" y="28" width="118" height="34" rx="6" fill="#f6e9d6"/>
  <rect x="254" y="28" width="118" height="34" rx="6" fill="#f0dccd"/>
  <text x="59"  y="44" text-anchor="middle" font-family="Liberation Sans" font-size="8"
        font-weight="bold" fill="#748156" letter-spacing="1">DÍAS 1-7</text>
  <text x="59"  y="56" text-anchor="middle" font-family="Liberation Serif" font-size="10.5"
        fill="#3b2a20">Sostener</text>
  <text x="186" y="44" text-anchor="middle" font-family="Liberation Sans" font-size="8"
        font-weight="bold" fill="#9a6c1e" letter-spacing="1">DÍAS 8-14</text>
  <text x="186" y="56" text-anchor="middle" font-family="Liberation Serif" font-size="10.5"
        fill="#3b2a20">Reconstruir</text>
  <text x="313" y="44" text-anchor="middle" font-family="Liberation Sans" font-size="8"
        font-weight="bold" fill="#a8502e" letter-spacing="1">DÍAS 15-21</text>
  <text x="313" y="56" text-anchor="middle" font-family="Liberation Serif" font-size="10.5"
        fill="#3b2a20">Avanzar</text>
  <path d="M119 45 l6 0" stroke="#9c7c63" stroke-width="1.2"/>
  <path d="M246 45 l6 0" stroke="#9c7c63" stroke-width="1.2"/>
  <text x="0"   y="80" font-family="Liberation Sans" font-size="7.4" fill="#9c7c63">Estabilidad y olor</text>
  <text x="127" y="80" font-family="Liberation Sans" font-size="7.4" fill="#9c7c63">Calma reforzada y olfato</text>
  <text x="254" y="80" font-family="Liberation Sans" font-size="7.4" fill="#9c7c63">Nueva normalidad</text>
</svg>'''

p14 = '''
<p class="eyebrow terra">Actuar</p>
<h1 class="title">El protocolo de 21 días</h1>
<p class="lead">Tres semanas, tres fases, una tarea al día. Pensado para hacerse
mientras tú también estás mal.</p>

<div class="fig">%s</div>

<p>Veintiún días no es un plazo mágico: es el tiempo que suele tardar la conducta
de búsqueda en completar su curva, según lo que vimos en la página de Skinner.
Algunos animales necesitan menos. Otros, sobre todo los que llevaban toda la vida
con el compañero, necesitan bastante más.</p>

<div class="box green">
  <p class="lbl">Tres reglas para todo el protocolo</p>
  <p><strong>No fuerces nada.</strong> Ofrece siempre, impón nunca. Si rechaza una
  propuesta, no insistas: repítela mañana.<br>
  <strong>Adelántate a la demanda.</strong> Dale atención cuando está tranquilo,
  antes de que la pida llorando.<br>
  <strong>Registra.</strong> Tres marcas al día en la página final. Sin registro no
  vas a poder distinguir una mala tarde de un empeoramiento real.</p>
</div>

<div class="box left-terra">
  <p class="lbl">Antes del día 1</p>
  <p>Si hay cualquier señal roja del semáforo, el protocolo no empieza hoy: empieza
  la consulta veterinaria. Este plan asume un animal sano que está triste, no un
  animal enfermo.</p>
</div>
''' % MAPA

# ------------------------------------------------------------ fases
FASES = [
 ("Sostener", "Días 1 a 7", "01",
  "Estabilidad total. No se cambia nada, no se retira nada, no se exige nada. "
  "Tu único objetivo esta semana es que el entorno vuelva a ser predecible.",
  [("1","Fija los horarios de comida, paseo y sueño, y escríbelos en un papel visible. No se mueven en 21 días."),
   ("2","Deja todos los objetos del compañero exactamente donde están. Su cama, su manta, su cuenco."),
   ("3","Permítele oler esos objetos todo el tiempo que quiera, sin llamarle ni interrumpirle."),
   ("4","Quince minutos de presencia tranquila: en la misma habitación, sin exigir contacto ni juego."),
   ("5","Comprueba y anota lo básico: come, bebe, orina, defeca, duerme. Sí o no."),
   ("6","Paseo de olfato de veinte minutos, dejándole elegir dónde huele. Nada de correr ni entrenar."),
   ("7","Revisión de la semana — repasa el semáforo entero y decide si hace falta llamar al veterinario.")],
  "Esta semana es normal que empeore. Es el estallido de extinción: busca más, "
  "llama más, duerme peor. No cambies el plan por ello."),

 ("Reconstruir", "Días 8 a 14", "02",
  "Empezar a reforzar la calma y a reactivar el sistema de búsqueda, sin retirar "
  "todavía nada de lo que le ancla.",
  [("8","Refuerza la calma: cada vez que le veas tumbado y relajado, acércate y prémiale en voz baja."),
   ("9","Atención programada: tres momentos fijos al día que empiezas tú, no cuando él la reclama."),
   ("10","Nosework en casa: esconde diez premios por una habitación y déjale buscarlos solo."),
   ("11","Ofrece juego corto, dos minutos. Si no responde, guárdalo y vuelve a ofrecerlo mañana."),
   ("12","Retira el primer objeto: el que menos use. Solo uno. Guárdalo sin lavar."),
   ("13","Salida distinta: una ruta nueva, corta, tranquila. Que pueda parar a oler cuanto quiera."),
   ("14","Revisión de la semana — compara con el día 7. ¿La búsqueda ha empezado a bajar?")],
  "Si vive pegado a ti, empieza también trabajo de independencia: sal de la "
  "habitación treinta segundos y vuelve sin saludar. Ve alargando poco a poco."),

 ("Avanzar", "Días 15 a 21", "03",
  "Consolidar la nueva normalidad y decidir, con datos, si hace falta algo más.",
  [("15","Consolida la rutina nueva: la que quieres mantener dentro de seis meses, no la de emergencia."),
   ("16","Retira un segundo objeto. Mantén siempre al menos uno con su olor."),
   ("17","Encuentro social tranquilo: un perro conocido y afín, o una persona a la que quiera. Sin multitudes."),
   ("18","Enriquecimiento estable: kong, tapete de olfateo o juguete dispensador, a la misma hora cada día."),
   ("19","Repasa el semáforo completo y compáralo con el del día 7."),
   ("20","Si sigue habiendo señales ámbar, pide cita veterinaria y lleva tu registro y un vídeo."),
   ("21","Revisión final — compara el día 21 con el día 1, categoría por categoría.")],
  "Al terminar, no retomes la vida anterior: construye la nueva. La rutina que "
  "sostengas a partir de aquí es la que va a sostenerle a él."),
]

def fase_page(name, days, num, obj, items, tip):
    rows = ''.join(
        '<tr><td class="day">%s</td><td>%s</td><td class="tick"><span class="chk"></span></td></tr>'
        % (d, t) for d, t in items)
    return '''
<div class="wk-head">
  <div class="wk-num terra">%s</div>
  <div class="txt"><p class="eyebrow terra">%s</p><h1 class="title">Fase %s: %s</h1></div>
</div>

<div class="box green">
  <p class="lbl">Objetivo de la fase</p>
  <p>%s</p>
</div>

<table>
  <thead class="terra"><tr><th style="width:26pt">Día</th><th>Qué hacer</th>
  <th class="tick">&#10003;</th></tr></thead>
  <tbody>%s</tbody>
</table>

<div class="dashed">
  <p style="font-size:8.6pt;line-height:1.6;margin:0">
  <b style="color:#a8502e">Ojo:</b> %s</p>
</div>
''' % (num, days, num.lstrip('0'), name, obj, rows, tip)

# ------------------------------------------- p18 · refuerzo y errores
p18 = '''
<p class="eyebrow">Actuar · B. F. Skinner aplicado</p>
<h1 class="title">Reforzar la calma, no el llanto</h1>
<p class="lead">Sin querer, es fácil enseñarle que la única forma de conseguirte
es estar mal.</p>

<p>Si solo te acercas cuando llora, cuando aúlla o cuando rasca la puerta, esas
conductas obtienen tu presencia — que es justo lo que más valor tiene para él ahora
mismo. La consecuencia es que se hacen más frecuentes. No porque manipule: porque
así funciona el aprendizaje.</p>

<div class="box green">
  <p class="lbl">La regla de los tres momentos</p>
  <p>Elige tres momentos fijos del día para darle atención plena. Los empiezas
  tú. Y busca activamente, varias veces al día, momentos en los que esté tumbado y
  tranquilo, para acercarte, acariciarle en voz baja o dejarle un premio junto a la
  cama. Eso es reforzar la calma.</p>
</div>

<h2 class="sec">Los ocho errores más frecuentes</h2>
<ul class="clean terra">
  <li><b>Retirarlo todo el primer día</b> «para que no sufra». Le borras la información que necesita.</li>
  <li><b>Adoptar otro animal de inmediato</b> para que no esté solo. Añade estrés justo cuando menos margen tiene.</li>
  <li><b>Atender solo cuando llora.</b> Refuerzas exactamente la conducta que quieres reducir.</li>
  <li><b>Cambiarlo todo:</b> mudanza, obras, viajes, muebles nuevos. Este mes, si puedes, nada de eso.</li>
  <li><b>Llamar duelo a lo que es dolor.</b> Revisa siempre la página del semáforo antes de interpretar.</li>
  <li><b>Forzar el juego o el contacto.</b> Ofrecer sí, insistir no.</li>
  <li><b>Castigar las conductas regresivas</b> — pipí en casa, destrozos. Son síntomas, no desafíos.</li>
  <li><b>Olvidarte de ti.</b> Tu estado es su entorno. Cuidarte a ti es, literalmente, cuidarle a él.</li>
</ul>

<p class="note">Y uno que no es un error, aunque lo parezca: hablarle en voz alta
del que se fue. Puedes hacerlo. A él le llega tu tono, y a ti te hace bien.</p>
'''

# ---------------------------------------------- p19 · otro compañero
p19 = '''
<p class="eyebrow">Decidir</p>
<h1 class="title">¿Otro compañero para él?</h1>
<p class="lead">La pregunta llega siempre. La respuesta correcta depende del
animal que tienes delante, no de lo que a ti te alivie.</p>

<div class="grid2">
  <div class="box green" style="height:auto">
    <p class="lbl">Señales de que podría ir bien</p>
    <p>Ha recuperado apetito y sueño · busca a otros animales en la calle ·
    siempre fue sociable · han pasado al menos seis u ocho semanas · puedes
    decidirlo con la cabeza serena, no para llenar tu propio silencio.</p>
  </div>
  <div class="box left-terra" style="height:auto">
    <p class="lbl">Señales de que todavía no</p>
    <p>Sigue sin comer bien o sin dormir · no juega nada · siempre prefirió estar
    solo · es mayor, tiene dolor o una enfermedad crónica · han pasado menos de
    seis semanas · lo piensas porque no soportas verle triste.</p>
  </div>
</div>

<h2 class="sec">Si decides que sí</h2>
<ul class="clean">
  <li><b>Terreno neutro.</b> La primera presentación, fuera de casa: un paseo paralelo, sin saludo forzado.</li>
  <li><b>Recursos duplicados.</b> Dos camas, dos cuencos, dos bebederos, dos areneros más uno, en sitios distintos.</li>
  <li><b>Espacios separados</b> las primeras semanas, con encuentros cortos que terminas tú antes de que se tuerzan.</li>
  <li><b>Nada de comparar.</b> No busques uno «parecido» al que se fue: esa comparación le perjudica desde el primer día.</li>
  <li><b>Prioriza al que ya está.</b> Su rutina, su sitio y su atención se mantienen intactos. El que llega se adapta a ellos.</li>
</ul>

<div class="box left-green">
  <p class="lbl">Y una posibilidad que casi nadie plantea</p>
  <p>Algunos animales, tras años compartiendo casa, están mejor solos: más
  tranquilos y con menos competencia por los recursos. Si el tuyo mejora semana a
  semana estando solo, esa también es una respuesta.</p>
</div>
'''

# ------------------------------------------------- p20 · registro 21 días
rows21 = ''.join(
    '<tr><td class="day green">%d</td><td></td><td></td><td></td><td></td><td></td></tr>' % d
    for d in range(1, 22))
p20 = '''
<p class="eyebrow">Registro</p>
<h1 class="title">Mis 21 días</h1>
<p class="lead">Una marca por casilla. Sin registro no hay forma de distinguir una
mala tarde de un empeoramiento real.</p>

<table class="compact" style="margin-bottom:6pt">
  <thead><tr><th style="width:24pt">Día</th><th style="width:44pt">Come</th>
  <th style="width:44pt">Bebe</th><th style="width:46pt">Duerme</th>
  <th style="width:44pt">Juega</th><th>Qué he observado hoy</th></tr></thead>
  <tbody>%s</tbody>
</table>

<p class="note" style="margin-top:4pt">Marca &#10003; si es normal, &#8211; si está
por debajo de lo habitual, &#10007; si no lo hace en absoluto. En la última columna,
tres palabras bastan. Compara el día 21 con el día 1 columna por columna.</p>
''' % rows21

# ------------------------------------------------------------ p21 · cierre
p21 = '''
<p class="eyebrow">Para cerrar</p>
<h1 class="title">Los dos duelos de esta casa</h1>

<p>Hay algo que muchas personas descubren en estas semanas y que casi nadie
anticipa: cuidar del animal que se quedó las sostiene a ellas.</p>

<p>Porque obliga a levantarse a una hora. A salir a la calle. A comprar comida. A
mantener una rutina cuando lo único que apetece es no tener ninguna. Y porque, al
final del día, hay alguien que sigue subiéndose al sofá.</p>

<p>No es casualidad. Las dos cosas que mejor funcionan para él — rutina estable y
presencia tranquila — son exactamente las dos que mejor funcionan para ti. Este
libro es, en el fondo, un mismo plan escrito para dos.</p>

<div class="quote">Estáis haciendo el duelo juntos.<br>
Tu calma es su calma.<br>Y su compañía, aunque no lo parezca hoy, es la tuya.</div>

<hr class="rule soft">

<h2 class="sec">Para seguir leyendo</h2>
<p class="ref"><b>Konrad Lorenz</b> — <em>Hablaba con las bestias, los peces y los
pájaros</em> · <em>Cuando el hombre encontró al perro</em>.</p>
<p class="ref"><b>Jaak Panksepp</b> — <em>Affective Neuroscience</em> ·
<em>The Archaeology of Mind</em>.</p>
<p class="ref"><b>Alexandra Horowitz</b> — <em>En la mente de un perro</em> ·
<em>Ser perro</em>.</p>
<p class="ref"><b>Brian Hare y Vanessa Woods</b> — <em>El genio de los perros</em> ·
<em>La supervivencia de los más amigables</em>.</p>
<p class="ref"><b>Temple Grandin</b> — <em>Interpretar a los animales</em> ·
<em>Cómo hacer felices a los animales</em>.</p>
<p class="ref"><b>B. F. Skinner</b> — <em>Ciencia y conducta humana</em>.</p>
<p class="ref"><b>Iván Pávlov</b> — <em>Los reflejos condicionados</em>.</p>
<p class="ref"><b>Margaret Gruen</b> — publicaciones sobre dolor y medicina del
comportamiento, College of Veterinary Medicine, NC State University.</p>

<p class="note" style="text-align:center;margin-top:14pt">
Sigue Contigo — Libro 4 de 4 · Ellos También se Despiden<br>tremdora</p>
'''

pages = [page(cover, cls='cover'), page(p2, 2), page(p3, 3), page(p4, 4), page(p5, 5),
         page(p6, 6), page(p7, 7), page(p8, 8), page(p9, 9), page(p10, 10),
         page(p11, 11), page(p12, 12), page(p13, 13), page(p14, 14)]
for i, (nm, dy, num, obj, items, tip) in enumerate(FASES):
    pages.append(page(fase_page(nm, dy, num, obj, items, tip), 15 + i))
pages += [page(p18, 18), page(p19, 19), page(p20, 20), page(p21, 21)]

html = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<title>Sigue Contigo — Ellos También se Despiden</title><style>%s</style>'
        '</head><body>%s</body></html>') % (CSS, ''.join(pages))
open(D + '/libro4-ellos-tambien-se-despiden.html', 'w', encoding='utf-8').write(html)
print('escrito libro4', len(pages), 'páginas')
