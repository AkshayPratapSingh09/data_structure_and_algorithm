class node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.head = None

    # def takeinput(self,data):
    #     newnode = node(data)
    #     if self.head is None:
    #         self.head =  newnode

    #     else:
    #         par = self.head
    #         while par is not None:
    #             par = par.left 
    #         par = newnode

    def addelement(self,data):
        newnode = node(data)
        if self.head:
            par = self.head
            if data < par.data:
                print("Data")
    
    def print(self):
        par = self.head 
        while par:
            print(par.data)
            par = par.left        