class LetterNode:

    def __init__(self):
        self.children = {}
        self.isEndNode = False

class WordDictionary:

    def __init__(self):
        self.root = LetterNode()
        
    def addWord(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = LetterNode()
            curr_node = curr_node.children[letter]
        curr_node.isEndNode = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for letter in word:
            
            if letter == ".":
                if not curr_node.children == {}:
                    curr_node = list(curr_node.children.values())[0]
                else:
                    return False
            else:
                if letter not in curr_node.children:
                    return False
                curr_node = curr_node.children[letter]
        return curr_node.isEndNode
    
instructions_list = ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
input_list = [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

for indx, instruction in enumerate(instructions_list):
    if instruction == "WordDictionary":
        wd = WordDictionary()
    if instruction == "addWord":
        wd.addWord(input_list[indx][0])
    if instruction == "search":
        chk = wd.search(input_list[indx][0])
        print(f"input = {input_list[indx][0]}, output = {chk}")
    