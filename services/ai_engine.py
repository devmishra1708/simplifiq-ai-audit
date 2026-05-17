import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)


def generate_company_audit(
    company_name,
    website_data
):

    fallback_audit = f"""
# AI Business Audit Report

## Company Overview
{company_name} appears to operate in a competitive digital business environment with opportunities for automation and scalable growth.

## Website Analysis
The company website presents business information and customer-focused messaging. Improving clarity, CTA placement, and modern UX patterns could improve engagement.

## Growth Opportunities
- Improve SEO optimization
- Enhance conversion funnels
- Introduce AI-powered customer workflows
- Optimize lead nurturing systems

## AI Automation Opportunities
- AI chatbot integration
- Automated lead qualification
- AI email personalization
- Customer analytics dashboards

## Lead Generation Improvements
- Stronger landing pages
- Better CTA positioning
- Automated follow-up systems
- Personalized outreach workflows

## Strategic Recommendations
The business can benefit significantly from AI-driven automation and modern conversion optimization strategies to improve operational efficiency and customer acquisition.
"""

    try:

        model = genai.GenerativeModel(
            "gemini-1.5-flash"
        )

        prompt = f"""
        You are an expert AI business consultant.

        Analyze this company professionally.

        Company:
        {company_name}

        Website Data:
        {website_data}

        Generate:
        1. Company Overview
        2. Website Analysis
        3. Growth Opportunities
        4. AI Recommendations
        5. Lead Generation Improvements
        6. Final Strategic Advice

        Make it highly personalized.
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        print("Gemini API Failed:", e)

        return fallback_audit