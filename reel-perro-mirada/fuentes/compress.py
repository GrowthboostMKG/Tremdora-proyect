import json,subprocess
TEMPO=1.08
v=[float(l.split()[1]) for l in open('sil.txt')]
sil=list(zip(v[0::2],v[1::2]))
segs=json.load(open('trans.json'))
END=70.1126
def ctx(s):
    # text segment ending just before silence start
    prev=[g for g in segs if g['end']<=s+0.15]
    return prev[-1]['text'].strip() if prev else ''
keep=[];cur=0.0;mapping=[]
for s,e in sil:
    if e>=END-0.01: # trailing
        keep.append((cur,s+0.05)); cur=None; break
    t=ctx(s)
    if 30<s<32: k=0.45
    elif t.endswith(('?','.','!')): k=0.32
    else: k=0.17
    d=e-s
    if d<=k: continue
    # keep head of silence k/2, tail k/2
    keep.append((cur,s+k/2)); cur=e-k/2
if cur is not None: keep.append((cur,END))
# build mapping orig->new
pos=0;m=[]
for a,b in keep: m.append((a,b,pos)); pos+=b-a
total=pos/TEMPO
json.dump({'keep':m,'tempo':TEMPO,'total':total},open('map.json','w'))
print('new length',round(total,2),'pieces',len(keep))
f=''.join(f"[0]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={b-a-0.012:.4f}:d=0.012[p{i}];" for i,(a,b) in enumerate(keep))
f+=''.join(f"[p{i}]" for i in range(len(keep)))+f"concat=n={len(keep)}:v=0:a=1,atempo={TEMPO},loudnorm=I=-15:TP=-1.5:LRA=9[out]"
subprocess.run(['ffmpeg','-v','error','-y','-i','audio/voz_original.mp3','-filter_complex',f,'-map','[out]','-ar','48000','audio/voz_edit.wav'],check=True)
