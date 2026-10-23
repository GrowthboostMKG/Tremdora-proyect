# Inventario de PDF · todo lo listo para Shopify

Actualizado tras la revisión completa. **Nueve PDF listos para vender.**

---

## 1 · Hogar en Calma

| Archivo | Páginas | Peso | Portada |
|---|---|---|---|
| `Hogar-en-Calma-Tremdora.pdf` | 59 | 1,2 MB | `portadas/portada-Hogar-en-Calma.jpg` |
| `muestras/Hogar-en-Calma-MUESTRA-GRATIS.pdf` | 13 | 0,6 MB | `muestras/portada-muestra-Hogar-en-Calma.jpg` |

## 2 · Edad Dorada

| Archivo | Páginas | Peso | Portada |
|---|---|---|---|
| `Edad-Dorada-Tremdora.pdf` | 55 | 1,1 MB | `portadas/portada-Edad-Dorada.jpg` |
| `muestras/Edad-Dorada-MUESTRA-GRATIS.pdf` | 13 | 0,6 MB | `muestras/portada-muestra-Edad-Dorada.jpg` |

## 3 · Sigue Contigo — la serie del duelo, cinco piezas

| Archivo | Páginas | Peso | Portada |
|---|---|---|---|
| `sigue-contigo/pdf/0. Empieza por aqui.pdf` | 1 | 92 KB | `portada-1-Empieza-por-aqui.jpg` |
| `sigue-contigo/pdf/1. Sigue Contigo - eBook completo.pdf` | 43 | 467 KB | `portada-2-eBook-completo.jpg` |
| `sigue-contigo/pdf/2. Sigue Contigo - Diario del Oleaje.pdf` | 20 | 508 KB | `portada-3-Diario-del-Oleaje.jpg` |
| `sigue-contigo/pdf/3. Sigue Contigo - Plan Practico 8 Semanas.pdf` | 16 | 459 KB | `portada-4-Plan-Practico-8-Semanas.jpg` |
| `sigue-contigo/pdf/4. Sigue Contigo - Ellos Tambien se Despiden.pdf` | 21 | 495 KB | `portada-5-Ellos-Tambien-se-Despiden.jpg` |

Las portadas del pack están en `sigue-contigo/portadas/`.

---

## Comprobado en los nueve

- **Sin contraseña ni restricciones** de copia o impresión.
- **Texto seleccionable y buscable** (ninguno es imagen escaneada).
- **Ninguno pasa de 1,2 MB** — el límite de Shopify son 20 MB por archivo.
- **Marca Tremdora** y **`tremdora.com · @tremdora_pets`** dentro de los nueve.
- **Ninguna página desbordada:** el número de páginas del PDF coincide con el número
  de secciones del origen en los cuatro primeros, y el verificador de la serie da
  «sin desbordes» en los cinco de Sigue Contigo.

---

## Lo corregido en «Sigue Contigo» en esta pasada

El pack estaba **muy limpio de redacción**: ni un solo «sólo» con tilde, ni
«éste/ésta» acentuados, y el registro ya era de España. Tenía además bien resueltos
los avisos delicados («si necesitas hablar con un profesional», «si estás atravesando
un momento muy difícil»), que en un producto de duelo es lo primero que hay que mirar.

Lo que faltaba:

1. **No había página de autora en ninguna de las cinco piezas.** Ni «Victoria», ni
   «Paris», ni una firma. Ahora el eBook principal cierra con **«Diecisiete años con
   Paris»**, con la foto, escrita desde la despedida — que es de lo que va este pack:
   que se acompaña muy poco, que nadie te explica lo que viene, y que una despedida
   puede doler y ser a la vez un acto de amor.
2. **No había contacto en ninguna.** «tremdora» aparecía en minúscula y suelto.
   Ahora las cinco cierran con **TREMDORA · tremdora.com · @tremdora_pets**.
3. **«Empieza por aquí» no llevaba marca ninguna** — y es la primera página que abre
   quien compra. Ya la lleva.
4. **Dos castellanismos** en el libro cuarto: *caja de arena* → **arenero**, y
   *tapete de olfateo* → **alfombra olfativa**.
5. Al añadir el pie, la página 19 del Diario se desbordó 17 pt. Corregido y verificado.

---

## Una decisión que te queda a ti: el tamaño de página

Hay **dos formatos** en el catálogo:

| | Tamaño |
|---|---|
| Hogar en Calma y Edad Dorada (y sus muestras) | **A4** · 210 × 297 mm |
| Los cinco de Sigue Contigo | **165 × 240 mm** (formato libro) |

Los dos están bien, pero **no son el mismo**. Quien compre dos packs se encontrará
unos PDF con forma de libro y otros con forma de documento.

**Yo unificaría al formato de la serie (165 × 240 mm)**, por tres motivos: ya lo usan
cinco de los nueve archivos, se lee mucho mejor en móvil y en tablet, y es el formato
en el que se imprime un libro de verdad si algún día lo sacas en papel.

**Pero no lo he hecho por mi cuenta**, porque pasar 59 y 55 páginas de A4 a un papel
más pequeño rompe todos los saltos de página y obliga a rehacer entero el repaso de
desbordes de los dos libros y sus dos muestras. Es trabajo de una tarde y lo hago
cuando me lo digas — pero prefería no dejarte a medias algo que ahora mismo está
verificado página a página.

---

## Lo que sigue sin existir

De los tres packs, estas piezas están prometidas en la estrategia y **no existen
todavía**:

**Hogar en Calma** — Diario · Plan de 8 Semanas · Rutinas de Calma · Frecuencia
**Edad Dorada** — Diario de Bienestar Senior · Plan de 8 Semanas · Nutrición Dorada ·
20 Momentos · Cartas de Conexión · Ritual de 10 Minutos

Y hay un choque de nombres que conviene resolver antes de crearlas: **los tres packs
llevan un «Diario» y un «Plan Práctico de 8 Semanas»**. *Sigue Contigo* ya lo resolvió
bien llamando al suyo **«Diario del Oleaje»**. Los otros dos necesitan también nombre
propio, o quien compre dos packs tendrá cuatro archivos casi homónimos.

---

## Cómo regenerar

```
# Hogar en Calma, Edad Dorada y las dos muestras
python3 fuentes/muestra.py     # regenera el HTML de las muestras desde el completo
python3 fuentes/build.py       # genera los cuatro PDF

# Sigue Contigo
cd sigue-contigo && CHROME=/opt/pw-browsers/chromium ./build.sh
```
