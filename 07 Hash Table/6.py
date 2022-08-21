

a = [2,5,1,2,3,5,1,2,4]
def repeat_number(a):
    for i in range(len(a)-1):
        for j in range(len(a)):
             if a[i] == a[j]:
                print(i)
    return i

print(repeat_number(a))

