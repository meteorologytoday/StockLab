from yahoofinancials import YahooFinancials

ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)

apple_net_income = yahoo_financials.get_net_income()
