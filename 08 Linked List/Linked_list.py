
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
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
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data)



if __name__=="__main__":
    root = LinkedList()
    # root.insert_at_beginning(5)
    # root.insert_at_beginning(10)
    # root.insert_at_beginning(15)
    root.insert_at_end(105)
    root.print()
# print(root.get_length())
