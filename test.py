from iex import Stock


watchList = ['AAPL', 'AMZN', 'ACB', 'AMD', 'CRON', 'CVX', 'CSCO', 'IBM', 'KO', 'MJ', 'MRK', 'MSFT', 'PFE', 'PG', 'QCOM', 'ROKU', 'SO', 'SQ', 'TWTR', 'TLRY', 'TSLA', 'VZ', 'XOM']


class sec:
	def __init__(self, name, price, openn, high, low, closee, dayChange):
		self.name = name
		self.price = price
		self.open = openn
		self.high = high
		self.low = low
		self.closee = closee
		self.dayChange = dayChange


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
	i = sec(str(i), price, openn, high, low, closee, netChange)
	
	print('stock: {} price: {} open: {} high: {} low: {} close: {} net change for the day: {}'.format(i.name, i.price, i.open, i.high, i.low, i.closee, i.dayChange))
	print('\n')


