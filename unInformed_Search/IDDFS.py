'''
Performs Iterative Deepening Depth-First Search on a maze.
IDDFS combines the space efficiency of DFS with the optimality of BF
'''

from pyamaze import maze, agent, COLOR

def IDDFS(m, start=None, maxDepth = None):
    
    # STEP 1: INITIALIZATION
    #========================

    # Set maximum depth to search 
    # Default: total cells in the maze (m.rows * m.cols)
    if maxDepth is None:
        maxDepth = m.rows * m.cols

    # Set the starting position if not provided by the user
    # Default: bottom right cell
    if start is None:
        start = (m.rows,m.cols)
    
    # Track all cells explored across all iterations
    totalExplored = []

    # STEP 2: Iterative deepining loop
    #=================================

    # We gradually increase depth limit until limit is reached or goal is found
    # Start with depth 0 then 1 then 2 etc...
    for limit in range(1, maxDepth + 1):

        # STEP 3: Setup for this depth iteration
        #=======================================

        # Frontier is our DFS stack
        # We use stack (LIFO) because this is DFS
        frontier = [(start,0)]

        # Track all cells explored in this iteration
        explored_this_iteration = {start}

        # Store the path: maps each cell to its parent cell
        # Format: {child:parent}
        parent = {}

        # Flag variable to track if goal was found
        # Will be used to determine if we need optimal path or not
        pathFound = False

        # STEP 4: Depth limited DFS
        #=======================================
        
        # In this step we perform DFS but we stop at the current limit

        while len(frontier) > 0: 
            parentCell, depth = frontier.pop() # Stack DS

            
            # Mark the cell as explored
            totalExplored.append(parentCell)

            # STEP 5: GOAL CHECK
            # ==================
            # Check if we've reached the goal (usually at position (1,1))
            if parentCell == m._goal:
                pathFound = True    # Set pathFound flag to true
                break  # Exit the while loop - we found the goal!
            
            # STEP 6: EXPAND NEIGHBORS (if within depth limit)
            # =================================================
            
            # Only expand children if we haven't reached the depth limit
            if depth < limit:
                
                for d in 'ESWN':
                    # Check if there's an open path in this direction
                    # m.maze_map[cell][direction] is True if path exists
                    if m.maze_map[parentCell][d]:
                        
                        # Calculate the coordinates of the child cell
                        # based on the direction we're moving
                        if d == 'E':  # East: move right (increase column)
                            childCell = (parentCell[0], parentCell[1] + 1)
                        elif d == 'W':  # West: move left (decrease column)
                            childCell = (parentCell[0], parentCell[1] - 1)
                        elif d == 'S':  # South: move down (increase row)
                            childCell = (parentCell[0] + 1, parentCell[1])
                        else:  # North: move up (decrease row)
                            childCell = (parentCell[0] - 1, parentCell[1])
                    
                        # Skip if we already explored this cell
                        if childCell in explored_this_iteration:
                            continue

                        explored_this_iteration.add(childCell)

                        # Add child to frontier with incremented depth
                        frontier.append((childCell, depth + 1))

                        # Record the path
                        parent[childCell] = parentCell

        # STEP 7: CHECK IF GOAL WAS FOUND
        # ================================
        # If we found the goal at this depth, reconstruct the path and return
        if pathFound:
            
            # Reconstruct the optimal path by backtracking from goal to start
            optimalPath = {}
            cell = m._goal
            
            # Walk backwards through iddfsPath until we reach the start
            while cell != start:
                # Reverse the direction: if iddfsPath[child] = parent,
                # then optimalPath[parent] = child
                optimalPath[parent[cell]] = cell
                cell = parent[cell]
            
            # Return both the exploration history and the optimal path
            return totalExplored, optimalPath
    
    # STEP 8: NO PATH FOUND
    # =====================
    # If we've tried all depths up to maxDepth and found no path
    # Return empty results indicating failure
    return totalExplored, {}


# Create maze
m = maze()
m.CreateMaze(theme = COLOR.light, loopPercent = 50)

# Get path
explored, path = IDDFS(m)

# Create agents to visualize the search

# Blue agent shows all explored cells
a = agent(m, footprints=True, color=COLOR.blue, filled=True)
    
# Red agent shows the optimal path
b = agent(m, footprints=True, color=COLOR.red, filled=True)
    
# Trace the paths on the maze
m.tracePath({a: explored}, delay=50)  # Show exploration
m.tracePath({b: path}, delay=100)     # Show optimal path
    
# Display the maze
m.run()




    