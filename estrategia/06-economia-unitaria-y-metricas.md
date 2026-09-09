# 6. Economía unitaria, métricas y reglas de decisión

Este es el documento que separa "hacer marketing" de "ser Growth Partner". Si solo lees uno, que sea este.

## 6.1 Tu unidad económica

Supuestos de trabajo (**sustituye por tus números reales antes de encender nada**):

| Concepto | Sin palancas AOV | **Con bumps + upsell** |
|---|---|---|
| AOV | 62,00 € | **78,00 €** |
| Coste del producto (COGS) | −18,60 € | −18,60 € *(el digital no añade coste)* |
| Envío + packaging | −5,00 € | −5,00 € |
| Comisiones de pago (~1,7 %) | −1,05 € | −1,33 € |
| Apps / plataforma por pedido | −1,00 € | −1,00 € |
| **Margen de contribución** | **36,35 €** | **52,07 €** |
| **CAC máximo (break-even)** | **36,35 €** | **52,07 €** |
| **ROAS de break-even** | **1,71** | **1,50** |

> **Lee esto dos veces:** añadir contenido digital sin coste marginal sube tu CAC asumible un **43 %** y baja tu ROAS de equilibrio de 1,71 a 1,50. Puedes pagar 52 € por un cliente donde tu competencia solo puede pagar 36 €. **Esa es tu ventaja, y es gratis.**

**Objetivo de rentabilidad sana:** CAC ≤ 60 % del margen de contribución → **CAC objetivo ≈ 31 €** con AOV 78 €. Eso deja ~21 € de beneficio por pedido para reinvertir.

## 6.2 Proyección realista a 90 días (escenario base)

| | **Mes 1** | **Mes 2** | **Mes 3** |
|---|---|---|---|
| Inversión en ads | 1.200 € | 1.200 € | 1.200 € |
| CTR (enlace) | 1,2 % | 1,7 % | 1,9 % |
| CVR de la tienda | 1,3 % | 2,2 % | 2,5 % |
| Pedidos de pago | ~19 | ~41 | ~48 |
| **CPA** | **63 €** | **29 €** | **25 €** |
| AOV | 68 € | 76 € | 78 € |
| Ingresos de pago | 1.292 € | 3.116 € | 3.744 € |
| Ingresos de email | ~0 € | ~310 € | ~1.100 € |
| **Ingresos totales** | **~1.290 €** | **~3.430 €** | **~4.840 €** |
| Margen tras ads | **−420 €** | **+690 €** | **+1.700 €** |
| Emails en lista | ~250 | ~550 | ~950 |

**El mes 1 pierde dinero y está bien.** Estás comprando datos del píxel y creativos validados. El error que arruina el 90 % de los lanzamientos es apagar los anuncios en la semana 3 porque "no es rentable".

**Escenario conservador:** desplaza todo un mes (el mes 2 se parece al mes 1). **Escenario optimista:** un creativo se dispara en orgánico y el mes 2 ya va a CPA 22 €.

⚠️ *Son proyecciones basadas en benchmarks del mercado español, no promesas. Tu CPM, tu CVR y tu COGS reales mandan.*

## 6.3 El cuadro de mando semanal (7 números, cada lunes)

Abre una hoja de cálculo. Estos 7 números y ninguno más:

| # | Métrica | Cómo se calcula | Objetivo mes 1 | Objetivo mes 3 |
|---|---|---|---|---|
| 1 | **Hook rate** | Repr. 3 s ÷ impresiones | > 25 % | > 30 % |
| 2 | **CTR (enlace)** | Clics enlace ÷ impresiones | > 1,2 % | > 1,8 % |
| 3 | **CVR de tienda** | Pedidos ÷ sesiones | > 1,3 % | > 2,5 % |
| 4 | **CPA** | Gasto ÷ pedidos | < 63 € | **< 31 €** |
| 5 | **AOV** | Ingresos ÷ pedidos | > 65 € | **> 78 €** |
| 6 | **MER** (ROAS global) | Ingresos totales ÷ gasto total en ads | > 1,1 | **> 3,0** |
| 7 | **% ingresos de email** | Ingresos email ÷ ingresos totales | — | **> 20 %** |

> **MER es tu métrica reina**, no el ROAS que te muestra Meta. Meta se atribuye ventas que habrías hecho igual. El MER (ingresos totales de Shopify ÷ gasto total en ads) no miente.

## 6.4 Reglas de decisión: cuándo matar y cuándo escalar

Sin reglas escritas de antemano, decidirás con el estómago y a las 23:00. Escríbelas ahora.

### Matar un anuncio
- **Gasto ≥ 1,5 × break-even CAC (≈ 78 €) y 0 pedidos** → apagar
- **Hook rate < 15 % con 2.000+ impresiones** → apagar (el problema es el hook, no la oferta)
- **CTR < 0,7 % con 2.000+ impresiones** → apagar
- **Buen CTR pero CVR < 0,5 %** → el anuncio funciona, **el problema es tu PDP**. No lo apagues: arregla la página.

### Escalar un anuncio
- **CPA < 31 € durante 3 días seguidos** → sube el presupuesto un **20 %, no más**, y espera 48 h
- Nunca subas más de un 20-30 % al día: reinicias la fase de aprendizaje y quemas el rendimiento
- Nunca escales y cambies la creatividad el mismo día: no sabrás qué causó qué

### Tocar la cuenta
- **Máximo un cambio cada 72 h.** El instinto de "optimizar" a diario es el enemigo nº 1 de una cuenta con presupuesto bajo.
- Con 40 €/día, cualquier dato de menos de 3 días es ruido estadístico. No reacciones a él.

## 6.5 La regla de los 3 diagnósticos

Cuando algo no funciona, el problema **siempre** está en uno de estos tres sitios. Diagnostícalo en este orden:

```
¿Hook rate bajo (<20 %)?
        └──► El problema es EL PRIMER SEGUNDO. Graba 5 hooks nuevos.

¿Hook rate bien pero CTR bajo (<1 %)?
        └──► El problema es EL ÁNGULO. No conecta con un dolor real.

¿CTR bien pero CVR bajo (<1 %)?
        └──► El problema es LA PÁGINA O LA OFERTA. Precio, prueba
             social, garantía o velocidad de carga.
```

Nunca cambies las tres cosas a la vez. Nunca culpes al algoritmo antes de haber pasado por este árbol.
