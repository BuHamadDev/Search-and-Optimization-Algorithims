'''
Iteritave deepining Depth First Search
'''

from pyamaze import maze, agent, COLOR

def IDDFS(m, start=None, maxDepth = None):
    
    # Assign max depth if user didnt specify
    if maxDepth is None:
        maxDepth = m.rows * m.cols

    # If start is not specified by user start from bottom right
    if start is None:
        start(m.rows, m.cols)


    totalExplored = []

    for limit in range(maxDepth):
        frontier = [(start, 0)] # (cell, depth)
        explored_this_iteration = {start}
        iddfsPath = {}
        pathFound = False
        
        while len(frontier) > 0 :
            parentCell, depth = frontier.pop()

            if parentCell in totalExplored:
                continue
            totalExplored.append((parentCell, depth))

            if parentCell == m._goal:
                pathFound = True
                break

            if depth < limit : 
                for d in 'ESWN':
                    pass
                    #TODO: Finish the search

m = maze()