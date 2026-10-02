from src.analytics.stock_analyzer import StockAnalyzer


class MultiAssetAnalyzer:
    """Analyze multiple assets."""

    def __init__(self, prices):
        """Initialize the multi-asset analyzer."""
        self.prices = prices

    def calculate_returns(self):
        """Calculate returns for every asset."""
        all_returns = {}

        for asset in self.prices:
            analyzer = StockAnalyzer(self.prices[asset])
            all_returns[asset] = analyzer.calculate_returns()

        return all_returns

    def get_returns_list(self):
        """Return all asset returns as a list."""
        all_returns = self.calculate_returns()

        return list(all_returns.values())
