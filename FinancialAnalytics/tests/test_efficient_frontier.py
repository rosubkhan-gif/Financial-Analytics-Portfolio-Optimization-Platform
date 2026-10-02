from src.analytics.efficient_frontier import EfficientFrontier
from src.analytics.portfolio_analyzer import PortfolioAnalyzer


def test_generate_frontier():
    """Test efficient frontier generation."""
    returns = [
        [0.01, 0.02, 0.03],
        [0.02, 0.03, 0.04],
        [0.03, 0.02, 0.01]
    ]

    analyzer = PortfolioAnalyzer(returns)

    average_returns = [
        0.02,
        0.03,
        0.02
    ]

    frontier = EfficientFrontier(
        analyzer,
        average_returns
    )

    portfolios = frontier.generate_frontier(10)

    assert len(portfolios) == 10

    for portfolio in portfolios:
        weights = portfolio["weights"]

        assert len(weights) == 3
        assert abs(sum(weights) - 1) < 0.000001
        assert portfolio["volatility"] >= 0
