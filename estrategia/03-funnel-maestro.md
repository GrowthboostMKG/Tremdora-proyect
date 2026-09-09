# 3. El funnel maestro TREMDORA (arquitectura completa)

Este es el esqueleto que usan **los dos productos**. Cambia el copy y el ángulo; la mecánica es idéntica. Móntalo una vez y reutilízalo.

## 3.1 Vista general

```
                          TRÁFICO FRÍO
              ┌───────────────┬───────────────┐
              │               │               │
        Meta Ads (40€/d)  Orgánico       Búsqueda
              │           TikTok/IG/YT     (SEO/Google)
              └───────────────┼───────────────┘
                              ▼
              ┌───────────────────────────────┐
              │  RUTA A: ADVERTORIAL          │  ← tráfico muy frío
              │  (artículo/quiz pre-venta)    │
              └───────────────┬───────────────┘
                              ▼
              ┌───────────────────────────────┐
              │  PDP — Página de producto     │  ← núcleo de conversión
              │  Oferta + prueba social       │
              └───────────────┬───────────────┘
                              ▼
              ┌───────────────────────────────┐
              │  CARRITO + ORDER BUMP (+14€)  │  ← palanca AOV #1
              └───────────────┬───────────────┘
                              ▼
              ┌───────────────────────────────┐
              │  CHECKOUT (Shop Pay acelerado)│
              └───────────────┬───────────────┘
                              ▼
              ┌───────────────────────────────┐
              │  UPSELL POST-COMPRA 1-CLIC    │  ← palanca AOV #2
              └───────────────┬───────────────┘
                              ▼
              ┌───────────────────────────────┐
              │  THANK-YOU + ENTREGA DIGITAL  │  ← inicio de la relación
              └───────────────┬───────────────┘
                              ▼
              ╔═══════════════════════════════╗
              ║  KLAVIYO — 8 FLUJOS           ║  ← donde está el beneficio
              ║  LTV, cross-sell, recompra    ║
              ╚═══════════════════════════════╝

     RUTA B (paralela, para quien NO compra hoy):
     Ad / orgánico → LEAD MAGNET → email → secuencia bienvenida → venta
```

## 3.2 Las dos rutas y cuándo usar cada una

| | **Ruta A — Venta directa** | **Ruta B — Captación de lead** |
|---|---|---|
| Destino del anuncio | PDP o advertorial | Landing de lead magnet |
| Objetivo de campaña | Compras | Clientes potenciales / Compras |
| Ventaja | Ingreso hoy, valida la oferta | Coste por lead 10–20× menor |
| Riesgo | CPA alto al principio | No cobras hoy |
| **Cuándo** | Desde el día 1, con el 70 % del presupuesto | Desde el día 1, con el 30 % |

> **Por qué las dos a la vez y no solo la A:** con 40 €/día vas a captar muy pocos compradores, pero puedes captar **muchos emails**. Esos emails son el activo que hace posible lanzar Edad Dorada sin gastar en ads en el mes 3. La Ruta B es, literalmente, cómo financias el segundo lanzamiento.

## 3.3 Paso 1 — El anuncio (creatividad)

La creatividad es el 80 % del resultado. Estructura de vídeo UGC que funciona (15–30 s):

```
0-3 s   HOOK        Interrumpe. Visual + texto en pantalla + frase.
3-8 s   PROBLEMA    Nombra la fricción cotidiana concreta.
8-15 s  MECANISMO   Enseña el producto resolviéndolo. Cómo funciona.
15-22 s PRUEBA      Resultado, testimonio, antes/después.
22-30 s CTA         Oferta + urgencia suave + "toca el enlace".
```

**Regla de producción:** 1 concepto × 5 hooks distintos = 5 anuncios. Es más barato y más eficaz que 5 vídeos distintos. El hook es lo que hay que testear.

**Formatos a producir (mínimo 15 piezas antes de encender ads):**
- 5 × UGC hablado a cámara (testimonio/descubrimiento)
- 4 × Demostración sin voz + texto (ASMR / satisfying)
- 3 × Estático de oferta (bundle, precio, garantía)
- 2 × Carrusel educativo ("las 5 señales de que…")
- 1 × Vídeo de fundador ("por qué creé TREMDORA")

## 3.4 Paso 2 — El advertorial (opcional, alto impacto)

Un advertorial es un artículo de 700–1.100 palabras que **pre-vende** antes de llegar a la ficha de producto. Sube el CVR entre un 30 % y un 80 % en tráfico frío, porque la gente llega a la PDP ya convencida.

Estructura:
1. **Titular** — promesa o historia ("Por qué cambié toda la rutina de las noches en casa")
2. **Historia personal** — identificación con el lector
3. **El problema real** — por qué lo obvio no funciona
4. **El descubrimiento** — presentación del mecanismo
5. **Cómo funciona** — 3 puntos, con visual
6. **Prueba social** — 3 testimonios + fotos reales
7. **La oferta** — precio, bonus digital, garantía
8. **CTA** — botón a la PDP con descuento aplicado

Móntalo en Shopify como página (`/pages/historia-hogar-en-calma`), no en un blog externo.

## 3.5 Paso 3 — La PDP (ficha de producto)

Esta página decide si el negocio funciona. Orden obligatorio arriba del pliegue:

1. **Galería** — 7 imágenes: producto solo, en uso, en contexto de hogar, detalle, comparativa, infografía de beneficio, el bonus digital visualizado
2. **Título con beneficio**, no descriptivo → *"Hogar en Calma — El sistema para que tu casa te baje las pulsaciones"* (no *"Difusor de aromas 300 ml"*)
3. **Estrellas + nº de reseñas** (usa Judge.me gratis; empieza pidiendo reseñas a tus primeros 10 pedidos)
4. **Precio con ancla** → ~~89 €~~ **69 €**
5. **Selector de bundle** (ver 3.6)
6. **Botón CTA** — "Quiero mi Hogar en Calma"
7. **Barra de confianza** — envío 24-48 h · garantía 30 días · pago seguro · atención en español

Debajo: los 3 beneficios con iconos, el "cómo funciona" en 3 pasos, el bonus digital detallado con valor asignado, FAQ de 8 preguntas (que respondan objeciones reales), reseñas con foto.

## 3.6 Paso 4 — Palancas de AOV (aquí se gana el dinero)

Con un CAC dado, **el AOV es lo que decide si hay beneficio.** Tres palancas, en orden de facilidad:

### a) Escalera de bundles en la PDP
| Opción | Precio | Descuento | Etiqueta |
|---|---|---|---|
| 1 unidad | 69 € | — | |
| **2 unidades** | **118 €** | 15 % | **★ MÁS ELEGIDA** (preseleccionada) |
| 3 unidades | 159 € | 23 % | Mejor precio |

Preselecciona siempre la del medio. Solo esto sube el AOV un 20–35 %.

### b) Order bump en el carrito (+14 €)
Un extra digital de bajo precio y **margen ~100 %**, marcado con un checkbox:

> ☐ **Añade el Audio-Programa "21 Noches en Calma" por solo 14 €** *(en lugar de 39 €)* — 21 audios de 10 min para reprogramar tus noches. Acceso inmediato.

Adopción esperada: 20–30 %. Aporta **+3 a +4 € de margen limpio por pedido**.

### c) Upsell post-compra a 1 clic
Tras pagar, antes del thank-you. **No pide tarjeta otra vez** → conversión del 10–20 %.
- Para Hogar en Calma → recambio/pack anual con descuento, o el acceso premium
- Para Edad Dorada → segunda unidad "para regalar a alguien que también lo necesita"

App recomendada en Shopify: **AfterSell** o **Zipify OCU** (~30–50 $/mes; se paga solo con 2 upsells).

**Impacto conjunto:** AOV de 62 € → **78–85 €**. Eso mueve el CAC máximo asumible de 37 € a **~50 €**. Es la diferencia entre poder escalar y no poder.

## 3.7 Paso 5 — Los 8 flujos de Klaviyo (el motor de beneficio)

Móntalos **antes** de encender los anuncios. Plan gratuito de Klaviyo hasta 250 contactos; después ~20–45 €/mes.

| # | Flujo | Disparador | Emails | Objetivo |
|---|---|---|---|---|
| 1 | **Bienvenida** | Alta en lista / lead magnet | 5 | Entregar valor + primera venta |
| 2 | **Carrito abandonado** | Añadió al carrito, no compró | 3 + SMS | Recuperar 10-15 % |
| 3 | **Checkout abandonado** | Inició pago, no terminó | 3 | Recuperar 20-30 % |
| 4 | **Navegación abandonada** | Vio PDP 2×, no añadió | 2 | Reactivar interés |
| 5 | **Post-compra / onboarding** | Compra confirmada | 4 | Entregar el digital, reducir devoluciones |
| 6 | **Solicitud de reseña** | 14 días tras entrega | 2 | Generar prueba social y UGC |
| 7 | **Cross-sell TREMDORA** | 30 días tras compra | 3 | Vender el otro producto |
| 8 | **Winback** | 75 días sin comprar | 3 | Recuperar dormidos |

### Detalle del flujo 1 — Bienvenida (el más importante)

| Email | Momento | Asunto (ejemplo) | Contenido |
|---|---|---|---|
| 1 | Inmediato | "Aquí tienes tu guía 👇" | Entrega el lead magnet. **Sin vender.** |
| 2 | +1 día | "El error que comete casi todo el mundo" | Educación. Nombra el problema. Presenta el mecanismo. |
| 3 | +2 días | "Cómo nació TREMDORA" | Historia de marca. Conexión. Menciona el producto de pasada. |
| 4 | +4 días | "Lo que nos escribió Carmen" | Prueba social pura. 2-3 testimonios. CTA suave. |
| 5 | +6 días | "Tu −10 % caduca esta noche" | Oferta con caducidad real. CTA directo. |

> **Regla GP:** los emails 1–4 no venden, **construyen el derecho a vender** del email 5. Una lista quemada por vender desde el minuto uno no vale nada.

### Detalle del flujo 5 — Post-compra (donde vive tu ventaja híbrida)
1. **Inmediato:** "Tu acceso a [contenido digital]" — enlace, botón grande, cero fricción
2. **+2 días:** "Empieza por aquí" — el primer paso del método. Genera uso.
3. **+7 días:** "¿Cómo va la primera semana?" — pide respuesta. Los reply suben la entregabilidad.
4. **+14 días:** "Un truco que casi nadie usa" — valor extra + primera semilla del cross-sell

## 3.8 Paso 6 — Retargeting (a partir de la semana 5)

No lo actives antes: no tendrás suficiente tráfico para llenar las audiencias.

| Audiencia | Ventana | Mensaje |
|---|---|---|
| Vio PDP, no compró | 14 días | Prueba social + garantía |
| Añadió al carrito | 7 días | Objeción + urgencia |
| Vio 50 % del vídeo | 30 días | Ángulo distinto al que ya vio |
| Compradores | 180 días | **Cross-sell al otro producto** |

Presupuesto: 10 €/día como máximo, y solo cuando el tráfico lo justifique.
