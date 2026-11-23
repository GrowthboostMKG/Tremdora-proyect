# Genera libros/30-dias-contigo.html (Libro 3 de 4 de la colección «Sigue contigo»).
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

SEMANAS = {
 1: ("Sostenerte", "Los primeros días no se trata de hacer, sino de aguantar con cuidado. Estos gestos son pequeños a propósito: están pensados para cuando casi no tienes fuerzas."),
 8: ("Sentir y decir", "Ahora toca dejar salir lo que llevas dentro. Esta semana vas a ponerle palabras al dolor, a la culpa y al amor. Llorar forma parte del camino."),
 15: ("Recordar y honrar", "El recuerdo empieza a ocupar el lugar de la herida. Esta semana vas a crear espacios, objetos y rituales para que su memoria tenga un sitio bonito."),
 22: ("Seguir caminando", "No se trata de olvidar ni de «pasar página», sino de aprender a llevarla contigo. Estos últimos días miran hacia delante, con ella dentro."),
}

DIAS = [
 ("Respira", "Siéntate o túmbate. Pon una mano en el pecho y otra en el vientre. Inspira contando hasta 4 y espira contando hasta 6. Repítelo diez veces mientras te dices: «Esto duele, y voy a sobrevivir a ello».",
  "La respiración lenta calma el sistema nervioso en pocos minutos. Es el ejercicio 1 de <em>Sigue contigo</em>; puedes repetirlo cada vez que llegue una ola fuerte."),
 ("Algo caliente y sencillo", "Hoy, tu único objetivo es comer algo caliente y beber agua. Una sopa, una tostada, una infusión. No hace falta más.",
  "El duelo altera el apetito y el descanso. Cuidar lo básico es la base para poder sostener todo lo demás."),
 ("Dilo en voz alta", "Llama o escribe a una persona de confianza y dile, con estas palabras o con las tuyas: «La echo mucho de menos. Hoy estoy mal».",
  "Nombrar el dolor delante de alguien que lo sostiene alivia la soledad del duelo. Elige a alguien de tu círculo seguro."),
 ("No decidas nada todavía", "Deja sus cosas donde están: su cama, su cuenco, su manta. No regales ni tires nada estos días. Ya habrá tiempo.",
  "En la fase de shock, las decisiones importantes suelen tomarse en piloto automático, y luego pesan. Esperar es protegerte."),
 ("Diez minutos de luz", "Sal a la calle, al balcón o junto a una ventana abierta durante diez minutos. Mira el cielo. No tienes que hacer nada más.",
  "La luz natural ayuda a regular el sueño y el ánimo, que el duelo suele desordenar."),
 ("Tu primera frase", "Antes de dormir, escribe: «Hoy he sentido ____ y mi cuerpo ha estado ____». Si tienes el <em>Diario del Oleaje</em>, este es el día de empezarlo.",
  "Poner palabras a las emociones reduce su intensidad. Una sola frase basta."),
 ("Pide una cosa concreta", "Piensa en algo práctico que te cueste hacer ahora mismo (la compra, una gestión, cocinar) y pídeselo a alguien. Con nombre y fecha.",
  "Mucha gente quiere ayudar y no sabe cómo. Una petición concreta les da la oportunidad y a ti te quita un peso."),
 ("La carta que nunca le enviaste", "Coge papel y bolígrafo y escríbele una carta. Empieza con «Querida [su nombre]» y déjate llevar: lo que no le dijiste, lo que te dio, lo que te duele.",
  "La escritura expresiva ayuda a ordenar lo que sientes. Es el ejercicio 2 del libro. Puedes guardarla o dejarla junto a su urna."),
 ("Permiso para llorar", "Reserva quince minutos para mirar sus fotos o escuchar una canción que te recuerde a ella. Si llegan las lágrimas, déjalas salir sin pedir perdón.",
  "Darle al dolor un tiempo y un lugar evita que aparezca de golpe en cualquier momento. Lo que no se siente no se cura."),
 ("Responde a tu culpa", "Escribe la frase que más te repites («Debí darme cuenta antes», «Esperé demasiado»). Debajo, escribe lo que le dirías a una amiga que te dijera exactamente eso.",
  "La culpa es un síntoma del duelo, no una verdad sobre lo que hiciste. Hablarte con ternura cambia la forma en que la vives."),
 ("Prepara tu respuesta", "Escribe una frase corta para cuando alguien te diga «era solo un animal». Por ejemplo: «Para mí no era “solo”. Era familia». Apréndetela.",
  "Tener la respuesta preparada te protege y te ahorra energía. También puedes elegir no responder: es igual de válido."),
 ("Mueve el cuerpo", "Da un paseo suave de veinte minutos, sin prisa y sin objetivo. Si puedes, por un sitio que te guste.",
  "El movimiento ayuda a descargar la tensión que el duelo acumula en el cuerpo y mejora el descanso."),
 ("Su objeto puente", "Elige un objeto suyo —su collar, su manta, su juguete— y colócalo en un lugar visible pero protegido. Cógelo cuando necesites sentirla cerca.",
  "Los objetos de vínculo ayudan a mantener la conexión emocional sin necesidad de su presencia. Es el ejercicio 8 del libro."),
 ("Mira tu semana con cariño", "Repasa estos siete días. No para evaluarte, sino para reconocer lo que has atravesado. Escribe una cosa que hayas hecho bien.",
  "Reconocer tu esfuerzo te ayuda a seguir. Has sobrevivido a días muy difíciles."),
 ("Empieza la caja de la memoria", "Busca una caja bonita y guarda en ella lo primero que quieras conservar: una foto, su placa, un mechón de pelo. La irás llenando poco a poco.",
  "Un espacio delimitado para el recuerdo evita que el duelo invada toda la casa y te permite volver a él cuando tú elijas. Es el ejercicio 9."),
 ("Cinco fotos", "Elige tus cinco fotos favoritas con ella e imprímelas. Una para la caja, otra para su rincón y las demás donde tú quieras.",
  "Tener sus fotos en papel convierte el recuerdo en algo que puedes tocar y compartir."),
 ("Lo que me enseñó", "Escribe una sola cosa que aprendiste a su lado. Puede ser diminuta: «Me enseñó que un rato al sol lo arregla casi todo».",
  "Encontrar significado en la pérdida es uno de los factores que más ayudan a integrarla. Es el ejercicio 6 del libro."),
 ("Una anécdota divertida", "Cuéntale a alguien una historia graciosa de ella: una travesura, una manía, algo que siempre os hacía reír.",
  "Recordar con alegría también es honrarla. La risa y la tristeza pueden convivir."),
 ("El paseo simbólico", "Si era un perro, haz vuestro paseo de siempre y, al terminar, di: «Gracias por todos los paseos». Si era un gato, recorre la casa por sus rincones favoritos y despídete en cada uno.",
  "Los rituales de transición ayudan a cerrar etapas de una manera que el simple pensamiento no consigue. Es el ejercicio 7."),
 ("Su rincón", "Crea un pequeño espacio para ella: su urna o una foto, una vela, una planta y algo suyo. Cuando termines, di en voz alta: «Aquí te quedas. Aquí estás conmigo».",
  "Necesitamos lugares físicos donde dirigir el amor que ya no tiene destinatario. Es el ejercicio 11 del libro."),
 ("Una página de su historia", "Abre <em>Su historia</em> y completa una página: cómo llegó a tu vida, sus manías o su comida favorita. Sin prisa.",
  "Escribir su historia la convierte en algo que perdura y que podrás enseñar a otras personas."),
 ("Sus cosas, con calma", "Si te sientes con fuerzas, decide qué hacer con alguna de sus cosas: guardarla, regalarla o donar mantas y comida a una protectora. Si no estás preparada o preparado, déjalo para otro día.",
  "Dar un destino a sus cosas, cuando llega el momento, puede convertir el dolor en un gesto de amor hacia otros animales."),
 ("Respiración del cariño", "Cierra los ojos e imagínala. Al inspirar, di mentalmente: «Gracias por haber estado». Al espirar: «Te llevo conmigo». Cinco minutos.",
  "Combinar respiración y afecto ayuda a asociar su recuerdo con el cariño y no solo con la pérdida. Es el ejercicio 10."),
 ("Un rato para ti", "Haz algo que te guste durante una hora: leer, cocinar, quedar con alguien, ver una película. Si aparece la culpa, recuérdate que reír no es traicionarla.",
  "Permitirte momentos buenos es parte de la integración. Ella no querría que dejaras de vivir."),
 ("Si hay niños en casa", "Leed juntos el cuento <em>Cuando un amigo se va</em> o haced un dibujo de ella entre todos. Si no hay niños, escribe a alguien que también la quería y compartid un recuerdo.",
  "Compartir el duelo lo hace más llevadero y enseña a los más pequeños que el dolor se puede atravesar acompañados."),
 ("Si hay otra mascota", "Dedica quince minutos solo a ella: cepillarla, jugar suave o simplemente estar a su lado. Si no hay otra mascota, cuida algo vivo: riega una planta o siembra una semilla.",
  "El contacto tranquilo con un animal libera oxitocina en los dos. Es el ejercicio 15 del libro."),
 ("Un gesto en su nombre", "Haz algo bueno en su memoria: una donación a una protectora, una tarde de voluntariado, plantar una flor o compartir su historia.",
  "Convertir el amor en acción da sentido a la pérdida y mantiene vivo su legado."),
 ("Las fechas difíciles", "Apunta en tu calendario su cumpleaños, el aniversario de su llegada y el de su despedida. Junto a cada fecha, escribe un pequeño plan para cuidarte ese día.",
  "Las fechas señaladas suelen traer olas fuertes. Anticiparlas te ayuda a vivirlas con más calma."),
 ("Mira hacia atrás", "Relee tus notas de estos 28 días o tu <em>Diario del Oleaje</em>. Fíjate en cómo han cambiado tus palabras.",
  "Ver el camino recorrido por escrito muestra que algo se ha ido moviendo, aunque no lo notaras día a día."),
 ("Lo que ella te diría", "Imagina que pudiera escribirte una carta. Escríbela tú, con su voz: lo que te agradecería, lo que querría para ti a partir de ahora.",
  "Darle voz a quien se fue ayuda a cerrar el círculo y a llevarse su amor hacia delante. Sigue contigo."),
]

def dia_html(n, titulo, texto, por_que):
    sem = ""
    if n in SEMANAS:
        t, s = SEMANAS[n]
        idx = list(SEMANAS).index(n) + 1
        sem = f'''<section class="chapter"{' data-mark="p-d1"' if n == 1 else ''}><div class="center-page">
  <div class="kicker" style="margin-top:0">Semana {idx}</div><h1 class="ch">{t}</h1><div class="orn">——— · ———</div>
  <p class="sub" style="max-width:110mm;margin:0 auto">{s}</p>
  <p class="serie">Días {n} a {min(n+6 if n<22 else 30, 30)}</p></div></section>'''
    return sem + f'''
<section class="chapter">
  <div class="big-n">{n}</div>
  <h1 class="ch" style="text-align:left;margin-top:.1em">{titulo}</h1>
  <div class="orn" style="text-align:left;margin:.5em 0 .9em">——— · ———</div>
  <p>{texto}</p>
  <p class="note" style="text-align:left;margin:1em 0">{por_que}</p>
  <div class="check">Hoy lo he hecho</div>
  <div class="q"><div class="prompt">Cómo me he sentido</div><div class="lines l4"></div></div>
  <div class="q"><div class="prompt">Algo de ella que hoy quiero recordar</div><div class="lines l3"></div></div>
</section>'''

dias = "".join(dia_html(i, *d) for i, d in enumerate(DIAS, 1))

html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>30 días contigo · Tremdora</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
{{{{CSS}}}}
<style>:root{{--accent:#b5655a;}} .big-n{{text-align:left}}</style>
</head><body>
{{{{DEFS}}}}

<section class="page"><div class="halftitle">
  <div class="brand">Tremdora</div><div class="orn">——— · ———</div>
  <h1>30 días<br>contigo</h1><div class="orn">——— · ———</div>
  <div class="tag">Un pequeño gesto cada día</div>
  <div class="tag2">Colección Sigue contigo · Libro 3 de 4</div>
</div></section>

<section class="page"><div class="legal">
  <p><strong>30 días contigo</strong><br>Un pequeño gesto cada día · Colección Sigue contigo, libro 3 de 4</p>
  <p>© 2026 Tremdora. Todos los derechos reservados.<br>Se permite imprimir este cuaderno para uso personal de quien lo ha adquirido. Queda prohibida su reproducción, distribución o comunicación pública sin autorización previa y por escrito de Tremdora.</p>
  <p>Este cuaderno es una herramienta de acompañamiento con fines divulgativos. No sustituye la atención de profesionales de la psicología o la medicina. Si tu malestar es muy intenso o se prolonga en el tiempo, busca ayuda profesional.</p>
  <p>Primera edición: 2026</p>
</div></section>

<section class="chapter">
  <div class="kicker">Antes de empezar</div>
  <h1 class="ch">Un paso cada día</h1>
  <div class="orn">——— · ———</div>
  <p>Cuando alguien a quien quieres se va, a veces lo más difícil es saber qué hacer con el día. Las horas se hacen largas, la casa está demasiado silenciosa y las fuerzas no llegan para grandes cosas.</p>
  <p>Por eso este cuaderno no te pide grandes cosas. Te propone un gesto pequeño cada día, durante treinta días. Algunos son tan sencillos como respirar o comer algo caliente. Otros te invitan a escribir, a recordar o a crear un lugar bonito para ella.</p>
  <p>Muchos de estos gestos son los ejercicios de <em>Sigue contigo</em>, ordenados para que no tengas que pensar por dónde empezar.</p>
  <p class="quote">No tienes que superarlo en 30 días.<br>Solo tienes que dar el paso de hoy.</p>
  <p class="sign">Con todo el cariño,<br>el equipo de Tremdora</p>
</section>

<section class="chapter">
  <div class="kicker">Cómo usar este cuaderno</div>
  <h1 class="ch">Tu ritmo manda</h1>
  <div class="orn">——— · ———</div>
  <h3>Un día, un gesto</h3>
  <p>Cada página tiene un gesto, una breve explicación de por qué ayuda y un espacio para anotar cómo te has sentido. Lee la página por la mañana y haz el gesto cuando puedas.</p>
  <h3>Cuatro semanas, cuatro etapas</h3>
  <p>Los días están agrupados en cuatro semanas: <em>sostenerte</em>, <em>sentir y decir</em>, <em>recordar y honrar</em> y <em>seguir caminando</em>. Siguen el orden natural del duelo, aunque cada persona lo vive a su manera.</p>
  <h3>Sin exigencias</h3>
  <p>Si un día no puedes, no pasa nada. Repite el gesto anterior, salta al siguiente o deja el cuaderno unos días. No es una carrera ni un examen. Es un acompañamiento.</p>
  <p class="note">Si en algún momento sientes que el dolor te supera de una forma que te asusta, busca ayuda profesional. Al final del cuaderno encontrarás recursos.</p>
</section>

{dias}

<section class="chapter" data-mark="p-fin">
  <div class="kicker">Treinta días después</div>
  <h1 class="ch">¿Y ahora?</h1>
  <div class="orn">——— · ———</div>
  <p>Quizá el dolor sigue ahí, y es normal: el duelo no tiene fecha de caducidad. Pero has dado treinta pasos. Has respirado, has escrito, has llorado, has recordado y le has dado a su amor un lugar bonito.</p>
  <p>Quédate con los gestos que más te han ayudado y vuelve a ellos cuando lo necesites, sobre todo en las fechas difíciles.</p>
  <div class="q"><div class="prompt">Los tres gestos que quiero conservar</div><div class="lines l3"></div></div>
  <p class="note" style="text-align:left">Si sigues sintiendo que no puedes funcionar, habla con un profesional. Si te vienen pensamientos de hacerte daño, pide ayuda de inmediato: en España, 024 (24 horas) o 112; en otros países, los servicios de emergencia locales.</p>
  <p class="sign">Con todo el cariño,<br>Tremdora<br><span style="color:var(--accent)">Ellos se merecen lo mejor.</span></p>
</section>
</body></html>'''
(ROOT / 'libros' / '30-dias-contigo.html').write_text(html)
print('ok', len(DIAS))
