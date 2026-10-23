import os, subprocess, base64, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = HERE
PHOTO = os.path.join(HERE, "..", "..", "ebooks", "fuentes", "victoria-paris.jpg")
CHROME = "/opt/pw-browsers/chromium"

photo_b64 = base64.b64encode(open(PHOTO, "rb").read()).decode()

EMBLEMA = '''<svg viewBox="0 0 150 150">
  <circle cx="75" cy="75" r="62" fill="none" stroke="#748156" stroke-width="1.1"/>
  <path d="M75 108 C52 90 44 76 44 64 c0-11 9-19 19-19 6 0 10 3 12 7
           2-4 6-7 12-7 10 0 19 8 19 19 0 12-8 26-31 44z"
        fill="#f6e9d6" stroke="#a8502e" stroke-width="1.6" stroke-linejoin="round"/>
  <ellipse cx="75" cy="76" rx="7.5" ry="6" fill="#e2cfb4"/>
  <ellipse cx="67" cy="65" rx="2.8" ry="4" fill="#e2cfb4" transform="rotate(-18 67 65)"/>
  <ellipse cx="75" cy="61" rx="2.8" ry="4.2" fill="#e2cfb4"/>
  <ellipse cx="83" cy="65" rx="2.8" ry="4" fill="#e2cfb4" transform="rotate(18 83 65)"/>
</svg>'''

CSS = """
:root{
  --bg:#fbf3e6; --paper:#fdf8f0; --panel:#f6e9d6;
  --ink:#3b2a20; --ink-soft:#6b4a38; --muted:#9c7c63; --line:#e2cfb4;
  --green:#748156; --green-soft:#e6eada; --terra:#a8502e; --terra-soft:#c1613a;
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:"Caladea",Georgia,serif;color:var(--ink);background:var(--paper);
     -webkit-font-smoothing:antialiased}
.s{width:1080px;height:1350px;position:relative;display:flex;flex-direction:column;
   padding:96px 92px 88px;background:var(--paper)}
.s.calma{background:var(--bg)}
.s.centro{justify-content:center}

/* --- marca arriba --- */
.marca{font-family:"Inter",sans-serif;font-size:21px;font-weight:600;letter-spacing:.30em;
       text-transform:uppercase;color:var(--muted)}
.regla{height:2px;background:var(--line);margin-top:26px}

/* --- cuerpo --- */
.cuerpo{flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px}
.grande{font-size:68px;line-height:1.20;letter-spacing:-.012em}
.media{font-size:54px;line-height:1.26;letter-spacing:-.008em}
.apoyo{font-size:38px;line-height:1.44;color:var(--ink-soft)}
.menor{font-family:"Inter",sans-serif;font-size:29px;line-height:1.52;color:var(--muted);
       font-weight:400}
em{font-style:italic;color:var(--terra)}
strong{font-weight:700}
.verde{color:var(--green)}

/* --- pie --- */
.pie{display:flex;align-items:center;justify-content:space-between;
     font-family:"Inter",sans-serif;font-size:24px;color:var(--muted)}
.pie .num{font-weight:600;letter-spacing:.08em}
.sigue{font-family:"Inter",sans-serif;font-size:25px;font-weight:600;color:var(--terra);
       letter-spacing:.02em}

/* --- portada --- */
.s.portada{background:
   radial-gradient(900px 620px at 18% 8%, #f7e4c0 0%, rgba(247,228,192,0) 62%),
   radial-gradient(820px 640px at 88% 96%, #dfe3cd 0%, rgba(223,227,205,0) 60%),
   #fbf3e6}
.emb{width:132px;height:132px;margin-bottom:60px}
.emb svg{width:100%;height:100%}
.portada .hook{font-size:78px;line-height:1.14;letter-spacing:-.018em}
.portada .desliza{position:absolute;left:92px;bottom:88px;font-family:"Inter",sans-serif;font-size:27px;font-weight:600;color:var(--terra)}
.portada .bajada{font-size:42px;line-height:1.38;color:var(--ink-soft);margin-top:44px}

/* --- la foto --- */
.s.foto{padding:0;display:flex;flex-direction:column;background:var(--bg)}
.foto .alto{height:185px;padding:96px 92px 0}
.foto img{width:1080px;height:810px;object-fit:cover;display:block}
.foto .banda{flex:1;padding:52px 92px 88px;display:flex;flex-direction:column}
.foto .nm{font-size:50px;line-height:1.2}
.foto .dt{font-family:"Inter",sans-serif;font-size:28px;color:var(--muted);margin-top:16px}

/* --- cierre --- */
.s.cierre{background:
   radial-gradient(880px 600px at 80% 12%, #e6eada 0%, rgba(230,234,218,0) 62%),
   radial-gradient(760px 600px at 10% 92%, #f7e4c0 0%, rgba(247,228,192,0) 60%),
   #fbf3e6}
.verbos{font-family:"Inter",sans-serif;font-size:40px;font-weight:600;color:var(--green);
        letter-spacing:.02em;line-height:1.5}
.cierre .cta{font-size:64px;line-height:1.2;margin-top:8px}
.cierre .cuenta{font-family:"Inter",sans-serif;font-size:32px;font-weight:600;
                color:var(--terra);letter-spacing:.04em}
.cierre .remate{font-size:34px;line-height:1.45;color:var(--ink-soft);margin:36px 0 52px}
.cierre .emb{width:108px;height:108px;margin:0 0 48px}
"""

def pie(n, sigue=True):
    s = '<div class="sigue">Desliza →</div>' if sigue else '<div></div>'
    return f'<div class="pie"><div class="num">{n} / 9</div>{s}</div>'

S = {}

S[1] = f'''<div class="s portada centro">
  <div class="emb">{EMBLEMA}</div>
  <div class="hook">Diecisiete años<br>compitiendo con ella.</div>
  <div class="bajada">Y aun así, hubo cosas suyas que no entendí<br>hasta mucho después.</div>
  <div class="desliza">Desliza →</div>
</div>'''

S[2] = f'''<div class="s foto">
  <div class="alto"><div class="marca">Tremdora</div></div>
  <img src="data:image/jpeg;base64,{photo_b64}" alt="Victoria y Paris">
  <div class="banda">
    <div class="nm">Victoria y <em>Paris</em>.</div>
    <div class="dt">Diecisiete años de equipo</div>
    <div style="flex:1"></div>
    {pie(2)}
  </div>
</div>'''

def hoja(n, bloques, calma=False, sigue=True):
    clase = "s calma" if calma else "s"
    cuerpo = "\n".join(bloques)
    return f'''<div class="{clase}">
  <div class="marca">Tremdora</div><div class="regla"></div>
  <div class="cuerpo">{cuerpo}</div>
  {pie(n, sigue)}
</div>'''

S[3] = hoja(3, [
  '<div class="media">Paris no fue mi mascota.<br>Fue mi <em>compañera de equipo</em> durante casi toda mi vida adulta.</div>',
  '<div class="menor">Madrugones, viajes, los nervios de justo antes de entrar, y la vuelta a casa las dos calladas y agotadas.</div>',
])

S[4] = hoja(4, [
  '<div class="media">Era muy tranquila. Durante años pensé que ese era su carácter y ya está.</div>',
  '<div class="apoyo">Hoy sé que la calma de un animal <strong>también se construye</strong>.</div>',
], calma=True)

S[5] = hoja(5, [
  '<div class="media">Pero lo que me habría cambiado todo era más sencillo: <em>saber cómo funciona su cerebro</em>.</div>',
  '<div class="apoyo">Por qué hacía lo que hacía. Qué sentía cuando yo creía que estaba «rara».</div>',
])

S[6] = hoja(6, [
  '<div class="media">Y luego está el tiempo. Siempre pensé que habría más.</div>',
  '<div class="apoyo">Se me fueron pasando los años esperando un momento mejor. Y ese momento no llega solo: <strong>se busca, o no pasa</strong>.</div>',
], calma=True)

S[7] = hoja(7, [
  '<div class="grande">De ahí viene<br><span class="verde">Tremdora</span>.</div>',
  '<div class="apoyo">Juntar lo que la ciencia ya sabe con lo que necesitas el martes por la tarde, en tu salón, con tu animal delante.</div>',
  '<div class="menor">Sin dominación. Sin castigo. Sin trucos.</div>',
])

S[8] = hoja(8, [
  '<div class="media">Si llevas años con tu animal y sientes que hay cosas suyas que no entiendes: <em>es lo normal</em>.</div>',
  '<div class="apoyo">Nadie nos lo ha explicado nunca. Eso es lo que vengo a hacer aquí.</div>',
], calma=True)

S[9] = f'''<div class="s cierre centro">
  <div class="emb">{EMBLEMA}</div>
  <div class="verbos">Entender · Cuidar · Acompañar · Celebrar</div>
  <div class="cta">Si te suena,<br><em>quédate</em>.</div>
  <div class="remate">Aquí vas a encontrar cómo entender a tu animal<br>y cómo acompañarle. Sin culpa y sin trucos.</div>
  <div class="cuenta">Sígueme · <strong>@tremdora_pets</strong></div>
</div>'''

for n in sorted(S):
    html = f'<!doctype html><html lang="es"><meta charset="utf-8"><style>{CSS}</style>{S[n]}</html>'
    hp = os.path.join(OUT, f"s{n}.html")
    open(hp, "w").write(html)
    png = os.path.join(OUT, f"tremdora-presentacion-{n}.png")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1350",
                    f"--screenshot={png}", f"file://{hp}"],
                   check=True, capture_output=True)
    print("ok", os.path.basename(png))
