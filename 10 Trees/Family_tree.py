class treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    balli = treenode("Balli Singh")

    ramkaran = treenode("RamKaran Singh")
    Rajaram = treenode("Raja Ram Singh")
    ramkaran.add_child(Rajaram)
    Lalji = treenode("Lalji Singh")
    ramkaran.add_child(Lalji)
    # laptop.add_child(treenode("Thinkpad"))

    x = treenode("X Singh")
    x.add_child(treenode("Rajendra Singh"))
    x.add_child(treenode("Nalni Singh"))
    x.add_child(treenode("Shambhu Singh"))
    x.add_child(treenode("Y Singh"))
    # cellphone = treenode("X Singh")

    
    a = treenode("Avinash Kumar Singh") 
    b = treenode("Ajay Kumar Singh")
    Lalji.add_child(a)
    Lalji.add_child(b)

    c = treenode("Ajeet Kumar Singh") 
    Rajaram.add_child(c)
    c = treenode("Arun Kumar Singh") 
    Rajaram.add_child(c)
    c = treenode("Anjani Kumar Singh") 
    Rajaram.add_child(c)
    c = treenode("Abhay Kumar Singh") 
    Rajaram.add_child(c)
    c = treenode("Sanjay Kumar Singh") 
    Rajaram.add_child(c)
    # cellphone.add_child(treenode("Rajendra Singh"))
    # cellphone.add_child(treenode("Nalni Singh"))
    # cellphone.add_child(treenode("Shambhu Singh"))
    # cellphone.add_child(treenode("Y Singh"))

    
    # tv = treenode("TV")
    # tv.add_child(treenode("Samsung"))
    # tv.add_child(treenode("LG"))
    # tv.add_child(treenode("Sony"))

    balli.add_child(ramkaran)
    balli.add_child(x)
    # root.add_child(tv)

    # return root

# def print_tree(self):
#     print(self.data)
#     for child in self.children:
#         child.print_tree
    balli.print_tree()



# a = build_product_tree()
# a = treenode(20)
# b = treenode()
# a.add_child(b)
# print(b.parent)
# print(a.data)
# print(a.print_tree())
# b = a.build_product_tree
build_product_tree()

# print(a.build_product_tree.root.data)