class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

# class tree:
#     def __init__(self):
#         self.root = None

#     def root(self):
#         return self.root

#     def addchild(self,data):
#         if self.root is None:
#             self.root = node(data)
#         else:
#             self.add()

 # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

def printPostorder(root):
    if root:


        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val)


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

# print("Pre order Traversal: ", end="")
# root.traversePreOrder()
# print("\nIn order Traversal: ", end="")
# root.traverseInOrder()
# print("\nPost order Traversal: ", end="")
# root.traversePostOrder()
printPostorder(root)