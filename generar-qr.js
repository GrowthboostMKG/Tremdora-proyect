#!/usr/bin/env node

/**
 * Script para generar códigos QR para el ebook "Hogar en Calma"
 * Uso: node generar-qr.js
 */

const fs = require('fs');
const QRCode = require('qrcode');

// Configuración
const config = {
    // Actualiza esto con tu URL real
    url: 'https://tu-dominio.com/descargas-hogar-calma.html',

    // O si usas Vercel:
    // url: 'https://tu-proyecto.vercel.app/descargas-hogar-calma.html',

    // O si usas GitHub Pages:
    // url: 'https://tu-usuario.github.io/tremdora-proyect/descargas-hogar-calma.html',

    outputDir: './qr-codes',
    filename: 'hogar-en-calma-qr.png'
};

// Crear directorio si no existe
if (!fs.existsSync(config.outputDir)) {
    fs.mkdirSync(config.outputDir, { recursive: true });
}

// Opciones del QR
const qrOptions = {
    errorCorrectionLevel: 'H',  // Nivel alto de corrección de errores
    type: 'image/png',
    quality: 0.95,
    margin: 1,
    width: 500,  // Tamaño en píxeles
    color: {
        dark: '#000000',    // Color del código
        light: '#FFFFFF'    // Color de fondo
    }
};

console.log('🔄 Generando código QR...\n');
console.log(`📱 URL del QR: ${config.url}\n`);

QRCode.toFile(
    `${config.outputDir}/${config.filename}`,
    config.url,
    qrOptions,
    (err) => {
        if (err) {
            console.error('❌ Error al generar QR:', err);
            process.exit(1);
        }

        const filePath = `${config.outputDir}/${config.filename}`;
        const stats = fs.statSync(filePath);

        console.log('✅ ¡Código QR generado exitosamente!\n');
        console.log(`📁 Archivo guardado en: ${filePath}`);
        console.log(`📊 Tamaño del archivo: ${(stats.size / 1024).toFixed(2)} KB\n`);

        console.log('📋 Próximos pasos:');
        console.log('1. Descarga el archivo QR del directorio ./qr-codes/');
        console.log('2. Imprime o comparte en tus materiales de marketing');
        console.log('3. Asegúrate de que la URL sea accesible antes de distribuir\n');

        console.log('💡 Consejo: Prueba el QR escaneándolo con tu teléfono');
        console.log('   para verificar que apunta a la página correcta.\n');
    }
);

/**
 * INSTALACIÓN:
 *
 * 1. Instala la dependencia:
 *    npm install qrcode
 *
 * 2. Ejecuta este script:
 *    node generar-qr.js
 *
 * 3. Tu QR estará en: ./qr-codes/hogar-en-calma-qr.png
 */
