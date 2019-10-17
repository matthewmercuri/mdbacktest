import datahandler as dh

#eventually want this to come from a file that has all the tickers
#we need to gather
tradeables = ['AAPL','TD','AMD','SPY','NFLX']

dh.grab_ticker_data(tradeables)