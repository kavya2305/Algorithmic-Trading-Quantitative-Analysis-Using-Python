# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 15:16:18 2025
Handling NaN values. Here it is done with alpha_vantage instead of Yfinance
@author: kavya
"""

import datetime as dt
import yfinance as yf
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

key_path = "C:\\Users\\kavya\\OneDrive\\\Desktop\Quantinsti\\key.txt"

stocks = ["AMZN","MSFT","FB","GOOG"]
start = "2010-02-01"
end = "2012-05-17"
cl_price = pd.DataFrame()
ohlcv = {}

for ticker in stocks:
    # cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
    ts = TimeSeries(key=open(key_path,'r').read(),output_format='pandas')
    data=ts.get_daily(ticker,outputsize='compact')[0]
    data.columns = ["open","high","low","close","volume"]
    cl_price[ticker]=data["close"]
    
    #to fillna with some values
# cl_price.fillna({"FB":0,"GOOG":1})   
# cl_price.fillna(0) 
cl_price.fillna(method='ffill',axis=0,inplace=True)

    #to drop na values
cl_price.dropna(axis=0, how='any')

for ticker in stocks:
    ohlcv['ticker']= yf.download(ticker,start,end)

