# Fondo crema a sangre en todas las páginas + metadatos.
import sys, io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
src, title = sys.argv[1], sys.argv[2]
r = PdfReader(src); w = PdfWriter()
for page in r.pages:
    W, H = float(page.mediabox.width), float(page.mediabox.height)
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(W, H))
    c.setFillColorRGB(0xf7/255, 0xf1/255, 0xe8/255); c.rect(0, 0, W, H, stroke=0, fill=1); c.save()
    page.merge_page(PdfReader(buf).pages[0], over=False); w.add_page(page)
w.add_metadata({'/Title': title, '/Author': 'Tremdora', '/Subject': 'Colección Sigue contigo'})
with open(src, 'wb') as f: w.write(f)
