from dotenv import load_dotenv
from fetchers.newsapi import fetch_from_newsapi


def test_fetch_from_newsapi():
    load_dotenv()
    data = fetch_from_newsapi()

    print(f"Articles fetched: {len(data)}")
    print(data[0])

    assert len(data) > 0

