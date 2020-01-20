#Assignent One: Tic Tac Toe
#Creator: YuYing Liang, EngSci 2T2
#Date Submitted: September 21, 2018

#Note:	0 -- unoccupied position
#	1 -- X occipied position
#	2 -- O occupied position

import random

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
	
	#print board
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
#	-1 - error	<-- never returns this, using website code
def analyzeBoard(t):	
	if t[0] == t[1] == t[2] != 0:
		return t[0]
	if t[3] == t[4] == t[5] != 0:
		return t[3]
	if t[6] == t[7] == t[8] != 0:
		return t[6]
	if t[0] == t[3] == t[6] != 0:
		return t[0]
	if t[1] == t[4] == t[7] != 0:
		return t[1]
	if t[2] == t[5] == t[8] != 0:
		return t[2]
	if t[0] == t[4] == t[8] != 0:
		return t[0]
	if t[2] == t[4] == t[6] != 0:
		return t[2]

	n_opens=0
	for i in t:
		if i==0:
	  		n_opens+=1
	if n_opens == 0:
		return 3
	else:
		return 0

#genNonLoser and genWinningMove are assuming there are no errors in T
def genNonLoser(T, player):
	#player - 1: X
	#	- 2: O

	if player != 1 and player != 2:
		return -1

	TBoard = list(T)
	opponent = 1

	if player == 1:
		opponent = 2
	
	length = 9

	for i in range(0, length, 1):
		if TBoard[i] == 0:
			TBoard[i] = opponent
			if analyzeBoard(TBoard) == opponent:
				return i
			else:
				TBoard = list(T)
	return -1

def genWinningMove(T, player):
	
	if player != 1 and player != 2:
		return -1

	TBoard = list(T)
	length = 9

	for i in range(0, length, 1):
		if TBoard[i] == 0:
			TBoard[i] = player
			if analyzeBoard(TBoard) == player:
				return i
			else:
				TBoard = list(T)
				
	return -1

def genRandomMove(T, player):
	if player != 1 and player != 2:
		return -1

	emptyLocations = []

	for i in range(0, len(T), 1):
		if T[i] == 0:
			emptyLocations += [i]

	if len(emptyLocations) == 0:
		return -1
	else:
		return emptyLocations[random.randint(0, len(emptyLocations) - 1)]

#genOpenMove tires to look for the best possible move for the player,
#it first checks if there are any winning moves, if not, it will check to block any of the opponent's 
#winning moves, if there are no winning moves it generates a random move
def genOpenMove(T, player):
	winningMove = genWinningMove(T, player)
	nonloser = genNonLoser(T, player)
	ran = genRandomMove(T, player)
	
	newTTTBoard = list(T)

	if winningMove != -1:
		return winningMove	
	elif nonloser != -1:
		return nonloser
	elif ran != -1:
		return ran
	else:
		return -1

		
