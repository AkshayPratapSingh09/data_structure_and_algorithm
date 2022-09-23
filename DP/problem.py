def solution(arr):
    if len(arr) == 0: return 0

    min_sum_element = [arr[0]]
    min_sum = arr[0]

    for i in range(1,len(arr)):
        num = arr[i]
        print("nuum here is",num)
        cur_min = min(num, num + min_sum_element[i-1])
        print("Cur Min here is",cur_min)
        min_sum_element.append(cur_min)
        print("Elements in min: ",min_sum_element)
        min_sum = min(min_sum, cur_min)
        print("Min Sum",min_sum)
    return min_sum, min_sum_element

arr = [20, -7, -3, 9, -4, 6, -9, 10]

print(solution(arr))
