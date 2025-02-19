class TreeNode:
    pass

class Tree:

    def __init__(self):
        self.root = None

    def arc_traversal(self):

        dict_level_nodes = {}

        Q = [self.root]
        level = 1
        dict_level_nodes[level] = self.root
        
        while Q:

            top = Q.pop(-1)
            for child in top.children:
                Q.appned(child)



