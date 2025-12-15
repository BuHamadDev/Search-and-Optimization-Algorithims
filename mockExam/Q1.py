'''
Task to be completed:

1) Create a virtual environment by name MockLabTest and install Pyamaze library in
that. You need to use this virtual environment for rest of the lab test.


2) For each of the four algorithms (DFS, BFS, A*, Greedy BFS), modify the code so
that it computes and prints:

- Number of nodes expanded (i.e., how many distinct cells were removed from
the frontier/open list and processed).

- Path length from start to goal (number of steps in the returned path).


3) Use different agents or different colors in pyamaze to show the final path returned
by each algorithm on the same maze.


'''
from pyamaze import maze, agent, COLOR,textLabel
from queue import PriorityQueue

def h(cell):
    x1,y1=cell
    x2,y2= m._goal
    return abs(x1-x2)+abs(y1-y2)

def DFS(m):

    explored = []
    start=(m.rows,m.cols)
    frontier = [start]
    parent = {}
    expanded_counter = 0

    while len(frontier)>0:
        parentCell = frontier.pop()
        expanded_counter+=1

        explored.append(parentCell)
        if parentCell == m._goal:
            break

        for d in 'ESWN':
            if m.maze_map[parentCell][d]:
                if d =='E':
                    childCell = (parentCell[0],parentCell[1]+1)
                elif d =='W':
                    childCell = (parentCell[0],parentCell[1]-1)
                elif d == 'S':
                    childCell = (parentCell[0]+1,parentCell[1])
                else:
                    childCell = (parentCell[0]-1, parentCell[1])
                
                if childCell not in explored and childCell not in frontier:
                    frontier.append(childCell)
                    
                    parent[childCell]=parentCell

    #reconstruct path
    fwdPath = []
    cell = m._goal
    pathLength = 1
    while cell != start:
        fwdPath.append(cell) 
        cell = parent[cell]
        pathLength+=1
    fwdPath.reverse()
    return fwdPath,explored, pathLength, expanded_counter                    

def BFS(m):

    explored = []
    start=(m.rows,m.cols)
    frontier = [start]
    parent = {}
    expanded_counter = 0

    while len(frontier)>0:
        parentCell = frontier.pop(0)
        expanded_counter+=1

        explored.append(parentCell)
        if parentCell == m._goal:
            break

        for d in 'ESWN':
            if m.maze_map[parentCell][d]:
                if d =='E':
                    childCell = (parentCell[0],parentCell[1]+1)
                elif d =='W':
                    childCell = (parentCell[0],parentCell[1]-1)
                elif d == 'S':
                    childCell = (parentCell[0]+1,parentCell[1])
                else:
                    childCell = (parentCell[0]-1, parentCell[1])
                
                if childCell not in explored and childCell not in frontier:
                    frontier.append(childCell)
                    
                    parent[childCell]=parentCell

    #reconstruct path
    fwdPath = []
    cell = m._goal
    pathLength = 1
    while cell != start:
        fwdPath.append(cell) 
        cell = parent[cell]
        pathLength+=1
    fwdPath.reverse()
    return fwdPath,explored, pathLength, expanded_counter    

def astar(m):

    explored = []
    start = (m.rows,m.cols)
    g_cost = {cell: float("inf") for cell in m.grid}
    g_cost[start] = 0
    frontier = PriorityQueue()
    frontier.put((h(start),start))
    parent = {}
    exploredCounter = 0

    while not frontier.empty():
        parentCell = frontier.get()[1]
        exploredCounter+=1
        if parentCell not in explored:
            explored.append(parentCell)

        if parentCell == m._goal:
            break

        for d in 'ESWN':
            if m.maze_map[parentCell][d]:
                if d =='E':
                    childCell = (parentCell[0],parentCell[1]+1)
                elif d =='W':
                    childCell = (parentCell[0],parentCell[1]-1)
                elif d == 'S':
                    childCell = (parentCell[0]+1,parentCell[1])
                else:
                    childCell = (parentCell[0]-1, parentCell[1])
                
                
                parent_g = g_cost[parentCell]
                child_g = parent_g + 1
                if child_g < g_cost[childCell]:
                    g_cost[childCell] = child_g
                    frontier.put((child_g+h(childCell), childCell))
                    parent[childCell] = parentCell

    #reconstruct path
    fwdPath = []
    cell = m._goal
    pathLength = 0
    while cell != start:
        fwdPath.append(cell)
        pathLength+=1
        cell = parent[cell]
    fwdPath.reverse()
    return fwdPath,explored,pathLength,exploredCounter

m=maze(50,50)
m.CreateMaze(theme=COLOR.light,loopPercent=50)

a = agent(m,color=COLOR.yellow,footprints=True,filled=True)
a1 = agent(m,color=COLOR.black, footprints=True,shape='arrow')

#path, explored, pathCounter, exploredCounter = DFS(m)
path, explored, pathCounter, exploredCounter = astar(m)

m.tracePath({a:explored},delay=80)
m.tracePath({a1:path}, delay = 20)
print(f"Explored count:{exploredCounter}")
print(f"Path length:{pathCounter}")
m.run()