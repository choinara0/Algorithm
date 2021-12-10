import sys

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        dp[x][y] = max(dp[x-1][y], dp[x][y-1])
        dp[x][y] += maze[x][y]

print(dp[N-1][M-1])