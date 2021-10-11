import sys

N = int(sys.stdin.readline())
dp = list([[1] * 10])

for _ in range(N):
    dp.append(list([0] * 10))

for i in range(1, N+1):
    for j in range(0, 10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(dp[N][9]%10007)



