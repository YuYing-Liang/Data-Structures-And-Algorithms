#This weeks lesson: recursion

#excercise 1: exponentiation recursively
def exponentiate(b,p):
	if p == 0:
		return 1
	elif p == 1:
		return b
	elif p == -1:
		return 1/b
	elif p < 0:
		return (1/b) * exponentiate(b, p+1)
	else:
		return b * exponentiate(b, p-1)

#ex1 test code:
print(str(exponentiate(4,2)))
print(str(exponentiate(2, -3)))

#excercise 2: write a recursive function to sum the elements of a numeric list
def sum(nums):
	newlist = list(nums)
	if len(newlist) == 0:
		return 0
	elif len(newlist) == 1:
		return newlist[0]
	else:
		return newlist[0] + sum(newlist[1:len(newlist)])

#ex2 test code:
numList = [1,2,3,4,5,6,7,8,9,10]
numList2 = [-1,3,-4,6,-8,5,9]
print(sum(numList))	#sum = 55
print(sum(numList2))	#sum = 10 
	
#excercise 3: express the fibonacci number n in python
def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	elif n < 0:
		return -1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

#ex3 test code
print(fibonacci(5))
print(fibonacci(2))
print(fibonacci(-5))

#excercise 4: function to generate the first N fibonacci numbers
def genfib(n): #nums is an empty list
	if n == 0:
		return [fibonacci(0)]
	else:
		return [fibonacci(n)] + genfib(n-1)
		
#ex4 test code
emptylist = []
print(genfib(5))

#excercise 5: function to generate the nth line of pascal's triangle
def pascalTriangle(n):
	if n < 0:
		return -1
	if n == 0:
		return [1]
	else:
		return [1] + compress(pascalTriangle(n - 1)) + [1]

#function to compress previous line in pascal's triangle
def compress(l):
	accum = []
	for i in range(0, len(l) - 2, 1):
		accum += [l[i] + l[i + 1]]
	return accum

#ex4 test code
print(pascalTriangle(10))

