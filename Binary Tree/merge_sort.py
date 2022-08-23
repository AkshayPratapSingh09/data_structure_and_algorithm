def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        # print(left_arr)
        right_arr = arr[len(arr)//2:]
        # print(right_arr)

        # Now We will Make all subarrays using recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        print(left_arr)
        print(right_arr)

        #Will merge now and will bind them according to the condition 
        i = 0
        j = 0
        k = 0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
               
            else:
                arr[k] = right_arr[k]
                j+=1
            k+=1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

        

arr = [33,21,45,56,67,78,23,14]
merge_sort(arr)
print(arr)