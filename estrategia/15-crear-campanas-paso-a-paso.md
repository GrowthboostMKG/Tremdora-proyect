# 15. Crear las campañas y subir los anuncios — clic a clic

> Continuación del documento 12. Aquí la cuenta y el píxel ya están montados y la compra de prueba ya funciona. **Si el evento "Compra" todavía no llega correctamente, no sigas: vuelve al paso 18 del documento 12.**

Vas a crear **dos campañas**. Te llevará unos 45 minutos la primera vez.

---

## CAMPAÑA A — Captación · 9 €/día

Es tu laboratorio de creativos: aquí aprendes qué ángulo funciona a 1,35 € el lead en lugar de a 45 € la compra.

### Nivel 1 — La campaña

1. Entra en **Administrador de anuncios** → botón verde **"Crear"**
2. Objetivo: **"Clientes potenciales"**
3. Nombre de la campaña: `CAPTACION | Frecuencia + 12 Señales`
4. **Deja desactivada** la optimización del presupuesto de la campaña (así controlas el presupuesto en el nivel de abajo)
5. Siguiente

### Nivel 2 — El conjunto de anuncios

6. Nombre: `Amplio ES 25-55`
7. **Ubicación de conversión: "Sitio web"** (no "Formularios instantáneos" — quieres el email en tu Klaviyo, no dentro de Meta)
8. **Evento de conversión:** el de tu página de gracias de la muestra gratis (normalmente *Cliente potencial* o *Lead*)
9. **Presupuesto diario: 9 €**
10. Fecha de inicio: hoy. **Sin fecha de fin**
11. **Público:**
    - Ubicación: **España**
    - Edad: **25-55**
    - Sexo: todos
    - **Intereses: NINGUNO.** Déjalo vacío
12. **Ubicaciones: automáticas (Advantage+)**
13. Siguiente

> **Por qué sin intereses:** con 9 €/día, segmentar estrecha el alcance y encarece el CPM sin mejorar nada. En 2026 el algoritmo encuentra a tu público mejor que tú si le das buena creatividad. **Testeas ángulos, no públicos.**

### Nivel 3 — Los anuncios

Repites esto **3 veces**, uno por cada vídeo (1, 2 y 3 del documento 14):

14. Nombre del anuncio: `V1 Frecuencia accion` (que el nombre diga qué es — dentro de dos semanas no te acordarás)
15. Identidad: tu **Página de Facebook** y tu **cuenta de Instagram**
16. Formato: **Imagen o vídeo única**
17. **Subir el vídeo** → recorta a 9:16 si hace falta
18. **Texto principal:** el copy del documento 04 o 05 según el producto
19. **Titular:** corto, 5-7 palabras (*"Escucha la Frecuencia de Calma"*)
20. **Enlace:** la URL de tu landing de muestra gratis
21. **Llamada a la acción: "Más información"** (convierte mejor que "Descargar" en frío)
22. **Comprueba abajo que el píxel está activado** en "Seguimiento de eventos"
23. **Publicar**

---

## CAMPAÑA B — Venta · 6 €/día

24. **Crear** → Objetivo: **"Ventas"**
25. Nombre: `VENTA | Edad Dorada`
26. Conjunto: `Amplio ES 30-65`
    - **Evento de conversión: "Compra"**
    - **Presupuesto diario: 6 €**
    - España · **30-65** · sin intereses · ubicaciones automáticas
27. Dos anuncios: los vídeos **4 y 5** del documento 14
28. **Enlace: la página de producto de Edad Dorada**, no la home
29. **Llamada a la acción: "Comprar"**
30. Publicar

> **Edad 30-65 aquí y 25-55 en captación** porque el comprador de Edad Dorada es mayor que el de Hogar en Calma. No es una segmentación fina: es quitar de en medio a quien seguro no compra.

---

## Antes de darle a publicar — revisa estas 6 cosas

- [ ] La suma de presupuestos diarios es **15 €**, no más (mira las dos campañas juntas)
- [ ] El **límite de gasto de la cuenta está en 500 €**
- [ ] Los enlaces abren la página correcta **en el móvil**
- [ ] Los vídeos llevan **subtítulos**
- [ ] El píxel aparece activado en los dos conjuntos
- [ ] **Has hecho la compra de prueba** y el evento llegó bien

---

## Los primeros 7 días: no toques nada

A 3 €/día por anuncio, cualquier dato de menos de una semana es ruido estadístico. Tocar la cuenta a diario es lo que más dinero cuesta con presupuesto bajo.

| Día | Qué haces |
|---|---|
| 1-3 | **Nada.** Mira si quieres, pero no cambies nada |
| 4 | Primer vistazo al *hook rate* por anuncio. Sin decidir todavía |
| 7 | **Primera decisión:** apagar lo que cumpla criterio de matar, y grabar hooks nuevos del mejor |

**Matar un anuncio:** *hook rate* < 15 % con 1.500 impresiones, o coste por lead > 3 € tras 25 € gastados.
**Mantener:** *hook rate* > 25 %, aunque todavía no haya ventas.

> **Arranque suave:** los primeros 3-4 días pon 5 €/día en captación y 3 €/día en venta, y de ahí subes a 9 y 6. Las cuentas nuevas que empiezan a gastar de golpe son las que Meta bloquea.

---

## Dónde se miran las métricas

En el Administrador de anuncios, en el nivel de **Anuncios**, pulsa **"Columnas" → "Personalizar columnas"** y deja solo estas:

| Columna | Qué te dice |
|---|---|
| Importe gastado | Cuánto llevas |
| Impresiones | Si hay datos suficientes para juzgar |
| **Reproducciones de 3 segundos** | Con las impresiones, te da el *hook rate* |
| **CTR (porcentaje de clics en el enlace)** | Si el ángulo conecta |
| **Clientes potenciales** o **Compras** | El resultado |
| **Coste por resultado** | Tu CPL o tu CPA |

Guarda ese conjunto de columnas como preajuste. **Hook rate** = reproducciones de 3 s ÷ impresiones; Meta no te lo da hecho, lo calculas tú.

---

## El árbol de decisión de cada lunes

```
¿Hook rate < 20 %?          → El problema es EL PRIMER SEGUNDO. Graba 4 hooks nuevos.
¿Hook bien, CTR < 1 %?      → El problema es EL ÁNGULO. No conecta con un dolor real.
¿CTR bien, pocos leads?     → El problema es LA LANDING. Arregla la página, no el anuncio.
```

Nunca cambies las tres cosas a la vez: si lo haces, no sabrás qué funcionó.
