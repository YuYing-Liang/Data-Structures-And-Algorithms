from stackLib import *

def bc(string):
	#0th element = True or False
	#1st element = pos where bracket fails
	stack = stackLib([])
	popped = ''
	r_val = [True, -1] #if true, element 1 will return -1

	for i in range(0, len(string), 1):
		if string[i] == '(' or string[i] == '[' or string[i] == '{':
			stack.push(string[i])
		elif string[i] == ')':
			popped = stack.pop()
			if popped != '(':
				r_val = [False, i]			
		elif string[i] == ']':
			popped = stack.pop()
			if popped != '[':
				r_val = [False, i]
		elif string[i] == '}':
			popped = stack.pop()
			if popped != '{':
				r_val = [False, i]

	if stack.getValues() != []:
		 r_val = [False, len(string) - 1]

	return r_val


