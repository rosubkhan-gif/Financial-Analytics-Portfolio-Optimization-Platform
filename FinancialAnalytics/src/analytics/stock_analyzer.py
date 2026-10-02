class StockAnalyzer:
    """Analyze historical stock price data."""

    def __init__(self, prices):
        if len(prices) == 0:
            raise ValueError("Price data cannot be empty.")

        for price in prices:
            if price <= 0:
                raise ValueError("Stock prices must be positive.")

        self.prices = prices

    def calculate_returns(self):
        """Calculate the daily returns for the stock."""
        returns = []

        for i in range(1, len(self.prices)):
            previous_price = self.prices[i - 1]
            current_price = self.prices[i]

            daily_return = (current_price - previous_price) / previous_price
            returns.append(daily_return)

        return returns

    def calculate_volatility(self):
        """Calculate the standard deviation of daily returns."""
        returns = self.calculate_returns()

        mean_return = sum(returns) / len(returns)

        squared_differences = []

        for daily_return in returns:
            difference = daily_return - mean_return
            squared_differences.append(difference ** 2)

        variance = sum(squared_differences) / len(returns)
        volatility = variance ** 0.5

        return volatility

    def calculate_average_return(self):
        """Calculate the average daily return."""
        returns = self.calculate_returns()

        average_return = sum(returns) / len(returns)

        return average_return
