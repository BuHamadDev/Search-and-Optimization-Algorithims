import random
from pyamaze import maze, agent, COLOR


def UCS(m, start = None):
    if start is None:
        start = (m.rows,m.cols)

    # Assign random movement costs for each direction
    cell_costs = {}
    for cell in m.grid:
        cell_costs[cell] = {d: random.randint(1,5) for d in 'ESWN'}
    
    frontier = [(start,0)]
    explored = []
    parent = {}

    while len(frontier) > 0:
        frontier.sort(key = lambda x : x[1] )
        parentCell, currCost = frontier.pop(0)

        if parentCell in explored:
            continue

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
                    childCell = (parentCell[0] - 1, parentCell[1])
                

                if childCell not in explored:
                    step_cost = cell_costs[parentCell][d]
                    totalCost = currCost + step_cost
                    frontier.append((childCell, totalCost))
                    parent[childCell] = parentCell

    
    # Build optimal path
    if m._goal not in explored:
        print("Goal is unreachable")
        return {}, explored
    else:
        optimalPath = {}
        cell = m._goal
        while cell != start:
            optimalPath[parent[cell]] = cell
            cell = parent[cell]

        return optimalPath, explored
    

m = maze()
m.CreateMaze(theme=COLOR.light, loopPercent=50)

a1 = agent(m,color=COLOR.blue, footprints=True, filled=True)
a2 = agent(m,color=COLOR.red, footprints=True, shape='arrow')

path, explored = UCS(m)


m.tracePath({a1:explored}, delay=50)
if path:
    m.tracePath({a2:path}, delay=50)

m.run()              

                

                




