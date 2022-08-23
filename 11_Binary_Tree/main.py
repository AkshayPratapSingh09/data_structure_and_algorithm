class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.data = value

class Tree:
    def createNode(self,data):
        return Node(data)
# a = Tree
# print(a.createNode(10,20))
# print(a.Node.value)

    def insert(self,node,data):
        if Node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
            return Node

