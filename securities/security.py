class Security:

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
		return(str(self.name) + '\n  last price: ' + str(self.price) + '\n  open: ' + str(self.open) + '\n  high: ' + str(self.high) + '\n  low: ' + str(self.low) + '\n  close: '+ str(self.closee) + '\n  net change: ' + str(self.dayChange) + '\n  percent change: ' + str(percentChange) + '%\n')