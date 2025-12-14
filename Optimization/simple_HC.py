import random
N = 6



def randomize_board():
    return [random.randint(0,N-1) for _ in range(N)]

def h_evaluate(board):
    h = 0
    
    for c1 in range(N):
        for c2 in range(c1+1,N):
            if board[c1] == board[c2]:
                h+=1
            if abs(board[c1]-board[c2]) == abs(c1-c2):
                h+=1
    
    return h

def print_board(board):
    for r in range(N):
        for c in range(N):
            if board[c] == r:
                print('Q', end=" ")
            else:
                print('.',end=" ")
        print()

    print('Attacks: ', h_evaluate(board))


def simple_hill_climbing(board):
    current_h = h_evaluate(board)
    print("Initial board: ")
    print_board(board)
    print()

    MAX_STEPS = 100
    step = 0
    while step<MAX_STEPS:
        step +=1
        improved = False

        for c in range(N):
            orig_r = board[c]
            for r in range(N):
                if r == orig_r:
                    continue
                temp_board = board[:]

                temp_board[c] = r

                temp_h = h_evaluate(temp_board)

                if temp_h < current_h:
                    improved = True
                    board[c] = r
                    current_h = temp_h
                    print_board(board)
                    print(f"\n Step {step}: move Q in column {c} to row {r} .")
                    break
            
            if improved:
                break
        
        if not improved:
            print("Reached global/local minima (no improving neighbour)")
            break

    return board


board = randomize_board()

board = simple_hill_climbing(board)

print("\nFinal board:")
print_board(board)





