arr = [45,54,7,89,87,9,32,90,4,81,98]
x = 32
count =0
for i in arr:
    count +=1
    if i == x:
        print(f"Found {x} at",count-1)