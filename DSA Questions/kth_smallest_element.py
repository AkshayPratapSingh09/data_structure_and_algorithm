arr = [7 ,10, 4, 3, 20, 15]
arr3 = [7 ,10 ,4 ,20 ,15]
arr.sort()
arr3.sort()
# k = int(input("Enter the kth number: "))
k2 = int(input("Enter the kth number: "))
# arr2 = list(enumerate(arr,start = 1))
arr4 = list(enumerate(arr3,start = 1))
# print(arr2)
# print(arr3)
# print("Kth smallest number:",arr2[k-1][1])
print("Kth smallest number:",arr4[k2-1][1])
