import os
import smtplib

from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


def send_audit_email(
    recipient_email,
    company_name,
    pdf_path
):

    sender_email = os.getenv(
        "EMAIL_HOST_USER"
    )

    sender_password = os.getenv(
        "EMAIL_HOST_PASSWORD"
    )

    msg = EmailMessage()

    msg["Subject"] = (
        f"{company_name} - AI Business Audit Report"
    )

    msg["From"] = sender_email

    msg["To"] = recipient_email

    msg.set_content(f"""
Hi,

Attached is your personalized AI Business Audit Report for {company_name}.

The report contains:
- business analysis
- growth opportunities
- AI automation recommendations
- strategic insights

Thank you.

Regards,
SimplifIQ AI
""")

    with open(pdf_path, "rb") as f:

        file_data = f.read()

        file_name = os.path.basename(
            pdf_path
        )

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="pdf",
        filename=file_name
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            sender_email,
            sender_password
        )

        smtp.send_message(msg)