
##########################################################################
startstr = start.strftime("%y/%m/%d")
endstr = end.strftime("%y/%m/%d")

path = path + "\\data\\1 Day\\"

file = path + ticker + ".csv"


data = pd.read_csv(file, index_col=0, parse_dates=True)

color = mpf.make_marketcolors(
    up='red',
    down='green',
    edge='',
    wick='inherit',
    volume='inherit')
s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=color)
mpf.plot(
    data[start:end],
    mav=(20, 50),
    type='candle',
    title=ticker + "   " + startstr + " - " + endstr,
    style=s,
    tight_layout=True,
    volume=True)
