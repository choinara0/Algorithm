import sys

M, N = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
left, right = 0, max(arr)
answer = 0

while left <= right:
    people = 0
    mid = (left + right) // 2
    if mid == 0:
        people = 0
        break

    for x in arr:
        if x >= mid:
            people += (x//mid)

    if people >= M:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)