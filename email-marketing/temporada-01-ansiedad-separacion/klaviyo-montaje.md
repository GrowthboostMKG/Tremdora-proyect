# Montaje en Klaviyo — Temporada 1

Estado a fecha de creación. Cuenta Klaviyo `RhM862` · Tienda Shopify `tremdora.com`.

---

## 1. Corrección importante: esto NO son campañas programadas

La pregunta original era "programar día y hora de envío de cada email". En Klaviyo eso
son **Campaigns**, y para esta secuencia sería el montaje equivocado.

| | Campaign | **Flow** ← lo correcto aquí |
|---|---|---|
| Se envía | En una fecha y hora absolutas | X tiempo después de que la persona se suscriba |
| Sirve para | Newsletter puntual, promoción, lanzamiento | Secuencias evergreen |
| Si alguien se suscribe mañana | Se perdió todo lo anterior | Empieza por el E01, como todo el mundo |

Una temporada evergreen tiene que arrancar en el **día 0 de cada suscriptor**, no en una
fecha del calendario. Si fueran 13 campañas programadas, quien se apuntara el día 20
recibiría el episodio 9 sin haber visto los ocho anteriores, y la serialización —que es
justo lo que hace funcionar el formato— se rompería.

Por eso está montado como **Flow con retardos entre emails**.

---

## 2. Lo que está creado

**Lista:** `Newsletter Tremdora — Mascotas` · ID `X8UJKA` · **double opt-in**

**Flow:** `Temporada 1 — Ansiedad por separación (13 emails / 30 días)` · ID `UxY3Uf`
- Estado: **BORRADOR** (no puede enviar nada)
- Disparador: *Added to List* → `Newsletter Tremdora — Mascotas`
- Reentrada: desactivada (nadie repite la temporada)
- Todos los mensajes en estado `draft`, con asunto y preheader ya cargados

### Calendario real montado

| # | Retardo desde el anterior | Día acumulado | Hora | Asunto |
|---|---|---|---|---|
| E01 | inmediato al suscribirse | 0 | — | El vídeo que Elena no quería ver |
| E02 | 2 días | 2 | 07:15 | El manojo de llaves |
| E03 | 2 días | 4 | 07:15 | La cara de culpa que no era culpa |
| E04 | 3 días | 7 | 07:15 | Tu perro huele el tiempo |
| E05 | 2 días | 9 | 07:15 | Lo que Skinner vería en tus despedidas |
| E06 | 3 días | 12 | 07:15 | El día que todo empeoró |
| E07 | 2 días | 14 | 07:15 | ¿Y si no es ansiedad? ¿Y si le duele? |
| E08 | 3 días | 17 | 07:15 | El miedo no se apaga con calma |
| E09 | 2 días | 19 | 07:15 | Tu estrés viaja por la correa |
| E10 | 3 días | 22 | 07:15 | Este episodio no va de tu perro |
| E11 | 3 días | 25 | 07:15 | Lo que unos gansos austríacos… |
| E12 | 3 días | 28 | 07:15 | El vídeo que sí quería ver (finale) |
| E13 | 2 días | 30 | 07:15 | Escena post-créditos |

**Por qué el E01 sale inmediato y no a las 07:15:** el primer email de bienvenida es el
que más se abre de toda la secuencia, y se abre porque llega cuando la persona acaba de
darte su correo y se acuerda de ti. Retenerlo hasta la mañana siguiente tira esa ventaja
a la basura. A partir del E02, las 07:15 sí tienen sentido: es la hora en que el lector
está a punto de salir de casa y dejar al perro solo.

**Zona horaria:** configurada como *la del perfil*. Quien tenga zona horaria conocida
recibe a las 07:15 de su hora local; el resto usa la de la cuenta.

⚠️ La cuenta de Klaviyo está en `Europe/Berlin` y la tienda en España. Mismo horario
todo el año, así que no rompe nada — pero conviene cambiarla a `Europe/Madrid` en
Settings → Account para evitar confusiones futuras.

**Deriva de hasta 24 h:** un retardo de "2 días + esperar a las 07:15" se cuenta desde el
momento exacto de la suscripción. Quien se apunte a las 20:00 recibirá el E02 en la
mañana del día 3, no del día 2. Es el comportamiento normal de Klaviyo y no merece la
pena corregirlo.

---

## 3. ⚠️ Bloqueantes antes de poder enviar

Ninguno de estos lo puede resolver la API. Son de panel.

| # | Bloqueante | Dónde | Por qué importa |
|---|---|---|---|
| 1 | **No hay dominio de envío verificado** | Settings → Domains | Sin DKIM/SPF sobre un dominio propio, envías desde infraestructura compartida. Con una lista nueva es la vía rápida a la carpeta de spam. |
| 2 | **Falta la dirección postal de la organización** | Settings → Account | Es obligatoria por ley en el pie de todo email comercial (CAN-SPAM, y la normativa europea equivalente). Klaviyo bloquea el envío sin ella. |
| 3 | **Remitente con posible errata** | Settings → Email | Los mensajes salen como **"TREMADORA SHOP" \<info@tremdorashop.com\>**. La tienda es *Tremdora* (tremdora.com). Reviso: parece una errata en el nombre, y además el dominio del remitente no coincide con el de la tienda. Aparece en cada bandeja de entrada: verifícalo antes de activar. |
| 4 | **Los 13 emails no tienen plantilla** | Editor del flow | Están creados con asunto y preheader, pero sin cuerpo. El copy está en `emails/E01…E13.md`. |
| 5 | **Shopify NO está sincronizando con Klaviyo** | Ver sección 4 | Hay 3 suscriptores en Shopify que Klaviyo no ve. |

---

## 4. El formulario de Shopify no llega a Klaviyo

Comprobado: la tienda tiene **3 contactos con marketing aceptado**, y la cuenta de
Klaviyo tiene **0 perfiles y 0 listas**. Es decir, quien se suscriba hoy en tremdora.com
entra en la lista de clientes de Shopify y **no entra en el flow**.

Dos opciones para arreglarlo:

**Opción A — Instalar la integración oficial Klaviyo ↔ Shopify (recomendada)**
Klaviyo sincroniza clientes, pedidos y eventos de navegación. Ojo: la integración manda
los suscriptores a la lista que le indiques, así que hay que apuntarla a
`Newsletter Tremdora — Mascotas` (`X8UJKA`) o el flow no se disparará.
Como extra, desbloquea carrito abandonado y navegación abandonada, que en una tienda
con ebooks suelen rendir más que cualquier campaña.

**Opción B — Sustituir el formulario nativo por un formulario de Klaviyo**
Klaviyo Forms (popup o embebido) escribiendo directamente en la lista. Más control sobre
el double opt-in y sobre qué campos capturas, pero pierdes la sincronización de pedidos.

En ambos casos: los 3 contactos que ya están en Shopify hay que decidir si entran o no.
**Recomendación: no los metas en el flow todavía.** Uno es tu propia dirección y los
otros dos son de junio, sin pedidos y sin relación previa contigo. Mándales primero un
email suelto pidiendo confirmación.

---

## 5. Orden de trabajo sugerido

1. Verificar dominio de envío y esperar propagación de DNS.
2. Rellenar dirección postal de la organización.
3. Corregir el nombre y el correo del remitente.
4. Conectar Shopify → lista `X8UJKA`.
5. Maquetar las 13 plantillas con el copy de `emails/`.
6. **Probar el flow entero contigo mismo** antes de activarlo: cambia temporalmente los
   retardos a minutos, suscríbete, comprueba los 13 emails, y devuelve los retardos a
   días. Este paso no es opcional.
7. Pasar el flow de borrador a **Live** — y con él, cada uno de los 13 mensajes, que
   tienen su propio estado. **Un flow activo con mensajes en borrador no envía nada:**
   es el fallo más común al estrenar una secuencia en Klaviyo.

---

## 6. Repetir esto para las Temporadas 2-6

Cada temporada es un flow nuevo con su propia lista o su propio segmento, y la misma
estructura de retardos. Si las encadenas, el E13 de cada temporada debería añadir a la
persona a la lista disparadora de la siguiente mediante una acción de *List Update*.
