class counter:
	def __init__(self,initCnt):
		self.cnt = initCnt

	def evolve(self, x):
		self.cnt += x
		return True

	def getState(self):
		return self.cnt
