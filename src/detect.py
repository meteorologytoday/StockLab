import datetime
import numpy as np
from scipy import stats
from scipy import signal
import pickle
from yahoofinancials import YahooFinancials
import pprint
import StockAnalysis as SA
import random
import pandas as pd
import sys



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

target = sys.argv[1]
target_N = int(sys.argv[2])

valid_stock_exchanges = {
    'US': [
        'ASE',
        'CME',
        'CMX',
        'DJI',
        'NAS',
        'NCM',
        'NGM',
        'NIM',
        'NMS',
        'NYB',
        'NYM',
        'NYQ',
        'NYS',
        'PCX',
        'WCB',
    ], 'TW': [
    'TAI',
    'TWO',
    ]
}[target]

print("Now select: %s" % target)
print("Included Stock Exchange: ")
print(valid_stock_exchanges)

print("Going to test %d stocks." % target_N)

filename = "../data/generic.pickle"

pp = pprint.PrettyPrinter(indent=4)

tickers = pickle.load( open(filename, "rb") )

beg = (datetime.date.today() - datetime.timedelta(366)).strftime("%Y-%m-%d")
end = (datetime.date.today() - datetime.timedelta(  1)).strftime("%Y-%m-%d")

data = {}
result = []


print("Time: %s to %s" % (beg, end))

# Randomly choose some stock ticker out
print("Randomly pick tickers...")
tmp = list(tickers.symbols.keys())


target_symbols = []

for target_symbol in tmp:
    # Judge exchange center
    stock_exchange = tickers.symbols[target_symbol].exchange
    if stock_exchange in valid_stock_exchanges:
        target_symbols.append(target_symbol)


print("There are %d target symbols." % len(target_symbols))

random.shuffle(target_symbols)

cnt = 0
for i, target_symbol in enumerate(target_symbols):
    # Judge exchange center
    stock_exchange = tickers.symbols[target_symbol].exchange
    if stock_exchange not in valid_stock_exchanges:
        continue

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
    close_p = stock['close']
    close_p_clean = close_p[np.isfinite(close_p)] 
    ana = SA.getAnalysis(close_p)

    long_term  = close_p[-20:]
    short_term = close_p[-5:]

    avg_price = np.mean(long_term)


    long_slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(long_term)), long_term)
    short_slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(short_term)), short_term)
  

    variability = np.mean(np.abs((close_p_clean[1:] - close_p_clean[:-1]) / avg_price))
  
    detrend = signal.detrend(close_p_clean) 
    power = np.abs(np.fft.fft(detrend)) ** 2.0
    tot_power = np.sum(power)
    n = int(np.floor(len(detrend) / 30.0))
    sw_rel_pow = np.sum(power[n:]) / tot_power

 
    if short_slope > long_slope  and avg_price > 15.0 and sw_rel_pow > 0.1:
        result.append([target_symbol, long_slope, short_slope, avg_price, variability])
        print("MATCH.")
    else:

        print("X.")

    cnt += 1
    if cnt >= 100:
        break

# Output data result

print("# Result:")
result.sort(key=lambda r: r[0])
for target_symbol in result:
    print(target_symbol)



df = pd.DataFrame(result, columns=["Symbol", "Long_term_slope", "Short_term_slope", "Avg_price", "Variability"])

df.to_csv("../data//simple_analysis_%s.csv" % target, encoding='utf-8', index=False)


