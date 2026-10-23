#!/usr/bin/env python3
"""Detecta páginas cuyo contenido se sale de la caja de 679.92 pt.

Inyecta un script de medición en una copia del HTML, la abre con Chromium
headless (--dump-dom) y lee el informe que el script deja en el DOM.
"""
import re, subprocess, sys, tempfile, os

CHROME = os.environ.get('CHROME', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome')

PROBE = """
<script>
(function(){
  var out=[];
  document.querySelectorAll('.page').forEach(function(p,i){
    var pad=parseFloat(getComputedStyle(p).paddingBottom);
    var top=p.getBoundingClientRect().top, low=0;
    p.querySelectorAll(':scope > *').forEach(function(c){
      if(c.classList.contains('pfoot')) return;
      low=Math.max(low, c.getBoundingClientRect().bottom-top);
    });
    var limit=p.clientHeight-pad;
    if(low>limit+1) out.push((i+1)+':alto+'+(low-limit).toFixed(1));
    var wide=0;
    p.querySelectorAll('table,.fig,svg,img,pre').forEach(function(c){
      wide=Math.max(wide, c.scrollWidth||0, c.getBoundingClientRect().width);
    });
    var wlimit=p.clientWidth-parseFloat(getComputedStyle(p).paddingLeft)
                            -parseFloat(getComputedStyle(p).paddingRight);
    if(wide>wlimit+1) out.push((i+1)+':ancho+'+(wide-wlimit).toFixed(1));
  });
  var d=document.createElement('div');
  d.id='overflow-report';
  d.textContent='REPORT['+out.join(' ')+']';
  document.body.appendChild(d);
})();
</script>
"""

def check(path):
    html = open(path, encoding='utf-8').read().replace('</body>', PROBE + '</body>')
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False,
                                     encoding='utf-8') as fh:
        fh.write(html); tmp = fh.name
    try:
        dom = subprocess.run(
            [CHROME, '--headless', '--no-sandbox', '--disable-gpu',
             '--virtual-time-budget=4000', '--dump-dom', tmp],
            capture_output=True, text=True, timeout=120).stdout
    finally:
        os.unlink(tmp)
    m = re.search(r'id="overflow-report"[^>]*>REPORT\[(.*?)\]</div>', dom)
    if not m:
        return None
    return [x for x in m.group(1).split() if x]

if __name__ == '__main__':
    bad = 0
    for f in sys.argv[1:]:
        r = check(f)
        name = os.path.basename(f)
        if r is None:
            print('??  %s — no se pudo medir' % name); bad = 1
        elif not r:
            print('OK  %s — sin desbordes' % name)
        else:
            bad = 1
            print('!!  %s — desbordes (pág:exceso pt): %s' % (name, ', '.join(r)))
    sys.exit(bad)
