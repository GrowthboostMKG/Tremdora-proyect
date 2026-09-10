# Email marketing — Secuencias evergreen tipo serie

Campañas de email marketing con estructura narrativa serializada ("formato Netflix")
para ebooks sobre comportamiento y bienestar de mascotas, apoyadas en investigación real
de neurociencia y psicología animal y humana.

## Temporadas

| Temporada | Tema | Estado | Emails |
|---|---|---|---|
| **T1** | Ansiedad por separación | ✅ Completa | 13 |
| T2 | Alimentación | 📋 Planificada | — |
| T3 | Cachorro / adopción | 📋 Planificada | — |
| T4 | Vejez | 📋 Planificada | — |
| T5 | Integrar una segunda mascota | 📋 Planificada | — |
| T6 | Paseo, ejercicio y reactividad | 📋 Planificada | — |

Las temporadas planificadas están mapeadas (protagonista, giro, científicos, episodio
humano) en `temporada-01-ansiedad-separacion/plantilla-otras-temporadas.md`.

## Temporada 1 — "El perro que llora cuando te vas"

30 días · 13 episodios · secuencia evergreen.

```
temporada-01-ansiedad-separacion/
├── 00-estrategia-y-calendario.md   Arco, personajes, calendario, segmentación, KPIs
├── emails/                          Copy completo de los 13 episodios
├── banco-de-asuntos.md              60+ asuntos, preheaders y reglas de A/B
├── fuentes-cientificas.md           Referencias reales + checklist de verificación
└── plantilla-otras-temporadas.md    El molde para replicarlo con los demás temas
```

**Empieza por `00-estrategia-y-calendario.md`.**

## Antes de publicar

1. Sustituye todos los `[PLACEHOLDERS]`: `[NOMBRE_EBOOK]`, `[ENLACE_EBOOK]`,
   `[ENLACE_BLOG]`, `[FIRMA]`, `[PRECIO]`, `[GARANTÍA]`, `[ENLACE_VOTO_1..5]`.
2. Recorre el checklist completo de `fuentes-cientificas.md`. Se citan científicos
   reales por su nombre: las atribuciones tienen que ser correctas.
3. Añade el aviso veterinario al pie de los 13 emails.
4. Verifica que no queda ninguna fecha absoluta en el copy (es evergreen).
