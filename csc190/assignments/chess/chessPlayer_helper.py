# player = 10: white
# player = 20: black


def getPiece(name):
    if name == "pawn":
        return 0
    elif name == "knight":
        return 1
    elif name == "bishop":
        return 2
    elif name == "rook":
        return 3
    elif name == "queen":
        return 4
    elif name == "king":
        return 5
    else:
        return -1


def genBoard():
    r = [0]*64
    white = 10
    black = 20
    for i in [white, black]:
        if i == white:
            factor =+ 1
            shift = 0
        else:
            factor =- 1
            shift = 63

        r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
        r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
        r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
        if i == white:
            r[shift+factor*4] = i+getPiece("queen")  # queen is on its own color square
            r[shift+factor*3] = i+getPiece("king")
        else:
            r[shift+factor*3] = i+getPiece("queen")  # queen is on its own color square
            r[shift+factor*4] = i+getPiece("king")

        for j in range(0, 8):
            r[shift+factor*(j+8)] = i+getPiece("pawn")

    return r


def printBoard(board):
    accum = "---- BLACK SIDE ----\n"
    max_num = 63
    for j in range(0, 8, 1):
        for i in range(max_num-j*8, max_num-j*8-8, -1):
            accum += '{0:<5}'.format(board[i])
        accum += "\n"
    accum += "---- WHITE SIDE ----"
    return accum


def GetPlayerPositions(board, player):
    player_pos = []
    player = player//10

    for i in range(len(board)):
        if board[i]//10 == player:
            player_pos += [i]
    return player_pos


def GetPieceLegalMoves(board, position):
    piece = board[position] % 10
    r_list = []

    if piece == 0:
        # pawn
        r_list = GetPawnMoves(position, board)
    elif piece == 1:
        # knight
        r_list = GetKnightMoves(position, board)
    elif piece == 2:
        # bishop
        r_list = GetBishopMoves(position, board)
    elif piece == 3:
        # rook
        r_list = GetRookMoves(position, board)
    elif piece == 4:
        # queen
        r_list = GetQueenMoves(position, board)
    elif piece == 5:
        # king
        r_list = GetKingMoves(position, board)
    return r_list


def GetPawnMoves(pos, board):
    r_list = []
    player = board[pos]
    opp = 1
    if player // 10 == 1:
        opp = 2
        fwd = pos + 8
        diagL = pos + 9
        diagR = pos + 7
    else:
        fwd = pos - 8
        diagL = pos - 7
        diagR = pos - 9


    if IsOnBoard(fwd):
        if board[fwd] == 0:
            r_list += [fwd]
        if (pos + 1) % 8 != 0:
            if board[diagL] // 10 == opp:
                r_list += [diagL]
        if pos % 8 != 0:
           if board[diagR] // 10 == opp:
                r_list += [diagR]

    return r_list


def GetBishopMoves(pos, board):
    player = board[pos] // 10
    opp = 1
    if player == 1:
        opp = 2

    nr = pos % 8
    nl = 7 - (pos % 8)
    accum = []
    ul = ll = ur = lr = pos

    for i in range(0, nr, 1):
        lr -= 9
        if IsOnBoard(lr):
            if board[lr] == 0:
                accum += [lr]
            else:
                if board[lr] // 10 == opp:
                    accum += [lr]
                break

    for i in range(0, nr, 1):
        ur += 7
        if IsOnBoard(ur):
            if board[ur] == 0:
                accum += [ur]
            else:
                if board[ur] // 10 == opp:
                    accum += [ur]
                break

    for i in range(0, nl, 1):
        ul += 9
        if IsOnBoard(ul):
            if board[ul] == 0:
                accum += [ul]
            else:
                if board[ul] // 10 == opp:
                    accum += [ul]
                break

    for i in range(0, nl, 1):
        ll -= 7
        if IsOnBoard(ll):
            if board[ll] == 0:
                accum += [ll]
            else:
                if board[ll] // 10 == opp:
                    accum += [ll]
                break

    return accum


def GetRookMoves(pos, board):
    player = board[pos] // 10
    opp = 1
    if player == 1:
        opp = 2

    nl = pos % 8
    nr = 7 - (pos % 8)
    nd = pos // 8
    nu = 7 - (pos // 8)
    accum = []
    l = r = u = d = pos

    for i in range(0, nl, 1):
        l -= 1
        if IsOnBoard(l):
            if board[l] == 0:
                accum += [l]
            else:
                if board[l] // 10 == opp:
                    accum += [l]
                break

    for i in range(0, nr, 1):
        r += 1
        if IsOnBoard(r):
            if board[r] == 0:
                accum += [r]
            else:
                if board[r] // 10 == opp:
                    accum += [r]
                break

    for i in range(0, nd, 1):
        d -= 8
        if IsOnBoard(d):
            if board[d] == 0:
                accum += [d]
            else:
                if board[d] // 10 == opp:
                    accum += [d]
                break

    for i in range(0, nu, 1):
        u += 8
        if IsOnBoard(u):
            if board[u] == 0:
                accum += [u]
            else:
                if board[u] // 10 == opp:
                    accum += [u]
                break

    return accum


def GetKnightMoves(pos, board):
    r_list = []
    player = board[pos]
    opp = 1
    if player//10 == 1:
        opp = 2

    # clockwise from the top right hand move
    moves = [pos + 15, pos + 6, pos - 10, pos - 17, pos - 15, pos - 6, pos + 10, pos + 17]
    if pos % 8 == 0:
        moves = moves[4:len(moves)]
    elif (pos+1) % 8 == 0:
        moves = moves[0:5]
    elif (pos-1) % 8 == 0:
        moves = [moves[0]] + moves[3:len(moves)]
    elif (pos+2) % 8 == 0:
        moves = moves[0:5] + [moves[len(moves) - 1]]

    for i in moves:
        if IsOnBoard(i):
            if board[i] == 0 or board[i]//10 == opp:
                r_list += [i]

    return r_list


def GetQueenMoves(pos, board):
    return GetRookMoves(pos, board) + GetBishopMoves(pos, board)


def GetKingMoves(pos, board):
    r_list = []
    opp = 1
    if board[pos]//10 == 1:
        opp = 2

    moves = [pos + 7, pos - 1, pos - 7, pos - 8, pos + 1, pos - 9, pos + 9, pos + 8]
    if pos % 8 == 0:
        moves = moves[3:len(moves)]
    elif (pos + 1) % 8 == 0:
        moves = moves[0:4] + [moves[len(moves)-1]]

    for i in moves:
        if IsOnBoard(i) and (board[i] // 10 == opp or board[i] == 0):
            r_list += [i]

    return r_list


def IsOnBoard(pos):
    if (pos >= 0) and (pos <= 63):
        return True
    else:
        return False


def IsPositionUnderThreat(board, position, player):
    opp = 1
    if player == 10:
        opp = 2

    # threatened by pawn
    opp_pos_p = GetPawnMoves(position, board)
    for i in opp_pos_p:
        if (i != position + 8 or i != position - 8) and (board[i] // 10 == opp and board[i] % 10 == 0):
            return True

    # threatened by knight
    opp_pos_kn = GetKnightMoves(position, board)
    for i in opp_pos_kn:
        if board[i] // 10 == opp and board[i] % 10 == 1:
            return True

    # threatened by bishop
    opp_pos_b = GetBishopMoves(position, board)
    for i in opp_pos_b:
        if board[i]//10 == opp and board[i] % 10 == 2:
            return True

    # threatened by rook
    opp_pos_r = GetRookMoves(position, board)
    for i in opp_pos_r:
        if board[i]//10 == opp and board[i] % 10 == 3:
            return True

    # threatened by queen
    opp_pos_q = opp_pos_b + opp_pos_r
    for i in opp_pos_q:
        if board[i]//10 == opp and board[i] % 10 == 4:
            return True

    # threatened by king
    opp_pos_k = GetKingMoves(position, board)
    for i in opp_pos_k:
        if IsOnBoard(i):
            if board[i]//10 == opp and board[i] % 10 == 5:
                return True

    return False


def PieceThreatening(board, position, player):
    opp = 1
    if player == 10:
        opp = 2

    # threatened by pawn
    opp_pos_p = GetPawnMoves(position, board)
    for i in opp_pos_p:
        if (i != position + 8 or i != position - 8) and (board[i] // 10 == opp and board[i] % 10 == 1):
            return i

    # threatened by knight
    opp_pos_kn = GetKnightMoves(position, board)
    for i in opp_pos_kn:
        if board[i] // 10 == opp and board[i] % 10 == 1:
            return i

    # threatened by bishop
    opp_pos_b = GetBishopMoves(position, board)
    for i in opp_pos_b:
        if board[i]//10 == opp and board[i] % 10 == 2:
            return i

    # threatened by rook
    opp_pos_r = GetRookMoves(position, board)
    for i in opp_pos_r:
        if board[i]//10 == opp and board[i] % 10 == 3:
            return i

    # threatened by queen
    opp_pos_q = opp_pos_b + opp_pos_r
    for i in opp_pos_q:
        if board[i]//10 == opp and board[i] % 10 == 4:
            return i

    # threatened by king
    opp_pos_k = GetKingMoves(position, board)
    for i in opp_pos_k:
        if IsOnBoard(i):
            if board[i]//10 == opp and board[i] % 10 == 5:
                return i

    return -1


def getPieceScore(piece, player):
    opp = piece // 10
    piece = piece % 10
    score = 0

    if piece == 0:
        score = 10
    elif piece == 1 or piece == 2:
        score = 30
    elif piece == 3:
        score = 50
    elif piece == 4:
        score = 90
    elif piece == 5:
        score = 900

    if opp == player:
        score *= -1

    return score


def IsInCheck(board, player):
    king = player + 5
    k_pos = 0

    for i in range(len(board)):
        if board[i] == king:
            k_pos = i
            break

    if IsPositionUnderThreat(board, k_pos, player):
        return True

    return False
