import math
def solution(arr):
    answer = []
    new_arr = []
    n = int(math.log2(len(arr)))
    for i in range(n):
        if sum(arr[i])==math.pow(2,n) or sum(arr[i]) == 0:

    return answer

solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])