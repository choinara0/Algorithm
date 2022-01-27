import sys

N = int(sys.stdin.readline())
life_point = [0] + list(map(int, sys.stdin.readline().split()))
happy_point = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0]*101 for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 101):
        if life_point[i] <= j :
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - life_point[i]] + happy_point[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][99])