import pytest


from src.analytics.stock_analyzer import StockAnalyzer


def test_stock_analyzer_creation():
    prices = [100, 102, 101, 105]

    analyzer = StockAnalyzer(prices)

    assert analyzer.prices == prices

def test_calculate_returns():
    prices = [100, 102, 101, 105]
    analyzer = StockAnalyzer(prices)

    returns = analyzer.calculate_returns()

    assert returns[0] == 0.02
    assert round(returns[1], 4) == -0.0098
    assert round(returns[2], 4) == 0.0396

def test_calculate_volatility():
    prices = [100, 102, 101, 105]
    analyzer = StockAnalyzer(prices)

    volatility = analyzer.calculate_volatility()

    assert round(volatility, 4) == 0.0203

def test_calculate_average_return():
    prices = [100, 102, 101, 105]
    analyzer = StockAnalyzer(prices)

    average_return = analyzer.calculate_average_return()

    assert round(average_return, 4) == 0.0166

def test_empty_prices():
    with pytest.raises(ValueError):
        StockAnalyzer([])


def test_invalid_price():
    with pytest.raises(ValueError):
        StockAnalyzer([100, 0, 105])
