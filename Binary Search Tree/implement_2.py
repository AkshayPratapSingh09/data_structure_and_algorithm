# def applyOperations(nums):
#     for i in range(len(nums)-1):
#         if nums[i] == nums[i+1]:
#             nums[i] = nums[i]*2
#             nums[i+1] = 0
#             return nums

# nums = [1,2,2,1,1,0]
# print(applyOperations(nums))

# a = []
# a.append(0)
# a.append(0)
# print(a)
nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
cout = 0
zeros = []

for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        nums[i] = nums[i]*2
        nums[i+1] = 0

for i in range(len(nums)-2):
    print(i)
    if nums[i] == 0:
        cout += 1
        nums.pop(i)
        zeros.append(0)
nums.extend(zeros)
print(nums)
nums.reverse()
print(nums)