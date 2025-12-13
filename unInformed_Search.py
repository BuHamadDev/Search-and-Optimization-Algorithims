'''
Implement DFS & BFS


Search Approach:

-Start with a frontier list that contains the initial state.
-Start with an empty explored set. 

Repeat:
    -If the frontier is empty, then no solution. 
    -Remove a node from the frontier.
    -If node contains goal state, return the solution.
    -Add the node to the explored set.
    -Expand node, add resulting node to the frontier if they aren’t already in the frontier or the explored list. 

The main difference between DFS and BFS is the way we pop from the frontier.
BFS uses FIFO data structure, while DFS uses FILO data structure.

To implement BFS we simply change the way we pop from the frontier.

Line 49 :

BFS --> currCell = frontier.pop(0) # FIFO
DFS --> currCell = frontier.pop()  # LIFO


'''
# Import pyamaze
from pyamaze import maze, agent, COLOR


def DFS(m, start = None):

    # If user did not specify starting node then start from the bottom right
    if start == None:
        start = (m.rows, m.cols)
    
    # Initialize frontier & explored lists
    explored = []
    frontier = [start]

    dfscells = [] # We return this list, which contains the path taken by DFS

    # Keep looping until frontier is empty
    while len(frontier) > 0 :

        # Remove a node from frontier
        currCell = frontier.pop()

        #Add node to explored and dfs lists
        explored.append(currCell)
        dfscells.append(currCell)

        # Check if this cell is the goal state
        if currCell == m._goal:
            break

        # Check neighboring nodes and expand the node
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True :
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1 )
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1 )
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1] )
                if d == 'N':
                    childCell = (currCell[0] - 1, currCell[1] )
                
                
                # Add child cell to the frontiet if its not reached yet
                if childCell in frontier or childCell in explored:
                    continue
                
                frontier.append(childCell)
        
    # Return path taken
    return dfscells


# Create maze
m = maze()
m.CreateMaze(theme = COLOR.light, loopPercent = 50)

# Create Agent
a = agent(m, color=COLOR.red, footprints=True, shape='arrow')

# Get the path using DFS function we implemented
path = DFS(m)

# Trace the path
m.tracePath({a:path}, delay=100)

# Run the maze
m.run()


