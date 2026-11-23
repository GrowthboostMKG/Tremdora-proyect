# Genera portadas planas (1600x2560) con el estilo de «Sigue contigo».
import json, sys, html, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
TPL = """<!doctype html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,500&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>
 :root{--ink:#2f2622;--soft:#6b5a52;--accent:%(accent)s;--paper:#f7f1e8;}
 html,body{margin:0;background:var(--paper)}
 .cover{position:relative;width:1600px;height:2560px;overflow:hidden;background:var(--paper);font-family:'EB Garamond',serif;color:var(--ink)}
 .photo{position:absolute;left:0;right:0;bottom:0;height:%(photo_h)spx;background:url('../fotos/%(photo)s') center %(photo_pos)s/cover no-repeat}
 .photo::before{content:'';position:absolute;inset:0 0 auto 0;height:640px;background:linear-gradient(to bottom,var(--paper) 0%%,rgba(247,241,232,.86) 30%%,rgba(247,241,232,.35) 70%%,rgba(247,241,232,0) 100%%)}
 .frame{position:absolute;inset:46px;border:2px solid var(--accent);opacity:.6}
 .frame::after{content:'';position:absolute;inset:12px;border:1px solid var(--accent);opacity:.6}
 .top{position:absolute;top:%(top)spx;left:80px;right:80px;text-align:center}
 .brand{font-family:'Cormorant Garamond',serif;letter-spacing:.42em;font-size:40px;color:var(--accent);text-transform:uppercase;padding-left:.42em}
 .rule{color:var(--accent);font-size:30px;letter-spacing:.35em;margin:30px 0 8px;opacity:.8}
 .kick{display:inline-block;margin-top:26px;font-size:38px;letter-spacing:.2em;text-transform:uppercase;color:var(--accent);border:2px solid var(--accent);border-radius:60px;padding:10px 34px 8px}
 h1{font-family:'Cormorant Garamond',serif;font-weight:500;font-size:%(size)spx;line-height:.92;margin:24px 0 0;letter-spacing:-2px}
 h1 em{display:block;font-style:italic;font-weight:400;color:var(--accent)}
 .sub{font-style:italic;font-size:%(sub_size)spx;line-height:1.25;color:var(--soft);margin-top:40px}
</style></head><body><div class="cover" id="cover">
 <div class="photo"></div><div class="frame"></div>
 <div class="top"><div class="brand">Tremdora</div><div class="rule">——— · ———</div>%(kick)s
 <h1>%(t1)s<em>%(t2)s</em></h1>%(sub)s</div>
</div></body></html>"""
data = json.load(open(ROOT/'tools'/'covers.json'))
for c in data:
    d = dict(accent=c.get('accent','#b0603f'), photo=c['photo'], photo_h=c.get('photo_h',1600), photo_pos=c.get('photo_pos','center'),
             top=c.get('top',170), size=c.get('size',260), sub_size=c.get('sub_size',62),
             t1=html.escape(c['t1']), t2=html.escape(c['t2']),
             kick=f'<div><span class="kick">{html.escape(c["kick"])}</span></div>' if c.get('kick') else '',
             sub=f'<div class="sub">{c["sub"]}</div>' if c.get('sub') else '')
    (ROOT/'portadas'/f"{c['id']}.html").write_text(TPL % d)
print(len(data))
