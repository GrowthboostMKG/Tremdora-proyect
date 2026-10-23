#!/usr/bin/env python3
"""Mide la altura real de cada .page y avisa de las que se pasan de A4."""
import pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).parent
name = sys.argv[1]
css = (HERE/"book.css").read_text(encoding="utf-8")
html = (HERE/f"{name}.html").read_text(encoding="utf-8").replace("/*CSS*/", css, 1)

probe = """<script>
window.addEventListener('load', function(){
  var mm = 297, px = mm * 96 / 25.4;
  var out = [];
  document.querySelectorAll('.page').forEach(function(s, i){
    var top = s.getBoundingClientRect().top;
    var last = s.lastElementChild;
    var h = last ? (last.getBoundingClientRect().bottom - top + 83) : 0;
    var id = (s.querySelector('.ch-title, h1, h2') || {}).textContent || '';
    out.push((i+1) + '|' + Math.round(h/96*25.4) + '|' + id.trim().slice(0,46).replace(/\\s+/g,' '));
  });
  var pre = document.createElement('pre');
  pre.id = 'MEDIDAS';
  pre.textContent = out.join('\\n');
  document.body.appendChild(pre);
});
</script></body>"""
html = html.replace("</body>", probe, 1)
tmp = HERE/f"{name}.measure.html"
tmp.write_text(html, encoding="utf-8")

dom = subprocess.run(["/opt/pw-browsers/chromium","--headless","--disable-gpu",
    "--no-sandbox","--virtual-time-budget=5000","--dump-dom", str(tmp)],
    capture_output=True, text=True).stdout
m = re.search(r'<pre id="MEDIDAS">(.*?)</pre>', dom, re.S)
if not m:
    sys.exit("no se pudo medir")
bad = 0
for line in m.group(1).strip().splitlines():
    n, h, t = line.split("|", 2)
    h = int(h)
    if True:
        bad += 1 if h > 297 else 0
        flag = "⚠" if h > 297 else ("·" if h > 285 else " ")
        print(f"  {flag} pág {n:>3}  {h:>4} mm  {t}")
print(f"\n{bad} secciones se pasan de A4 · {len(m.group(1).strip().splitlines())} secciones en total")
