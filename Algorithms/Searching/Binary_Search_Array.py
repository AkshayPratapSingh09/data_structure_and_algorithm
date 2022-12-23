arr = [45,54,7,89,87,9,32,90,4,81,98]
arr.sort()
l = len(arr)
x = 32
first = 0
last = l-1
# def binary_search(arr,l,x):
while first <=last:
    mid = (first+last)//2
    if arr[mid]==x:
        print("Number found at",mid+1,"Location")
        break
    elif arr[mid]>x:
        last = mid-1
    else:
        first = mid+1
if first>last:
    print("Number not Available in the list")


    