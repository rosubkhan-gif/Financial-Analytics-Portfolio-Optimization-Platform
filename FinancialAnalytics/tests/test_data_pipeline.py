from src.analytics.stock_analyzer import StockAnalyzer
from src.data.price_loader import PriceLoader


def test_price_data_to_stock_analysis():
    loader = PriceLoader("data/sample_prices.csv")

    prices = loader.get_closing_prices("Stock_A")

    analyzer = StockAnalyzer(prices)

    returns = analyzer.calculate_returns()

    assert len(returns) == 9
    assert round(returns[0], 4) == 0.0200
    assert round(returns[1], 4) == -0.0098
    assert round(returns[2], 4) == 0.0396


def test_price_data_to_volatility():
    loader = PriceLoader("data/sample_prices.csv")

    prices = loader.get_closing_prices("Stock_A")

    analyzer = StockAnalyzer(prices)

    volatility = analyzer.calculate_volatility()

    assert round(volatility, 4) == 0.0175
