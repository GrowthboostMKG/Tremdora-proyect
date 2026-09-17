# 12. Montar Meta desde cero — paso a paso

> Todo esto se puede hacer **desde el extranjero y sin estar dada de alta todavía**. Crear la estructura y el píxel no requiere ser autónoma; solo gastar y vender lo requiere. Es trabajo útil mientras esperas el aplazamiento.

## Aclaración previa: el píxel no se "pide"

El píxel (Meta lo llama ahora **conjunto de datos**) vive en el **portfolio empresarial**, no en la cuenta publicitaria. Se puede asignar a la cuenta publicitaria que quieras, y sus datos sobreviven aunque crees otra cuenta.

Lo que sí se pierde al crear una cuenta publicitaria nueva es **el historial de esa cuenta**: pagos, campañas y la confianza de facturación acumulada. Por eso importa acertar a la primera con moneda y zona horaria — no porque se pierdan los datos del píxel.

---

## PASO 0 — Comprueba qué existe ya

Con Shopify montado **es posible que ya haya un píxel creado**. Crear un segundo parte los datos en dos y ninguno sirve.

- [ ] Shopify → *Configuración → Aplicaciones y canales de venta*
- [ ] ¿Está la app **"Facebook e Instagram"** instalada? Si sí, ábrela y anota **qué píxel y qué cuenta publicitaria** tiene conectados
- [ ] Si no hay nada, empieza por la Fase 1

---

## FASE 1 — La estructura · ~40 min

El orden importa: cada paso necesita el anterior.

- [ ] **1. Perfil personal de Facebook.** Usa **el de siempre**, no crees uno nuevo: los perfiles recién creados que abren cuentas publicitarias son la causa número uno de bloqueos
- [ ] **2. Página de Facebook de TREMDORA** — *Páginas → Crear nueva página*. Categoría: tienda de mascotas. Sin página no puedes anunciarte
- [ ] **3. Instagram profesional** — *Configuración → Tipo de cuenta → Cuenta profesional → Empresa*
- [ ] **4. Portfolio empresarial** (antes "Business Manager") en **business.facebook.com** → *Crear cuenta*. Usa un email de la marca, no el personal
- [ ] **5. Verificación en dos pasos (2FA)** — obligatoria para administrar, y te protege de un robo de cuenta con dinero dentro
- [ ] **6. Mete Página e Instagram en el portfolio** — *Configuración del negocio → Cuentas → Páginas → Añadir*, y lo mismo en *Cuentas de Instagram*

---

## FASE 2 — La cuenta publicitaria · ~15 min

- [ ] **7.** *Configuración del negocio* → **Cuentas publicitarias** → *Añadir* → **"Crear una cuenta publicitaria nueva"**

**8. ⚠️ Las dos decisiones irreversibles:**

| Campo | Valor |
|---|---|
| Nombre | TREMDORA |
| **Zona horaria** | **(GMT+1) Madrid** |
| **Moneda** | **EUR** |

Cambiarlas después obliga a crear otra cuenta desde cero. Aunque pagues con tarjeta extranjera, pon EUR: facturas en euros y tus informes tienen que estar en euros.

- [ ] **9.** ¿Para tu negocio o para un cliente? → **para tu propio negocio**
- [ ] **10.** Asígnate **"Administrar cuenta publicitaria"** (acceso total)
- [ ] **11.** *Configuración de pagos* → *Añadir método de pago*
- [ ] **12. Límite de gasto de la cuenta: 500 €**, antes de crear ninguna campaña

---

## FASE 3 — El píxel · ~30 min · la parte que más gente hace mal

- [ ] **13.** *Administrador de eventos* → *Conectar orígenes de datos* → **Web** → crear **conjunto de datos**. Nómbralo "TREMDORA Web" y anota el ID
- [ ] **14. Conexión con Shopify — sin tocar código.** Instala en Shopify la app oficial **"Facebook e Instagram" de Meta**, conecta portfolio y píxel, y en el nivel de intercambio de datos de clientes elige **el máximo ("Enhanced" / "Máximo")**

> Ese nivel activa el píxel **y la API de Conversiones a la vez**. La API envía las compras de servidor a servidor, así que no la bloquean los bloqueadores del navegador: es la diferencia entre ver el 70 % de tus conversiones o el 100 %. Sin ella optimizas a ciegas.

- [ ] **15. Asigna el píxel a la cuenta publicitaria** — *Configuración del negocio → Orígenes de datos → Conjuntos de datos → Asignar activos → tu cuenta publicitaria*. **Este paso se olvida muchísimo** y sin él la cuenta no puede usar el píxel
- [ ] **16. Verifica el dominio** — *Configuración del negocio → Seguridad de la marca → Dominios*. Te da un código que pegas en Shopify (*Preferencias → metaetiquetas*)
- [ ] **17. Eventos priorizados** — *Administrador de eventos → tu conjunto de datos → Configuración de eventos web agregados*. **"Compra" en el puesto 1**
- [ ] **18. LA PRUEBA QUE NO TE PUEDES SALTAR.** Crea un producto oculto de 1 €, cómpralo de verdad y comprueba en el *Administrador de eventos* que llega el evento **"Compra" con el valor correcto**

> Si el paso 18 no funciona, todo lo demás da igual: estarías pagando publicidad sin poder medir nada.

---

## FASE 4 — Calentar la cuenta antes de gastar

Las cuentas nuevas que empiezan a gastar de golpe son las que Meta bloquea.

- [ ] Primeros **3-4 días a 5-8 €/día**, y de ahí subes a los 15 €
- [ ] No crear y borrar campañas compulsivamente los primeros días
- [ ] Datos coherentes: nombre real, negocio real, dominio que coincide

**Nota por trabajar fuera de España:** vas a crear una cuenta española desde una IP extranjera y después viajarás. A Meta eso a veces le llama la atención. No suele ser problema, pero **accede siempre desde el mismo dispositivo y navegador** y no alternes mucho. Con 2FA activado el riesgo baja bastante.

---

## Presupuesto: cómo evitar que se dispare

**Capa 1 — presupuesto diario, por campaña (nunca por cuenta):**

| Campaña | Diario |
|---|---|
| Captación (laboratorio de creativos) | 9 € |
| Venta | 6 € |
| **Total** | **15 €/día** |

> **Error más común:** duplicar una campaña para probar algo y dejarse las dos encendidas a 15 € = 30 €/día. Revisa siempre la suma de lo que tienes activo.

**Capa 2 — límite de gasto de la cuenta: 500 €.** Tope duro sobre toda la cuenta; al alcanzarse, Meta **pausa todos los anuncios**. Es acumulativo desde que lo pones, no mensual: hay que restablecerlo a mano cada mes, lo que te obliga a revisar antes de seguir.

**El 25 % diario.** Meta puede gastar hasta un 25 % más en un día concreto (hasta 18,75 € con 15 €/día), pero **se compensa dentro de la semana natural**: nunca más de 105 €/semana.

**El umbral de facturación no es gasto, es cuándo te cobran.** Meta cobra al acumular cierto importe (al principio ~25 €) o a fin de mes, lo que llegue antes. Con 15 €/día verás un cargo cada dos días al principio. Son muchos cargos pequeños, no cargos extra. Se puede subir el umbral en *Configuración de pagos*.

**Alternativa de tope absoluto: pago manual / prepago.** Cargas 100 € y no puedes gastar 101 €. Contras: los anuncios **se paran en seco** al agotarse el saldo (puede romperte un test a mitad) y con pago manual **no puedes poner límite de gasto de la cuenta**.
