// Uso: node render2.js <carpeta vs-estetica> "60€" "80€" "100€"
const {chromium}=require('playwright');const path=require('path');
const [R,P60='— €',P90='— €',P120='— €']=process.argv.slice(2);
const S=(f)=>'file://'+path.join(R,'src',f);const O=(f)=>path.join(R,'final',f);
(async()=>{const b=await chromium.launch();
 const open=async(file,w,h,dsf)=>{const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:dsf});await p.goto(S(file));
  await p.evaluate(([a,c,d])=>{document.body.innerHTML=document.body.innerHTML.replace('{P60}',a).replace('{P90}',c).replace('{P120}',d);},[P60,P90,P120]);
  await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);return p;};
 let p=await open('post2.html',1080,1350,1);await (await p.$('#page')).screenshot({path:O('06_Post_Ritual_Aurea_v2_1080x1350.png')});
 p=await open('flyer2.html',800,1130,3.125);await (await p.$('.page')).screenshot({path:O('07_Flyer_Ritual_Aurea_v2_A4.png')});
 await p.pdf({path:O('07_Flyer_Ritual_Aurea_v2_A4_Imprenta.pdf'),printBackground:true,preferCSSPageSize:true});
 console.log(await p.evaluate(()=>{const a=document.querySelector('.page').getBoundingClientRect(),f=document.querySelector('.foot').getBoundingClientRect();return 'sobra '+((a.bottom-f.bottom)/3.78).toFixed(1)+'mm'}));
 await b.close();})();
