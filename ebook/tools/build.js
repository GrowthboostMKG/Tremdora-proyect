// Genera ebook/Sigue_contigo_Tremdora.pdf a partir de sigue-contigo.html
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path'); const { execSync } = require('child_process');
const dir = path.resolve(__dirname, '..');
const src = fs.readFileSync(path.join(dir, 'sigue-contigo.html'), 'utf8');
const footer = `<div style="width:100%;font-family:Georgia,serif;font-size:7.5pt;color:#9a8478;text-align:center;letter-spacing:.15em;">
  tremdora · <span class="pageNumber"></span></div>`;
async function render(html, out, withFooter) {
  const b = await chromium.launch(); const p = await b.newPage();
  const tmp = path.join(dir, '.tmp.html'); fs.writeFileSync(tmp, html);
  await p.goto('file://' + tmp, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: out, format: 'A5', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: withFooter, headerTemplate: '<div></div>', footerTemplate: withFooter ? footer : '<div></div>' });
  await b.close(); fs.unlinkSync(tmp);
}
(async () => {
  // Pase 1: marcadores invisibles para localizar la página de cada sección
  let marked = src.replace(/data-mark="([^"]+)">/g, (m, k) => `${m}<span style="position:absolute;font-size:1px;color:transparent">§${k}§</span>`);
  marked = marked.replace(/\{\{(p-[^}]+)\}\}/g, '00');
  const p1 = path.join(dir, '.pass1.pdf'); await render(marked, p1, true);
  const n = parseInt(execSync(`pdfinfo ${p1} | awk '/^Pages/{print $2}'`).toString());
  const pages = {};
  for (let i = 1; i <= n; i++) {
    const t = execSync(`pdftotext -f ${i} -l ${i} ${p1} -`).toString();
    for (const m of t.matchAll(/§(p-[^§]+)§/g)) pages[m[1]] = pages[m[1]] || i;
  }
  console.log(pages);
  const final = src.replace(/\{\{(p-[^}]+)\}\}/g, (m, k) => pages[k] || '??');
  const out = path.join(dir, 'Sigue_contigo_Tremdora.pdf');
  await render(final, out, true);
  fs.unlinkSync(p1);
  execSync(`python3 ${path.join(__dirname, 'background.py')} ${out}`);
})();
