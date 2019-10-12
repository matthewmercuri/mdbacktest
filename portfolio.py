import pandas as pd


#define starting parameters for portfolio
start_cash = 10000


#functions creates an empty dataframe with required columns to represent holdings in portfolio obj
def _create_starting_positions():

	df = pd.DataFrame(columns=['SecurityName','SecurityType','SecurityQuantity','UnitPurchaseValue','UnitMarketValue'])

	return df




class Myportoflio:

	def __init__(self, start_cash=start_cash):
		self.cash = start_cash
		self.positions = _create_starting_positions()








#port = Myportoflio()
#print(port.cash)
#print(port.positions.head())
