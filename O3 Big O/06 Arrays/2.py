#we use List in python for array


a = [1,2,3,4,5] #-->List
print("Simple list\n",a)
a.append(67) #-->Will add at the end of the list
print("List after appending\n",a)

a.pop(3) #--> will remove 4th element(by index) from the list
print("List after removing element\n",a)

a.insert(4,"word") #--> Will add word at the 5th index position
print("List after adding 1 element\n",a)

a.remove(3)
print("List after removing 1 element\n",a)

b = ["Dog", "Cat", "Sheep"]
a.extend(b) #--> Will Merge 2 list of tuple,dict
print("List after merging 2 list\n",a)