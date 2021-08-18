from pytickersymbols import PyTickerSymbols
import yfinance as yf
import datetime as dt
import pickle
import pandas as pd
import time
import gc
import readchar
import Merge
import os


path = os.getcwd()

csvpath = path+"/csv"

stockpath = path+"/csv/sub"
# print(stockpath)

filelist = []
for file in os.listdir(stockpath):
    if os.path.isfile(os.path.join(stockpath, file)):
        filelist.append(stockpath+"/" + file)
# print("--------------------------------------------")
filelist.sort()
# for f in filelist:
#     print(f)

outpath = path + "/data/1 Day/"
start = dt.datetime(2000, 1, 1)
end = dt.datetime.today()
interval = "1d"

# #############################################################################
def get_yahoo_data(tickers, start, end, interval):
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
        
    return Data


# ############################################################################

for file in filelist:
    tickers = list(pd.read_csv(file)["Ticker"])

    data = {}
    data = get_yahoo_data(tickers, start, end, interval)

    for i in tickers:
        df = data[i]
        f = outpath + i + ".csv"
        df.to_csv(f)

    print(file+ "--Finish----")
    gc.collect()
    del data
    del df
    print("wait 5 second")
    time.sleep(5)

print("press any key to exit!!")
k = readchar.readchar()
