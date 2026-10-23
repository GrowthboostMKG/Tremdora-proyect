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
