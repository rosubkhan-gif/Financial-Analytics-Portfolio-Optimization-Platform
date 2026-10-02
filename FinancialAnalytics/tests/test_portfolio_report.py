from src.analytics.portfolio_report import generate_portfolio_report


def test_generate_portfolio_report():
    weights = [0.4, 0.3, 0.3]

    report = generate_portfolio_report(
        "data/sample_prices.csv",
        weights,
        0.001
    )

    assert "portfolio_return" in report
    assert "portfolio_volatility" in report
    assert "sharpe_ratio" in report

    assert report["portfolio_volatility"] > 0
