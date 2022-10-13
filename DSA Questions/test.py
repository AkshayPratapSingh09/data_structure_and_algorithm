def searchInsert(nums,target):


        for i in range(len(nums)):
            print(f"Checking if {nums[i]} == {target}")



            if nums[i]==target:
                print(f"Here I found the number at {i}")
                break



            if nums[i]>target:
                print(f"Couldn't found the number but got a higher number at {i}")
                break
        else: 
            print(len(nums))


nums = [1,2,3,4,5,6,7,8,9]
target = 9

searchInsert(nums,target)
