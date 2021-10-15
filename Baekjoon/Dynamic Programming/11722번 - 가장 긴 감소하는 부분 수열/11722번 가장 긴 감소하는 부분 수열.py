import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if num[j] > num[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))