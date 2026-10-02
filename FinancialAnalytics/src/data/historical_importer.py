import pandas as pd


class HistoricalDataImporter:
    """Convert multiple historical files into one dataset."""

    def __init__(self, files):
        """Initialize the importer."""
        self.files = files

    def convert(self, output_path):
        """Combine historical files into one CSV."""
        combined_data = None

        for asset, file_path in self.files.items():
            data = pd.read_csv(file_path)

            if "Date" not in data.columns:
                raise ValueError(
                    "Data must contain a Date column."
                )

            if "Close" not in data.columns:
                raise ValueError(
                    "Data must contain a Close column."
                )

            data["Date"] = pd.to_datetime(
                data["Date"],
                errors="coerce"
            )

            if data["Date"].isna().any():
                raise ValueError(
                    "Dates must be valid."
                )

            if data["Close"].isna().any():
                raise ValueError(
                    "Closing prices cannot be missing."
                )

            if (data["Close"] <= 0).any():
                raise ValueError(
                    "Closing prices must be positive."
                )

            prices = data[["Date", "Close"]].copy()

            prices = prices.rename(
                columns={"Close": asset}
            )

            if combined_data is None:
                combined_data = prices
            else:
                combined_data = combined_data.merge(
                    prices,
                    on="Date",
                    how="inner"
                )

        if combined_data is None:
            raise ValueError(
                "At least one data file is required."
            )

        combined_data = combined_data.sort_values(
            "Date"
        )

        combined_data.to_csv(
            output_path,
            index=False
        )

        return combined_data
