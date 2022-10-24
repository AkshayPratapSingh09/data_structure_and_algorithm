# arr = [1,2,3,4,6,5,7,8,9,10]
# arr2 = [1,3,2,2,2,4,5,6]
# arr3 = [2,6,4,8,10,9,15]
# res = []
# max_val = 0
# print(arr)
# for i in range(len(arr)-1):
#     n = arr[i]
#     m = arr[i+1]
#     if n>m:
#         max_val=max(max_val,i)
#         res.append(i)
# print(res)
# print(max_val)
# print(arr[res[0]:res[-1]+1])
    

arr = [1, 4, 7, 3, 10, 48, 17, 26, 30, 45, 50, 62]
# start = arr[0]
oper = []
for i in range(0,len(arr)-1):
    m = arr[i]
    n = arr[i+1]
    print(f"{m} : {n}")
    # print(f" Numbers in op : {i} {i+1}")
    if n<m:
        arr[i],arr[i+1] =arr[i+1],arr[i]
        # print("Here replaced")
    n = m
    print(f"{m} : {n}")
print(arr)
