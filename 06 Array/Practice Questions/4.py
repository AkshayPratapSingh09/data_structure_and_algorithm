
#4. Given two arrays a[] and b[] of size
#   n and m respectively. The task is to 
#   find union between these two arrays.

#   Union of the two arrays can be defined 
# as the set containing distinct elements 
# from both the arrays. If there are 
# repetitions, then only one occurrence 
# of element should be printed in the union

l1 = [1,2,3,44,5,6,7,8]
l2 = [8,3,5,66,77,99,101]

def solution(l1,l2):
    l3 = l1 + l2
    l3 = list(set(l3))
             

