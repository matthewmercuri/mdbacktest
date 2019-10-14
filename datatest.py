from events import Events
import pandas as pd


#THIS IS ONLY A TEST FILE

df = pd.read_csv('WorkingStockData/AAPL.csv', index_col=0)

print(df.head())

Events.date_frequency(df, 'daily')

print(df.head())

df.to_csv('test.csv')