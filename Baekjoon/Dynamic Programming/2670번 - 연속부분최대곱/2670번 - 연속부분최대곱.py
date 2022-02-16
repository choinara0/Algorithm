import sys

N = int(sys.stdin.readline())
dp = []
for i in range(N):
    dp.append(float(sys.stdin.readline()))

for i in range(1, N):
    dp[i] = max(dp[i], dp[i-1] * dp[i])

print('{:.3f}'.format(max(dp)))