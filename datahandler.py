import datafetcher
import os



#Deletes all previous data saved to the working folder if it
#deletedata is True
def delete_old_data(deletedata=False):

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
def grab_ticker_dfs(tradeables):

	delete_old_data(False)

	for ticker in tradeables:
		df = datafetcher.dailydata(ticker, get_csv=True)


#grab_ticker_dfs(['AAPL'])






if __name__ == "__main__":
    pass
