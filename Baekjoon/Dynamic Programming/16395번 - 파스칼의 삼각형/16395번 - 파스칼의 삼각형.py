import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[1] * i for i in range(31)]

for i in range(3, 31):
    for j in range(1, i-1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k-1])