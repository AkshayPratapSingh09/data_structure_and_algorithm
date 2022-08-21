# Stacks are Implemented in Python Using List and Deque Library
# LIFO --> "Last In First Out"
# Redo is Done using Stacks


s = []
s.append("akshay")
s.append("arpan")
s.append("Arman")
s.append("fisul")
# print(s)
# s.pop( )
# s.pop( )
# s.pop( )
# s.pop( )
# s.pop( )

#-->We donot prefer to use array to apply stack
#   cause They increase the shelf my same length
#   Eg :  len(a)=10  ---> New Len(a)=20 
#   And then only array will implement the change

from collections import deque
# stack = deque()
# print(dir(stack))

#--> Deque use Double Linked List(Forward/Backward Pointer)
#--> quite Similar to list

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        return self.container.append(val)

    def pop(self,val):
        return self.container.pop()

    def peek(self,val):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

a = Stack()
a.push(20)
a.push(30)
a.push(40)
print(a.container)

