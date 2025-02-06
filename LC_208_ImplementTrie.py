class TrieNode:
    
    # A node in Trie data structure
    
    # children --> dictionary; isEndNode --> indicates leaf node.
    # character is stored as key in the dictionary.
    def __init__(self):
        self.children = {}
        self.isEndNode = False

class Trie:
 
    def __init__(self):
        
        # initialize with a root node
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        
        # point the curr_node to root.
        curr_node = self.root
        
        for c in word:
        
            # if the current character in the word is not in the children
            # add the current character as the key and value as a new trie node.
            if not c in curr_node.children:
                curr_node.children[c] = TrieNode()
                
            # Move the pointer to the child.
            curr_node = curr_node.children[c]
            
        # Mark the last node as leaf.
        curr_node.isEndNode = True
    
    def search(self, word: str) -> bool:
        
        # point the curr_node to root.
        curr_node = self.root
        
        for c in word:
        
            # if the current character is not found in the children, return False.
            # indicating that the word is not found.
            if not c in curr_node.children:
                return False
                
            # Move the pointer to the child.
            curr_node = curr_node.children[c]
            
        # Return True if the curr_node is end node.
        return curr_node.isEndNode

    def startsWith(self, prefix: str) -> bool:
        
        # point the curr_node to root.
        curr_node = self.root
        
        for c in prefix:
        
            # if the current character is not found in the children, return False.
            # indicating that the prefix is not found.
            if not c in curr_node.children:
                return False
                
            # Move the pointer to the child.
            curr_node = curr_node.children[c]
            
        # return True if all the characters in the prefix are found in the Trie.
        return True