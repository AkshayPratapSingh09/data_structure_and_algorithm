arr = [-5,4,6,-3,4,-1]
sum_max = 0
# print(sum(arr))
for i in range(len(arr)):
    for j in range(len(arr)):
        f = arr[i:j] 
        if sum(f)>sum_max:
            case = f
            sum_max = max(sum(f),sum_max)

print(case)
print(sum_max)


