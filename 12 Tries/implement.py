#We will make a node consisting of all the child 
#self.children -->It can contain 26 children 
#We will add children as a hashmap to access them more efficiently
# Children["a"] = Trienode()
# In this form we will be adding the nodes
#We need Self.enfOfWord--> to determine the end of the word


class trienode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class trie:
    def __init__(self):
        self.root = trienode()

    def insert(self,word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                 cur.children[c] = trienode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self,word):
        cur = self.root 

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
    
    def startswith(self,prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

Trie = trie()
Trie.insert("apple")
Trie.search("apple")
print(Trie.search("app"))
print(Trie.startswith("app"))
print(Trie.insert("app"))
Trie.search("app")
print(Trie.root.children.keys)