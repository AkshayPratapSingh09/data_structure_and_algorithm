arr = [8,0,7,1,3]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1,len(arr)):
        print("i =",i,"j =",j)

        if arr[min_index] > arr[j]:
            min_index = j
            # temp = arr[min_index]
            arr[i] = arr[min_index]
            arr[min_index] = arr[i]
            print(arr[min_index])
            print(arr[i])
    #     # j += 1
    #     if arr[j] < min:
    #         min = arr[j]
    #         arr[i] = min
print(arr)