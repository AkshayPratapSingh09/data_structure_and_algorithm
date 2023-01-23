def recr(n):
    if n ==1:
        return n
    
    return n * recr(n-1)

print(recr(5))