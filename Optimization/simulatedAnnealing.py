import random
import math

N = 6

def h_evaluate(board):
    h=0
    for c1 in range(N):
        for c2 in range(c1+1,N):
            r1,r2 = board[c1], board[c2]
            if r1==r2 or (abs(c1-c2)==abs(r1-r2)):
                h+=1
    return h
def randomize_board():
    return [random.randint(0,N-1) for _ in range(N)]


def print_board(board):
    for r in range(N):
        for c in range(N):
            if board[c]==r:
                print('Q', end=" ")
            else:
                print('.', end=" ")
        print()


def sa(board, minTemp = 0.01, reducingFactor = 0.999, T = 100):
    
    print("initial board:\n")
    print_board(board)

    MAX_STEPS = 100
    step = 0

    while T > minTemp and step<MAX_STEPS:
        current_h = h_evaluate(board)
        temp_board = board[:]

        #Pick a random move
        moveFound = False
        while not moveFound:   
            
            c = random. randint(0,N-1)
            r = random.randint(0,N-1)
            if board[c] != r:
                moveFound = True
            
        temp_board[c] = r
        temp_h = h_evaluate(temp_board)

        if temp_h<=current_h:
            board = temp_board
            current_h = temp_h
            print_board(board)
            print(f"Step {step}: moved Q in column {c} to row {r}")
            step+=1
        
        else:
            delta_h = temp_h - current_h
            p = math.exp(-delta_h/T)
            num = random.random()
            if num < p:
                board = temp_board
                current_h = temp_h
                T*=reducingFactor
                print_board(board)
                print(f"Step {step}: moved Q in column {c} to row {r} (worse move)")
                step+=1



board = randomize_board()
sa(board)