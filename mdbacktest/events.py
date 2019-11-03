class Events:

    def sma_crossover(self, stock_df, short_period, long_period):
        '''Compares the short period and the long period SMAs and
        creates a new column that signals the event, should they
        crossover. We use the stock_df to find the short period
        and the long period for the SMAs

        arguments:
        stock_df (df): accepts a df of stock data
        short_period (int): shorter length period
        long_period (int): longer length period

        returns:
        stock_df (df): creaetes a new column contain the event
                       of a SMA crossover between the two periods
        '''
        pass

    def rebalance_trigger(self, rebalance_period):
        '''Creates a new column that contains an indicator
        for whatever period we are to rebalance the portfolio.

        arguments:
        rebalance_period (str or int): how often we want to
                                       rebalance

        retruns:
        stock_df (df): contains new indicators column for the
                       event triggering a rebalance
        '''
        pass
