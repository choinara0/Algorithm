import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
dp = [0] * (k+1)
dp[0] = 1

for c in coin:
    for i in range(1, k+1):
        if i-c >= 0:
            dp[i] += dp[i-c]
print(dp[k])