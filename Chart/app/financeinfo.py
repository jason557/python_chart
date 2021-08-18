import yfinance as yf
import os
import pandas as pd
import matplotlib.pyplot as plt
import sys
plt.style.use('seaborn')


symbol = 'MSFT'
if len(sys.argv)==2:
    symbol=sys.argv[1]
else:
    symbol=input("Please input Symbol  \n")    

os.system('cls')
stock = yf.Ticker(symbol)

df = stock.dividends  # returns a dataframe
data = df.resample('Y').sum()  # sum dividends by year
data = data.reset_index()
data['Year'] = data['Date'].dt.year  # create a new dataframe co

plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend Yield (s)')
plt.xlabel('Year')
plt.title(symbol + ' Dividend History')
plt.xlim(2000, 2021)
plt.show()
