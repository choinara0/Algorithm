import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
left, right = 0, max(arr)*M

while left <= right:
    mid = (left + right) // 2
    time = 0
    for i in arr:
        time += (mid//i)

    if time >= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)