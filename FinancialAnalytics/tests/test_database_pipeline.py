from src.data.database_pipeline import DatabasePipeline


def test_database_pipeline(tmp_path):
    database_path = tmp_path / "prices.db"

    pipeline = DatabasePipeline(
        "data/sample_prices.csv",
        database_path
    )

    pipeline.import_data()

    data = pipeline.load_data()

    assert len(data) == 30
    assert list(data.columns) == [
        "Date",
        "Asset",
        "Price"
    ]
    assert data["Asset"].nunique() == 3
