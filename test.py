import yfinance as yf

# Example: Fetching data for Reliance Industries (ticker: RELIANCE.BO)
ticker = "RELIANCE.BO"

# Fetch historical data
data = yf.download(ticker, start="2023-01-01", end="2023-12-31")

# Display the first few rows
print(data)

# Fetch live data
stock = yf.Ticker(ticker)
live_data = stock.history(period="1d")
print(live_data)

