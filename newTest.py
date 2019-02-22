"""
New version working with iexfinance v0.4.0
"""

from iexfinance.stocks import Stock
from securities import *


watchList = ['AAPL',
			 'AMZN',
			 'ACB',
			 'AMD',
			 'CRON',
			 'CVX',
			 'CSCO',
			 'IBM',
			 'KO',
			 'MJ',
			 'MRK',
			 'MSFT',
			 'PFE',
			 'PG',
			 'QCOM',
			 'ROKU',
			 'SO',
			 'SQ',
			 'TWTR',
			 'TLRY',
			 'TSLA',
			 'VZ',
			 'XOM']

#Retrieve price information for a single stock
def retrieveSingleStockInfo(securitiesList, stockName):

	stockObj = Stock(stockName)
	priceInfo = stockObj.get_price()
	ohlcInfo = stockObj.get_ohlc()

	price = priceInfo
	Open = ohlcInfo['open']['price']
	close = ohlcInfo['close']['price']
	high = ohlcInfo['high']
	low = ohlcInfo['low']

	#Calculate net stock change
	change = close - Open
	netChange = '{:+.2f}'.format(change)

	#print(f'Stock: {stock}\n  Price: {price}\n  Open: {Open}\n  Close: {close}\n  High: {high}\n  Low: {low}\n')

	#Store this stock information in a security object
	tempSec = Security(stockName, price, Open, high, low, close, netChange)
	securitiesList.append(tempSec)

#Get price information for every stock in our watchlist
def retrieveBatchStockInfo(securitiesList, batchList):

	"""
	Pulling all OHLC information for our entire stock watch list in one request.
	Returns a json blob (example below) with the main key being each stock in our watch list.
	Minor keys being the ohlc information (open, close, high, and low)
	
	{'AAPL': {'open': {'price': 169.55, 'time': 1550586600765}, 'close': {'price': 170.93, 'time': 1550610000472}, 'high': 171.44, 'low': 169.49}, 'AMZN': {'open': {'price': 1602, 'time': 1550586601038}, 'close': {'price': 1627.58, 'time': 1550610000375}, 'high': 1634, 'low': 1600.56}
	"""
	batch = Stock(batchList)
	priceInfo = batch.get_price()
	ohlcInfo = batch.get_ohlc()

	for stock in batchList:

		#Storing all information from each stock's json info
		price = priceInfo[stock]
		Open = ohlcInfo[stock]['open']['price']
		close = ohlcInfo[stock]['close']['price']
		high = ohlcInfo[stock]['high']
		low = ohlcInfo[stock]['low']

		#Calculate net stock change
		change = close - Open
		netChange = '{:+.2f}'.format(change)

		#print(f'Stock: {stock}\n  Price: {price}\n  Open: {Open}\n  Close: {close}\n  High: {high}\n  Low: {low}\n')

		#Store this stock information in a security object
		tempSec = Security(stock, price, Open, high, low, close, netChange)
		securitiesList.append(tempSec)

#Get user input for supplemental stock information if necessary
def getAdditionalStockInfo(securitiesList):

	keepAsking = True
	tempStockList = []

	while keepAsking:
		ask = input("Would you like to look at additional stocks? (y/n) ")

		if ask not in ['y', 'n']:
			print("Please enter a valid option.")
		else:
			if ask == 'n':
				keepAsking = False
			elif ask == 'y':
				getStock = input("Enter the stock: ")

				#Just testing to see if the stock is a valid index in the iex db
				try:
					test = Stock(getStock).get_price()
				except Exception as e:
					print("Error retrieving that stock information.")
					continue

				tempStockList.append(getStock.upper())
				print(tempStockList)

	if len(tempStockList) > 1:
		retrieveBatchStockInfo(securitiesList, tempStockList)
	else:
		retrieveSingleStockInfo(securitiesList, *tempStockList)
				

def main(securitiesList):

	#Initial watchlist stock information is stored.
	retrieveBatchStockInfo(securitiesList, watchList)

	#Get additional stock information if necessary.
	getAdditionalStockInfo(securitiesList)

if __name__ == '__main__':

	#List to hold all security objects
	securitiesList = []

	main(securitiesList)

	for i in range(len(securitiesList)):
		print(securitiesList[i])
