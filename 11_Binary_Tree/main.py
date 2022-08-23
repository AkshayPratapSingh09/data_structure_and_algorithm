class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.data = value

class Tree:
    def createNode(self,data):
        return Node(data)
a = Tree
print(a.createNode(10,20))
print(a.Node.value)