from iex import Stock


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
	#init empty security objects
	for i in watchList:
		i = security(str(i), 0, 0, 0, 0, 0, 0)

	#init blank list of security objects
	stocks = []	

	#loop through watchlist
	for i in watchList:
		#get price
		price = Stock(i).price()
		#get open
		ohlc = Stock(i).ohlc()
		openn = ohlc['open']['price']
		#get high 🚀
		high = ohlc['high']
		#get low
		low = ohlc['low']
		#get close
		closee = ohlc['close']['price']
		#calculate net change
		change = closee - openn
		netChange = '{:+.2f}'.format(change)
		
		#set 
		i = security(str(i), price, openn, high, low, closee, netChange)
		stocks.append(i)
	
	#loop though list of security object
	for i in range(0,len(stocks)):
		print(stocks[i - 1])

main()