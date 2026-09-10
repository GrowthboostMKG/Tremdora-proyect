# Serie «Sigue Contigo» — complementos

Tres cuadernos complementarios del eBook **Sigue Contigo** (57 págs.), construidos
con el mismo sistema editorial que se usó en *Edad Dorada* y *Hogar en Calma*.

| # | Libro | Págs. | Qué es |
|---|-------|-------|--------|
| 1 | **Sigue Contigo** — eBook completo | 42 | El libro principal, remaquetado al formato de la serie |
| 2 | **Diario del Oleaje** | 20 | Registro de 8 semanas: dos escalas y una frase por noche |
| 3 | **Plan Práctico de 8 Semanas** | 16 | 56 tareas, una por día, con los ejercicios del eBook repartidos |
| 4 | **Ellos También se Despiden** | 21 | Guía científica para acompañar a la mascota que se queda, con protocolo de 21 días |

## Base científica de los Libros 2 y 3 — el duelo humano

Cada ejercicio va anclado a la literatura que lo sostiene, y ambos libros cierran
con su página de fuentes.

- **Mary-Frances O'Connor** — neurociencia del duelo; el anhelo y el circuito de recompensa.
- **John Bowlby** y **Colin Murray Parkes** — apego, protesta y conducta de búsqueda.
- **Margaret Stroebe** y **Henk Schut** — modelo del vaivén (proceso dual, 1999); es el armazón de las 8 semanas y de las tres columnas del diario.
- **George Bonanno** — trayectorias de resiliencia; reír durante el duelo (con Keltner, 1997).
- **James Pennebaker** — escritura expresiva.
- **Matthew Lieberman** y **Naomi Eisenberger** — etiquetado afectivo; el dolor social en las vías del dolor físico.
- **Klass, Silverman y Nickman** — vínculos continuados (1996); y **Packman**, aplicado a la pérdida de mascotas.
- **Robert Neimeyer** — reconstrucción de significado. **Kristin Neff** — autocompasión.
- **Kenneth Doka** — duelo desautorizado. **Katherine Shear** — terapia de duelo complicado.
- Criterios de **trastorno de duelo prolongado** del DSM-5-TR (2022) y la CIE-11, con la salvedad explícita de que se escribieron para la muerte de personas.
- Se señala además que las cinco etapas de Kübler-Ross no describen el duelo (Maciejewski y cols., *JAMA*, 2007).

## Base científica del Libro 4 — el animal que se queda

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

## El pack para Shopify

```bash
./build.sh && python3 make_pack.py
```

Deja `dist/Sigue Contigo - Pack completo.zip` con una única carpeta raíz dentro,
nombres de archivo en ASCII (sin acentos ni ñ, para que Windows no los rompa) y
sin archivos ocultos:

```
Sigue Contigo - Pack completo/
├── 0. Empieza por aqui.pdf                       ·  1 pág  · portada del pack
├── 1. Sigue Contigo - eBook completo.pdf         · 42 págs
├── 2. Sigue Contigo - Diario del Oleaje.pdf      · 20 págs
├── 3. Sigue Contigo - Plan Practico 8 Semanas.pdf· 16 págs
└── 4. Sigue Contigo - Ellos Tambien se Despiden.pdf · 21 págs
```

### Añadir la frecuencia

Deja el audio en `assets/` con el nombre `5. Sigue Contigo - Frecuencia XXX Hz.mp3`
y vuelve a ejecutar `python3 make_pack.py`. El script lo detecta por extensión
(`.mp3`, `.wav`, `.m4a`, `.flac`, `.aac`, `.ogg`), lo mete en el ZIP y regenera la
página «Empieza por aquí» con su fila ya incluida — no hay que tocar nada más.

`assets/` guarda las piezas que no genera este repo. Ahora mismo está vacío: solo
espera la frecuencia.

## El eBook principal, remaquetado

El libro 1 venía en A5 (419×595 pt) desde otra herramienta, así que en el pack
convivían dos formatos. Se ha rehecho al trim de la serie **sin reescribir nada**:

1. `tools/parse_libro1.py` extrae el original en modo *layout* — que conserva
   sangrías y líneas en blanco — y lo convierte en 278 bloques tipados
   (capítulo, párrafo, cita centrada, lista, ejercicio, «por qué funciona»).
   El texto se copia literal; el parser solo decide qué es cada bloque.
2. `src/libro1_ebook.py` los viste con el sistema de la serie y los reparte en
   páginas **midiendo la altura real de cada bloque en Chromium**, de modo que
   ningún bloque se corta y los capítulos abren página.
3. `tools/verificar_libro1.py` compara los dos PDF como flujos de caracteres sin
   espacios — inmune a saltos de línea, partición de párrafos y al
   *letter-spacing* de los rótulos — y falla si falta algo:

```
original :  30485 caracteres
nuevo    :  30530 caracteres (45 añadidos por la nueva edición)
conserva :  30485  ->  100.000% del original
```

Los 45 caracteres añadidos son los números de página del índice, que el original
no tenía, y el rótulo «Sigue Contigo» de esa misma página. De 57 páginas A5 pasa
a 42 del formato de la serie.

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
src/pack_intro.py       portada del pack (se regenera según lo que haya)
src/libro2_diario.py    generadores de HTML (contenido + maquetación)
src/libro3_plan.py
src/libro4_ellos.py
assets/                 piezas que no genera este repo (eBook principal, frecuencia)
pdf/                    PDF generados
dist/                   el ZIP del pack
```
