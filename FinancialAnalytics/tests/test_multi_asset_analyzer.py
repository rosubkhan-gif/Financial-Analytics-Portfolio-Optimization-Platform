from src.analytics.multi_asset_analyzer import MultiAssetAnalyzer


def test_calculate_returns():
    prices = {
        "Stock_A": [100, 102, 101],
        "Stock_B": [200, 198, 201]
    }

    analyzer = MultiAssetAnalyzer(prices)

    returns = analyzer.calculate_returns()

    assert round(returns["Stock_A"][0], 4) == 0.0200
    assert round(returns["Stock_B"][0], 4) == -0.0100

def test_get_returns_list():
    prices = {
        "Stock_A": [100, 102, 101],
        "Stock_B": [200, 198, 201]
    }

    analyzer = MultiAssetAnalyzer(prices)

    returns = analyzer.get_returns_list()

    assert len(returns) == 2
    assert round(returns[0][0], 4) == 0.0200
    assert round(returns[1][0], 4) == -0.0100
