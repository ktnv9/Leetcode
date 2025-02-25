
# input: list of edges

# stack to traverse the graph.
# visited set to capture visited nodes.
# counter to keep track of edges to be reversed.
# function: given u, get the unvisited node v such that u->v edge exists
# function: given u, get the unvisited node v such that v->u edge exists


connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]



def reorder_routes(connections, destination):

    if connections == []:
        return 0

    def unvisited_neighbour(node, dict_neighbours, visited):
        if node in dict_neighbours:
            for neighbour in dict_neighbours[node]:
                if neighbour not in visited:
                    return neighbour
        return None

    dict_forward_neighbours = {}
    dict_backward_neighbours = {}
    for edge in connections:
        if edge[0] not in dict_forward_neighbours:
            dict_forward_neighbours[edge[0]] = [edge[1]]
        else:
            dict_forward_neighbours[edge[0]].append(edge[1])

        if edge[1] not in dict_backward_neighbours:
            dict_backward_neighbours[edge[1]] = [edge[0]]
        else:
            dict_backward_neighbours[edge[1]].append(edge[0])
        
    stack = [destination]
    visited = set()
    visited.add(destination)
    reorder_edge_count = 0
    while stack:

        top = stack[-1]
        unv_node = unvisited_neighbour(top, dict_forward_neighbours, visited)
        if unv_node:
            reorder_edge_count += 1
            stack.append(unv_node)
            visited.add(unv_node)
        else:
            unv_node = unvisited_neighbour(top, dict_backward_neighbours, visited)
            if unv_node:
                stack.append(unv_node)
                visited.add(unv_node)
            else:
                stack.pop()

    return reorder_edge_count

connections = [[1,0],[1,2],[3,2],[3,4]]
connections = [[1,0],[2,0]]
connections = [[1,0]]
reorder_count = reorder_routes(connections, 0)
print(reorder_count)