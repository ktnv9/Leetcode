
def equal_rows_colums(grid):

    # convert columns to tuples to store them as keys in a dictionary; values are their frequency. 
    column_counts = {}
    for col_index in range(len(grid[0])):

        # obtain the column as a tuple & store the column & its frequency in the dictionary.
        column = tuple([grid[row_index][col_index] for row_index in range(len(grid))])
        if not column in column_counts:
            column_counts[column] = 1
        else:
            column_counts[column] += 1

    # check if row is present in the column counts dictionary and increment the pairs count. 
    pairs_count = 0
    for row_index in range(len(grid)):

        row = tuple(grid[row_index])
        if row in column_counts:
            pairs_count += column_counts[row]
    
    return pairs_count

        



    '''
    pairs_count = 0
    for row_index in range(len(grid)):

        for col_index in range(len(grid[0])):

            match_found = True
            for k in range(len(grid)):
                if not grid[row_index][k] == grid[k][col_index]:
                    match_found = False
                    break
            if match_found:
                pairs_count += 1

    return pairs_count
    '''

    '''
    def get_columns():

        def get_column(col_index):

            column = []
            rows_count = len(grid)
            for row_index in range(rows_count):
                column.append(grid[row_index][col_index])
            return column

        columns = []
        columns_count = len(grid[0])

        for col_index in range(columns_count):
            column = get_column(col_index)
            columns.append(column)
        return columns 

    columns = get_columns()
    
    equal_pairs_count= 0
    for row in grid:
        for col in columns:
            if row == col:
                equal_pairs_count+=1
    
    return equal_pairs_count
    '''

grid = [[3,2,1],[1,7,6],[2,7,7]]
# grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
equal_pairs = equal_rows_colums(grid)
print(equal_pairs)
