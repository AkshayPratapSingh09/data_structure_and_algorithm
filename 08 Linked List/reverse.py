class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def addchild(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode

        else:
            par = self.head
            while par.next is not None:
                par = par.next
            par.next = newnode

    def print(self):
        par = self.head
        while par is not None:
            print(par.data)
            par = par.next

    def reverse(self):
        prev, curr = None, self.head
        while  curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
         



a = Linkedlist()
a.addchild(10)
a.addchild(20)
a.addchild(30)
a.addchild(40)
a.addchild(50)
# a.reverse()
a.print()