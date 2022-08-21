class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        itr = self.head
        llstr = " "
        while itr:
            suffix = " "
            if itr.next:
                suffix = "-->"
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_end(self,data):
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)
        


a = LinkedList()
a.insert_at_begining(20)
a.insert_at_begining(30)
a.print()