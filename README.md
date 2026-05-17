# SimplifIQ AI Business Audit Automation

An AI-powered lead intake and business audit automation platform built using React and Django.

## Features

- Lead capture form
- Website scraping
- AI-generated business audit reports
- Automated PDF report generation
- Email delivery system
- Google Sheets lead logging
- Local PDF archiving
- REST API backend

## Tech Stack

### Frontend
- React.js
- Vite
- Tailwind CSS

### Backend
- Django
- Django REST Framework

### AI & Automation
- Google Gemini API
- BeautifulSoup
- ReportLab
- Gmail SMTP
- Google Sheets API

---

## Setup Instructions

### Backend

```bash
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py runserver
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Workflow

1. User submits lead form
2. Website content is scraped
3. AI generates business audit
4. PDF report is generated
5. Report emailed automatically
6. Lead logged into Google Sheets

---

## Future Improvements

- OAuth-based Google Drive uploads
- Advanced AI personalization
- Dashboard analytics
- Deployment with Docker
- CRM integrations

---

## Author

Dev Mishra
