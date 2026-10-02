from src.analytics.portfolio_analyzer import PortfolioAnalyzer

import pytest
import numpy as np

def test_calculate_covariance():
    returns_a = [0.01, 0.02, 0.03]
    returns_b = [0.02, 0.04, 0.06]

    analyzer = PortfolioAnalyzer([returns_a, returns_b])

    covariance = analyzer.calculate_covariance(
        returns_a, returns_b
    )

    assert round(covariance, 6) == 0.000133

def test_calculate_correlation():
    returns_a = [0.01, 0.02, 0.03]
    returns_b = [0.02, 0.04, 0.06]

    analyzer = PortfolioAnalyzer([returns_a, returns_b])

    correlation = analyzer.calculate_correlation(
        returns_a, returns_b
    )

    assert round(correlation, 4) == 1.0

def test_calculate_covariance_matrix():
    returns = [
        [0.01, 0.02, 0.03],
        [0.02, 0.04, 0.06],
        [0.03, 0.02, 0.01]
    ]

    analyzer = PortfolioAnalyzer(returns)

    matrix = analyzer.calculate_covariance_matrix()

    assert len(matrix) == 3
    assert len(matrix[0]) == 3
    assert round(matrix[0][1], 6) == 0.000133

def test_covariance_matrix_is_symmetric():
    returns = [
        [0.01, 0.02, 0.03],
        [0.02, 0.04, 0.06],
        [0.03, 0.02, 0.01]
    ]

    analyzer = PortfolioAnalyzer(returns)

    matrix = analyzer.calculate_covariance_matrix()

    assert matrix[0][1] == matrix[1][0]
    assert matrix[0][2] == matrix[2][0]
    assert matrix[1][2] == matrix[2][1]

def test_get_covariance_matrix():
    returns = [
        [0.01, 0.02, 0.03],
        [0.02, 0.04, 0.06],
        [0.03, 0.02, 0.01]
    ]

    analyzer = PortfolioAnalyzer(returns)

    matrix = analyzer.get_covariance_matrix()

    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (3, 3)

def test_calculate_portfolio_volatility():
    returns = [
        [0.01, 0.02, 0.03],
        [0.02, 0.04, 0.06],
        [0.03, 0.02, 0.01]
    ]

    analyzer = PortfolioAnalyzer(returns)

    weights = np.array([0.5, 0.3, 0.2])

    volatility = analyzer.calculate_portfolio_volatility(weights)

    assert round(volatility, 6) == 0.007348

def test_calculate_portfolio_return():
    average_returns = np.array([0.02, 0.04, 0.01])
    weights = np.array([0.5, 0.3, 0.2])

    analyzer = PortfolioAnalyzer([])

    portfolio_return = analyzer.calculate_portfolio_return(
        average_returns, weights
    )

    assert round(portfolio_return, 4) == 0.024

def test_invalid_portfolio_weights():
    analyzer = PortfolioAnalyzer([])

    weights = np.array([0.5, 0.5, 0.5])

    with pytest.raises(ValueError):
        analyzer.validate_weights(weights)

def test_negative_portfolio_weights():
    analyzer = PortfolioAnalyzer([])

    weights = np.array([0.7, -0.2, 0.5])

    with pytest.raises(ValueError):
        analyzer.validate_weights(weights)

def test_find_minimum_risk_weights():
    returns = [
        [0.01, 0.02, 0.03],
        [0.02, 0.04, 0.06],
        [0.03, 0.02, 0.01]
    ]

    analyzer = PortfolioAnalyzer(returns)

    weights = analyzer.find_minimum_risk_weights()

    assert len(weights) == 3
    assert round(sum(weights), 6) == 1.0
    assert all(weight >= 0 for weight in weights)

def test_minimum_risk_is_lower_than_equal_weight():
    returns = [
        [0.01, 0.02, 0.03],
        [0.02, 0.04, 0.06],
        [0.03, 0.02, 0.01]
    ]

    analyzer = PortfolioAnalyzer(returns)

    equal_weights = np.array([1 / 3, 1 / 3, 1 / 3])

    equal_weight_risk = analyzer.calculate_portfolio_volatility(
        equal_weights
    )

    optimized_weights = analyzer.find_minimum_risk_weights()

    optimized_risk = analyzer.calculate_portfolio_volatility(
        optimized_weights
    )

    assert optimized_risk <= equal_weight_risk

def test_calculate_sharpe_ratio():
    portfolio_return = 0.08
    risk_free_rate = 0.02
    portfolio_volatility = 0.10

    analyzer = PortfolioAnalyzer([])

    sharpe_ratio = analyzer.calculate_sharpe_ratio(
        portfolio_return,
        risk_free_rate,
        portfolio_volatility
    )

    assert round(sharpe_ratio, 4) == 0.6

def test_sharpe_ratio_zero_volatility():
    analyzer = PortfolioAnalyzer([])

    with pytest.raises(ValueError):
        analyzer.calculate_sharpe_ratio(
            0.08,
            0.02,
            0
        )

def test_maximize_sharpe_ratio():
    returns = [
        [0.01, 0.02, 0.03],
        [0.02, 0.04, 0.05],
        [0.03, 0.025, 0.018]
    ]

    analyzer = PortfolioAnalyzer(returns)

    average_returns = np.array([0.02, 0.04, 0.01])
    risk_free_rate = 0.01

    weights = analyzer.maximize_sharpe_ratio(
        average_returns,
        risk_free_rate
    )

    assert len(weights) == 3
    assert round(sum(weights), 6) == 1.0
    assert all(weight >= 0 for weight in weights)
