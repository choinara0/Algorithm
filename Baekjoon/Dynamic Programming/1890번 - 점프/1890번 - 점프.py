import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == N-1 and y == N-1:
            break
        temp = board[x][y]
        nx, ny = x + temp, y + temp
        if nx < N:
            dp[nx][y] += dp[x][y]
        if ny < N:
            dp[x][ny] += dp[x][y]
print(dp[N-1][N-1])