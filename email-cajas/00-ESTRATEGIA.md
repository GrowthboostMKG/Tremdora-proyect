# Secuencias de email — Caja de Navidad y Caja de Cumpleaños
### 12 de septiembre de 2026

---

# Por qué estas secuencias son el producto

**La caja de Navidad se vende por email con 0 € de publicidad.** No es un canal de apoyo: es *el*
canal. Si estos catorce emails no funcionan, no hay preventa — y sin preventa no hay dinero para
comprar el material, que es lo que sostiene todo el plan.

Así que esto no es marketing accesorio. **Es la caja registradora.**

---

# El tono, heredado de la temporada 01

He escrito estas secuencias en la misma voz que la serie de ansiedad por separación que ya tienes:
asuntos A/B con preheader, párrafos cortos, negritas en el momento que importa, y ningún emoji de
relleno ni «¡ÚLTIMAS HORAS!».

**Dos cosas cambian respecto a esa temporada, y a propósito:**

**① No hay «científico eje».** Un lanzamiento de una caja regalo no necesita a Pávlov. Meter
ciencia aquí sería pastiche. La autoridad de estos emails es otra: **están escritos por quien monta
las cajas a mano.**

**② El narrador eres tú, en primera persona.** En la temporada 01 la protagonista es Elena. Aquí
la protagonista eres tú, tus manos y tu mesa. Es lo único que un competidor no puede copiar, y es
justo lo que hace que alguien pague 49,90 € por una caja de 13 € de material.

---

# Las dos secuencias de un vistazo

| | **Navidad** | **Cumpleaños** |
|---|---|---|
| Tipo | Lanzamiento con fechas fijas | Evergreen, por disparador |
| Emails | 10 de venta + 4 post-compra | 4 + 1 anual |
| Cuándo | 12 oct – 30 nov | Todo el año |
| Se dispara con | La lista de espera | El diagnóstico y la fecha de compra |
| Archivo | `01-NAVIDAD.md` | `02-CUMPLEANOS.md` |

---

# La regla que no se salta en ninguno de los catorce

> ### En **todos** los emails de Navidad aparece la fecha de entrega. Sin excepción.
>
> *«Se envía del 12 al 16 de diciembre. La tienes en casa antes del 22.»*

Es una preventa: la fecha no es un dato secundario, es la mitad del producto. Y repetirla en cada
email es lo que hace que nadie compre creyendo que le llega mañana. **Un email sin esa línea es un
reembolso esperando a pasar.**

---

# Cómo se monta en Klaviyo

| Secuencia | Cómo | Dónde va |
|---|---|---|
| Navidad, emails N1–N10 | **Campañas programadas**, no flujo | Una por fecha, a la lista completa |
| Navidad, post-compra P1–P4 | **Flujo**, disparador «pedido realizado» | Filtrado por el producto de la caja |
| Cumpleaños C1–C3 | **Flujo**, disparador: etiqueta `problema:ninguno` | Del diagnóstico |
| Cumpleaños C4 | **Flujo** de carrito abandonado | 4 h y 24 h |
| Cumpleaños R1 | **Flujo** con espera de 11 meses desde la compra | El más rentable de todos |

La guía de montaje paso a paso está en la otra rama:
`netflix-email-sequence-pets-j3gnjx/email-marketing/temporada-01-ansiedad-separacion/klaviyo-montaje.md`

---

# Las variables que hay que rellenar antes

Búscalas y reemplázalas en los dos archivos:

| Variable | Qué es |
|---|---|
| `[URL]` | El enlace de la caja en tu tienda |
| `[N]` | Unidades reales de la edición. **Si haces 50, di 50** |
| `[QUEDAN]` | Las que queden de verdad el día del email N7 |
| `[NOMBRE_MASCOTA]` | Tu propia mascota, para los emails en primera persona |
