# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:44:57 2020

@author: dhruv
"""

import pandas as pd
import yfinance as yf

stocks=["IDEA.NS","HDFCBANK.NS","MSFT"]
period="1d"
def Create_Data(stocks,period):
    for stock in stocks:
        name=str(stock)
        
        ticker=yf.Ticker(name)
        data=ticker.history(period=period)
        data=data[["Open",'High',"Close","Low"]]
        data.to_excel(name+".xlsx")
    
    

Create_Data(stocks, period)
        
        
            
            
            
        
        
    