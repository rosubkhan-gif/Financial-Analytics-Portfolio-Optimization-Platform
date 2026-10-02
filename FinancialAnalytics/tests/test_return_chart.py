import matplotlib

matplotlib.use("Agg")

from pathlib import Path

from src.data.price_loader import PriceLoader
from src.analytics.multi_asset_analyzer import MultiAssetAnalyzer
from src.visualization.return_chart import plot_returns


def test_plot_returns(tmp_path):
    loader = PriceLoader("data/sample_prices.csv")

    prices = loader.get_all_closing_prices()
    data = loader.load_data()

    analyzer = MultiAssetAnalyzer(prices)

    returns = analyzer.calculate_returns()

    dates = data["Date"]

    file_path = tmp_path / "daily_returns.png"

    plot_returns(
        dates,
        returns,
        file_path
    )

    assert Path(file_path).exists()
