L = range(1,10,1)

def square(x):
	return x*x

M = map(square,L)

def reducingSum(a,b):
	return a+b

def reduce(fnc, n):
	#wrong lol
	x = list(n)
	if len(x) == 1:
		return int(x[0])
	else:
		lastTerm = x[len(x) - 1]
		newX = map(reducingSum, x[0:len(x)-1], lastTerm)
		return reduce(fnc, newX)
	'''
	x = list(n)
	if len(x) == 1:
		return int(x)
	elif len(x) % 2 == 0:
		listOne = x[0:len(x)//2]
		listTwo = x[len(x)//2:len(x)]
		listTotal = map(fnc, listOne, listTwo)
		print(list(listTotal))	
		return reduce(fnc, listTotal)
	else:
		first = x[0]
		listOne = x[1:len(x)//2 + 1]
		listTwo = x[len(x)//2 + 1: len(x)]
		listTotal = map(fnc, listOne, listTwo)
		print(list(listTotal))
		return [first] +  reduce(fnc, listTotal)

	#doesn't work: return map(fnc,x)
	'''

msum = reduce(reducingSum, M)
print(msum)		
