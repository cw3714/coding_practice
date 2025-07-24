def solution(n):
    arr = [[0 for i in range(n)] for j in range(n)] 
    for i in range(len(arr)):
        arr[i][i] = 1
    return arr