dict1 = {"Name": "Akshay", "Class":12, "School": "RRK"}

print("The name of the student is",dict1["Name"])
print("The class is",dict1["Class"])
print("The kid reads in",dict1["School"])

# dict2 = {"n"}

import random
a = []
for i in range(10):
    n = random.randint(0,100)
    a.append(n)

print(a)
b = []
for i in range(10):
    n = random.randstr("a","z")
    b.append(n)

print(b)

dict2 = dict(zip(a))
print(dict2)
