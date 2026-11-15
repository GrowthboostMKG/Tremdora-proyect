import json
M=json.load(open('map.json'));T=M['tempo']
def nt(t):
    best=None
    for a,b,p in M['keep']:
        if a<=t<=b: return (p+t-a)/T
        if t<a: return p/T   # inside removed gap -> snap to next piece start
    a,b,p=M['keep'][-1]; return (p+b-a)/T
segs=json.load(open('trans.json'))
out=[]
for s in segs:
    ws=[{'w':w['w'].strip(),'s':round(nt(w['s']),3),'e':round(nt(w['e']),3)} for w in s['words']]
    out.append({'text':s['text'].strip(),'start':ws[0]['s'],'end':ws[-1]['e'],'words':ws})
    print(f"{ws[0]['s']:6.2f}-{ws[-1]['e']:6.2f} {s['text'].strip()}")
json.dump(out,open('trans_new.json','w'),ensure_ascii=False,indent=1)
