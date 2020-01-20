# Calculating the product between two integers
def mult(x,y):
	sum = 0
	while y > 0:
		sum += x
		y -= 1
	return sum


