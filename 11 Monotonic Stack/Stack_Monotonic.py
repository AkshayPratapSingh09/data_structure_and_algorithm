def mono(insert_values):
    stack = []
    for entries in insert_values:
        if stack and stack[-1] <=entries:
            stack.insert(0,entries)
            print(stack)
        else:
            stack.append(entries)
    print(stack)

a = mono([1,2,3,76,43,4,54,67,89,5])
# # l.sort()
# print(l.insert(0,45))