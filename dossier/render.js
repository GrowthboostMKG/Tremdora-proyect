const { chromium } = require('playwright');
(async () => {
  const dir = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 794 } });
  await p.goto('file://' + dir + '/dossier.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: dir + '/Dossier_Residencia_Senorial_Madrid.pdf', width: '297mm', height: '210mm', printBackground: true });
  const pages = await p.$$('.page');
  for (let i = 0; i < pages.length; i++) {
    await pages[i].screenshot({ path: dir + '/prev_' + String(i + 1).padStart(2, '0') + '.png' });
  }
  await b.close();
  console.log('pages', pages.length);
})();
