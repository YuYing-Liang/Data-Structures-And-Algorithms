
class tree:
        def __init__(self, x):
            self.store = [x, []]
            self.score = 0

        def AddSuccessor(self, x):
            self.store[1] += [x]
            return True

        def getVal(self):
            return self.store[0]

        def getChildren(self):
            return self.store[1]

