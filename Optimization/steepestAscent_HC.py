import random
N = 6
def print_board(board):
    for r in range(N):
        for c in range(N):
            if board[c] == r:
                print('Q', end=" ")
            else:
                print('.', end=" ")
        print()


def h_evaluate(board):
    h=0
    for c1 in range(N):
        for c2 in range(c1+1,N):
            r1,r2 = board[c1],board[c2]
            if r1 == r2 or (abs(c1-c2)== abs(r1-r2)):
                h+=1
    return h

def randomize_board():
    return [ random.randint(0,N-1) for _ in range(N)]

def sa(board):

    print("Initial board:")
    print_board(board)
    print()
    current_h = h_evaluate(board)
    MAX_STEPS = 100
    step = 0

    while step<MAX_STEPS:
        best_move = None
        
        for c in range(N):
            orig_r = board[c]
            for r in range(N):
                if r == orig_r:
                    continue

                temp_board = board[:]
                temp_board[c] = r
                temp_h = h_evaluate(temp_board)

                if temp_h < current_h:
                    best_move = (temp_h,temp_board,r,c)
            
        if best_move is None or current_h == 0:
            print(f"Stuck in local/global minima (h={current_h})")
            return
        else:
            step+=1
            current_h, board,r,c = best_move
            print_board(board)
            print(f"Step {step}: moved Q in column {c} to row {r}")
            
board = randomize_board()
sa(board)