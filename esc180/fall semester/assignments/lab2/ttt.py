from tttlib import *

T = genBoard()

print("You are player X, your turn is first, if you enter an invalid turn position you will be penalized.")
printBoard(T)

#assuming value entered by x is an integer because we haven't learned try, catch yet
while True:
	
	Xmove = int(input("x move?"))
	
	if Xmove < 0 or Xmove > len(T) - 1:
		print("invalid position, your turn is lost.")
	elif T[Xmove] == 0:
		T[Xmove] = 1
		printBoard(T)
		print()

		state = analyzeBoard(T)

		if state == 1:
			print("X won!")
			break
		elif state == 2:
			print("O won!")
			break
		elif state == 3:
			print("Tie game!")
			break
		elif state == -1:
			print("error")
			break
	else:
		print("invalid position, your turn is lost")

	Omove = genOpenMove(T, 2)
	
	print("O Move:" + str(Omove))

	T[Omove] = 2

	printBoard(T)
	print()

	state = analyzeBoard(T)
	
	if state == 1:
		print("X won!")
		break
	elif state == 2:
		print("O won!")
		break
	elif state == 3:
		print("Tie game!")
		break
	elif state == -1:
		print("error")

	
	
	
		
