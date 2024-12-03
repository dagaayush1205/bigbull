import yfinance as yf
import pandas as pd

ticker = "AAPL"
data = yf.download(ticker, start="2017-01-01", end="2017-12-31", interval="1h")

data.to_csv("AAPL_2017.csv")

print(data.head())
