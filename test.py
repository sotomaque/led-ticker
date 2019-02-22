from iex import Stock


watchList = ['AAPL']




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
		percentChange = float(self.dayChange) / float(self.open) * 100
		percentChange = '{:+.3f}'.format(percentChange)
		return(str(self.name) + '\n last price: ' + str(self.price) + '\n open: ' + str(self.open) + '\n high: ' + str(self.high) + '\n low: ' + str(self.low) + '\n close: '+ str(self.closee) + '\n net change: ' + str(self.dayChange) + '; ' + str(percentChange) + '%')

def watchlistQuotes(watchList):
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
		#get high 
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

def getQuotes():
	
	x = input('If you would like additional quotes, enter a symbol at any time: ')
	x = x.upper()
	#get price
	price = Stock(x).price()
	#get open
	ohlc = Stock(x).ohlc()
	openn = ohlc['open']['price']
	#get high 
	high = ohlc['high']
	#get low
	low = ohlc['low']
	#get close
	closee = ohlc['close']['price']
	#calculate net change
	change = closee - openn
	netChange = '{:+.2f}'.format(change)

	#set 
	y = security(str(x), price, openn, high, low, closee, netChange)
	print('\n')
	print(y)


def main():
	watchlistQuotes(watchList)
	print('\n')
	getQuotes()
	

if __name__ == '__main__':
	main()