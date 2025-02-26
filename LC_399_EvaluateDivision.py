
def calc_equation(equations, values, queries):

    # weighted undirected graph to store the equations and evaluate expressions. 
    # nodes are variables in the equations.
    graph = {}

    for index, equation in enumerate(equations):

        numerator_variable = equation[0]
        denominator_variable = equation[1]
        division_value = values[index]

        # create forward edges with weights (weight of an forward edge = division value)
        if numerator_variable not in graph:
            graph[numerator_variable] = [(denominator_variable, division_value)]
        else:
            graph[numerator_variable].append((denominator_variable, division_value))

        # create backward edges with weights (weight of an backward edge = 1/division value)
        if denominator_variable not in graph:
            graph[denominator_variable] = [(numerator_variable, 1/division_value)]
        else:
            graph[denominator_variable].append((numerator_variable, 1/division_value))

    query_values = [] 
    for query in queries:

        numerator_variable = query[0]
        denominator_variabe = query[1]

        # handle the case where numerator or denominator is not in the graph
        if not ((numerator_variable in graph) and (denominator_variabe in graph)):
            query_values.append(-1)
            continue

        # traverse from source variable to destination variable using dfs, multiplying the edge weights on the way.
       
        source_variable = query[0]
        target_variable = query[1]

        target_found = False # to check if target is found during dfs traversal.
        query_value = 1  # to keep track of the query value so far on the dfs path.  

        stack = [(source_variable, 1)] # stack for dfs traversal

        visited = set() # dictioary to keep track of visited nodes
        visited.add(source_variable)
        while stack:

            top = stack[-1]
            current_variable = top[0]

            # stop when target variable is reached.
            if current_variable == target_variable:
                target_found = True
                break
            
            # find the unvisited neighbour of the top variable in the stack.
            unv_neighbour_found = False
            if current_variable in graph:
                for (neighbour_variable, division_value) in graph[current_variable]:
                    if neighbour_variable not in visited:

                        # append the neighbour &  to the stack along with
                        stack.append((neighbour_variable, division_value))
                        visited.add(neighbour_variable)

                        query_value *= division_value # multiply division value (weight of the edge) to compute query value obtained so far.
                        unv_neighbour_found = True
                        break

            # if neighbours are all visited, pop the stack to backtrack the graph
            if not unv_neighbour_found:
                popped = stack.pop()
                query_value *= 1/popped[1] # make sure to get rid the multiplied edge weight while back tracking

        # if target is reached, capture the query value; else output -1
        if target_found:
            query_values.append(query_value)
        else:
            query_values.append(-1)

    return query_values
        

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

'''
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]


equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
'''

equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]


values = calc_equation(equations, values, queries)
print(values)
