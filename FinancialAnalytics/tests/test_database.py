import sqlite3

import pandas as pd

from src.data.database import PriceDatabase


def test_create_table(tmp_path):
    database_path = tmp_path / "prices.db"

    database = PriceDatabase(database_path)

    database.create_table()

    assert database_path.exists()


def test_insert_prices(tmp_path):
    database_path = tmp_path / "prices.db"

    database = PriceDatabase(database_path)

    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Stock_A": [100, 102],
        "Stock_B": [200, 198]
    })

    database.insert_prices(data)

    connection = sqlite3.connect(database_path)

    cursor = connection.execute(
        "SELECT COUNT(*) FROM prices"
    )

    count = cursor.fetchone()[0]

    connection.close()

    assert count == 4


def test_get_prices(tmp_path):
    database_path = tmp_path / "prices.db"

    database = PriceDatabase(database_path)

    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Stock_A": [100, 102],
        "Stock_B": [200, 198]
    })

    database.insert_prices(data)

    prices = database.get_prices("Stock_A")

    assert prices == [
        ("2026-01-01", 100.0),
        ("2026-01-02", 102.0)
    ]


def test_get_assets(tmp_path):
    database_path = tmp_path / "prices.db"

    database = PriceDatabase(database_path)

    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Stock_A": [100, 102],
        "Stock_B": [200, 198]
    })

    database.insert_prices(data)

    assets = database.get_assets()

    assert assets == ["Stock_A", "Stock_B"]
