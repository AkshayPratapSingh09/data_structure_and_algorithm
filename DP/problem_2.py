# ques::

# Given an  integer n, return the minimum
# steps to minimize n to 1

# Available Steps are::
# -->Decrement n by 1:
# -->If n is divisible by 2, then divide n by 2
# -->If n is divisible by 3, then divide n by 3




num = 45
count = 0

def solution(num):
    
    global count

    if num<2:
        return num

    elif num%3 == 0:
        num = num/3
        count += 1
        return solution(num)
    
    elif num%2 == 0:
        num = num/2
        count += 1
        return solution(num)
    return count + 1

print(solution(15))

    
    
