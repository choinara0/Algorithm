import sys
sys.setrecursionlimit(10000)

M, N = map(int, sys.stdin.readline().split())
matrix = []
for i in range(M):
    matrix.append(list(map(int, sys.stdin.readline().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < M and 0 <= ny < N ) and matrix[x][y] < matrix[nx][ny]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

dp = [[-1]*N for i in range(M)]
print(dfs(M-1, N-1))