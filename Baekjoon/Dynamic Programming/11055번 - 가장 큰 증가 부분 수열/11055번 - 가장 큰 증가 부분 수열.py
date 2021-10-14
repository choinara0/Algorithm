import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dp = [1] * N
dp[0] = num[0]

for i in range(1, N):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + num[i])
        else:
            dp[i] = max(dp[i], num[i])
print(max(dp))
