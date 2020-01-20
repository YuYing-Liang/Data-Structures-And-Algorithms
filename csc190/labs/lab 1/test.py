import tree
import binary_tree

#convert to binary tree

print("General Trees")

x=tree.tree(1)
y=tree.tree(2)
z=tree.tree(3)
a=tree.tree(4)
b=tree.tree(5)
c=tree.tree(6)
x.AddSuccessor(y)
x.AddSuccessor(z)
x.AddSuccessor(a)
y.AddSuccessor(b)
y.AddSuccessor(c)

print(x.Get_LevelOrder())
b = x.ConvertToBinaryTree()
print("Equivalent Binary Tree")
print(b.Get_LevelOrder())
print("Testing ...")
g = b.ConvertToTree()
if g[0]:
	print(g[1].Get_LevelOrder())

#convert to general tree
'''
Tree:		1
	2		3
		    4	    5
'''

print("Binary Trees")
x=binary_tree.binary_tree(1)
a=binary_tree.binary_tree(2)
x.AddLeft(a)
y=binary_tree.binary_tree(3)
y.AddLeft(binary_tree.binary_tree(4))
y.AddRight(binary_tree.binary_tree(5))
x.AddRight(y)
print("Tree Zero:")
print(x.Get_LevelOrder())
t = x.ConvertToTree()
if t[0]:
	print(t[1].Get_LevelOrder())
else:
	print("Cannot Convert")
'''
Tree:			1
		2
	   5	     3
	      6		4
'''

a = binary_tree.binary_tree(1)
b = binary_tree.binary_tree(2)
c = binary_tree.binary_tree(3)
d = binary_tree.binary_tree(4)
e = binary_tree.binary_tree(5)
f = binary_tree.binary_tree(6)
a.AddLeft(b)
b.AddLeft(e)
b.AddRight(c)
e.AddRight(f)
c.AddRight(d)
print("Tree One:")
print(a.Get_LevelOrder())
t2 = a.ConvertToTree()
if t2[0]:
	print("Equivalent General Tree:")
	print((t2[1]).Get_LevelOrder())
#adding more nodes
g = binary_tree.binary_tree(7)
h = binary_tree.binary_tree(8)
i = binary_tree.binary_tree(9)
j = binary_tree.binary_tree(10)
e.AddLeft(g)
g.AddLeft(j)
g.AddRight(h)
h.AddRight(i)
print("Tree Two:")
print(a.Get_LevelOrder())
t3 = a.ConvertToTree()
if t3[0]:
	print("Equivalent General Tree:")
	print(t3[1].Get_LevelOrder())
