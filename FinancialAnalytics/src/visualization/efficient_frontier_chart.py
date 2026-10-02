import matplotlib.pyplot as plt


def plot_efficient_frontier(
        portfolios,
        file_path=None
):
    """Plot the efficient frontier."""
    volatilities = []
    returns = []

    for portfolio in portfolios:
        volatilities.append(
            portfolio["volatility"]
        )
        returns.append(
            portfolio["return"]
        )

    plt.plot(
        volatilities,
        returns
    )

    plt.xlabel("Portfolio Volatility")
    plt.ylabel("Portfolio Return")
    plt.title("Efficient Frontier")

    plt.tight_layout()

    if file_path is not None:
        plt.savefig(file_path)

    plt.show()
    plt.close()
