from pyamaze import maze, agent, COLOR
from queue import PriorityQueue

def h(cell):
    x1,y1 = cell
    x2,y2 = m._goal
    return abs(x1-x2) + abs(y1- y2)

def astar(m, start = None):

    if start == None:
        start = (m.rows, m.cols)
    
    explored = []

    

    g_cost = {cell: float("inf") for cell in m.grid}
    g_cost[start] = 0

    frontier = PriorityQueue()
    frontier.put((g.get()[0] + h(start), start))
    parent = {}

    while not frontier.empty():

        parentCell = frontier.get()[1]
        parent_g = g_cost[parentCell]
        

        explored.append(parentCell)

        if parentCell == m._goal:
            break

        
        for d in 'ESWN':
            if m.maze_map[parentCell][d]:
                if d == 'E':
                    childCell = (parentCell[0], parentCell[1] + 1)
                elif d == 'W':
                    childCell = (parentCell[0], parentCell[1] - 1)
                elif d == 'S':
                    childCell = (parentCell[0] + 1, parentCell[1])
                else:
                    childCell = (parentCell[0] + 1, parentCell[1])

                g_cost[childCell] = child_g = parent_g + 1
                
                child_h = h(childCell)

                if childCell in explored:
                    continue

                frontier.put((child_g + child_h, childCell))





        
    

    


m = maze()
m.CreateMaze()

explored, path = astar(m)

a1 = agent(m,color=COLOR.blue, footprints=True,filled=True)
a2 = agent(m,color=COLOR.red, footprints=True, shape='arrow')

m.tracePath({a1:explored}, delay=70)
m.tracePath({a2:path}, delay=10)

m.run()