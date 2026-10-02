import pandas as pd

from src.data.database import PriceDatabase
from src.data.price_loader import PriceLoader


class DatabasePipeline:
    """Load price data into a database."""

    def __init__(self, csv_path, database_path):
        """Initialize the database pipeline."""
        self.loader = PriceLoader(csv_path)
        self.database = PriceDatabase(database_path)

    def import_data(self):
        """Import CSV data into the database."""
        data = self.loader.load_data()

        self.database.insert_prices(data)

    def load_data(self):
        """Load database data as a DataFrame."""
        rows = self.database.get_all_prices()

        return pd.DataFrame(
            rows,
            columns=["Date", "Asset", "Price"]
        )
