import numpy as np

#Creating Array
a = np.array([1,2,3,4,5,6])
print(a)

#Appending IT --> format np.append(array, variable)
c = 45
b = np.append(a,c)
print(b)

#Deleting Items From Array --> format np.delete(array, index)
d = np.delete(a,3)
print(d)

#Deleting Items From Array By Value --> format np.delete(array, index)
#                                   --> Removes only first occurence

g = a.remove(3)
print(g)

#Adding Items in the Beginning Of Array --> format np.insert(array, index, element)
f = 62
e = np.insert(a,0,f)
print(e)

