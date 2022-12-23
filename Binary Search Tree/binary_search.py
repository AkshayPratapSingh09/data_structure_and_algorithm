def search(nums,target):
    l = 0
    u = len(nums) - 1

    while l<=u:
        mid = (l+u)//2
        print("Mid here is",mid)

        if nums[mid] == target:
            print("Found answer")
            return mid+1
            break
        
        elif nums[mid] > target:
            u = mid-1

        else:
            l = mid+1

    if l>u:
        return False

arr = [45,56,76,78,79.89,90]
target = 76

print(search(arr,target))