# Calculating the factorial of a given number
def factorial(num):
	factorial = 1
	while num > 0:
		factorial *= num
		num -= 1
	return factorial
