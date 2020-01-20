class seqdetector:
	#initialize
	def __init__(self):
		self.val = ""
		self.matchSequence="herearethesolutionstothenextexam"

	#returns True -- if detected and False if not
	def evolve(self, word):
		self.val += word

		lenSelfVal = len(self.val)
		if lenSelfVal == len(self.matchSequence):
			if self.val == self.matchSequence:
				return True
			else:
				return False
			self.val = ""
		else:
			if self.val != self.matchSequence[0:lenSelfVal]:
				self.val = ""	
			return False
