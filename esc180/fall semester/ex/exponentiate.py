# Calculating the power of a given base and a given exponent
def exponentiate(b,e):
	power = 1
	while e > 0 :
		power *= b
		e -= 1
	return power 
