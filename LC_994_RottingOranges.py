
def oranges_rotting(grid):

    # handle invalid input
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # check if location (row, col) is within the grid.
    def is_valid_location(location):
        return 0<=location[0]<rows and 0<=location[1]<cols

    current_time = 0 # intial time
    queue = [] # for bfs-traversal.
    visited = set()  # to keep track of locations of all the rotten oranges.

    # add all the locations and time for all the rotten oranges and mark the locations visited.
    fresh_oranges = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append(((row, col), current_time))
                visited.add((row, col))
            if grid[row][col] == 1:
                fresh_oranges+=1

    # while all the queues are not empty
    while queue:

        current_location, current_time = queue.pop(0)

        for dr, dc in [(1,0), (-1,0), (0,1), (0, -1)]:        

            next_location = (current_location[0] + dr, current_location[1] + dc)
                    
            # next location must be valid location & unvisited & must conatin a fresh orange.
            if is_valid_location(next_location) and next_location not in visited and grid[next_location[0]][next_location[1]] == 1:        
                    
                queue.append((next_location, current_time + 1))   
                visited.add(next_location) 
                grid[next_location[0]][next_location[1]] = 2 # mark orange rotten 
                fresh_oranges -= 1         

    # check if any more fresh oranges left.
    if fresh_oranges > 0:
        return -1

    return current_time

    
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
grid = [[0]]
grid = [[1],[2],[2]]
grid = [[2,2,1,1,1,1],[0,0,2,0,1,0],[2,0,0,0,2,2],[0,2,1,0,1,0],[2,0,1,2,1,2],[0,0,2,1,0,0],[2,1,1,2,2,1]]
time = oranges_rotting(grid)
print(time)
