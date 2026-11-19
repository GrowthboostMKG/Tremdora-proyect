import json,sys
from faster_whisper import WhisperModel
m=WhisperModel(sys.argv[2],device="cpu",compute_type="int8")
import numpy as np
segs,_=m.transcribe(np.fromfile(sys.argv[1],dtype=np.float32),language="es",word_timestamps=True,beam_size=5)
out=[]
for s in segs:
    print(f"[{s.start:.2f}-{s.end:.2f}] {s.text}",flush=True)
    out.append({"start":s.start,"end":s.end,"text":s.text,"words":[{"w":w.word,"s":w.start,"e":w.end} for w in s.words]})
json.dump(out,open("words.json","w"),ensure_ascii=False,indent=1)
