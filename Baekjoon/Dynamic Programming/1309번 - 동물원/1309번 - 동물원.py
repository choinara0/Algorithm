import sys
N = int(sys.stdin.readline())
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 3
for i in range(2, len(dp)):
    dp[i] = (dp[i-2] + (dp[i-1] * 2)) % 9901
print(dp[N])