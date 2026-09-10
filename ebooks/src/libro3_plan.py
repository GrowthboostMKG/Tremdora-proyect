# -*- coding: utf-8 -*-
"""Sigue Contigo — Libro 3 de 4 · Plan Práctico de 8 Semanas (generador HTML)."""

D = __file__.rsplit('/', 1)[0]
CSS = open(D + '/tremdora.css', encoding='utf-8').read()
FOOT = ('<div class="pfoot"><span>Plan Práctico de 8 Semanas · Sigue Contigo · Libro 3 de 4</span>'
        '<span class="n">{}</span></div>')

def page(inner, n=None, cls=''):
    return '<div class="page %s">%s%s</div>' % (cls, inner, FOOT.format(n) if n else '')

EMBLEM = '''
<svg viewBox="0 0 150 150">
  <circle cx="75" cy="75" r="62" fill="none" stroke="#748156" stroke-width="1.1"/>
  <path d="M34 104 C50 104 52 76 68 76 C84 76 86 52 104 52 C112 52 116 55 120 60"
        fill="none" stroke="#c1613a" stroke-width="2" stroke-linecap="round"/>
  <circle cx="34" cy="104" r="4.4" fill="#fbf3e6" stroke="#a8502e" stroke-width="1.6"/>
  <circle cx="68" cy="76"  r="4.4" fill="#fbf3e6" stroke="#a8502e" stroke-width="1.6"/>
  <circle cx="104" cy="52" r="4.4" fill="#fbf3e6" stroke="#a8502e" stroke-width="1.6"/>
  <path d="M120 60 l6 -3 -1 6z" fill="#a8502e"/>
  <text x="75" y="128" text-anchor="middle" font-family="Liberation Serif"
        font-size="15" font-style="italic" fill="#9c7c63">8 semanas</text>
</svg>'''

cover = '''
<div class="badge">Libro 3 de 4 · la hoja de ruta</div>
<div class="kicker">Programa día a día</div>
<div class="emblem">%s</div>
<h1>Plan Práctico<br>de <i>8 Semanas</i></h1>
<div class="sub">Una tarea pequeña cada día,<br>para no tener que decidir nada cuando no puedes decidir</div>
<div class="foot">Tercer libro de la serie <b>Sigue Contigo</b><br>
Basado en los diez capítulos del eBook</div>
''' % EMBLEM

ARCO = '''
<svg viewBox="0 0 372 118">
  <path d="M18 92 C70 92 78 30 130 30 C182 30 188 74 238 74 C290 74 296 24 354 24"
        fill="none" stroke="#e2cfb4" stroke-width="8" stroke-linecap="round"/>
  <path d="M18 92 C70 92 78 30 130 30 C182 30 188 74 238 74 C290 74 296 24 354 24"
        fill="none" stroke="#c1613a" stroke-width="1.6" stroke-dasharray="3 4"/>
  %s
</svg>'''
_pts = [(18,92,'1'),(66,89,'2'),(112,36,'3'),(158,30,'4'),
        (204,58,'5'),(250,74,'6'),(300,45,'7'),(354,24,'8')]
ARCO = ARCO % ''.join(
    '<circle cx="%d" cy="%d" r="7.5" fill="#fbf3e6" stroke="#748156" stroke-width="1.4"/>'
    '<text x="%d" y="%d" text-anchor="middle" font-family="Liberation Sans" font-size="7.4"'
    ' font-weight="bold" fill="#748156">%s</text>' % (x, y, x, y + 2.6, t)
    for x, y, t in _pts)

p2 = '''
<p class="eyebrow">Sobre este plan</p>
<h1 class="title">Plan Práctico de 8 Semanas</h1>
<p class="lead">Un paso concreto cada día. Sin tener que decidir qué hacer, ni
recordar en qué capítulo estaba lo que necesitas hoy.</p>

<p>El duelo agota la capacidad de decidir. Esa es una de las cosas que menos se
cuentan: no es solo que estés triste, es que elegir qué desayunar se vuelve una
montaña. Por eso este plan existe.</p>

<p>Toma los diez capítulos del eBook <em>Sigue Contigo</em> y los quince ejercicios que
contiene, y los reparte en una secuencia de ocho semanas: una tarea por día,
pequeña, concreta, hecha para días en los que no queda casi nada.</p>

<div class="fig">%s<div class="figcap">Las ocho semanas no bajan en línea recta — y este plan tampoco lo pretende</div></div>

<div class="box left-terra">
  <p class="lbl">Esto no es un tratamiento</p>
  <p>Es una estructura de acompañamiento. Si el dolor te desborda de forma sostenida,
  o aparece la idea de no querer seguir aquí, esto no sustituye a un profesional:
  busca ayuda hoy, no la semana que viene.</p>
</div>

<p class="note">Usa el <em>Diario del Oleaje</em> (segundo libro de la serie) en paralelo:
este plan te dice qué hacer, el diario recoge cómo te fue.</p>
''' % ARCO

p3 = '''
<p class="eyebrow">Antes de empezar</p>
<h1 class="title">Lo que vas a necesitar</h1>

<div class="grid2" style="margin-bottom:12pt">
  <div>
    <p><span class="pill"><b>Un cuaderno</b> y un bolígrafo</span></p>
    <p><span class="pill"><b>Papel suelto</b> para las cartas</span></p>
    <p><span class="pill"><b>Una vela</b></span></p>
    <p><span class="pill"><b>Sus fotos</b>, las que puedas mirar</span></p>
  </div>
  <div>
    <p><span class="pill"><b>Una caja</b> para sus cosas</span></p>
    <p><span class="pill"><b>Una planta</b> viva</span></p>
    <p><span class="pill"><b>Un sitio</b> de la casa para su rincón</span></p>
    <p><span class="pill"><b>El Diario</b> del Oleaje</span></p>
  </div>
</div>

<div class="box green">
  <p class="lbl">Cómo leer cada semana</p>
  <p>Cada página tiene un objetivo y siete tareas, una por día. Los días no tienen
  que coincidir con lunes a domingo: empieza cualquier día y sigue el orden. Si un
  día no puedes, pásala al siguiente. Aquí no se suspende, y no hay retraso posible.</p>
</div>

<div class="box left-terra">
  <p class="lbl">Puedes saltarte semanas</p>
  <p>Si la semana 3 —la de la culpa— no es la tuya porque no hubo decisión que tomar,
  pásala. Si la semana 7 no aplica porque no quedó otro animal en casa, dedícale esos
  siete días a la semana que más te pesó.</p>
</div>

<div class="box left-terra">
  <p class="lbl">No empieces el mismo día</p>
  <p>Si la pérdida ha sido hace menos de cuarenta y ocho horas, no empieces todavía.
  Los primeros dos días no son para hacer nada: son para dejar pasar el golpe.
  Vuelve el tercero.</p>
</div>

<p class="note">Este plan es general y complementario. Cualquier indicación de tu
psicólogo o de tu veterinario tiene siempre prioridad sobre lo que leas aquí.</p>
'''

WEEKS = [
 ("Los primeros siete días",
  "Sobrevivir. Nada más. Comer, beber, dormir lo que salga y no tomar ninguna decisión.",
  [("L","Escribe en un papel «esta semana no decido nada» y pégalo en la nevera. Ni ropa, ni cama, ni juguetes."),
   ("M","Come algo caliente aunque no tengas hambre, y bebe agua a lo largo del día. Es literal, no metafórico."),
   ("X","Avisa a una sola persona. Un mensaje basta: «se ha ido; no quiero hablar todavía, solo que lo sepas»."),
   ("J","Deja sus cosas exactamente donde están. Hoy no se toca nada de él, de ella."),
   ("V","Anclaje 4-6 dos veces, mañana y noche (ejercicio 1 del eBook). Primera noche del Diario del Oleaje."),
   ("S","Sal a la calle diez minutos. No a pasear ni a hacer recados: solo a que te dé el aire."),
   ("D","Revisión — ¿qué has conseguido comer, beber y dormir esta semana? Sin juicio, solo el dato.")],
  "Si no puedes con la tarea del día, pásala al siguiente sin culpa. En la primera semana, "
  "haber llegado al domingo ya es haber hecho el trabajo completo."),

 ("Nombrar y escribir",
  "Sacar el dolor de la cabeza y ponerlo en papel — es lo que permite que deje de dar vueltas.",
  [("L","A partir de hoy, tres minutos de Diario del Oleaje cada noche. Sin fallar y sin explicarte."),
   ("M","Escribe la carta que nunca le enviaste (ejercicio 2). A mano, veinte minutos, sin corregir ni releer."),
   ("X","Decide qué haces con esa carta: guardarla, quemarla, enterrarla, dejarla junto a su urna. Cúmplelo hoy."),
   ("J","Nombra en voz alta la emoción del día con una palabra exacta. «Mal» no vale: rabia, vacío, injusticia, alivio."),
   ("V","Pon música que asocies a él o a ella. Diez minutos sentada, sentado. Deja que llegue lo que llegue."),
   ("S","Elige tres fotos suyas. Solo tres. Guárdalas en una carpeta del móvil con su nombre."),
   ("D","Revisión — ¿qué palabra se ha repetido más esta semana?")],
  "La escritura expresiva estudiada por James Pennebaker muestra efectos medibles con una sola "
  "sesión de veinte minutos. No tiene que estar bien escrita. Solo tiene que salir."),

 ("La culpa, de frente",
  "Sacar la culpa del bucle mental. Lo que se escribe y se mira deja de repetirse solo.",
  [("L","Escribe tu frase de culpa exacta, tal cual suena por dentro, en una hoja aparte. Una sola vez."),
   ("M","Al lado, escribe únicamente los datos que tenías aquel día. No los de ahora. Solo los de entonces."),
   ("X","Ejercicio de la silla vacía (ejercicio 5): pregúntale si tomaste la decisión correcta y escucha la respuesta."),
   ("J","Si hubo eutanasia, escribe qué sufrimiento concreto le ahorraste. Sé específica, específico."),
   ("V","Si te quedaron preguntas médicas sin responder, llama a tu veterinario y hazlas. Todas."),
   ("S","Lee tu frase de culpa en voz alta. Después vuelve a leerla como si la dijera alguien a quien quieres."),
   ("D","Revisión — ¿la culpa sigue del mismo tamaño que el lunes?")],
  "La culpa del duelo casi nunca es un juicio sobre lo que hiciste: es el intento del cerebro de "
  "recuperar control sobre algo que nunca lo tuvo. Decidir por amor no es lo mismo que fallar."),

 ("Quién sostiene y quién no",
  "Construir tu círculo seguro y usarlo de verdad, en vez de aguantar sola, solo.",
  [("L","Dibuja los tres círculos del ejercicio 4 con nombres reales. Sin ser amable: honesta, honesto."),
   ("M","Habla de él o de ella con alguien del círculo del medio. Media hora, sin resumir."),
   ("X","Prepara tu frase para cuando alguien minimice: «para mí no era 'solo'. Era familia». Apréndetela."),
   ("J","Busca un grupo o foro de duelo animal. Hoy solo léelo. No tienes que escribir nada."),
   ("V","Di que no a un plan que hoy no puedes sostener. Sin explicaciones, sin disculparte de más."),
   ("S","Pide algo concreto a una persona: que te acompañe a un sitio, que te traiga comida, que te llame."),
   ("D","Revisión — ¿quién ha sostenido esta semana y quién no? Ajusta tus círculos.")],
  "El apoyo social es uno de los factores que mejor predicen la integración del duelo. Pero el apoyo "
  "malo — el que minimiza o compara — hace más daño que la soledad. Filtrar no es rencor: es cuidarte."),

 ("Su lugar en casa",
  "Darle un sitio concreto. Un lugar al que ir cuando la ausencia no cabe en ninguna parte.",
  [("L","Elige el sitio exacto de la casa donde va a estar su rincón. Que lo veas a diario, no escondido."),
   ("M","Reúne los objetos: una foto tuya con él o ella, su collar, un juguete, algo que recogisteis en un paseo."),
   ("X","Si tienes sus cenizas, decide dónde reposan y en qué. Mereces que te guste mirarlo."),
   ("J","Prepara la caja de la memoria: fotos, su chapa, un mechón de pelo, la huella si la tienes, dibujos."),
   ("V","El ritual del primer día (ejercicio 11): música suave, colocar cada cosa despacio, encender la vela, hablarle."),
   ("S","Enséñaselo a alguien que también la quería. Contadle una historia suya en voz alta."),
   ("D","Revisión — ¿qué sientes al pasar por delante de ese rincón?")],
  "Los rituales convierten algo abstracto — la muerte — en algo concreto y manejable. Por eso todas "
  "las culturas humanas los han inventado, siempre, en todas partes."),

 ("Recoger su herencia",
  "Nombrar qué te dio. No para consolarte: para que no se vaya con él, con ella.",
  [("L","Abre un cuaderno y escribe arriba «lo que me enseñó». Apunta la primera cosa."),
   ("M","La segunda. Puede ser diminuta: alegrarse cuando alguien vuelve a casa, por ejemplo."),
   ("X","La tercera. Y hoy, aplícala. Literalmente, hazla en algún momento del día."),
   ("J","La cuarta. Escribe también dónde y cuándo la aprendiste."),
   ("V","La quinta. Pregunta a alguien de casa qué le enseñó a él o a ella. Anótalo también."),
   ("S","La sexta y la séptima. Léelas todas seguidas, en voz alta."),
   ("D","Revisión — ¿cuál de las siete te llevas al mes que viene?")],
  "Los estudios sobre construcción de sentido en duelo muestran que quienes logran nombrar qué les "
  "aportó el vínculo integran mejor la pérdida. No es pensar en positivo: es reconstruir la historia."),

 ("Quien se queda",
  "Acompañar a la otra mascota de la casa — o a ti, si quien se quedó solo eres tú.",
  [("L","Observa a tu otra mascota diez minutos sin intervenir. Anota qué hace, dónde se pone, a quién busca."),
   ("M","Fija horarios exactos de comida, paseo y sueño, y no los muevas. La previsibilidad baja el cortisol."),
   ("X","Déjale oler la manta o el collar del que se fue. No retires todavía su sitio."),
   ("J","Quince minutos exclusivos: solo ella y tú, sin móvil. Cepillado, caricias o presencia en silencio."),
   ("V","Alarga el paseo diez minutos, o añade un juego corto de olfato en casa."),
   ("S","Comprueba lo básico: ¿come, bebe, duerme, juega? Anota sí o no, sin interpretar."),
   ("D","Revisión — ¿mejor, igual o peor que el lunes?")],
  "Si a las tres o cuatro semanas sigue sin comer, no juega o se aísla por completo, consulta al "
  "veterinario. El cuarto libro de la serie tiene el protocolo completo, día a día."),

 ("Integrar, que no es olvidar",
  "Mirar las ocho semanas enteras y decidir qué necesitas tú a partir de aquí.",
  [("L","Relee el Diario del Oleaje desde la primera noche. Entero, sin saltarte nada."),
   ("M","Escribe qué ha cambiado, aunque sea poco. Y qué sigue exactamente igual."),
   ("X","Haz una cosa que dejaste de hacer cuando se fue. Una sola. La que menos te cueste."),
   ("J","Marca en el calendario las fechas difíciles del año que viene (usa la página siguiente)."),
   ("V","Decide si hoy quieres plantearte adoptar. «Todavía no» y «nunca más» son respuestas completas."),
   ("S","Si la idea te ronda, haz el ejercicio 12: pídele permiso, aunque sepas que no lo necesitas."),
   ("D","Revisión — ¿qué necesitas tú, tú y no él, para el mes que viene?")],
  "Reír no es traicionarlo. Integrar no es olvidar: es que su recuerdo deje de partirte "
  "y empiece a abrigarte. Tarda lo que tarda, y no hay calendario correcto."),
]

def week_page(i, title, goal, tasks, tip):
    rows = ''.join(
        '<tr><td class="day">%s</td><td>%s</td><td class="tick"><span class="chk"></span></td></tr>'
        % (d, t) for d, t in tasks)
    return '''
<div class="wk-head">
  <div class="wk-num terra">%02d</div>
  <div class="txt"><p class="eyebrow terra">Semana %d</p><h1 class="title">%s</h1></div>
</div>

<div class="box green">
  <p class="lbl">Objetivo de la semana</p>
  <p>%s</p>
</div>

<table>
  <thead class="terra"><tr><th style="width:22pt">Día</th><th>Tarea del día</th>
  <th class="tick">&#10003;</th></tr></thead>
  <tbody>%s</tbody>
</table>

<div class="dashed">
  <p style="font-size:8.6pt;line-height:1.6;margin:0">
  <b style="color:#a8502e">Consejo:</b> %s</p>
</div>
''' % (i, i, title, goal, rows, tip)

p12 = '''
<p class="eyebrow">Después de las ocho semanas</p>
<h1 class="title">El calendario de las fechas difíciles</h1>
<p class="lead">El duelo no acaba en la semana ocho. Vuelve en fechas concretas —
y una fecha que ves venir duele menos que una que te asalta.</p>

<p>Anticiparlas no es regodearse: es quitarles el factor sorpresa. Escribe cada
fecha y, al lado, qué vas a hacer ese día. Algo concreto y pequeño: encender su
vela, ir al sitio donde paseabais, mirar sus fotos con alguien, cocinar algo que
te guste.</p>

<table>
  <thead><tr><th style="width:74pt">Fecha</th><th style="width:120pt">Qué representa</th>
  <th>Qué voy a hacer ese día</th></tr></thead>
  <tbody>
  %s
  </tbody>
</table>

<div class="box left-green">
  <p class="lbl">Las que casi siempre duelen</p>
  <p>El día que llegó a casa · su cumpleaños o el día que lo celebrabais ·
  el aniversario de su marcha · la primera Navidad · el primer viaje sin él ·
  el cambio de estación en el que salíais más · el día que caduca su chip o
  llega el recordatorio de la vacuna.</p>
</div>

<p class="note">El recordatorio automático del veterinario es uno de los golpes más
duros y más comunes. Llama y pide que lo retiren, antes de que llegue.</p>
''' % ''.join('<tr><td class="blank"></td><td></td><td></td></tr>' for _ in range(7))

p13 = '''
<p class="eyebrow terra">Cuando hace falta más</p>
<h1 class="title">Cuándo pedir ayuda profesional</h1>
<p class="lead">Pedir ayuda no significa que lo estés haciendo mal. Significa que
esto es demasiado grande para atravesarlo sola, solo — y casi siempre lo es.</p>

<h3 class="sub">Señales para buscar apoyo ahora, sin esperar</h3>
<ul class="clean terra">
  <li>Aparece la idea de no querer seguir aquí, aunque sea de forma vaga o pasajera.</li>
  <li>Llevas semanas sin comer o sin dormir de forma sostenida.</li>
  <li>Has dejado de ir al trabajo, de salir o de contestar a nadie.</li>
  <li>Estás usando alcohol o pastillas para no sentir.</li>
  <li>La culpa se ha convertido en un castigo diario que no puedes parar.</li>
</ul>

<h3 class="sub">Señales para buscarlo pasados unos meses</h3>
<ul class="clean">
  <li>A los seis meses el dolor sigue igual de intenso que la primera semana, sin ninguna variación.</li>
  <li>No puedes hablar de él o de ella, ni ver una foto, ni entrar en una habitación.</li>
  <li>O al contrario: no puedes hacer nada que no sea pensar en la pérdida.</li>
  <li>Has dejado sus cosas exactamente igual durante meses y no puedes ni mirarlas.</li>
  <li>Sientes que tu vida se detuvo el día que se fue y no ha vuelto a arrancar.</li>
</ul>

<div class="box green">
  <p class="lbl">Qué esperar de una terapia de duelo</p>
  <p>No suele ser un proceso largo. Muchas personas necesitan tres, cuatro o seis
  sesiones para atravesar el momento más duro. Busca, si puedes, a alguien con
  experiencia en duelo — cada vez hay más profesionales que trabajan
  específicamente el duelo por animales, porque cada vez se reconoce más.</p>
</div>

<p class="note">Que tu entorno no entienda tu dolor no lo hace más pequeño. Que
necesites ayuda para sostenerlo no te hace más débil. Cuidarte es exactamente lo
que harías por él, por ella, sin dudarlo un segundo.</p>
'''

p14 = '''
<p class="eyebrow">Para cerrar</p>
<h1 class="title">Ocho semanas después</h1>

<p>Has hecho cincuenta y seis cosas pequeñas en un tiempo en el que ni siquiera
podías decidir qué desayunar. Eso no es poco: eso es exactamente cómo se atraviesa
un duelo, con gestos diminutos repetidos muchos días.</p>

<p>Es probable que sigas doliendo. Es probable que haya semanas que no pudiste
completar. Nada de eso es un fallo del plan ni tuyo. El objetivo nunca fue llegar
a la semana ocho sin dolor: fue llegar a la semana ocho acompañada, acompañado,
y con algo hecho cada día.</p>

<div class="quote">Lo que aprendiste queriéndole<br>—estar presente, alegrarte de lo pequeño,<br>
querer sin medida—<br>es justo lo que ahora te toca<br>aplicarte a ti.</div>

<hr class="rule soft">

<h2 class="sec">Si quieres repetirlo</h2>
<p>Este plan se puede volver a hacer. Muchas personas repiten las semanas que peor
llevaron — la de la culpa, la de los demás — meses después, cuando tienen más
fuerzas para mirarlas de frente. Otras lo retoman entero al llegar el primer
aniversario. Las dos cosas están bien.</p>

<div class="dashed">
  <p class="lbl">Lo que me llevo de estas ocho semanas</p>
  <div class="write dot"></div>
  <div class="write dot"></div>
  <div class="write dot"></div>
</div>

<p class="note" style="text-align:center;margin-top:14pt">
Sigue Contigo — Libro 3 de 4 · Plan Práctico de 8 Semanas<br>tremdora</p>
'''

pages = [page(cover, cls='cover'), page(p2, 2), page(p3, 3)]
for i, (t, g, tk, tip) in enumerate(WEEKS, start=1):
    pages.append(page(week_page(i, t, g, tk, tip), 3 + i))
pages += [page(p12, 12), page(p13, 13), page(p14, 14)]

html = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<title>Sigue Contigo — Plan Práctico de 8 Semanas</title><style>%s</style>'
        '</head><body>%s</body></html>') % (CSS, ''.join(pages))
open(D + '/libro3-plan-8-semanas.html', 'w', encoding='utf-8').write(html)
print('escrito libro3', len(pages), 'páginas')
