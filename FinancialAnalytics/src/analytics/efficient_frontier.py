import numpy as np
from scipy.optimize import minimize


class EfficientFrontier:
    """Calculate the minimum-risk portfolio for target returns."""

    def __init__(self, analyzer, average_returns):
        """Initialize the efficient frontier."""
        self.analyzer = analyzer
        self.average_returns = np.array(average_returns)

    def generate_frontier(self, number_of_points=50):
        """Generate portfolios along the efficient frontier."""
        minimum_return = min(self.average_returns)
        maximum_return = max(self.average_returns)

        target_returns = np.linspace(
            minimum_return,
            maximum_return,
            number_of_points
        )

        number_of_assets = len(self.average_returns)
        initial_weights = (
            np.ones(number_of_assets) / number_of_assets
        )

        portfolios = []

        for target_return in target_returns:

            def objective(weights):
                return self.analyzer.calculate_portfolio_volatility(
                    weights
                )

            constraints = [
                {
                    "type": "eq",
                    "fun": lambda weights: sum(weights) - 1
                },
                {
                    "type": "eq",
                    "fun": lambda weights: (
                        self.analyzer.calculate_portfolio_return(
                            self.average_returns,
                            weights
                        ) - target_return
                    )
                }
            ]

            bounds = [
                (0, 1)
                for i in range(number_of_assets)
            ]

            result = minimize(
                objective,
                initial_weights,
                method="SLSQP",
                bounds=bounds,
                constraints=constraints
            )

            if result.success:
                portfolios.append({
                    "return": target_return,
                    "volatility": result.fun,
                    "weights": result.x
                })

        return portfolios
