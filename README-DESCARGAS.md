# 📱 Hogar en Calma - Sistema de Descargas con QR + Audio 432Hz

Sistema completo para vender tu ebook con acceso a recursos descargables mediante código QR.

---

## 🚀 INICIO RÁPIDO (5 minutos)

### 1️⃣ Preparar archivos
```bash
# Crea la estructura de carpetas
mkdir -p archivos public qr-codes

# Coloca tus archivos aquí:
# archivos/hogar-en-calma-ebook.pdf
# archivos/diario-bienestar.pdf
# archivos/plan-8-semanas.pdf
# archivos/432hz-angelical-dreams.mp3
```

### 2️⃣ Instalar dependencias
```bash
npm install
# O si prefieres:
# yarn install
```

### 3️⃣ Probar localmente
```bash
npm start
# Abre: http://localhost:3000
```

### 4️⃣ Generar código QR
```bash
npm run generate-qr
# Tu QR estará en: ./qr-codes/hogar-en-calma-qr.png
```

---

## 📦 ¿Qué incluye este sistema?

✅ **Página de descargas** - HTML responsive  
✅ **Reproductor de audio** - Incrustado desde SoundCloud  
✅ **Generador de QR** - Automático  
✅ **Servidor Express** - Para probar localmente  
✅ **Ready para Vercel** - Deploy gratuito en 1 minuto  
✅ **API de descargas** - Con logging de uso  

---

## 📂 Estructura de archivos

```
├── descargas-hogar-calma.html    ← Página principal
├── server.js                      ← Servidor Express
├── generar-qr.js                  ← Script para QR
├── package.json                   ← Dependencias
├── vercel.json                    ← Config Vercel
├── .env.example                   ← Variables de entorno
│
├── archivos/                      ← Tus descargas
│   ├── hogar-en-calma-ebook.pdf
│   ├── diario-bienestar.pdf
│   ├── plan-8-semanas.pdf
│   └── 432hz-angelical-dreams.mp3
│
└── public/                        ← Para producción
    ├── descargas-hogar-calma.html
    └── archivos/ (copiar desde ./archivos/)
```

---

## 🌐 Desplegar en Internet (Elige una opción)

### ⚡ Opción 1: Vercel (Más fácil)
```bash
# 1. Instala Vercel CLI
npm install -g vercel

# 2. Deploy
vercel

# Tu sitio estará en: https://tu-proyecto.vercel.app
```

### 🐙 Opción 2: GitHub Pages
```bash
# 1. Sube a GitHub
git add .
git commit -m "Add Hogar en Calma descargas"
git push origin main

# 2. En GitHub: Settings → Pages
# 3. Tu sitio en: https://tu-usuario.github.io/tremdora-proyect/
```

### 🏠 Opción 3: Tu servidor personal
```bash
# 1. Copia los archivos a tu servidor
scp -r public/* usuario@tu-servidor.com:/var/www/

# 2. Instala dependencias en el servidor
ssh usuario@tu-servidor.com "cd /var/www && npm install"

# 3. Inicia el servidor
npm start
```

---

## 🎯 Flujo de usuario

```
1. Cliente ve código QR (impreso, redes sociales, etc.)
2. Escanea con su celular
3. Se abre tu página de descargas
4. Ve el reproductor de audio (432Hz en vivo)
5. Descarga: Ebook + Diario + Plan + Audio MP3
6. ✅ Todo en un mismo lugar
```

---

## 📱 Conectar con SoundCloud

1. Sube tu audio a [SoundCloud.com](https://soundcloud.com)
2. Copia la URL: `https://soundcloud.com/tu-usuario/432hz-...`
3. Actualiza la URL en `descargas-hogar-calma.html` (línea 127)

```html
<!-- Busca esta línea y cambia la URL -->
<source src="https://soundcloud.com/tu-usuario/tu-track" type="audio/mpeg">
```

---

## 🎨 Personalizar la página

Edita `descargas-hogar-calma.html`:

```html
<!-- Cambiar título -->
<h1>✨ Tu Título Aquí</h1>

<!-- Cambiar colores -->
.container { background: linear-gradient(135deg, #TU_COLOR1, #TU_COLOR2); }

<!-- Cambiar descripciones -->
<p>Tu descripción aquí</p>
```

---

## 🔐 Variables de entorno

Copia `.env.example` a `.env` y actualiza:

```bash
cp .env.example .env
```

Edita `.env`:
```
PORT=3000
SOUNDCLOUD_URL=https://soundcloud.com/tu-usuario/tu-track
DOMAIN=https://tu-dominio.com
```

---

## 📊 Rastrear descargas

El servidor registra automáticamente:
- Nombre del archivo descargado
- IP del usuario
- Navegador utilizado
- Hora exacta

Verás logs como:
```
📥 DESCARGA REGISTRADA
├─ Archivo: hogar-en-calma-ebook.pdf
├─ IP: 192.168.1.1
├─ User-Agent: Mozilla/5.0...
└─ Hora: 02/09/2026, 14:30:45
```

---

## 🐛 Solucionar problemas

### No funciona `npm install`
```bash
# Actualiza npm
npm install -g npm@latest

# Intenta de nuevo
npm install
```

### Error "Cannot find module"
```bash
# Elimina node_modules
rm -rf node_modules package-lock.json

# Reinstala
npm install
```

### El QR no se genera
```bash
# Verifica que tienes qrcode instalado
npm install qrcode

# Intenta generar de nuevo
npm run generate-qr
```

### La página no carga en Vercel
1. Verifica que `vercel.json` está bien
2. Ejecuta: `vercel logs`
3. Asegúrate de que `public/` existe

---

## 📚 Documentación completa

Para más detalles, revisa:
- [`GUIA-QR-EBOOK-432Hz.md`](./GUIA-QR-EBOOK-432Hz.md) - Guía detallada
- [`estructura-proyecto.md`](./estructura-proyecto.md) - Explicación de carpetas

---

## 💡 Tips

1. **Antes de vender**: Prueba el QR escaneándolo con tu celular
2. **Audio en SoundCloud**: Ponlo en privado o "secret link only"
3. **Certificados HTTPS**: Vercel los incluye automáticamente
4. **Dominios personalizados**: Puedes usar uno tuyo en Vercel
5. **Backups**: Haz copias de tus archivos PDF y MP3

---

## 🎉 Checklist final

- [ ] Archivos PDF y MP3 preparados
- [ ] Audio subido a SoundCloud
- [ ] `npm install` ejecutado sin errores
- [ ] `npm start` funciona en localhost
- [ ] QR generado correctamente
- [ ] Página se ve bien en móvil
- [ ] Desplegado en Vercel/GitHub Pages
- [ ] URL del QR funciona desde celular
- [ ] Pago integrado (Gumroad/Stripe)
- [ ] ¡Listo para vender! 🚀

---

## 📞 Soporte

Si tienes problemas:

1. Revisa los logs: `npm start` muestra errores claros
2. Verifica la estructura de carpetas
3. Asegúrate de que tus archivos están en `/archivos/`
4. Prueba en navegadores diferentes

---

## 📄 Licencia

Este proyecto es tuyo para usar como quieras.

---

**¿Lista la primera venta? 🎊**

Próximos pasos:
1. Comparte el QR en redes sociales
2. Imprime el QR en tus materiales
3. Incluye el QR en la contraportada del ebook
4. ¡Vende con confianza!

---

Hecho con ❤️ para tu proyecto Hogar en Calma
