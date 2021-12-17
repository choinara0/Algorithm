import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
dp = [[0]*n for i in range(n)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[x][y] < board[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)