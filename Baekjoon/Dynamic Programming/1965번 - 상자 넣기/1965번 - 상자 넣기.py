import sys

n = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))