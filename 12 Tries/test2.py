
class trienode:
    def __init__(self,char):
        self.child = {}
        self.isEndOfWord = False
        self.char = char
        self.counter = 0

    
class Trie:

    def __init__(self):
        self.root = trienode("")

    def insert(self,word):
        node = self.root

        for char in word:
            if char in node.child:
                node = node.child[char]

            else:
                new_node = trienode(char)
                node.child[char] = new_node
                node = new_node

        node.isEndOfWord = True
    
    def dfs(self,node,prefix):

        if node.isEndOfWord:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child)
    