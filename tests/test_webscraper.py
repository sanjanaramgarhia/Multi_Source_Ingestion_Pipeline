from fetchers.web_scraper import fetch_from_web


def test_fetch_from_web():
    data = fetch_from_web()

    print(f"Total articles scraped: {len(data)}")
    print(data[0])

    assert len(data) > 0
