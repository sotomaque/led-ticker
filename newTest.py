"""
New version working with iexfinance v0.4.0
"""

from iexfinance.stocks import Stock


watchList = ['AAPL', 'AMZN', 'ACB', 'AMD', 'CRON', 'CVX', 'CSCO', 'IBM', 'KO', 'MJ', 'MRK', 'MSFT', 'PFE', 'PG', 'QCOM', 'ROKU', 'SO', 'SQ', 'TWTR', 'TLRY', 'TSLA', 'VZ', 'XOM']


class security:

	def __init__(self, name, price, openn, high, low, closee, dayChange):
		self.name = name
		self.price = price
		self.open = openn
		self.high = high
		self.low = low
		self.closee = closee
		self.dayChange = dayChange

	def __str__(self):
		return(str(self.name) + ' last price: ' + str(self.price) + ' open: ' + str(self.open) + ' high: ' + str(self.high) + ' low: ' + str(self.low) + ' close: '+ str(self.closee) + ' net change: ' + str(self.dayChange))


def main():

	#List to hold all security objects
	securitiesList = []
	
	"""
	Pulling all OHLC information for our entire stock watch list in one request.
	Returns a json blob (example below) with the main key being each stock in our watch list.
	Minor keys being the ohlc information (open, close, high, and low)
	
	{'AAPL': {'open': {'price': 169.55, 'time': 1550586600765}, 'close': {'price': 170.93, 'time': 1550610000472}, 'high': 171.44, 'low': 169.49}, 'AMZN': {'open': {'price': 1602, 'time': 1550586601038}, 'close': {'price': 1627.58, 'time': 1550610000375}, 'high': 1634, 'low': 1600.56}
	"""
	batch = Stock(watchList)
	priceInfo = batch.get_price()
	ohlcInfo = batch.get_ohlc()

	for stock in watchList:

		#Storing all information from each stock's json info
		price = priceInfo[stock]
		Open = ohlcInfo[stock]['open']['price']
		close = ohlcInfo[stock]['close']['price']
		high = ohlcInfo[stock]['high']
		low = ohlcInfo[stock]['low']

		#Calculate net change
		change = close - Open
		netChange = '{:+.2f}'.format(change)

		#print(f'Stock: {stock}\n  Price: {price}\n  Open: {Open}\n  Close: {close}\n  High: {high}\n  Low: {low}\n')

		#Store this stock information in a security object
		tempSec = security(stock, price, Open, high, low, close, netChange)
		securitiesList.append(tempSec)

	for i in range(len(securitiesList)):
		print(securitiesList[i])

if __name__ == '__main__':
	main()
