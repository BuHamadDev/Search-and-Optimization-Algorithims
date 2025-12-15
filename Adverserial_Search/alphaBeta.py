import time

board = {i:'' for i in range(1,10)}

def print_board():
    pass

def checkForWin():
    winPos = [
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (1,4,7),
        (2,5,8),
        (3,6,9),
        (1,5,9),
        (3,5,7)
    ]

    for pos in winPos:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] and board[pos[0]] == '':
            return board[pos[0]]
        
    return None

def checkForDraw():
    return all(board[pos] != '' for pos in board.keys)

def isFreeSpace(pos):
    return board[pos] == ''




def insertLetter(player,pos):
    if isFreeSpace(pos):
        board[pos] = player
        if checkForDraw():
            print("Draw")
            exit()

        winner = checkForWin()
        if winner:
            print(f"{winner} wins")

    else:
        pos = int(input("Ente: "))
        insertLetter(player, pos)

def bestMove():
    bestMove = None
    bestScore = -float("inf")
    for pos in board.keys:
        if isFreeSpace(pos):
            board[pos] = 'X'
            score = minmax(False)
            board[pos] = ''
            if bestScore<score:
                bestScore=score
                move = pos
    return move


def minmax(isMaximizer):
    winner = checkForWin()
    if winner:
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        elif checkForDraw():
            return 0
    
    if isMaximizer:
        bestScore = -float('inf')
        for pos in board.keys:
            if isFreeSpace(pos):
                board[pos] = 'X'
                score = minmax(False)
                board[pos] = ''
                if score> bestScore:
                    bestScore = score
        
        return bestScore
    
    else:
        bestScore = float('inf')
        for pos in board.keys:
            if isFreeSpace(pos):
                board[pos] = 'O'
                score = minmax(True)
                board[pos] = ''
                if bestScore>score:
                    bestScore = score
        return bestScore