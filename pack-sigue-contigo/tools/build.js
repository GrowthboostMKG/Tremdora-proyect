// Uso: node tools/build.js libros/xxx.html "Título" final/Salida.pdf
// Maqueta un libro del pack con el estilo de «Sigue contigo» (A5, pie «tremdora · n», fondo crema a sangre).
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path'); const { execSync } = require('child_process');
const [,, input, title, output] = process.argv;
const root = path.resolve(__dirname, '..');
let src = fs.readFileSync(path.resolve(root, input), 'utf8');
src = src.replace('{{CSS}}', '<style>' + fs.readFileSync(path.join(__dirname, 'base.css'), 'utf8') + fs.readFileSync(path.join(__dirname, 'extra.css'), 'utf8') + '</style>')
         .replace('{{DEFS}}', fs.readFileSync(path.join(__dirname, 'defs.svg'), 'utf8'));
const footer = `<div style="width:100%;font-family:Georgia,serif;font-size:7.5pt;color:#9a8478;text-align:center;letter-spacing:.15em;">tremdora · <span class="pageNumber"></span></div>`;
async function render(html, out) {
  const b = await chromium.launch(); const p = await b.newPage();
  const tmp = path.join(path.dirname(path.resolve(root, input)), '.tmp_' + path.basename(input));
  fs.writeFileSync(tmp, html);
  await p.goto('file://' + tmp, { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: out, format: 'A5', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true,
                headerTemplate: '<div></div>', footerTemplate: footer });
  await b.close(); fs.unlinkSync(tmp);
}
(async () => {
  const marked = src.replace(/data-mark="([^"]+)">/g, (m, k) => `${m}<span style="position:absolute;font-size:1px;color:transparent">§${k}§</span>`)
                    .replace(/\{\{(p-[^}]+)\}\}/g, '00');
  const p1 = path.join(root, '.pass1.pdf'); await render(marked, p1);
  const n = parseInt(execSync(`pdfinfo ${p1} | awk '/^Pages/{print $2}'`).toString());
  const pages = {};
  for (let i = 1; i <= n; i++) {
    const t = execSync(`pdftotext -f ${i} -l ${i} ${p1} - 2>/dev/null`).toString();
    for (const m of t.matchAll(/§(p-[^§]+)§/g)) pages[m[1]] = pages[m[1]] || i;
  }
  const out = path.resolve(root, output);
  await render(src.replace(/\{\{(p-[^}]+)\}\}/g, (m, k) => pages[k] || '??'), out);
  fs.unlinkSync(p1);
  execSync(`python3 ${path.join(__dirname, 'background.py')} "${out}" "${title}"`);
  console.log(output, execSync(`pdfinfo "${out}" | awk '/^Pages/{print $2}'`).toString().trim(), 'páginas');
})();
