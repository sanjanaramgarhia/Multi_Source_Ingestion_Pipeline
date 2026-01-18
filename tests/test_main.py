from main import run


def test_main_run(monkeypatch):
    # mock data
    fake_article = {
        "title": "test",
        "description": "",
        "content": "hello",
        "source": "test",
        "url": "",
        "fetched_at": "2026-01-01T00:00:00Z"
    }

    # mock fetchers
    monkeypatch.setattr(
        "main.fetch_from_newsapi",
        lambda: [fake_article]
    )
    monkeypatch.setattr(
        "main.fetch_from_csv",
        lambda path: [fake_article]
    )
    monkeypatch.setattr(
        "main.fetch_from_web",
        lambda: [fake_article]
    )

    data = run()

    assert isinstance(data, list)
    assert len(data) == 3
