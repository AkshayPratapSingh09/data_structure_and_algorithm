def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i -1):
            print("i =",i,"j =",j)
            if arr[j]>arr[j+1]:
                print(f"{arr[j]} replaced with {arr[j+1]}")
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

            # print("j =",j)

data = [-2, 45, 0, 11, -9]
# print(len(data))
# print(len(data) -1)    
print(bubble_sort(data))