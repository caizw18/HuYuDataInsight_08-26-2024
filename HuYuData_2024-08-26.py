# Here's a Python code example for performing a simple time series analysis on Google's stock price using libraries like pandas, yfinance, matplotlib, and statsmodels.
# This code will download historical stock price data, plot it, and conduct a basic analysis such as decomposing the time series to understand its components.
#
# python
# Copy code
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Download historical stock price data for Google (GOOGL)
ticker = "GOOGL"
data = yf.download(ticker, start="2015-01-01", end="2023-01-01")

# Plot the adjusted close price
plt.figure(figsize=(14, 7))
plt.plot(data['Adj Close'], label='GOOGL Adjusted Close Price')
plt.title(f'{ticker} Stock Price')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price (USD)')
plt.legend()
plt.show()

# Decompose the time series to observe trend, seasonality, and residuals
decomposition = seasonal_decompose(data['Adj Close'], model='multiplicative', period=365)

# Plot the decomposed components
plt.figure(figsize=(14, 10))

plt.subplot(411)
plt.plot(decomposition.observed, label='Observed')
plt.legend(loc='upper left')

plt.subplot(412)
plt.plot(decomposition.trend, label='Trend', color='orange')
plt.legend(loc='upper left')

plt.subplot(413)
plt.plot(decomposition.seasonal, label='Seasonality', color='green')
plt.legend(loc='upper left')

plt.subplot(414)
plt.plot(decomposition.resid, label='Residuals', color='red')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
# Explanation:
# Download Data: The code uses the yfinance library to download Google's historical stock price data.
# Plotting: It plots the adjusted close price over time.
# Decomposition: The time series is decomposed into its components: trend, seasonality, and residuals using the
# seasonal_decompose function from the statsmodels library.
# Visualization: Each component of the decomposition is plotted to give a better understanding of the underlying patterns in the stock price.