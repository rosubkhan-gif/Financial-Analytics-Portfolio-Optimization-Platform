from pathlib import Path

from src.data.price_loader import PriceLoader
from src.analytics.multi_asset_analyzer import MultiAssetAnalyzer
from src.analytics.portfolio_analyzer import PortfolioAnalyzer
from src.visualization.price_chart import plot_prices
from src.visualization.return_chart import plot_returns

from src.analytics.efficient_frontier import (
    EfficientFrontier
)

from src.visualization.efficient_frontier_chart import (
    plot_efficient_frontier
)

def print_weights(title, assets, weights):
    """Print portfolio weights."""
    print(title)

    for asset, weight in zip(assets, weights):
        print(f"  {asset}: {weight:.2%}")

    print()


def main():
    """Run the financial analytics application."""
    project_root = Path(__file__).resolve().parents[1]

    data_path = (
        project_root / "data" / "historical_prices.csv"
    )

    loader = PriceLoader(data_path)
    data = loader.load_data()

    prices = loader.get_all_closing_prices()
    assets = loader.get_asset_names()

    multi_asset = MultiAssetAnalyzer(prices)
    returns = multi_asset.calculate_returns()

    analyzer = PortfolioAnalyzer(
        multi_asset.get_returns_list()
    )

    average_returns = []

    for asset in assets:
        asset_returns = returns[asset]
        average_return = sum(asset_returns) / len(asset_returns)
        average_returns.append(average_return)

    equal_weights = [
        1 / len(assets)
        for i in range(len(assets))
    ]

    portfolio_return = analyzer.calculate_portfolio_return(
        average_returns,
        equal_weights
    )

    portfolio_volatility = (
        analyzer.calculate_portfolio_volatility(
            equal_weights
        )
    )

    sharpe_ratio = analyzer.calculate_sharpe_ratio(
        portfolio_return,
        0,
        portfolio_volatility
    )

    minimum_risk_weights = (
        analyzer.find_minimum_risk_weights()
    )

    maximum_sharpe_weights = (
        analyzer.maximize_sharpe_ratio(
            average_returns,
            0
        )
    )

    frontier = EfficientFrontier(
        analyzer,
        average_returns
    )

    portfolios = frontier.generate_frontier(50)

    print()
    print("=" * 50)
    print("FINANCIAL ANALYTICS REPORT")
    print("=" * 50)
    print()

    print("Assets:")
    for asset in assets:
        print(f"  {asset}")

    print()
    print("Average Daily Returns")

    for asset, average_return in zip(
            assets,
            average_returns
    ):
        print(
            f"  {asset}: {average_return:.4%}"
        )

    print()
    print("Equal-Weight Portfolio")
    print(
        f"  Return: {portfolio_return:.4%}"
    )
    print(
        f"  Volatility: {portfolio_volatility:.4%}"
    )
    print(
        f"  Sharpe Ratio: {sharpe_ratio:.4f}"
    )
    print()

    print_weights(
        "Minimum-Risk Portfolio",
        assets,
        minimum_risk_weights
    )

    print_weights(
        "Maximum-Sharpe Portfolio",
        assets,
        maximum_sharpe_weights
    )

    print("=" * 50)

    print()
    print("Generating charts...")

    chart_path = (
        project_root
        / "data"
        / "historical_prices.png"
    )

    plot_prices(data, chart_path)

    return_chart_path = (
        project_root
        / "data"
        / "daily_returns.png"
    )

    plot_returns(
        data["Date"],
        returns,
        return_chart_path
    )

    frontier_chart_path = (
            project_root
            / "data"
            / "efficient_frontier.png"
    )

    plot_efficient_frontier(
        portfolios,
        frontier_chart_path
    )

    print("Charts saved successfully.")


if __name__ == "__main__":
    main()
