from typing import List, Dict
import csv
from fetchers.common import normalize_article

def fetch_from_csv(csv_path: str) -> List[Dict]:
    articles = []

    with open(csv_path, newline="", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)

        for row in reader:
            article = normalize_article(
                title=row.get("title"),
                content=row.get("text"), # main article text
                source="csv",
                url="",                  # not present
                fetched_at=""          
            )
            articles.append(article)

    return articles
