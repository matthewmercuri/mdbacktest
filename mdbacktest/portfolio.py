import pandas as pd


class Portfolio:

    def __init__(self, starting_cash):
        '''initializes portfolio object

        arguments:
        startingcash (int): starting cash balance of the portfolio

        returns:
        portfolio (obj): cotnains all the positions and cash balance
        '''
        self.cash = starting_cash

        position_df_columns = ['SecurityName', 'SecurityType',
                               'SecurityQuantity', 'UnitPurchaseValue',
                               'UnitMarketValue']
        self.positions = pd.DataFrame(columns=position_df_columns)

    def rebalance(self, rebalance_strategy):
        '''rebalances the portfolio

        arguments:
        self (obj): the portfolio object
        rebalance_strategy(dict): a dictionary that lists the positions (key),
        how much of the porfolio should be invested in each position (value)

        returns:
        portfolio(obj): returns the portfolio object after rebalancing
        '''
