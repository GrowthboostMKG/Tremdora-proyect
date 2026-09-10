# Landings con el píxel ya montado

Cuatro páginas listas para publicar. **Solo hay que sustituir tres cosas** — están todas
marcadas en MAYÚSCULAS dentro de los archivos.

## Los archivos

```
Anuncios HC1 y HC2  ──►  hogar-en-calma.html  ──►  gracias-hogar-en-calma.html   [Lead ✓]
Anuncio  ED1        ──►  edad-dorada-lista-espera.html ──► gracias-edad-dorada.html [Lead ✓]
```

El evento `Lead` está **solo en las dos páginas de gracias**. Ahí es donde tiene que estar: es la
prueba de que alguien dejó su email, no de que entró a mirar.

## Lo que tienes que sustituir

**① `PEGA_AQUI_TU_ID_DE_PIXEL`** — tu número de 15-16 cifras.
Lo saces de `business.facebook.com` → Administrador de eventos.
Aparece **dos veces en cada archivo** (en `fbq('init'...)` y en la etiqueta `<noscript>`).
Cambia las dos, en los cuatro archivos.

Para hacerlo de golpe desde la terminal, dentro de esta carpeta:

```bash
sed -i 's/PEGA_AQUI_TU_ID_DE_PIXEL/123456789012345/g' *.html
```

**② `PEGA_AQUI_LA_URL_DE_TU_FORMULARIO`** — la dirección que te da tu servicio de email.
Está en las dos landings (no en las de gracias).

| Servicio | Plan gratis | Dónde está la URL |
|---|---|---|
| **Brevo** | 300 envíos/día | Contactos → Formularios → *Compartir* → HTML |
| **MailerLite** | 1.000 suscriptores | Formularios → Embedded form → *action* del HTML |
| **Mailchimp** | 500 contactos | Audience → Signup forms → Embedded form |

En los tres, busca en el HTML que te dan la parte `action="…"` y copia esa dirección.

**③ La redirección a la página de gracias.**
En el panel de tu servicio de email, en los ajustes del formulario, busca
**"Página de agradecimiento" / "Redirect URL" / "Custom thank you page"** y pon ahí la URL de
`gracias-hogar-en-calma.html`. Sin esto el visitante no llega a la página de gracias y **el
evento Lead nunca se dispara.**

## Publicarlas

Desde la carpeta `landing/`:

```bash
npm install -g vercel
vercel
```

Te devuelve una URL tipo `https://tremdora.vercel.app/hogar-en-calma.html`. Esa es la que pones
en el campo **URL del sitio web** del anuncio.

## Comprobación final (obligatoria)

1. Extensión **Meta Pixel Helper** en Chrome.
2. Abre la landing → el icono se pone azul, *1 pixel found*, evento **PageView**.
3. Envía el formulario con tu propio email.
4. En la página de gracias el Pixel Helper debe mostrar **PageView** y **Lead**.

Si el paso 4 no muestra `Lead`, no publiques la campaña: casi siempre es que falta la
redirección del punto ③.
