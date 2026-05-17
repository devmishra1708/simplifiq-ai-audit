import gspread

from google.oauth2.service_account import Credentials

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from datetime import datetime


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

# SHEETS SETUP
client = gspread.authorize(creds)

sheet = client.open(
    "AI Lead Tracker"
).sheet1


# DRIVE SETUP
drive_service = build(
    "drive",
    "v3",
    credentials=creds
)


def upload_pdf_to_drive(pdf_path):

    file_metadata = {
        "name": pdf_path,
        "parents":["1QN4l-j9r0cgGSk-kiasqWNdP9Kgcwu7B"]
    }

    media = MediaFileUpload(
        pdf_path,
        mimetype="application/pdf"
    )

    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    file_id = uploaded_file.get("id")

    # PUBLIC ACCESS
    drive_service.permissions().create(
        fileId=file_id,
        body={
            "type": "anyone",
            "role": "reader"
        }
    ).execute()

    drive_link = (
        f"https://drive.google.com/file/d/{file_id}/view"
    )

    return drive_link


def log_lead_to_sheets(
    name,
    email,
    company,
    status,
    pdf_link
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    row = [
        name,
        email,
        company,
        timestamp,
        status,
        pdf_link
    ]

    sheet.append_row(row)