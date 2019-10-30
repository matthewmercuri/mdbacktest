class Trade:

    def __init__(self):
        pass

    def buy_stock(self, portfolio, security, units, price):
        '''buys security and adds it to the portfolio.
        First checks if the trade is valid given the current
        positions and cash balance. Logs the trade afterward.

        arguments:
        portfolio (df): current state of the portfolio
        security (str): the ticker of the equity
        units (int): the number of units to buy
        price (float): the market price to purchase the shares

        returns:
        portfolio (df): new state of the portfolio after trade
        '''
        pass

    def sell_stock(self, portfolio, security, units, price):
        '''sells security and removes it from the portfolio.
        First checks if the trade is valid given the current
        positions and cash balance. Logs the trade afterward.

        arguments:
        portfolio (df): current state of the portfolio
        security (str): the ticker of the equity
        units (int): the number of units to sell
        price (float): the market price to sell the shares

        returns:
        portfolio (df): new state of the portfolio after trade
        '''
        pass
