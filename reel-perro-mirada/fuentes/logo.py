import math,sys
from PIL import Image,ImageDraw,ImageFont,ImageChops
col=tuple(int(sys.argv[1][i:i+2],16) for i in (0,2,4))
SC=6;W,H=700*SC,330*SC
def heart(r,cx,cy):
    return [(cx+r*16*math.sin(t)**3, cy-r*(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))) for t in [i/4000*2*math.pi for i in range(4001)]]
m=Image.new('L',(W,H),0);d=ImageDraw.Draw(m)
cx,cy=W/2,105*SC
sw=7.5*SC
for (px,py) in heart(5.4*SC,cx,cy):
    d.ellipse((px-sw/2,py-sw/2,px+sw/2,py+sw/2),fill=255)
w=int(8*SC)
d.line([(cx-17*SC,cy+6*SC),(cx,cy+21*SC),(cx+17*SC,cy+6*SC)],fill=255,width=w)
for p in [(cx-17*SC,cy+6*SC),(cx,cy+21*SC),(cx+17*SC,cy+6*SC)]:
    d.ellipse((p[0]-w/2,p[1]-w/2,p[0]+w/2,p[1]+w/2),fill=255)
f=ImageFont.truetype('fonts/package/Poppins_500Medium.ttf',int(62*SC))
tr=24*SC;txt='TREMDORA'
tw=sum(f.getlength(c) for c in txt)+tr*(len(txt)-1)
x=cx-tw/2
for c in txt:
    d.text((x,262*SC),c,font=f,fill=255,anchor='lm'); x+=f.getlength(c)+tr
im=Image.new('RGBA',(W,H),col+(0,)); im.putalpha(m)
im=im.crop(m.getbbox()); im=im.resize((im.width//SC,im.height//SC),Image.LANCZOS)
im.save(sys.argv[2]);print(im.size)
