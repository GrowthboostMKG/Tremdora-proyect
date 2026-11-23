# Exporta las 6 imágenes finales: alta resolución + carrusel 1080x1350 + ZIP + hoja de vista previa.
import os, zipfile
from PIL import Image
names = ["01_Hogar_en_Calma_y_Rutinas","02_Edad_Dorada_y_Cartas","03_Hogar_en_Calma_coleccion",
         "04_Edad_Dorada_pack","05_Hogar_en_Calma_pack","06_Edad_Dorada_coleccion"]
os.makedirs('final/alta_resolucion', exist_ok=True); os.makedirs('final/carrusel_instagram', exist_ok=True)
thumbs=[]
for i,n in enumerate(names,1):
    im = Image.open(f'ia/up{i}.png').convert('RGB')
    # recorte exacto a 4:5
    w,h = im.size; tw = min(w, int(h*4/5)); th = int(tw*5/4)
    im = im.crop(((w-tw)//2,(h-th)//2,(w-tw)//2+tw,(h-th)//2+th))
    im.save(f'final/alta_resolucion/{n}.jpg', quality=95)
    c = im.resize((1080,1350), Image.LANCZOS); c.save(f'final/carrusel_instagram/{i:02d}_slide.jpg', quality=93)
    t = im.resize((360,450), Image.LANCZOS); thumbs.append(t)
sheet = Image.new('RGB',(360*6+70,450+40),'#efe6da')
for k,t in enumerate(thumbs): sheet.paste(t,(10+k*370,20))
sheet.save('final/vista_previa_carrusel.jpg', quality=90)
with zipfile.ZipFile('final/Carrusel_Tremdora.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir('final/carrusel_instagram')): z.write(f'final/carrusel_instagram/{f}', f)
with zipfile.ZipFile('final/Imagenes_Tremdora_alta_resolucion.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir('final/alta_resolucion')): z.write(f'final/alta_resolucion/{f}', f)
print('ok', im.size)
