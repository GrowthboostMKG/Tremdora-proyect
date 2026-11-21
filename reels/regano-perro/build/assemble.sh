#!/bin/bash
# Une imagen + etalonaje cálido + subtítulos + mezcla. uso: assemble.sh <picture.mp4> <subs.ass> <mix.wav> <salida.mp4>
set -e
PIC=$1; ASS=$2; MIX=$3; OUT=$4
# loudnorm en dos pasadas: -14 LUFS, pico real -1.5 dBTP (Instagram)
J=$(ffmpeg -hide_banner -i "$MIX" -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true"
ffmpeg -v error -y -i "$PIC" -i "$MIX" -filter_complex "\
[0:v]colorbalance=rs=.025:gs=.008:bs=-.035:rm=.02:gm=.005:bm=-.025:rh=.01:bh=-.015,\
eq=contrast=0.96:brightness=0.01:saturation=1.04:gamma=1.02,\
vignette=angle=PI/5.5,noise=alls=3:allf=t,\
ass='$ASS',fade=t=out:st=98.4:d=1.2[v];\
[1:a]$LN,aresample=48000[a]" -map "[v]" -map "[a]" \
 -c:v libx264 -preset slow -crf 19 -profile:v high -pix_fmt yuv420p -r 30 -movflags +faststart \
 -c:a aac -b:a 256k -ar 48000 -shortest "$OUT"
