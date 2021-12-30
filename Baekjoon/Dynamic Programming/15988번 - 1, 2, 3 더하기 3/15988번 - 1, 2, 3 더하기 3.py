import sys

dp = [0 for i in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, len(dp)):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])