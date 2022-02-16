import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1

if n == 0:
    print(0)
elif n == 1 and n == 2:
    print(1)
else:
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[n])