import pandas as pd


class Portfolio:

    def __init__(self, startingcash):
        self.cash = startingcash

        position_df_columns = ['SecurityName', 'SecurityType', 'SecurityQuantity', 'UnitPurchaseValue', 'UnitMarketValue']
        self.positions = pd.DataFrame(columns=position_df_columns)
