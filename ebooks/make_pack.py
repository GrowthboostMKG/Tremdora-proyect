#!/usr/bin/env python3
"""Monta el ZIP del pack «Sigue Contigo», listo para subir a Shopify.

Toma los PDF generados en `pdf/`, el material externo de `assets/` (el eBook
principal y, cuando esté, el audio de la frecuencia) y los empaqueta en un
único ZIP con una carpeta raíz, para que al descomprimir no se desparrame.

La página «Empieza por aquí» se regenera antes de empacar, así que en cuanto
dejes la frecuencia en `assets/` aparecerá listada sola: basta con volver a
ejecutar `./build.sh && python3 make_pack.py`.
"""
import hashlib, os, subprocess, sys, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
PACK = 'Sigue Contigo - Pack completo'
AUDIO_EXT = {'.mp3', '.wav', '.m4a', '.flac', '.aac', '.ogg'}

# Orden de entrega. Cada pieza se busca primero en pdf/ y luego en assets/.
ORDEN = [
    '0. Empieza por aqui.pdf',
    '1. Sigue Contigo - eBook completo.pdf',
    '2. Sigue Contigo - Diario del Oleaje.pdf',
    '3. Sigue Contigo - Plan Practico 8 Semanas.pdf',
    '4. Sigue Contigo - Ellos Tambien se Despiden.pdf',
]


def localizar(nombre):
    for carpeta in ('pdf', 'assets'):
        ruta = os.path.join(ROOT, carpeta, nombre)
        if os.path.exists(ruta):
            return ruta
    return None


def frecuencia():
    """Audio de la frecuencia, si ya está en assets/."""
    adir = os.path.join(ROOT, 'assets')
    if not os.path.isdir(adir):
        return []
    return [os.path.join(adir, n) for n in sorted(os.listdir(adir))
            if os.path.splitext(n)[1].lower() in AUDIO_EXT]


def main():
    # La portada del pack se regenera para que el listado refleje lo que hay.
    subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'pack_intro.py')],
                   check=True, capture_output=True)
    hecho = subprocess.run([os.path.join(ROOT, 'build.sh'), '0-empieza'],
                           capture_output=True, text=True)
    if hecho.returncode:
        print('No se pudo montar el pack: la página «Empieza por aquí» no cabe\n'
              'en una hoja con las piezas que hay ahora en pdf/ y assets/.\n'
              'Acorta las descripciones en src/pack_intro.py y repite.\n')
        print((hecho.stdout or '') + (hecho.stderr or ''))
        sys.exit(1)

    piezas, faltan = [], []
    for nombre in ORDEN:
        ruta = localizar(nombre)
        (piezas if ruta else faltan).append(ruta or nombre)
    piezas += frecuencia()

    if faltan:
        print('FALTAN estas piezas, el ZIP se monta sin ellas:')
        for f in faltan:
            print('   ·', f)
        print()

    os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
    destino = os.path.join(ROOT, 'dist', PACK + '.zip')
    with zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for ruta in piezas:
            z.write(ruta, '%s/%s' % (PACK, os.path.basename(ruta)))

    print('%s\n' % os.path.relpath(destino, ROOT))
    total = 0
    with zipfile.ZipFile(destino) as z:
        for info in z.infolist():
            total += info.file_size
            print('   %-52s %7.0f KB' % (info.filename.split('/', 1)[1],
                                         info.file_size / 1024))
    tam = os.path.getsize(destino)
    sha = hashlib.sha256(open(destino, 'rb').read()).hexdigest()
    print('\n   %d archivos · %.1f MB sin comprimir · %.1f MB el ZIP'
          % (len(piezas), total / 1e6, tam / 1e6))
    print('   sha256 %s' % sha)

    if not frecuencia():
        print('\n   Nota: aún no hay audio de frecuencia en assets/.'
              '\n   Déjalo ahí y vuelve a ejecutar este script: se añadirá al ZIP'
              '\n   y aparecerá listado en la página «Empieza por aquí».')


if __name__ == '__main__':
    main()
