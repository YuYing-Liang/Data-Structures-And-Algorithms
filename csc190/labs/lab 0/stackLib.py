#Stack Library
class stackLib:
	def __init__(self, data):
		if type(data) == list:
			self.values = data #assumes data is a list
		else:
			self.values = []

	def push(self, val):
		#add to head
		self.values = [val] + self.values
		return 0

	def pop(self):
		#take from head
		x = self.values[0]
		self.values = self.values[1:len(self.values)]
		return x

	def getValues(self):
		return self.values
