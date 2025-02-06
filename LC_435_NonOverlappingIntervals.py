
class GraphNode:
    def __init__(self, id):
        self.id = id
        self.children = {}

    def adj_nodes_count(self):
        return len(self.children)
    
class Graph:
    def __init__(self):
        self._dict_id_node = {}

    def add_node(self, node, parent):
        if parent is not None:
            parent.children[node.id] = node
        if node.id not in self._dict_id_node:
            self._dict_id_node[node.id] = node

    def remove_node(self, id):
        for adj_node in list(self._dict_id_node[id].children.values()):
            del adj_node.children[id]
        del self._dict_id_node[id]
    
    def print_graph(self):
        for id in self._dict_id_node:
            print(id)
            for child_key in self._dict_id_node[id].children:
                print(" -->",child_key)

"""   
node1 = GraphNode(1)
node2 = GraphNode(2)

graph = Graph()
graph.add_node(node2, node1)
graph.add_node(node1, node2)

adj_nodes1 = node1.adj_nodes_count()
adj_nodes2 = node2.adj_nodes_count()

print(adj_nodes1, adj_nodes2)

print("-----------")
graph.print_graph()

graph.remove_node(2)

print("-----------")
graph.print_graph()
"""

intervals = [[1,2],[2,3],[3,4],[1,3]]

graph = Graph()

def intersecting_intervals(interval_a, interval_b):
    if (interval_a[1] < interval_b[0]) or (interval_b[0] < interval_a[1]):
        return False
    return True

num_intervals = len(intervals)

dict_id_children = {}

for indx_a in range(num_intervals):
    dict_id_children[indx_a] = []

for indx_a in range(num_intervals-1):
    interval_a = intervals[indx_a]
    for indx_b in range(1, num_intervals):
        interval_b = intervals[indx_b]

        if intersecting_intervals(interval_a, interval_b):
            dict_id_children[indx_a].append(indx_b)
            dict_id_children[indx_b].append(indx_a)
        
print(dict_id_children)

        

