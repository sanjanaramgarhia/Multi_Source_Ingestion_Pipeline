import os
import requests
from typing import List, Dict
from fetchers.common import normalize_article

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def fetch_from_newsapi() -> List[Dict]:
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError("NEWS_API_KEY not found in environment")

    params = {
        "country": "us",
        "pageSize": 5,
        "apiKey": api_key
    }

    response = requests.get(NEWS_API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    articles = []

    for item in data.get("articles", []):
        article = normalize_article(
            title=item.get("title"),
            content=item.get("content"),
            source="newsapi",
            url=item.get("url"),
            fetched_at=item.get("publishedAt")
        )
        articles.append(article)

    return articles
