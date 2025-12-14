from pyamaze import maze, agent, COLOR
from queue import PriorityQueue


def h(cell):
    x1, y1 = cell
    x2, y2 = m._goal
    return abs(x1-x2) + abs(y1-y2)

def GBFS(m, start = None):
    if start == None:
        start = (m.rows, m.cols)

    frontier = PriorityQueue()
    frontier.put((h(start), start))

    explored = []
    parent = {}

    while not frontier.empty():
        parentCell = frontier.get()[1]

        if parentCell == m._goal:
            break

        explored.append(parentCell)

        for d in 'EWNS':
            if m.maze_map[parentCell][d]:
                if d == 'E':
                    childCell = (parentCell[0], parentCell[1]+1)
                elif d == 'W':
                    childCell = (parentCell[0], parentCell[1]-1)
                elif d == 'S':
                    childCell = (parentCell[0]+1, parentCell[1])
                else:
                    childCell = (parentCell[0]-1, parentCell[1])
                
                if childCell in explored:
                    continue

                
                child_h = h(childCell)
                frontier.put((child_h, childCell))
                parent[childCell] = parentCell
    
    optimalPath = {}
    cell = m._goal
    while cell != start:
        optimalPath[parent[cell]] = cell
        cell = parent[cell]

    return explored, optimalPath


m = maze()
m.CreateMaze(theme=COLOR.light, loopPercent=70)

explored, path = GBFS(m)

a1 = agent(m, color=COLOR.blue, footprints=True, filled=True)
a2 = agent(m, color=COLOR.red, footprints=True, shape='arrow')

m.tracePath({a1:explored}, delay=70)
m.tracePath({a2:path}, delay = 70)

m.run()

