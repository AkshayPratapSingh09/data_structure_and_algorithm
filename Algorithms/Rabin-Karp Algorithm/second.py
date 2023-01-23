class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

btn = node(1)
btn1 = node(2)
btn2 = node(3)

btn.left = btn1
btn.right = btn2

def printtree(root):
    if root == None:
        return 
    print(root.data, end=": ")
    if root.left != None:
        print("L",root.left.data, end=" ")
    if root.right != None:
        print("R",root.right.data, end=" ")
    print()
    printtree(root.left)
    printtree(root.right)

printtree(btn)
