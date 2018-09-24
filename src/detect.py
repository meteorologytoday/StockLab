import datetime
import numpy as np
from scipy import stats
import pickle
from yahoofinancials import YahooFinancials
import pprint
import StockAnalysis as SA
import random


def makeStockArray(stock_prices):

    if stock_prices is None:
        raise Exception("Stock price is None.")


    prices = stock_prices['prices']

    if len(prices) == 0:
        raise Exception("No data")

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

    return {
        'time'   :   ts,
        'open'   :   opns,
        'close'  :   clos,
        'high'   :   hs,
        'low'    :   ls,
        'volume' :   vols
    }


filename = "../data/generic.pickle"

pp = pprint.PrettyPrinter(indent=4)

tickers = pickle.load( open(filename, "rb") )
target_symbols = list(tickers.symbols.keys())[0:2]


beg = (datetime.date.today() - datetime.timedelta(366)).strftime("%Y-%m-%d")
end = (datetime.date.today() - datetime.timedelta(  1)).strftime("%Y-%m-%d")

print("Time: %s to %s" % (beg, end))

# Randomly choose some stock ticker out
print("Randomly pick tickers...")
target_symbols = list(tickers.symbols.keys())
random.shuffle(target_symbols)

target_symbols = target_symbols[:100]
data = {}

result = []


for i, target_symbol in enumerate(target_symbols):

    # Download their data

    try:
        yahoo_financials = YahooFinancials(target_symbol)
        historical_stock_prices = yahoo_financials.get_historical_price_data(beg, end, 'daily')

    except Exception as e:
        print("Internal error of YahooFinancials package: %s" % e)
        continue

    print("Ticker: %s (%s)" % (target_symbol.encode('utf-8'), str(tickers.symbols[target_symbol]).encode('utf-8'),), end='')

    try:
        stock = makeStockArray(historical_stock_prices[target_symbol])
    except Exception as e:
        print(e)
        continue


    #print(stock['close'])
    #data[target_symbol] = SA.getAnalysis(clos)
    
    # Detect
    ana = SA.getAnalysis(stock['close'])

    long_term  = stock['close'][-75:]
    short_term = stock['close'][-25:]

    avg_price = np.mean(long_term)


    long_slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(long_term)), long_term)
    short_slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(short_term)), short_term)
    
    if short_slope > long_slope and avg_price > 20.0:
        result.append(target_symbol)
        print("MATCH.")
    else:

        print("X.")

# Output data result

print("# Result:")
result.sort()
for target_symbol in result:
    print("%s" % target_symbol)

