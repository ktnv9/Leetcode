
def valid_path_bfs(edges, source, destination):

    # dictionary to store adjacency list
    graph = {}
    for edge in edges:
        u, v = edge[0], edge[1]
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    # handle invalid source, destination nodes.
    if source not in graph or destination not in graph:
        return False
    
    # use bfs traversal to check if destination can be reached from the source.
    queue = [source]
    visited = set([source])
    while queue:
        first = queue.pop(0)

        # check if destination is reached.
        if first == destination:
            return True
        
        for neighbour in graph[first]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

    return False

edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

is_valid = valid_path_bfs(edges, source, destination)

print(is_valid)