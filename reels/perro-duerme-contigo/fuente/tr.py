import json,sys
from faster_whisper import WhisperModel
m=WhisperModel('medium',device='cpu',compute_type='int8',cpu_threads=4)
import numpy as np,subprocess
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',sys.argv[1],'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
segs,info=m.transcribe(a,language='es',word_timestamps=True,beam_size=5)
out=[]
for s in segs:
    print(f"[{s.start:.2f}-{s.end:.2f}] {s.text}",flush=True)
    out+= [dict(w=w.word,s=w.start,e=w.end) for w in s.words]
json.dump(out,open('words.json','w'),ensure_ascii=False,indent=0)
