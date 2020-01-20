from chessPlayer_helper import *
from chessPlayer_tree import *


def chessPlayer(board, player):

    try:

        opp = 10
        if player//10 == 1:
            opp = 20

        status = True      # function success

        if isKingAlive(board):
            r_list = genTree(board, player, opp, [])
            sub_trees = r_list[0]
            candidateMoves = r_list[1]      # candidate[i][0] = 2-item move list candidate[i][1] = float -> how good the move is
            root = tree(board)              # placeholder for now

            for i in sub_trees:
                root.AddSuccessor(i)

            index = 0
            minimax(root, 0, True, -10000000000, 10000000000)
            bestScore = 0

            for i in range(len(candidateMoves)):
                candidateMoves[i][1] = float(root.getChildren()[i].score)
                if bestScore <= candidateMoves[i][1]:
                    bestScore = candidateMoves[i][1]
                    index = i

            print(index)
            move = candidateMoves[index][0]     # 2-item list where
            #                                   # move[0] is the current location of the piece and
            #                                   # move[1] is the desired location

            # evalTree = root.Get_LevelOrder()
            evalTree = [root.getVal()] + r_list[2]  # level order traversal of tree being used

            return [status, move, candidateMoves, evalTree]
        else:
            return [False, None, None, None]
    except:

        return [False, None, None, None]


def isKingAlive(board):
    whiteKing = False
    blackKing = False

    for i in board:
        if i == 15:
            whiteKing = True
        elif i == 25:
            blackKing = True

    return whiteKing and blackKing


def genTree(board, player, opp, can_moves):
    levelOrder = []
    possible_moves_trees = []
    possible_moves = []     # in format [[curr_pos, [possible_pos]] .... ]
    inCheckMoves = []

    # player move
    player_pos = GetPlayerPositions(board, player)
    for i in player_pos:
        indiv_moves = GetPieceLegalMoves(board, i)
        possible_moves += [[i, indiv_moves]]

    for i in possible_moves:
        # make different boards
        curr = i[0]
        if i[1] != []:
            for j in i[1]:
                nxt = j
                newBoard = list(board)
                newBoard[nxt] = newBoard[curr]
                newBoard[curr] = 0
                child = tree(newBoard)
                if IsInCheck(board, player):
                    king_pos = 0
                    for q in range(len(board)):
                        if board[q]//10 == player and board[q]%10 == 5:
                            king_pos = q

                    t_index = PieceThreatening(board, king_pos, player)

                    if nxt == t_index:
                        child.score = 10000

                if IsInCheck(newBoard, player):
                    inCheckMoves += [len(possible_moves_trees)]
                    child.score = -10000
                else:
                    child.score += evalFunction(newBoard, board, nxt, player, opp)

                can_moves += [[[curr, nxt], 0]]
                possible_moves_trees += [child]
                levelOrder += [child.getVal()]

    # opponent move
    index = 0
    inCheckIndex = 0
    inCheckMoves += [len(possible_moves_trees)]
    repeatedMoves = []

    for x in possible_moves_trees:
        if index != inCheckMoves[inCheckIndex]:
            nextBoard = list(x.getVal())
            opp_pos = GetPlayerPositions(nextBoard, opp)
            possible_moves = []

            for i in opp_pos:
                indiv_moves = GetPieceLegalMoves(nextBoard, i)
                possible_moves += [[i, indiv_moves]]

            isRepeated = False
            for i in repeatedMoves:
                if possible_moves == i:
                    isRepeated = True

            if not isRepeated:
                # print(possible_moves)
                for i in possible_moves:
                    # make different boards
                    curr = i[0]
                    if i[1] != []:
                        for j in i[1]:
                            nxt = j
                            newBoard = list(nextBoard)
                            newBoard[nxt] = newBoard[curr]
                            newBoard[curr] = 0
                            child = tree(newBoard)
                            #if kills king
                            if nextBoard[nxt]//10 == player//10 and nextBoard[nxt] % 10 == 5:
                                child.score = -10000

                            x.AddSuccessor(child)

                            levelOrder += [child.getVal()]
                repeatedMoves += [possible_moves]


        else:
            inCheckIndex += 1
        index += 1


    # player move (again)
    repeatedMoves = []

    for x in possible_moves_trees:
        # print("hello")
        children = x.getChildren()
        for q in children:
            nextBoard = list(q.getVal())
            player_pos = GetPlayerPositions(nextBoard, player)
            possible_moves = []

            for i in player_pos:
                indiv_moves = GetPieceLegalMoves(nextBoard, i)
                possible_moves += [[i, indiv_moves]]

                safe_move = []
                for j in indiv_moves:
                    if not (IsPositionUnderThreat(board, j, player)):
                        safe_move += [j]
                if safe_move != []:
                    possible_moves += [[i, safe_move]]

            isRepeated = False
            for i in repeatedMoves:
                if possible_moves == i:
                    isRepeated = True

            if not isRepeated:
                for i in possible_moves:
                    # make different boards
                    curr = i[0]
                    if i[1] != []:
                        for j in i[1]:
                            nxt = j
                            newBoard = list(nextBoard)
                            newBoard[nxt] = newBoard[curr]
                            newBoard[curr] = 0
                            child = tree(newBoard)
                            if IsInCheck(newBoard, player):
                                child.score = -10000
                            else:
                                child.score += evalFunction(newBoard, nextBoard, nxt, player, opp)

                            q.AddSuccessor(child)
                            levelOrder += [child.getVal()]
                repeatedMoves += [possible_moves]

    return [possible_moves_trees, can_moves, levelOrder]


def minimax(node, depth, isMaxPlayer, alpha, beta):
    if node.getChildren() == []:
        return node.score

    if isMaxPlayer:
        bestVal = -10000000000
        children = list(node.getChildren())
        for i in range(len(children)):
            value = minimax(children[i], depth+1, False, alpha, beta)
            bestVal = max(value, bestVal)
            alpha = max(alpha, bestVal)

            if value >= alpha:
                node.score += alpha

            if beta <= alpha:
                break
        return bestVal
    else:
        bestVal = 10000000000
        children = list(node.getChildren())
        for i in range(len(children)):
            value = minimax(children[i], depth + 1, True, alpha, beta)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)

            if value <= beta:
                node.score += beta

            if beta <= alpha:
                break
        return bestVal


def get_pos_factor(piece):
    player = piece // 10
    piece = piece % 10

    if piece == 0:
        pawnEvalBlack = [
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
            1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
            0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
            0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
            0.0, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.0,
            0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        ]
        if player == 2:
            return pawnEvalBlack
        else:
            return reverse(pawnEvalBlack)

    elif piece == 1:
        return [
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
            -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
            -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
            -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
            -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,
            -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,
            -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
            -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0
        ]

    elif piece == 2:
        bishopEvalBlack = [
            -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
            -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
            -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
            -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
            -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
            -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
            -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
            -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0
        ]
        if player == 2:
            return bishopEvalBlack
        else:
            return reverse(bishopEvalBlack)
    elif piece == 3:
        rookEvalBlack = [
            0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
            0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
            0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0
        ]
        if player == 2:
            return rookEvalBlack
        else:
            return reverse(rookEvalBlack)
    elif piece == 4:
        return [
            -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
            -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
            -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
            -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
            0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
            -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
            -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
            -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0
        ]

    elif piece == 5:
        kingEvalBlack = [
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
            -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
            -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
            -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
            2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
            2.0, 3.0, 3.0, 1.0, 1.0, 3.0, 3.0, 2.0
        ]
        if player == 2:
            return kingEvalBlack
        else:
            return reverse(kingEvalBlack)


def reverse(array):
    newList = []
    for i in range(len(array) - 1, -1, -1):
        newList += [array[i]]

    return newList


def evalFunction(newBoard, nextBoard, nxt, player, opp):
    score = 0
    factor = 50
    opp = opp//10

    piece_score = getPieceScore(newBoard[nxt], player)
    pos_factor = get_pos_factor(newBoard[nxt])
    piece = PieceThreatening(newBoard, nxt, player)

    if piece >= 0:
        score += getPieceScore(newBoard[piece], player)

    if nextBoard[nxt] // 10 == opp:
        score += getPieceScore(nextBoard[nxt], player) * ((factor * 2)//piece_score)

    score += factor * (score//(abs(score) + 0.0001))

    score *= movability(newBoard, nxt)

    return score


def movability(board, pos):
    if board[pos] % 10 == 3:
        r_list = GetRookMoves(pos, board)
        return (len(r_list))//8
    elif board[pos] % 10 == 2:
        r_list = GetBishopMoves(pos, board)
        return (len(r_list))//8
    else:
        return 1
