class Node:
    def __init__(self,data=None,next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        # print(node.data)
        # print(self.head)
        self.head = node
        

    def print(self):
        itr = self.head
        print(itr)
        llstr = " "
        while itr:
            suffix = " "
            if itr.next:
                suffix = "-->"
            print(str(itr.data))
            llstr += str(itr.data) + suffix
            itr = itr.next
            print(itr)
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self,index,data):
        if index < 0 or index > self.get.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return 

a = LinkedList()
a.insert_at_begining(10)
a.insert_at_begining(20)
a.insert_at_begining(30)
a.print()