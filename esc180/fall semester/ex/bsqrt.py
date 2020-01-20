# calculating babylonian square roots
# square root function
def bsqrt(square, accuracy):
	if square > 0 :
		estimate = square / 2
		diff = square - estimate * estimate
		if diff > accuracy:
			estimate = (estimate + (square/estimate)/2)
			return estimate
		else:
			return 0
	else:
		return -1
	
