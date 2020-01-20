from queue import *
import binary_tree

class tree:
	def __init__(self, x):
		self.store = [x,[]]
	
	def AddSuccessor(self,x):
		self.store[1] += [x]
		return True

	def Print_DepthFirst(self):
		#same as traversal but with a stack
		return True
	
	def Get_LevelOrder(self):
		q = queue([])
		returnList = []

		if self.store == []:
			return False

		q.push(self.store)

		while q.getLength() > 0:
			currNode = q.getValues()[0]			
			for i in range(len(currNode[1])):
				if currNode[1][i].store != []:
					q.push(currNode[1][i].store)
			val = q.shift()
			returnList += [val[0]]

		return returnList
		 

	def ConvertToBinaryTree(self):
		return self.Recursive_Turn_To_Binary(self)

	def Recursive_Turn_To_Binary(self, root):
		b_tree = binary_tree.binary_tree(root.store[0])
		children = []
					
		if root.store[1] != []:
			for i in range(len(root.store[1])):
				children += [binary_tree.binary_tree(root.store[1][i].store[0])]

			for i in range(len(children)-1):
				if root.store[1][i].store[1] != []:			
					children[i] = self.Recursive_Turn_To_Binary(root.store[1][i])
				children[i].AddRight(children[i+1])
			
			b_tree.AddLeft(children[0])
					
		return b_tree


