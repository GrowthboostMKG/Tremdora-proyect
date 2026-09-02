# ⚡ Comandos Rápidos - Hogar en Calma

## 📋 Resumen de comandos esenciales

### 🚀 Inicio
```bash
# Instalar todo
npm install

# Probar localmente
npm start

# Generar QR
npm run generate-qr
```

---

## 📱 URLs Clave

```
Local:          http://localhost:3000
Vercel:         https://tu-proyecto.vercel.app
GitHub Pages:   https://tu-usuario.github.io/tremdora-proyect/
Tu dominio:     https://tu-dominio.com/descargas-hogar-calma.html
```

---

## 📁 Archivos que DEBES tener

```
✅ archivos/hogar-en-calma-ebook.pdf
✅ archivos/diario-bienestar.pdf
✅ archivos/plan-8-semanas.pdf
✅ archivos/432hz-angelical-dreams.mp3
```

Sin estos, no podrá descargar nada.

---

## 🎵 Audio en SoundCloud

```
1. Ve a: https://soundcloud.com
2. Upload → Tu archivo WAV
3. Copia la URL (ej: https://soundcloud.com/tu-user/432hz)
4. Edita: descargas-hogar-calma.html (línea 127)
5. Pega la URL en: <source src="TU_URL_AQUI">
```

---

## 🎫 Generar QR

### Opción A: Con script (recomendado)
```bash
npm run generate-qr
# Output: ./qr-codes/hogar-en-calma-qr.png
```

### Opción B: Online (sin instalar)
https://www.qr-code-generator.com/

### Opción C: URL dinámico
https://api.qrserver.com/v1/create-qr-code/?size=500x500&data=TU_URL

---

## 🌐 Desplegar en Vercel

```bash
# 1. Instalar CLI
npm install -g vercel

# 2. Deploy
vercel

# 3. Tu sitio estará en: https://tu-proyecto.vercel.app
```

---

## 🐙 Desplegar en GitHub Pages

```bash
# 1. Sube a GitHub
git add .
git commit -m "Hogar en Calma descargas"
git push origin main

# 2. En GitHub: Settings → Pages → Deploy from branch: main
# 3. Tu sitio: https://tu-usuario.github.io/tremdora-proyect/
```

---

## 💾 Variables de entorno

```bash
# Copiar template
cp .env.example .env

# Editar con tus datos
nano .env  # O tu editor preferido
```

Mínimo necesario:
```
PORT=3000
SOUNDCLOUD_URL=https://soundcloud.com/tu-usuario/432hz
```

---

## 🔍 Testing

```bash
# Probar servidor
curl http://localhost:3000

# Listar archivos disponibles
curl http://localhost:3000/api/status

# Generar QR dinámicamente
curl -X POST http://localhost:3000/api/generar-qr \
  -H "Content-Type: application/json" \
  -d '{"url":"http://localhost:3000"}'
```

---

## 🎨 Personalizar

### Cambiar colores
```html
/* En descargas-hogar-calma.html, línea ~40 */
background: linear-gradient(135deg, #TU_COLOR1, #TU_COLOR2);
```

### Cambiar título
```html
<h1>✨ Tu Título Aquí</h1>
```

### Cambiar descripciones
```html
<p>Tu descripción personalizada</p>
```

---

## 📊 Ver logs de descargas

Cuando alguien descarga algo, verás:
```
📥 DESCARGA REGISTRADA
├─ Archivo: hogar-en-calma-ebook.pdf
├─ IP: 192.168.1.100
├─ User-Agent: Mozilla/5.0...
└─ Hora: 02/09/2026, 14:30:45
```

Útil para saber qué descargan tus clientes.

---

## 🚨 Errores comunes

### "Cannot find module 'express'"
```bash
npm install
```

### "EADDRINUSE :::3000"
El puerto 3000 ya está en uso.
```bash
npm start -- --port 3001
```

### "File not found"
Verifica que tus archivos están en `/archivos/`

---

## 📦 Estructura esperada

```
tremdora-proyect/
├── descargas-hogar-calma.html
├── server.js
├── generar-qr.js
├── package.json
├── vercel.json
├── .env.example
├── .env ← Crea este desde .env.example
│
├── archivos/
│   ├── hogar-en-calma-ebook.pdf ← VITAL
│   ├── diario-bienestar.pdf     ← VITAL
│   ├── plan-8-semanas.pdf       ← VITAL
│   └── 432hz-angelical-dreams.mp3 ← VITAL
│
├── public/ ← Para Vercel
│   ├── descargas-hogar-calma.html
│   └── archivos/
│
└── qr-codes/ ← Aquí va tu QR
    └── hogar-en-calma-qr.png
```

---

## 🎯 Flujo rápido desde cero

```bash
# 1. Setup
npm install

# 2. Configura variables
cp .env.example .env
nano .env  # Edita con tus datos

# 3. Coloca tus archivos en archivos/

# 4. Prueba local
npm start
# Abre http://localhost:3000

# 5. Genera QR
npm run generate-qr

# 6. Sube a internet
vercel  # O tu opción elegida

# 7. ¡Vende!
```

---

## 💡 Pro Tips

- Usa QR dinámicos si quieres cambiar la URL después
- Mantén los archivos bajo 50MB total
- Prueba en móvil ANTES de distribuir QRs
- Haz backups de tus PDFs y MP3
- Los QRs se expiran? No, duran para siempre
- Comparte el QR en redes: Facebook, Instagram, etc.

---

## 🔗 Links útiles

- [QR Code Generator](https://www.qr-code-generator.com)
- [SoundCloud](https://soundcloud.com)
- [Vercel](https://vercel.com)
- [GitHub Pages](https://pages.github.com)
- [Gumroad (para vender)](https://gumroad.com)

---

## 🎊 Checklist de lanzamiento

```
□ npm install - ¡OK!
□ npm start - ¡OK!
□ Todos los archivos en /archivos/ - ¡OK!
□ Audio en SoundCloud - ¡OK!
□ QR generado - ¡OK!
□ Desplegado en internet - ¡OK!
□ QR funciona en celular - ¡OK!
□ ¡LANZAMIENTO! 🚀
```

---

**¿Atascado? Vuelve a esta página y busca tu problema. Está todo aquí. 💪**
