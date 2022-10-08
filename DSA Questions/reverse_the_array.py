arr = [1, 2, 3]
# print(arr[::-1])

# Alternate Approach ::-
def reverse(arr,start,end):
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

print(reverse(arr,0,len(arr)-1))
