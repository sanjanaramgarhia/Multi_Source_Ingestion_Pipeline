from fetchers.csv_reader import fetch_from_csv


def test_fetch_from_csv_with_print():
    data = fetch_from_csv("sample_data.csv")

    print(f"Total rows loaded: {len(data)}")
    print("First record:")
    print(data[0])

    assert len(data) > 0
