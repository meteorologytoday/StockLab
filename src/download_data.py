from yahoofinancials import YahooFinancials

ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)

balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
income_statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income')
all_statement_data_qt =  yahoo_financials.get_financial_stmts('quarterly', ['income', 'cash', 'balance'])
apple_earnings_data = yahoo_financials.get_stock_earnings_data()

historical_stock_prices = yahoo_financials.get_historical_price_data('2018-01-01', '2018-08-22', 'daily')


print(historical_stock_prices)
