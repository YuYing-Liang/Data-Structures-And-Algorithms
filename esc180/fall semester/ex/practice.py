import random

class conway:
	def __init__(self, numLists, numIntegers, strInts):
		self.numLists = numLists
		self.numIntegers = numIntegers
		self.strInts = strInts
		self.content = []
		if self.strInts == "zero":
			#set all numIntegers in numLists of lists to 0
		elif self.strInts == "random":
			#set all numIntegers in numLists of lists to ran fnc

	def getDisp(self):
		des = ""
		for l in self.content:
			data = l
			for i in data:
				if i == 0:
					des += " "
				else:
					des += "*"
			des += "\n"
		return des

	def printDisp(self):
		print self.getDisp()
		return True
		
	def setPos(self, row, col, val):
		if type(val) == int:
			if val == 0 or val == 1:
				self.contents[row][col] = val
				return True
			else:
				return False
		else:
			return False

	def getNeighbours(self, row, col):
		
