// Uso: node render.js archivo.html salida.png [selector] [ancho] [alto] [transparente]
const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const [,,file,out,sel='body',w='1600',h='2560',tr]=process.argv;
 const b=await chromium.launch(); const p=await b.newPage({viewport:{width:+w,height:+h}});
 await p.goto('file://'+path.resolve(__dirname,file),{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
 await (await p.$(sel)).screenshot({path:out, omitBackground: !!tr}); await b.close(); })();
