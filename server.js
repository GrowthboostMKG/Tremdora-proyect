/**
 * Servidor Express para alojar tu página de descargas
 * Ejecución: npm install && node server.js
 * Luego abre: http://localhost:3000
 */

const express = require('express');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.static('public'));
app.use(express.json());

// Servir archivos descargables
app.use('/archivos', express.static(path.join(__dirname, 'archivos')));

// Ruta principal - Sirve la página de descargas
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'descargas-hogar-calma.html'));
});

// Ruta de descargas con logging
app.get('/archivos/:archivo', (req, res, next) => {
    const archivo = req.params.archivo;
    const rutaArchivo = path.join(__dirname, 'archivos', archivo);

    // Log de descargas
    console.log(`
📥 DESCARGA REGISTRADA
├─ Archivo: ${archivo}
├─ IP: ${req.ip}
├─ User-Agent: ${req.get('user-agent')}
└─ Hora: ${new Date().toLocaleString('es-ES')}
    `);

    // Verificar que el archivo existe
    if (!require('fs').existsSync(rutaArchivo)) {
        return res.status(404).json({
            error: 'Archivo no encontrado',
            archivo: archivo
        });
    }

    // Descargar
    res.download(rutaArchivo, (err) => {
        if (err) {
            console.error('Error al descargar:', err);
        }
    });
});

// API para generar QR dinámicamente
app.post('/api/generar-qr', (req, res) => {
    const QRCode = require('qrcode');
    const { url } = req.body;

    if (!url) {
        return res.status(400).json({ error: 'URL requerida' });
    }

    QRCode.toDataURL(url, {
        errorCorrectionLevel: 'H',
        type: 'image/png',
        width: 500,
        margin: 1,
        color: {
            dark: '#000000',
            light: '#FFFFFF'
        }
    }, (err, qrUrl) => {
        if (err) {
            return res.status(500).json({ error: 'Error al generar QR' });
        }
        res.json({ qr: qrUrl });
    });
});

// Rutas de prueba
app.get('/api/status', (req, res) => {
    res.json({
        status: '✅ Servidor funcionando',
        url: `http://localhost:${PORT}`,
        archivos_disponibles: [
            'hogar-en-calma-ebook.pdf',
            'diario-bienestar.pdf',
            'plan-8-semanas.pdf',
            '432hz-angelical-dreams.mp3'
        ],
        timestamp: new Date().toISOString()
    });
});

// Manejo de errores
app.use((err, req, res, next) => {
    console.error('Error:', err);
    res.status(500).json({ error: 'Error interno del servidor' });
});

// 404
app.use((req, res) => {
    res.status(404).json({
        error: 'Ruta no encontrada',
        path: req.path,
        metodos_disponibles: ['GET /', 'GET /archivos/*', 'POST /api/generar-qr']
    });
});

// Iniciar servidor
app.listen(PORT, () => {
    console.log(`
╔════════════════════════════════════════════════════════════════╗
║                   🎉 SERVIDOR INICIADO 🎉                      ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  ✅ Servidor ejecutándose en: http://localhost:${PORT}
║  📄 Página de descargas: http://localhost:${PORT}/
║  📊 Estado del servidor: http://localhost:${PORT}/api/status
║                                                                ║
║  📁 Archivos disponibles en: /archivos/
║     - hogar-en-calma-ebook.pdf
║     - diario-bienestar.pdf
║     - plan-8-semanas.pdf
║     - 432hz-angelical-dreams.mp3
║                                                                ║
║  🎵 Audio en SoundCloud:
║     ${process.env.SOUNDCLOUD_URL || 'Configura en .env'}
║                                                                ║
║  💡 Presiona Ctrl+C para detener el servidor                  ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
    `);

    // Mostrar instrucciones
    console.log('📋 PRUEBAS QUE PUEDES HACER:\n');
    console.log('1️⃣  Abre en tu navegador:');
    console.log(`   http://localhost:${PORT}\n`);

    console.log('2️⃣  Prueba descargar un archivo:');
    console.log(`   http://localhost:${PORT}/archivos/hogar-en-calma-ebook.pdf\n`);

    console.log('3️⃣  Verifica el estado del servidor:');
    console.log(`   curl http://localhost:${PORT}/api/status\n`);

    console.log('4️⃣  Genera un QR dinámicamente:');
    console.log(`   curl -X POST http://localhost:${PORT}/api/generar-qr \\`);
    console.log(`        -H "Content-Type: application/json" \\`);
    console.log(`        -d '{"url":"http://localhost:${PORT}"}\n`);
});

// Manejo de cierre elegante
process.on('SIGINT', () => {
    console.log('\n\n👋 Servidor detenido');
    process.exit(0);
});

module.exports = app;
