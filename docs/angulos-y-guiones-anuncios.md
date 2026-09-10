# Ángulos y guiones de anuncios — Hogar en Calma · Edad Dorada
### Nicho mascotas · 15 €/día · guiones listos para grabar

> Fecha: 10 de septiembre de 2026
> **Versión 2 — corregida.** La versión 1 de este documento describía los libros como productos
> de bienestar para personas. Era falso. Ver apartado 0.

---

# 0. La corrección, y qué documentos quedan invalidados

## 0.1 Qué son los libros de verdad

| Libro | Tema real |
|---|---|
| **Hogar en Calma** | Cómo tratar la **ansiedad de tu mascota** |
| **Edad Dorada** | Cómo cuidar de tu mascota cuando **ya es mayor** |

Toda la tienda es nicho mascotas.

## 0.2 De dónde salió el error

Los funnels de la rama `claude/tremdora-launch-strategy-tbbah7` abren, literalmente, así:

> *"**Supuesto de trabajo:** Hogar en Calma es un producto físico para el
> bienestar/descanso/ambiente del hogar…"*

Es una suposición declarada, no una descripción del producto. La leí como si fuera un dato
verificado y construí encima. De ahí salió el avatar equivocado, y de ahí que en la versión 1 de
este documento te dijera que los libros no iban de mascotas.

## 0.3 Qué hay que tirar y qué se conserva

**⛔ INVÁLIDOS — no los uses para nada:**

| Documento | Por qué |
|---|---|
| `estrategia/04-funnel-hogar-en-calma.md` | Avatar, ángulos, copys y lead magnet escritos para una mujer que no desconecta al llegar a casa. Nada sirve |
| `estrategia/05-funnel-edad-dorada.md` | Construido entero sobre "comprador ≠ usuario: la hija compra para su madre de 76". **En tu caso el comprador y el dueño son la misma persona.** El funnel entero está mal planteado |
| Guiones de la versión 1 de este archivo | Sustituidos por los de abajo |

**✅ SIGUEN VALIENDO:**

| Documento | Estado |
|---|---|
| `docs/manual-meta-ads-paso-a-paso.md` | Válido. Sus guiones de ejemplo eran de mascotas y apuntaban bien: "ansiedad por separación" **es** Hogar en Calma |
| `docs/paso-a-paso-meta-clic-a-clic.md` | Válido entero. Los clics de Meta no dependen del tema |
| `docs/estrategia-lanzamiento.md` | Válido, y **su calendario editorial de 12 meses es correcto**: son 12 problemas de mascotas. Hogar en Calma es el mes 1 y Edad Dorada el mes 11 |
| `landing/` | Válidos los archivos y el píxel. **Cambia los textos** por los de este documento |

## 0.4 Dos avisos que cambian de sentido con el tema real

**① La política de "atributos personales" de Meta ya no te afecta.** Te avisé de que Edad Dorada
podía tumbarte la cuenta por dar a entender la edad o la salud del que mira. Esa norma protege
**atributos del usuario**, no de su perro. La edad de un animal no es un atributo personal de
nadie. **Puedes decir "tu perro ya es mayor" sin problema.** Retira esa preocupación.

**② Pero aparece otra, y es más seria: promesas de salud animal.** Ver apartado 4.1. Esta sí
importa, legal y éticamente.

**③ El audio 432 Hz ahora tiene sentido** — es música para dejar puesta cuando sales de casa, y
eso es una categoría real: hay estudios que miden cómo la música afecta a las conductas de estrés
en perros de refugio. Lo que **no** tiene respaldo es que *432 Hz* concretamente tenga una
propiedad especial. Así que sigue en pie la corrección de forma, no de fondo:

| ❌ No | ✅ Sí |
|---|---|
| "Frecuencia sanadora de 432 Hz" | "Audio para dejar puesto cuando sales de casa" |
| "Cura la ansiedad de tu perro" | "Forma parte del protocolo de las 21 noches" |

---

# 1. Qué lanzas, en qué orden y a qué precio

| | Hogar en Calma | Edad Dorada |
|---|---|---|
| **Precio** | **39,90 €** | **49,90 €** |
| **Anuncios ahora** | **2** | **1** |
| A dónde lleva | Lead magnet completo | **Lista de espera** |
| Secuencia de email | Sí, las 6 | Ninguna todavía |

**Por qué Hogar en Calma va primero y más barato:** la ansiedad por separación es, con mucha
diferencia, el problema de conducta más buscado por dueños de perro. Es tu audiencia más ancha,
la más fácil de grabar —te sirve tu propio perro y tu propia puerta— y la que no tiene ningún
campo de minas legal. Es tu cabeza de playa: tiene que entrar el máximo de gente posible.

**Por qué Edad Dorada va segundo y más caro:** audiencia más estrecha pero mucho más intensa.
Quien tiene un perro de 13 años gasta lo que haga falta. Ahí la disposición a pagar es alta y la
sensibilidad del mensaje también, así que entra cuando ya tengas reseñas y lista.

**Y hay un tercero que ya tienes escrito.** En la rama `claude/sigue-contigo-ebooks-pptgr6` está
la serie *Sigue Contigo*, con *Ellos También se Despiden*. Junto con los otros dos te queda una
escalera emocional muy coherente para una marca de mascotas, y el tercer peldaño ya está
construido:

```
Hogar en Calma   →   Edad Dorada   →   Sigue Contigo
la ansiedad          el perro mayor     la despedida
(mes 1)              (mes 3)            (mes 5-6, o upsell)
```

Cada uno le vende al comprador del anterior, por email, con coste publicitario cero.

---

# 2. La oferta de Hogar en Calma

Contenido confirmado (de tu propia página de descargas, rama `qr-432hz-frequency-qah9fw`):

```
┌──────────────────────────────────────────────────────────┐
│  HOGAR EN CALMA — El protocolo de 21 días                │
│                                                          │
│  ✓ eBook Hogar en Calma                    valor  29 €   │
│  ✓ Diario de Bienestar — 30 días           valor  19 €   │
│  ✓ Plan Práctico de 8 Semanas              valor  24 €   │
│  ✓ Audio para dejar puesto al salir        valor   9 €   │
│  ─────────────────────────────────────────────────────   │
│  VALOR TOTAL                                      81 €   │
│  HOY                                           39,90 €   │
│                                                          │
│  🛡 30 días. Si no te sirve, te devolvemos el dinero.    │
└──────────────────────────────────────────────────────────┘
```

Son **cuatro piezas**. Eso es lo que sostiene 39,90 € y es lo que hay que enseñar en el vídeo:
un plano cenital de las cuatro cosas dice más que treinta segundos de argumentos.

> **Una duda que conviene aclarar:** tu página de descargas describe el Diario de Bienestar como
> *"30 días de reflexiones y prácticas de mindfulness"*. Si el diario es para que **el dueño**
> registre la conducta del perro (a qué hora empezó a llorar, cuánto duró, qué pasó antes), el
> ángulo del anuncio es "cada día te dice qué toca y qué apuntar", y es potentísimo. Si de verdad
> son reflexiones de mindfulness para el dueño, encaja peor en un producto de conducta canina.
> Dime cuál de las dos cosas es, porque cambia el bloque 4 de los guiones.

---

# 3. HOGAR EN CALMA — los ángulos y sus guiones

## 3.1 El avatar

**Quién:** dueño de perro, 28-55, mayoritariamente mujer, piso urbano, trabaja fuera de casa.

**El dolor real, en orden de intensidad:**
1. **Los vecinos.** Notas en el buzón, quejas al administrador, miedo real a una denuncia.
2. **La culpa.** "Le estoy haciendo daño y no sé cómo evitarlo."
3. **No poder salir.** Ni a cenar, ni un fin de semana, sin angustia todo el rato.
4. **Los destrozos.** La puerta, el marco, el sofá.
5. **La vergüenza.** No lo cuenta porque parece que es un mal dueño.

**Lo que ya ha probado y no le funcionó:** dejarle la tele o la radio, cansarlo con un paseo
largo antes de salir, el Kong relleno, juguetes nuevos, quizá un collar antiladridos, quizá una
sesión de adiestrador que no pudo permitirse repetir.

**Su objeción número uno no es el precio: es "ya lo he probado todo".** Los tres ángulos la
atacan desde sitios distintos.

---

## HC1 — "La cámara" *(este es tu anuncio principal)*

**Por qué funciona:** hoy casi todo el mundo ha puesto una cámara para ver qué hace su perro
cuando se va. Y casi todo el mundo se ha llevado el mismo susto. Es un recuerdo compartido, y por
eso el gancho para en seco.

```
[0-4 s]  A cámara, en tu casa. Tono bajo, sin dramatizar.
         "Puse una cámara para ver qué hacía mi perro cuando me iba.
          Y ojalá no la hubiera puesto."

[4-11 s] Plano de una puerta de entrada por dentro, con marcas de arañazos.
         Voz encima.
         "No estaba enfadado. No me estaba castigando.
          Llevaba cuarenta minutos jadeando y dando vueltas
          por el pasillo."

[11-19 s] Vuelta a cámara.
         "Y lo que más me costó entender es que no se arregla
          cansándolo antes de salir. Eso yo lo hacía todos los días.
          Se arregla cambiando los noventa segundos ANTES
          de coger las llaves."

[19-27 s] Plano cenital: tablet con el eBook, el diario, el plan, el altavoz.
         "Aquí está el protocolo entero: veintiún días,
          diez minutos al día, el diario para ir apuntando
          y el audio para dejarle puesto al salir."

[27-31 s] A cámara.
         "Te dejo la primera parte gratis en el enlace."
```

> **Rodaje:** el plano de los arañazos en la puerta es el que vende. Si tu puerta no los tiene,
> graba el sofá, el marco de una ventana, un cojín abierto. Tiene que haber **una prueba física**
> del problema: es lo que hace que el que mira se reconozca.

---

## HC2 — "Ya lo he probado todo" *(el que rompe la objeción principal)*

```
[0-4 s]  Cortes rápidos, uno por objeto, con rótulo. Tu voz encima.
         "La tele puesta. El paseo largo antes de salir.
          El Kong relleno. El juguete nuevo."

[4-10 s] A cámara.
         "Lo hice todo. Y seguía llorando a los tres minutos
          de cerrar la puerta."

[10-19 s] Sigue a cámara, más despacio.
         "Porque ninguna de esas cosas le enseñaba lo único
          que necesitaba aprender: que cuando te vas, vuelves.
          Y eso no se enseña con un juguete.
          Se enseña con repeticiones cortas, en un orden concreto."

[19-27 s] Plano del plan de 8 semanas abierto, pasando páginas.
         "Ese orden es esto. Ocho semanas, cada día te dice
          qué toca. Tú solo lo haces."

[27-31 s] "Primera parte gratis en el enlace."
```

---

## HC3 — "La nota en el buzón" *(el dolor más agudo — pruébalo, puede ser el ganador)*

```
[0-4 s]  Primer plano de un papel doblado en un buzón. Se saca.
         Tu voz: "Me dejaron esta nota en el buzón.
          Y no era la primera."

[4-10 s] A cámara.
         "'Su perro lleva toda la mañana ladrando.'
          Y lo peor es que yo no podía ni discutirlo."

[10-18 s] Plano del perro tranquilo, tumbado, mirando a cámara.
         "No ladraba por vicio. Ladraba porque estaba solo
          y no había aprendido a estarlo. Son cosas distintas,
          y se tratan distinto."

[18-27 s] Plano cenital de las cuatro piezas.
         "Veintiún días. Diez minutos al día.
          Sin collares de castigo y sin dejarlo llorar."

[27-31 s] "Te dejo la primera parte gratis abajo."
```

> **Este ángulo suele ganar** cuando el problema tiene una consecuencia social. La ansiedad por
> separación la tiene: no es solo que el perro sufra, es que hay un vecino enfadado. Ese miedo
> mueve a la acción más rápido que la culpa.

---

## En la recámara (para cuando muera alguno)

- **HC4 — "POV", sin voz.** Rótulo *"POV: día 21 del protocolo"*. Solo la pantalla de la cámara
  del perro: se cierra la puerta, y el perro se queda tumbado. Se graba en 10 minutos, no hay que
  hablar, y suele dar el mejor hook rate de todos.
- **HC5 — "Los 90 segundos".** Un solo consejo, entero y gratis: los tres gestos que haces al
  salir y que empeoran la despedida. Regalar valor real capta a un público más frío.

## 3.2 Textos del anuncio

**Texto principal:**
```
Puse una cámara para ver qué hacía mi perro cuando me iba.
Ojalá no la hubiera puesto.

Cuarenta minutos jadeando y dando vueltas por el pasillo.
No estaba enfadado conmigo: estaba en pánico.

Y no se arreglaba cansándolo antes de salir. Eso yo lo hacía
todos los días.

Hogar en Calma es el protocolo que sí funcionó: 21 días,
10 minutos al día. Con el diario para ir apuntando lo que
pasa cada día y el audio para dejarle puesto al salir.

Sin collares de castigo. Sin dejarlo llorar hasta que se calle.

🛡 30 días de garantía.

👉 Descarga gratis la primera parte
```

**Titular:** `El protocolo de 21 días`
**Descripción:** `Primera parte gratis`
**Llamada a la acción:** `Descargar`

## 3.3 El lead magnet

> **"Los 90 segundos antes de salir de casa — los 3 gestos que empeoran la ansiedad de tu perro,
> y qué hacer en su lugar"**

Cumple las tres condiciones de un buen lead magnet: **se aplica hoy mismo** (esta tarde, al
salir), **no habla del producto** y **demuestra que sabes de lo que hablas** antes de pedir
dinero. Y deja la puerta abierta al libro de forma natural: si tres gestos cambian algo, el
protocolo completo cambia más.

---

# 4. EDAD DORADA — el ángulo y su guion

## 4.1 Antes de escribir: la línea que no se cruza

Aquí no hay riesgo de política de atributos personales, pero **sí de promesas sanitarias**, y en
salud animal es un asunto legal y ético a la vez.

| ❌ Nunca | ✅ En su lugar |
|---|---|
| "Alivia la artrosis de tu perro" | "Cómo adaptar la casa para que le cueste menos moverse" |
| "Previene la demencia canina" | "Qué significan las vueltas de madrugada, y cómo acompañarlas" |
| "Cura la incontinencia" | "Rutinas para las noches, sin regañinas y sin culpa" |
| "Alarga la vida de tu perro" | "Que los años que le queden sean buenos años" |

**Y la regla que no es negociable:** el libro **no sustituye al veterinario**, y hay que decirlo
en la landing, en la página de gracias y en la primera página del eBook. No es letra pequeña
defensiva: es lo que hace que el producto sea honesto. Un dueño angustiado con un perro de 14
años es alguien vulnerable, y lo que necesita oír es "esto te ayuda a acompañarlo y a saber qué
preguntarle a tu veterinario", no "esto lo arregla".

Frase para poner tal cual:

> *Edad Dorada es una guía de acompañamiento y cuidado en casa. No es un tratamiento
> veterinario y no sustituye a tu veterinario. Si notas un cambio brusco, la consulta va primero.*

## 4.2 El avatar

**Quién:** dueño de perro o gato de 9 años o más. Ha estado con el animal media vida.

**El dolor real:**
- **La duda sobre el dolor.** "¿Le duele algo y yo no me estoy dando cuenta?" Los animales lo
  esconden, y el dueño lo sabe. Esa duda no se va nunca.
- **"Es que ya es mayor."** La frase con la que se explica todo, y por la que se dejan pasar
  cosas que sí se podían abordar.
- **Las noches.** Se levanta a las cuatro, da vueltas, se queda mirando una pared.
- **La cuenta atrás.** Sabe que queda menos que lo que ha pasado. No lo dice en voz alta.
- **La culpa anticipada.** "¿Estoy haciendo todo lo que puedo?"

**Su objeción número uno:** *"esto es cosa de la edad, no hay nada que hacer"*. Y el ángulo
principal la ataca de frente.

---

## ED1 — "Es que ya es mayor"

```
[0-4 s]  A cámara, tranquilo. El perro tumbado al lado, en plano.
         "Llevaba un año diciéndome lo mismo:
          'es que ya es mayor'."

[4-11 s] Plano del perro subiendo con dificultad a un sofá — o dudando antes de subir.
         Sin dramatismo, plano corto.
         "Que dormía más porque era mayor.
          Que ya no me saludaba en la puerta porque era mayor.
          Que se levantaba de noche porque era mayor."

[11-20 s] Vuelta a cámara.
         "Y era verdad, tenía trece años.
          Pero 'ser mayor' no explicaba todo.
          Había cosas que sí se podían hacer, y yo no las sabía."

[20-28 s] Plano cenital de las piezas del producto.
         "Eso es Edad Dorada: qué mirar, qué preguntarle
          al veterinario, y cómo montarle la casa y el día
          para que le cueste menos."

[28-32 s] A cámara, más bajo.
         "No sé cuánto nos queda. Sí sé cómo quiero que sea.
          Te dejo la guía gratis en el enlace."
```

> **Rodaje:** ni un plano lastimero. Nada de música triste, ni cámara lenta, ni el perro mirando
> a la nada. Tono **sereno y cálido**, no fúnebre. Si el vídeo da pena, el que lo ve pasa de largo
> para no sentirse mal; si da compañía, se queda. Y en el último plano que el perro esté
> **tranquilo y bien**, nunca sufriendo.

## Textos — Edad Dorada

**Texto principal:**
```
Llevaba un año diciéndome lo mismo: "es que ya es mayor".

Que dormía más porque era mayor. Que ya no me saludaba en la
puerta porque era mayor. Que se levantaba a las cuatro de la
mañana y daba vueltas porque era mayor.

Y era verdad, tenía trece años. Pero "ser mayor" no explicaba
todo. Había cosas que sí se podían hacer, y yo no las sabía.

Edad Dorada es eso: qué mirar, qué preguntarle a tu veterinario,
y cómo adaptar la casa y el día para que le cueste menos.

No sé cuánto nos queda. Sí sé cómo quiero que sea.

Guía de acompañamiento en casa. No sustituye a tu veterinario.

👉 Descarga gratis la guía de señales
```

**Titular:** `Que sean buenos años`
**Descripción:** `Guía gratuita`

**Lead magnet:**

> **"Las 12 señales que confundimos con 'es que ya es mayor' — y cuáles conviene consultar"**

Es el mejor activo de captación de los dos libros. Toca la duda exacta que no se le va de la
cabeza, es útil de inmediato, y **posiciona bien**: no promete curar nada, ayuda a decidir cuándo
ir al veterinario. Eso construye confianza, que es justo lo que hace falta para que alguien te
pague 49,90 €.

**Landing: lista de espera.** Una pantalla, sin secuencia de emails todavía:

```
Las 12 señales que confundimos con "es que ya es mayor"

Y cuáles conviene consultar con tu veterinario.

[ tu email ]  [ Enviádmela ]

Te llega ahora. Y te avisamos cuando salga Edad Dorada,
con precio de lanzamiento para esta lista.
```

---

# 5. Qué grabas este fin de semana

Todo sale de una tarde, con tu perro y tu casa.

| Orden | Anuncio | Qué necesitas | Dificultad |
|---|---|---|---|
| 1º | **HC1 "La cámara"** | Tu puerta con marcas, o el sofá. Plano de la cámara del perro si la tienes | 🟡 Media |
| 2º | **HC2 "Lo he probado todo"** | La tele, la correa, un Kong, un juguete. Cuatro planos de objetos | 🟢 Fácil |
| 3º | **HC3 "La nota"** | Un papel doblado y tu buzón. Nada más | 🟢 Fácil |
| 4º | **ED1 "Es que ya es mayor"** | **Otro día, otra ropa, luz distinta.** Tu perro tumbado tranquilo | 🟡 Media |

**Reglas de la sesión:**
- **Graba a tu propio perro.** Es tu ventaja frente a cualquiera que venda un PDF genérico, y no
  cuesta nada. Nada de vídeos de banco de imágenes: se notan y matan la credibilidad.
- El gancho (3 primeros segundos) **grábalo 5 veces**, cambiando la entonación.
- Planos de recurso de sobra: la puerta, el buzón, la correa, el perro durmiendo, las cuatro
  piezas del producto en la mesa. Con eso montas creativos nuevos sin volver a grabar.
- **Cámbiate de ropa y de día entre los dos libros.** Son dos audiencias distintas y no deben
  parecer la misma campaña.
- **Nada de imágenes de animales sufriendo.** Ni en Hogar en Calma ni en Edad Dorada. Meta lo
  penaliza y el público lo rechaza.

---

# 6. Lo que sigue pendiente

| Pregunta | Por qué importa |
|---|---|
| ¿El Diario de Bienestar es un registro de conducta del animal o reflexiones para el dueño? | Cambia el bloque 4 de los guiones y el argumento de venta más fuerte |
| ¿Edad Dorada lleva también diario y plan, o solo el eBook? | Sin saberlo no puedo cerrar su pila de valor |
| ¿*Sigue Contigo* está en venta? | Es el tercer peldaño de la escalera y ya está construido. Puede ser producto o upsell, a coste cero |

---

# 7. PERROS Y GATOS: qué cambia

Los dos libros cubren perro y gato. Eso te dobla el mercado, pero **no se resuelve escribiendo
"perros y gatos" en el anuncio.**

## 7.1 La regla que hay detrás

> **Un dueño de gato no se siente aludido por un anuncio con un perro. Y al revés.**

No es una cuestión de gustos: es identificación. El que ve un vídeo de un perro arañando la
puerta piensa "esto no va conmigo" y sigue bajando, aunque tenga un gato con exactamente el mismo
problema. Un anuncio que dice "para perros y gatos" no le habla a nadie en concreto, y por eso no
para a nadie.

**Consecuencia práctica: cada especie necesita su propio creativo y su propia landing.** No dos
productos: dos puertas de entrada al mismo producto.

## 7.2 Cómo se prueba sin pasar de 15 €/día

Con 15 €/día siguen siendo **3 anuncios activos**, siempre. No cuatro. Así que los gatos entran
por rotación, no por ampliación:

| Semanas | Los 3 anuncios activos |
|---|---|
| **1 – 3** | Las tres versiones de la especie que puedas grabar hoy |
| **4** | En la revisión del lunes, el **más débil de los tres** se sustituye por la versión de la otra especie del ángulo ganador |
| **5+** | Si el de la otra especie sale más barato, es la señal para hacerle sus otros dos ángulos |

Es un test limpio: el mismo ángulo, el mismo mensaje, la misma landing en estructura. Lo único
que cambia es la especie. Si el coste por lead cambia mucho, sabes exactamente por qué.

## 7.3 ¿Con cuál empiezas?

**Con el animal con el que vives.** Esta regla manda sobre cualquier cálculo de tamaño de mercado:
grabar a tu propio animal en tu propia casa es tu única ventaja frente a cualquiera que venda un
PDF genérico, y no se puede improvisar. Un vídeo con un perro de banco de imágenes se nota en dos
segundos y hunde la credibilidad de todo lo demás.

Si tienes los dos, empieza por el **perro**: la audiencia de dueños de perro en Meta es más ancha
y está más acostumbrada a comprar contenido de conducta. Los gatos suelen tener **CPM más barato**
por menos competencia, así que a menudo compensan; por eso conviene probarlos en la semana 4.

## 7.4 El mismo problema, síntomas distintos

Esto es lo que hace que los guiones no se puedan traducir cambiando "perro" por "gato": **el
problema es el mismo, pero lo que ve el dueño no se parece en nada.**

### Ansiedad — Hogar en Calma

| Perro | Gato |
|---|---|
| Llora, aúlla, ladra al quedarse solo | **Se hace pis fuera del arenero** |
| Araña la puerta, destroza el marco | **Se lame hasta hacerse calvas** (sobreacicalado) |
| Destroza sofá, cojines, zapatos | Maullidos largos, sobre todo de noche |
| Jadea y da vueltas | Vomita, o come demasiado rápido, o deja de comer |
| Se hace pis dentro pese a estar educado | Se esconde durante horas y no sale ni a comer |

### La mascota mayor — Edad Dorada

| Perro | Gato |
|---|---|
| Le cuesta subir al sofá o al coche | **Deja de saltar a su sitio de siempre** |
| Duerme más, ya no saluda en la puerta | Duerme en sitios nuevos y escondidos |
| Se desorienta de noche, da vueltas | **Deja de acicalarse**: el pelo se ve mate y descuidado |
| Se hace pis dentro | Cambios en el arenero, dentro o fuera |
| — | **Bebe mucha más agua de lo normal** |

> ⚠️ Esa última fila es la más importante del documento en términos de responsabilidad. En un
> gato mayor, beber mucha más agua es una señal que **conviene consultar con el veterinario, y
> pronto**. Tu libro puede y debe decir "esto se consulta". Lo que no puede hacer, ni en el libro
> ni en el anuncio, es dar a entender que lo aborda o lo mejora. Sé especialmente cuidadoso aquí:
> es justo la señal que más se confunde con "es que ya es mayor", y por eso es la que más vidas
> alarga cuando alguien la consulta a tiempo. Trátala como lo que es.

## 7.5 El ángulo de gato que no tiene equivalente en perro

Y es el mejor de todos, porque **rompe una creencia**:

> *"Los gatos son independientes, a ellos no les afecta que te vayas."*

Eso lo cree casi todo el mundo, incluidos muchos dueños de gato. Por eso la ansiedad por
separación en gatos pasa desapercibida durante años: el dueño no interpreta el pis fuera del
arenero como ansiedad, lo interpreta como que su gato "le está castigando". Un anuncio que
desmonta eso para en seco a quien lo ve, porque le está explicando algo que llevaba años
entendiendo mal.

### HC1-G — "El mito de la independencia"

```
[0-4 s]  A cámara. Directo, sin rodeos.
         "Si tu gato se hace pis fuera del arenero cuando te vas,
          no te está castigando."

[4-11 s] Plano del gato mirando por la ventana, o de un arenero.
         "Nos han dicho tantas veces que los gatos son independientes
          que cuando uno lo pasa mal, no lo vemos.
          Lo llamamos 'rencor'."

[11-20 s] Vuelta a cámara.
         "El pis fuera del arenero, lamerse hasta hacerse calvas,
          los maullidos de madrugada. Eso no es carácter.
          Y se trabaja distinto que en un perro,
          porque en un gato no se corrige: se cambia el entorno."

[20-28 s] Plano cenital de las cuatro piezas.
         "Veintiún días. El protocolo está pensado
          también para gatos, que es lo que casi nadie hace."

[28-32 s] "Te dejo la primera parte gratis en el enlace."
```

> **El bloque de 11-20 s es el que vende.** Ahí estás diciendo lo único que un dueño de gato no
> ha oído nunca: que existe un método pensado para su especie y no un método de perros con el
> nombre cambiado. Es tu diferenciador real, y hay muy poca competencia diciéndolo.

### ED1-G — "Los gatos lo esconden mejor"

```
[0-4 s]  Plano del gato tumbado, tranquilo. Tu voz encima.
         "Mi gata dejó de subirse al armario.
          Tardé cuatro meses en darme cuenta de lo que significaba."

[4-12 s] A cámara.
         "Los gatos esconden el dolor mejor que cualquier otro animal
          que viva en una casa. Es instinto: en la naturaleza,
          mostrar debilidad te mata.
          Así que no se quejan. Dejan de hacer cosas."

[12-21 s] Planos cortos: un sitio alto vacío, un bebedero, el pelo del gato.
         "Deja de saltar. Deja de acicalarse.
          Bebe más agua. Y cada una de esas cosas, por separado,
          parece que no es nada."

[21-29 s] Plano de las piezas del producto.
         "Edad Dorada es la lista de qué mirar,
          y cuáles de esas señales conviene consultar
          con tu veterinario sin esperar."

[29-33 s] "Te dejo la guía de señales gratis en el enlace."
```

> Fíjate en que el guion **no promete arreglar nada**: promete ayudarte a *ver*. Es honesto, es
> lo que de verdad hace un libro, y paradójicamente vende mejor, porque un dueño angustiado
> distingue perfectamente quién le está vendiendo humo y quién le está ayudando a decidir.

## 7.6 Las landings

He añadido `landing/hogar-en-calma-gatos.html`, con el píxel ya montado igual que las demás y
apuntando a la misma página de gracias.

**La regla es que el anuncio y la landing tienen que coincidir en especie.** Si un anuncio de
gatos cae en una landing con un perro de foto, el visitante entiende que se ha equivocado de
sitio y se va: has pagado el clic para nada. Es uno de los errores que más silenciosamente
arruinan una campaña, porque las métricas del anuncio salen bien y la conversión sale mal.

| Anuncio | Landing |
|---|---|
| HC1, HC2, HC3 (perro) | `hogar-en-calma.html` |
| HC1-G (gato) | `hogar-en-calma-gatos.html` |
| ED1 (perro) | `edad-dorada-lista-espera.html` |

Para Edad Dorada, cuando llegue el momento del gato, duplica la de lista de espera igual que hice
con la de Hogar en Calma: cambia el texto de las tres viñetas por las señales felinas de la tabla
del 7.4 y listo.
