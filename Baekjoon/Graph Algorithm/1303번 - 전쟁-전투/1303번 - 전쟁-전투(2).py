import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for i in range(M)]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
visited = [[0]*N for i in range(M)]
w_power, b_power = 0, 0

def dfs(x, y, cnt):
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and board[nx][ny] == board[x][y]:
            visited[nx][ny] = 1
            cnt = dfs(nx, ny, cnt+1)

    return cnt


for i in range(M):
    for j in range(N):
        if not visited[i][j] and board[i][j] == 'W':
            w_power += dfs(i,j,1) ** 2
        elif not visited[i][j] and board[i][j] == 'B':
            b_power += dfs(i,j,1) ** 2

print(w_power, b_power)