# Genera libros/su-historia.html (Libro 4 de 4 de la colección «Sigue contigo»).
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

def pagina(kicker, titulo, cuerpo, sub=None, mark=None):
    m = f' data-mark="{mark}"' if mark else ''
    s = f'<p class="sub">{sub}</p>' if sub else ''
    return f'''<section class="chapter fillpage"{m}>
  <div class="kicker">{kicker}</div><h1 class="ch">{titulo}</h1>{s}
  <div class="orn">——— · ———</div>
  {cuerpo}
</section>'''

def p(pregunta, n=3):
    return f'<div class="q"><div class="prompt">{pregunta}</div><div class="lines l{n}"></div></div>'

def foto(alto=60, texto="Pega aquí una foto"):
    return f'<div class="box" style="height:{alto}mm">{texto}</div>'

def f(etiqueta, sufijo=""):
    return f'<div class="fill"><span>{etiqueta}</span><i></i>{f"<span>{sufijo}</span>" if sufijo else ""}</div>'

CARACTER = ["Cariñosa", "Juguetona", "Dormilona", "Glotona", "Curiosa", "Independiente", "Protectora",
            "Miedosa", "Valiente", "Testaruda", "Tranquila", "Traviesa", "Charlatana", "Pegajosa", "Sabia", "Payasa"]
car = '<div class="row" style="flex-wrap:wrap;gap:0 4mm">' + "".join(
    f'<div class="check" style="flex:0 0 30%">{c}</div>' for c in CARACTER) + '</div>'

paginas = [
 pagina("Su ficha", "Así era", foto(58, "Pega aquí su foto favorita") +
        f("Su nombre:") + f("Cómo la llamábamos en casa:") + f("Especie y raza:") + f("Color y señas particulares:") +
        f("Nació (o llegó) el:") + f("Se despidió el:") + f("Vivimos juntos", "años."), mark="p-ficha"),
 pagina("Capítulo 1", "Cómo llegó a mi vida", p("¿Dónde y cómo nos encontramos?", 4) + p("¿Por qué la elegimos (o nos eligió ella)?", 3) + foto(48, "Una foto de sus primeros días")),
 pagina("Capítulo 2", "Nuestro primer día", p("¿Qué recuerdo de su primer día en casa?", 4) + p("¿Dónde durmió la primera noche?", 2) + p("Lo primero que me hizo sonreír", 3)),
 pagina("Capítulo 3", "Su carácter", '<p>Marca las palabras que mejor la describen y añade las tuyas.</p>' + car + p("Si tuviera que describirla en una frase…", 3)),
 pagina("Capítulo 4", "Sus manías y rarezas", p("Esas cosas que solo hacía ella", 5) + p("Su forma de pedir lo que quería", 3) + p("El ruido, la cosa o la persona que no soportaba", 2)),
 pagina("Capítulo 5", "Lo que más le gustaba", f("Su comida favorita:") + f("Su juguete favorito:") + f("Su sitio favorito de la casa:") +
        f("Su paseo o rincón preferido:") + f("Su persona favorita:") + f("Su momento favorito del día:") + p("Lo que la hacía más feliz", 4)),
 pagina("Capítulo 6", "Un día cualquiera a su lado", '<p>Cuenta cómo era un día normal con ella, desde que os levantabais hasta la noche.</p>' +
        f("Por la mañana:") + f("A mediodía:") + f("Por la tarde:") + f("Por la noche:") + p("El pequeño ritual que más echo de menos", 4)),
 pagina("Capítulo 7", "Sus travesuras", p("La travesura más grande que hizo", 4) + p("Aquella vez que nos hizo reír a todos", 4) + foto(40, "Una foto divertida")),
 pagina("Capítulo 8", "Nuestros lugares", p("Los sitios que recorrimos juntos", 4) + p("Un viaje, una excursión o un día especial", 4) + foto(42, "Una foto de vuestro lugar")),
 pagina("Capítulo 9", "Su familia", '<p>Las personas y los animales que la quisieron. Pide a cada uno que escriba su nombre y una frase para ella.</p>' + '<div class="lines l16"></div>'),
 pagina("Álbum", "Fotos que no quiero olvidar", '<div class="row">' + foto(50) + foto(50) + '</div><div class="row">' + foto(50) + foto(50) + '</div>'),
 pagina("Álbum", "Más momentos", '<div class="row">' + foto(50) + foto(50) + '</div><div class="row">' + foto(50) + foto(50) + '</div>'),
 pagina("Un recuerdo que se toca", "Su huella", '<p>Si conservas la huella de su pata, un mechón de pelo o la placa de su collar, este es su lugar.</p>' +
        foto(95, "Su huella, su pelo o su placa") + f("Fecha:")),
 pagina("Capítulo 10", "Lo que me enseñó", p("Lo que aprendí a su lado", 6) + p("La versión de mí que existe gracias a ella", 5)),
 pagina("Capítulo 11", "Lo que quiero que se sepa de ella", '<p>Si alguien que no la conoció abriera este libro, ¿qué te gustaría que supiera?</p>' + '<div class="lines l12"></div>'),
 pagina("Capítulo 12", "Nuestra despedida", '<p class="note" style="text-align:left">Esta página es opcional. Complétala solo si quieres y cuando te sientas con fuerzas.</p>' +
        p("Cómo fue nuestro último día juntos", 5) + p("Lo que le dije (o lo que me habría gustado decirle)", 5)),
 pagina("Para ti", "Una carta para ella", '<div class="lines l16"></div>'),
]

html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>Su historia · Tremdora</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
{{{{CSS}}}}
<style>:root{{--accent:#a06a3c;}}
 .fillpage{{height:166mm;display:flex;flex-direction:column;box-sizing:border-box}}
 .fillpage > .q:last-child{{flex:1;display:flex;flex-direction:column}}
 .fillpage > .q:last-child .lines{{flex:1;height:auto}}
 .fillpage > .lines:last-child, .fillpage > .box:last-child{{flex:1;height:auto!important}}
</style>
</head><body>
{{{{DEFS}}}}

<section class="page"><div class="halftitle">
  <div class="brand">Tremdora</div><div class="orn">——— · ———</div>
  <h1>Su<br>historia</h1><div class="orn">——— · ———</div>
  <div class="tag">El libro de su vida</div>
  <div class="tag2">Colección Sigue contigo · Libro 4 de 4</div>
</div></section>

<section class="page"><div class="legal">
  <p><strong>Su historia</strong><br>El libro de su vida · Colección Sigue contigo, libro 4 de 4</p>
  <p>© 2026 Tremdora. Todos los derechos reservados.<br>Se permite imprimir este álbum para uso personal de quien lo ha adquirido. Queda prohibida su reproducción, distribución o comunicación pública sin autorización previa y por escrito de Tremdora.</p>
  <p>Primera edición: 2026</p>
</div></section>

<section class="page"><div class="center-page">
  <div class="kicker" style="margin-top:0">La historia de</div>
  <div style="border-bottom:1.5px solid var(--accent);width:85mm;margin:12mm auto 4mm;height:12mm"></div>
  <p class="sub">contada con amor por</p>
  <div style="border-bottom:1px solid #b89d88;width:70mm;margin:8mm auto 0;height:8mm"></div>
  <div class="orn" style="margin-top:14mm">——— · ———</div>
</div></section>

<section class="chapter">
  <div class="kicker">Antes de empezar</div>
  <h1 class="ch">Para que su historia no se pierda</h1>
  <div class="orn">——— · ———</div>
  <p>Cada animal que pasa por nuestra vida tiene una historia única: cómo llegó, sus manías, sus travesuras, la forma en que nos miraba. Con el tiempo, algunos detalles se desdibujan. Este libro existe para que eso no pase.</p>
  <p>Aquí vas a escribir la historia de tu compañera o compañero, con tus palabras, tus fotos y tus recuerdos. No hace falta hacerlo de una vez ni en orden. Hay páginas que te saldrán solas y otras que necesitarán su momento.</p>
  <p>Cuando lo termines, podrás releerlo en los aniversarios, guardarlo junto a su urna o en su caja de la memoria y, algún día, enseñárselo a alguien para contarle quién fue. Porque contar su historia es una forma de que siga contigo.</p>
  <p class="note">Imprímelo en papel grueso si puedes, pega las fotos y escribe a mano: tu letra también forma parte del recuerdo.</p>
  <p class="sign">Con todo el cariño,<br>el equipo de Tremdora</p>
</section>

{"".join(paginas)}

<section class="chapter"><div class="center-page">
  <div class="orn">——— · ———</div>
  <p class="quote" style="font-size:18pt">No la has perdido.<br>La llevas contigo.<br>Está en cómo miras,<br>en cómo quieres,<br>en cómo cuidas.</p>
  <p style="text-align:center;font-family:'Cormorant Garamond',serif;font-size:22pt;color:var(--accent)">Sigue contigo. Siempre.</p>
  <p class="sign" style="text-align:center">Tremdora<br><span style="color:var(--accent)">Ellos se merecen lo mejor.</span></p>
</div></section>
</body></html>'''
(ROOT / 'libros' / 'su-historia.html').write_text(html)
print('ok', len(paginas))
