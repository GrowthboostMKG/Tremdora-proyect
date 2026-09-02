# 📱 Guía Completa: QR + Ebook + Audio 432Hz + Sistema de Descargas

## 🎯 Objetivo Final
Crear un sistema donde:
- ✅ Clientes pagan por el ebook
- ✅ Reciben un código QR
- ✅ Al escanear el QR acceden a: Ebook + Diario + Plan 8 semanas + Audio 432Hz
- ✅ Pueden descargar todo facilmente

---

## 📋 PASO 1: Preparar tu Audio (432Hz)

### 1.1 Convertir el archivo a MP3 (si lo necesitas)
```bash
# Si tienes ffmpeg instalado:
ffmpeg -i "Air Bender 777 - Angelical Dreams (432Hz).wav" -q:a 5 "432hz-angelical-dreams.mp3"
```

### 1.2 Subir a SoundCloud
1. Ve a [SoundCloud.com](https://soundcloud.com)
2. Inicia sesión (crea cuenta si no tienes)
3. Click en **Upload** (arriba a la derecha)
4. Selecciona tu archivo MP3
5. **Configuración importante:**
   - Título: `432Hz Frecuencia - Hogar en Calma`
   - Descripción: `Frecuencia sanadora que acompaña el ebook Hogar en Calma`
   - Etiquetas: `432Hz, frecuencia, bienestar, meditación`
   - **Privacidad: "Private" o "Secret link only"** (para control)
6. Click **"Save"**
7. **Copia la URL que generó** (ej: `https://soundcloud.com/tu-usuario/432hz-hogar-en-calma`)

---

## 🎨 PASO 2: Crear el Código QR

### Opción A: QR Simple (Recomendado para empezar)
1. Ve a [QR Code Generator](https://www.qr-code-generator.com/qr-code-marketing/)
2. Pega tu URL de SoundCloud
3. Personaliza:
   - Tamaño: 500x500px
   - Formato: PNG
   - Color: Negro sobre blanco (o tus colores de marca)
4. Descarga el QR

### Opción B: QR Dinámico (Para control total)
1. Ve a [QR Code Dynamic](https://www.qr-code-dynamic.com/)
2. Crea una cuenta gratuita
3. Crea un QR dinámico que apunte a tu landing page
4. **Ventaja:** Puedes cambiar la URL sin regenerar el QR

### Opción C: QR con tu página de descargas (Lo más profesional)
1. Genera el QR apuntando a esta URL:
   ```
   https://tu-dominio.com/descargas-hogar-calma.html
   ```
2. El QR abrirá tu página completa de descargas

---

## 🌐 PASO 3: Crear tu Página de Descargas (Landing Page)

### 3.1 Usar la página HTML que te proporcioné
Ya tienes el archivo `descargas-hogar-calma.html` listo en tu repositorio.

### 3.2 Alojar la página (Elige una opción)

#### **Opción A: Usar Vercel (Gratis y fácil)**
```bash
# 1. Instala Vercel CLI
npm install -g vercel

# 2. En tu carpeta del proyecto
vercel

# 3. Sigue las instrucciones
# Tu página estará en: https://tu-proyecto.vercel.app/descargas-hogar-calma.html
```

#### **Opción B: Usar GitHub Pages (Gratis)**
1. Sube tu archivo `descargas-hogar-calma.html` a tu repo
2. En GitHub → Settings → Pages
3. Elige "Deploy from a branch"
4. Tu página estará en: `https://tu-usuario.github.io/tremdora-proyect/descargas-hogar-calma.html`

#### **Opción C: Tu propio servidor**
- Sube el archivo a tu hosting actual
- URL: `https://tu-dominio.com/descargas-hogar-calma.html`

---

## 📁 PASO 4: Preparar tus Archivos Descargables

Necesitas tener listos estos 4 archivos:
```
/archivos/
  ├── hogar-en-calma-ebook.pdf
  ├── diario-bienestar.pdf
  ├── plan-8-semanas.pdf
  └── 432hz-angelical-dreams.mp3
```

### 4.1 Servir los archivos desde tu servidor

#### **Opción A: Con Node.js/Express**
```javascript
// server.js
const express = require('express');
const path = require('path');
const app = express();

app.use(express.static('public'));
app.use('/archivos', express.static('archivos'));

// Rastrear descargas
app.get('/archivos/:archivo', (req, res) => {
    console.log(`Descargado: ${req.params.archivo}`);
    res.download(path.join(__dirname, 'archivos', req.params.archivo));
});

app.listen(3000, () => console.log('Servidor en puerto 3000'));
```

#### **Opción B: Con Vercel (automático)**
Solo coloca los archivos en `/public/archivos/` y Vercel los sirve automáticamente.

#### **Opción C: Con tu hosting actual**
Sube los PDFs y MP3 a una carpeta `/descargas/` en tu servidor.

---

## 🔗 PASO 5: Vincular Todo (El Flujo Completo)

### 5.1 URL Final del Código QR
```
https://tu-dominio.com/descargas-hogar-calma.html
```

### 5.2 Flujo de Usuario
1. Cliente paga por el ebook
2. Recibe el código QR impreso/digital
3. Escanea con su celular
4. Se abre la página de descargas
5. Ve el reproductor de audio (SoundCloud incrustado)
6. Descarga todos los archivos con un click

---

## 💳 PASO 6: Integración con Plataformas de Pago

### Opción A: Usar Gumroad (Recomendado)
1. Ve a [Gumroad.com](https://gumroad.com)
2. Crea un producto:
   - Nombre: "Hogar en Calma - Pack Completo"
   - Precio: El que definas
   - Descripción: Incluye la imagen del código QR
3. En la sección de archivos:
   - Sube tu ebook PDF
   - Agrega nota: "Escanea el código QR para acceder a audio + materiales"
4. Gumroad envía todo automáticamente al cliente

### Opción B: Usar tu página + Stripe
```html
<!-- Agregar botón de pago con Stripe -->
<button id="checkout-btn" class="download-btn">💳 Comprar Ahora</button>

<script src="https://js.stripe.com/v3/"></script>
<script>
const stripe = Stripe('pk_test_tu_clave');

document.getElementById('checkout-btn').addEventListener('click', async () => {
    const response = await fetch('/create-checkout-session', {
        method: 'POST',
    });
    const session = await response.json();
    await stripe.redirectToCheckout({sessionId: session.id});
});
</script>
```

### Opción C: Usar MercadoPago (América Latina)
Código similar al de Stripe, pero con la API de MercadoPago.

---

## 🎨 PASO 7: Diseño de tu Código QR Impreso

### Para incluir en:
- **Portada del Ebook** (esquina inferior)
- **Contraportada** (centrado, grande)
- **Publicidad** (Instagram, Facebook)

### Tamaño recomendado:
- Impresión: 3cm x 3cm mínimo
- Digital: 200x200px mínimo
- Asegúrate de incluir texto debajo: "📱 Escanea para descargar"

---

## 📊 PASO 8: Rastrear Descargas (Opcional)

### 8.1 Agregar Google Analytics
```html
<!-- Agregar a tu página descargas-hogar-calma.html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');

  // Rastrear descargas
  function descargarArchivo(archivo) {
    gtag('event', 'download', {
      'file_name': archivo,
      'file_type': 'pdf' // o 'mp3'
    });
    // ... código de descarga
  }
</script>
```

---

## ✅ CHECKLIST FINAL

- [ ] Audio subido a SoundCloud
- [ ] Código QR generado y descargado
- [ ] Página HTML (`descargas-hogar-calma.html`) alojada en internet
- [ ] URL del QR = URL de tu página de descargas
- [ ] Archivos PDF y MP3 subidos al servidor
- [ ] Prueba: Escanea el QR con tu celular ¿Funciona?
- [ ] Plataforma de pago configurada (Gumroad/Stripe/MercadoPago)
- [ ] Imagen del QR lista para imprimir/distribuir

---

## 🚀 PRÓXIMOS PASOS

1. **Esta semana:** Prepara tus PDFs y MP3
2. **Semana 2:** Aloja todo en internet (Vercel/GitHub Pages)
3. **Semana 3:** Configura pago y prueba el flujo completo
4. **Semana 4:** Lanza con tus primeros clientes

---

## 📞 Preguntas Frecuentes

**P: ¿Es gratis alojar la página?**
R: Sí, con Vercel o GitHub Pages es 100% gratis.

**P: ¿Puedo cambiar el QR después de imprimirlo?**
R: Si usas QR dinámicos sí, con los estáticos no.

**P: ¿Qué pasa si un cliente pierde su enlace?**
R: Agregalos a una lista de emails y reenvialo.

**P: ¿Puedo vender esto en Gumroad y también en mi web?**
R: Claro, puedes vender en múltiples plataformas.

---

## 🎯 Tu URL Final será algo así:

```
Paso 1: Audio en SoundCloud
https://soundcloud.com/tu-usuario/432hz-hogar-en-calma

Paso 2: QR apunta a tu página de descargas
https://tu-dominio.com/descargas-hogar-calma.html

Paso 3: Cliente escanea QR y descarga TODO
Ebook + Diario + Plan + Audio

¡Listo! 🎉
```

---

**¿Necesitas ayuda con algún paso específico? Escríbeme cuál es tu siguente paso y te ayudo a implementarlo.**
