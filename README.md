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
## Frontend screenshot
<img width="1915" height="1026" alt="image" src="https://github.com/user-attachments/assets/e4f6708a-eba2-4c24-86ec-e76c89581422" />
## Automated email with pdf attached screenshot
<img width="1917" height="1030" alt="image" src="https://github.com/user-attachments/assets/5c5d771f-5681-41f2-bbee-fa07f64e06cb" />
## Google sheets update with timestamp screenshot
<img width="1497" height="792" alt="image" src="https://github.com/user-attachments/assets/11ff563d-ed60-4860-9749-28ed19d5a444" />

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
