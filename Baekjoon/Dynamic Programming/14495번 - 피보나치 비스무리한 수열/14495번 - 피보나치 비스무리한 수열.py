import sys

n = int(sys.stdin.readline())
dp = [1] * (n+1)
if n == 1 or n == 2 or n == 3:
    print(1)
else:
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3]
    print(dp[n])