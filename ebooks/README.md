# Serie «Sigue Contigo» — complementos

Tres cuadernos complementarios del eBook **Sigue Contigo** (57 págs.), construidos
con el mismo sistema editorial que se usó en *Edad Dorada* y *Hogar en Calma*.

| # | Libro | Págs. | Qué es |
|---|-------|-------|--------|
| 1 | *Sigue Contigo* — eBook completo | 57 | El libro principal (ya existente) |
| 2 | **Diario del Oleaje** | 16 | Registro de 8 semanas: dos escalas y una frase por noche |
| 3 | **Plan Práctico de 8 Semanas** | 14 | 56 tareas, una por día, con los ejercicios del eBook repartidos |
| 4 | **Ellos También se Despiden** | 21 | Guía científica para acompañar a la mascota que se queda, con protocolo de 21 días |

## Base científica del Libro 4

La cadena de disciplinas del cuarto libro sigue este recorrido, y cada capítulo
lleva el nombre del referente del que procede:

`Etología` → `Neurociencia afectiva` → `Cognición animal` → `Teoría del aprendizaje`
→ `Lenguaje corporal` → `Bienestar animal` → `Comportamiento clínico`
→ `Dolor y comportamiento` → `Envejecimiento cognitivo` → `Refuerzo positivo`

- **Konrad Lorenz** — el duelo animal documentado en gansos; el vínculo como sistema biológico.
- **Jaak Panksepp** — los siete sistemas emocionales; el circuito de PÁNICO / DUELO.
- **Alexandra Horowitz** — el *umwelt* olfativo; la regla del olor.
- **Brian Hare** — cognición social canina; tu estado emocional como parte de su entorno.
- **Iván Pávlov** — señales condicionadas en casa; recuperación espontánea.
- **B. F. Skinner** — extinción, estallido de extinción y refuerzo de la calma.
- **Margaret Gruen** — el cambio de conducta como primer signo de dolor.
- **Temple Grandin** — entorno predecible y activación del sistema de búsqueda.

## Sistema visual

Heredado de la serie: trim **468 × 679,92 pt**, tipografías serif (display) y sans
(texto), y la paleta cálida de la marca.

| Token | Valor | Uso |
|-------|-------|-----|
| `--ink` | `#3b2a20` | Texto |
| `--bg` / `--panel` / `--paper` | `#fbf3e6` / `#f6e9d6` / `#fdf8f0` | Fondos |
| `--line` | `#e2cfb4` | Filetes |
| `--green` / `--green-soft` | `#748156` / `#e6eada` | Acento salvia |
| `--terra` / `--terra-soft` | `#a8502e` / `#c1613a` | Acento terracota |

Gráficos en SVG inline: curva del oleaje, arco de las 8 semanas, donut de los
sistemas de Panksepp, curva de extinción, escala de receptores olfativos, mapa de
fases y semáforo de señales.

## Cómo reconstruir los PDF

```bash
./build.sh            # los tres libros
./build.sh libro4     # solo uno
```

Cada generador de `src/` escribe su HTML y `build.sh` lo imprime con Chromium
headless (`--print-to-pdf`), el mismo pipeline con el que se hicieron los libros
anteriores de la serie. Al terminar se ejecuta `check_overflow.py`, que abre el
HTML en Chromium y avisa si en alguna página el contenido se sale de la caja, a lo
alto o a lo ancho.

```
src/tremdora.css        sistema de estilos de la serie
src/libro2_diario.py    generadores de HTML (contenido + maquetación)
src/libro3_plan.py
src/libro4_ellos.py
pdf/                    salida lista para entregar
```
