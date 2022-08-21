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
print(names)
# pr



dict1 = dict(zip(num,names))
print(dict1)

