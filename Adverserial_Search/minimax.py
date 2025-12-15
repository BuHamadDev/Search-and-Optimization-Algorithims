board = {i: '' for i in range(1,10)}

def print_board():
    print("\n      -------------")
    print(f"      | {board[1] or ' '} | {board[2] or ' '} | {board[3] or ' '} |")
    print("      -------------")
    print(f"      | {board[4] or ' '} | {board[5] or ' '} | {board[6] or ' '} |")
    print("      -------------")
    print(f"      | {board[7] or ' '} | {board[8] or ' '} | {board[9] or ' '} |")
    print("      -------------")

def isFreeSpace(pos):
    return board[pos] == ''

def checkFoWin():
    winPos = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]
    ]
    for pos in winPos:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] and board[pos[0]]!='':
            return board[pos[0]]
    return None

def checkForDraw():
    return all(board[pos] != '' for pos in board.keys())

def insertLetter(player,pos):
    if isFreeSpace(pos):
        board[pos] = player
        winner = checkFoWin()
        if winner:
            print("\nPlayer {player} won! The other Player is a joke hhhhhhhhh")
            exit()
        elif checkForDraw():
            print("game ended in a draw")
            exit()
    else:
        pos = int(input("Wrong move, try again"))    
        insertLetter(pos)
def bestMove():
    move = None
    bestScore = -float('Inf')
    for pos in board.keys():
        if isFreeSpace(pos):
            board[pos] = 'X'
            score = miniMax(False)
            board[pos] = ''
            if score > bestScore:
                bestScore = score
                move = pos
    return move

def miniMax(isMaximizer):
    winner = checkFoWin()
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif checkForDraw():
        return 0
    
    if isMaximizer:
        bestScore = float('inf')
        for pos in board.keys:
            if isFreeSpace(pos):
                board[pos] = 'X'
                score = miniMax(False)
                board[pos] = ''
                if score> bestScore:
                    bestScore = score
        return bestScore

    if not isMaximizer():
        bestScore = float('inf')
        for pos in board.keys:
            if isFreeSpace(pos):
                board[pos] = 'O'
                score = miniMax(True)
                board[pos] = 'X'
                if bestScore>score:
                    bestScore = score
        return bestScore
    


