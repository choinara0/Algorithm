n = int(input())
left, right = 0, n
answer = right

while left <= right:
    mid = (left + right) // 2

    if mid ** 2 <= n:
        left = mid + 1
        answer = left
    else:
        right = mid -1

print(answer)