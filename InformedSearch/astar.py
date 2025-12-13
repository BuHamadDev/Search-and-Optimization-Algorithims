from pyamaze import maze, agent, COLOR
from queue import PriorityQueue

def h(cell):
    x1,y1 = cell
    x2,y2 = m._goal
    return abs(x1-x2) + abs(y1- y2)

def astar(m):
    #TODO: implement A*
    pass


m = maze()
m.CreateMaze()

explored, path = astar(m)

a1 = agent(m,color=COLOR.blue, footprints=True,filled=True)
a2 = agent(m,color=COLOR.red, footprints=True, shape='arrow')

m.tracePath({a1:explored}, delay=70)
m.tracePath({a2:path}, delay=10)

m.run()