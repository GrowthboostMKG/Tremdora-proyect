# Reel TREMDORA — «Regañó a su perro»

- `TREMDORA_reel_regano_perro.mp4`: Reel final 1080×1920, 30 fps, 99,6 s, H.264 + AAC, −14 LUFS, pico real −1,5 dBTP.
- `subtitulos.srt`: transcripción palabra por palabra, sincronizada con la voz (para subir como subtítulos aparte si se quiere).
- `montaje_planos.json`: lista de planos (inicio/fin, archivo de origen y frase que cubre).
- `build/`: scripts para volver a generarlo.
  - `shots.py`: montaje (orden, encuadre, zoom).
  - `render_video.py`: imagen. `make_subs.py`: subtítulos ASS. `make_music.py`: guitarra de nailon original.
  - `mix_audio.py`: mezcla voz + música con ducking. `assemble.sh`: etalonaje, subtítulos, loudness y exportación.
