import numpy as np
from scipy.optimize import minimize

class PortfolioAnalyzer:
    """Analyze relationships between multiple stocks."""

    def __init__(self, returns):
        """Initialize the portfolio analyzer."""
        self.returns = returns

    def calculate_covariance(self, returns_a, returns_b):
        """Calculate covariance between two sets of returns."""
        mean_a = sum(returns_a) / len(returns_a)
        mean_b = sum(returns_b) / len(returns_b)

        products = []

        for i in range(len(returns_a)):
            difference_a = returns_a[i] - mean_a
            difference_b = returns_b[i] - mean_b
            products.append(difference_a * difference_b)

        covariance = sum(products) / len(returns_a)

        return covariance

    def calculate_correlation(self, returns_a, returns_b):
        """Calculate correlation between two sets of returns."""
        covariance = self.calculate_covariance(returns_a, returns_b)

        mean_a = sum(returns_a) / len(returns_a)
        mean_b = sum(returns_b) / len(returns_b)

        squared_a = []
        squared_b = []

        for i in range(len(returns_a)):
            difference_a = returns_a[i] - mean_a
            difference_b = returns_b[i] - mean_b

            squared_a.append(difference_a ** 2)
            squared_b.append(difference_b ** 2)

        variance_a = sum(squared_a) / len(returns_a)
        variance_b = sum(squared_b) / len(returns_b)

        volatility_a = variance_a ** 0.5
        volatility_b = variance_b ** 0.5

        correlation = covariance / (volatility_a * volatility_b)

        return correlation

    def calculate_covariance_matrix(self):
        """Calculate the covariance matrix for all stocks."""
        matrix = []

        for returns_a in self.returns:
            row = []

            for returns_b in self.returns:
                covariance = self.calculate_covariance(
                    returns_a, returns_b
                )
                row.append(covariance)

            matrix.append(row)

        return matrix

    def get_covariance_matrix(self):
        """Return the covariance matrix as a NumPy array."""
        matrix = self.calculate_covariance_matrix()

        return np.array(matrix)

    def calculate_portfolio_volatility(self, weights):
        """Calculate portfolio volatility from asset weights."""
        covariance_matrix = self.get_covariance_matrix()

        weights = np.array(weights)

        portfolio_variance = (
                weights.T @ covariance_matrix @ weights
        )

        portfolio_volatility = portfolio_variance ** 0.5

        return portfolio_volatility

    def calculate_portfolio_return(self, average_returns, weights):
        """Calculate the weighted portfolio return."""
        average_returns = np.array(average_returns)
        weights = np.array(weights)

        portfolio_return = weights.T @ average_returns

        return portfolio_return

    @staticmethod
    def validate_weights(weights):
        """Validate portfolio weights."""
        weights = np.array(weights)

        if any(weights < 0):
            raise ValueError("Portfolio weights cannot be negative.")

        if not np.isclose(sum(weights), 1.0):
            raise ValueError("Portfolio weights must sum to 1.")

        return True

    def find_minimum_risk_weights(self):
        """Find weights that minimize portfolio volatility."""
        number_of_stocks = len(self.returns)

        initial_weights = np.ones(number_of_stocks) / number_of_stocks

        def objective(weights):
            return self.calculate_portfolio_volatility(weights)

        constraints = {
            "type": "eq",
            "fun": lambda weights: sum(weights) - 1
        }

        bounds = [(0, 1) for i in range(number_of_stocks)]

        result = minimize(
            objective,
            initial_weights,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints
        )

        if not result.success:
            raise ValueError("Portfolio optimization failed.")

        return result.x

    @staticmethod
    def calculate_sharpe_ratio(
            portfolio_return,
            risk_free_rate,
            portfolio_volatility
    ):
        """Calculate the Sharpe ratio of a portfolio."""
        if portfolio_volatility == 0:
            raise ValueError("Portfolio volatility cannot be zero.")

        sharpe_ratio = (
                               portfolio_return - risk_free_rate
                       ) / portfolio_volatility

        return sharpe_ratio

    def maximize_sharpe_ratio(self, average_returns, risk_free_rate):
        """Find weights that maximize the Sharpe ratio."""
        number_of_stocks = len(self.returns)

        initial_weights = np.ones(number_of_stocks) / number_of_stocks

        def objective(weights):
            portfolio_return = self.calculate_portfolio_return(
                average_returns, weights
            )

            portfolio_volatility = self.calculate_portfolio_volatility(
                weights
            )

            if portfolio_volatility < 1e-10:
                return 0

            sharpe_ratio = (
                portfolio_return - risk_free_rate
            ) / portfolio_volatility

            return -sharpe_ratio

        constraints = {
            "type": "eq",
            "fun": lambda weights: sum(weights) - 1
        }

        bounds = [(0, 1) for i in range(number_of_stocks)]

        result = minimize(
            objective,
            initial_weights,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints
        )

        if not result.success:
            raise ValueError("Sharpe ratio optimization failed.")

        return result.x
