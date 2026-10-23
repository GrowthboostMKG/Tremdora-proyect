#!/usr/bin/env bash
# Genera un reel vertical 1080x1920 a partir de las slides del carrusel.
# Uso: ./make_reel.sh [salida.mp4]
set -euo pipefail
cd "$(dirname "$0")"

OUT="${1:-reel.mp4}"
FPS=30
DUR=3.6      # segundos por slide
FADE=0.45    # duración de la transición
ZOOM=0.07    # zoom lento (Ken Burns) por slide

slides=(slides/*.png)
n=${#slides[@]}
frames=$(awk "BEGIN{print int($DUR*$FPS)}")

inputs=()
filters=""
for i in "${!slides[@]}"; do
  inputs+=(-i "${slides[$i]}")
  # delogo borra el contador "x/8" de la esquina superior derecha
  filters+="[$i:v]delogo=x=975:y=18:w=135:h=80,split[f$i][b$i];"
  # fondo: la misma imagen ampliada, desenfocada y algo oscurecida
  filters+="[b$i]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.06,setsar=1[bg$i];"
  # primer plano con zoom suave hacia el centro
  filters+="[f$i]scale=2160:-1,zoompan=z='1+$ZOOM*on/$frames':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=$frames:s=1080x1350:fps=$FPS,setsar=1[fg$i];"
  filters+="[bg$i][fg$i]overlay=0:(H-h)/2,fps=$FPS,format=yuv420p[v$i];"
done

prev="v0"
for ((i=1; i<n; i++)); do
  offset=$(awk "BEGIN{print $i*($DUR-$FADE)}")
  filters+="[$prev][v$i]xfade=transition=smoothleft:duration=$FADE:offset=$offset[x$i];"
  prev="x$i"
done
filters="${filters%;}"

ffmpeg -y "${inputs[@]}" -filter_complex "$filters" -map "[$prev]" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r "$FPS" -movflags +faststart "$OUT"
