# Inventario de PDF · todo lo listo para Shopify

Actualizado tras la revisión completa. **Dieciocho PDF listos para vender.** Los tres packs, completos.

---

## 1 · Hogar en Calma · cinco piezas

| Archivo | Págs | Peso |
|---|---|---|
| `Hogar-en-Calma-Tremdora.pdf` — el método | 59 | 1,2 MB |
| `complementos/Hogar-en-Calma-2-Diario-de-la-Calma.pdf` | 18 | 0,6 MB |
| `complementos/Hogar-en-Calma-3-Plan-8-Semanas.pdf` | 13 | 0,5 MB |
| `complementos/Hogar-en-Calma-4-Rutinas-de-Calma.pdf` | 9 | 0,4 MB |
| `muestras/Hogar-en-Calma-MUESTRA-GRATIS.pdf` | 13 | 0,6 MB |

*Falta solo la Frecuencia, de la que se encarga la autora.*

## 2 · Edad Dorada · ocho piezas

| Archivo | Págs | Peso |
|---|---|---|
| `Edad-Dorada-Tremdora.pdf` — el método | 55 | 1,1 MB |
| `complementos/Edad-Dorada-2-Diario-de-los-Dias-Buenos.pdf` | 11 | 0,5 MB |
| `complementos/Edad-Dorada-3-Plan-8-Semanas.pdf` | 12 | 0,4 MB |
| `complementos/Edad-Dorada-4-Nutricion-Dorada.pdf` | 7 | 0,4 MB |
| `complementos/Edad-Dorada-5-20-Momentos.pdf` | 9 | 0,4 MB |
| `complementos/Edad-Dorada-6-Cartas-de-Conexion.pdf` | 10 | 0,3 MB |
| `complementos/Edad-Dorada-7-Ritual-de-10-Minutos.pdf` | 6 | 0,4 MB |
| `muestras/Edad-Dorada-MUESTRA-GRATIS.pdf` | 13 | 0,6 MB |

**Pack completo.** Las portadas de los complementos están en `complementos/portadas/`.

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

## El formato, unificado

**Los dieciocho PDF comparten ya la misma hoja: 468 × 679,92 pt (165 × 240 mm).** Es el
formato de libro que ya usaba *Sigue Contigo*, y ahora lo usan los tres packs.

Se eligió ese y no A4 por tres motivos: se lee mucho mejor en móvil y en tablet, que es
donde se van a leer; tiene menos margen muerto en proporción al texto; y es el formato
en el que se imprime un libro de verdad, por si algún día sale en papel.

**Cómo se hizo, por si algún día hay que tocarlo.** La maqueta estaba diseñada en A4 y
rehacer los saltos de página a mano habría obligado a repartir de nuevo 180 páginas, con
el riesgo de romper lo que ya estaba verificado. En vez de eso, la hoja pasa a
165 × 240 mm y **el contenido entero se escala al mismo factor que el ancho** (0,7857),
con lo que la composición se conserva exactamente y solo cambia el tamaño del papel. Está
en `fuentes/book.css`: `@page { size: 165mm 240mm }` y `body { zoom: 0.7857 }`, con las
cajas de página declaradas en 210 × 305,4 mm, que es lo que da 165 × 240 al escalar.

Verificado tras el cambio: **las secciones del origen siguen coincidiendo con las páginas
del PDF en los trece archivos**, así que no se perdió nada por el camino.

> **Si imprimes los diarios y los planes**, en el cuadro de impresión elige *ajustar a
> página* sobre A4: el papel se amplía un 27 % y las líneas de escritura quedan en unos
> 9 mm, que es el alto de un cuaderno normal.

---

## Dónde va la página de autora, y dónde no

Al principio la llevaban **catorce de los dieciocho**. Eso significaba que quien compra
el pack de Edad Dorada se leía la misma historia **ocho veces seguidas** — y una página
que emociona la primera vez, a la quinta es relleno.

**Página entera, solo donde se gana el sitio:**

| | Por qué |
|---|---|
| Los dos libros principales | Es el que todo el mundo abre, y donde la historia explica el método |
| Las dos muestras gratis | Es **la página de conversión**: quien la lee no tiene ninguna otra pieza |
| *Cartas de Conexión* | Ahí la página no es biografía, **es contenido**: «lo que más me duele no es haberla perdido, es lo que no recuerdo» es el argumento para hacer el ejercicio |
| *Sigue Contigo · eBook* | Igual que los otros principales |

**Firma breve en las ocho piezas restantes:** la foto en redondo, su nombre, «Fundadora
de Tremdora · por Paris», y una línea que remite al libro principal. Mantiene la
presencia humana sin repetir la historia, y le quita una página a cada complemento.

---

## Los nombres de los complementos

Los tres packs llevaban un «Diario» y un «Plan» casi homónimos. Resuelto:

| Pack | Diario | Plan |
|---|---|---|
| Hogar en Calma | **Diario de la Calma** | Plan de 8 Semanas |
| Edad Dorada | **Diario de los Días Buenos** | Plan de 8 Semanas |
| Sigue Contigo | Diario del Oleaje | Plan Práctico de 8 Semanas |

Las **25 menciones** de los dos libros principales están actualizadas.

---

## Una nota sobre «Nutrición Dorada»

Está escrita **a propósito como guía y no como recetario**, y conviene que sepas por qué.

Una dieta casera que sustituya al alimento completo es, salvo que la formule un
veterinario nutricionista, una dieta desequilibrada — y en un animal mayor con el riñón
o el hígado trabajando peor, eso hace daño de verdad. Un recetario habría sido la pieza
más vendible del pack y la única capaz de causarle un problema serio a un animal.

Así que la guía deja clarísimo desde la primera página que **la base es un alimento
completo**, y se centra en lo que sí aporta valor sin riesgo: los alimentos tóxicos (la
página que puede salvar una vida), las cuatro causas tratables de la pérdida de apetito,
la prueba de las costillas para el peso, la hidratación en gatos y la regla del 10 % para
premios y añadidos.

Si en algún momento quieres un recetario de verdad, hay una forma de hacerlo bien:
encargar las recetas a un **veterinario nutricionista** que las firme. Cuesta dinero y
es la única versión defendible.

## Cómo regenerar

```
# Hogar en Calma, Edad Dorada, muestras y complementos
python3 fuentes/complementos.py  # los cuatro diarios y planes
python3 fuentes/extras.py        # las cinco piezas extra
python3 fuentes/muestra.py       # regenera las muestras desde los libros completos
python3 fuentes/build.py         # genera los trece PDF

# Sigue Contigo
cd sigue-contigo && CHROME=/opt/pw-browsers/chromium ./build.sh
```
