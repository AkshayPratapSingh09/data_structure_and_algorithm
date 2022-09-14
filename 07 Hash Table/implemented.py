import random as rand

a = [rand.randint(0,100) for i in range(10)]
b = [i for i in range(10)]
print(a)

c = dict(zip(b,a))
print(c)
for k,j in c:
    print("Key:",k,"Value:",j)