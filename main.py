from dotenv import load_dotenv
load_dotenv()

from fetchers.newsapi import fetch_from_newsapi
from fetchers.csv_reader import fetch_from_csv
from fetchers.web_scraper import fetch_from_web
import json
import os


def run():
    articles = []

    # 1 from NewsAPI
    news_articles = fetch_from_newsapi()
    if news_articles:
        articles.append(news_articles[0])

    # 1 from CSV
    csv_articles = fetch_from_csv("sample_data.csv")
    if csv_articles:
        articles.append(csv_articles[0])

    # 1 from Web Scraper
    web_articles = fetch_from_web()
    if web_articles:
        articles.append(web_articles[0])

    os.makedirs("output", exist_ok=True)
    with open("output/articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2)

    return articles


if __name__ == "__main__":
    run()
