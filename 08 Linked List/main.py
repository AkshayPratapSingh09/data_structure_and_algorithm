#-->Will Make each node for the combining in the final Linked List
class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

#--> Actual Linked List Instance
class linked_list:
    def __init__(self):
        self.head = node()

#--> Will add node at the end of the linked list 
#       ->1st_data = None
#       ->1st_next = new_node

# -------Updated after the loop checks till next is not None for the end------------------#

#       ->Added_data = data
#       ->Added_next = Next 
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

#-->Will Calculate the total number of nodes in the Linked List
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total +=1
            cur=cur.next
        return total

#-->Will Print all the Elements in the Linked List
    def print(self):
        cur = self.head
        while cur.next != None:
            print(cur.next.data)
            cur = cur.next
        
#-->Will search for the given data in the nodes      
    def search(self,data):
        ser = self.head
        loc = 0
        while ser.next != None:
            if ser.data == data:
                print(f"Found data at location at position {loc}")
                ser.data = data
                break
            ser = ser.next 
            loc += 1

        
    def get(self,index):
        if index >= self.length() or index<0:
            print("Not in Range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx==index:
                return cur_node.data
            cur_idx += 1

    def erase(self,index):
        if index>=self.length() or index<0:
            print("Not in Range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx ==index:
                last_node.next = cur_node.next
                return
            cur_idx += 1    
        
        

            
a = linked_list()
a.append(20)
a.append(30)
a.append(40)
a.append(50)
# a.print()
# print(a.length())
# a.search(40)
print(a.get())

    