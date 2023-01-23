def pow(num,p):
    if p<1:
        return 1
    return num * pow(num,p-1)

print(pow(2,10))