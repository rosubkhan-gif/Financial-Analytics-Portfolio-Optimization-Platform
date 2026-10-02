import matplotlib

matplotlib.use("Agg")

from pathlib import Path

from src.data.price_loader import PriceLoader
from src.visualization.price_chart import plot_prices


def test_plot_prices(tmp_path):
    loader = PriceLoader("data/sample_prices.csv")

    data = loader.load_data()

    file_path = tmp_path / "historical_prices.png"

    plot_prices(data, file_path)

    assert Path(file_path).exists()
