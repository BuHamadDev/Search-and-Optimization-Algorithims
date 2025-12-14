import random
import time
N = 6
def randomize_board():
    return [random.randint(0,N-1) for _ in range(N)]


def h_evaluate(board):
    h = 0

    for c1 in range(N):
        for c2 in range(c1+1,N):
            if board[c1] == board[c2]:
                h+=1
            if abs(board[c1] - board[c2]) == abs(c1-c2):
                h+=1
    return h

def print_board(board):
    for r in range(N):
        for c in range(N):
            if board[c] == r:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def RR(board):

    current_h = h_evaluate(board)
    print("Initial board:\n")
    print_board(board)
    print("Attacks: ", current_h)

    
    MAX_STEPS = 100
    step = 0

    while step < MAX_STEPS:
        step+=1
        improved = False
        current_h = h_evaluate(board)

        for c in range(N):
            orig_r = board[c]
            for r in range(N):
                if r == orig_r:
                    continue
                
                temp_board = board[:]
                temp_board[c] = r
                temp_h = h_evaluate(temp_board)

                if temp_h < current_h :
                    improved = True
                    board = temp_board
                    current_h = temp_h
                    print_board(board)
                    
                    print(f"Step {step} moved Q in column {c} to row {r}\n")
                    time.sleep(0.5)
                    break
            
            if improved:
                break
        
        if current_h == 0:
            print("Reached global minima. h = 0")
            return
        
        if not improved:
            print("Reached local minima. No improving neighbour. Restartig . . .")
            board = randomize_board()
            time.sleep(3)
            print("New board:\n")
            print_board(board)
            
            


board = randomize_board()
RR(board)


