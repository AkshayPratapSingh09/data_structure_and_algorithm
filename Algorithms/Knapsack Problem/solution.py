val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
maxval = 0
for i in range(len(val)):
    for j in range(i,len(val)):
        cur = wt[i:j]
        print(cur," ",sum())
        cur_sum = sum(wt[i:j])
        if cur_sum<W:
            maxval = max(maxval, sum(val[i:j]))

print(maxval)