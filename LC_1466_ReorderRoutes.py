
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

def reorder_routes(connections, destination):

    # handle invalid input case
    if connections == []:
        return 0

    # get unvisited neighbour of a node.
    def unvisited_neighbour(node, dict_neighbours, visited):
        if node in dict_neighbours:
            for neighbour in dict_neighbours[node]:
                if neighbour not in visited:
                    return neighbour
        return None

    
    dict_forward_neighbours = {} # adjacency list (graph) to keep track of forward edges.
    dict_backward_neighbours = {} # adjacency list (graph) to keep track of backward edges.
    
    # construct adjaceny lists.
    for edge in connections:
        if edge[0] not in dict_forward_neighbours:
            dict_forward_neighbours[edge[0]] = [edge[1]]
        else:
            dict_forward_neighbours[edge[0]].append(edge[1])

        if edge[1] not in dict_backward_neighbours:
            dict_backward_neighbours[edge[1]] = [edge[0]]
        else:
            dict_backward_neighbours[edge[1]].append(edge[0])
    
    stack = [destination] # stack to traverse the graph.
    visited = set() # set to capture visited nodes.
    visited.add(destination) # mark the destination node visited.
    reorder_edge_count = 0 # counter to keep track of edges to be reorderd.
    
    # traverse the graph using dfs
    while stack:

        top = stack[-1]

        # if unvisited forward neighbour is available, then increment the reorder count.
        unv_node = unvisited_neighbour(top, dict_forward_neighbours, visited)
        if unv_node:
            reorder_edge_count += 1

            stack.append(unv_node) # push the neighbour to stack.
            visited.add(unv_node) # mark the neighbour visited.

        else:

            # if forward neighbour is not availble, look for unvisited backward neighbour 
            unv_node = unvisited_neighbour(top, dict_backward_neighbours, visited)
            if unv_node:
                
                # push the neighbour to the stack and mark it visited.
                stack.append(unv_node)
                visited.add(unv_node)

            else:

                # if forward/backward neighbours are all visited, then pop the stack for dfs to traverse the other routes.
                stack.pop()

    return reorder_edge_count

connections = [[1,0],[1,2],[3,2],[3,4]]
connections = [[1,0],[2,0]]
connections = [[1,0]]
reorder_count = reorder_routes(connections, 0)
print(reorder_count)