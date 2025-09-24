# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 23:20:15 2025
volatility Implementation
@author: kavya
"""

import yfinance as yf
import numpy as np

tickers = ["AMZN","GOOG","MSFT"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker,period='7mo',interval='1d')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp

def volatility(DF):
    "function to calculate annualized volatility of a trading strategy"
    df = DF.copy()
    df["daily_ret"] = DF["Close"].pct_change()
    vol = df["daily_ret"].std() * np.sqrt(252)
    return vol

for ticker in ohlcv_data:
    print("vol for {} = {}".format(ticker,volatility(ohlcv_data[ticker])))
