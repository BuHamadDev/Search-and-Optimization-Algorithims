N= 4
board = [-1]*N

def print_board():
    for r in range(N):
        for c in range(N):
            if board[c]==r:
                print('Q',end=" ")
            else:
                print('.',end=" ")
        print()

def consistent(col,row):
    for c in range(col):
        r=board[c]
        if r==row or (abs(col-c)==abs(row-r)):
            return False
    return True

def forward_check(col):
    for c in range(col+1, N):
        found_safe_move = False
        for r in range(N):
            if consistent(c,r):
                found_safe_move=True
                break
            else:
                return False
    
    return True

def solve_fc(col=0):
    if col ==N:
        return True
    
    for r in range(N):
        if consistent(col,r):
            board[col] = r
            if forward_check(col):
                if solve_fc(col+1):
                    return True
                

        board[col] = -1
        