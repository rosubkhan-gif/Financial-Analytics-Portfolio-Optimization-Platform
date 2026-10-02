from src.data.price_loader import PriceLoader
from src.analytics.multi_asset_analyzer import MultiAssetAnalyzer
from src.analytics.portfolio_analyzer import PortfolioAnalyzer


class PortfolioPipeline:
    """Connect price data to portfolio analysis."""

    def __init__(self, file_path):
        """Initialize the portfolio pipeline."""
        self.loader = PriceLoader(file_path)

    def create_analyzer(self):
        """Create a portfolio analyzer from the price data."""
        prices = self.loader.get_all_closing_prices()

        multi_asset_analyzer = MultiAssetAnalyzer(prices)

        returns = multi_asset_analyzer.get_returns_list()

        return PortfolioAnalyzer(returns)
