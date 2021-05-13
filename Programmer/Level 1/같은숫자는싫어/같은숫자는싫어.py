def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, int(len(arr))):
       if arr[i] != arr[i-1]:
           answer.append(arr[i])
    return answer
'''
1 1 3 3 0 1
1 1 3 3 0 1
'''
