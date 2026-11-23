# Genera libros/diario-oleaje.html (Libro 2 de 4 de la colección «Sigue contigo»).
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

SEMANAS = [
 ("El golpe", "Los primeros días todo parece irreal",
  "Puede que funciones en piloto automático, que no llores o que llores sin parar. Las dos cosas son normales. Esta semana no tienes que hacer nada más que respirar, comer algo sencillo y escribir tu frase cada noche. Nada más.",
  ["¿Qué ha sido lo más difícil de esta semana?", "¿Quién o qué me ha sostenido estos días?"]),
 ("Lo que duele", "Permitirte sentir",
  "Ahora el dolor se nota de verdad. Aparece en momentos concretos: al llegar a casa, a la hora del paseo, al ver su cuenco. No huyas de él. Lo que no se siente no se cura, y ponerle nombre ya es empezar a sostenerlo.",
  ["¿En qué momento del día la echo más de menos?", "¿Qué me gustaría decirle hoy?"]),
 ("La culpa", "Una mentira que tu cerebro te cuenta",
  "«¿Esperé demasiado?», «¿Debí darme cuenta antes?». La culpa es un síntoma del duelo, no una verdad sobre lo que hiciste. Esta semana vas a mirarla de frente, con la misma ternura con la que mirarías a una amiga.",
  ["¿De qué me estoy culpando?", "Si una amiga me contara exactamente esto, ¿qué le diría yo?"]),
 ("Lo que me dio", "Volver a los buenos recuerdos",
  "El dolor es tan grande porque el amor fue enorme. Esta semana vas a dejar que vuelvan los recuerdos alegres: sus manías, sus travesuras, la forma en que te esperaba. Llorar y sonreír a la vez también está permitido.",
  ["Tres recuerdos que me hacen sonreír", "Algo que me enseñó y quiero conservar"]),
 ("Mi cuerpo también recuerda", "Cuidarte como la cuidabas a ella",
  "El duelo cansa: altera el sueño, el apetito y las defensas. Esta semana presta atención a tu cuerpo. Bebe agua, sal a que te dé la luz, muévete un poco. No es egoísmo: es lo que ella querría para ti.",
  ["¿Qué necesita hoy mi cuerpo?", "Un pequeño gesto de cuidado que me he regalado esta semana"]),
 ("Los días buenos", "Reír no es traicionarla",
  "Quizá empiecen a aparecer ratos de calma o incluso de alegría, y con ellos, la culpa por sentirlos. Recuerda: lo que aprendiste a su lado —alegrarte por las cosas pequeñas— es justo lo que ahora puedes aplicar a tu vida.",
  ["¿Qué me ha hecho sentir bien esta semana?", "¿Cómo puedo honrarla viviendo, no solo recordando?"]),
 ("Su lugar", "Darle un sitio al amor",
  "Necesitamos lugares donde dirigir el amor que ya no tiene destinatario. Esta semana piensa en su rincón: una foto, una vela, su collar, su urna. Un sitio bonito donde puedas visitarla cuando lo necesites.",
  ["¿Cómo es (o cómo será) su rincón?", "¿Qué ritual quiero mantener para recordarla?"]),
 ("Lo que me llevo", "Del dolor al recuerdo",
  "Ocho semanas después, el oleaje sigue ahí, pero quizá ya no te arrastra igual. No se trata de olvidarla ni de «superarlo», sino de llevarla contigo de una forma nueva. Esta semana mira hacia atrás y reconoce el camino que has hecho.",
  ["¿Qué ha cambiado en mí desde la primera semana?", "Lo que quiero llevarme de ella para siempre"]),
]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def dia(nombre):
    olas = "".join(f'<span class="c">{n}</span>' for n in range(1, 11))
    return f'''<div class="day"><div class="h"><b>{nombre}</b><span>Fecha: ____ / ____</span></div>
  <div class="s">Hoy he sentido <i></i> y mi cuerpo ha estado <i></i>.</div>
  <div class="ola"><span>Ola de hoy</span>{olas}</div></div>'''

semanas_html = []
for i, (titulo, sub, texto, preguntas) in enumerate(SEMANAS, 1):
    roman = ["I","II","III","IV","V","VI","VII","VIII"][i-1]
    semanas_html.append(f'''
<section class="chapter"{' data-mark="p-s1"' if i == 1 else ''}>
  <div class="kicker">Semana {i}</div>
  <h1 class="ch">{titulo}</h1>
  <p class="sub">{sub}</p>
  <div class="orn">——— · ———</div>
  <p>{texto}</p>
  <div class="q"><div class="prompt">{preguntas[0]}</div><div class="lines l5"></div></div>
  <div class="q"><div class="prompt">{preguntas[1]}</div><div class="lines l5"></div></div>
</section>
<section class="chapter">
  <div class="tag">Semana {i} · Mi oleaje diario</div>
  {''.join(dia(d) for d in DIAS[:4])}
</section>
<section class="chapter">
  <div class="tag">Semana {i} · Mi oleaje diario</div>
  {''.join(dia(d) for d in DIAS[4:])}
  <div class="q"><div class="prompt">Mirando la semana: ¿cómo ha sido mi oleaje?</div><div class="lines l6"></div></div>
</section>''')

html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Diario del Oleaje · Tremdora</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
{{{{CSS}}}}
<style>:root{{--accent:#6f8a63;}}</style>
</head><body>
{{{{DEFS}}}}

<section class="page"><div class="halftitle">
  <div class="brand">Tremdora</div><div class="orn">——— · ———</div>
  <h1>Diario<br>del Oleaje</h1><div class="orn">——— · ———</div>
  <div class="tag">8 semanas de registro</div>
  <div class="tag2">Colección Sigue contigo · Libro 2 de 4</div>
</div></section>

<section class="page"><div class="legal">
  <p><strong>Diario del Oleaje</strong><br>8 semanas de registro · Colección Sigue contigo, libro 2 de 4</p>
  <p>© 2026 Tremdora. Todos los derechos reservados.<br>Se permite imprimir este diario para uso personal de quien lo ha adquirido. Queda prohibida su reproducción, distribución o comunicación pública sin autorización previa y por escrito de Tremdora.</p>
  <p>Este diario es una herramienta de acompañamiento con fines divulgativos. No sustituye la atención de profesionales de la psicología o la medicina. Si tu malestar es muy intenso o se prolonga en el tiempo, busca ayuda profesional.</p>
  <p>Primera edición: 2026</p>
</div></section>

<section class="chapter">
  <div class="kicker">Antes de empezar</div>
  <h1 class="ch">Una ola cada noche</h1>
  <div class="orn">——— · ———</div>
  <p>En <em>Sigue contigo</em> te contamos que el duelo no es una línea recta, sino un oleaje: vas y vienes, hay días en que crees que estás mejor y, al siguiente, vuelves al principio sin previo aviso.</p>
  <p>Este diario nace del ejercicio 3 de ese libro, <em>El diario del oleaje</em>, y lo convierte en un compañero para las próximas ocho semanas. No necesitas escribir mucho. No necesitas escribir bien. Solo necesitas una frase cada noche y un poco de honestidad contigo.</p>
  <p>Cuando lo termines, podrás releerlo y ver tu oleaje por escrito. Verás que no todos los días fueron iguales. Y verás cómo, sin que te dieras cuenta, algo se fue moviendo.</p>
  <p class="quote">No tienes que estar mejor.<br>Solo tienes que estar.</p>
  <p class="sign">Con todo el cariño,<br>el equipo de Tremdora</p>
</section>

<section class="chapter">
  <div class="kicker">Cómo usar este diario</div>
  <h1 class="ch">Tres gestos sencillos</h1>
  <div class="orn">——— · ———</div>
  <h3>1 · Cada noche, una frase</h3>
  <p>Antes de dormir, completa: <em>«Hoy he sentido ____ y mi cuerpo ha estado ____»</em>. Solo eso. No tienes que explicarte ni justificarte.</p>
  <h3>2 · Marca tu ola</h3>
  <p>Rodea un número del 1 al 10 según la intensidad del dolor ese día: 1 es un mar en calma y 10, una ola que te arrastra. No hay respuestas correctas, solo la tuya.</p>
  <h3>3 · Una pausa cada semana</h3>
  <p>Cada semana empieza con un tema y dos preguntas para escribir con calma, y termina con una mirada a los siete días. Hazlo cuando puedas, aunque sea con retraso.</p>
  <p class="note">Si un día no escribes, no pasa nada. Retoma al día siguiente. Este diario no es un examen: es un lugar para ti.</p>
</section>

<section class="chapter">
  <div class="kicker">Mi punto de partida</div>
  <h1 class="ch">Hoy empiezo</h1>
  <div class="orn">——— · ———</div>
  <div class="fill"><span>Su nombre:</span><i></i></div>
  <div class="fill"><span>Me acompañó durante</span><i></i><span>años.</span></div>
  <div class="fill"><span>Fecha en que se fue:</span><i></i></div>
  <div class="fill"><span>Fecha en que empiezo este diario:</span><i></i></div>
  <div class="q"><div class="prompt">Así me siento hoy</div><div class="lines l4"></div></div>
  <div class="q"><div class="prompt">Lo que más necesito en estas semanas</div><div class="lines l3"></div></div>
  <div class="q"><div class="prompt">Mi ola de hoy, del 1 al 10</div>
  <div class="ola" style="justify-content:center;gap:3mm;margin-top:.6em">{"".join(f'<span class="c">{n}</span>' for n in range(1, 11))}</div></div>
</section>

{"".join(semanas_html)}

<section class="chapter" data-mark="p-fin">
  <div class="kicker">Ocho semanas después</div>
  <h1 class="ch">Relee tu oleaje</h1>
  <div class="orn">——— · ———</div>
  <p>Vuelve a las páginas de cada semana. Calcula, a ojo, tu ola media de esos siete días y marca un punto en su columna. Después une los puntos. Lo que verás no será una línea recta, sino tu propio mar.</p>
  <table class="chart">
    {"".join(f'<tr><td class="lab">{n}</td>' + '<td></td>'*8 + '</tr>' for n in range(10, 0, -1))}
    <tr class="weeks"><td class="lab"></td>{"".join(f'<td>Sem. {i}</td>' for i in range(1, 9))}</tr>
  </table>
  <p class="note">Si la línea sube y baja, es normal: así es el duelo. Lo importante es que estás aquí, ocho semanas después, todavía caminando.</p>
</section>

<section class="chapter">
  <div class="kicker">Para cerrar</div>
  <h1 class="ch">Carta a mí</h1>
  <p class="sub">Escríbete como le escribirías a alguien a quien quieres mucho</p>
  <div class="orn">——— · ———</div>
  <div class="lines l16"></div>
</section>

<section class="chapter">
  <div class="kicker">Si el oleaje no baja</div>
  <h1 class="ch">Pedir ayuda también es cuidarte</h1>
  <div class="orn">——— · ———</div>
  <p>Si después de estas semanas sigues sintiendo que no puedes funcionar —no sales, no comes, no duermes o no le encuentras sentido a nada—, por favor, habla con un profesional. Hay psicólogos y psicólogas especializados en duelo por mascotas, y muchos atienden en línea.</p>
  <p>Si en algún momento te vienen pensamientos de hacerte daño, pide ayuda de inmediato.</p>
  <ul>
    <li><strong>España:</strong> 024, línea de atención a la conducta suicida (gratuita, confidencial y disponible las 24 horas). Emergencias: 112.</li>
    <li><strong>Otros países:</strong> contacta con el número de emergencias local o con los servicios de salud de tu zona.</li>
  </ul>
  <p class="sign">Con todo el cariño,<br>Tremdora<br><span style="color:var(--accent)">Ellos se merecen lo mejor.</span></p>
</section>
</body></html>'''
(ROOT / 'libros' / 'diario-oleaje.html').write_text(html)
print('ok')
