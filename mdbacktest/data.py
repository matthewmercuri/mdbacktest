import pandas as pd


class Data:

    def get_stock_data(self, list_of_tickers):
        '''Iterates over the tickers in the list and pulls all the
        data for those tickers. Saves them locally at first in
        WorkingStockData/ticker.csv

        arguments:
        self (obj): our data object
        list_of_ticker (list): contains list of strings that
                               represents the tickers that we need
                               to get data for

        returns:
        None: saves tickers of all the stocks we may trade
        '''

    def simple_moving_average(self, period):
        '''Takes in the events object and extracts df. From there, it
        creates a new column that computes the moving average for the
        desired period

        arguments:
        self (obj): df of all stock data
        period (int): a period in which we would like to compute a
                      moving average

        returns:
        stock_df (df): returns a df comtaiing a new column of SMA
        '''
        try:
            df = self
            assert type(df) == pd.DataFrame
        except TypeError:
            print(f'{self} is not a DataFrame!')

    def add_event_indicators(self, list_of_events):
        '''Uses list of events to add columns of indicators for those
        events occuring, should they occur. Essentially a 1 will show
        the event occured and a 0 will show it has not

        arguments:
        self (obj): df of all stock data
        list_of_events (list): list containing strings of all the event
                               indicators to be added

        returns:
        stock_df (df): returns a df containing event indicators (ones or
                       zeros)
        '''


'''Notes:
-want this class to store all our data that we need to work our
backtrader
-maybe should reach utilize another events class to apply events to our
data
-in order to call another mehtod withing the same class, be sure
to use self.method()
'''
