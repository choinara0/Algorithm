import sys

T = int(sys.stdin.readline())
dp = [[0]*30 for i in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(dp[N][M])