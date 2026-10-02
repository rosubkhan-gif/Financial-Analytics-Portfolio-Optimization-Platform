import pandas as pd
import pytest

from src.data.price_loader import PriceLoader


def test_load_data(tmp_path):
    file_path = tmp_path / "prices.csv"

    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Stock_A": [100, 102],
        "Stock_B": [200, 201]
    })

    data.to_csv(file_path, index=False)

    loader = PriceLoader(file_path)
    loaded_data = loader.load_data()

    assert len(loaded_data) == 2
    assert list(loaded_data.columns) == [
        "Date",
        "Stock_A",
        "Stock_B"
    ]


def test_empty_data(tmp_path):
    file_path = tmp_path / "prices.csv"

    data = pd.DataFrame(
        columns=["Date", "Stock_A"]
    )

    data.to_csv(file_path, index=False)

    loader = PriceLoader(file_path)

    with pytest.raises(ValueError):
        loader.load_data()


def test_missing_date_column(tmp_path):
    file_path = tmp_path / "prices.csv"

    data = pd.DataFrame({
        "Stock_A": [100, 102]
    })

    data.to_csv(file_path, index=False)

    loader = PriceLoader(file_path)

    with pytest.raises(ValueError):
        loader.load_data()


def test_invalid_price(tmp_path):
    file_path = tmp_path / "prices.csv"

    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Stock_A": [100, 0]
    })

    data.to_csv(file_path, index=False)

    loader = PriceLoader(file_path)

    with pytest.raises(ValueError):
        loader.load_data()


def test_invalid_date(tmp_path):
    file_path = tmp_path / "prices.csv"

    data = pd.DataFrame({
        "Date": ["2026-01-01", "not-a-date"],
        "Stock_A": [100, 102]
    })

    data.to_csv(file_path, index=False)

    loader = PriceLoader(file_path)

    with pytest.raises(ValueError):
        loader.load_data()


def test_get_closing_prices():
    loader = PriceLoader("data/sample_prices.csv")

    prices = loader.get_closing_prices("Stock_A")

    assert prices == [
        100, 102, 101, 105, 107,
        106, 109, 111, 110, 113
    ]


def test_get_asset_names():
    loader = PriceLoader("data/sample_prices.csv")

    assets = loader.get_asset_names()

    assert assets == [
        "Stock_A",
        "Stock_B",
        "Stock_C"
    ]


def test_missing_asset():
    loader = PriceLoader("data/sample_prices.csv")

    with pytest.raises(ValueError):
        loader.get_closing_prices("Stock_D")

def test_get_all_closing_prices():
    loader = PriceLoader("data/sample_prices.csv")

    prices = loader.get_all_closing_prices()

    assert list(prices.keys()) == [
        "Stock_A",
        "Stock_B",
        "Stock_C"
    ]

    assert prices["Stock_A"][0] == 100
    assert prices["Stock_B"][0] == 200
    assert prices["Stock_C"][0] == 150

def test_duplicate_dates(tmp_path):
    file_path = tmp_path / "prices.csv"

    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-01"],
        "Stock_A": [100, 102]
    })

    data.to_csv(file_path, index=False)

    loader = PriceLoader(file_path)

    with pytest.raises(ValueError):
        loader.load_data()
