'''
Depth-Limited Search Algorithim

In this search algorithim we implement normal dfs BUT with a depth limit, so we dont get stuck in infinite loops.

'''

from pyamaze import maze, agent, COLOR

def DLS(m, start = None, limit = 10):

    # If start is not specified by use then use default (bottom right)
    if start == None:
        start = (m.rows, m.cols)
    

    parent = {} # Maps Parent --> Child
    frontier = [(start,0)] # Track stack/queue
    explored = []

    # Keep serching until goal is found or frontier is empty
    while len(frontier) > 0:

        parentCell, depth = frontier.pop() # Use stack data structure
        
        # Stop expanding if we reached the depth limit
        if depth>=limit:
            continue
        
        if parentCell in explored:
            continue

        explored.append(parentCell)

        # Break if goal was found
        if parentCell == m._goal:
            break
        
        

        #Get child cell
        for d in 'EWNS':
            if m.maze_map[parentCell][d]:
                if d == 'E':
                    childCell = (parentCell[0], parentCell[1] + 1 )
                elif d == 'W':
                    childCell = (parentCell[0], parentCell[1] - 1 )
                elif d == 'N':
                    childCell = (parentCell[0] - 1, parentCell[1] ) 
                else :
                    childCell = (parentCell[0] + 1, parentCell[1] )
                
                # Add the child to frontier and parent dictionary if not yet explored
                if childCell in frontier or childCell in explored:
                    continue

                frontier.append((childCell, depth + 1)) # CRITICAL : Increment depth
                parent[childCell] = parentCell
        
    if m._goal in explored and start != m._goal:       
            optimalPath = {}
            cell = m._goal
            while cell != start:
                optimalPath[parent[cell]] = cell
                cell = parent[cell]
    else:
        optimalPath = None
            
    return optimalPath, explored
        
# Create maze
m = maze(5,5)
m.CreateMaze(theme=COLOR.light, loopPercent=50)

# Get paths
optimal, explored = DLS(m, limit=15) # Try different limits

# Create agents
a1 = agent(m, color=COLOR.blue, footprints=True, filled=True)
a2 = agent(m, color=COLOR.red, footprints=True, shape='arrow')

# Trace paths
m.tracePath({a1:explored}, delay=70)

if optimal:
    m.tracePath({a2:optimal}, delay=70)
    print("Goal cell is within the depth limit. Goal cell is reachable.")

else:
    print("Depth limit reached, goal cell is unreachable.")
m.run()




    