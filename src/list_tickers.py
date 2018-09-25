import datetime
import numpy as np
from scipy import stats
import pickle
from yahoofinancials import YahooFinancials
from pprint import pprint
import StockAnalysis as SA
import random

filename = "../data/generic.pickle"

#pp = pprint.PrettyPrinter(indent=4)

tickers = pickle.load( open(filename, "rb") )
target_symbols = list(tickers.symbols.keys())[0:2]


beg = (datetime.date.today() - datetime.timedelta(366)).strftime("%Y-%m-%d")
end = (datetime.date.today() - datetime.timedelta(  1)).strftime("%Y-%m-%d")

print("Time: %s to %s" % (beg, end))

target_symbols = list(tickers.symbols.keys())


exchanges = []

for target_symbol in target_symbols:
    #print(target_symbol)
    _exchange = [
        tickers.symbols[target_symbol].exchange,
        tickers.symbols[target_symbol].exchangeDisplay 
    ]
    
    flag = False
    for exchange in exchanges:
        if exchange[0] == _exchange[0] and exchange[1] == _exchange[1]:
            flag = True
            break

    if flag == False:
        exchanges.append(_exchange)

exchanges.sort(key=lambda ex: ex[0])

pprint(exchanges)
    
