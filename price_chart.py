import matplotlib.pyplot as plt


def plot_prices(data, file_path=None):
    """Plot historical prices for all assets."""
    dates = data["Date"]

    for column in data.columns[1:]:
        plt.plot(
            dates,
            data[column],
            label=column
        )

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Historical Asset Prices")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    if file_path is not None:
        plt.savefig(file_path)

    plt.show()
    plt.close()
