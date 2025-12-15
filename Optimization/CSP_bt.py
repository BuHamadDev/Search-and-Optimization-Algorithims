N = 4
board = [-1] * N

def print_board():
    for r in range(N):
        for c in range(N):
            if board[c] == r:
                print('Q', end=" ")
            else:
                print('.', end=" ")
        print()


def consistent(col,row):
    for c in range(col):
        r = board[c]
        if (r==row) or (abs(c-col)==abs(r-row)):
            return False
    return True

def bt(col=0):
    if col == N:
        return True
    
    for r in range(N):
        if consistent(col,r):
            board[col] = r

            if bt(col+1):
                return True
        
        board[col] = -1
    
    return False

bt()
print_board()