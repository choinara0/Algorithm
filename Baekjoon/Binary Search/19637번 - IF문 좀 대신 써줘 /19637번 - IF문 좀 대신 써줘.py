import sys
input = sys.stdin.readline

def binary_search(n):
    left, right = 0, len(arr) - 1
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if int(arr[mid][1]) >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer

N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]
for _ in range(M):
    num = int(input())
    print(arr[binary_search(num)][0])