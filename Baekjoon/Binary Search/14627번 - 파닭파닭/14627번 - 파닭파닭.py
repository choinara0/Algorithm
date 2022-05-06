import sys
input = sys.stdin.readline

S, C = map(int, input().split())
arr = [int(input()) for _ in range(S)]
left, right = 1, max(arr)
result = 0
answer = 0
while left <= right:
    mid = (left + right) // 2
    chicken = 0

    for n in arr:
        chicken += (n//mid)

    if chicken < C:
        right = mid - 1
    else:
        left = mid + 1
        result = mid

answer = sum(arr) - (C *result)
print(answer)