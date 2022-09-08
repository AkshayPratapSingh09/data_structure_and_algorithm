class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def build_trees(self,data):
        root = node(data)
        
    def add_child(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    return
                else:
                    self.left.data = data
            else:
                if data > self.data:
                    if self.right:
                        return
                    else:
                        self.right.data = data
        else:
            self.data = data
            
            