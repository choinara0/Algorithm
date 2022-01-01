import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
dp1 = [1] * N
dp2 = [1] * N

for i in range(1, N):
    if numList[i] >= numList[i-1]:
        dp1[i] = max(dp1[i], dp1[i-1] + 1)
    if numList[i] <= numList[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1] + 1)

print(max(max(dp1), max(dp2)))