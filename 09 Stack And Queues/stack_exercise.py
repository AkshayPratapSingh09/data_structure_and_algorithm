# Problem 2
# Write a function in python that checks if paranthesis
# in the string are balanced or not. Possible parantheses 
# are "{}',"()" or "[]". Use Stack class from the tutorial.


# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

from collections import deque

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

    def reverse(self,str):
        return str[::-1]
    
    def para(self,str):
        a = str
        b = list(a)
        if ("[" in b and "]" in b):
            if (b.index("[") < b.index("]")):
                print("The string",a,"Balanced")

        elif ("{" in b and "}" in b):
            if (b.index("{") < b.index("}")):
                print("The string",a,"is balanced") 

        elif ("(" in b and ')' in b):
            if (b.index("(")< b.index(")")):
                print("The string",a,"is Balanced")

        else:
            print("The string",a,"is Unbalanced")

a = Stack()
print(a.reverse("We will conquere COVID-19"))
a.para("{a+b")