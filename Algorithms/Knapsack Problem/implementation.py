def knapsack(capacity,weights,profits,n):
    if (n==0) or capacity==0:
        return 0
    
    if weights[n-1]>capacity:
        return knapsack(capacity,weights,profits,n-1)

    else:
        return max(profits[n-1]+knapsack(capacity-weights[n-1],weights,profits,n-1),knapsack(capacity,weights,profits,n-1))

print("Enter the profits:")
profits = list(map(int,input().split(" ")))
print("Enter the weights:")
weights = list(map(int,input().split(" ")))
capacity = int(input("Enter the maximum capacity:"))
n = len(weights)
print(knapsack(capacity,weights,profits,n))
