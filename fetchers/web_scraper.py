import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from fetchers.common import normalize_article

def fetch_from_web() -> List[Dict]:
    url = "https://www.geeksforgeeks.org/python-programming-language/"
    articles = []

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("h1")
    paragraphs = soup.find_all("p")

    title = title_tag.get_text(strip=True) if title_tag else "Example Website"

    content = " ".join(
        p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)
    )

    article = normalize_article(
        title=title,
        content=content,
        source="web",
        url=url,
        fetched_at=""
    )

    articles.append(article)

    return articles
