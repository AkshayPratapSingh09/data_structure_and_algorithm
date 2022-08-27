class node:
    def __init__(self,data=None):
        self.data = data
        self.right = None
        self.left = None
    
    
    def add_child(self,data):
        # if data == self.data:
        #     return 
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.add_child(data)
                else:
                    self.left = node(data)
            else:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = node(data)
        else:
            self.data = data
            

    # def build_tree(self):
    #     data = input("Enter the data :")
    #     int(data)
    #     root = node(data)

    #     if data == -1:
    #         return None

    #     left = input("Enter the left data:")
    #     self.binary_tree()
    #     right = input("Enter the right data:") 
        
    #     return root

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def build_tree(self):
        data = int(input("Enter the data:"))
        root = node(data)

        if data == -1:
            return None
        print("Enter data for inserting in left of ", data)
        self.left = self.build_tree()
        print("Enter data for inserting in right of ", data)
        self.right = self.build_tree()
        return root



        



a = node(30)
# a.build_tree()
# a.add_child(20)
# a.add_child(45)
# a.add_child(30)
# print(a.left.data)
# print(a.right.data)
# print(a.left.data)
a.build_tree()
a.print_tree()
