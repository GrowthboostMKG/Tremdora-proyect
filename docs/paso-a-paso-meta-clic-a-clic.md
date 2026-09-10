# Meta Ads clic a clic — el libro de operaciones
### Cada movimiento, en orden, sin dar nada por sabido

> Fecha: 10 de septiembre de 2026
> Este documento responde a siete dudas concretas. Hazlo en orden, de la Parte A a la Parte H.
> **No te saltes la Parte B.** Si el píxel no funciona, todo lo demás es dinero tirado.

---

# PARTE A — "3 ángulos por 2 libros": lo entendiste al revés

Tu lectura fue: *3 ángulos × 2 libros = 6 anuncios, uno por cada combinación.*

**No.** Los 6 guiones son **un banco de ideas**. De ahí sacas los que puedes pagar.

```
LO QUE TIENES ESCRITO (el banco)        LO QUE LANZAS AHORA (3 anuncios)

Hogar en Calma                          ┌─────────────────────────────┐
  ├── HC1 "La señal"          ────────► │ ✅ HC1  "La señal"          │
  ├── HC2 "Anti-app"          ────────► │ ✅ HC2  "Anti-app"          │
  └── HC3 "22:47"                       │ ✅ ED1  "El domingo"        │
                                        └─────────────────────────────┘
Edad Dorada                                   ⬆ estos 3, y nada más
  ├── ED1 "La llamada del domingo" ────►
  ├── ED2 "Ayudar sin invadir"                HC3, ED2 y ED3 se quedan
  └── ED3 "Las conversaciones"                en la recámara para el mes 2
```

## Las tres reglas que hay detrás

**① Un anuncio = un ángulo = un libro.** Nunca mezcles dos libros en un vídeo. El que lo ve tiene
que entender en 3 segundos de qué le hablas. Si le hablas de dos cosas, no entiende ninguna.

**② El número de anuncios lo decide tu presupuesto, no tu catálogo.**

> **15 € ÷ 5 € por ángulo = 3 anuncios.**

Con 6 anuncios y 15 €, cada uno recibe 2,50 €/día. Con 2,50 € al día un anuncio consigue unas
300 impresiones: **no llega ni a poder juzgarse.** Acabarías con 6 anuncios de los que no sabes
nada, en vez de 3 de los que sabes la verdad.

**③ Los 3 no se reparten mitad y mitad.** Van 2 de Hogar en Calma y 1 de Edad Dorada, porque
Hogar en Calma es el que lanzas de verdad y Edad Dorada solo está midiendo el mercado con una
lista de espera.

| Anuncio | Libro | A dónde lleva |
|---|---|---|
| HC1 "La señal" | Hogar en Calma | Landing del lead magnet |
| HC2 "Anti-app" | Hogar en Calma | La misma landing |
| ED1 "El domingo" | Edad Dorada | Landing de lista de espera |

---

## Y sí: los 3 conjuntos de 5 € son un error. Confirmado.

Tenías razón en la duda. **Nunca hagas esto:**

```
❌ MAL                                  ✅ BIEN

Conjunto 1 → 5 €/día → HC1              Conjunto único → 15 €/día
Conjunto 2 → 5 €/día → HC2                    ├── HC1
Conjunto 3 → 5 €/día → ED1                    ├── HC2
                                              └── ED1
```

**Por qué el de la izquierda arruina la cuenta, en dos motivos:**

**Motivo 1 — Ninguno aprende.** Facebook necesita **50 resultados en 7 días por conjunto** para
salir de la fase de aprendizaje. Un conjunto con 5 €/día consigue unos 20 a la semana. Tres
conjuntos ciegos rinden peor que uno que ve.

**Motivo 2 — Obligas a que el peor cobre lo mismo que el mejor.** Estás apostando 5 € a cada
caballo *antes* de que empiece la carrera. En la bolsa única, al tercer día Facebook le está
dando 11 € al ganador y 2 € a cada perdedor, **él solo**. Eso es exactamente lo que quieres.

---

# PARTE B — El píxel: instalarlo y pegarlo en tu landing

## B.1 Crear el píxel y copiar el código

1. Entra en `business.facebook.com`.
2. Menú ☰ (arriba a la izquierda) → busca **Administrador de eventos**.
3. Botón verde **Conectar orígenes de datos** → **Web** → **Conectar**.
4. Nombre: `Pixel Tremdora` → **Crear**.
5. Verás un número largo de 15-16 cifras. **Ese es tu ID de píxel.** Cópialo en una nota:
   lo vas a usar tres veces.
6. Te preguntará cómo instalarlo → elige **Instalar el código manualmente**.
7. Aparece un recuadro con código. Pulsa **Copiar código**.

> El código que copias **ya lleva tu ID dentro**. Por eso hay que copiarlo de ahí y no de un
> tutorial de internet: el de internet lleva el ID de otro.

El código tiene esta forma (el tuyo será más largo, con tu número donde pone `TU_ID`):

```html
<!-- Meta Pixel Code -->
<script>
  !function(f,b,e,v,n,t,s){ ... }(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'TU_ID');
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=TU_ID&ev=PageView&noscript=1"/></noscript>
<!-- End Meta Pixel Code -->
```

## B.2 Dónde se pega — según dónde tengas la landing

### Caso 1: tu landing es un archivo HTML tuyo *(es tu caso)*

Te he dejado la landing ya montada en este repositorio, en la carpeta `landing/`. **Lo único que
tienes que hacer es sustituir el texto `PEGA_AQUI_TU_ID_DE_PIXEL` por tu número.** El resto ya
está puesto en su sitio.

Si prefieres hacerlo a mano en otro archivo, la regla es:

> El código va **dentro de `<head>`, justo antes de `</head>`**, y en **todas** las páginas.

```html
<head>
  <title>...</title>

  <!-- 👇 AQUÍ, justo antes de que se cierre el head -->
  <!-- Meta Pixel Code -->
  <script> ... </script>
  <!-- End Meta Pixel Code -->

</head>
```

### Caso 2: la landing está en Shopify
Shopify → **Aplicaciones** → busca **Facebook & Instagram** → **Instalar** → sigue el asistente
→ conecta tu cuenta de empresa → elige `Pixel Tremdora`. Shopify enviará solo los eventos
ViewContent, AddToCart, InitiateCheckout y Purchase. **No pegues nada a mano además de esto**, o
contarás cada compra dos veces.

### Caso 3: usas un constructor (Systeme, MailerLite, Carrd, Wix…)
Busca en sus ajustes **"Código personalizado" / "Custom code" / "Head tracking code"** y pega el
bloque ahí. Todos los constructores tienen ese hueco, aunque cada uno lo llame distinto.

## B.3 El evento Lead: la línea que de verdad importa

El código de arriba solo cuenta **visitas**. Para que Facebook sepa **quién te dejó el email**
—que es el resultado por el que estás optimizando— hace falta una línea más:

```html
<script>fbq('track', 'Lead');</script>
```

**Esa línea va en la página de GRACIAS**, la que se ve *después* de enviar el formulario. No en
la landing.

```
Landing  ──► pixel base (PageView)          ← "ha entrado alguien"
   │
   ▼ (rellena el formulario)
Gracias  ──► pixel base + fbq('track','Lead')  ← "alguien ha dejado el email"  ✅
```

En la carpeta `landing/` te he dejado las dos páginas, con la línea ya puesta en la de gracias.

## B.4 Comprobar que funciona — no te saltes esto

1. Instala en Chrome la extensión **Meta Pixel Helper**.
2. Abre tu landing. El icono de la extensión debe ponerse **azul** y decir *1 pixel found*.
3. Rellena tu propio formulario con tu email.
4. En la página de gracias, el Pixel Helper debe mostrar **PageView** y **Lead**.
5. Segunda comprobación, la buena: Administrador de eventos → pestaña **Probar eventos** → pega
   la URL de tu landing → repite el proceso. Los eventos deben ir apareciendo en pantalla en
   tiempo real, mientras navegas.

> ⛔ **Si aquí no ves el evento Lead, PARA.** No montes la campaña. Sin ese evento, Facebook no
> sabe a quién buscar y estarás pagando por un algoritmo ciego. Es el punto donde más gente tira
> el dinero sin enterarse.

---

# PARTE C — El candado del gasto (y no, 105 no)

## C.1 Tu pregunta: ¿pongo 105 semanales?

**No, y es importante que se entienda por qué.** Estás mezclando dos cosas distintas.

| | Presupuesto diario | Límite de gasto de la cuenta |
|---|---|---|
| Qué es | El **ritmo** al que gastas | Un **freno de mano** total |
| Dónde se pone | En el conjunto de anuncios | En Facturación |
| Cuánto | 15 €/día | Un total acumulado |
| ¿Se reinicia? | Cada día, solo | **NUNCA.** Va sumando desde que lo pones |
| Qué pasa al llegar | Nada, sigue mañana | **Se apagan todos tus anuncios** |

Los **105 €** salieron de mi explicación de que Facebook cuadra el gasto en ventanas de 7 días
(7 × 15 = 105). Eso es **automático**, no hay que configurarlo en ningún sitio.

**Si pones 105 € como límite de cuenta, el día 7 se te apaga todo.** Y como no se reinicia solo,
te quedas parado hasta que entres a mano a subirlo. Justo en mitad de la fase de aprendizaje,
que es el peor momento posible para que se pare una campaña.

## C.2 Lo que sí debes poner

> **450 €** — que es un mes entero a 15 €/día.

Si te da respeto empezar con esa cifra, pon **150 €** (unos 10 días). Funciona igual; solo
tendrás que entrar a subirlo antes.

## C.3 Cómo se pone, clic a clic

1. `adsmanager.facebook.com`
2. Menú **☰** arriba a la izquierda → en el buscador escribe **Facturación**
   → entra en **Facturación y pagos**.
3. Pestaña **Configuración de pagos**.
4. Busca la sección **Límite de gasto de la cuenta** → **Establecer límite**.
5. Escribe **450** → **Establecer límite** → **Guardar**.

**Cuando llegues a 450 €:** vuelves a la misma pantalla y pulsas **Restablecer límite de gasto**
o **Cambiar límite** y pones la cifra del mes siguiente. Mientras no lo hagas, todo sigue parado.

## C.4 La otra protección que casi nadie configura

En esa misma pantalla busca **Umbral de facturación** (o *Límite de facturación*).

Es la cantidad que Facebook deja acumular antes de cobrarte. Empieza bajo (25 €) y **la va
subiendo sola** hasta 750 € o más, sin avisarte.

**Bájalo a mano a 50 €.** Así te cobra a menudo y en importes pequeños. Si algo se descontrola,
lo ves en tu banco en 2-3 días en vez de en la factura de fin de mes.

## C.5 Resumen de las tres capas

```
Capa 1 · Presupuesto diario del conjunto ····· 15 €/día    (el ritmo)
Capa 2 · Límite de gasto de la campaña ······· 450 €       (freno de esa campaña)
Capa 3 · Límite de gasto de la CUENTA ········ 450 €       (freno de todo) 🔒
```

La capa 3 es la que te salva si un día duplicas una campaña sin querer.

---

# PARTE D — Crear la campaña, clic a clic

Entra en `adsmanager.facebook.com` y pulsa el botón verde **+ Crear**.

## D.1 Pantalla 1 — Objetivo

Te salen 6 tarjetas. Pulsa **Clientes potenciales** → **Continuar**.

> *(Si tu landing vendiera directamente, aquí irías a "Ventas". No es tu caso: tu landing pide
> un email, así que es "Clientes potenciales".)*

## D.2 Pantalla 2 — Nivel CAMPAÑA

| Campo | Qué pones | ⚠️ |
|---|---|---|
| Nombre de la campaña | `TR - Leads - Sep26` | |
| Categoría especial de anuncios | **Ninguna** | |
| Objetivo de la campaña | *(ya viene puesto)* | |
| Prueba A/B | **Desactivada** | |
| **Presupuesto Advantage para campañas** | **DESACTIVADO** | 🔴 Importante. Si lo dejas activado, el dinero se pone aquí y no abajo. Queremos ponerlo abajo |

**Siguiente**.

## D.3 Pantalla 3 — Nivel CONJUNTO DE ANUNCIOS *(aquí va el dinero)*

| Campo | Qué pones |
|---|---|
| Nombre del conjunto | `Amplio - ES - 25-65` |
| Ubicación de conversión | **Sitio web** |
| Conjunto de datos / Píxel | `Pixel Tremdora` |
| **Evento de conversión** | **Lead** 🔴 |
| **Presupuesto diario** | **15,00 €** 🔴 *(el único sitio donde va el dinero)* |
| Programación → Fecha de inicio | **Mañana, 00:00** |
| Programación → Fecha de finalización | **Sin fecha de finalización** |
| Ubicación | **España** |
| Edad | **25 – 65+** |
| Sexo | **Todos** |
| Público objetivo Advantage+ | **Activado** *(así no metes intereses: Facebook busca solo)* |
| Ubicaciones | **Ubicaciones Advantage+** (automáticas) |

**Siguiente**.

> 🔴 **Aquí es donde se equivoca todo el mundo.** Vas a crear **UN SOLO** conjunto. No pulses
> "duplicar conjunto" en ningún momento. Los tres anuncios van dentro de este.

## D.4 Pantalla 4 — Nivel ANUNCIO (el primero)

| Campo | Qué pones |
|---|---|
| Nombre del anuncio | `HC1 - La senal - video` |
| Identidad → Página de Facebook | Tu página de Tremdora |
| Identidad → Cuenta de Instagram | La tuya |
| Configuración del anuncio | **Crear anuncio** |
| Formato | **Una sola imagen o vídeo** |
| Contenido → Añadir multimedia | **Añadir vídeo** → sube tu vídeo HC1 |
| Texto principal | El texto de Hogar en Calma *(guiones, apartado 3)* |
| Titular | `El método de las 21 noches` |
| Descripción | `Primer capítulo gratis` |
| Destino | **Sitio web** |
| URL del sitio web | La URL de tu landing |
| Llamada a la acción | **Descargar** |

**No pulses Publicar todavía.** Faltan dos anuncios.

---

# PARTE E — Meter los 3 anuncios en la misma bolsa

Esto es lo que preguntabas: *"¿cómo se hace y dónde?"*.

**Respuesta corta: no hay ningún botón de "meterlos en la misma bolsa". Se hace duplicando el
anuncio hacia dentro del mismo conjunto.**

## E.1 Entiende la columna de la izquierda

En el Administrador de anuncios, a la izquierda, hay un árbol de tres niveles. **Ese árbol es
"la bolsa"**, visualmente:

```
📁 TR - Leads - Sep26              ← CAMPAÑA (aquí eliges el objetivo)
   └── 📁 Amplio - ES - 25-65      ← CONJUNTO = LA BOLSA (aquí está el dinero: 15 €/día)
         ├── 📄 HC1 - La senal     ← ANUNCIO
         ├── 📄 HC2 - Anti-app     ← ANUNCIO   } los tres, dentro
         └── 📄 ED1 - El domingo   ← ANUNCIO   } de la MISMA carpeta
```

Estar "en la misma bolsa" = **estar dentro de la misma carpeta de conjunto**. Nada más. Si están
ahí, compiten solos, sin que tú configures nada.

## E.2 Los clics exactos para añadir el segundo anuncio

1. En la columna izquierda, localiza tu anuncio `HC1 - La senal`.
2. **Clic derecho encima** → se abre un menú → **Duplicar**.
   *(Si no te sale el clic derecho: marca la casilla del anuncio y pulsa el botón
   **Duplicar** de la barra de arriba.)*
3. Se abre una ventana que dice **"Duplicar en…"**. 🔴 **Aquí está el punto crítico:**

   | Opción | ¿Elegirla? |
   |---|---|
   | **Conjunto de anuncios existente** → `Amplio - ES - 25-65` | ✅ **ESTA** |
   | Nuevo conjunto de anuncios | ❌ NO. Esto crea otra bolsa |
   | Nueva campaña | ❌ NO |

4. Número de copias: **1** → **Duplicar**.
5. La copia aparece en el árbol, dentro de la misma carpeta, llamada `HC1 - La senal - Copia`.
6. **Púlsala y cámbiale todo:**
   - Nombre → `HC2 - Anti-app - video`
   - Multimedia → quita el vídeo HC1 y sube el HC2
   - Texto principal, titular → los de HC2
   - URL → la misma landing de Hogar en Calma
7. **Repite los pasos 1 a 6** para el tercero:
   - Nombre → `ED1 - El domingo - video`
   - Vídeo ED1, textos de Edad Dorada
   - 🔴 **URL → la landing de LISTA DE ESPERA**, no la de Hogar en Calma

## E.3 La comprobación antes de publicar

Mira la columna izquierda. **Tiene que verse exactamente así:**

```
📁 TR - Leads - Sep26
   └── 📁 Amplio - ES - 25-65    ·  15,00 €/día
         ├── 📄 HC1 - La senal - video
         ├── 📄 HC2 - Anti-app - video
         └── 📄 ED1 - El domingo - video
```

**UNA carpeta de campaña. UNA carpeta de conjunto. TRES hojas de anuncio.**

Si ves dos o tres carpetas de conjunto, lo has hecho mal: has duplicado hacia fuera. Borra las
carpetas de más y repite el paso E.2 eligiendo bien la opción del punto 3.

Cuando el árbol esté así → botón verde **Publicar**.

---

# PARTE F — Desactivar anuncios: las bajas

## F.1 Qué es "dar de baja" un anuncio

Es **apagarlo** para que deje de gastar, pero **sin borrarlo**.

> 🔴 **Desactivar, nunca borrar.** Si lo borras, pierdes su histórico y ya no puedes comparar
> qué funcionó. Y si mañana quieres volver a encenderlo, tendrías que crearlo otra vez desde cero.

## F.2 Los clics

1. `adsmanager.facebook.com`
2. Arriba, las tres pestañas: **Campañas · Conjuntos de anuncios · Anuncios**.
   Pulsa **Anuncios**.
3. Arriba a la derecha, el selector de fechas → **Últimos 7 días**.
4. En la lista, localiza el anuncio por su nombre.
5. **A la izquierda del nombre hay un interruptor azul.** Púlsalo.
6. Se pone **gris**. Ya está apagado. No gastará ni un céntimo más.

Para volver a encenderlo: el mismo interruptor.

## F.3 Cuándo hay que dar de baja — la tabla

Revisa esto **una vez por semana, los lunes**. No cada día.

| Lo que ves | Veredicto |
|---|---|
| 1.000 impresiones y **0 clics** | ☠️ Baja |
| 2.000 impresiones y **CTR por debajo de 0,7 %** | ☠️ Baja |
| **8 € gastados sin un solo Lead** | ☠️ Baja |
| **Frecuencia por encima de 3** | 😴 Quemado → baja y sube uno nuevo del banco |
| Coste por lead un 50 % peor que el mejor, con 20 € gastados | 🟡 Baja |
| El coste por lead más bajo de los tres | 🏆 Déjalo, y grábale 2 variantes |

## F.4 Las dos reglas que hacen que esto funcione

**① Nunca antes del día 5.** Los primeros 4 días son la fase de aprendizaje: los datos no valen
nada y cualquier cambio la reinicia.

**② Todas las bajas de golpe, una vez por semana.** Cada vez que apagas un anuncio, el conjunto
recalcula. Si apagas uno cada día, el conjunto vive reiniciándose y nunca aprende. Los lunes,
miras los tres, decides, y ejecutas todas las bajas en dos minutos.

## F.5 Y lo que haces después de cada baja

Una baja deja un hueco. **Rellénalo el mismo día** con un anuncio del banco de la recámara
(HC3, ED2, ED3), duplicando como en la Parte E.

> Tres anuncios activos, siempre. No dos, no cuatro. Si bajas uno, subes uno.

---

# PARTE G — Retargeting (esto es para la semana 4, no para ahora)

## G.1 Qué es, en una frase

Enseñarle anuncios **solo a la gente que ya ha estado en tu web** y no dejó el email o no compró.

Es la publicidad más barata que existe —convierte 3 a 5 veces mejor que el tráfico frío— porque
ya te conocen. Pero necesita una cosa: **que haya pasado gente por tu web**.

## G.2 Por qué no puedes hacerlo hoy

Para que Facebook pueda construir ese público, necesita tener personas "fichadas" por tu píxel.
Con menos de unas 1.000 acciones registradas en 30 días, el público sale tan pequeño que:

- o Facebook no lo entrega (te dice *"público demasiado pequeño"*),
- o lo entrega y le enseña el anuncio 9 veces a las mismas 40 personas, quemándolas y gastando
  tus 5 € en nada.

> **Tu señal para activarlo:** Administrador de eventos → tu píxel → ahí ves cuántos eventos has
> registrado en 30 días. **Cuando pase de 1.000, es el momento.** Con 15 €/día, eso suele caer
> entre la semana 3 y la 5.

## G.3 Paso 1 — Crear el público (esto sí puedes hacerlo ya)

Créalo hoy aunque no lo uses: **empieza a acumular gente desde el primer día**, así cuando llegue
la semana 4 el público ya está lleno.

1. `business.facebook.com` → menú ☰ → **Públicos**.
2. **Crear un público** → **Público personalizado**.
3. Elige el origen: **Sitio web**.
4. Configura:

   | Campo | Qué pones |
   |---|---|
   | Origen | `Pixel Tremdora` |
   | Eventos | **Todos los visitantes del sitio web** |
   | Conservación | **30 días** |
   | Nombre | `Web - visitantes 30d` |

5. **Crear público**.

6. Crea un segundo, para excluir a los que ya te dejaron el email:
   - Mismo proceso, pero en **Eventos** elige **Lead**
   - Conservación: **180 días**
   - Nombre: `Leads - 180d`

## G.4 Paso 2 — Montar la campaña de retargeting (semana 4)

1. **+ Crear** → objetivo **Ventas** *(aquí sí vendes: esta gente ya te conoce)*.
2. Nombre de campaña: `TR - Retargeting - Oct26`.
3. Nivel conjunto:

   | Campo | Qué pones |
   |---|---|
   | Nombre | `RTG - visitantes 30d` |
   | Evento de conversión | **Purchase** |
   | **Presupuesto diario** | **5,00 €** |
   | Públicos personalizados → **Incluir** | `Web - visitantes 30d` |
   | Públicos personalizados → **Excluir** | `Leads - 180d` 🔴 |
   | Ubicación | España |
   | Público objetivo Advantage+ | **Desactivado** 🔴 |

   > 🔴 **Las dos casillas rojas son las que hacen que esto funcione.**
   > **Excluir** evita que pagues por enseñarle "déjame tu email" a quien ya te lo dio.
   > **Advantage+ desactivado** evita que Facebook se salga de tu público y se vaya al frío —
   > si lo dejas activado, deja de ser retargeting.

4. Nivel anuncio: **2 anuncios**, y aquí el mensaje cambia por completo. Al frío le cuentas el
   problema; a esta gente **ya se lo contaste**. Aquí van:
   - **Objeciones y garantía:** "30 días. Si no te sirve, te devolvemos el dinero."
   - **Qué hay dentro exactamente:** enseña las cuatro piezas, una por una.
   - Un testimonio real, en cuanto tengas el pedido nº 10.

5. Y ajusta el reparto: el conjunto frío baja de 15 € a **10 €/día**, el de retargeting se lleva
   **5 €/día**. Total: los mismos 15 €.

---

# PARTE H — Checklist antes de pulsar Publicar

Imprímelo. No publiques con una sola casilla sin marcar.

**El píxel**
- [ ] El Pixel Helper se pone azul en mi landing
- [ ] En la página de gracias aparecen **PageView** y **Lead**
- [ ] Lo he comprobado también en **Probar eventos**
- [ ] He verificado mi dominio en el Administrador de eventos

**El dinero**
- [ ] Límite de gasto de la **cuenta**: 450 € puesto
- [ ] Umbral de facturación bajado a 50 €
- [ ] Tarjeta añadida y validada

**La estructura**
- [ ] En el árbol veo **1 campaña · 1 conjunto · 3 anuncios**
- [ ] El presupuesto de 15 €/día está en el **conjunto**, no en la campaña
- [ ] "Presupuesto Advantage para campañas" está **desactivado**
- [ ] Evento de conversión = **Lead**
- [ ] Fecha de inicio = **mañana a las 00:00**
- [ ] Es martes o miércoles

**Los anuncios**
- [ ] Los 3 vídeos son verticales 9:16
- [ ] Los 3 llevan subtítulos quemados
- [ ] Ninguno pasa de 35 segundos
- [ ] HC1 y HC2 → landing de Hogar en Calma
- [ ] ED1 → landing de **lista de espera**
- [ ] He releído el de Edad Dorada con la tabla de política de Meta delante
- [ ] En ningún texto digo "frecuencia sanadora" ni ninguna promesa de salud

**Después de publicar**
- [ ] Los 4 primeros días **no toco nada**
- [ ] Tengo el lunes marcado en el calendario para la revisión semanal
