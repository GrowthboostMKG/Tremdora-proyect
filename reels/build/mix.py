import numpy as np, subprocess, os, sys
from scipy.io import wavfile
S=os.path.dirname(os.path.abspath(__file__)); SR=48000
def lufs(x):
    wavfile.write(S+"/_m.wav",SR,x.astype(np.float32))
    o=subprocess.run(["ffmpeg","-hide_banner","-i",S+"/_m.wav","-af","ebur128","-f","null","-"],capture_output=True,text=True).stderr
    return float(o.rsplit("I:",1)[1].split("LUFS")[0])
sr,v=wavfile.read(S+"/voice_pre.wav"); v=v.astype(np.float32); v/= (32768 if np.abs(v).max()>2 else 1)
m=np.load(S+"/music.npy"); fx=np.load(S+"/sfx.npy"); N=min(len(v),len(m)); v,m,fx=v[:N],m[:N],fx[:N]
v*=10**((-16-lufs(v))/20)
m*=10**((-29.5-lufs(m))/20)
# voice-activity envelope -> dynamic ducking of music
win=int(.05*SR); e=np.sqrt(np.convolve(v**2,np.ones(win)/win,'same')+1e-12)
act=(20*np.log10(e)>-42).astype(np.float32)
sm=np.zeros_like(act); a_up=1-np.exp(-1/(.08*SR)); a_dn=1-np.exp(-1/(.6*SR)); y=0
for i in range(0,N,48):
    t=act[i]; y+= (a_up if t>y else a_dn)*48*(t-y)/48*48 if False else ((a_up*48) if t>y else (a_dn*48))*(t-y)
    sm[i:i+48]=y
duck_db=-3.0*sm + 2.5*(1-sm)            # dip under words, lift in breaths/pauses
t=np.arange(N)/SR
arc=np.interp(t,[0,8,25,45,62,70.4,71,74.6,76,82,86,88.8],[0,0,.5,1,2,2,-.5,-.5,3.5,4,2,1])   # story arc (dB)
m*=10**((duck_db+arc)/20)
mix=v+m+fx
wavfile.write(S+"/mix_pre.wav",SR,mix.astype(np.float32))
print("voice",lufs(v),"music",lufs(m),"mix",lufs(mix))
