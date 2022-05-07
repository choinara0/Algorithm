import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
answer = 0
left, right = arr[0], arr[-1]

while left <= right:
    mid = (left + right) // 2
    sum_level = 0

    for i in arr:
        if i >= mid:
            break
        sum_level += (mid-i)

    if sum_level <= K:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)