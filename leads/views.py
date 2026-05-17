from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from services.email_service import (
    send_audit_email
)

from services.scraper import (
    scrape_company_website
)

from services.ai_engine import (
    generate_company_audit
)

from services.pdf_generator import (
    generate_pdf_report
)

from services.google_services import (
    log_lead_to_sheets
)

@api_view(['POST'])
def submit_lead(request):

    try:

        data = request.data

        company_name = data.get(
            "company_name"
        )

        website = data.get(
            "website"
        )

        website_data = scrape_company_website(
            website
        )

        audit = generate_company_audit(
            company_name,
            website_data
        )

        pdf_path = generate_pdf_report(
            company_name,
            audit
        )
        pdf_link = pdf_path
        
        
        send_audit_email(
            data.get("email"),
            company_name,
            pdf_path
        )
        log_lead_to_sheets(
            data.get("name"),
            data.get("email"),
            company_name,
            "Completed",
            pdf_link
        )

        return Response({

            "message": "Audit Generated",

            "audit": audit,

            "pdf_path": pdf_path

        }, status=status.HTTP_200_OK)

    except Exception as e:

        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)