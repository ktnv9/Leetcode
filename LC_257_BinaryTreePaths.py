
class BinaryTreeNode:

    # initializes a binary tree node | set left and right as None by default.
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # checks if given binary tree node is a leaf (i.e., node with no children)
    def is_leaf(self):
        return not self.left and not self.right
    
class BinaryTree:

    # takes a list of values as input and constructs binary tree.
    def __init__(self, tree_values):
        self._tree_values = tree_values
        self.root = self._build_tree()

    # constructs binary tree
    def _build_tree(self):

        # handle empty input case.
        if not self._tree_values:
            return None

        # create nodes and store them in a list. 
        nodes = [BinaryTreeNode(val) if val else None for val in self._tree_values]
        
        num_elements = len(self._tree_values)

        # construct the connections | for a node at index i, the left node is at index 2*i+1; and right node at 2*i+2.
        for index in range(num_elements):

            if nodes[index]: #skip None values

                # connect the left node.
                left_index = (2 * index) + 1
                if left_index < num_elements:
                    nodes[index].left = nodes[left_index]
            
                # connect the right node.
                right_index = (2 * index) + 2
                if right_index < num_elements:
                    nodes[index].right = nodes[right_index]

        # return the root of the binary tree.
        return nodes[0]
    
    def get_paths(self):

        # list to store the paths.
        paths = []
        
        # construct a path using backtracking technique
        def construct_path(path, root):
            
            # handle edge case.
            if not root:
                return
            
            # add the node to path
            path.append(str(root.val))

            # base case: if root is leaf, then store the path & return
            if root.is_leaf():
                
                # make sure to strip off the '->' at the beginning of the path.
                paths.append("->".join(path))
            else:
            
                # move left to construct the path using recursion.
                construct_path(path, root.left)

                # move right to construct the path using recursion.
                construct_path(path, root.right)

            path.pop() # remove the appended node to back track to the parent.


        # intially the path is an empty list & the path begins at the root of the binary tree.
        construct_path([], self.root)

        # return the paths list.
        return paths
    
root = [1,2,3,None,5]
#root = [1]
#root = [1,None,3,None,None,6,7]
bin_tree = BinaryTree(root)
paths = bin_tree.get_paths()

print(paths)
