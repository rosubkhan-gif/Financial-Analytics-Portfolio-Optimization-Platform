from pathlib import Path

from src.data.historical_importer import HistoricalDataImporter


PROJECT_ROOT = Path(__file__).resolve().parents[2]

files = {
    "AAPL": PROJECT_ROOT / "data" / "raw" / "AAPL.csv",
    "MSFT": PROJECT_ROOT / "data" / "raw" / "MSFT.csv",
    "NVDA": PROJECT_ROOT / "data" / "raw" / "NVDA.csv"
}

output_path = PROJECT_ROOT / "data" / "historical_prices.csv"

importer = HistoricalDataImporter(files)

importer.convert(output_path)
