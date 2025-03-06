def find_missing_repeated_values(grid):

    n = len(grid)**2
    
    ideal_sum = n*(n+1)//2
    ideal_sq_sum = n*(n+1)*(2*n+1)//6
    
    grid_sum = 0
    grid_sq_sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid_sum += grid[row][col]
            grid_sq_sum += grid[row][col]**2

    minus_ab = grid_sum-ideal_sum
    minus_sq_ab = grid_sq_sum-ideal_sq_sum
    plus_ab = minus_sq_ab // minus_ab

    a = (plus_ab + minus_ab)//2
    b = (plus_ab - minus_ab)//2

    return [a,b]

grid = [[1,3],[2,2]]
grid = [[9,1,7],[8,9,2],[3,4,6]]
dup_miss = find_missing_repeated_values(grid)
print(dup_miss)