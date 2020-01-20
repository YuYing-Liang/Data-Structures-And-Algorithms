from counterlib import *

def main():
	myCnt = counter(100)
	x = counter(75)
	y = counter(25)
	
	for i in range(0,10,1):
		myCnt.evolve(3+i)
		x.evolve(3)
		y.evolve(i)
		print(str(x.getState()) + " " + str(y.getState()) + " " + str(myCnt.getState()))
	return True

main()
