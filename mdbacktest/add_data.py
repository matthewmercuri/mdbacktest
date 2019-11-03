import pandas as pd


class AddData:

    def simple_moving_average(self, period):
        '''Takes in the events object and extracts df. From there, it
        creates a new column that computes the moving average for the
        desired period

        arguments:
        self(df): df of all stock data
        period(int): a period in which we would like to compute a
                    moving average

        returns:
        stock_df(df): returns a df comtaiing a new column of SMA
        '''
        try:
            df = self
            assert df == pd.DataFrame
        except TypeError:
            print(f'{self} is not a DataFrame!')
