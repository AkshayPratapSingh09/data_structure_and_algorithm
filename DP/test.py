s = [-7,3,4,-2,-3,1,-3]
# for i in range(len(s)):
# a = 90
# b = 80
res = []
mins = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        mins = min(mins, sum(s[i:j]))
        res.append(sum(s[i:j]))
if 
print((res))
print(mins)