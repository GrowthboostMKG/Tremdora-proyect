const { chromium } = require('playwright'); const path=require('path');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1600,height:2560}});
 await p.goto('file://'+path.resolve(__dirname,process.argv[2]),{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
 const sel=process.argv[4]||'body'; await (await p.$(sel)).screenshot({path:process.argv[3]}); await b.close(); })();
