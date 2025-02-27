
class Maze:

    def __init__(self, maze, entrance):
        self._maze = maze
        self._entrance = entrance
        self._rows_count = len(self._maze)
        self._cols_count = len(self._maze[0])
    
    def _is_wall(self, row, col):
        return self._maze[row][col] == "+"
    
    def _is_empty(self, row, col):
        return self._maze[row][col] == "."
    
    def _is_outside(self, row, col):
        return not (0 <= row < self._rows_count and 0 <= col < self._columns_count)
    
    def _is_exit(self, row, col):

        # exit = boundary cell & empty cell & not the entrance cell.
        return (row == 0 or row == self._rows_count-1 or col == 0 or col == self._columns_count-1) and self._is_empty(row,col) and \
                not (row == self._entrance[0] and col == self._entrance[1])

    def _is_valid_empty_cell(self, row, col):
        return not (self._is_outside(row, col) or self._is_wall(row, col))  and self._is_empty(row, col)

    def _get_unvisited_neighbour_cells(self, row, col, visited):
        potential_cells = [(row+1,col), (row-1,col),(row,col+1), (row,col-1)]
        unvisted_neighbours = []
        for potn_cell in potential_cells:
            if self._is_valid_empty_cell(potn_cell[0], potn_cell[1]) and potn_cell not in visited:
                unvisted_neighbours.append(potn_cell)
        return unvisted_neighbours


    def nearest_exit_steps_count(self):

        if not self._maze or not self._entrance:
            return -1
        
        entrance_row = self._entrance[0]
        entrance_col = self._entrance[1]
        if self._is_wall(entrance_row, entrance_col) or self._is_outside(entrance_row, entrance_col):
            return -1
        
        queue = [(entrance_row, entrance_col, 0)]
        visited = set()
        visited.add((entrance_row, entrance_col))

        while queue:

            current_row, current_col, steps_so_far = queue.pop(0)
            
            unvisited_neighbours = self._get_unvisited_neighbour_cells(current_row, current_col, visited)
            if unvisited_neighbours:
                for neighbour in unvisited_neighbours:
                    if self._is_exit(neighbour[0], neighbour[1]):
                        return steps_so_far + 1
                    queue.append((neighbour[0], neighbour[1], steps_so_far+1))
                    visited.add(neighbour)

        return -1


maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]

maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

maze = [[".","+"]]
entrance = [0,0]

maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".",".",".","+"],["+","+","+","+",".","+","."]]
entrance = [0,1]

maze_object = Maze(maze, entrance)
steps = maze_object.nearest_exit_steps_count()

print(steps)


    




