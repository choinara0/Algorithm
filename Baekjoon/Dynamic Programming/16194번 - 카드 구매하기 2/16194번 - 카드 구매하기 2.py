import sys

N = int(sys.stdin.readline())
card = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (N+1)
dp[1] = card[1]
dp[2] = min(card[2], card[1]*2)

for i in range(3, N+1):
    dp[i] = card[i]
    for j in range(1, i//2 + 1):
        dp[i] = min(dp[i], dp[j] + dp[i-j])

print(dp[N])