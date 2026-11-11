import numpy as np, subprocess, wave, json
SR=44100
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i','vo.mp3','-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32)
segs=[(0.13,2.577),(8.600,12.085),(20.503,29.946),(35.923,50.932),(56.44,59.485),(68.522,83.604)]
pauses=[0.55,0.45,0.5,0.5,0.55]
lead,tail=0.10,0.9
fade=int(0.015*SR)
out=[np.zeros(int(lead*SR),np.float32)]; tl=[]; t=lead
for i,(a,b) in enumerate(segs):
    s=x[int((a-0.03)*SR):int((b+0.05)*SR)].copy()
    r=np.linspace(0,1,fade,dtype=np.float32); s[:fade]*=r; s[-fade:]*=r[::-1]
    tl.append(dict(orig=[a,b],new=[t,t+len(s)/SR])); out.append(s); t+=len(s)/SR
    gap=pauses[i] if i<len(pauses) else tail
    out.append(np.zeros(int(gap*SR),np.float32)); t+=gap
y=np.concatenate(out)
with wave.open('vo_cut.wav','wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(y,-1,1)*32767).astype('<i2').tobytes())
json.dump(tl,open('segments.json','w'),indent=1); print(round(len(y)/SR,2)); [print(s) for s in tl]
