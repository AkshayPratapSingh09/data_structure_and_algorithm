a = [1,2,3,4,5]
b = [5,6,7,8,9]
class merge1:
    def __init__(self,list1,list2):
        self.data1 = list1
        self.length1 = len(list1)
        self.data2 = list2
        self.length2 = len(list2)

    def prnt(self):
        return list(set(self.data1 + self.data2))

c = merge1(a,b)
print(c.prnt())
