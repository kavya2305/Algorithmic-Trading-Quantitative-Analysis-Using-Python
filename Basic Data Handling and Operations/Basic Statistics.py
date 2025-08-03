# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 22:41:54 2025

@author: kavya
"""

import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","MSFT","FB","GOOG"]
start =dt.datetime.today()-dt.timedelta(3650)
end=dt.datetime.today()
cl_price=pd.DataFrame()

for ticker in stocks:
    cl_price[ticker]=yf.download(ticker,start,end)["Close"]

#Some basic stats    
cl_price.dropna(axis=0,inplace=True,how="any")    
cl_price.mean()
cl_price.std()
cl_price.median()
cl_price.describe()

#Below two methods is for daily return
daily_return=cl_price.pct_change()
daily_return1=cl_price/cl_price.shift(1) - 1

#In Quant Finance stats on the returns are of value rather than on price
daily_return.mean()
daily_return.std()
daily_return.describe()

#Rolling operations
daily_return.rolling(window=10).mean()
daily_return.rolling(window=10).std()
daily_return.rolling(window=10).max()
daily_return.rolling(window=10).min()

#equivalent Weighted
daily_return.ewm(com=10,min_periods=10).mean()
