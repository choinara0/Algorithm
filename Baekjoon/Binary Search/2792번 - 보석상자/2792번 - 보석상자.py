import sys
import math

N, M = map(int, sys.stdin.readline().split())
jewels = [int(sys.stdin.readline()) for i in range(M)]
left, right = 1, max(jewels)
answer = sys.maxsize

while left <= right:
    mid = (left + right) // 2
    temp = 0

    for jewel in jewels:
        temp += math.ceil(jewel/mid)

    if temp > N:
        left = mid + 1
    else:
        right = mid - 1
        answer = min(answer, mid)

print(answer)