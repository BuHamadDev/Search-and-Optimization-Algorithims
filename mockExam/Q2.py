'''
Begin with a randomly generated board, placing exactly one queen in each column. You
will repeatedly modify this board by creating a neighbour: choose a column at random
and move its queen to a different row within the same column. After generating each
neighbour, decide whether to keep it or revert to the previous state.

At every iteration, the temperature must cool down according to the schedule:

T_new=0.99 x T_old

Stop the process when either:
- You reach a board with zero conflicts, or
- The temperature drops below 0.001.

Throughout the search, you should display the progression of your solver in the terminal.
Print the initial board and its conflict count. Then, whenever a move is accepted, print the
step number, the new board, the updated conflict value, and the current temperature. At
the end of the run, print the final state and clearly indicate whether a valid solution was
found.
'''

import random
import math

N = 15

def randomize_board():
    return [random.randint(0,N-1) for _ in range(N)]

def h_evaluate(board):
    h = 0
    for c1 in range(N):
        for c2 in range(c1+1,N):
            r1,r2 = board[c1],board[c2]
            if r1 == r2 or abs(c1-c2)==abs(r1-r2):
                h+=1
    return h

def print_board(board):
    for r in range(N):
        for c in range(N):
            if board[c] == r:
                print('Q', end=" ")
            else: 
                print('.', end=" ")
        print()
def sa(board,minTemp = 0.001, cool_rate = 0.99, T = 10000000000):
    
    step = 0
    while minTemp < T:
        
        curr_h = h_evaluate(board)
        temp_board = board[:]
        found_move = False
        while not found_move:
            c = random.randint(0,N-1)
            r = random.randint(0,N-1)
            if temp_board[c] != r:
                temp_board[c] = r
                found_move = True
        
        
        temp_h = h_evaluate(temp_board)

        if temp_h<= curr_h:
            curr_h = temp_h
            board = temp_board
            step+=1
            if curr_h == 0:
                print(f"Solution found at T = {T}")
                break
        
        else:
            delta_h = temp_h - curr_h
            p = math.exp(-delta_h/T)
            num = random.random()
            if num < p:
                curr_h = temp_h
                board = temp_board
                step+=1
        
        
        T= T * cool_rate
    
    print("No solutuion")
    return board





print_board(sa(randomize_board()))