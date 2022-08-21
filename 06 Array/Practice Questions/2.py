# 2.Write a Python program to remove
#  all duplicate elements from a given
#   array and returns a new array.
a = [1,2,3,44,55,66,77,55,2,44,99,55,55,44,6]
print("Array Before Operation",a)
a = list(set(a))
print("Array After Operation",a)