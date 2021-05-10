def solution(n, lost, reserve):
    answer = 0
    arr = [1 for i in range(n+2)]
    arr[0] = -1
    arr[n+1] = -1
    for i in reserve:
        if arr[i] == 1:
            arr[i] = 2

    for i in lost:
        arr[i] -=1


    for i in range(1, len(arr)):
        if arr[i] == 2 and arr[i-1] == 0:
            arr[i] -= 1
            arr[i-1] += 1
        elif arr[i] == 2 and arr[i+1] == 0:
            arr[i] -= 1
            arr[i+1] += 1
    for i in range(1, len(arr)-1):
        if arr[i] >=1:
            answer += 1
    return answer


solution(5, [2,4], [1,3,5])
