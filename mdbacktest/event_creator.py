import pandas as pd

#takes a df and the frequency and returns a new df
#with indicator column built
def _date_frequency_helper(df, n):
	if n == 5:
		frequency = 'weekly'
	elif n == 21:
		frequency = 'monthly'
	elif n == 252:
		frequency = 'yearly'
	else:
		frequency = 'arbitrary'

	total_row_count = len(df)
	print(total_row_count)
	df[f'date_frequency_{frequency}'] = 0
	#iterates through all rows of df and flags every nth row
	for i in range(0, total_row_count, n):
		if i % n == 0:
			if i != 0:
				df.iloc[i, df.columns.get_loc(f'date_frequency_{frequency}')] = 1

	return df






class Events:

	#methods that can be applied to DF
	def __init__(self):
		pass

	def momentum(self):
		pass

	def date_frequency(self, frequency):

		if isinstance(self, pd.DataFrame):

			if frequency == 'daily':
				self['date_frequency_daily'] = 1
			elif frequency == 'weekly':
				_date_frequency_helper(self, 5)
			elif frequency == 'monthly':
				_date_frequency_helper(self, 21)
			elif frequency == 'yearly':
				_date_frequency_helper(self, 252)
			elif frequency == int:
				_date_frequency_helper(self, frequency)
			else:
				print('Wrongly defined frequency!')

		else:
			print('You did not pass a pandas DataFrame!')




if __name__ == "__main__":
    pass
