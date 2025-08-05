# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 22:44:11 2025

@author: kavya
"""

# Import necesary libraries
import yfinance as yf

# Download historical data for required stocks
tickers = ["AMZN","GOOG","MSFT"]
ohlcv_data = {}

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in tickers:
    temp = yf.download(ticker,period='1mo',interval='5m')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp

def Boll_Band(DF, n=14):
    "function to calculate Bollinger Band"
    df = DF.copy()
    df["MB"] = df["Close"].rolling(n).mean()
    df["UB"] = (df["Close"].rolling(n).mean() + 2*df["Close"].rolling(n).std(ddof=0))
    df["LB"] = (df["Close"].rolling(n).mean() - 2*df["Close"].rolling(n).std(ddof=0))
    df["BB_Width"] = df["UB"] - df["LB"]
    return df[["MB","UB","LB","BB_Width"]]

for ticker in ohlcv_data:
    ohlcv_data[ticker][[("MB",ticker),("UB",ticker),("LB",ticker),("BB_Width",ticker)]] = Boll_Band(ohlcv_data[ticker])
    
    