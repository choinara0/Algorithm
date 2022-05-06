import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
left, right = 1, max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    people = 0
    for n in arr:
        people += (n // mid)

    if people < K:
        right = mid - 1
    else:
        left = mid + 1
        answer = mid

print(answer)