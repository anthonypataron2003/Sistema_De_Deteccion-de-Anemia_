from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus import Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors

import sys
from pathlib import Path
import re
from datetime import datetime

INPUT_MD = Path(__file__).resolve().parent.parent / 'USER_GUIDE.md'
OUTPUT_PDF = Path(__file__).resolve().parent.parent / 'GUIA_DE_USO.pdf'


def md_to_flowables(md_text):
    styles = getSampleStyleSheet()
    heading1 = ParagraphStyle(
        'Heading1', parent=styles['Heading1'], fontSize=18, leading=22, spaceAfter=6
    )
    heading2 = ParagraphStyle(
        'Heading2', parent=styles['Heading2'], fontSize=14, leading=18, spaceAfter=6)
    body = ParagraphStyle('Body', parent=styles['BodyText'], fontSize=11, leading=14)

    flowables = []
    lines = md_text.splitlines()
    buffer = []

    def flush_buffer():
        nonlocal buffer
        if buffer:
            text = ' '.join(line.strip() for line in buffer)
            # convert **bold** to <b>bold</b>
            text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
            # convert `code` to italic text (avoid font mapping issues)
            text = re.sub(r"`(.+?)`", r"<i>\1</i>", text)
            flowables.append(Paragraph(text, body))
            flowables.append(Spacer(1, 6))
            buffer = []

    for ln in lines:
        s = ln.strip()
        if not s:
            flush_buffer()
            continue
        # detect markdown image: ![alt](path)
        m_img = re.match(r"!\[(.*?)\]\((.*?)\)", s)
        if m_img:
            flush_buffer()
            alt_text = m_img.group(1)
            img_path = m_img.group(2)
            # resolve relative path
            img_file = Path(img_path)
            if not img_file.is_absolute():
                img_file = Path(__file__).resolve().parent.parent / img_file
            if img_file.exists():
                try:
                    print(f"DEBUG: insertando imagen -> {img_file}")
                    im = RLImage(str(img_file))
                    # scale to fit page width (use a slightly smaller max width for compact layout)
                    max_w = 120 * mm
                    im.drawHeight = im.drawHeight * (max_w / im.drawWidth)
                    im.drawWidth = max_w
                    flowables.append(im)
                    print(f"DEBUG: imagen agregada al flujo -> {img_file.name}")
                    flowables.append(Spacer(1, 4))
                    flowables.append(Paragraph(f"<i>{alt_text}</i>", body))
                    flowables.append(Spacer(1, 10))
                except Exception as e:
                    flowables.append(Paragraph(f"(No se pudo insertar imagen: {img_file.name})", body))
                    flowables.append(Spacer(1, 6))
            else:
                flowables.append(Paragraph(f"(Imagen no encontrada: {img_path})", body))
                flowables.append(Spacer(1, 6))
            continue
        if s.startswith('# '):
            flush_buffer()
            flowables.append(Paragraph(s[2:].strip(), heading1))
            flowables.append(Spacer(1, 6))
            continue
        if s.startswith('## '):
            flush_buffer()
            flowables.append(Paragraph(s[3:].strip(), heading2))
            flowables.append(Spacer(1, 6))
            continue
        # code blocks fences or triple backticks - skip and print as monospaced paragraph
        if s.startswith('```'):
            # simple: skip fence markers
            continue
        # normal paragraph line
        buffer.append(s)

    flush_buffer()
    return flowables


def generate_pdf(input_path=INPUT_MD, output_path=OUTPUT_PDF):
    if not input_path.exists():
        print(f"ERROR: No se encontró el archivo {input_path}")
        sys.exit(1)

    md_text = input_path.read_text(encoding='utf-8')
    doc = SimpleDocTemplate(str(output_path), pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    flowables = md_to_flowables(md_text)

    # Add a cover page with title, optional logo and date
    styles = getSampleStyleSheet()
    cover_style = ParagraphStyle('CoverTitle', parent=styles['Title'], fontSize=28, alignment=1, spaceAfter=12)
    subtitle_style = ParagraphStyle('CoverSubtitle', parent=styles['Normal'], fontSize=14, alignment=1, textColor=colors.grey)
    date_style = ParagraphStyle('CoverDate', parent=styles['Normal'], fontSize=10, alignment=1, textColor=colors.grey)

    cover = []
    # optional logo at img/logo.png
    logo_path = Path(__file__).resolve().parent.parent / 'img' / 'logo.png'
    if logo_path.exists():
        try:
            logo = RLImage(str(logo_path))
            logo.drawWidth = 60 * mm
            logo.drawHeight = logo.drawHeight * (logo.drawWidth / logo.drawWidth)
            cover.append(Spacer(1, 20))
            cover.append(logo)
            cover.append(Spacer(1, 12))
        except Exception:
            pass

    title_text = 'GUÍA DE USO — Anemia Detection'
    cover.append(Paragraph(title_text, cover_style))
    cover.append(Spacer(1, 6))
    cover.append(Paragraph('Manual de uso para la aplicación web de detección de anemia', subtitle_style))
    cover.append(Spacer(1, 12))
    cover.append(Paragraph(f'Fecha: {datetime.utcnow().strftime("%d/%m/%Y")}', date_style))
    cover.append(PageBreak())

    # insert cover at beginning
    flowables = cover + flowables

    doc.build(flowables)
    print(f"PDF generado en: {output_path}")


if __name__ == '__main__':
    generate_pdf()
