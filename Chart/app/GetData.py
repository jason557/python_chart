from pytickersymbols import PyTickerSymbols
import yfinance as yf
import datetime as dt
import pickle
import pandas as pd
import time

import os
os.system("cls")

path=os.getcwd()
with open("filelist.txt", "r") as f:
    file = f.readline()

rawfile = path + "/raw/binarydata"
filelist = []
filelist.append(file)


outpath = path + "/data/1 Day/"
start = dt.datetime(2000, 1, 1)
end = dt.datetime.today()
interval = "1d"

# https://www.nasdaq.com/market-activity/stocks/screener
############################################################################


def get_yahoo_data(name, tickers, start, end, interval):
    Data = {}
    for ticker in tickers:
        # get the data
        print("get {} ...".format(ticker))
        stock = yf.download(ticker,
                            start=start,
                            end=end,
                            interval=interval,
                            progress=False)

        # drop na rows
        stock.dropna(inplace=True)

        if len(stock) == 0:
            continue

        # save to dictionary by ticker
        Data[ticker] = stock

    with open(name, "wb") as f:
        pickle.dump(Data, f)

    return Data


############################################################################

#### Read the raw data fom disk ############################################
def get_ohlcv(file):
    if os.path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
############################################################################


for file in filelist:
    tickers = list(pd.read_csv(file)["Ticker"])

    data = {}
    data = get_yahoo_data(rawfile, tickers, start, end, interval)

    for i in tickers:
        df = data[i]
        file = outpath + i + ".csv"
        df.to_csv(file)

    print("--Finish----")

time.sleep(5) 
# print("press any key to exit!!")
# x = input()
