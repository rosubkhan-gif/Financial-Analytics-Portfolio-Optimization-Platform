Financial Analytics Platform

A Python-based financial analytics platform that uses statistics, linear algebra, and numerical optimization to analyze historical asset prices and portfolio risk.

Features
Historical price data processing and validation
Daily return and average return calculations
Volatility analysis
Covariance and correlation analysis
Portfolio return and volatility calculations
Sharpe ratio calculation
Minimum-risk portfolio optimization
Maximum-Sharpe portfolio optimization
Efficient frontier generation
Portfolio risk-return visualization
SQLite database storage
Automated testing with pytest
Technologies
Python
NumPy
Pandas
SciPy
Matplotlib
SQLite
Pytest
Project Structure
FinancialAnalytics/
├── data/
│   ├── raw/
│   ├── sample_prices.csv
│   └── historical_prices.csv
├── src/
│   ├── analytics/
│   ├── data/
│   ├── visualization/
│   └── main.py
├── tests/
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
How It Works

The project processes historical price data through several stages:

Historical Price Data
        ↓
Data Validation
        ↓
Return Calculation
        ↓
Risk Analysis
        ↓
Portfolio Optimization
        ↓
Efficient Frontier
        ↓
Visualizations

The portfolio analysis uses covariance matrices to measure relationships between assets and numerical optimization to find portfolio weights under constraints.

Portfolio Analysis

The platform calculates:

Average asset returns
Portfolio return
Portfolio volatility
Covariance
Correlation
Sharpe ratio

It also uses constrained optimization to calculate:

Minimum-risk portfolio weights
Maximum-Sharpe portfolio weights
Efficient frontier portfolios
Data

The current dataset contains a small synthetic dataset representing AAPL, MSFT, and NVDA price data.

The synthetic data is used for development, testing, and demonstrating the analytics pipeline. It is not real market data and should not be interpreted as actual historical investment performance.

Installation

Clone the repository and install the required Python packages:

pip install -r requirements.txt
Running the Project

Run the main application:

python src/main.py

The program generates portfolio analysis results and saves visualizations in the data directory.

Running Tests

Run the complete test suite with:

python -m pytest

The project uses pytest to test data loading, analytics, portfolio calculations, optimization, database functionality, and visualizations.

Purpose

This project was developed to apply concepts from computer science, statistics, linear algebra, and numerical optimization to a practical financial analytics problem.

The project is intended for educational and analytical purposes and does not provide financial advice.
