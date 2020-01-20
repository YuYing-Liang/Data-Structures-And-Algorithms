from queue import *
import tree

class binary_tree:
	def __init__(self, val):
		self.store = [val,[],[]]

	def AddLeft(self, val):
		self.store[1] += [val]
		return True

	def AddRight(self, val):
		self.store[2] += [val]
		return True

	def Get_LevelOrder(self):
		q = queue([])
		returnList = []

		if self.store == []:
			return False

		q.push(self.store)

		while q.getLength() > 0:
			currNode = q.getValues()[0]
			if type(currNode[0]) != int:
				currNode = currNode[0].store
	
			if len(currNode) > 1:
				if currNode[1] != []:
					if type(currNode[1][0]) == int:
						q.push(currNode[1])
					else:
						q.push(currNode[1][0].store)
				if currNode[2] != []:
					if type(currNode[2][0]) == int:
						q.push(currNode[2])
					else:
						q.push(currNode[2][0].store)

			val = q.shift()
			returnList += [val[0]]

		return returnList
	
	def ConvertToTree_Helper(self, root):
		genTree = tree.tree(root.store[0])
		gen_children = []
		b_children = []
		child_node = root.store[1][0]
		
		while True:			
			gen_children += [tree.tree(child_node.store[0])]
			b_children += [child_node]
			if child_node.store[2] != []:
				child_node = child_node.store[2][0]
			else:
				break
		
		for i in range(len(b_children)):
			if b_children[i].store[1] != []:
				gen_children[i] = self.ConvertToTree_Helper(b_children[i])
			genTree.AddSuccessor(gen_children[i])

		return genTree
	
	def ConvertToTree(self):
		if self.store[2] != []:
			return [False, None]
		if self.store[0] == []:
			return [False, None]
		if self.store[1] == []:
			return [True, self]

		return [True, self.ConvertToTree_Helper(self)]
