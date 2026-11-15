import sys,json
from faster_whisper import WhisperModel
m=WhisperModel(sys.argv[2],device='cpu',compute_type='int8')
import numpy as np,wave
w=wave.open(sys.argv[1]);a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
segs,_=m.transcribe(a,language='es',word_timestamps=True,beam_size=5)
out=[]
for s in segs:
    print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text}")
    out.append({'start':s.start,'end':s.end,'text':s.text,'words':[{'w':w.word,'s':w.start,'e':w.end} for w in s.words]})
json.dump(out,open(sys.argv[3],'w'),ensure_ascii=False,indent=1)
