import sys

N, M = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
start, end = 0, 1
result = 0

while start <= N and end <= N:
    temp = sum(numList[start:end])

    if temp == M:
        result += 1

    if temp <= M:
        end += 1
        continue
    elif temp > M and start < end:
        start += 1
        continue
    else:
        start += 1
        end += 1


print(result)
