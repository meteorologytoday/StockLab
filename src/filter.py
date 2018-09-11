import datetime
import numpy as np
import pickle
from yahoofinancials import YahooFinancials
import pprint
import StockAnalysis as SA
filename = "../data/generic.pickle"

pp = pprint.PrettyPrinter(indent=4)

tickers = pickle.load( open(filename, "rb") )
target_symbols = list(tickers.symbols.keys())[0:2]

beg = (datetime.date.today() - datetime.timedelta(366)).strftime("%Y-%m-%d")
end = (datetime.date.today() - datetime.timedelta(  1)).strftime("%Y-%m-%d")

print("Time: %s to %s", beg, end)


def makeStockArray(stock_prices):
    prices = stock_prices['prices']

    ts    = np.zeros((len(prices),), dtype=float)
    hs    = np.zeros_like(ts)
    ls    = np.zeros_like(ts)
    vols  = np.zeros_like(ts)
    clos  = np.zeros_like(ts)
    opns  = np.zeros_like(ts)

    for i, price in enumerate(prices):
        ts[i] = price['date'] 
        hs[i] = price['high'] 
        ls[i] = price['low'] 
        vols[i] = price['volume'] 
        clos[i] = price['close'] 
        opns[i] = price['open'] 

    return opns, clos, hs, ls, vols



for i, target_symbol in enumerate(target_symbols):
    yahoo_financials = YahooFinancials(target_symbol)
    historical_stock_prices = yahoo_financials.get_historical_price_data(beg, end, 'daily')

    print("Ticker: %s" % (tickers.symbols[target_symbol],))
    opns, clos, hs, ls, vols = makeStockArray(historical_stock_prices[target_symbol])

    data = SA.getAnalysis(clos)
    import matplotlib.pyplot as plt

    plt.figure()
    plt.plot(data['macd'])
    plt.plot(data['dif'])
    plt.show()
    pp.pprint(clos)
