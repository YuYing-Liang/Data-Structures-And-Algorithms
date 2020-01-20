#Assignent One: Tic Tac Toe
#Creator: YuYing Liang, EngSci 2T2
#Date Submitted: September 21, 2018

#Note:	0 -- unoccupied position
#	1 -- X occipied position
#	2 -- O occupied position


#unoccupied board
def genBoard():
	count = 9
	board = []
	for i in range(0, count, 1):
		board += [0]

	return board


#Remember: if position is unoccupied, display board position 
def printBoard(T):
	board = ""
	#check errors
	if not(type(T) is list):
		return -1

	if len(T) != 9:
		return False
	
	for index in range(0, len(T), 1):
		if T[index] == 0:
			board += " " + str(index) + " "	
		elif T[index] == 1:
			board += " X "
		elif T[index] == 2:
			board += " O "
		else:
			return False
		
		if index == 2 or index == 5:	
			print(board)
			print("---|---|---")
			board = ""
		elif index != len(T) - 1:
			board += "|"
		else:
			print(board)
	return True	
 
#analyzing gameplay
#	0 -- board is in play
#	1 -- X won
#	2 -- O won
#	3 -- draw
#	-1 - error
def analyzeBoard(T):
	#assuming draw is default, if other situations occur, status will change
	winner = 3
	winningSet = []

	#check for errors

	if not(type(T) is list):
		return -1

	if len(T) != 9:
		return -1
	
        #checking for right number of Xs and Os
	numX = 0
	numO = 0

	for i in T:
		if not(i == 0 or i == 1 or i == 2):
			return -1	
		elif i == 0:
			#draw cannot occur, default is now set to board in play
			winner = 0
		if i == 1:
			numX += 1
		elif i == 2:
			numO += 1

	if not(numX == numO or numX == numO + 1 or numX + 1 == numO):
		return -1
					
	#check rows and columns
	numRowsAndCols = len(T)//3

	for i in range(0, numRowsAndCols, 1):
		if T[i] != 0:
			#checking rows
			if T[i] == T[i + 1] and T[i] == T[i + 2]:
				if winner == 0 or winner == 3:
					winner = T[i]					
					winningSet = [i, i + 1, i + 2]
				else:
					if winner == T[i]:
						otherSet = [i, i + 1, i + 2]
						if (winningSet[0] + 6 == otherSet[0] and winningSet[1] + 6 == otherSet[1]) or (winningSet[0] + 3 == otherSet[0] or winningSet[1] + 3 == otherSet[1]):
							return -1
					else:
						return -1
			#checking columns
			if T[i] == T[i + 3] and T[i] == T[i + 6]:
				if winner == 0 or winner == 3:
					winner = T[i]
					winningSet = [i, i + 3, i + 6]
				else:
					if winner == T[i]:
						otherSet = [i, i + 3, i + 6]
						if(winningSet[0] + 1  == otherSet[0] and winningSet[1] + 1 == otherSet[1]) or (winningSet[0] + 2 == otherSet[0] and winningSet[1] + 2 == otherSet[1]):
							return -1
					else:
						return -1


	#checking for diagonals
	if T[4] != 0:
		if T[0] == T[4] and T[0] == T[8]:
			if winner == 0 or winner == 3:	           
				winner = T[0]
			else:
				if winner != T[i]:
					return -1
				
		if T[2] == T[4] and T[2] == T[6]:
			if winner == 0 or winner == 3:
				winner = T[2]
			else:
				if winner != T[i]:
					return -1
	return winner

