import sqlite3


class PriceDatabase:
    """Store and retrieve historical price data."""

    def __init__(self, database_path):
        """Initialize the database."""
        self.database_path = database_path

    def create_table(self):
        """Create the prices table."""
        connection = sqlite3.connect(self.database_path)

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS prices (
                date TEXT,
                asset TEXT,
                price REAL
            )
            """
        )

        connection.commit()
        connection.close()

    def insert_prices(self, data):
        """Insert price data into the database."""
        self.create_table()

        connection = sqlite3.connect(self.database_path)

        for _, row in data.iterrows():
            date = str(row["Date"])

            for asset in data.columns[1:]:
                price = row[asset]

                connection.execute(
                    """
                    INSERT INTO prices (date, asset, price)
                    VALUES (?, ?, ?)
                    """,
                    (date, asset, price)
                )

        connection.commit()
        connection.close()

    def get_prices(self, asset):
        """Retrieve prices for one asset."""
        connection = sqlite3.connect(self.database_path)

        cursor = connection.execute(
            """
            SELECT date, price
            FROM prices
            WHERE asset = ?
            ORDER BY date
            """,
            (asset,)
        )

        results = cursor.fetchall()

        connection.close()

        return results

    def get_assets(self):
        """Return all assets in the database."""
        connection = sqlite3.connect(self.database_path)

        cursor = connection.execute(
            """
            SELECT DISTINCT asset
            FROM prices
            ORDER BY asset
            """
        )

        assets = [row[0] for row in cursor.fetchall()]

        connection.close()

        return assets

    def get_all_prices(self):
        """Retrieve all price data."""
        connection = sqlite3.connect(self.database_path)

        cursor = connection.execute(
            """
            SELECT date, asset, price
            FROM prices
            ORDER BY date, asset
            """
        )

        results = cursor.fetchall()

        connection.close()

        return results
