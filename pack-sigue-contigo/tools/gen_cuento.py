# Genera libros/cuento.html — «Cuando un amigo se va» (regalo de la colección «Sigue contigo»).
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

HISTORIA = [
 ("cuento_01", "Lucía y Canela eran las mejores amigas del mundo. Canela había llegado a casa antes que Lucía, así que siempre había estado ahí: en los desayunos, en los paseos y en las tardes de jugar en el jardín.",
  "Miso, el gato, las miraba desde el banco. Él también quería a Canela, aunque a su manera."),
 ("cuento_02", "Pero Canela se fue haciendo mayor. Su hocico se volvió blanco, caminaba muy despacito y dormía casi todo el día.",
  "Lucía se sentaba a su lado y le acariciaba la cabeza.<br>—Descansa, Canela —le susurraba—. Yo te cuido."),
 ("cuento_03", "Una tarde, mamá se sentó en la alfombra, le cogió las manos y le dijo la verdad:<br>—Lucía, Canela estaba muy enferma. Su cuerpo dejó de funcionar y ha muerto. Ya no va a volver.",
  "Lucía sintió un nudo muy grande en la garganta.<br>—Está bien estar triste —le dijo mamá—. Yo también lo estoy."),
 ("cuento_04", "Los días siguientes, la casa parecía muy grande y muy silenciosa. La camita de Canela estaba vacía.",
  "A veces Lucía estaba triste. A veces estaba enfadada. Y a veces no sabía muy bien lo que sentía. Miso también buscaba a Canela por todos los rincones."),
 ("cuento_05", "Por las noches, a Lucía le salían muchas preguntas.<br>—Papá, ¿fue culpa mía? ¿Porque un día la regañé?<br>—No, cariño. No fue culpa de nadie. Canela era muy mayor y estaba enferma.",
  "—¿Y tú también te vas a morir?<br>—Lo normal es que vivamos muchísimos años. Y yo voy a estar aquí para cuidarte.<br>Lucía hizo las mismas preguntas muchas noches, y papá le contestó siempre con la misma calma."),
 ("cuento_06", "Un domingo, la familia preparó una despedida. Encendieron una vela junto a la foto de Canela y cada uno dijo algo que le gustaba de ella.<br>—Era muy blandita —dijo Lucía.<br>—Movía la cola cuando llegábamos —dijo papá.<br>—Nos quería muchísimo —dijo mamá.",
  "Después apagaron la vela juntos y se dieron un abrazo muy, muy largo."),
 ("cuento_07", "Al día siguiente, Lucía dibujó a Canela con sus ceras favoritas: con su collar rojo, en el jardín y con un corazón enorme.",
  "Dibujar la ayudaba a decir cosas que no le salían con palabras."),
 ("cuento_08", "Mamá le regaló una caja de madera.<br>—Es tu caja de los recuerdos —le dijo.<br>Lucía guardó dentro el collar rojo, su dibujo y la pelota mordisqueada de Canela.",
  "Cuando la echaba de menos, abría la caja. Y era como darle un abrazo."),
 ("cuento_09", "Poco a poco, volvieron los días de sol. Una tarde, Lucía se dio cuenta de que se estaba riendo a carcajadas mientras jugaba con Miso, y por un momento se sintió rara.",
  "—Reír no significa que la quieras menos —le dijo mamá—. A Canela le encantaba verte feliz."),
 ("cuento_10", "Ahora, cuando Lucía mira el atardecer, a veces piensa en Canela, y alguna nube hasta se le parece. Ya no duele tanto como al principio.",
  "Se pone la mano en el corazón y nota que su amiga sigue ahí, en todo lo que aprendió a su lado: a querer, a jugar y a cuidar."),
]

paginas = "".join(f'''
<section class="chapter story"{' data-mark="p-h"' if i == 0 else ''}>
  <div class="ill-img" style="background-image:url('../img/{img}.png')"></div>
  <p>{a}</p><p>{b}</p>
</section>''' for i, (img, a, b) in enumerate(HISTORIA))

html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Cuando un amigo se va · Tremdora</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
{{{{CSS}}}}
<style>
 :root{{--accent:#5c7d99;}}
 .story .ill-img{{height:98mm;margin:0 0 5mm;border-radius:4mm;background-size:cover;background-position:center 40%;box-shadow:0 1mm 3mm rgba(60,40,30,.12)}}
 .story p{{font-size:12.5pt;line-height:1.45;text-align:left;hyphens:manual;margin-bottom:.5em}}
 .kids .prompt{{font-size:15pt}}
 .kids p{{font-size:12.5pt;text-align:left}}
 .color-page img{{width:100%;height:150mm;object-fit:contain;display:block;margin-top:3mm}}
 .fillpage{{height:166mm;display:flex;flex-direction:column;box-sizing:border-box}}
 .fillpage > .q:last-child{{flex:1;display:flex;flex-direction:column}}
 .fillpage > .q:last-child .lines{{flex:1;height:auto}}
 .fillpage > .box:last-child, .fillpage > .lines:last-child{{flex:1;height:auto!important}}
 .kids .lines{{background-image:repeating-linear-gradient(to bottom,transparent 0,transparent 10mm,#cdb8a6 10mm,#cdb8a6 10.3mm)}}
 .cover-ill{{height:78mm;border-radius:4mm;background:url('../img/cuento_01.png') center 45%/cover;margin:4mm 0 2mm}}
</style>
</head><body>
{{{{DEFS}}}}

<section class="page"><div class="halftitle" style="justify-content:center;box-sizing:border-box;padding:6mm 0">
  <div class="brand">Tremdora</div>
  <h1 style="font-size:30pt;margin-top:4mm">Cuando un<br>amigo se va</h1>
  <div class="cover-ill" style="margin-left:8mm;margin-right:8mm"></div>
  <div class="tag">Un cuento para niños</div>
  <div class="tag2" style="margin-top:1em">Regalo de la colección Sigue contigo</div>
</div></section>

<section class="page"><div class="legal">
  <p><strong>Cuando un amigo se va</strong><br>Un cuento para acompañar a los niños en la pérdida de su mascota · Regalo de la colección Sigue contigo</p>
  <p>© 2026 Tremdora. Todos los derechos reservados.<br>Se permite imprimir este cuento para uso personal y familiar de quien lo ha adquirido. Queda prohibida su reproducción, distribución o comunicación pública sin autorización previa y por escrito de Tremdora.</p>
  <p>Primera edición: 2026</p>
</div></section>

<section class="chapter">
  <div class="kicker">Para las personas adultas</div>
  <h1 class="ch">Antes de leerlo juntos</h1>
  <div class="orn">——— · ———</div>
  <p>Este cuento está pensado para niños y niñas de 3 a 8 años que acaban de perder a su perro, a su gato o a cualquier otro compañero. Sigue las mismas ideas del capítulo IX de <em>Sigue contigo</em>: decir la verdad con palabras sencillas, dar permiso para sentir y acompañar sin prisas.</p>
  <h3>Algunas ideas para leerlo</h3>
  <ul>
    <li>Leedlo despacio, con el niño en el regazo o a vuestro lado.</li>
    <li>Parad cuando haga preguntas. No hay respuestas perfectas: basta con que sean sinceras.</li>
    <li>Podéis cambiar «Canela» por el nombre de vuestra mascota.</li>
    <li>Si lloráis, no lo escondáis: vuestro llanto le da permiso para el suyo.</li>
    <li>Al final encontraréis actividades para hacer juntos.</li>
  </ul>
  <p class="note">El cuento usa la palabra «murió» a propósito. Expresiones como «se ha dormido» o «se ha ido de viaje» pueden confundir a los niños o hacer que tengan miedo de dormir.</p>
</section>

{paginas}

<section class="chapter"><div class="center-page">
  <p class="quote" style="font-size:20pt">Porque cuando un amigo se va,<br>el amor que nos dio<br>se queda para siempre<br>en el corazón.</p>
  <p style="text-align:center;font-family:'Cormorant Garamond',serif;font-size:24pt;color:var(--accent)">Fin</p>
</div></section>

<section class="chapter kids fillpage" data-mark="p-act">
  <div class="kicker">Ahora te toca a ti</div>
  <h1 class="ch">Dibuja a tu amigo</h1>
  <div class="orn">——— · ———</div>
  <div class="fill"><span style="font-size:13pt">Se llamaba:</span><i></i></div>
  <div class="box" style="height:110mm">Dibújalo aquí, como tú lo recuerdas</div>
</section>

<section class="chapter kids fillpage">
  <div class="kicker">Ahora te toca a ti</div>
  <h1 class="ch">Lo que más me gustaba de él o de ella</h1>
  <div class="orn">——— · ———</div>
  <div class="q"><div class="prompt">Jugábamos a…</div><div class="lines" style="height:21mm"></div></div>
  <div class="q"><div class="prompt">Me hacía reír cuando…</div><div class="lines" style="height:21mm"></div></div>
  <div class="q"><div class="prompt">Lo que más echo de menos es…</div><div class="lines"></div></div>
</section>

<section class="chapter kids fillpage">
  <div class="kicker">Ahora te toca a ti</div>
  <h1 class="ch">Una carta para mi amigo</h1>
  <p class="sub">Puedes escribirla tú o pedir a un adulto que te ayude</p>
  <div class="orn">——— · ———</div>
  <div class="fill"><span style="font-size:13pt">Querido / Querida</span><i></i></div>
  <div class="lines"></div>
</section>

<section class="chapter kids">
  <div class="kicker">Ahora te toca a ti</div>
  <h1 class="ch">Mi caja de los recuerdos</h1>
  <div class="orn">——— · ———</div>
  <p>Como Lucía, puedes tener tu propia caja. Busca una caja bonita, decórala y guarda dentro cosas que te recuerden a tu amigo. Marca lo que vas guardando:</p>
  <div class="check">Una foto suya</div>
  <div class="check">Su collar o su placa</div>
  <div class="check">Su juguete favorito</div>
  <div class="check">Un dibujo que he hecho</div>
  <div class="check">Mi carta para él o para ella</div>
  <div class="check">Algo de nuestro sitio favorito (una hoja, una piedra…)</div>
  <div class="check">Otra cosa: ______________________</div>
  <p class="note">Cuando le eches de menos, abre la caja. Es como darle un abrazo.</p>
</section>

<section class="chapter kids">
  <div class="kicker">Ahora te toca a ti</div>
  <h1 class="ch">Cuando estoy triste, puedo…</h1>
  <div class="orn">——— · ———</div>
  <div class="check">Llorar todo lo que necesite</div>
  <div class="check">Pedir un abrazo muy largo</div>
  <div class="check">Hablar de mi amigo con alguien de mi familia</div>
  <div class="check">Hacerle un dibujo</div>
  <div class="check">Abrir mi caja de los recuerdos</div>
  <div class="check">Mirar sus fotos</div>
  <div class="check">Respirar despacio, como si oliera una flor y soplara una vela</div>
  <div class="check">Jugar y reír: eso no significa que lo quiera menos</div>
  <p class="note">Y recuerda: no fue culpa tuya. Nunca.</p>
</section>

<section class="chapter color-page">
  <div class="kicker">Para colorear</div>
  <img src="../img/colorear_1.png" alt="">
</section>

<section class="chapter color-page">
  <div class="kicker">Para colorear</div>
  <img src="../img/colorear_2.png" alt="">
</section>

<section class="chapter">
  <div class="kicker">Para las personas adultas</div>
  <h1 class="ch">Después del cuento</h1>
  <div class="orn">——— · ———</div>
  <p>Cada niño vive el duelo a su manera. Algunos preguntan una y otra vez; otros parecen indiferentes y, de repente, lloran por algo pequeño. Todo eso es normal.</p>
  <h3>Lo que más les ayuda</h3>
  <ul>
    <li>Escuchar la verdad, con palabras sencillas.</li>
    <li>Oír que no fue culpa suya.</li>
    <li>Mantener sus rutinas.</li>
    <li>Participar en una pequeña despedida.</li>
    <li>Ver que los adultos también están tristes, y que se sigue adelante.</li>
  </ul>
  <p class="note">Si pasadas varias semanas notas pesadillas frecuentes, miedo intenso a separarse de ti, retrocesos (como volver a mojar la cama) o tristeza que no cede, coméntalo con su pediatra o con un psicólogo infantil.</p>
  <p class="sign">Con todo el cariño,<br>Tremdora<br><span style="color:var(--accent)">Ellos se merecen lo mejor.</span></p>
</section>
</body></html>'''
(ROOT / 'libros' / 'cuento.html').write_text(html)
print('ok')
