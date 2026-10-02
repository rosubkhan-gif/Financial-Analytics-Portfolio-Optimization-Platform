import matplotlib.pyplot as plt


def plot_returns(dates, returns, file_path=None):
    """Plot daily returns for multiple assets."""
    for asset in returns:
        asset_returns = returns[asset]
        return_dates = dates[1:]

        plt.plot(
            return_dates,
            asset_returns,
            label=asset
        )

    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.title("Daily Asset Returns")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    if file_path is not None:
        plt.savefig(file_path)

    plt.show()
    plt.close()
