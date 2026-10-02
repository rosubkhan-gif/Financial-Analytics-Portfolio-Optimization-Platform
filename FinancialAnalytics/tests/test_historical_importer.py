import pandas as pd
import pytest

from src.data.historical_importer import HistoricalDataImporter


def create_test_file(path, prices):
    """Create a test historical price file."""
    data = pd.DataFrame({
        "Date": [
            "2026-01-01",
            "2026-01-02",
            "2026-01-03"
        ],
        "Close": prices
    })

    data.to_csv(path, index=False)


def test_convert_multiple_assets(tmp_path):
    stock_a = tmp_path / "stock_a.csv"
    stock_b = tmp_path / "stock_b.csv"
    output = tmp_path / "combined.csv"

    create_test_file(
        stock_a,
        [100, 102, 104]
    )

    create_test_file(
        stock_b,
        [200, 198, 201]
    )

    files = {
        "Stock_A": stock_a,
        "Stock_B": stock_b
    }

    importer = HistoricalDataImporter(files)

    result = importer.convert(output)

    assert len(result) == 3
    assert list(result.columns) == [
        "Date",
        "Stock_A",
        "Stock_B"
    ]

    assert result["Stock_A"].tolist() == [
        100,
        102,
        104
    ]


def test_missing_close(tmp_path):
    file_path = tmp_path / "input.csv"

    data = pd.DataFrame({
        "Date": ["2026-01-01"],
        "Open": [100]
    })

    data.to_csv(file_path, index=False)

    importer = HistoricalDataImporter({
        "Stock_A": file_path
    })

    with pytest.raises(ValueError):
        importer.convert(
            tmp_path / "output.csv"
        )


def test_empty_files(tmp_path):
    importer = HistoricalDataImporter({})

    with pytest.raises(ValueError):
        importer.convert(
            tmp_path / "output.csv"
        )
