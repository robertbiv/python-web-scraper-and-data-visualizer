import heapq
from eastgate_helper import get_office_grid, get_terrain_costs, test_scenarios

def dist(pos1, pos2):
    # custom heuristic for 8-dir movement
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    # diagonal distance: min(dx,dy)*sqrt(2) + abs(dx-dy)*1
    return min(dx, dy) * 1.414 + abs(dx - dy)

def get_path(parent, node):
    # build path backwards
    path = [node]
    while node in parent:
       node = parent[node]
       path.append(node)
    path.reverse()
    return path

def a_star(grid, start, goal, costs=None):
    # a star pathfinding
    if not grid or not grid[0]:
        return None

    rows = len(grid)
    cols = len(grid[0])

    def valid(r, c):
        # check if in grid
        return r >= 0 and r < rows and c >= 0 and c < cols

    # validate start and goal
    if not valid(start[0], start[1]) or not valid(goal[0], goal[1]):
        return None
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None

    if costs is None:
        # default costs
        costs = [[1 for j in range(cols)] for i in range(rows)]

    def cell_cost(r, c):
        # get cost to enter cell
        val = costs[r][c]
        if val < 1: 
            return 1
        return val

    open_list = [] 
    counter = 0 
    g = {start: 0} 
    parent = {} 

    heapq.heappush(open_list, (dist(start, goal), counter, start))

    # 8 directions: ortho + diagonals
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1),  # orthogonal
             (1, 1), (1, -1), (-1, 1), (-1, -1)]  # diagonal

    closed = {}

    while open_list:
        f, count, current = heapq.heappop(open_list)
        
        if current == goal:
            return get_path(parent, current)

        cur_g = g.get(current, 99999)
        if closed.get(current, 99999) <= cur_g:
            continue
        closed[current] = cur_g

        for move in moves:
            next_r = current[0] + move[0]
            next_c = current[1] + move[1]
            if not valid(next_r, next_c):
                continue
            if grid[next_r][next_c] == 1:
                continue  # wall
            
            # diagonal moves cost sqrt(2) ≈ 1.414
            move_cost = 1.414 if abs(move[0]) + abs(move[1]) == 2 else 1.0
            new_g = cur_g + cell_cost(next_r, next_c) * move_cost
            next_pos = (next_r, next_c)
            if new_g < g.get(next_pos, 99999):
                parent[next_pos] = current
                g[next_pos] = new_g
                heuristic = dist(next_pos, goal) 
                counter += 1
                heapq.heappush(open_list, (new_g + heuristic, counter, next_pos))
                
    return None  # no path found


def show_grid(grid, path=None, costs=None):
    # extra credit: visualize grid with path and costs
    print("\nGrid Visualization:")
    if costs:
        print("Costs:")
        for i in range(len(costs)):
            for j in range(len(costs[0])):
                print(f"{costs[i][j]}", end=" ")
            print()
    
    print("\nGrid with path:")
    path_coords = set(path) if path else set()
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in path_coords:
                if (r, c) == path[0]:  # start
                    print("S", end=" ")
                elif (r, c) == path[-1]:  # goal
                    print("G", end=" ")
                else:
                    print("*", end=" ")  # path
            elif grid[r][c] == 1:
                print("#", end=" ")  # wall
            else:
                print(".", end=" ")  # open
        print()


if __name__ == '__main__':
    # run basic tests
    test_scenarios(a_star)
    
    # extra credit visualization
    grid = get_office_grid()
    costs = get_terrain_costs(grid)
    path = a_star(grid, (0, 0), (4, 4), costs)
    show_grid(grid, path, costs)
