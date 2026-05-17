import requests
from bs4 import BeautifulSoup


def scrape_company_website(url):

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.title.string if soup.title else ""

        paragraphs = soup.find_all("p")

        content = " ".join([
            p.get_text().strip()
            for p in paragraphs[:20]
        ])

        return {
            "title": title,
            "content": content[:5000]
        }

    except Exception as e:

        return {
            "error": str(e)
        }