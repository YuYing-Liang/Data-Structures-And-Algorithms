def fibo(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

def fiboL(n):
	if n == 0:
		return [1]
	else:
		return [fibo(n)] + fiboL(n - 1)

def redfibo(n):
	if n < 0:
		return -1
	else:
		listFibo = fiboL(n)
		return reduce(reducingProduct, listFibo)	


def reduce(fnc, argList):
	if len(argList) == 1:
		return argList[0]
	elif len(argList) == 2:
		return fnc(argList[0], argList[1])
	else:
		return fnc(argList[0], reduce(fnc, argList[1:len(argList) - 1]))

def reducingProduct(a,b):
	return a * b
	

