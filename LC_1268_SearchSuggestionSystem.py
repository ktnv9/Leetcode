
'''
    Approach1 : Using Dictionary<Prefix, List of Words>
'''
def suggestedProducts(products, searchWord):
    
    dict_prefix_suggestions = {}

    for product in products:

        prefix = ''
        for c in product:
            prefix += c
            if prefix in dict_prefix_suggestions:
                dict_prefix_suggestions[prefix].append(product)
            else:
                dict_prefix_suggestions[prefix] = [product]

    prefix = ''
    prefix_suggestions = []
    for letter in searchWord:
        prefix += letter
        if prefix in dict_prefix_suggestions:
            suggestions = dict_prefix_suggestions[prefix]
            suggestions.sort()
            if len(suggestions) > 3:
                prefix_suggestions.append(suggestions[:3])
            else:
                prefix_suggestions.append(suggestions)
        else:
            prefix_suggestions.append([])

    return  prefix_suggestions


'''
    Approach2: Using Trie Data Structure to store the words and suggestions at each node.
'''

class TrieNode:

    def __init__(self):
        self.children = {}
        self.prefix_words = []
        self.isEndNode = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode()
            curr_node.prefix_words.append(word)
            curr_node = curr_node.children[letter]
        curr_node.prefix_words.append(word)
        curr_node.isEndNode = True
        
    def get_prefix_words(self, prefix):
        curr_node = self.root
        for letter in prefix:
            if letter not in curr_node.children:
                return []
            curr_node =  curr_node.children[letter]
        return curr_node.prefix_words

def suggestedProducts(products, searchWord):
    
    trie = Trie()
    for product in products:
        trie.insert(product)

    prefix = ''
    prefix_suggestions = []
    for letter in searchWord:
        prefix += letter
        suggestions = trie.get_prefix_words(prefix)
        suggestions.sort()
        prefix_suggestions.append(suggestions[:3])

    return prefix_suggestions

products = ["havana"]
searchWord = "tatiana"

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
prefix_suggestions = suggestedProducts(products, searchWord)

print(prefix_suggestions)