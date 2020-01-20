from tttlib import *

T = genBoard()
'''
B = [-5,1,1,298347,2,2,1,1,1]

state = analyzeBoard(B)
if state == 1:
	print("X won!")
elif state == 2:
	print("O won!")
elif state == 3:
	print("Tie game!")
elif state == -1:
	print("error")

A = ["asdf",0,0,0,0,0,0,0,0]

state = analyzeBoard(A)
if state == 1:
        print("X won!")
elif state == 2:
        print("O won!")
elif state == 3:
        print("Tie game!")
elif state == -1:
        print("error")

'''

while printBoard(T):

	moveX = input("X move?")

	#checking if moveX is an integer
	try:
		if int(moveX) == -1:
			break;
		T[int(moveX)] = 1
	except ValueError:
		print("invalid move, to punish you, you miss a turn")
	
	state = analyzeBoard(T)

	if state == 1:
		printBoard(T)
		print("X won the game congratulations!")
		break
	elif state == 3:
		printBoard(T)
		print("Tie game!")
		break
	else:
		print("error")

	if printBoard(T):

		moveO = input("O move?")
	
		#checking if moveO is an integer
		try:
			if int(moveX) == -1:
				break
			T[int(moveO)] = 2
		except ValueError:
			print("invalid move, to punish you, you miss a turn")
	
		state = analyzeBoard(T)
	
		if state == 2:
			printBoard(T)
			print("O won the game congratulations!")	
			break
		elif state == 3:
			printBoard(T)
			print("Tie game!")
			break
		else:
			print("error")
	else:
		break
