def recr(num1,num2):
    if num2 == 1:
        return num1
    else:
        return num1 + recr(num1,num2-1)

print(recr(4,5))