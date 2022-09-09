import random as rand
a = []
for i in range(10):
    a.append(rand.randint(1,100))

print(a)
b = 0
sum = 0
def summ(list,a):
    while a < len(list):
        global sum
        sum += list[a]
        # print(sum)
        return (summ(list,a+1))
    return sum

print(summ(a,b))
# print(sum(a))
    