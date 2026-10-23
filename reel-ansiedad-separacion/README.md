# Reel: ansiedad por separación

`reel.mp4`: reel vertical 1080x1920, 30 fps, ~25 s, sin audio, generado a partir de las 8 slides del carrusel (`slides/`).

- Fondo desenfocado de la propia imagen + zoom lento sobre cada slide (3,6 s por slide).
- Transición tipo barrido entre slides.
- Se borra el contador "x/8" de la esquina.

Para regenerarlo (requiere ffmpeg): `./make_reel.sh reel.mp4`. Los tiempos se ajustan con `DUR`, `FADE` y `ZOOM` al principio del script.
