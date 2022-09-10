
class treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    # def get_level(self):
    #     level = 0
    #     p = self.parent
    #     while p:
    #         level += 1

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def build_product_tree():
        root = treenode("Electronics")

        laptop = treenode("Laptops")
        laptop.add_child(treenode("MAC"))
        laptop.add_child(treenode("Surface"))
        laptop.add_child(treenode("Thinkpad"))

        cellphone = treenode("Cellphone")
        cellphone.add_child(treenode("Iphone"))
        cellphone.add_child(treenode("Google Pixel"))
        cellphone.add_child(treenode("Vivo"))

        tv = treenode("TV")
        tv.add_child(treenode("Samsung"))
        tv.add_child(treenode("LG"))
        tv.add_child(treenode("Sony"))

        root.add_child(laptop)
        root.add_child(cellphone)
        root.add_child(tv)

        return root

    def print_tree(self):
        self.build_product_tree()
        print(root.data)
        for child in self.children:
            child.print_tree()


# a = build_product_tree()
a = treenode(20)
b = treenode(30)
a.add_child(b)
# print(b.parent)
# print(a.data)
# print(a.print_tree())
a.build_product_tree
a.print_tree
# print(b)
# print(a.build_product_tree.root.data)