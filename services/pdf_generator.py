from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

import os


def generate_pdf_report(
    company_name,
    audit_content
):

    folder = "generated_reports"

    os.makedirs(folder, exist_ok=True)

    file_path = f"{folder}/{company_name}_audit.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        f"<b>{company_name} - AI Business Audit Report</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    paragraphs = audit_content.split("\n")

    for para in paragraphs:

        if para.strip():

            p = Paragraph(
                para,
                styles['BodyText']
            )

            elements.append(p)

            elements.append(
                Spacer(1, 12)
            )

    doc.build(elements)

    return file_path