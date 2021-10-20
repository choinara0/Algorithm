import sys

N, K = int(sys.stdin.readline()), int(sys.stdin.readline())
start, end = 0, K

def binarySearch(N, K, start, end):

    answer = 0

    while start <= end:
        mid = (start + end) // 2
        temp = 0

        for i in range(1, N+1):
            temp += min(mid//i, N)

        if temp >= K:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

print(binarySearch(N, K, start, end))
