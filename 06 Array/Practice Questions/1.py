# 1.Write a Python program to find the
# missing number in a given array of 
# numbers between 10 and 20.
# Original array: 10 11 12 13 14 16 17 18 19 20

array =  [10 ,11 ,12 ,13 ,14 ,16 ,17 ,18 ,19 ,20]
for i in range(11,21):
    if i in array:
        print(f"found {i} in array")
    else:
        print(f"Didn't Found {i} in array")
        