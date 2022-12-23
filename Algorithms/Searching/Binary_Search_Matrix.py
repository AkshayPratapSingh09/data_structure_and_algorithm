def search(matrix,target):
    if len(matrix) == 0: return False 
    l = len(matrix)
    m = len(matrix[0])
    row, col = 0, m - 1
            
    while (row < l and col >= 0):
        if matrix[row][col] == target:
            return row,col
            break
        
        elif matrix[row][col] < target:
            row += 1
            
        else :
            col -= 1
            
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 20
row,col = search(matrix,target)
if search(matrix,target):
    print(f"Found {target} at [{row}] [{col}]")
else:
    print("Not Found")