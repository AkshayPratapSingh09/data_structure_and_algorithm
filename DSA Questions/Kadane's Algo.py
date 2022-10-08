arr = [-5,4,6,-3,4,-1]

def maxsum(arr):
    sum_max = 0
    cur_sum = 0
 
    for i in range(len(arr)):
        print("Current Sum is",cur_sum)
        cur_sum = cur_sum+arr[i]
        print("Current Sum after op is",cur_sum)
        
        if (cur_sum>sum_max):
            sum_max = cur_sum
            print("Max Sum updated =",sum_max)

        if cur_sum<0:
            print("Current Sum updated to 0")
            cur_sum=0
    
    return sum_max
print(maxsum(arr))
