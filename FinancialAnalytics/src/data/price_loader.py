import pandas as pd


class PriceLoader:
    """Load and validate historical price data."""

    def __init__(self, file_path):
        """Initialize the price loader."""
        self.file_path = file_path

    def load_data(self):
        """Load and validate historical price data."""
        data = pd.read_csv(self.file_path)

        if data.empty:
            raise ValueError("Price data cannot be empty.")

        if "Date" not in data.columns:
            raise ValueError("CSV must contain a Date column.")

        if len(data.columns) < 2:
            raise ValueError(
                "CSV must contain at least one asset."
            )

        data["Date"] = pd.to_datetime(
            data["Date"],
            errors="coerce"
        )

        if data["Date"].isna().any():
            raise ValueError("Dates must be valid.")

        if data["Date"].duplicated().any():
            raise ValueError("Dates cannot be duplicated.")

        asset_columns = data.columns[1:]

        for column in asset_columns:
            if data[column].isna().any():
                raise ValueError(
                    "Asset prices cannot be missing."
                )

            if (data[column] <= 0).any():
                raise ValueError(
                    "Asset prices must be positive."
                )

        data = data.sort_values("Date")

        return data

    def get_closing_prices(self, asset):
        """Return closing prices for one asset."""
        data = self.load_data()

        if asset not in data.columns:
            raise ValueError("Asset not found.")

        return data[asset].tolist()

    def get_asset_names(self):
        """Return the names of all assets."""
        data = self.load_data()

        return list(data.columns[1:])

    def get_all_closing_prices(self):
        """Return closing prices for all assets."""
        data = self.load_data()

        prices = {}

        for asset in self.get_asset_names():
            prices[asset] = data[asset].tolist()

        return prices
