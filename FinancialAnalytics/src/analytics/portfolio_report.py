from src.analytics.portfolio_pipeline import PortfolioPipeline


def generate_portfolio_report(
        file_path,
        weights,
        risk_free_rate
):
    """Generate a portfolio analysis report."""
    pipeline = PortfolioPipeline(file_path)
    analyzer = pipeline.create_analyzer()

    average_returns = []

    for returns in analyzer.returns:
        average_return = sum(returns) / len(returns)
        average_returns.append(average_return)

    portfolio_return = analyzer.calculate_portfolio_return(
        average_returns,
        weights
    )

    portfolio_volatility = analyzer.calculate_portfolio_volatility(
        weights
    )

    sharpe_ratio = analyzer.calculate_sharpe_ratio(
        portfolio_return,
        risk_free_rate,
        portfolio_volatility
    )

    return {
        "portfolio_return": portfolio_return,
        "portfolio_volatility": portfolio_volatility,
        "sharpe_ratio": sharpe_ratio
    }
