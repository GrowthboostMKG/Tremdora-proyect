# Pinta el fondo crema a sangre en todas las páginas del PDF (incluidos los márgenes).
import sys, io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
src = sys.argv[1]
r = PdfReader(src); w = PdfWriter()
for page in r.pages:
    W, H = float(page.mediabox.width), float(page.mediabox.height)
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(W, H))
    c.setFillColorRGB(0xf7/255, 0xf1/255, 0xe8/255); c.rect(0, 0, W, H, stroke=0, fill=1); c.save()
    bg = PdfReader(buf).pages[0]
    page.merge_page(bg, over=False)
    w.add_page(page)
w.add_metadata({'/Title': 'Sigue contigo', '/Author': 'Tremdora',
                '/Subject': 'Una guía para acompañarte en la pérdida de tu mascota',
                '/Keywords': 'duelo, mascotas, pérdida, perro, gato, niños, Tremdora'})
with open(src, 'wb') as f: w.write(f)
