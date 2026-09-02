# 📁 Estructura de Carpetas Recomendada

```
tremdora-proyect/
│
├── 📄 descargas-hogar-calma.html       ← Tu página de descargas
├── 📄 generar-qr.js                     ← Script para generar QR
├── 📄 GUIA-QR-EBOOK-432Hz.md          ← Guía completa (este archivo)
│
├── 📁 archivos/                         ← Archivos que se descargan
│   ├── 📄 hogar-en-calma-ebook.pdf
│   ├── 📄 diario-bienestar.pdf
│   ├── 📄 plan-8-semanas.pdf
│   └── 🎵 432hz-angelical-dreams.mp3
│
├── 📁 qr-codes/                         ← QR generados
│   └── 🎫 hogar-en-calma-qr.png
│
├── 📁 public/                           ← Para Vercel/Node.js
│   ├── 📄 descargas-hogar-calma.html
│   └── 📁 archivos/
│
├── 📁 .github/                          ← Para GitHub Pages
│   └── 📁 workflows/
│       └── deploy.yml
│
├── 📄 package.json                      ← Dependencias Node.js
├── 📄 vercel.json                       ← Config de Vercel (opcional)
└── 📄 README.md                         ← Documentación
```

---

## 🎯 PASOS PARA CREAR LA ESTRUCTURA

### 1️⃣ Crear las carpetas
```bash
mkdir -p archivos qr-codes public
```

### 2️⃣ Crear archivos de prueba (mientras preparas los reales)
```bash
# Crea PDFs dummy para testing
touch archivos/hogar-en-calma-ebook.pdf
touch archivos/diario-bienestar.pdf
touch archivos/plan-8-semanas.pdf
touch archivos/432hz-angelical-dreams.mp3
```

### 3️⃣ Copiar tu HTML a la carpeta public
```bash
cp descargas-hogar-calma.html public/
cp -r archivos/ public/
```

### 4️⃣ Crear package.json
```bash
npm init -y
npm install express cors dotenv --save
npm install qrcode --save-dev
```

### 5️⃣ Crear archivo .env (para variables sensibles)
```bash
cat > .env << EOF
SOUNDCLOUD_URL=https://soundcloud.com/tu-usuario/432hz-hogar-en-calma
DOMAIN=https://tu-dominio.com
PORT=3000
EOF
```

---

## 📋 ARCHIVOS QUE NECESITAS PREPARAR

### Documentos PDF
- [ ] hogar-en-calma-ebook.pdf (tu libro)
- [ ] diario-bienestar.pdf (30 días de reflexiones)
- [ ] plan-8-semanas.pdf (plan de transformación)

### Audio
- [ ] 432hz-angelical-dreams.mp3 (convertido desde WAV)

### Imágenes
- [ ] hogar-en-calma-qr.png (generado con generar-qr.js)
- [ ] thumbnail.jpg (preview para redes sociales)

---

## ✅ CHECKLIST DE IMPLEMENTACIÓN

- [ ] Estructura de carpetas creada
- [ ] Archivos descargables en `/archivos/`
- [ ] HTML alojado en internet
- [ ] QR generado con generar-qr.js
- [ ] URL del QR apunta a tu página
- [ ] Prueba: Escanear QR funciona
- [ ] Audio en SoundCloud disponible
- [ ] Pago integrado (Gumroad/Stripe)
- [ ] Documentación actualizada

---

## 🚀 SIGUIENTES PASOS

1. Copia esta estructura en tu proyecto
2. Prepara tus PDFs y audio
3. Sube todo a Vercel o GitHub Pages
4. Prueba el flujo completo
5. ¡Lanza tu producto!
