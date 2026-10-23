#!/usr/bin/env python3
"""Inyecta el CSS en el HTML y renderiza el PDF con Chromium."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium"
OUT = HERE / "pdf"
OUT.mkdir(exist_ok=True)


def build(name: str, pdf_name: str) -> pathlib.Path:
    css = (HERE / "book.css").read_text(encoding="utf-8")
    html = (HERE / f"{name}.html").read_text(encoding="utf-8")
    if "/*CSS*/" not in html:
        sys.exit(f"{name}.html: falta el marcador /*CSS*/")
    html = html.replace("/*CSS*/", css, 1)

    built = HERE / f"{name}.built.html"
    built.write_text(html, encoding="utf-8")

    pdf = OUT / pdf_name
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--virtual-time-budget=6000",
            f"--print-to-pdf={pdf}",
            str(built),
        ],
        check=True,
        capture_output=True,
    )
    return pdf


if __name__ == "__main__":
    jobs = [
        ("hogar", "Hogar-en-Calma-Tremdora.pdf"),
        ("edad", "Edad-Dorada-Tremdora.pdf"),
        ("muestra-hogar", "Hogar-en-Calma-MUESTRA-GRATIS.pdf"),
        ("muestra-edad", "Edad-Dorada-MUESTRA-GRATIS.pdf"),
        ("c2-diario-calma", "Hogar-en-Calma-2-Diario-de-la-Calma.pdf"),
        ("c3-plan-calma", "Hogar-en-Calma-3-Plan-8-Semanas.pdf"),
        ("c2-diario-dias", "Edad-Dorada-2-Diario-de-los-Dias-Buenos.pdf"),
        ("c3-plan-dorada", "Edad-Dorada-3-Plan-8-Semanas.pdf"),
        ("x1-rutinas-calma", "Hogar-en-Calma-4-Rutinas-de-Calma.pdf"),
        ("x2-nutricion-dorada", "Edad-Dorada-4-Nutricion-Dorada.pdf"),
        ("x3-20-momentos", "Edad-Dorada-5-20-Momentos.pdf"),
        ("x4-cartas-conexion", "Edad-Dorada-6-Cartas-de-Conexion.pdf"),
        ("x5-ritual-10-minutos", "Edad-Dorada-7-Ritual-de-10-Minutos.pdf"),
    ]
    if len(sys.argv) > 1:
        jobs = [j for j in jobs if j[0] in sys.argv[1:]]
    for name, pdf_name in jobs:
        p = build(name, pdf_name)
        info = subprocess.run(
            ["pdfinfo", str(p)], capture_output=True, text=True
        ).stdout
        pages = next(
            (l.split()[1] for l in info.splitlines() if l.startswith("Pages")), "?"
        )
        kb = p.stat().st_size // 1024
        print(f"{pdf_name}: {pages} páginas · {kb} KB")
