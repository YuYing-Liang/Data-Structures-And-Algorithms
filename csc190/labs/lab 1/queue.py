class queue:
	def __init__(self, data):
		if type(data) == list:
			self.values = data #assumes data is a list
		else:
			self.values = []

	def push(self, val):
		#add to tail
		self.values += [val]
		return True

	def shift(self):
		#take from head
		x = self.values[0]
		self.values = self.values[1:len(self.values)]
		return x

	def getValues(self):
		return self.values

	def getLength(self):
		return len(self.values)
