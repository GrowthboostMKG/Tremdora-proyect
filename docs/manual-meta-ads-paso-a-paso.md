# Manual Meta Ads paso a paso — Tremdora
### Para empezar de cero con 15 €/día y dos eBooks de 39,90 € y 49,90 €

> Fecha: 10 de septiembre de 2026
> Nivel: cero. Aquí no se da nada por sabido.
> Las cifras de coste (CPM, CPC, coste por lead) son **rangos de referencia del mercado español
> en el nicho mascotas**, no datos de tu cuenta. Tus números reales pueden salir un 30–50 %
> por encima o por debajo. En la Parte 7 se explica cómo sustituirlos por los tuyos.

---

# AVISO IMPORTANTE: tus precios cambian el plan anterior

En el documento anterior calculé todo suponiendo un eBook de **9,90 €**. Me dices que son
**39,90 €** y **49,90 €**. Eso es 4–5 veces más caro, y cambia tres cosas:

**Lo bueno:** cada venta deja ~38 € de margen (el coste de un producto digital es casi cero).
Puedes permitirte pagar hasta 15 € por conseguir un cliente y seguir ganando dinero. Con 9,90 €
no podías pagar ni 6 €.

**Lo malo:** un eBook de 39,90 € **no se vende bien a puerta fría.** Nadie que no te conoce paga
40 € por un PDF tras ver un vídeo de 20 segundos. La tasa de conversión cae de ~2,5 % a ~1 %.

**Las cuentas reales con 15 €/día y venta directa en frío:**

| Concepto | Cálculo | Resultado |
|---|---|---|
| Impresiones al día | 15 € ÷ 8 € CPM × 1.000 | ~1.900 |
| Clics al día | 1.900 × 1,5 % CTR | ~28 |
| Ventas al día | 28 × 1 % de conversión | ~0,3 → **1 venta cada 3–4 días** |
| Ventas al mes | | 8–10 |
| Ingresos al mes | 9 × 39,90 € | ~360 € |
| Gasto en ads al mes | 15 € × 30 | **450 €** |
| **Resultado** | | **–90 €** |

Con 15 €/día y venta directa en frío, lo más probable es que pierdas dinero los primeros meses.
No es un fallo tuyo: es que **15 €/día es presupuesto de aprendizaje, no de escalado**, y un
producto de 40 € necesita confianza previa.

## La corrección: vende gratis primero, cobra después

En vez de pedir 39,90 € a un desconocido, le pides su email a cambio de una **mini-guía gratis**.
Después le vendes el libro por email, cuando ya te conoce.

```
Anuncio  →  Mini-guía GRATIS (pide email)  →  6 emails en 10 días  →  Venta del libro 39,90 €
```

| Concepto | Venta directa | Mini-guía + email |
|---|---|---|
| Coste por conseguir un email | — | 1,00–2,00 € |
| Emails al mes con 15 €/día | — | **250–450** |
| Ventas al mes | 8–10 | 8–18 |
| **Lista de email al cabo de 6 meses** | ~55 personas | **~2.000 personas** |
| A quién le vendes el libro de octubre | Vuelves a pagar ads | Gratis, a tu lista |
| Quién compra la caja de Navidad | Desconocidos | Tu lista |

**Esa lista es todo el negocio que me describiste.** Es lo que hace que el libro de cada mes no
cueste dinero en publicidad, y es lo que vacía la caja de Navidad en preventa sin gastar en ads.

**Y hay una razón técnica igual de importante:** Facebook necesita unos **50 resultados por semana**
para aprender a quién enseñar tu anuncio (esto se llama *fase de aprendizaje*, ver glosario).
Con venta directa consigues 2–3 ventas por semana → el algoritmo nunca aprende y tus anuncios
rinden mal para siempre. Con emails consigues 60–100 por semana → **sí aprende**. Es la diferencia
entre una cuenta que funciona y una que no.

## Reparto recomendado de tus 15 €/día

| Semanas | A por emails | A venta directa | Anuncios activos |
|---|---|---|---|
| 1–3 | 15 €/día | 0 € | 3 |
| 4 en adelante | 10 €/día | 5 €/día (retargeting) | 3 + 2 |

> **Corrección de lo que te dije antes:** con 15 €/día no pongas 6 anuncios, pon **3**.
> Antes hablábamos de un producto barato con muchas conversiones; con uno de 40 € las
> conversiones son más raras y cada anuncio necesita más presupuesto para poder juzgarlo.
> Menos presupuesto ⇒ menos anuncios, no más.

---

# PARTE 0 — Glosario: todo lo que no entendías

Léelo entero una vez. Sin esto, el resto no se entiende.

| Término | Qué es, en cristiano |
|---|---|
| **Administrador de anuncios** | La web donde se crean y controlan los anuncios: `adsmanager.facebook.com`. Es tu panel de mando. |
| **Campaña** | El nivel de arriba. Aquí eliges **el objetivo**: ¿quiero ventas? ¿quiero emails? Nada más. |
| **Conjunto de anuncios** | El nivel de en medio. Aquí eliges **a quién, dónde y cuánto dinero**: el público, los países, el presupuesto diario. |
| **Anuncio** | El nivel de abajo. Es **el vídeo o la imagen concreta** con su texto. |
| **Impresión** | Una vez que tu anuncio aparece en la pantalla de alguien. 1.500 impresiones = se mostró 1.500 veces (a menos personas, porque se repite). |
| **Alcance** | Personas distintas que lo vieron. Siempre menor que las impresiones. |
| **CPM** | Lo que te cuesta que se muestre 1.000 veces. En España, mascotas: **6–10 €**. |
| **Clic en el enlace** | Alguien pulsó y fue a tu web. |
| **CTR (enlace)** | De cada 100 personas que lo vieron, cuántas pulsaron. **Por encima de 1,2 % está bien.** |
| **CPC** | Lo que te cuesta cada clic. **Por debajo de 0,60 € está bien.** |
| **Píxel** (hoy Meta lo llama *conjunto de datos*) | Un trocito de código que se pega en tu web. Es **el chivato**: le cuenta a Facebook lo que hace la gente en tu tienda. Sin él, Facebook está ciego y no puede optimizar nada. Es lo primero que hay que instalar. |
| **Evento** | Cada acción que el chivato reporta. Los que importan: **ViewContent** (vio el producto), **AddToCart** (lo metió al carrito), **InitiateCheckout** (empezó a pagar), **Purchase** (compró), **Lead** (te dejó su email). |
| **"1.000 eventos de píxel en 30 días"** | No son 1.000 €, son **1.000 acciones registradas** por el chivato en los últimos 30 días. Es el umbral a partir del cual tienes suficiente gente "fichada" como para hacer retargeting. |
| **Retargeting** *(lo que escribiste como "Wretched")* | Volver a enseñar anuncios **solo a quien ya visitó tu web** y no compró. Es la publicidad más barata que existe, pero necesita que ya haya pasado gente por tu web. Por eso no se hace el primer día. |
| **Fase de aprendizaje** | Los primeros 3–7 días de un conjunto. Facebook está probando a quién enseñárselo. Los resultados son malos e inestables. **Si tocas algo, vuelve a empezar de cero.** No toques nada. |
| **Ángulo** | El *motivo* por el que alguien debería comprar. No el diseño: el argumento. Ver Parte 2. |
| **Creativo** | El vídeo o la imagen en sí. |
| **Público amplio** | No elegir intereses. Le dices a Facebook "España, 25–65" y que él busque. Con presupuesto pequeño funciona mejor que elegir intereses a mano. |
| **CPA / Coste por resultado** | Lo que te cuesta cada venta (o cada email). Es **la métrica que manda**. |
| **AOV / Ticket medio** | Lo que gasta de media cada comprador. |
| **ROAS** | Euros que ingresas por cada euro gastado en ads. ROAS 3 = ingresas 3 € por cada 1 € invertido. |
| **Frecuencia** | Cuántas veces de media ha visto la misma persona tu anuncio. **Por encima de 2,5 la gente se satura.** |
| **Hook rate** | De los que vieron el vídeo, cuántos aguantaron 3 segundos. **Por encima del 25 % está bien.** Mide si tu primer segundo funciona. |

---

# PARTE 1 — Antes de tocar un anuncio (1 día de trabajo)

**No lances nada hasta terminar esta parte.** Si lanzas sin píxel, tiras el dinero: Facebook no
sabrá quién compra y no podrá buscarte más gente parecida.

### Paso 1.1 — Crea la cuenta de empresa
1. Entra en `business.facebook.com` con tu cuenta personal de Facebook.
2. **Crear cuenta** → nombre "Tremdora", tu nombre, tu email.
3. Dentro: **Configuración del negocio** → **Cuentas** → **Cuentas publicitarias** → **Añadir** → **Crear una cuenta publicitaria nueva**. Moneda: **EUR**. Zona horaria: **Europa/Madrid**.
   > ⚠️ La zona horaria **no se puede cambiar nunca más**. Si la pones mal, todos tus informes diarios estarán desfasados para siempre.
4. **Configuración del negocio** → **Pagos** → añade tu tarjeta.

### Paso 1.2 — Instala el píxel en tu tienda
1. `business.facebook.com` → menú → **Administrador de eventos**.
2. **Conectar orígenes de datos** → **Web** → **Conectar**.
3. Ponle nombre: `Pixel Tremdora`. Copia el **ID del píxel** (un número largo) en una nota.
4. Si tu tienda es **Shopify**: Shopify → **Apps** → busca **Facebook & Instagram** → instálala →
   sigue el asistente → conecta tu cuenta de empresa → elige el píxel `Pixel Tremdora`.
   Shopify enviará solos los eventos ViewContent, AddToCart, InitiateCheckout y Purchase.
5. Si es otra plataforma: en el Administrador de eventos elige **Instalar código manualmente**,
   copia el bloque y pégalo en el `<head>` de todas las páginas.

### Paso 1.3 — Verifica tu dominio
Administrador de eventos → **Configuración del origen de datos** → **Verificar dominio** →
elige **Metaetiqueta HTML** → pega la etiqueta en el `<head>` de tu web → **Verificar**.

Sin esto, Apple bloquea buena parte de tus datos y verás menos conversiones de las reales.

### Paso 1.4 — Ordena tus eventos por prioridad
Administrador de eventos → **Configuración total de eventos** → tu dominio → **Administrar eventos**.
Ordénalos así, de arriba abajo:

```
1. Purchase        (compra)
2. InitiateCheckout (empezó a pagar)
3. Lead            (te dejó el email)   ← imprescindible para el plan de la mini-guía
4. AddToCart       (añadió al carrito)
5. ViewContent     (vio el producto)
```

### Paso 1.5 — Comprueba que el chivato funciona (no te saltes esto)
1. Instala en Chrome la extensión **Meta Pixel Helper**.
2. Abre tu web. El icono debe ponerse azul con el número de eventos.
3. Añade un producto al carrito. El Pixel Helper debe mostrar **AddToCart**.
4. También: Administrador de eventos → pestaña **Probar eventos** → pega la URL de tu tienda →
   navega y comprueba que los eventos van apareciendo en tiempo real.

**Si aquí no ves eventos, para. No sigas. Arregla esto primero.** Todo lo demás depende de ello.

### Paso 1.6 — Pon el candado del gasto (esto es lo que te protege)
Administrador de anuncios → arriba a la derecha, el menú ☰ → **Facturación y pagos** →
**Configuración de pagos** → **Límite de gasto de la cuenta** → **Establecer límite** →
escribe **450 €**.

**Qué hace esto:** cuando la cuenta llegue a 450 € gastados en total, Facebook **apaga todos tus
anuncios automáticamente**. Es un tope duro que ninguna configuración puede saltarse. Es tu red
de seguridad contra un error de configuración que te vacíe la tarjeta.

Cada mes, cuando quieras seguir, entras y lo subes en otros 450 €.

---

# PARTE 2 — "Tres ángulos por dos libros": qué significa y cómo se hace

## Qué es un ángulo

Un ángulo **no es un diseño distinto, es un argumento distinto**. Es la razón por la que alguien
debería pararse a mirar.

Estos **NO** son 3 ángulos, son 1 ángulo con 3 maquetaciones:
- ❌ El mismo vídeo con música alegre / con música triste / sin música
- ❌ La misma foto en azul / en verde / en naranja

Estos **SÍ** son 3 ángulos:
- ✅ **Miedo:** "Tu perro no está triste cuando te vas. Está en pánico."
- ✅ **Error:** "Los 4 errores que hacen que tu perro llore cuando sales de casa."
- ✅ **Prueba:** "Marta lo intentó todo durante 2 años. Esto lo arregló en 11 días."

Se prueban ángulos distintos porque **no sabes cuál va a funcionar**. Ninguno lo sabe. El anuncio
que a ti te parece el mejor casi nunca es el que gana. Por eso se prueban varios y se deja que
el dinero decida.

## Los 6 ángulos de Tremdora (3 por libro)

> ⚠️ No me has dicho de qué van tus dos libros. He usado dos temas de ejemplo. **Sustituye el tema
> por el tuyo real** y quédate con la estructura de los tres ángulos, que sí es transferible.

### LIBRO A (39,90 €) — ejemplo: *ansiedad por separación*

| # | Ángulo | Gancho (primeros 3 segundos) |
|---|---|---|
| A1 | **Miedo / dolor** | "Si tu perro llora cuando te vas, no te echa de menos. Está teniendo un ataque de pánico." |
| A2 | **Los errores** | "Estos 3 gestos que haces al salir de casa son los que empeoran a tu perro." |
| A3 | **Prueba social** | "Llevaba 2 años sin poder ir a comprar. Mira cómo está ahora." |

### LIBRO B (49,90 €) — ejemplo: *tirar de la correa*

| # | Ángulo | Gancho (primeros 3 segundos) |
|---|---|---|
| B1 | **Miedo / dolor** | "Tu perro no tira porque sea desobediente. Tira porque le has enseñado a tirar sin querer." |
| B2 | **Los errores** | "Tirar de la correa hacia atrás. Ese es el error. Y lo hacemos todos." |
| B3 | **Prueba social** | "Antes no podía ni sacarlo solo. Este es el paseo de ayer." |

## Cuáles lanzas primero

Con 15 €/día **no lanzas los 6**. Cada anuncio necesita presupuesto para poder juzgarlo, y
15 € entre 6 anuncios son 2,50 € por anuncio: no da para nada.

**La regla "un ángulo nuevo por cada 5 €/día"** significa exactamente eso:

| Tu presupuesto | Ángulos que puedes juzgar |
|---|---|
| 15 €/día | **3** |
| 25 €/día | 5 |
| 40 €/día | 8 |

**Semana 1 lanzas 3 anuncios:** A1, B1 y A2 (o B2 — elige el tema que más te convenza).
Los otros tres entran más adelante, sustituyendo a los que vayan muriendo.

---

# PARTE 3 — "Compiten en el mismo conjunto": cómo se hace, clic a clic

## Qué significa

Un conjunto de anuncios es una bolsa de dinero. Cuando metes 3 anuncios dentro de **la misma**
bolsa, Facebook prueba los tres durante unas horas y luego **empieza a dar casi todo el dinero
al que mejor funciona**. Lo hace solo, sin que tú toques nada.

```
✅ ASÍ (correcto: compiten)          ❌ ASÍ NO (se reparten a ciegas)

Conjunto único — 15 €/día            Conjunto 1 — 5 €/día → Anuncio A1
├── Anuncio A1  ┐                    Conjunto 2 — 5 €/día → Anuncio B1
├── Anuncio B1  ├─ Facebook          Conjunto 3 — 5 €/día → Anuncio A2
└── Anuncio A2  ┘  reparte solo
```

**Por qué el de la derecha está mal:** cada bolsa de 5 €/día tiene tan poco dinero que Facebook
no aprende en ninguna. Y tú fuerzas que el peor anuncio se lleve 5 € igual que el mejor. Estás
apostando 1/3 de tu dinero a cada caballo antes de saber cuál corre.

**Por qué el de la izquierda está bien:** un solo cerebro con 15 € decide. En 3 días el ganador
se lleva 11 € y los perdedores 2 € cada uno. **Y de paso te dice cuál de tus dos libros interesa
más al mercado, sin que tengas que adivinarlo.** Eso es exactamente lo que querías: abrir dos
temas sin duplicar la inversión.

## Cómo se hace en la práctica

No hay ningún botón de "hacer que compitan". Ocurre solo por el hecho de estar en el mismo
conjunto. Lo único que tienes que hacer es **crear un conjunto y meter dentro los 3 anuncios**,
en vez de crear 3 conjuntos. Los pasos exactos vienen en la Parte 4.

---

# PARTE 4 — Cómo grabar los vídeos, paso a paso

## 4.1 Lo que necesitas

| | |
|---|---|
| Cámara | **Tu móvil.** No compres nada. Los vídeos de móvil rinden mejor que los de productora. |
| Luz | Una ventana. Ponte **de cara** a ella, nunca de espaldas. |
| Sonido | Grábate en una habitación con alfombra/sofá (menos eco). Sin música de fondo mientras hablas. |
| Edición | **CapCut** (gratis, móvil y ordenador). |
| Duración | **20–30 segundos.** Ni uno más. |
| Formato | **Vertical 9:16, 1080 × 1920 px.** |

## 4.2 La estructura obligatoria (los 5 bloques)

Todos tus vídeos llevan estos 5 bloques, siempre en este orden y con estos tiempos:

| Bloque | Tiempo | Qué va aquí |
|---|---|---|
| **1. GANCHO** | 0–3 s | Una sola frase que le duela a quien tiene ese problema. Sin saludos, sin "hola soy", sin logo. |
| **2. PROBLEMA** | 3–8 s | Describes su día a día con tal precisión que piensa "me está describiendo a mí". |
| **3. GIRO** | 8–15 s | "El problema no es lo que crees, es esto otro." Aquí es donde deja de irse. |
| **4. SOLUCIÓN** | 15–25 s | Nombras la guía y dices **qué se lleva**, concreto y en días. |
| **5. LLAMADA** | 25–30 s | Una sola orden clara. "Toca en el enlace y descárgate el primer capítulo gratis." |

**El bloque 1 se lleva el 80 % del resultado.** Si el gancho falla, los otros 25 segundos no
existen porque nadie los ve.

## 4.3 Guion completo — Anuncio A1 (miedo)

```
[0-3 s]  A cámara, primer plano, tú.
         "Si tu perro llora cuando te vas de casa,
          no te está echando de menos."

[3-8 s]  Corte. Plano del perro en la puerta / rascando.
         "Le está dando un ataque de pánico.
          Y cada vez que vuelves y le riñes, va a peor."

[8-15 s] Vuelta a cámara.
         "Esto no se arregla cansándolo antes de salir.
          Ni dejándole la tele puesta. Yo probé las dos.
          Se arregla cambiando los 90 segundos ANTES de coger las llaves."

[15-25 s] Plano de la guía en una tablet o impresa.
         "Está todo en esta guía: el protocolo día a día,
          14 días, 10 minutos al día. Sin gritos y sin jaula."

[25-30 s] A cámara, mirando fijo.
         "Toca el enlace. El primer capítulo te lo llevas gratis."
```

## 4.4 Guion completo — Anuncio A2 (los errores)

```
[0-3 s]  Rótulo grande en pantalla + tu voz.
         "3 cosas que haces al salir de casa
          y que están empeorando a tu perro."

[3-10 s] Corte rápido por cada error, rótulo numerado.
         "Uno: despedirte. Dos: montar el drama al volver.
          Tres: dejarle un juguete nuevo justo al salir."

[10-18 s] A cámara.
         "Los tres le dicen lo mismo a su cabeza:
          que irte es un acontecimiento. Y por eso lo vigila."

[18-26 s] Plano de la guía.
         "En la guía tienes los 3 corregidos, con el paso a paso
          de 14 días para que salir de casa le dé exactamente igual."

[26-30 s] "Enlace abajo. El primer capítulo es gratis."
```

## 4.5 Guion completo — Anuncio B1 (miedo, libro 2)

```
[0-3 s]  Plano real de un perro tirando de la correa. Tu voz encima.
         "Tu perro no tira porque sea desobediente."

[3-9 s]  Corte a cámara.
         "Tira porque le hemos enseñado a tirar. Sin querer.
          Cada vez que tiras tú de la correa hacia atrás,
          le confirmas que así se avanza."

[9-17 s] Plano del paseo bien hecho.
         "Se arregla en el minuto uno del paseo, no en la clase de los sábados."

[17-26 s] Plano de la guía.
         "Aquí tienes el método completo: 21 días,
          15 minutos al día, sin collares de castigo."

[26-30 s] "Enlace abajo. Primer capítulo gratis."
```

## 4.6 Cómo grabarlo (rutina de una tarde)

1. **Escribe el guion en el móvil** y ponlo justo debajo de la cámara para leerlo sin bajar la vista.
2. **Graba cada bloque por separado.** No intentes hacer los 30 segundos de una toma.
3. **Graba 3 tomas de cada bloque.** La tercera siempre sale mejor.
4. **Graba el gancho 5 veces**, cambiando la entonación. Es el que más importa.
5. **Graba también "planos de recurso"**: el perro, la correa, la puerta, tus manos con la tablet.
   Sirven para tapar cortes y para que el vídeo no sea una cara hablando 30 segundos.
6. En una tarde tienes material para los 3 anuncios. Hazlo todo el mismo día.

## 4.7 Cómo editarlo en CapCut

1. **Nuevo proyecto** → importa tus clips.
2. Arriba a la derecha, **Relación de aspecto → 9:16**.
3. Monta los bloques en orden. **Corta todos los silencios**: el vídeo tiene que ir apretado.
4. **Subtítulos:** menú **Texto** → **Subtítulos automáticos** → español → **Generar**.
   Luego revísalos uno a uno, porque se equivocan.
   > El **85 % de la gente ve los vídeos sin sonido.** Un vídeo sin subtítulos es un vídeo que
   > no se entiende. Esto no es opcional.
5. Subtítulos: letra grande, blanca, con borde negro, colocados **en el tercio central**,
   nunca abajo del todo (Instagram tapa la parte inferior con su interfaz).
6. **Música:** solo de fondo y muy baja, o ninguna. Nunca por encima de tu voz.
7. **Exportar:** 1080p, 30 fps. **Desactiva la marca de agua de CapCut**
   (Ajustes → quitar marca final).

## 4.8 Lo que NO debes hacer

- ❌ Empezar con tu logo. Pierdes al 40 % en el primer segundo.
- ❌ Empezar con "Hola, soy X de Tremdora". A nadie le importa todavía quién eres.
- ❌ Vídeos horizontales o cuadrados.
- ❌ Vídeos de más de 35 segundos.
- ❌ Vídeos sin subtítulos.
- ❌ Decir el precio en el vídeo. El precio se dice en la web, no en el anuncio.
- ❌ Poner los 3 ángulos en un mismo vídeo. Un vídeo, una idea.

---

# PARTE 5 — Montar la campaña, clic a clic

Entra en `adsmanager.facebook.com` y pulsa el botón verde **+ Crear**.

## Nivel 1 — CAMPAÑA

| Campo | Qué eliges |
|---|---|
| Objetivo | **Clientes potenciales** (si haces la mini-guía) o **Ventas** (si vendes directo) |
| Configuración de la campaña | **Manual**, no "Advantage+ compras" |
| Nombre | `TR - Leads - Sep26` |
| Prueba A/B | **Desactivada** |
| Presupuesto Advantage para campañas | **DESACTIVADO** ← importante, el presupuesto lo pones abajo |
| Categoría especial de anuncios | **Ninguna** |

Pulsa **Siguiente**.

## Nivel 2 — CONJUNTO DE ANUNCIOS (aquí va el dinero y el público)

| Campo | Qué eliges |
|---|---|
| Nombre | `Amplio - ES - 25-65` |
| Ubicación de conversión | **Sitio web** |
| Conjunto de datos (píxel) | `Pixel Tremdora` |
| Evento de conversión | **Lead** (o **Purchase** si vendes directo) |
| **Presupuesto diario** | **15,00 €** ← **el único sitio donde se pone el dinero** |
| Programación | **Fecha de inicio: mañana, 00:00.** Sin fecha de fin. |
| Ubicación (público) | **España** |
| Edad | **25 – 65+** |
| Sexo | **Todos** |
| Público objetivo Advantage+ | **Activado** (esto es el "público amplio": no metas intereses) |
| Ubicaciones (dónde se muestra) | **Ubicaciones Advantage+ / automáticas** |

Pulsa **Siguiente**.

> ⚠️ **Solo creas UN conjunto.** No pulses "duplicar conjunto". Aquí es donde la gente se
> equivoca y acaba con 3 bolsas de 5 €.

## Nivel 3 — ANUNCIO (y aquí es donde metes los 3)

Para el **primer** anuncio:

| Campo | Qué eliges |
|---|---|
| Nombre | `A1 - Miedo - video` |
| Identidad | Tu página de Facebook + tu cuenta de Instagram |
| Formato | **Una sola imagen o vídeo** |
| Contenido | Sube tu vídeo A1 |
| Texto principal | El texto largo (ver plantilla abajo) |
| Titular | `La guía de 14 días para la ansiedad por separación` |
| Descripción | `Descarga gratis el primer capítulo` |
| Destino | **Sitio web** → la URL de tu landing |
| Llamada a la acción | **Más información** |

**Ahora la parte importante — añadir los otros dos anuncios dentro del MISMO conjunto:**

1. En la columna izquierda verás el árbol: Campaña → Conjunto → Anuncio.
2. Haz **clic derecho sobre el anuncio** que acabas de crear → **Duplicar**.
3. En la ventana que sale, en "Duplicar en", asegúrate de que dice **el mismo conjunto de
   anuncios**, no uno nuevo. → **Duplicar**.
4. Ahora cambia en la copia: el nombre a `B1 - Miedo - video`, sube el vídeo B1, cambia el
   texto, el titular y la URL de destino (la de tu otro libro).
5. Repite para el tercero, `A2 - Errores - video`.

**Resultado final del árbol izquierdo — compruébalo antes de publicar:**

```
📁 TR - Leads - Sep26                    (campaña)
  └── 📁 Amplio - ES - 25-65   15 €/día  (UN conjunto)
        ├── 📄 A1 - Miedo - video
        ├── 📄 B1 - Miedo - video
        └── 📄 A2 - Errores - video
```

Si ves más de una carpeta de conjunto, lo has hecho mal. Bórralas y déjalo así.

Pulsa **Publicar**.

## Plantilla de texto principal

```
¿Tu perro llora, araña la puerta o destroza cosas cada vez que te vas?

No es que te eche de menos. Es ansiedad por separación,
y no se arregla cansándolo antes de salir.

Dentro de la guía:
· El protocolo de 14 días, día por día
· Los 3 errores que casi todos cometemos al salir de casa
· Qué hacer las 2 primeras semanas si vives en piso
· Sin gritos, sin jaula, sin collares

Descarga gratis el primer capítulo 👇
```

---

# PARTE 6 — Controlar el gasto: que no pase de 15 €/día

Esto necesita que entiendas una cosa que a todo el mundo le pilla por sorpresa:

> **Facebook NO gasta exactamente 15 € cada día.** Puede gastar hasta un **25 % más** en un día
> bueno (18,75 €) y compensarlo gastando menos en otro. Lo que sí garantiza es el promedio:
> **en 7 días no gastará más de 7 × 15 € = 105 €.**

Esto es normal y no es un error. Si el día 3 ves 18,20 € gastados, **no toques nada.**

## Las tres capas de protección

**Capa 1 — El presupuesto diario del conjunto: 15 €**
Es el que ya has puesto. Controla el ritmo, con el margen del ±25 %.

**Capa 2 — Límite de gasto de la campaña**
Administrador de anuncios → marca la campaña → **Editar** → abajo, **Límite de gasto de la
campaña** → **450 €**. Cuando la campaña llegue ahí, se apaga sola.

**Capa 3 — Límite de gasto de la cuenta: 450 € (el candado de verdad)**
El que pusiste en el Paso 1.6. Este apaga **todo**, pase lo que pase. Es el que te salva si
un día duplicas una campaña sin querer.

## Una cuarta protección que casi nadie configura

Menú ☰ → **Facturación** → **Umbral de facturación**. Facebook te cobra cada vez que acumulas
X €. Al principio empieza bajo (25 €) y **lo va subiendo solo** hasta 750 € o más.
**Bájalo a mano a 50 €.** Así te cobra a menudo y en importes pequeños, y detectas cualquier
gasto raro en 2–3 días, no a final de mes.

## Revisión de gasto: 30 segundos al día

Administrador de anuncios → arriba, el selector de fechas → **Hoy**. Mira la columna
**Importe gastado**. A las 23:00 debe rondar los 15 €.

| Lo que ves | Qué significa | Qué haces |
|---|---|---|
| 14–19 € | Normal, incluido el margen del 25 % | Nada |
| 25 € o más | Hay más de una campaña activa | Ve a la lista de campañas y apaga las que no toquen |
| 3–6 € | Facebook no encuentra a quién enseñárselo | Ver Parte 8, "gasto insuficiente" |
| 0 € | Anuncio rechazado o tarjeta fallando | Mira la columna **Entrega**: te dirá el motivo |

---

# PARTE 7 — A qué hora y qué día lanzar

## La hora: programa el inicio a las 00:00

**No pulses "publicar" a las 8 de la tarde.** Si lo haces, Facebook intenta gastar los 15 €
en las 4 horas que quedan de día. Para conseguirlo puja mucho más caro, y tu primer día —
justo el que más pesa en el aprendizaje del algoritmo — sale carísimo y con datos malos.

**Lo correcto:** en el conjunto de anuncios, en **Programación**, pon **fecha de inicio mañana
a las 00:00**. Así el sistema tiene las 24 horas completas para repartir el presupuesto.

Tú puedes montarlo todo un martes a las 22:00; lo que importa es que **empiece** a las 00:00.

## El día: martes o miércoles

| Día de arranque | Por qué |
|---|---|
| **Martes o miércoles** | ✅ **El mejor.** La fase de aprendizaje (3–7 días) transcurre entera en días laborables, que es cuando la gente compra online con normalidad. |
| Lunes | 🟡 Aceptable |
| Jueves | 🟡 Aceptable |
| Viernes, sábado, domingo | ❌ **Evítalo.** El aprendizaje arranca con datos de fin de semana, que se comportan distinto, y el algoritmo aprende sesgado. |

## ¿Y apagarlo de noche para ahorrar?

**No.** Con 15 €/día no. Programar horas ("dayparting") en Meta obliga a usar presupuesto por
tiempo total en vez de diario, y encima recorta tanto el volumen que el algoritmo deja de
aprender. Déjalo 24/7.

Cuando llegues a 50 €/día y tengas 2 meses de datos, entonces sí miras por horas y recortas.
Ahora no.

## Fecha concreta que te propongo

| Día | Qué haces |
|---|---|
| **Jue 11 – vie 12 sep** | Parte 1 completa: píxel, dominio, eventos, límites de gasto |
| **Sáb 13 sep** | Grabas los vídeos (una tarde) |
| **Dom 14 sep** | Editas en CapCut. Montas la landing de la mini-guía |
| **Lun 15 sep** | Montas la campaña. Compruebas el árbol. **La dejas programada** |
| **Mar 16 sep, 00:00** | 🚀 Arranca sola |

---

# PARTE 8 — Tu rutina diaria de métricas

## 8.1 Primero: configura las columnas (esto se hace UNA vez)

Por defecto el Administrador te enseña columnas inútiles. Cámbialas:

1. Administrador de anuncios → pestaña **Anuncios**.
2. Arriba a la derecha: **Columnas: Rendimiento** → **Personalizar columnas**.
3. Busca y **marca solo estas**, quitando todo lo demás:

```
Importe gastado
Impresiones
Frecuencia
CPM (coste por 1.000 impresiones)
Clics en el enlace
CTR (porcentaje de clics en el enlace)
CPC (coste por clic en el enlace)
Reproducciones de vídeo de 3 segundos
Resultados                    ← tus leads o tus compras
Coste por resultado
Compras
Coste por compra
Valor de conversión de compras
ROAS de compras
```

4. Abajo a la izquierda marca **☑ Guardar como configuración predefinida** → nómbrala
   `Tremdora diario` → **Aplicar**.

Desde ahora entras y en un vistazo tienes lo que importa.

## 8.2 Tu revisión de cada día (5 minutos, por la mañana)

Hazlo **a la misma hora todos los días**, mejor por la mañana, mirando **el día anterior
completo** (selector de fechas → **Ayer**). Nunca decidas mirando el día en curso: está a medias.

### El orden exacto en el que hay que mirar

**① Gasto** — ¿ronda los 15 €? Si no, mira la tabla de la Parte 6.

**② ¿Hubo resultados?** (leads o compras)
- Sí → sigue al ③.
- No, pero llevas menos de 4 días → **normal, no toques nada.**
- No, y llevas 5 días o más → salta al diagnóstico del punto 8.4.

**③ Coste por resultado** — la métrica que manda:

| Si mides LEADS (mini-guía) | Si mides COMPRAS (venta directa) |
|---|---|
| 🟢 Menos de 1,20 € — muy bien, escala | 🟢 Menos de 12 € — muy bien |
| 🟡 1,20 – 2,00 € — normal, aguanta | 🟡 12 – 20 € — aceptable |
| 🔴 Más de 2,50 € — algo falla | 🔴 Más de 25 € — pierdes dinero |

**④ Baja al nivel de anuncio** y compara los 3. Aquí es donde decides qué matar.

**⑤ Frecuencia** — si pasa de 2,5, tus creativos están quemados: toca meter ángulos nuevos.

### Y sobre todo: LO QUE NO DEBES HACER CADA DÍA

- ❌ **No cambies nada los primeros 4 días.** Estás en fase de aprendizaje. Cada cambio la
  reinicia y tiras a la basura lo aprendido.
- ❌ **No mires las métricas 6 veces al día.** Una vez, por la mañana. Mirar más solo genera
  ansiedad y decisiones malas.
- ❌ **No toques el presupuesto sin haber pasado 3 días desde el último cambio.**
- ❌ **No juzgues por un día suelto.** Un día con 0 ventas y otro con 3 es completamente normal
  a este volumen.

## 8.3 "Matar un anuncio a las 1.500 impresiones o 10 € sin añadir al carrito": qué es y qué haces

### Qué significa en cristiano

Es una **regla de parada**. Sirve para no seguir pagando por un anuncio que ya te ha demostrado
que no funciona. Sin una regla escrita, uno se queda mirando un anuncio malo dos semanas
esperando que "arranque". No arranca.

- *1.500 impresiones* = se ha mostrado 1.500 veces. Suficiente para saber si llama la atención.
- *10 € gastados* = has pagado lo bastante como para exigirle algo.
- *sin un solo añadir al carrito* = nadie, ni una persona, llegó a interesarse de verdad.

Si un anuncio se muestra 1.500 veces y **nadie** hace nada, no es mala suerte. Es mal anuncio.

### Tus umbrales, recalculados para 39,90 € y 49,90 €

> Los 10 € que te dije antes eran para un libro de 9,90 €. Con productos de 40–50 € las
> conversiones son más raras, así que hay que **dar más margen** antes de matar.

Revisa esto **una vez por semana**, no cada día:

| Situación del anuncio | Veredicto | Qué haces |
|---|---|---|
| 1.000 impresiones, **0 clics** | ☠️ Muerto | Desactivar |
| 2.000 impresiones, **CTR por debajo de 0,7 %** | ☠️ Muerto | Desactivar |
| **8 € gastados sin un solo lead** | ☠️ Muerto | Desactivar |
| **20 € gastados sin una sola compra** (venta directa) | ☠️ Muerto | Desactivar |
| Hook rate por debajo del 15 % | ☠️ Muerto | Desactivar. El problema es el segundo 1 |
| Frecuencia por encima de 3 | 😴 Quemado | Desactivar y meter ángulo nuevo |
| Coste por resultado un 50 % peor que el mejor anuncio, con 20 € gastados | 🟡 Retirar | Desactivar |
| Coste por resultado el mejor de los tres | 🏆 Ganador | Déjalo y grábale 2 variantes nuevas |

### Cómo se mata, botón a botón

1. Administrador de anuncios → pestaña **Anuncios**.
2. Selector de fechas → **Últimos 7 días**.
3. Localiza el anuncio en la lista.
4. A la izquierda de su nombre hay un **interruptor azul**. Púlsalo: se pone gris.
5. Ya está. **Desactivar, no borrar.** Borrándolo pierdes el histórico y ya no puedes comparar.

> ⚠️ **Matar un anuncio también reinicia parcialmente el aprendizaje del conjunto.**
> Por eso las bajas se hacen **una vez por semana, todas juntas**, no de una en una cada día.

## 8.4 Si a los 5 días no hay ni un resultado: diagnóstico

Sigue este orden. Es de arriba abajo, y el fallo casi siempre está arriba.

| Lo que ves en los datos | Dónde está el problema | Qué arreglar |
|---|---|---|
| Pocas impresiones (menos de 800/día) | El anuncio no se está entregando | Mira la columna **Entrega**. Suele ser rechazo por normas o público demasiado pequeño |
| Muchas impresiones, **hook rate bajo (<15 %)** | **El primer segundo del vídeo** | Regraba solo el gancho. Lo demás sirve |
| Hook rate bien, **CTR bajo (<0,8 %)** | El cuerpo del vídeo o el texto | El vídeo engancha pero no convence. Reescribe los bloques 3 y 4 |
| CTR bien, **nadie deja el email / nadie compra** | **Tu landing page**, no el anuncio | El anuncio funciona. El problema está en tu web: carga lenta, no se ve bien en móvil, o el precio sorprende |
| Todo bien pero el coste es alto | Público o competencia | Espera a los 7 días completos antes de tocar nada |

**El patrón más frecuente con productos de 40 €:** CTR excelente y cero ventas. Significa que el
anuncio hace su trabajo y **la landing no**. No sigas cambiando vídeos: arregla la página.

## 8.5 Tu revisión semanal (30 minutos, los lunes)

1. Selector de fechas → **Últimos 7 días**.
2. Apunta en una hoja: gasto total, resultados, coste por resultado, y el mejor y peor anuncio.
3. Aplica la tabla de matar del punto 8.3, **todas las bajas de golpe**.
4. Sube 2 anuncios nuevos al mismo conjunto (de los 6 ángulos de la Parte 2).
5. Decide el presupuesto:

| Coste por resultado de la semana | Decisión |
|---|---|
| Mejor que tu objetivo | **Sube el presupuesto un 20 %** (15 € → 18 €). Nunca lo dupliques: reinicia el aprendizaje |
| En el objetivo | Déjalo igual. Solo cambia creativos |
| Peor que el objetivo 2 semanas seguidas | Bájalo a 10 €/día y dedícate a arreglar landing y creativos antes de gastar más |

6. Guarda la hoja. **A las 4 semanas tendrás tus propios números reales**, y entonces sustituyes
   todos los rangos de este documento por los tuyos. Esos son los que valen.

---

# PARTE 9 — Tus primeras 4 semanas, día a día

| Cuándo | Qué haces |
|---|---|
| **Sem. 1** | Setup técnico (Parte 1) · Grabar y editar 3 vídeos · Montar landing de la mini-guía · Publicar programado para el martes a las 00:00 |
| **Sem. 1, días 1–4** | **No tocar NADA.** Solo mirar el gasto 30 segundos al día. Fase de aprendizaje |
| **Sem. 1, día 5** | Primera lectura real de métricas. Si hay 0 resultados → diagnóstico 8.4 |
| **Sem. 2, lunes** | Primera revisión semanal. Matar perdedores. Subir 2 ángulos nuevos |
| **Sem. 2** | Escribir y programar la secuencia de 6 emails que vende el libro |
| **Sem. 3, lunes** | Revisión. Deberías tener 150–300 emails. Envía la secuencia y mira cuántos compran |
| **Sem. 3** | Con las ventas ya reales, recalcula: ¿cuánto te cuesta un cliente de verdad? |
| **Sem. 4, lunes** | Revisión. Si el píxel pasa de 1.000 eventos en 30 días → **activa retargeting**: nuevo conjunto, 5 €/día, público "visitantes web últimos 30 días que no compraron", 2 anuncios |
| **15 de octubre** | **Decisión GO/NO-GO de la caja de Navidad**, con datos reales en la mano |

---

# PARTE 10 — Los 10 errores que arruinan una cuenta pequeña

1. **Lanzar sin píxel funcionando.** Todo el dinero de esos días es dinero perdido.
2. **Crear un conjunto por anuncio.** Divide el presupuesto y mata el aprendizaje.
3. **Tocar cosas durante la fase de aprendizaje.** Cada cambio reinicia los 4 días.
4. **Mirar las métricas cada 2 horas** y decidir sobre datos de medio día.
5. **Matar un anuncio a las 12 horas** porque "no ha vendido".
6. **Duplicar el presupuesto de golpe** cuando algo funciona. Sube un 20 %, espera 3 días.
7. **Publicar a las 20:00** sin programar el inicio a las 00:00.
8. **Vídeos sin subtítulos.** El 85 % lo ve en silencio.
9. **Cambiar el vídeo cuando el problema es la landing.** Diagnostica antes de actuar (8.4).
10. **Rendirse en la semana 2.** Ninguna cuenta funciona en 14 días. La decisión real se toma
    con 4 semanas de datos.
