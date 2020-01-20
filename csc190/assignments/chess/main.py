# import helper functions
from chessPlayer_helper import *
from random import *
from chessPlayer import *

def main():
    # initialize state of the board
    board = genBoard()

    done = False
    while not done:
        print(printIndicies())
        print(printBoard(board))
        white_move = input("\nWhite Player Turn, Enter a move in format (current index, desired index):\n").split(",")
        is_legal = False

        # legal move?
        while not is_legal:
            curr = int(white_move[0])
            nxt = int(white_move[1])
            legal_moves = GetPieceLegalMoves(board, curr)
            for i in legal_moves:
                if i == nxt:
                    is_legal = True
                    board[nxt] = board[curr]
                    board[curr] = 0
                    break
            if is_legal:
                break
            else:
                white_move = input("\nillegal move, please enter another move in the same format\n").split(",")

        print(printIndicies())
        print(printBoard(board))
        black_move = input("\nBlack Player Turn, Enter a move in format (current index, desired index):\n").split(",")
        is_legal = False

        # legal move?
        while not is_legal:
            curr = int(black_move[0])
            nxt = int(black_move[1])
            legal_moves = GetPieceLegalMoves(board, curr)
            for i in legal_moves:
                if i == nxt:
                    is_legal = True
                    board[nxt] = board[curr]
                    board[curr] = 0
                    break
            if is_legal:
                break
            else:
                black_move = input("\nillegal move, please enter another move in the same format\n").split(",")


def main2():
    white = 10
    # black = 20
    # initialize state of the board
    board = genBoard()

    done = False
    while not done:
        # find white move
        possible_moves = []     # in format [[curr_pos, [possible_pos]] .... ]
        wplayer_pos = GetPlayerPositions(board, white)
        # print(wplayer_pos)
        for i in wplayer_pos:
            indiv_moves = GetPieceLegalMoves(board, i)
            # print("moves:")
            # print(indiv_moves)
            safe_move = []
            for j in indiv_moves:
                if not (IsPositionUnderThreat(board, j, white)):
                    safe_move += [j]
            if safe_move != []:
                possible_moves += [[i, safe_move]]
        print(possible_moves)

        # choose move
        piece_to_move = randint(0, len(possible_moves) - 1)
        pos_to_go = randint(0, len(possible_moves[piece_to_move][1]) - 1)
        curr = possible_moves[piece_to_move][0]
        nxt = possible_moves[piece_to_move][1][pos_to_go]
        board[nxt] = board[curr]
        board[curr] = 0

        print(printBoard(board))
        black_move = input("\nBlack Player Turn, Enter a move in format (current index, desired index):\n").split(",")
        is_legal = False

        # legal move?
        while not is_legal:
            curr = int(black_move[0])
            nxt = int(black_move[1])
            legal_moves = GetPieceLegalMoves(board, curr)
            for i in legal_moves:
                if i == nxt:
                    is_legal = True
                    board[nxt] = board[curr]
                    board[curr] = 0
                    break
            if is_legal:
                break
            else:
                black_move = input("illegal move, please enter another move in the same format\n").split(",")


def main3():
    white = 10
    black = 20
    # initialize state of the board
    board = genBoard()

    done = False
    while not done:
        print(printBoard(board))

        # find white move
        # [status, move, candidate moves, eval tree]
        r_list = chessPlayer(board, white)
        print(r_list[0])
        
        if not r_list[0]:
            if not isKingAlive(board):
                print("game ended")
                print("Black wins")
            break

        print("white moves:")
        print(r_list[2])
        #for i in r_list[3]:
            #print(printBoard(i))


        curr = r_list[1][0]
        nxt = r_list[1][1]
        board[nxt] = board[curr]
        board[curr] = 0

        print(printBoard(board))
        r_list = chessPlayer(board, black)

        if not r_list[0]:
            if not isKingAlive(board):
                print("game ended")
                print("White wins")
            break

        print("black moves:")
        print(r_list[2])
        # print(r_list[3])

        curr = r_list[1][0]
        nxt = r_list[1][1]
        board[nxt] = board[curr]
        board[curr] = 0


main3()
