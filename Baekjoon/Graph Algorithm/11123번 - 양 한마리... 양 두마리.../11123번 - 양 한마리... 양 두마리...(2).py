# dfs
import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx ,ny = x + dx[i], y + dy[i]
        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and board[nx][ny] == '#':
            dfs(nx, ny)

for t in range(T):
    H, W = map(int, sys.stdin.readline().split())
    board = [list(map(str, sys.stdin.readline().strip())) for i in range(H)]
    visited = [[0]*W for i in range(H)]
    cnt = 0

    for i in range(H):
        for j in range(W):
            if board[i][j] == '#' and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)