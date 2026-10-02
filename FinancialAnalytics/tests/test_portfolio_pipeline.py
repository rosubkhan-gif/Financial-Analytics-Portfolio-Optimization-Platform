from src.analytics.portfolio_analyzer import PortfolioAnalyzer
from src.analytics.portfolio_pipeline import PortfolioPipeline


def test_create_analyzer():
    pipeline = PortfolioPipeline(
        "data/sample_prices.csv"
    )

    analyzer = pipeline.create_analyzer()

    assert isinstance(analyzer, PortfolioAnalyzer)
    assert len(analyzer.returns) == 3
    assert len(analyzer.returns[0]) == 9

def test_create_covariance_matrix():
    pipeline = PortfolioPipeline(
        "data/sample_prices.csv"
    )

    analyzer = pipeline.create_analyzer()

    covariance_matrix = analyzer.get_covariance_matrix()

    assert covariance_matrix.shape == (3, 3)
    assert covariance_matrix[0][0] > 0
    assert covariance_matrix[1][1] > 0
    assert covariance_matrix[2][2] > 0

    assert covariance_matrix[0][1] == covariance_matrix[1][0]
    assert covariance_matrix[0][2] == covariance_matrix[2][0]
    assert covariance_matrix[1][2] == covariance_matrix[2][1]

def test_calculate_portfolio_volatility():
    pipeline = PortfolioPipeline(
        "data/sample_prices.csv"
    )

    analyzer = pipeline.create_analyzer()

    weights = [0.4, 0.3, 0.3]

    volatility = analyzer.calculate_portfolio_volatility(
        weights
    )

    assert volatility > 0
    assert volatility < 0.1

def test_calculate_portfolio_return():
    pipeline = PortfolioPipeline(
        "data/sample_prices.csv"
    )

    analyzer = pipeline.create_analyzer()

    average_returns = []

    for returns in analyzer.returns:
        average_return = sum(returns) / len(returns)
        average_returns.append(average_return)

    weights = [0.4, 0.3, 0.3]

    portfolio_return = analyzer.calculate_portfolio_return(
        average_returns,
        weights
    )

    assert portfolio_return > -0.1
    assert portfolio_return < 0.1

def test_calculate_sharpe_ratio():
    pipeline = PortfolioPipeline(
        "data/sample_prices.csv"
    )

    analyzer = pipeline.create_analyzer()

    average_returns = []

    for returns in analyzer.returns:
        average_return = sum(returns) / len(returns)
        average_returns.append(average_return)

    weights = [0.4, 0.3, 0.3]

    portfolio_return = analyzer.calculate_portfolio_return(
        average_returns,
        weights
    )

    portfolio_volatility = analyzer.calculate_portfolio_volatility(
        weights
    )

    risk_free_rate = 0.001

    sharpe_ratio = analyzer.calculate_sharpe_ratio(
        portfolio_return,
        risk_free_rate,
        portfolio_volatility
    )

    assert portfolio_volatility > 0
    assert sharpe_ratio != 0

def test_find_minimum_risk_weights():
    pipeline = PortfolioPipeline(
        "data/sample_prices.csv"
    )

    analyzer = pipeline.create_analyzer()

    weights = analyzer.find_minimum_risk_weights()

    assert len(weights) == 3
    assert abs(sum(weights) - 1.0) < 0.000001

    for weight in weights:
        assert weight >= 0
        assert weight <= 1

    optimized_volatility = (
        analyzer.calculate_portfolio_volatility(weights)
    )

    equal_weights = [1 / 3, 1 / 3, 1 / 3]

    equal_weight_volatility = (
        analyzer.calculate_portfolio_volatility(equal_weights)
    )

    assert optimized_volatility <= equal_weight_volatility

def test_maximize_sharpe_ratio():
    pipeline = PortfolioPipeline(
        "data/sample_prices.csv"
    )

    analyzer = pipeline.create_analyzer()

    average_returns = []

    for returns in analyzer.returns:
        average_return = sum(returns) / len(returns)
        average_returns.append(average_return)

    risk_free_rate = 0.001

    weights = analyzer.maximize_sharpe_ratio(
        average_returns,
        risk_free_rate
    )

    assert len(weights) == 3
    assert abs(sum(weights) - 1.0) < 0.000001

    for weight in weights:
        assert weight >= 0
        assert weight <= 1

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

    assert portfolio_volatility > 0
    assert sharpe_ratio != 0
