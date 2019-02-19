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
		return(str(self.name) + ' last price: ' + str(self.price) + ' open: ' + str(self.open) + ' high: ' + str(self.high) + ' low: ' + str(self.low) + ' close: '+ str(self.closee) + ' net change: ' + str(self.dayChange))