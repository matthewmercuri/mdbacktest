import datafetcher
import os


deletedata=False

#Deletes all previous data saved to the working folder if it
#deletedata is True
def delete_old_data(deletedata):

	if deletedata == True:
		folder = 'WorkingStockData'
		for file in os.listdir(folder):
			file_path = os.path.join(folder, file)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
			except Exception as e:
				print(e)

#function takes a list of tradeable stocks and
#gathers the stock data to an API and save it
#to a CSV file
def grab_ticker_data(tradeables):

	delete_old_data(deletedata)

	len_tradeables = len(tradeables)
	i_progress = 1

	for ticker in tradeables:
		len_tradeables = len(tradeables)
		if os.path.isfile((f'WorkingStockData/{ticker}.csv')):
			print(f'{ticker} file already exists!')
		else:
			datafetcher.dailydata(ticker, get_csv=True)

		#printing the progress in gathering data
		print(round((i_progress/len_tradeables)*100, 2),'% complete!')
		i_progress += 1






if __name__ == "__main__":
    pass
