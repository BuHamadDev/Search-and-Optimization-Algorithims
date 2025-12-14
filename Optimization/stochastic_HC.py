import time
import random

N = 6

def h_evaluate(board):
    h=0
    for c1 in range(N):
        for c2 in range(c1+1,N):
            r1, r2 = board[c1], board[c2]
            if r1 == r2 or (abs(c1-c2)==abs(r1-r2)):
                h+=1

    return h

def randomize_board():
    return [random.randint(0,N-1) for _ in range(N)]

def print_board(board):
    for r in range(N):
        for c in range(N):
            if board[c] == r:
                print('Q', end=" ")
            else:
                print('.', end=" ")

        print()


def sa(board):

    current_h = h_evaluate(board)
    print("Initial board:\n")
    print_board(board)
    MAX_STEPS = 100
    step = 0
    while step < MAX_STEPS:
        step+=1
        
        
        improving_moves = []

        for c in range(N):
            orig_r = board[c]
            for r in range(N):
                if r == orig_r:
                    continue
                temp_board = board[:]
                temp_board[c] = r
                temp_h = h_evaluate(temp_board)

                if temp_h < current_h:
                    improving_moves.append((temp_board,temp_h,c,r))
        
        if len(improving_moves) > 0:
            board, current_h, c , r = random.choice(improving_moves)
            print(f"Step {step}: moved Q in column {c} to row {r}")
            print_board(board)
            if current_h == 0:
                print("Reached global minima")
                return
        else:
            print("Stuck in local/global minima")
            return

board = randomize_board()
sa(board)
            
