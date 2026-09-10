# Tremdora — Estrategia de lanzamiento: eBooks mensuales → Cajas pack

> Fecha del plan: 10 de septiembre de 2026
> Estado de los datos: **no verificado contra la tienda**. El conector de Shopify pedía re-autorización,
> así que todas las cifras de precios, márgenes y CPA son *supuestos de referencia de mercado*, no datos
> reales de Tremdora. Antes de ejecutar, sustituye los supuestos del bloque siguiente por tus números.

## 0. Supuestos que hay que confirmar

| Variable | Supuesto usado | Confírmalo |
|---|---|---|
| Plataforma de ads | Meta (Facebook + Instagram) | ☐ |
| Mercado / moneda | España, EUR | ☐ |
| Precio eBook individual | 9,90 € | ☐ |
| Precio pack 2 eBooks | 14,90 € | ☐ |
| Precio caja física | 39–45 € | ☐ |
| Coste de la caja (COGS + envío) | 12–18 € | ☐ |
| Presupuesto de ads disponible/día | 15–20 € | ☐ |
| Píxel de Meta con histórico | No (cuenta fría) | ☐ |

Si tu presupuesto real es distinto, la tabla del punto 1 se reescala sola: **la regla es 1 ángulo
creativo nuevo por cada 5 €/día de inversión**.

---

## 1. ¿Cuántos anuncios poner a rodar?

**Respuesta corta: 6 anuncios activos, dentro de 1 solo conjunto, dentro de 1 sola campaña.**

El error más caro con presupuesto pequeño es abrir muchas campañas y conjuntos "para probar".
Cada conjunto necesita ~50 conversiones/semana para salir de la fase de aprendizaje. Si repartes
20 €/día entre 4 conjuntos, ninguno aprende y todos rinden mal.

### Estructura Fase 0 — Validación (semanas 1–3)

```
Campaña: Ventas (objetivo: Compra)
└── Conjunto único: público amplio, país completo, 25–65, sin intereses
    ├── Anuncio 1 — Libro A · ángulo "problema agitado" (vídeo UGC 20–30 s)
    ├── Anuncio 2 — Libro A · ángulo "los 5 errores que cometes" (carrusel)
    ├── Anuncio 3 — Libro A · ángulo "antes / después" (estático)
    ├── Anuncio 4 — Libro B · ángulo "problema agitado" (vídeo UGC)
    ├── Anuncio 5 — Libro B · ángulo "mini-diagnóstico / test" (vídeo)
    └── Anuncio 6 — Libro B · ángulo "testimonio" (estático o vídeo)
```

**Los dos libros van en el MISMO conjunto.** No repartas el presupuesto 50/50: deja que el algoritmo
decida cuál tema convierte mejor y te lo diga con datos, no con tu intuición. Cada anuncio lleva a
la landing de *su* libro.

Punto clave: cada ángulo tiene que ser un **argumento distinto**, no el mismo creativo en otro color.
6 variantes del mismo mensaje = 1 test, no 6.

### Tabla de escalado

| Presupuesto/día | Campañas | Conjuntos | Anuncios activos | Retargeting |
|---|---|---|---|---|
| 10–15 € | 1 | 1 | 4–6 | No |
| 20–30 € | 1 | 1–2 | 6–8 | No (aún) |
| 40–60 € | 1–2 | 2–3 | 8–12 | Sí, 1 conjunto / 2–3 anuncios / 15% del presupuesto |
| 80 €+ | 2 | 3–4 | 12–16 | Sí, 20% |

**No actives retargeting hasta tener ≥1.000 eventos de píxel en 30 días.** Antes de eso el público
es demasiado pequeño y te comes el presupuesto del frío.

Por debajo de 10 €/día no hay campaña que valga: no se generan datos suficientes para decidir nada.

### Reglas de matar y escalar

- **No toques nada los primeros 3–4 días.** Fase de aprendizaje.
- **Matar anuncio:** 1.500 impresiones o 10 € gastados sin un solo "añadir al carrito".
- **Matar anuncio:** 3× tu CPA objetivo gastado con 0 compras.
- **Escalar:** +20–30 % de presupuesto cada 3 días si el conjunto está por debajo del CPA objetivo.
  Nunca dupliques de golpe: reinicia el aprendizaje.
- **Refresco creativo:** 2–3 anuncios nuevos por semana. La fatiga creativa llega en 7–14 días
  con presupuesto bajo.

### KPIs de referencia (producto digital de ticket bajo)

| Métrica | Umbral sano |
|---|---|
| Hook rate (repr. 3 s / impresiones) | > 25 % |
| CTR (enlace) | > 1,5 % |
| CPC (enlace) | < 0,50 € |
| Landing → checkout iniciado | > 8 % |
| CPA | < 60 % del ticket medio (AOV) |

---

## 2. El problema real: un eBook a 9,90 € no aguanta el coste de adquisición

Con tráfico frío en Meta, un CPA realista para producto digital de ticket bajo está en **6–12 €**.
Si vendes un libro a 9,90 € sin nada más, estás en break-even o en pérdida. El negocio no está en
el precio del libro, está en el **ticket medio**.

### Embudo recomendado

```
Anuncio → Landing Libro A (9,90 €)
            └── Order bump en el checkout: "Añade el Libro B por +6,90 €"   [tasa típica 25–35 %]
                  └── Upsell post-compra: Club Tremdora, primer mes 1 €      [tasa típica 8–15 %]
```

Con esos ratios el AOV pasa de 9,90 € a ~**15–18 €**, y un CPA de 8–10 € sí es rentable.

**El order bump es la pieza que hace viable todo el plan.** Es también la forma de "abrir más campo
de posibilidades de venta con dos temas diferentes" sin duplicar la inversión publicitaria: el
segundo tema se vende gratis, dentro del checkout del primero.

---

## 3. "Un libro nuevo cada mes" → conviértelo en suscripción

Es la recomendación estratégica más importante de este documento.

Si lanzas 12 libros sueltos, pagas coste de adquisición **12 veces**. Si vendes el acceso, pagas
**una vez** y cobras 12.

> **Club Tremdora — 7,90 €/mes**
> Una guía nueva cada mes sobre un problema real de convivencia con tu mascota.
> Acceso inmediato a todo el archivo publicado. Cancela cuando quieras.

Por qué esto resuelve exactamente lo que buscas:

- **Solvencia**: ingreso recurrente y predecible. Con 150 socios son ~1.185 €/mes de caja fija —
  eso es lo que financia las cajas físicas sin descapitalizarte.
- **Menor riesgo de caja**: sabes en octubre cuánto vas a facturar en noviembre.
- **Cada libro mensual deja de ser un lanzamiento a vida o muerte** y pasa a ser contenido de
  retención. Baja la presión.
- **Lista de email propia**: es el activo que hace que las cajas físicas se vendan casi sin ads.

Los libros sueltos siguen vendiéndose en la web (front-end de captación); el Club es el back-end.

### Calendario editorial 12 meses (problemas cotidianos, alineado a estacionalidad)

| Mes | Tema | Por qué ese mes |
|---|---|---|
| Oct | Ansiedad por separación | Vuelta a la oficina tras verano |
| Nov | Tirar de la correa / paseo bajo control | Evergreen, alto volumen de búsqueda |
| Dic | Navidad segura: comida prohibida, adornos, visitas | Alimenta la caja de Navidad |
| Ene | Sobrepeso y alimentación: propósitos de año nuevo | Estacional fuerte |
| Feb | Cachorro: los primeros 90 días | Camadas de invierno |
| Mar | Ladridos excesivos y vecinos | Evergreen |
| Abr | Higiene dental y cuidados en casa | Evergreen |
| May | Convivencia con niños y con otros animales | Pre-verano |
| Jun | Miedo a petardos y tormentas | San Juan / verbenas |
| Jul | Golpe de calor y viajes con mascota | Estacional crítico |
| Ago | Perro senior: señales y cuidados | Evergreen |
| Sep | Rutina, soledad y vuelta al cole | Cierra el ciclo |

Regla: **el libro del mes es también el ángulo publicitario del mes.** Un solo mensaje, coherente
en ads, email y web.

---

## 4. Caja de Navidad: ¿llegas con el presupuesto?

### Cuenta atrás (hoy: 10 sep)

| Hito | Fecha límite |
|---|---|
| Entrega al cliente antes de Nochebuena | 22 dic |
| Última fecha de envío (península, con margen) | **15–17 dic** |
| Cajas montadas y en tu poder | **1 dic** |
| Pedido en firme al proveedor (3–5 sem. producción + envío) | **20–25 oct** |
| Decisión GO / NO-GO con dinero en mano | **15 de octubre** |

**Tienes 5 semanas de venta digital para generar la caja necesaria.** Es ajustado pero llegas —
si eliminas el riesgo de inventario.

### La solución: preventa. No compres stock, véndelo antes.

1. **Abre preventa del 1 al 20 de noviembre**, con unidades limitadas ("solo 100 cajas").
2. Cobras al 100 % en la preventa.
3. **Haces el pedido al proveedor con el dinero de tus clientes**, ya sabiendo la cantidad exacta.
4. Riesgo de inventario: cero. Necesidad de capital propio: casi cero.

Comunica siempre y de forma visible la fecha de entrega estimada ("recíbelo antes del 22 de
diciembre") y una política de reembolso clara si no llegas. La preventa solo funciona con
transparencia; si se retrasa el proveedor, el cliente tiene que enterarse por ti antes que por
el calendario.

### Simplifica la caja v1 (esto es lo que te hace llegar a tiempo y a presupuesto)

No hagas caja rígida con impresión personalizada el primer año: 4–6 semanas de plazo y MOQ de 300+.

| Componente | Opción cara | Opción v1 |
|---|---|---|
| Caja | Rígida impresa a medida | Caja kraft de stock + faja/sleeve impreso |
| Personalización | Impresión a 4 tintas | Pegatina + tarjeta impresa en digital |
| Contenido | 6–8 artículos | 3–4 artículos + guía impresa + acceso al Club |
| MOQ | 300 uds | 50–100 uds |
| Coste/unidad | 22–28 € | **10–14 €** |

Con COGS de 12 € y PVP de 42 € + 4,90 € de envío, el margen bruto por caja es ~30 €. Con 100 cajas
son ~3.000 € de margen. Eso es lo que arranca la caja de cumpleaños en enero.

### Recomendación contraria a tu orden previsto

Tú planteas: digital → caja cumpleaños → experiencia → Navidad si llegas.

**Yo invertiría el orden de las dos cajas.** Razón: la caja de cumpleaños es *evergreen*, no tiene
fecha de caducidad — si sale en enero no pierdes nada. La de Navidad tiene una ventana de 6 semanas
al año y una tasa de conversión 3–4× superior porque compite en el mercado de regalos, no en el de
capricho propio.

Si solo puedes hacer una caja en 2026, que sea la de Navidad. La de cumpleaños la lanzas en enero
con el dinero de la de Navidad y con la lista de email que la de Navidad te habrá construido.

---

## 5. Plan de ejecución (semana a semana)

### Semanas 1–2 (10–24 sep) — Encender el digital
- [ ] Landing por libro + checkout con **order bump** del otro libro. Sin bump no arranques.
- [ ] Píxel de Meta instalado + API de Conversiones. Verifica eventos: ViewContent, AddToCart, Purchase.
- [ ] 6 creativos (3 ángulos × 2 libros). Prioriza vídeo vertical UGC de 20–30 s.
- [ ] Lanzar campaña: 1 campaña / 1 conjunto / 6 anuncios / 15–20 €/día.
- [ ] Secuencia de email para compradores (5 correos): entrega → uso → problema siguiente → Club → oferta.

### Semanas 3–5 (25 sep – 15 oct) — Optimizar y decidir
- [ ] Matar perdedores, 2–3 creativos nuevos por semana.
- [ ] Lanzar el **Club Tremdora** como upsell post-compra.
- [ ] Publicar el libro de octubre (Ansiedad por separación).
- [ ] Cotizar proveedores de la caja: pedir 3 presupuestos con plazo real de producción por escrito.
- [ ] **15 oct: decisión GO/NO-GO de Navidad**, con este criterio:
      GO si (caja acumulada de ads ≥ 800 €) **y** (proveedor confirma entrega antes del 1 dic).

### Semanas 6–8 (16 oct – 5 nov) — Preparar Navidad
- [ ] Cerrar proveedor y bloquear producción (sin pagar aún, o con señal mínima).
- [ ] Fotos y landing de la caja. Contenido de la caja definido y cerrado.
- [ ] Calentar la lista: 3 emails de "algo viene" + lista de espera con acceso anticipado.
- [ ] Publicar el libro de noviembre.

### Semanas 9–11 (1–20 nov) — Preventa
- [ ] Abrir preventa, 100 uds, con contador visible.
- [ ] Ads a la caja: conjunto propio, 3–4 anuncios, ~25 €/día. Público: compradores de eBooks +
      lookalike 1 % de compradores + amplio.
- [ ] **20 nov: cierre de preventa y pedido en firme al proveedor.**

### Semanas 12–14 (21 nov – 17 dic) — Cumplir
- [ ] Recepción, montaje, envíos escalonados. Nada sale después del 17 dic.
- [ ] Black Friday (27 nov): oferta del pack digital, NO descuentes la caja (rompe el margen).
- [ ] Libro de diciembre (Navidad segura) como regalo para compradores de la caja.

### Enero
- [ ] Caja de cumpleaños, financiada con el margen de Navidad, ya con lista de email construida.

---

## 6. Semáforo de riesgos

| Riesgo | Señal de alarma | Acción |
|---|---|---|
| CPA por encima del AOV | Semana 2 con CPA > 12 € | Parar escalado, arreglar el bump antes que el anuncio |
| Proveedor no confirma plazo por escrito | Antes del 15 oct | NO-GO Navidad. Va a enero como caja de cumpleaños |
| Preventa por debajo del 40 % del objetivo el día 10 | 10 nov | Reducir tirada al número vendido, no forzar el mínimo |
| Fatiga creativa | Frecuencia > 2,5 y CTR cayendo | 3 creativos nuevos, no subir presupuesto |
| Caja sin margen | COGS + envío > 45 % del PVP | Recortar contenido, no subir precio |

---

## 7. Resumen en cinco frases

1. **6 anuncios, 1 conjunto, 1 campaña, 15–20 €/día.** Los dos libros compiten en el mismo conjunto.
2. **Sin order bump no lances**: un eBook de 9,90 € solo no paga su propio coste de adquisición.
3. **Convierte "un libro cada mes" en una suscripción de 7,90 €/mes.** Ahí está la solvencia real.
4. **Navidad se hace en preventa o no se hace.** Decisión el 15 de octubre, pedido el 20–25 de octubre.
5. **Navidad antes que cumpleaños**: la de cumpleaños puede esperar a enero sin perder nada.
