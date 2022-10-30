




# class trienode:
#     def __init__(self):
#         self.child = [None]*26
#         self.isEndOfWord = False


# class trie:
#     def __init__(self):
#         self.root = self.getNode()
    
#     def getNode(self):
#         return trienode()

#     def _chartoIndex(self,ch):
#         return ord(ch) - ord("a")

#     def insert(self,key):
#         new_word = self.root
#         length = len(key)
#         for level in range(length):
#             index = self._chartoIndex(key[level])

#             if not new_word.child[index]:
#                 new_word.child[index] = self.getNode()
#             new_word = new_word.child[index]

#         new_word.isEndOfWord = True

# def main():
    
#     Strings = ["Amongst", "Enlarging", "Kinetic", "Among","Amature","Entitlement"]
#     output = ["Present", "Absent"]

#     t = trie()
#     for key in Strings:
#         t.insert(key)

# if __name__ == "__main":
#     main()
