def fact(nums1):
    if nums1 == 1:
        return  1
    else:
        return nums1 * fact(nums1-1)
    
print(fact(5))

print("Solved")