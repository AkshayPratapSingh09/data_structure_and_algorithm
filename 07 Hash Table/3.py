
class hash:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def prnt(self):
        return dict(zip(self.key,self.value))


import random
names = []
num = []
with open("nameslist.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
for i in range(10):
    f = random.randint(0,3000)
    a = words[f]
    num.append(f)
    names.append(a)
# print(names)

h = hash(names,num)
print(h.prnt())
